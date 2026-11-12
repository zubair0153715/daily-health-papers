"""Corrected HP-034 (CDK6 / palbociclib) run, 2026-11-12.

FAULT in the first run (dock-HP-034-2026-11-12.json): the pipeline's
UniProt text search for "Cyclin-dependent kinase 6" returned P24941 —
which is CDK2, not CDK6 (verified live against rest.uniprot.org:
P24941 = Cyclin-dependent kinase 2; Q00534 = Cyclin-dependent kinase
6). The ChEMBL lookup then correctly returned CDK2's target
CHEMBL301, and the docking ran on 6Q4G, a CDK2 structure. The whole
first run is a CDK2 run mislabelled as CDK6; its numbers are kept in
the original JSON for audit and discarded.

CORRECTION (minimal, documented):
- Target query is the UniProt accession "Q00534", which the
  pipeline's own uniprot_target resolves to CDK6 (verified in-process
  before this run: accession Q00534, gene CDK6, 326 aa).
- chembl_target_by_uniprot is monkey-patched to return CHEMBL2508,
  "Cyclin-dependent kinase 6", verified live on the ChEMBL website
  (target report card CHEMBL2508, 2026-11-12). The ChEMBL
  target-by-accession API endpoint is returning HTTP 500 / timeouts
  today, so the patch bypasses it; the bioactivities call for
  CHEMBL2508 is the unmodified pipeline.
Everything else — PubChem verification of palbociclib, RDKit
similarity/ADMET/PAINS, ToxGuard, lead ranking, Vina docking via
dock_leads — is the unmodified LeadForge pipeline / run_docking.py
flow.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import sources as S  # noqa: E402
from app.discovery.pipeline import run_pipeline  # noqa: E402
from app.discovery import dock as D  # noqa: E402


def _chembl_target_by_uniprot_corrected(accession):
    """Return the true CDK6 ChEMBL target, not CDK2's CHEMBL301."""
    return {"ok": True, "data": [{
        "chembl_id": "CHEMBL2508",
        "name": "Cyclin-dependent kinase 6",
        "type": "SINGLE PROTEIN",
        "organism": "Homo sapiens",
        "components": 1,
    }]}


def _chembl_bioactivities_file_backed(target_chembl_id, limit=60):
    """Bioactivities from the verbatim ChEMBL API response saved to
    disk (same endpoint + query the pipeline uses), because the
    live activity endpoint is flapping today: limit=50 queries time
    out (>60 s) and limit=10 queries intermittently return the HTML
    500 page. The saved file is the top-25-by-pChEMBL page of the
    response for this target (page_meta total_count 1038) fetched
    2026-11-12 via curl with the NO_PROXY variant from:
    https://www.ebi.ac.uk/chembl/api/data/activity.json
      ?target_chembl_id=CHEMBL2508&pchembl_value__gte=5
      &limit=25&order_by=-pchembl_value
    Record shape and SMILES dedup are identical to
    sources.chembl_bioactivities; only the transport differs.
    """
    import os
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "../hidden_files/chembl-activities-CHEMBL2508-2026-11-12.json")
    with open(path) as f:
        d = json.load(f)
    out, seen = [], set()
    for a in (d.get("activities") or []):
        smi = a.get("canonical_smiles")
        if not smi or smi in seen:
            continue
        seen.add(smi)
        out.append({
            "molecule_chembl_id": a.get("molecule_chembl_id"),
            "smiles": smi,
            "pchembl": a.get("pchembl_value"),
            "activity_type": a.get("standard_type"),
            "value": a.get("standard_value"),
            "units": a.get("standard_units"),
            "assay_chembl_id": a.get("assay_chembl_id"),
        })
        if len(out) >= limit:
            break
    return {"ok": True, "data": out}


def main():
    S.chembl_target_by_uniprot = _chembl_target_by_uniprot_corrected
    S.chembl_bioactivities = _chembl_bioactivities_file_backed
    res = run_pipeline("Q00534", query_name="palbociclib",
                       top_n=25, dock_top_n=0)
    print("PIPELINE OK:", res.get("ok"), flush=True)
    for s in res.get("steps", []):
        print("STEP:", s, flush=True)
    tgt = res.get("target") or {}
    uni = tgt.get("uniprot") or {}
    print("UNIPROT:", uni.get("accession"), uni.get("name"),
          uni.get("organism"), flush=True)
    print("CHEMBL TARGET (corrected):",
          (tgt.get("chembl_target") or {}).get("chembl_id"),
          (tgt.get("chembl_target") or {}).get("name"), flush=True)
    leads = res.get("leads") or []
    print("LEADS:", len(leads), flush=True)

    docking = None
    acc = uni.get("accession")
    if leads and acc:
        docking = D.dock_leads(leads, acc, top_n=5)
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
        print("DOCKING SKIPPED: no leads or no UniProt accession.",
              flush=True)

    res["docking"] = docking
    res["topic"] = {"target": "Cyclin-dependent kinase 6 (CDK6)",
                    "reference": "palbociclib"}
    res["correction"] = (
        "First run resolved 'Cyclin-dependent kinase 6' to UniProt "
        "P24941 (CDK2) and ChEMBL CHEMBL301 (CDK2) and docked on 6Q4G; "
        "that run's numbers are discarded (kept in "
        "dock-HP-034-2026-11-12.json for audit). Corrected run: target "
        "by UniProt accession Q00534 (CDK6) and ChEMBL target CHEMBL2508 "
        "(Cyclin-dependent kinase 6, verified on the ChEMBL website). "
        "Bioactivities are the verbatim ChEMBL API response saved to "
        "hidden_files/chembl-activities-CHEMBL2508-2026-11-12.json "
        "(top 25 by pChEMBL of 1,038) because the live activity "
        "endpoint timed out / returned HTTP 500 pages throughout "
        "2026-11-12.")
    out = "../hidden_files/dock-HP-034c-2026-11-12.json"
    with open(out, "w") as f:
        json.dump(res, f, indent=1)
    print("RAW_SAVED:", out, flush=True)
    return 0 if res.get("ok") else 1


if __name__ == "__main__":
    sys.exit(main())
