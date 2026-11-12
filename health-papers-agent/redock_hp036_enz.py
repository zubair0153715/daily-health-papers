"""Re-dock enzalutamide (QUERY) into AR-LBD 8E1A at exhaustiveness 32.

HP-036 (2026-11-12): the standard run docked enzalutamide at +0.71 kcal/mol
(all three poses positive) on the centre-audited 8E1A pocket, while four
ChEMBL leads scored -6.96 to -9.88. This re-dock tests whether the failed
reference is an exhaustiveness artefact or robust.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

d = json.load(open("/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-036-2026-11-12.json"))
q = next(l for l in d["leads"] if l["label"] == "QUERY")
center = d["docking"]["center"]
print("SMILES:", q["smiles"])
print("center:", center)
r = D.dock(q["smiles"], "8E1A", center, box_size=22.5, exhaustiveness=32, n_poses=3)
print("REDOCK-ENZALUTAMIDE-exh32:", json.dumps(r))
with open("/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/redock-HP-036-enzalutamide-2026-11-12.json", "w") as f:
    json.dump(r, f, indent=1)
