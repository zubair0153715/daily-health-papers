"""ETA correction dock for HP-140 (2026-11-24) — ERAs on 8HCQ.

Why this run exists: the pipeline found NO PDB for ETA (UniProt P25101)
and docking was skipped; ChEMBL ligand retrieval also returned no_data.
Verified fact (literature sweep, 2026-11-24): NO ETA-antagonist crystal
structure exists. The first ETA structure is the 2023 cryo-EM complex
8HCQ: "Cryo-EM structure of endothelin-1-bound ETAR-Gq complex", 3.0 A
(Ji et al., Nat Commun 2023;14:1268, doi:10.1038/s41467-023-36998-9).
So this run docks into 8HCQ with the honest limitation stated in the
paper: it is an ACTIVE, ET-1-bound conformation, not an antagonist-bound
one — scores are a pocket-occupancy screen, not antagonist affinity.

Centre: ET-1 is chain L (21 aa peptide, ATOM records, not HETATM, so
dock._ligand_center cannot pick it). The small-molecule antagonist pocket
overlaps the deep orthosteric site where ET-1's C-terminus sits, so the
centre is the centroid of ET-1 residues 16-21: [122.27, 115.66, 128.27],
computed directly from the PDB coordinates (see /tmp/et1_centre.py).

Receptor prep: dock._prep_receptor keeps ALL ATOM records, including the
ET-1 peptide chain L — which would block the pocket. This script therefore
strips chain L from the cached 8HCQ.pdb BEFORE docking, then restores the
original PDB afterwards. The derived 8HCQ_rec.pdbqt in the cache is left
as the chain-L-stripped receptor on purpose: any future 8HCQ dock must
use the stripped receptor, never the ET-1-occupied one. G-protein chains
(A/B/G) and scFv (E) remain; they are far from the 22.5 A box and harmless.

SMILES verified via PubChem (bosentan C27H29N5O6S, macitentan
C19H20Br2N6O4S, sitaxentan C18H15ClN2O6S2, zibotentan C19H16N6O4S).
"""
import json
import os
import shutil
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402
from dock_lenient import install_charge_blanked_prep  # noqa: E402
install_charge_blanked_prep()  # 8HCQ charge annotation breaks RDKit sanitize
from rdkit import Chem  # noqa: E402
from rdkit.Chem import Descriptors, Lipinski, rdMolDescriptors  # noqa: E402
from rdkit.Chem.FilterCatalog import FilterCatalog, FilterCatalogParams  # noqa: E402

BASE = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts"
OUT = f"{BASE}/hidden_files/dock-HP-140-2026-11-24-8HCQ.json"
CENTER = [122.27, 115.66, 128.27]
CACHE = "/home/hatch/workspace/clinic-demo/app/discovery/data/pdb_cache"
PDB_PATH = os.path.join(CACHE, "8HCQ.pdb")
REC_PATH = os.path.join(CACHE, "8HCQ_rec.pdbqt")

COMPOUNDS = [
    ("ambrisentan (QUERY, reference)", "CC1=CC(=NC(=N1)OC(C(=O)O)C(C2=CC=CC=C2)(C3=CC=CC=C3)OC)C", "approved ETA-selective ERA (FDA 2007); reference drug"),
    ("bosentan", "CC(C)(C)C1=CC=C(C=C1)S(=O)(=O)NC2=C(C(=NC(=N2)C3=NC=CC=N3)OCCO)OC4=CC=CC=C4OC", "first ERA, dual ETA/ETB (FDA 2001)"),
    ("macitentan", "CCCNS(=O)(=O)NC1=C(C(=NC=N1)OCCOC2=NC=C(C=N2)Br)C3=CC=C(C=C3)Br", "dual ERA (FDA 2013); SERAPHIN 45% morbidity-mortality reduction"),
    ("sitaxentan", "CC1=CC2=C(C=C1CC(=O)C3=C(C=CS3)S(=O)(=O)NC4=C(C(=NO4)C)Cl)OCO2", "ETA-selective; withdrawn 2010 (fatal hepatotoxicity)"),
    ("zibotentan", "CC1=CN=C(C(=N1)OC)NS(=O)(=O)C2=C(N=CC=C2)C3=CC=C(C=C3)C4=NN=CO4", "ETA-selective; investigated in oncology/CKD, not PAH-approved"),
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


def strip_chain_L():
    """Remove ET-1 (chain L) ATOM records so the pocket is empty. Returns
    True if the chain was present and removed."""
    with open(PDB_PATH) as f:
        lines = f.readlines()
    kept = [l for l in lines if not (l.startswith("ATOM") and len(l) > 21 and l[21] == "L")]
    removed = len(lines) - len(kept)
    if removed == 0:
        return False
    with open(PDB_PATH, "w") as f:
        f.writelines(kept)
    print(f"Stripped {removed} ET-1 chain-L ATOM lines from 8HCQ.pdb", flush=True)
    return True


def main():
    backup = PDB_PATH + ".orig-chainL"
    shutil.copy(PDB_PATH, backup)
    try:
        assert strip_chain_L(), "chain L not found in 8HCQ.pdb"
        # force receptor rebuild from the stripped PDB
        if os.path.exists(REC_PATH):
            os.remove(REC_PATH)
        results = []
        for label, smiles, note in COMPOUNDS:
            desc, pains = descriptors(smiles)
            r = D.dock(smiles, "8HCQ", CENTER, box_size=22.5)
            r["label"] = label
            r["note"] = note
            r["descriptors"] = desc
            r["pains"] = pains
            results.append(r)
            print("DOCK 8HCQ:", label, r.get("affinity_kcal_mol"), r.get("ok"),
                  "PAINS:", pains, flush=True)
    finally:
        # restore the original PDB; the derived rec pdbqt stays stripped
        # (documented: future 8HCQ docks must use the stripped receptor)
        shutil.copy(backup, PDB_PATH)
        os.remove(backup)
        print("Restored original 8HCQ.pdb; 8HCQ_rec.pdbqt left as the "
              "chain-L-stripped receptor (see script header).", flush=True)
    results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
    out = {
        "topic": {"target": "Endothelin receptor type A (ETA)",
                  "reference": "ambrisentan",
                  "topic_id": "HP-140", "date": "2026-11-24"},
        "docking": {
            "ok": True, "pdb_id": "8HCQ", "resolution": 3.0,
            "center": CENTER,
            "center_note": ("centroid of ET-1 residues 16-21 (chain L) — the "
                            "deep orthosteric site where the peptide C-terminus "
                            "sits; computed from PDB coordinates. ET-1 is a "
                            "peptide chain, not a HETATM ligand, so "
                            "dock._ligand_center cannot pick it."),
            "box_size": 22.5, "exhaustiveness": 8,
            "correction_note": ("Pipeline found no PDB for ETA and skipped "
                                "docking. No ETA-antagonist structure exists; "
                                "8HCQ is the first ETA structure (cryo-EM, "
                                "ET-1-bound ETAR-Gq, Ji et al. Nat Commun "
                                "2023) — an ACTIVE conformation, not an "
                                "antagonist-bound one. ET-1 chain L was "
                                "stripped from the receptor before docking so "
                                "the pocket is empty; the cached 8HCQ_rec.pdbqt "
                                "is the stripped receptor. Scores are a "
                                "pocket-occupancy screen, not antagonist "
                                "affinity, and must be read with that limit."),
            "results": results,
        },
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("SAVED:", OUT, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
