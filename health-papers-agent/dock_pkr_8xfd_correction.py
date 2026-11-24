"""PKR correction dock for HP-146 (2026-11-24) — mitapivat + activators on 8XFD.

Why this run exists: the pipeline docked only the QUERY (mitapivat, -12.02)
on 7FS3 because ChEMBL ligand retrieval returned no_data. 7FS3 is LIVER
pyruvate kinase (PKL) in complex with "allosteric modulator 15" — the same
PKLR gene, but the liver isoform, not the red-cell isoform this paper is
about. The correct template is 8XFD: "Crystal structure of pyruvate kinase
tetramer in complex with allosteric activator, Mitapivat (MTPV, AG-348)",
2.10 A — erythrocyte PK with mitapivat itself bound. Centre audit:
dock._ligand_center on 8XFD picks mitapivat (WV2, 32 atoms, chain B),
[9.10, 11.33, 23.79]; FBP (20 atoms) is correctly not picked. This script
docks mitapivat + etavopivat + tebapivat (AG-946) on 8XFD. The 7FS3 result
is kept as a cross-isoform sensitivity check in the paper, not the headline.
SMILES verified via PubChem (etavopivat C22H23N3O6S, tebapivat C18H16N8OS).
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402
from dock_lenient import install_charge_blanked_prep  # noqa: E402
install_charge_blanked_prep()  # 8XFD charge annotation breaks RDKit sanitize
from rdkit import Chem  # noqa: E402
from rdkit.Chem import Descriptors, Lipinski, rdMolDescriptors  # noqa: E402
from rdkit.Chem.FilterCatalog import FilterCatalog, FilterCatalogParams  # noqa: E402

BASE = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts"
OUT = f"{BASE}/hidden_files/dock-HP-146-2026-11-24-8XFD.json"
CENTER = [9.10, 11.33, 23.79]

COMPOUNDS = [
    ("mitapivat (QUERY, reference)", "C1CC1CN2CCN(CC2)C(=O)C3=CC=C(C=C3)NS(=O)(=O)C4=CC=CC5=C4N=CC=C5", "approved PKR activator (FDA 2022 PK deficiency; Dec 2025 thalassaemia)"),
    ("etavopivat", "C1COC2=C(O1)C=C(C=N2)S(=O)(=O)N3CC4=C(C3)CN(C4)C(=O)C(CO)C5=CC=CC=C5", "investigational PKR activator; HIBISCUS Phase 2/3, NDA filed Nov 2026"),
    ("tebapivat (AG-946)", "CN1C2=C(C=NN(C2=O)CC3=NC(=CC=C3)N)C4=C1N=C(S4)CC5=CC=NN5", "investigational PKR activator; SCD programme stopped Jul 2026"),
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
        r = D.dock(smiles, "8XFD", CENTER, box_size=22.5)
        r["label"] = label
        r["note"] = note
        r["descriptors"] = desc
        r["pains"] = pains
        results.append(r)
        print("DOCK 8XFD:", label, r.get("affinity_kcal_mol"), r.get("ok"),
              "PAINS:", pains, flush=True)
    results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
    out = {
        "topic": {"target": "Red-cell pyruvate kinase (PKR/PKLR)",
                  "reference": "mitapivat",
                  "topic_id": "HP-146", "date": "2026-11-24"},
        "docking": {
            "ok": True, "pdb_id": "8XFD", "resolution": 2.1,
            "center": CENTER,
            "center_note": ("co-crystallised mitapivat (WV2) centroid, chain B — "
                            "verified by dock._ligand_center; FBP (20 atoms) "
                            "correctly not picked"),
            "box_size": 22.5, "exhaustiveness": 8,
            "correction_note": ("Pipeline docked only mitapivat (-12.02) on 7FS3 "
                                "(LIVER pyruvate kinase, PKL, with modulator 15) "
                                "because ChEMBL ligand retrieval returned no_data. "
                                "7FS3 is the same PKLR gene but the wrong isoform "
                                "for a red-cell paper; this run uses 8XFD, "
                                "erythrocyte PK with mitapivat itself bound, and "
                                "adds etavopivat + tebapivat. The 7FS3 score is "
                                "retained only as a cross-isoform sensitivity check."),
            "results": results,
        },
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("SAVED:", OUT, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
