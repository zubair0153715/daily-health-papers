"""Re-dock HP-113 leads at the CORRECT SrtA active-site centre.

Why: run_docking.py's _ligand_center fell back to the first MSE
(selenomethionine) residue of 1T2O (no drug-like ligand in that PDB),
centring the grid 22.1 A from the catalytic site. This script re-docks
the same 5 ligands with Vina at the catalytic-triad centroid
(His120 + Ala184[Cys->Ala] + Arg197, chain A, 1T2O) = [-39.89, -18.59, -0.79].
Same protocol otherwise: box 22.5 A, exhaustiveness 8, best of 3 poses.
"""
import json, sys
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

CENTER = [-39.89, -18.59, -0.79]
PDB = "1T2O"

d = json.load(open("../hidden_files/dock-HP-113-2026-11-27.json"))
leads = d["leads"][:5]  # QUERY berberine + top 4 ChEMBL leads (same set as run 2)
results = []
for l in leads:
    r = D.dock(l["smiles"], PDB, CENTER, box_size=22.5)
    r["label"] = l.get("label")
    r["rank"] = l.get("rank")
    results.append(r)
    print("DOCK:", r.get("label"), r.get("affinity_kcal_mol"), r.get("poses"), flush=True)
results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
out = {"ok": True, "pdb_id": PDB, "resolution": 2.3,
       "center": CENTER,
       "center_basis": "centroid of catalytic triad His120/Ala184(Cys184->Ala)/Arg197, chain A, 1T2O (26 atoms); 22.1 A from the erroneous MSE141 centroid used by run_docking.py",
       "box_size": 22.5, "exhaustiveness": 8,
       "note": "1T2O is the C184A mutant (catalytic Cys replaced by Ala); no inhibitor-bound SrtA structure exists, so the apo active site is used.",
       "results": results}
json.dump(out, open("../hidden_files/dock-HP-113-2026-11-27-redock.json", "w"), indent=1)
print("SAVED ../hidden_files/dock-HP-113-2026-11-27-redock.json")
