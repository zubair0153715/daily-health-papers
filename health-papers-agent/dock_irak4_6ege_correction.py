"""IRAK4 correction dock for HP-144 (2026-11-24) — inhibitors on 6EGE.

Why this run exists: the pipeline docked only the QUERY (PF-06650833,
-9.72) on 6EGE because ChEMBL ligand retrieval returned no_data. 6EGE IS
the correct template — verified: "Crystal structure of the unphosphorylated
IRAK4 kinase domain bound to a type I inhibitor", 1.40 A, and the centre
audit confirmed the pipeline centre [-13.32, -12.00, -6.41] is exactly the
co-crystallised inhibitor DL1 (chain D) centroid. This script docks
PF-06650833 + emavusertib (CA-4948) + BAY-1834845 + ND-2158 on the same
centre/box/exhaustiveness. NOTE: zimlovisertib IS PF-06650833 (identical
SMILES, C18H20FN3O4) — it is the same compound, not a separate comparator,
and is NOT docked twice. SMILES verified via PubChem (emavusertib
C24H25N7O5, BAY-1834845 C20H21F3N4O4S, ND-2158 C22H30N4O4S).
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402
from rdkit import Chem  # noqa: E402
from rdkit.Chem import Descriptors, Lipinski, rdMolDescriptors  # noqa: E402
from rdkit.Chem.FilterCatalog import FilterCatalog, FilterCatalogParams  # noqa: E402

BASE = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts"
OUT = f"{BASE}/hidden_files/dock-HP-144-2026-11-24-6EGE.json"
CENTER = [-13.32, -12.00, -6.41]

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
        r = D.dock(smiles, "6EGE", CENTER, box_size=22.5)
        r["label"] = label
        r["note"] = note
        r["descriptors"] = desc
        r["pains"] = pains
        results.append(r)
        print("DOCK 6EGE:", label, r.get("affinity_kcal_mol"), r.get("ok"),
              "PAINS:", pains, flush=True)
    results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
    out = {
        "topic": {"target": "Interleukin-1 receptor-associated kinase 4 (IRAK4)",
                  "reference": "PF-06650833",
                  "topic_id": "HP-144", "date": "2026-11-24"},
        "docking": {
            "ok": True, "pdb_id": "6EGE", "resolution": 1.4,
            "center": CENTER,
            "center_note": ("co-crystallised type I inhibitor DL1 centroid, "
                            "chain D — verified by dock._ligand_center; matches "
                            "the pipeline centre exactly"),
            "box_size": 22.5, "exhaustiveness": 8,
            "correction_note": ("Pipeline docked only PF-06650833 (-9.72) "
                                "because ChEMBL ligand retrieval returned "
                                "no_data. 6EGE is the correct IRAK4 template; "
                                "this run adds emavusertib, BAY-1834845 and "
                                "ND-2158 on the identical centre/box. "
                                "Zimlovisertib was NOT added: it is the same "
                                "compound as PF-06650833 (identical SMILES, "
                                "C18H20FN3O4)."),
            "results": results,
        },
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("SAVED:", OUT, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
