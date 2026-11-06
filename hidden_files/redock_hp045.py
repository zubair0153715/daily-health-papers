"""Re-dock HP-045 leads on 6QGV (PHD2/EGLN1 + spirodecanone inhibitor J2H, 1.40 A).
7Q5V (pipeline pick, 1.17 A) contains the HIF-2a CODD peptide in the pocket:
all ligands scored +17 to +30 kcal/mol (clash with the peptide). 6QGV is
single-chain, inhibitor-bound, no peptide. Same protocol: box 22.5 A,
exhaustiveness 8, 3 poses."""
import json, sys
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

src = json.load(open("../hidden_files/dock-HP-045b-2026-11-06.json"))
leads = src["leads"][:5]  # QUERY + top 4 ranked leads
pdb_id = "6QGV"
centre = D._ligand_center(D._pdb_path(pdb_id))
print("PDB:", pdb_id, "centre:", centre)
results = []
for l in leads:
    r = D.dock(l["smiles"], pdb_id, centre, box_size=22.5)
    r["label"] = l.get("label"); r["rank"] = l.get("rank")
    results.append(r)
    print(" DOCK:", r.get("label"), r.get("affinity_kcal_mol"), r.get("ok"), r.get("error"))
results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
out = {"pdb_id": pdb_id, "resolution": 1.40, "center": [round(c, 2) for c in centre],
       "note": "Re-dock on 6QGV; 7Q5V contains HIF peptide in pocket (+17..+30 kcal/mol clash scores)",
       "results": results}
json.dump(out, open("../hidden_files/dock-HP-045c-2026-11-06.json", "w"), indent=1)
print("SAVED dock-HP-045c-2026-11-06.json")
