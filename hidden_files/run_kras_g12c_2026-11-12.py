import sys, json, traceback
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery.pipeline import run_pipeline
from app.discovery import dock as D

TARGET = "KRAS"
DRUG = "sotorasib"
HF = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files"

def main():
    res = run_pipeline(TARGET, query_name=DRUG, top_n=25, dock_top_n=0)
    with open(f"{HF}/run_kras_g12c_2026-11-12_raw.json", "w") as f:
        json.dump(res, f, indent=1, default=str)
    print("PIPELINE_OK" if res.get("ok") else "PIPELINE_FAIL", res.get("error", ""))
    if not res.get("ok"):
        return
    leads = res.get("leads", []) or []
    t = res.get("target", {}) or {}
    acc = (t.get("uniprot") or {}).get("accession")
    print("ACCESSION:", acc)
    print("LEADS_N:", len(leads))
    for l in leads[:8]:
        print("LEAD:", l.get("chembl_id"), l.get("name"), l.get("ic50_nm"), l.get("smiles", "")[:60])
    if not acc or not leads:
        print("DOCK_SKIPPED")
        return
    dock_res = D.dock_leads(leads[:5], acc, top_n=5)
    with open(f"{HF}/dock_kras_g12c_2026-11-12_raw.json", "w") as f:
        json.dump(dock_res, f, indent=1, default=str)
    print("DOCK_DONE", "ok=", dock_res.get("ok"), "pdb=", dock_res.get("pdb_id"))

try:
    main()
except Exception:
    traceback.print_exc()
