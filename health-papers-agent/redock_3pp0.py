"""Re-dock HP-028 leads + lapatinib against the HER2 kinase domain (PDB 3PP0).

The pipeline auto-picked 8JYR, which is the HER2 extracellular domain I in an
antibody complex — the wrong pocket for a kinase inhibitor. 3PP0 is the HER2
kinase domain (2.25 A) co-crystallised with TAK-285 (03Q); grid centre is the
03Q centroid, same Vina protocol (box 22.5 A, exhaustiveness 8, 3 poses).
"""
import sys, json
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

src = json.load(open("../hidden_files/dock-HP-028b-2026-11-04.json"))
leads = {l["label"]: l for l in src["leads"]}
order = ["CHEMBL4105329", "CHEMBL203599", "CHEMBL203661", "CHEMBL258282", "CHEMBL483332", "QUERY"]
center = [17.098970588235293, 16.548676470588234, 26.60064705882353]
results = []
for lab in order:
    l = leads[lab]
    r = D.dock(l["smiles"], "3PP0", center, box_size=22.5)
    r["label"] = lab
    r["rank"] = l.get("rank")
    results.append(r)
    print("DOCK", lab, r.get("affinity_kcal_mol"), r.get("poses"), r.get("ok"), flush=True)
results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
out = {"ok": True, "pdb_id": "3PP0", "resolution": 2.25,
       "pdb_title": "Crystal Structure of the Kinase domain of Human HER2 (erbB2)",
       "co_crystallised_ligand": "03Q (TAK-285)",
       "center": [round(c, 2) for c in center], "box_size": 22.5,
       "exhaustiveness": 8, "vina": "1.2.7",
       "note": "Manual re-dock: pipeline auto-pick 8JYR is the HER2 extracellular domain I (antibody complex) - wrong pocket for a kinase inhibitor. Re-docked against the HER2 kinase domain 3PP0, same protocol.",
       "results": results}
json.dump(out, open("../hidden_files/dock-HP-028c-2026-11-04.json", "w"), indent=1)
print("SAVED")
