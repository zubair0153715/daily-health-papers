"""IRAK4 supplementary dock for HP-144 (2026-11-24) — inhibitors on 5UIU.

Why this run exists: the 6EGE correction dock is valid (PF-06650833 -9.87),
but the literature sweep found the better template: 5UIU, "Crystal
structure of IRAK4 in complex with compound 30", 2.02 A (Lee et al.,
J Med Chem 2017) — PF-06650833's OWN co-crystal. Verified via RCSB:
ligand 8CG is 1-{[(2S,3S,4S)-3-ethyl-4-fluoro-5-oxopyrrolidin-2-yl]methoxy}-
7-methoxyisoquinoline-6-carboxamide, formula C18H20FN3O4 = PF-06650833
(zimlovisertib). Centre audit: dock._ligand_center picks 8CG chain A,
[-25.84, -39.43, 10.30]; the TPO/SEP phospho-residues are correctly
excluded. Same four compounds as the 6EGE run, same box/exhaustiveness;
6EGE is kept as a cross-structure sensitivity check in the paper.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402
from rdkit import Chem  # noqa: E402
from rdkit.Chem import Descriptors, Lipinski, rdMolDescriptors  # noqa: E402
from rdkit.Chem.FilterCatalog import FilterCatalog, FilterCatalogParams  # noqa: E402

BASE = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts"
OUT = f"{BASE}/hidden_files/dock-HP-144-2026-11-24-5UIU.json"
CENTER = [-25.84, -39.43, 10.30]

COMPOUNDS = [
    ("PF-06650833 (QUERY, reference)", "CCC1C(NC(=O)C1F)COC2=NC=CC3=CC(=C(C=C32)OC)C(=O)N", "Pfizer IRAK4 inhibitor; also named zimlovisertib — same compound"),
    ("emavusertib (CA-4948)", "CC1=NC=CC(=C1)C2=NC(=CO2)C(=O)NC3=CC4=C(N=C3N5CCC(C5)O)N=C(O4)N6CCOCC6", "IRAK4/FLT3 inhibitor; clinical in MDS/AML, lymphoma"),
    ("BAY-1834845", "CC(C)(C1=CC2=NN(C=C2C=C1NC(=O)C3=NC(=CC=C3)C(F)(F)F)CCS(=O)(=O)C)O", "Bayer IRAK4 inhibitor; preclinical/clinical-stage"),
    ("ND-2158", "C1CC(CCC1N2CCOCC2)OC3=C4C5=C(CCC5CC(C(=O)N)O)SC4=NC=N3", "Nimbus IRAK4 inhibitor; preclinical"),
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
        r = D.dock(smiles, "5UIU", CENTER, box_size=22.5)
        r["label"] = label
        r["note"] = note
        r["descriptors"] = desc
        r["pains"] = pains
        results.append(r)
        print("DOCK 5UIU:", label, r.get("affinity_kcal_mol"), r.get("ok"),
              "PAINS:", pains, flush=True)
    results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
    out = {
        "topic": {"target": "Interleukin-1 receptor-associated kinase 4 (IRAK4)",
                  "reference": "PF-06650833",
                  "topic_id": "HP-144", "date": "2026-11-24"},
        "docking": {
            "ok": True, "pdb_id": "5UIU", "resolution": 2.02,
            "center": CENTER,
            "center_note": ("co-crystallised PF-06650833 (8CG) centroid, chain A — "
                            "verified by dock._ligand_center; phospho-residues "
                            "TPO/SEP correctly excluded"),
            "box_size": 22.5, "exhaustiveness": 8,
            "correction_note": ("Primary template is 5UIU, PF-06650833's own "
                                "co-crystal (Lee et al. J Med Chem 2017; ligand "
                                "8CG verified as PF-06650833, C18H20FN3O4). "
                                "The 6EGE run is retained as a cross-structure "
                                "sensitivity check. Zimlovisertib was NOT added: "
                                "it is the same compound as PF-06650833."),
            "results": results,
        },
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("SAVED:", OUT, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
