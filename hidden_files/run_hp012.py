import json, sys
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import pipeline as P
res = P.run_pipeline("Klebsiella pneumoniae carbapenemase KPC-2",
                     query_name="avibactam", top_n=25)
res["topic"] = "HP-012"
json.dump(res, open("pipeline-HP-012-2026-11-08.json", "w"), indent=1)
print("OK:", res.get("ok"))
print("target uniprot:", (res.get("target") or {}).get("uniprot", {}).get("accession"))
print("chembl_target:", (res.get("target") or {}).get("chembl_target"))
print("ligands:", res.get("ligands_found"), "leads:", len(res.get("leads", [])))
for l in res.get("leads", [])[:10]:
    print(" ", l.get("label"), l.get("chembl_id"), "score", l.get("score"), "sim", l.get("similarity"), "pchembl", l.get("pchembl"))
