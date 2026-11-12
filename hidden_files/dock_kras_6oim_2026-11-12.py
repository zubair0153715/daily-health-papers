"""Centre-audited Vina benchmark: 5 KRAS G12C covalent inhibitors on 6OIM.

6OIM = KRAS G12C covalently bound to sotorasib (AMG 510), 1.65 A,
Canon et al. Nature 2019;575:217-223. Grid centre = centroid of the
co-crystallised sotorasib (MOV, chain A, 41 atoms), computed with the
audited dock._ligand_center (GDP cofactor excluded). Same protocol as
Papers #1/#3: Vina 1.2.7, box 22.5 A, exhaustiveness 8, 3 poses.

Compounds (all SMILES verified in PubChem/ChEMBL on 2026-11-12):
- sotorasib (re-dock): PubChem CID 137278711
- adagrasib: PubChem CID 138611145
- divarasib: PubChem CID 146624881
- CHEMBL4856277: ChEMBL IC50 0.56 nM vs KRAS G12C/C51S/C80L/C118S
- CHEMBL4855521: ChEMBL IC50 0.51 nM vs same construct (deuterated analog)
CHEMBL4852458 (IC50 0.51 nM, same assay) could NOT be resolved: the
ChEMBL molecule endpoint returned HTTP 500 on three attempts, so no
SMILES is available for it. It is reported as missing, not invented.
"""
import sys, json
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D
from app.discovery import chem as C

HF = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files"
PDB = "6OIM"
CENTER = [1.87, -8.26, -1.36]  # MOV centroid, audited 2026-11-12

COMPOUNDS = [
    ("sotorasib", "C[C@H]1CN(CCN1C2=NC(=O)N(C3=NC(=C(C=C32)F)C4=C(C=CC=C4F)O)C5=C(C=CN=C5C(C)C)C)C(=O)C=C",
     "Ki 11 nM (GDP-KRAS G12C); pERK IC50 68 nM; H358 IC50 0.03 uM (Lanman 2020)"),
    ("adagrasib", "CN1CCC[C@H]1COC2=NC3=C(CCN(C3)C4=CC=CC5=C4C(=CC=C5)Cl)C(=N2)N6CCN([C@H](C6)CC#N)C(=O)C(=C)F",
     "cellular signalling IC50 ~5 nM; viability 10-973 nM (Hallin 2020)"),
    ("divarasib", "C[C@H]1CN(CCN1C2=NC(=NC3=C(C(=C(C=C32)Cl)C4=C(C(=CC(=N4)N)C)C(F)(F)F)F)OC[C@@H]5CCCN5C)C(=O)C=C",
     "nucleotide-exchange IC50 2.4 +/- 0.2 nM (Sci Rep 2025); HCC1171 EC50 2 nM"),
    ("CHEMBL4856277", "C=CC(=O)N1CCN(c2nc(=O)n3c4nc(c(Cl)cc24)-c2c(F)cccc2OCC(F)(F)CCc2ccnc(C(C)C)c2-3)[C@@H](C)C1",
     "ChEMBL IC50 0.56 nM vs KRAS G12C/C51S/C80L/C118S (pChEMBL 9.25)"),
    ("CHEMBL4855521", "[2H]C1([2H])Oc2ccc(F)c(F)c2-c2nc3c(cc2Cl)c(N2C[C@@H](C)N(C(=O)C=C)C[C@@H]2C)nc(=O)n3-c2c(ccnc2C(C)C)OC1([2H])[2H]",
     "ChEMBL IC50 0.51 nM vs KRAS G12C/C51S/C80L/C118S (pChEMBL 9.29); deuterated"),
]

def main():
    # centre audit: recompute and confirm it is the MOV centroid
    pdb_path = D._pdb_path(PDB)
    audited = D._ligand_center(pdb_path)
    dist = sum((a - b) ** 2 for a, b in zip(audited, CENTER)) ** 0.5
    print("AUDITED_CENTER:", audited, "distance_to_used_centre_A:", round(dist, 4))
    assert dist < 0.05, "centre mismatch!"
    results = []
    for label, smi, measured in COMPOUNDS:
        desc = C.descriptors(smi)
        pains = C.pains(smi)
        r = D.dock(smi, PDB, CENTER, box_size=22.5)
        r["label"] = label
        r["smiles"] = smi
        r["measured_potency"] = measured
        r["descriptors"] = desc
        r["pains"] = pains
        results.append(r)
        print("DOCK:", label, r.get("affinity_kcal_mol"), "poses:", r.get("poses"),
              "| ok:", r.get("ok"), r.get("error"), "| PAINS:", pains, flush=True)
    results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
    out = {"ok": True, "pdb_id": PDB, "resolution": 1.65,
           "center": CENTER, "center_audit": "MOV centroid via dock._ligand_center; GDP excluded as cofactor",
           "box_size": 22.5, "exhaustiveness": 8, "vina": "1.2.7",
           "note": "Non-covalent Vina: cannot model the covalent Cys12 bond. Scores are shape/complementarity only.",
           "results": results}
    with open(f"{HF}/dock_kras_6oim_2026-11-12.json", "w") as f:
        json.dump(out, f, indent=1)
    print("SAVED:", f"{HF}/dock_kras_6oim_2026-11-12.json")

try:
    main()
except Exception:
    import traceback; traceback.print_exc()
