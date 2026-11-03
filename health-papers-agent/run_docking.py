"""Run the LeadForge docking protocol for one health-paper topic.

Usage (with the RDKit venv):
  NO_PROXY=localhost,127.0.0.1,::1 ~/workspace/.venv-fc/bin/python run_docking.py \
      --target "Plasmodium falciparum PfATP4" --ref cipargamin \
      --out hidden_files/dock-HP-022-2026-11-04.json

What it does (same validated flow as ~/workspace/leadforge-daily/run_*.py):
  1. run_pipeline(target, query_name=ref, top_n=25, dock_top_n=0)
     (UniProtKB -> ChEMBL -> PubChem -> RDKit -> ADMET/PAINS -> ranking)
  2. Dock the top 5 leads + the reference query itself via D.dock_leads
     (PDB auto-pick; if no experimental structure exists the result says
     so honestly and docking is SKIPPED — never fake a structure).
  3. Saves the raw JSON to --out and prints a one-line summary.

Network notes: LeadForge API calls go through the stock proxy and flap
with RemoteDisconnected; retry once with NO prefix override if a step
fails (see ~/AGENTS.md FastAPI/medexplain lessons — both variants flap,
retry with the other one). Vina binary is cached at
clinic-demo/app/discovery/data/pdb_cache/vina (downloads itself on first
use). One ligand docking takes ~30s-3min; budget ~15-30 min per topic.
"""
import argparse
import json
import os
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery.pipeline import run_pipeline  # noqa: E402
from app.discovery import dock as D  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", required=True)
    ap.add_argument("--ref", required=True,
                    help="reference drug / query compound name")
    ap.add_argument("--top-n", type=int, default=25)
    ap.add_argument("--dock-top-n", type=int, default=5)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    res = run_pipeline(args.target, query_name=args.ref,
                       top_n=args.top_n, dock_top_n=0)
    print("PIPELINE OK:", res.get("ok"), flush=True)
    for s in res.get("steps", []):
        print("STEP:", s, flush=True)
    tgt = res.get("target") or {}
    uni = tgt.get("uniprot") or {}
    print("UNIPROT:", uni.get("accession"), uni.get("name"),
          uni.get("organism"), flush=True)
    leads = res.get("leads") or []
    print("LEADS:", len(leads), flush=True)

    docking = None
    acc = uni.get("accession")
    if leads and acc:
        docking = D.dock_leads(leads, acc, top_n=args.dock_top_n)
        print("DOCK_LEADS:", docking.get("ok"), docking.get("pdb_id"),
              docking.get("error"), flush=True)
        for r in docking.get("results", []):
            print("  DOCK:", r.get("label"), r.get("affinity_kcal_mol"),
                  r.get("ok"), flush=True)
        q = next((l for l in leads if l.get("label") == "QUERY"), None)
        docked = {r.get("label") for r in docking.get("results", [])}
        if docking.get("ok") and q and "QUERY" not in docked:
            r = D.dock(q["smiles"], docking["pdb_id"],
                       docking["center"], box_size=22.5)
            r["label"] = "QUERY"
            r["rank"] = q.get("rank")
            docking["results"].append(r)
            docking["results"].sort(
                key=lambda x: x.get("affinity_kcal_mol", 999))
            print("  DOCK-QUERY:", r.get("label"),
                  r.get("affinity_kcal_mol"), flush=True)
    else:
        print("DOCKING SKIPPED: no leads or no UniProt accession — "
              "paper must say so honestly.", flush=True)

    res["docking"] = docking
    res["topic"] = {"target": args.target, "reference": args.ref}
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(res, f, indent=1)
    print("RAW_SAVED:", args.out, flush=True)
    return 0 if res.get("ok") else 1


if __name__ == "__main__":
    sys.exit(main())
