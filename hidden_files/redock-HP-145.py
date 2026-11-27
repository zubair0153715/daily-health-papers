"""Re-dock HP-145 ligands on the CORRECT dengue NS5 MTase structure.

Why: run_docking.py resolved the target to the DENV2 polyprotein
(P29990) and ChEMBL target CHEMBL5980 (genome polyprotein), whose
bioactivities are a mixture of NS3-protease and whole-virus assays —
the top "lead" CHEMBL4862353 is an NS3-protease inhibitor (IC50 290 nM),
not an MTase inhibitor. It then docked on 7K93, which is DENV2 NS1 in
complex with an antibody scFv (Science 2021), not NS5 MTase. Every
score from that run is invalid for the MTase question.
This script docks the three SAM-site ligands with published MTase
data — sinefungin (reference), SAH (product inhibitor) and SAM
(natural cofactor) — on 1L9K (Egloff et al., EMBO J 2002, DENV2 MTase
+ SAH, 2.4 A) at the SAH ligand centroid [15.28, -42.04, 0.78] from
dock._ligand_center. Same protocol: box 22.5 A, exhaustiveness 8,
best of 3 poses.
"""
import json, sys
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D
from app.discovery.chem import descriptors, pains

CENTER = [15.28, -42.04, 0.78]
PDB = "1L9K"

d = json.load(open("../hidden_files/dock-HP-145-2026-11-27.json"))
sinefungin_smiles = [l for l in d["leads"] if l["label"] == "QUERY"][0]["smiles"]

ligands = [
    ("SINEFUNGIN", sinefungin_smiles),
    ("SAH", "C1=NC(=C2C(=N1)N(C=N2)C3C(C(C(O3)CSCCC(C(=O)O)N)O)O)N"),
    ("SAM", "C[S+](CCC(C(=O)[O-])N)CC1C(C(C(O1)N2C=NC3=C(N=CN=C32)N)O)O"),
]
results = []
for label, smi in ligands:
    r = D.dock(smi, PDB, CENTER, box_size=22.5)
    r["label"] = label
    r["descriptors"] = descriptors(smi)
    r["pains"] = pains(smi)
    results.append(r)
    print("DOCK:", label, r.get("affinity_kcal_mol"), r.get("poses"), r.get("descriptors"), r.get("pains"), flush=True)
results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
out = {"ok": True, "pdb_id": PDB, "resolution": 2.4,
       "center": CENTER,
       "center_basis": "centroid of co-crystallised SAH (26 atoms) in 1L9K via dock._ligand_center; 1L9K is the DENV2 NS5 MTase domain + SAH (Egloff et al., EMBO J 2002)",
       "box_size": 22.5, "exhaustiveness": 8,
       "excluded": "All four pipeline leads (CHEMBL4862353, CHEMBL5092085, CHEMBL5075993, CHEMBL5081752): ChEMBL target CHEMBL5980 is the genome polyprotein, and the top lead is an NS3-protease inhibitor, not an MTase inhibitor. Docking on 7K93 (DENV2 NS1 + antibody scFv) is invalid for the MTase question.",
       "note": "1L9K is the DENV2 MTase domain (residues 1-296 of NS5); the SAM site is where sinefungin, SAH and SAM bind. Serotype coverage: the MTase domain is conserved across DENV1-4, but this docking is DENV2 only.",
       "results": results}
json.dump(out, open("../hidden_files/dock-HP-145-2026-11-27-redock.json", "w"), indent=1)
print("SAVED ../hidden_files/dock-HP-145-2026-11-27-redock.json")
