"""Single retry of acarbose (QUERY) docking for HP-005, same protocol.

First attempt timed out at Vina's 900 s cap while 4-5 sibling Vina runs
shared the machine. The machine is now quiet (0 Vina processes), so one
retry with the identical protocol (1XCX, centre [5.01, 16.45, 41.56],
box 22.5, exhaustiveness 8, 3 poses). If it fails again, the paper compares
against the published acarbose docking range (-7.6 to -7.7 kcal/mol) and
says so plainly. Result is merged into dock-HP-005c-2026-11-07.json.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402

src = json.load(open("../hidden_files/dock-HP-005-2026-11-07.json"))
q = next(l for l in src["leads"] if l["label"] == "QUERY")
print("Retrying QUERY acarbose ...", flush=True)
try:
    r = D.dock(q["smiles"], "1XCX", [5.01, 16.45, 41.56], box_size=22.5)
except Exception as e:
    r = {"ok": False, "error": f"{type(e).__name__}: {e}"}
r["label"] = "QUERY"
r["rank"] = q.get("rank")
r["smiles"] = q["smiles"]
r["known_activity"] = q.get("known_activity")
r["descriptors"] = q.get("descriptors", {})
r["pains"] = q.get("pains", [])
print("  ->", r.get("affinity_kcal_mol"), r.get("poses"), r.get("ok"),
      r.get("error", ""), flush=True)

out = json.load(open("../hidden_files/dock-HP-005c-2026-11-07.json"))
out["results"] = [x for x in out["results"] if x["label"] != "QUERY"]
out["results"].append(r)
out["results"].sort(key=lambda x: x.get("affinity_kcal_mol", 999))
out["acarbose_retry"] = ("Second attempt on a quiet machine, identical "
                         "protocol; first attempt hit Vina's 900 s cap under "
                         "CPU contention from concurrent sibling runs.")
json.dump(out, open("../hidden_files/dock-HP-005c-2026-11-07.json", "w"),
          indent=1)
print("SAVED", flush=True)
