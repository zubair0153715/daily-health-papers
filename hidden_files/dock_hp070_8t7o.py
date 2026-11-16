"""Control docking for HP-070 (IDH1): the pipeline auto-picked 6BKX, which is
WILD-TYPE IDH1 (title: 'Novel modes of inhibition of wild-type IDH1'), so the
scores describe wild-type binding, not the mutant binding that defines
ivosidenib. Control: dock the same compounds on 8T7O, the R132H mutant bound
to AG-120 (ivosidenib) itself (McCoy et al. 2024 Nat Commun 15:7877, 2.05 A),
centre from the bound ivosidenib via D._ligand_center, same Vina protocol
(box 22.5, exhaustiveness 8, best of 3 poses).
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

LEADS = json.load(open("/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-070-2026-11-16.json"))["leads"]

pdb_path = D._pdb_path("8T7O")
center = D._ligand_center(pdb_path)
print("8T7O ligand centre:", center, flush=True)

todo = [LEADS[0]] + [l for l in LEADS[1:5]]
out = {"pdb_id": "8T7O", "center": center, "box_size": 22.5,
       "exhaustiveness": 8, "results": []}
for l in todo:
    r = D.dock(l["smiles"], "8T7O", center, box_size=22.5)
    r["label"] = l["label"]
    r["rank"] = l.get("rank")
    out["results"].append(r)
    print("  DOCK:", l["label"], r.get("affinity_kcal_mol"), r.get("ok"), flush=True)

with open("/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-070-8t7o-2026-11-16.json", "w") as f:
    json.dump(out, f, indent=1)
print("SAVED", flush=True)
