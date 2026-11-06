"""Re-dock HP-008 leads on 4C7K (11b-HSD1 + DZL inhibitor, 1.91 A).
1XU9 (pipeline pick, 1.55 A) fails RDKit receptor parse; 1XU7's centre is
a CHAPS detergent, not an inhibitor. 4C7K verified: DZL in the active site.
Same protocol as dock_leads: box 22.5 A, exhaustiveness 8, 3 poses."""
import json, sys
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

src = json.load(open("../hidden_files/dock-HP-008b-2026-11-06.json"))
leads = src["leads"][:5]  # QUERY + top 4 ranked leads
pdb_id = "4C7K"
centre = D._ligand_center(D._pdb_path(pdb_id))
print("PDB:", pdb_id, "centre:", centre)
results = []
for l in leads:
    r = D.dock(l["smiles"], pdb_id, centre, box_size=22.5)
    r["label"] = l.get("label"); r["rank"] = l.get("rank")
    results.append(r)
    print(" DOCK:", r.get("label"), r.get("affinity_kcal_mol"), r.get("ok"), r.get("error"))
results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
out = {"pdb_id": pdb_id, "resolution": 1.91, "center": [round(c, 2) for c in centre],
       "note": "Re-dock on 4C7K; 1XU9 receptor parse failed, 1XU7 centre is CHAPS detergent",
       "results": results}
json.dump(out, open("../hidden_files/dock-HP-008c-2026-11-06.json", "w"), indent=1)
print("SAVED dock-HP-008c-2026-11-06.json")
