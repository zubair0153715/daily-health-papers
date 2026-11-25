"""TRPV1 correction dock for HP-149 (2026-11-25) — modulators on 8GFA.

Why this run exists: the pipeline's run_docking.py reported
no_pdb_found, because find_pdb_for_uniprot only accepts X-ray
structures <3.0 A and every TRPV1 structure is cryo-EM. That is a
filter limitation, not an absence of structure: human TRPV1 in
complex with the antagonist SB-366791 exists as PDB 8GFA
(Neuberger et al., Nat Commun 2023;14:2451; PMID 37117175),
2.29 A, the best-resolution human TRPV1 structure available.

CENTRE AUDIT (the 2026-11-11 lesson): dock._ligand_center on 8GFA
returns [92.49, 85.19, 76.00] — that is the centroid of POV A 1201,
a PHOSPHOLIPID, not the drug site. POV is not in dock._LIPIDS, so
the picker takes the largest HETATM group (POV, 134 atoms) over
the drug (ZEI, 34 atoms). The POV centroid sits ~18.4 A from the
vanilloid pocket, so a box centred there would miss the pocket.
The correct centre is the centroid of the co-crystallised
SB-366791 (residue ZEI, chain A, seqnum 1202), computed directly
from the PDB file: [105.36, 80.97, 88.36]. The tetramer has four
equivalent vanilloid pockets (one per subunit); subunit A is used,
exactly as the IRAK4 papers used one pocket.

Compounds (SMILES verified against PubChem by molecular formula):
- capsaicin (QUERY, reference): the topical agonist comparator.
  NOT an oral systemic drug — stated in the paper.
- SB-366791: co-crystallised antagonist, self-dock control
  (SMILES from the RCSB ZEI chemical component record).
- Top 5 pipeline leads from dock-HP-149-2026-11-25.json.
  NOTE: CHEMBL17976 IS resiniferatoxin (same SMILES) — docked
  once, labelled as such, not twice.
- Known comparators: SB-705498, AMG-517, capsazepine (PubChem
  CIDs 9910486, 16007367, 2733484).

Caveat, stated in the paper: 8GFA is the ANTAGONIST-bound
(closed) conformation, so it may favour antagonists over agonists;
capsaicin and resiniferatoxin are agonists, and a docking score
measures pocket fit, not function — agonist and antagonist scores
are compared only as binding, never as analgesic potency.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402
from rdkit import Chem  # noqa: E402
from rdkit.Chem import Descriptors, Lipinski, rdMolDescriptors  # noqa: E402
from rdkit.Chem.FilterCatalog import FilterCatalog, FilterCatalogParams  # noqa: E402

BASE = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts"
OUT = f"{BASE}/hidden_files/dock-HP-149-2026-11-25-8GFA.json"
CENTER = [105.36, 80.97, 88.36]

COMPOUNDS = [
    ("capsaicin (QUERY, reference — topical agonist)",
     "CC(C)C=CCCCCC(=O)NCC1=CC(=C(C=C1)O)OC",
     "Reference drug; topical 8% patch (Qutenza); EC50 ~700 nM on TRPV1; NOT an oral systemic drug"),
    ("SB-366791 (co-crystallised antagonist — self-dock control)",
     "COc1cccc(NC(=O)/C=C/c2ccc(Cl)cc2)c1",
     "Antagonist bound in 8GFA (residue ZEI); PubChem CID 667594; ChEMBL CHEMBL122413"),
    ("CHEMBL3681230 (pipeline lead #1)",
     "COc1cc(CC(=O)NCc2ccc(C(F)(F)F)nc2N2CCC(C)CC2)cc(Br)c1O",
     "Top pipeline similarity lead vs ChEMBL TRPV1 actives"),
    ("resiniferatoxin (pipeline lead #2, CHEMBL17976)",
     "C=C(C)[C@]12C[C@@H](C)[C@@]34O[C@](Cc5ccccc5)(O[C@@H]1[C@@H]3C=C(COC(=O)Cc1ccc(O)c(OC)c1)C[C@]1(O)C(=O)C(C)=C[C@@H]41)O2",
     "Ultra-potent TRPV1 agonist, several thousand-fold more potent than capsaicin; same compound as CHEMBL17976, docked once"),
    ("CHEMBL228451 (pipeline lead #3)",
     "CC(C)(C)c1ccc(CNC(=S)NCc2ccc(NS(C)(=O)=O)cc2)cc1",
     "Pipeline similarity lead vs ChEMBL TRPV1 actives"),
    ("CHEMBL4242293 (pipeline lead #4)",
     "CC1CCN(c2nc(C(F)(F)F)ccc2CNC(=O)Cc2cc(Cl)c(N)c(Cl)c2)CC1",
     "Pipeline similarity lead vs ChEMBL TRPV1 actives"),
    ("CHEMBL3407765 (pipeline lead #5)",
     "CC(C(=O)NCc1ccc(C(F)(F)Cl)nc1OC1CCCC1)c1ccc(NS(C)(=O)=O)c(F)c1",
     "Pipeline similarity lead vs ChEMBL TRPV1 actives"),
    ("SB-705498 (known antagonist, Phase II)",
     "C1CN(C[C@@H]1NC(=O)NC2=CC=CC=C2Br)C3=NC=C(C=C3)C(F)(F)F",
     "GSK antagonist; pKi 7.6 human TRPV1; IC50 3 nM (capsaicin mode); Phase II completed; PubChem CID 9910486"),
    ("AMG-517 (known antagonist, Phase I — hyperthermia)",
     "CC(=O)NC1=NC2=C(C=CC=C2S1)OC3=NC=NC(=C3)C4=CC=C(C=C4)C(F)(F)F",
     "Amgen antagonist; IC50 <10 nM; Phase I stopped for hyperthermia (>40 C); PubChem CID 16007367"),
    ("capsazepine (first TRPV1 antagonist, preclinical)",
     "C1CC2=CC(=C(C=C2CN(C1)C(=S)NCCC3=CC=C(C=C3)Cl)O)O",
     "First identified TRPV1 antagonist; never reached clinic; PubChem CID 2733484"),
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
        r = D.dock(smiles, "8GFA", CENTER, box_size=22.5)
        r["label"] = label
        r["note"] = note
        r["descriptors"] = desc
        r["pains"] = pains
        results.append(r)
        print("DOCK 8GFA:", label, r.get("affinity_kcal_mol"), r.get("ok"),
              "PAINS:", pains, flush=True)
    results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
    out = {
        "topic": {"target": "Transient receptor potential vanilloid 1 (TRPV1)",
                  "reference": "capsaicin",
                  "topic_id": "HP-149", "date": "2026-11-25"},
        "docking": {
            "ok": True, "pdb_id": "8GFA", "resolution": 2.29,
            "center": CENTER,
            "center_note": ("co-crystallised antagonist SB-366791 (residue "
                            "ZEI, chain A, seqnum 1202) centroid, computed "
                            "directly from the PDB file. dock._ligand_center "
                            "returns the WRONG centre here ([92.49, 85.19, "
                            "76.00] = POV A 1201 phospholipid, ~18.4 A from "
                            "the pocket) because POV is not in dock._LIPIDS "
                            "and is larger than the drug (134 vs 34 atoms)."),
            "box_size": 22.5, "exhaustiveness": 8,
            "correction_note": ("Pipeline run_docking.py reported "
                                "no_pdb_found: find_pdb_for_uniprot accepts "
                                "only X-ray structures <3.0 A, and all TRPV1 "
                                "structures are cryo-EM. 8GFA is the "
                                "best-resolution human TRPV1 structure "
                                "(2.29 A) with an antagonist in the vanilloid "
                                "pocket. 8GFA is the antagonist-bound closed "
                                "conformation, which may favour antagonists "
                                "over agonists; scores compare pocket fit "
                                "only, never analgesic potency."),
            "results": results,
        },
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("SAVED:", OUT, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
