"""HP-039 corrected run: HIV-1 integrase / dolutegravir, docking SKIPPED.

Why this driver exists (2026-11-10): the standard run_docking.py path is
WRONG for this target, twice over, and both failures were verified live:

1. UniProt text search for "HIV-1 integrase" returns the Gag-Pol
   polyprotein P04585 (integrase is a cleavage product; UniProtKB has no
   standalone HIV-1 integrase entry for HXB2). The pipeline's PDB picker
   then takes P04585's PDB cross-references sorted by resolution and picks
   the best ligand-bound X-ray structure -- 6DV4, an HIV-1 PROTEASE
   structure at 1.14 A. The first run_docking.py attempt was killed
   mid-Vina once this was found; no result from it is used.
2. The same polyprotein mapping gives ChEMBL target CHEMBL3638360
   ("Gag-Pol polyprotein"), whose top bioactivities are HIV-1 PROTEASE
   assays (CHEMBL3887078) and whole-virus T-cell assays (CHEMBL3887045)
   -- not integrase assays. A paper built on those would be a protease
   paper mislabelled as integrase.

Correction (minimal, documented): monkeypatch only the
chembl_target_by_uniprot lookup so step 2 uses the true HIV-1 integrase
ChEMBL target CHEMBL3471 ("Human immunodeficiency virus type 1
integrase", SINGLE PROTEIN). Everything else -- UniProt lookup, PubChem
verification, RDKit similarity/ADMET/PAINS, ToxGuard, lead ranking --
is the unmodified LeadForge pipeline (run_pipeline, dock_top_n=0).

Docking is SKIPPED, honestly, per the pipeline's own rule: there is no
X-ray structure of HIV-1 integrase with a strand-transfer inhibitor at
the strand-transfer site. The dolutegravir-bound structures are cryo-EM
intasomes (e.g. 8FNG, G140A intasome + dolutegravir, Sci Adv 2023,
PMID 37478179) whose active site is a protein-DNA-Mg2+ interface that
rigid Vina docking cannot treat faithfully (no metal coordination, DNA
interface, megadalton complex); the X-ray integrase structures with
inhibitors are allosteric-site (LEDGIN) complexes such as 8CBT, a
different pocket. Docking dolutegravir on 6DV4 (protease) or 8CBT
(allosteric site) would produce numbers that look like results and are
not. The paper is therefore a ChEMBL potency + resistance-landscape
analysis, and says so.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import sources as S  # noqa: E402
from app.discovery.pipeline import run_pipeline  # noqa: E402


def _chembl_target_by_uniprot_corrected(accession):
    """Return the true HIV-1 integrase ChEMBL target, not the polyprotein."""
    return {"ok": True, "data": [{
        "chembl_id": "CHEMBL3471",
        "name": "Human immunodeficiency virus type 1 integrase",
        "type": "SINGLE PROTEIN",
        "organism": "Human immunodeficiency virus 1",
        "components": 1,
    }]}


def main():
    S.chembl_target_by_uniprot = _chembl_target_by_uniprot_corrected
    res = run_pipeline("HIV-1 integrase", query_name="dolutegravir",
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
    res["docking"] = {
        "ok": False,
        "skipped": True,
        "reason": ("No X-ray structure of HIV-1 integrase with a "
                   "strand-transfer inhibitor exists; dolutegravir-bound "
                   "structures are cryo-EM intasomes (e.g. 8FNG) whose "
                   "protein-DNA-Mg2+ active site rigid Vina cannot treat "
                   "faithfully. Pipeline default picked HIV-1 protease "
                   "6DV4 via the Gag-Pol polyprotein P04585; that run was "
                   "killed and discarded. ChEMBL polyprotein target "
                   "CHEMBL3638360 likewise returns protease assays, so the "
                   "true integrase target CHEMBL3471 was used instead."),
        "pdb_id": None,
    }
    res["topic"] = {"target": "HIV-1 integrase",
                    "reference": "dolutegravir"}
    res["corrections"] = ("Chembl target corrected P04585 polyprotein "
                          "CHEMBL3638360 -> CHEMBL3471 HIV-1 integrase; "
                          "docking skipped (see docking.reason); first "
                          "run_docking.py attempt killed mid-Vina on "
                          "protease structure 6DV4, no output saved.")
    out = "../hidden_files/dock-HP-039-2026-11-10.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(res, f, indent=1)
    print("RAW_SAVED:", out, flush=True)
    return 0 if res.get("ok") else 1


if __name__ == "__main__":
    sys.exit(main())
