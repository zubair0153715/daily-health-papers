"""Resume HP-098 re-dock (2026-11-20): dock the two remaining compounds
(PubChem-135205878, milvexian) on 7MBO, same centre/box as the pipeline run.
Loads the checkpointed JSON (3 results already saved) and appends.
Run detached with nohup so it survives session reaping.
"""
import json
import sys
import urllib.request

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

CENTER = [-1.0585, 9.923787878787879, -17.79771212121212]
PDB = "7MBO"
OUT = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-098-redock-2026-11-20.json"

analogues = json.load(open("/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/fxia_analogues-2026-11-20.json"))
jobs = [{"label": "PubChem-135205878",
         "smiles": analogues["135205878"]["smiles"],
         "formula": analogues["135205878"]["formula"],
         "mw": analogues["135205878"]["mw"]}]

req = urllib.request.Request(
    "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/118277544/property/CanonicalSMILES,ConnectivitySMILES,MolecularFormula,MolecularWeight/JSON",
    headers={"User-Agent": "LeadForge/1.0"})
with urllib.request.urlopen(req, timeout=90) as r:
    p = json.load(r)["PropertyTable"]["Properties"][0]
jobs.append({"label": "milvexian (co-crystallised ligand, Ki 0.11 nM)",
             "smiles": p.get("CanonicalSMILES") or p["ConnectivitySMILES"],
             "formula": p["MolecularFormula"], "mw": p["MolecularWeight"],
             "cid": p["CID"]})

data = json.load(open(OUT))
results = data["results"]
have = {r["label"] for r in results}
for j in jobs:
    if j["label"] in have:
        print("SKIP (already done):", j["label"], flush=True)
        continue
    print("DOCKING:", j["label"], flush=True)
    r = D.dock(j["smiles"], PDB, CENTER, box_size=22.5)
    r["label"] = j["label"]
    r["formula"] = j.get("formula")
    r["mw"] = j.get("mw")
    print("  ->", r.get("affinity_kcal_mol"), r.get("poses"), r.get("ok"), flush=True)
    results.append(r)
    with open(OUT, "w") as f:
        json.dump({"pdb_id": PDB, "center": CENTER, "results": results}, f, indent=1)
print("DONE", flush=True)
