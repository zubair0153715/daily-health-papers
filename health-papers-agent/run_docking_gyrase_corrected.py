"""Corrected HP-051 (S. Typhi DNA gyrase / azithromycin) run, 2026-11-12.

FAULT in the first run (dock-HP-051-2026-11-12.json): UniProt
P0A2I4 (S. Typhi DNA gyrase subunit B, gyrB, 804 aa) was correct,
but the ChEMBL target resolved to CHEMBL2074 maltase-glucoamylase
— the by-accession endpoint returned nothing/failed, and the
fallback picked the first entry of the garbage q= text-search list.
The first run's leads are N-substituted deoxynojirimycin
iminosugars (alpha-glucosidase inhibitors), not antibacterials;
its docking scores are meaningless for this topic and are
discarded (kept in dock-HP-051-2026-11-12.json for audit).
The structure picker was NOT wrong: PDB 6J90 (S. Typhi GyrB
N-terminal domain + ATP, 2.2 A) is the correct drug site, centre
= ATP centroid exactly.

BROWSER FINDING (2026-11-12, ChEMBL website search, verified
twice): NO ChEMBL target for "Salmonella Typhi DNA gyrase"
(subunit A or B) exists. The only S. Typhi targets are ORGANISM
targets. Closest verified target, confirmed on its own report
card: CHEMBL614448 "Salmonella typhi", type ORGANISM, organism
"Salmonella enterica subsp. enterica serovar Typhi", 3,065
associated compounds, 4,418 bioactivities, 387 assays.

CORRECTION (minimal, documented):
- Target query is the UniProt accession "P0A2I4" (gyrB), which the
  pipeline's own uniprot_target resolves directly.
- chembl_target_by_uniprot is monkey-patched to return
  CHEMBL614448, "Salmonella typhi" (ORGANISM). The ChEMBL
  target-by-accession API endpoint is returning HTTP 500 /
  timeouts today, so the patch bypasses it; the bioactivities
  call for CHEMBL614448 is the unmodified pipeline.
- HONEST FRAMING (must appear in the paper): CHEMBL614448
  bioactivities are PHENOTYPIC whole-cell data (MICs against
  S. Typhi), NOT gyrase binding data. The docking-vs-potency
  comparison is therefore a hypothesis test — does whole-cell
  anti-Typhi potency track with GyrB ATP-site binding? — not a
  target-validated benchmark. No claim that a lead "inhibits
  gyrase" can be made from this screen.
Everything else — PubChem verification of azithromycin, RDKit
similarity/ADMET/PAINS, ToxGuard, lead ranking, Vina docking via
dock_leads — is the unmodified LeadForge pipeline / run_docking.py
flow. The first run's azithromycin QUERY dock failed with a Vina
command error; this driver retries the QUERY dock explicitly and
logs a failure honestly if it fails again (macrolide, MW 749).
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import sources as S  # noqa: E402
from app.discovery.pipeline import run_pipeline  # noqa: E402
from app.discovery import dock as D  # noqa: E402


def _chembl_target_by_uniprot_corrected(accession):
    """Return the verified S. Typhi organism target.

    No S. Typhi DNA gyrase protein target exists in ChEMBL
    (website search verified 2026-11-12). CHEMBL614448 is the
    organism target; its bioactivities are phenotypic.
    """
    return {"ok": True, "data": [{
        "chembl_id": "CHEMBL614448",
        "name": "Salmonella typhi",
        "type": "ORGANISM",
        "organism": "Salmonella enterica subsp. enterica serovar Typhi",
        "components": 0,
    }]}


def _chembl_bioactivities_file_backed(target_chembl_id, limit=60):
    """Bioactivities from the verbatim ChEMBL API response saved to
    disk (same endpoint + query the pipeline uses), because the
    live activity endpoint is flapping today: limit=50 queries time
    out (>60 s) and limit=10 queries intermittently return the HTML
    500 page. The saved file is the complete response for this
    target (page_meta total_count 5, next None) fetched 2026-11-12
    via curl from:
    https://www.ebi.ac.uk/chembl/api/data/activity.json
      ?target_chembl_id=CHEMBL614448&pchembl_value__gte=5
      &limit=10&order_by=-pchembl_value
    Record shape and SMILES dedup are identical to
    sources.chembl_bioactivities; only the transport differs.
    """
    import os
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "../hidden_files/chembl-activities-CHEMBL614448-2026-11-12.json")
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
    res = run_pipeline("P0A2I4", query_name="azithromycin",
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
                  r.get("affinity_kcal_mol"), r.get("ok"),
                  r.get("error"), flush=True)
    else:
        print("DOCKING SKIPPED: no leads or no UniProt accession.",
              flush=True)

    res["docking"] = docking
    res["topic"] = {"target": "Salmonella Typhi DNA gyrase subunit B (gyrB)",
                    "reference": "azithromycin"}
    res["correction"] = (
        "First run resolved ChEMBL to CHEMBL2074 maltase-glucoamylase "
        "and docked iminosugars; that run's numbers are discarded "
        "(kept in dock-HP-051-2026-11-12.json for audit). Corrected "
        "run: target by UniProt accession P0A2I4 (gyrB) and ChEMBL "
        "target CHEMBL614448 'Salmonella typhi' (ORGANISM, verified "
        "on the ChEMBL website 2026-11-12) — no S. Typhi DNA gyrase "
        "protein target exists in ChEMBL, so the bioactivities are "
        "phenotypic whole-cell data, not gyrase binding data. "
        "Bioactivities are the verbatim ChEMBL API response saved to "
        "hidden_files/chembl-activities-CHEMBL614448-2026-11-12.json "
        "(complete set: 5 activities with pChEMBL >= 5) because the "
        "live activity endpoint timed out / returned HTTP 500 pages "
        "throughout 2026-11-12.")
    out = "../hidden_files/dock-HP-051c-2026-11-12.json"
    with open(out, "w") as f:
        json.dump(res, f, indent=1)
    print("RAW_SAVED:", out, flush=True)
    return 0 if res.get("ok") else 1


if __name__ == "__main__":
    sys.exit(main())
