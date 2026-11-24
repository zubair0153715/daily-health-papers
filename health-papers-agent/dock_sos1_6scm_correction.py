"""SOS1 correction dock for HP-128 (2026-11-24) — BI-3406 + inhibitors on 6SCM.

Why this run exists: the pipeline docked BI-3406 (-8.88) on 6V9M, which is
WRONG. Centre audit: dock._ligand_center on 6V9M picks GNP (32 atoms), a
GTP analogue bound to KRAS chain A — 6V9M is a SOS1-activator fragment
screen (SOS1 + KRAS-GNP complex), not an inhibitor-bound SOS1 structure.
BI-3406 was docked into the KRAS GTP pocket, so the -8.88 score is
meaningless and is DISCARDED. The correct template is 6SCM: "SOS1 in
Complex with Inhibitor BI-3406", 1.866 A — BI-3406's own co-crystal.
Centre audit: dock._ligand_center on 6SCM picks BI-3406 (L7H, 58 atoms),
[1.31, -31.24, -44.42]. This script docks BI-3406 + MRTX0902 + BAY-293 on
6SCM. SMILES verified via PubChem (MRTX0902 C22H24N6O, BAY-293 C25H28N4O2S).
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402
from rdkit import Chem  # noqa: E402
from rdkit.Chem import Descriptors, Lipinski, rdMolDescriptors  # noqa: E402
from rdkit.Chem.FilterCatalog import FilterCatalog, FilterCatalogParams  # noqa: E402

BASE = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts"
OUT = f"{BASE}/hidden_files/dock-HP-128-2026-11-24-6SCM.json"
CENTER = [1.31, -31.24, -44.42]

COMPOUNDS = [
    ("BI-3406 (QUERY, reference)", "CC1=NC2=CC(=C(C=C2C(=N1)NC(C)C3=CC(=CC(=C3)N)C(F)(F)F)OC4CCOC4)OC", "preclinical SOS1::KRAS PPI inhibitor; clinical analogue BI 1701963"),
    ("MRTX0902", "CC1=C(C=CC=C1C(C)NC2=NN=C(C3=CN=C(C=C32)N4CCOCC4)C)C#N", "brain-penetrant SOS1 inhibitor; Phase 1 NCT05578092"),
    ("BAY-293", "CC1=NC2=CC(=C(C=C2C(=N1)NC(C)C3=CC(=CS3)C4=CC=CC=C4CNC)OC)OC", "Bayer SOS1 tool inhibitor; research use"),
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
        r = D.dock(smiles, "6SCM", CENTER, box_size=22.5)
        r["label"] = label
        r["note"] = note
        r["descriptors"] = desc
        r["pains"] = pains
        results.append(r)
        print("DOCK 6SCM:", label, r.get("affinity_kcal_mol"), r.get("ok"),
              "PAINS:", pains, flush=True)
    results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
    out = {
        "topic": {"target": "Son of sevenless homolog 1 (SOS1)",
                  "reference": "BI-3406",
                  "topic_id": "HP-128", "date": "2026-11-24"},
        "docking": {
            "ok": True, "pdb_id": "6SCM", "resolution": 1.87,
            "center": CENTER,
            "center_note": ("co-crystallised BI-3406 (L7H) centroid, chain A — "
                            "verified by dock._ligand_center"),
            "box_size": 22.5, "exhaustiveness": 8,
            "correction_note": ("Pipeline docked BI-3406 (-8.88) on 6V9M, but the "
                                "centre audit shows 6V9M's largest drug-like "
                                "HETATM group is GNP, a GTP analogue bound to "
                                "KRAS chain A — the drug was docked into the "
                                "KRAS GTP pocket, not SOS1. That score is "
                                "DISCARDED. 6SCM is BI-3406's own co-crystal; "
                                "this run docks BI-3406 + MRTX0902 + BAY-293 on "
                                "it. BI-3406 itself never entered the clinic; "
                                "clinical data belong to analogue BI 1701963."),
            "results": results,
        },
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("SAVED:", OUT, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
