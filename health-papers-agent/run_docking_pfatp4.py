"""HP-022 corrected run: Plasmodium falciparum PfATP4 / cipargamin,
docking SKIPPED.

Why this driver exists (2026-11-11): the standard run_docking.py path is
WRONG for this target, and the failure was verified live:

1. The pipeline's ChEMBL target lookup for UniProt A0A143ZZK9 (PfATP4,
   1264 aa) returns a list of unrelated human targets and takes the
   first: CHEMBL2074, "Maltase-glucoamylase", Homo sapiens (UniProt
   O43451). Step 2 therefore queried maltase-glucoamylase bioactivities
   and found 0 (correctly — for the wrong enzyme). A paper built on
   that would be a maltase-glucoamylase paper mislabelled as PfATP4.
   Direct ChEMBL API check confirmed CHEMBL2074 = human
   maltase-glucoamylase.
2. The true PfATP4 ChEMBL target was found by direct API lookup:
   target_component accession A0A143ZZK9 -> component 23361 ->
   CHEMBL6066156, "P-type sodium-transporting ATPase4", SINGLE PROTEIN,
   Plasmodium falciparum (isolate 3D7). It carries 26 bioactivities
   across 7 compounds (verified live 2026-11-11).

Correction (minimal, documented): monkeypatch only the
chembl_target_by_uniprot lookup so step 2 uses CHEMBL6066156.
Everything else -- UniProt lookup, PubChem verification of cipargamin,
RDKit similarity/ADMET/PAINS, ToxGuard, lead ranking -- is the
unmodified LeadForge pipeline (run_pipeline, dock_top_n=0).

Docking is SKIPPED, honestly, per the pipeline's own rule: the
pipeline's structure picker is X-ray-only, and no X-ray structure of
PfATP4 exists. The first experimental PfATP4 structure was published
20 Oct 2025 (Haile et al., Nat Commun 16:9092, PMID 41115914): a 3.7 A
cryo-EM structure, PDB 9N10, of the APO pump in complex with the
newly discovered modulator PfABP -- no co-crystallised ligand, no
ligand-derived grid centre, and a 3.7 A cryo-EM map is outside the
pipeline's X-ray-only picker by design. Hand-rolling a grid centre on
9N10 (e.g. from the Na+ site or a homology-model pocket) would repeat
the 2026-11-11 TYK2 centre-pick error. Docking cipargamin on 9N10
would produce numbers that look like results and are not. The paper is
therefore a ChEMBL potency analysis of PfATP4 actives against
cipargamin, and says so in its title.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import sources as S  # noqa: E402
from app.discovery.pipeline import run_pipeline  # noqa: E402


def _chembl_target_by_uniprot_corrected(accession):
    """Return the true PfATP4 ChEMBL target, not maltase-glucoamylase."""
    return {"ok": True, "data": [{
        "chembl_id": "CHEMBL6066156",
        "name": "P-type sodium-transporting ATPase4",
        "type": "SINGLE PROTEIN",
        "organism": "Plasmodium falciparum (isolate 3D7)",
        "components": 1,
    }]}


def main():
    S.chembl_target_by_uniprot = _chembl_target_by_uniprot_corrected
    res = run_pipeline("Plasmodium falciparum PfATP4",
                       query_name="cipargamin",
                       top_n=25, dock_top_n=0)
    print("PIPELINE OK:", res.get("ok"), flush=True)
    for s in res.get("steps", []):
        print("STEP:", s, flush=True)
    tgt = res.get("target") or {}
    print("UNIPROT:", (tgt.get("uniprot") or {}).get("accession"),
          (tgt.get("uniprot") or {}).get("protein"), flush=True)
    print("CHEMBL TARGET (corrected):",
          (tgt.get("chembl_target") or {}).get("chembl_id"),
          (tgt.get("chembl_target") or {}).get("name"), flush=True)
    print("LEADS:", len(res.get("leads") or []), flush=True)
    for ld in res.get("leads") or []:
        print("  LEAD:", ld.get("rank"), ld.get("label"),
              "sim", ld.get("similarity"), "score", ld.get("score"),
              "pains", ld.get("pains"),
              "known", (ld.get("known_activity") or {}).get("pchembl_value")
              if ld.get("known_activity") else None, flush=True)
    res["docking"] = {
        "ok": False,
        "skipped": True,
        "reason": ("No X-ray structure of PfATP4 exists; the pipeline's "
                   "structure picker is X-ray-only by design. The only "
                   "experimental structure is the 3.7 A cryo-EM apo "
                   "structure PDB 9N10 (Haile et al., Nat Commun 2025, "
                   "PMID 41115914), with no co-crystallised ligand and no "
                   "ligand-derived grid centre; rigid Vina docking on it "
                   "would be a hand-rolled centre pick (cf. TYK2 lesson "
                   "2026-11-11). Pipeline default picked CHEMBL2074 "
                   "(human maltase-glucoamylase) as the ChEMBL target; "
                   "that run's step-2 zero is discarded and the true "
                   "target CHEMBL6066156 was used instead."),
        "pdb_id": None,
    }
    res["topic"] = {"target": "Plasmodium falciparum PfATP4",
                    "reference": "cipargamin"}
    res["corrections"] = ("ChEMBL target corrected: pipeline default "
                          "CHEMBL2074 (human maltase-glucoamylase) -> "
                          "CHEMBL6066156 (P-type sodium-transporting "
                          "ATPase4, P. falciparum 3D7); docking skipped "
                          "(see docking.reason); first run_docking.py "
                          "attempt's step-2 zero is discarded, its "
                          "UniProt/PubChem steps were correct.")
    out = "../hidden_files/dock-HP-022-2026-11-11.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(res, f, indent=1)
    print("RAW_SAVED:", out, flush=True)
    return 0 if res.get("ok") else 1


if __name__ == "__main__":
    sys.exit(main())
