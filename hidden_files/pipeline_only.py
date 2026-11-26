"""Run only the LeadForge pipeline (no dock_leads) and save the raw JSON."""
import json, sys
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery.pipeline import run_pipeline
target, ref, out = sys.argv[1], sys.argv[2], sys.argv[3]
res = run_pipeline(target, query_name=ref, top_n=25, dock_top_n=0)
res["topic"] = {"target": target, "reference": ref}
json.dump(res, open(out, "w"), indent=1)
print("OK:", res.get("ok"), "leads:", len(res.get("leads") or []), "->", out)
