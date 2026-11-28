"""DGAT1 docking for HP-106 (2026-11-28) — QUERY + top 4 leads on 8ESM.

Why a custom script: the pipeline run found the correct target
(CHEMBL6009, human DGAT1, 41 bioactivities, 26 leads) but reported
"no_pdb_found" — its PDB search missed the two human DGAT1 cryo-EM
structures. 8ESM is human DGAT1 in complex with the T863 inhibitor
(cryo-EM, 3.2 A; Sui et al., Nat Commun 2023, PMID 37248213), the same
inhibitor class as pradigastat. Centre audit: dock._ligand_center on
8ESM picks the T863 ligand centroid. Same box (22.5 A) and
exhaustiveness (8) as Papers #1/#3. Compounds (SMILES read from the
pipeline JSON).
Note: the first pipeline attempt used the wrong UniProt accession
(Q8W0K6, which does not exist — UniProt returns an empty record) and
fell back to the wrong ChEMBL target (CHEMBL2074, maltase-glucoamylase);
the rerun with the correct accession O75907 produced the leads used here.
The wrong-target run is preserved in the overwritten JSON's history only
as this note — the file dock-HP-106-2026-11-28.json now holds the
corrected O75907 run.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402

BASE = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts"
PIPE = f"{BASE}/hidden_files/dock-HP-106-2026-11-28.json"
OUT = f"{BASE}/hidden_files/dock-HP-106-2026-11-28-8ESM.json"


def main():
    pdb_path = D._pdb_path("8ESM")
    center = D._ligand_center(pdb_path)
    print("CENTER 8ESM:", center, flush=True)
    if not center:
        print("ERROR: no ligand centre in 8ESM", flush=True)
        return 1
    pipe = json.load(open(PIPE))
    leads = {l.get("label"): l for l in pipe["leads"]}
    wanted = ["QUERY", "CHEMBL3037924", "CHEMBL2036730", "CHEMBL4453443",
              "CHEMBL5864682"]
    results = []
    for label in wanted:
        l = leads[label]
        r = D.dock(l["smiles"], "8ESM", center, box_size=22.5)
        r["label"] = label
        r["rank"] = l.get("rank")
        results.append(r)
        print("DOCK 8ESM:", label, r.get("affinity_kcal_mol"), r.get("ok"),
              flush=True)
    results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
    out = {
        "topic": {"target": "DGAT1", "reference": "pradigastat",
                  "topic_id": "HP-106", "date": "2026-11-28"},
        "docking": {
            "ok": True, "pdb_id": "8ESM", "resolution": 3.2,
            "center": [round(c, 2) for c in center],
            "center_note": ("T863 inhibitor centroid via "
                            "dock._ligand_center — human DGAT1 + T863, "
                            "cryo-EM 3.2 A (Sui et al., Nat Commun 2023)"),
            "box_size": 22.5, "exhaustiveness": 8,
            "correction_note": ("Pipeline reported no_pdb_found for "
                                "DGAT1; two human DGAT1 cryo-EM structures "
                                "exist (8ESM, 8ETM) and were missed by its "
                                "PDB search. Docked on 8ESM, the "
                                "inhibitor-bound template."),
            "results": results,
        },
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("SAVED:", OUT, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
