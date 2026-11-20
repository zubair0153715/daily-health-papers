"""Supplementary docking for HP-092 (E. coli MurA, Paper #89).

Why this script exists: the LeadForge pipeline's ChEMBL bioactivity
retrieval returned 0 records for CHEMBL1984, but the live ChEMBL API
holds 522 activities (119 nM IC50s). The pipeline therefore ranked only
fosfomycin itself as a "lead" and docked nothing else. This script docks
the real top ChEMBL MurA actives (by nM IC50, distinct molecules) plus
four literature MurA inhibitors with published activity, on the SAME
structure (3KQJ, 1.7 A, E. coli MurA + UNAG), SAME grid centre
([60.69, -44.29, 115.28], verified centroid of co-crystallised UNAG via
dock._ligand_center), SAME box (22.5 A) and exhaustiveness (8) as the
pipeline's fosfomycin re-dock (-5.04 kcal/mol).

Compounds:
  ChEMBL (nM IC50 vs E. coli MurA, CHEMBL1984, live 2026-11-20):
    CHEMBL2335230  2,800 nM  (bromo-nitro furan)
    CHEMBL2335229  4,600 nM  (bromonitromethane)
    CHEMBL5219390  4,500 nM  (thiazole-furan carboxylate)
    CHEMBL5219133  4,800 nM  (thiazole-furan carboxylate)
  Literature (published MurA activity):
    ampelopsin (dihydromyricetin, PubChem CID 161557) - most potent of 13
      flavonoid MurA inhibitors, ACS Omega 2023 (range 480 nM-57 uM)
    quercetin (PubChem CID 5280343) - flavonoid MurA inhibitor, same study
    albendazole (PubChem CID 2082) - MIC 0.0625 mg/mL vs E. coli,
      Antibiotics 2022, 11(4):528 (PMID 35453279)
    diflunisal (PubChem CID 3059) - MIC 0.0625 mg/mL vs E. coli, same study
  Fosfomycin itself (CHEMBL1757, 100 nM IC50 in ChEMBL) was already
  docked by the pipeline: -5.04 kcal/mol. It is NOT re-docked here;
  its score is quoted from dock-HP-092-2026-11-20.json.

  NOTE: fosfomycin is covalent (Cys115). Vina scores non-covalent
  complementarity only and cannot price the covalent bond, so -5.04 is
  NOT a binding-affinity comparison - it is the benchmark that shows
  Vina under-scores the one drug that actually works.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import chem as C  # noqa: E402
from app.discovery import dock as D  # noqa: E402

CENTER = [60.69, -44.29, 115.28]
PDB = "3KQJ"

COMPOUNDS = [
    # (label, source, smiles, known_activity)
    ("CHEMBL2335230", "ChEMBL IC50 2800 nM vs MurA (CHEMBL1984)",
     "O=[N+]([O-])/C(Br)=C/c1ccc(Br)o1", "IC50 2.8 uM"),
    ("CHEMBL2335229", "ChEMBL IC50 4600 nM vs MurA (CHEMBL1984)",
     "O=[N+]([O-])CBr", "IC50 4.6 uM"),
    ("CHEMBL5219390", "ChEMBL IC50 4500 nM vs MurA (CHEMBL1984)",
     "CC(C)(C)OC(=O)C1=C(O)C(=O)N(c2nc3ccccc3s2)C1c1ccc(-c2ccc(Cl)cc2)o1",
     "IC50 4.5 uM"),
    ("CHEMBL5219133", "ChEMBL IC50 4800 nM vs MurA (CHEMBL1984)",
     "CCOC(=O)C1=C(O)C(=O)N(c2nc3ccc(C)cc3s2)C1c1ccc(-c2ccc(C(F)(F)F)cc2Cl)o1",
     "IC50 4.8 uM"),
    ("ampelopsin", "ACS Omega 2023 flavonoid MurA inhibitor (most potent of 13)",
     "C1=C(C=C(C(=C1O)O)O)C2C(C(=O)C3=C(C=C(C=C3O2)O)O)O",
     "MurA IC50 range 480 nM-57 uM (most potent)"),
    ("quercetin", "ACS Omega 2023 flavonoid MurA inhibitor",
     "C1=CC(=C(C=C1C2=C(C(=O)C3=C(C=C(C=C3O2)O)O)O)O)O",
     "MurA inhibitor (flavonoid library)"),
    ("albendazole", "Antibiotics 2022, 11:528 - MIC 0.0625 mg/mL vs E. coli",
     "CCCSC1=CC2=C(C=C1)N=C(N2)NC(=O)OC", "MIC 0.0625 mg/mL vs E. coli"),
    ("diflunisal", "Antibiotics 2022, 11:528 - MIC 0.0625 mg/mL vs E. coli",
     "C1=CC(=C(C=C1C2=C(C=C(C=C2)F)F)C(=O)O)O", "MIC 0.0625 mg/mL vs E. coli"),
]


def main():
    out = {"pdb_id": PDB, "center": CENTER, "box_size": 22.5,
           "exhaustiveness": 8, "results": []}
    for label, source, smi, activity in COMPOUNDS:
        desc = C.descriptors(smi)
        pains = C.pains(smi)
        r = D.dock(smi, PDB, CENTER, box_size=22.5)
        r["label"] = label
        r["source"] = source
        r["known_activity"] = activity
        r["smiles"] = smi
        r["descriptors"] = desc
        r["pains"] = pains
        out["results"].append(r)
        print(f"{label}: affinity={r.get('affinity_kcal_mol')} "
              f"poses={r.get('poses')} pains={pains} "
              f"mw={desc.get('mw')} logp={desc.get('logp')}", flush=True)
    out["results"].sort(key=lambda x: x.get("affinity_kcal_mol", 999))
    with open("../hidden_files/dock-HP-092-supp-2026-11-20.json", "w") as f:
        json.dump(out, f, indent=1)
    print("SAVED ../hidden_files/dock-HP-092-supp-2026-11-20.json")


if __name__ == "__main__":
    main()
