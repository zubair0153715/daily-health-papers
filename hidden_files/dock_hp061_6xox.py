"""Control docking for HP-061 (GLP-1R): the pipeline auto-picked 4ZGM, which is
the isolated extracellular domain with a semaglutide peptide fragment — NOT
the small-molecule pocket. Orforglipron's real pocket is the upper helical
bundle in the cryo-EM structure 6XOX (Kawai et al. 2020 PNAS, LY3502970 bound).
Dock the query + the top-5 pipeline leads on 6XOX, centre from the bound
LY3502970 (V6G) ligand via D._ligand_center, same Vina protocol (box 22.5,
exhaustiveness 8, best of 3 poses).
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

LEADS = json.load(open("/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-061-2026-11-16.json"))["leads"]

pdb_path = D._pdb_path("6XOX")
center = D._ligand_center(pdb_path)
print("6XOX ligand centre:", center, flush=True)

todo = [LEADS[0]] + [l for l in LEADS[1:6]]
out = {"pdb_id": "6XOX", "center": center, "box_size": 22.5,
       "exhaustiveness": 8, "results": []}
for l in todo:
    r = D.dock(l["smiles"], "6XOX", center, box_size=22.5)
    r["label"] = l["label"]
    r["rank"] = l.get("rank")
    out["results"].append(r)
    print("  DOCK:", l["label"], r.get("affinity_kcal_mol"), r.get("ok"), flush=True)

with open("/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-061-6xox-2026-11-16.json", "w") as f:
    json.dump(out, f, indent=1)
print("SAVED", flush=True)
