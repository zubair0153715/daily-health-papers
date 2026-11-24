"""GCGR correction dock for HP-107 (2026-11-24) — LY2409021 + comparators on 5EE7.

Why this run exists: the pipeline docked only the QUERY (LY2409021, -8.20)
because ChEMBL ligand retrieval returned no_data (chembl_targets empty).
5EE7 IS the correct template — verified: "Crystal structure of the human
glucagon receptor (GCGR) in complex with the antagonist MK-0893", 2.5 A,
and the centre audit confirmed the pipeline centre [-30.40, 1.77, -36.73]
is exactly the MK-0893 (5MV) centroid. This script re-docks LY2409021 plus
MK-0893 (the co-crystallised ligand = self-dock control), PF-06291874 and
LGD-6972, all GCGR antagonists, on the same centre/box/exhaustiveness.
SMILES verified via PubChem (formulas: MK-0893 C32H27Cl2N3O4,
PF-06291874 C26H28F3N3O4, LGD-6972 C43H46N2O5S).
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402
from rdkit import Chem  # noqa: E402
from rdkit.Chem import Descriptors, Lipinski, rdMolDescriptors  # noqa: E402
from rdkit.Chem.FilterCatalog import FilterCatalog, FilterCatalogParams  # noqa: E402

BASE = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts"
OUT = f"{BASE}/hidden_files/dock-HP-107-2026-11-24-5EE7.json"
CENTER = [-30.40, 1.77, -36.73]

COMPOUNDS = [
    ("LY2409021 (QUERY, reference)", "CC1=CC(=CC(=C1C2=CC=C(C=C2)C(C)(C)C)C)OC(CCC(F)(F)F)C3=CC=C(C=C3)C(=O)NCCC(=O)O", "discontinued Phase 2 GCGR antagonist; reference drug"),
    ("MK-0893", "CC(C1=CC=C(C=C1)C(=O)NCCC(=O)O)N2C(=CC(=N2)C3=CC(=CC(=C3)Cl)Cl)C4=CC5=C(C=C4)C=C(C=C5)OC", "co-crystallised ligand in 5EE7; discontinued Phase 2 (LDL/ALT)"),
    ("PF-06291874", "CCCC(C1=CC=C(C=C1)C(=O)NCCC(=O)O)OC2=CC(=C(C(=C2)C)N3C=C(C=N3)C(F)(F)F)C", "Pfizer Phase 2a GCGR antagonist; development stopped"),
    ("LGD-6972", "CC1=CC(=C(C(=C1)C)C2=CC=C(C=C2)NC(=O)C(CC3=CC=C(C=C3)C(=O)NCCS(=O)(=O)O)C4=CC=C(C=C4)C5=CC=C(C=C5)C(C)(C)C)C", "Ligand oral allosteric GCGR antagonist; status unclear"),
]


def descriptors(smiles):
    m = Chem.MolFromSmiles(smiles)
    params = FilterCatalogParams()
    params.AddCatalog(FilterCatalogParams.FilterCatalogs.PAINS)
    cat = FilterCatalog(params)
    pains = [e.GetDescription() for e in cat.GetMatches(m)]
    mw = Descriptors.MolWt(m)
    logp = Descriptors.MolLogP(m)
    hbd = Lipinski.NumHDonors(m)
    hba = Lipinski.NumHAcceptors(m)
    tpsa = rdMolDescriptors.CalcTPSA(m)
    rot = Lipinski.NumRotatableBonds(m)
    viol = sum([mw > 500, logp > 5, hbd > 5, hba > 10])
    return {"mw": round(mw, 2), "logp": round(logp, 2), "hbd": hbd, "hba": hba,
            "tpsa": round(tpsa, 2), "rotatable": rot,
            "lipinski_violations": viol,
            "lipinski_pass": viol == 0,
            "formula": rdMolDescriptors.CalcMolFormula(m)}, pains


def main():
    results = []
    for label, smiles, note in COMPOUNDS:
        desc, pains = descriptors(smiles)
        r = D.dock(smiles, "5EE7", CENTER, box_size=22.5)
        r["label"] = label
        r["note"] = note
        r["descriptors"] = desc
        r["pains"] = pains
        results.append(r)
        print("DOCK 5EE7:", label, r.get("affinity_kcal_mol"), r.get("ok"),
              "PAINS:", pains, flush=True)
    results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
    out = {
        "topic": {"target": "Glucagon receptor (GCGR)", "reference": "LY2409021",
                  "topic_id": "HP-107", "date": "2026-11-24"},
        "docking": {
            "ok": True, "pdb_id": "5EE7", "resolution": 2.5,
            "center": CENTER,
            "center_note": ("co-crystallised MK-0893 (5MV) centroid, chain A — "
                            "verified by dock._ligand_center; matches the "
                            "pipeline centre exactly"),
            "box_size": 22.5, "exhaustiveness": 8,
            "correction_note": ("Pipeline docked only LY2409021 (-8.20) because "
                                "ChEMBL ligand retrieval returned no_data. "
                                "5EE7 is the correct antagonist-bound GCGR "
                                "structure; this run adds MK-0893 (self-dock "
                                "control), PF-06291874 and LGD-6972 on the "
                                "identical centre/box. No LY2409021-GCGR "
                                "co-crystal exists."),
            "results": results,
        },
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("SAVED:", OUT, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
