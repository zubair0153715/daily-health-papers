"""Mpro docking for HP-037 (2026-11-14) — SARS-CoV-2 main protease.

Why this run exists: run_docking.py's first attempt resolved the
target to the wrong ChEMBL target (CHEMBL2074 maltase-glucoamylase)
because the ChEMBL text search returns an unfiltered junk list, and
it docked into 8AZC — the NSP3 macrodomain, not Mpro — with every
dock failing ("pdb parse failed"). The correct target is
CHEMBL4523582 (Replicase polyprotein 1ab), reached by querying the
pipeline with the UniProt accession P0DTD1. The correct structure is
7SI9 (2.0 A), Mpro in complex with nirmatrelvir (ligand 4WI, the
covalent thioimidate adduct with Cys145). This script docks five
unique compounds on 7SI9 centred on the chain-A 4WI centroid
[-10.40, 39.82, -17.96], box 22.5 A: nirmatrelvir (QUERY, re-dock
control) + four analogues from Ghosh et al. 2024. Note:
CHEMBL4802135 IS nirmatrelvir (verified pref_name) — it duplicates
the QUERY and is excluded from the docking set. Limitation, stated
in the paper: rigid docking cannot model the covalent bond to
Cys145 (nirmatrelvir is a covalent inhibitor; Vina scores only the
non-covalent pose), the receptor prep drops HETATM, and the measured
Ki values come from different assays (nirmatrelvir consensus Ki is
3.1 nM across 10 ChEMBL records; the pipeline's top record gave
0.26 nM and is treated as an outlier).
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402

BASE = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts"
MAIN = f"{BASE}/hidden_files/dock-HP-037-2026-11-14.json"
OUT = f"{BASE}/hidden_files/dock-HP-037-2026-11-14-7SI9.json"

# Chain-A nirmatrelvir adduct (4WI) centroid, from 7SI9 HETATM records.
CENTER = [-10.40, 39.82, -17.96]

# Pipeline ranks to dock: 1 (QUERY), 3, 4, 5, 6. Rank 2 (CHEMBL4802135)
# is nirmatrelvir itself — excluded as a duplicate of the QUERY.
WANTED = {"QUERY", "CHEMBL5574604", "CHEMBL5589941", "CHEMBL5178656",
          "CHEMBL5590149"}


def main():
    with open(MAIN, encoding="utf-8") as f:
        main_json = json.load(f)
    leads = [l for l in (main_json.get("leads") or [])
             if l.get("label") in WANTED]

    results = []
    for l in leads:
        r = D.dock(l["smiles"], "7SI9", CENTER, box_size=22.5)
        r["label"] = l.get("label")
        r["rank"] = l.get("rank")
        r["measured_potency"] = (l.get("known_activity") or {}).get("activity")
        r["pains"] = l.get("pains")
        results.append(r)
        print("DOCK 7SI9:", r["label"], r.get("affinity_kcal_mol"),
              r.get("ok"), flush=True)
    results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
    out = {
        "topic": {"target": "SARS-CoV-2 main protease Mpro (nsp5)",
                  "reference": "nirmatrelvir",
                  "topic_id": "HP-037", "date": "2026-11-14"},
        "docking": {
            "ok": True, "pdb_id": "7SI9", "resolution": 2.0,
            "center": CENTER,
            "center_note": ("co-crystallised nirmatrelvir adduct (4WI) "
                            "centroid, chain A — the active site, Cys145"),
            "box_size": 22.5, "exhaustiveness": 8,
            "correction_note": ("First run used the wrong ChEMBL target "
                                "(CHEMBL2074 maltase-glucoamylase) and the "
                                "wrong structure (8AZC, NSP3 macrodomain); "
                                "all docks failed. Correct target is "
                                "CHEMBL4523582 via UniProt P0DTD1; correct "
                                "structure is 7SI9 (nirmatrelvir-bound). "
                                "CHEMBL4802135 is nirmatrelvir itself — "
                                "excluded as a duplicate of the QUERY. "
                                "Rigid docking cannot model the covalent "
                                "Cys145 bond."),
            "results": results,
        },
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("SAVED:", OUT, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
