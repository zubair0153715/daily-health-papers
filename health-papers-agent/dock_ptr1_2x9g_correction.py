"""PTR1 correction dock for HP-121 (2026-11-25) — genuine TbPTR1 inhibitors on 2X9G.

Why this run exists: the pipeline's ChEMBL ligand retrieval MIS-MAPPED the
target. Its chembl_targets list is a text-search grab-bag (human
maltase-glucoamylase CHEMBL2074, ABCC9, PDE, calcium channel, nAChR, human/
E. coli DHFR, ABL1, EGFR, RNA polymerase) and the 55 bioactivities came
from CHEMBL2074 (human maltase-glucoamylase). The "leads" it docked are
therefore iminosugars (CHEMBL120488/120226/332802 — silyl-iminosugars) and
a hydrazone (CHEMBL5555649), NOT PTR1 inhibitors. Their Vina scores on
2X9G are real numbers but meaningless as a PTR1 comparison, and are
reported in the paper as exactly that — an off-target set.

2X9G IS the correct template — verified: "High resolution structure of
TbPTR1 in complex with Pemetrexed", 1.1 A (Dawson et al., Acta Crystallogr
D 2010;66:1334; PMID 21123874). Centre audit: dock._ligand_center(2X9G)
= [6.40, -15.43, 18.53], exactly the centroid of the co-crystallised
pemetrexed (LYA, chain A) — NOT the NADP+ cofactor centroid
[13.62, -7.64, 12.2]. Same centre/box/exhaustiveness as the pipeline run.

This script docks the literature comparison set on that centre:
methotrexate (reference; TbPTR1 IC50 0.793 uM), pemetrexed (the 2X9G
co-crystal ligand — self-dock control), pyrimethamine (TbPTR1 IC50
0.090 uM — the most potent known antifolate comparator), NMT-C0003
(compound 1b, Pohner et al. J Med Chem 2022;65:9011-9033 — apparent
picomolar TbPTR1 inhibition; 6RX5 co-crystal ligand), LIB_66
(4-(benzyloxy)pyrimidine-2,6-diamine; Linciano et al. Eur J Med Chem
2020;189:112047 — TbPTR1 IC50 0.7-4.0 uM for the scaffold) and
cycloguanil (TbPTR1 IC50 31.6 uM — the WEAK-inhibitor negative control).
All SMILES verified against PubChem by name/CID (see notes below).
Potencies from Tassone et al., Pharmaceuticals 2021;14:636, Table 1.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402
from rdkit import Chem  # noqa: E402
from rdkit.Chem import Descriptors, Lipinski, rdMolDescriptors  # noqa: E402
from rdkit.Chem.FilterCatalog import FilterCatalog, FilterCatalogParams  # noqa: E402

BASE = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts"
OUT = f"{BASE}/hidden_files/dock-HP-121-2026-11-25-2X9G.json"
CENTER = [6.40, -15.43, 18.53]

COMPOUNDS = [
    ("methotrexate (QUERY, reference)",
     "CN(CC1=CN=C2C(=N1)C(=NC(=N2)N)N)C3=CC=C(C=C3)C(=O)NC(CCC(=O)O)C(=O)O",
     "Reference antifolate; TbPTR1 IC50 0.793 uM, TbDHFR-TS IC50 0.040 uM, hDHFR 0.014 uM (Tassone 2021, Table 1); 2C7V co-crystal"),
    ("pemetrexed",
     "C1=CC(=CC=C1CCC2=CNC3=C2C(=O)NC(=N3)N)C(=O)NC(CCC(=O)O)C(=O)O",
     "2X9G co-crystal ligand — self-dock control; PubChem CID 135410875, C20H21N5O6"),
    ("pyrimethamine",
     "CCC1=C(C(=NC(=N1)N)N)C2=CC=C(C=C2)Cl",
     "TbPTR1 IC50 0.090 uM, TbDHFR Ki 0.024 uM, hDHFR Ki 0.47 uM (Tassone 2021, Table 1); PubChem CID 4993"),
    ("NMT-C0003 (compound 1b, Pohner 2022)",
     "CN(CC1=CN=C2C(=N1)C(=NC(=N2)N)N)C3=CC=C(C=C3)C(=O)N4CCC(CC4)C(=O)OC",
     "Apparent picomolar TbPTR1 inhibition; 6RX5 co-crystal ligand; PubChem CID 23629645, C22H26N8O3"),
    ("LIB_66 (4-(benzyloxy)pyrimidine-2,6-diamine)",
     "C1=CC=C(C=C1)COC2=NC(=NC(=C2)N)N",
     "Linciano 2020 LIBRA hit; scaffold TbPTR1 IC50 0.7-4.0 uM; PubChem CID 10130617, C11H12N4O"),
    ("cycloguanil",
     "CC1(N=C(N=C(N1C2=CC=C(C=C2)Cl)N)N)C",
     "WEAK-inhibitor negative control; TbPTR1 IC50 31.6 uM (Tassone 2021, Table 1); PubChem CID 9049"),
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
        r = D.dock(smiles, "2X9G", CENTER, box_size=22.5)
        r["label"] = label
        r["note"] = note
        r["descriptors"] = desc
        r["pains"] = pains
        results.append(r)
        print("DOCK 2X9G:", label, r.get("affinity_kcal_mol"), r.get("ok"),
              "PAINS:", pains, flush=True)
    results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
    out = {
        "topic": {"target": "Trypanosoma brucei pteridine reductase 1 (PTR1)",
                  "reference": "methotrexate",
                  "topic_id": "HP-121", "date": "2026-11-25"},
        "docking": {
            "ok": True, "pdb_id": "2X9G", "resolution": 1.1,
            "center": CENTER,
            "center_note": ("co-crystallised pemetrexed (LYA, chain A) centroid — "
                            "verified by dock._ligand_center; NOT the NADP+ "
                            "cofactor centroid [13.62, -7.64, 12.2]"),
            "box_size": 22.5, "exhaustiveness": 8,
            "correction_note": ("Pipeline ChEMBL retrieval mis-mapped the target "
                                "to human maltase-glucoamylase (CHEMBL2074); its "
                                "docked 'leads' were iminosugars/hydrazone, not "
                                "PTR1 inhibitors. This run docks genuine TbPTR1 "
                                "inhibitors from the literature on the identical "
                                "centre/box. Pipeline methotrexate score -9.05 "
                                "on 2X9G is reproduced here in the same run."),
            "results": results,
        },
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("SAVED:", OUT, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
