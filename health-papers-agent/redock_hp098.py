"""Re-dock for HP-098 (2026-11-20): PubChem analogues of asundexian + milvexian
(self-dock control) on 7MBO, same centre/box as the pipeline run.

ChEMBL activity endpoint returned HTTP 500 all day, so the comparison set
comes from PubChem fastsimilarity_2d (T>=0.85) instead of ChEMBL bioactivities.
No measured potency is attached to the analogues; that is stated in the paper.
Milvexian is the co-crystallised ligand of 7MBO (Ki 0.11 nM, Dilger 2022).
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

CENTER = [-1.0585, 9.923787878787879, -17.79771212121212]
PDB = "7MBO"

analogues = json.load(open("/tmp/fxia_analogues.json"))
# pick 4: smallest, closest-to-asundexian formula, largest, N7 variant
picks = [135205642, 135205940, 135205866, 135205878]

jobs = []
for cid in picks:
    a = analogues[str(cid)]
    jobs.append({"label": f"PubChem-{cid}", "smiles": a["smiles"],
                 "formula": a["formula"], "mw": a["mw"]})

# milvexian SMILES from PubChem (fetched by name at runtime)
import urllib.request
req = urllib.request.Request(
    "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/milvexian/property/CanonicalSMILES,ConnectivitySMILES,MolecularFormula,MolecularWeight/JSON",
    headers={"User-Agent": "LeadForge/1.0"})
with urllib.request.urlopen(req, timeout=90) as r:
    p = json.load(r)["PropertyTable"]["Properties"][0]
print("MILVEXIAN CID:", p["CID"], p["MolecularFormula"], p["MolecularWeight"], flush=True)
jobs.append({"label": "milvexian (co-crystallised ligand, Ki 0.11 nM)",
             "smiles": p.get("CanonicalSMILES") or p["ConnectivitySMILES"],
             "formula": p["MolecularFormula"], "mw": p["MolecularWeight"],
             "cid": p["CID"]})

results = []
for j in jobs:
    print("DOCKING:", j["label"], flush=True)
    r = D.dock(j["smiles"], PDB, CENTER, box_size=22.5)
    r["label"] = j["label"]
    r["formula"] = j.get("formula")
    r["mw"] = j.get("mw")
    print("  ->", r.get("affinity_kcal_mol"), r.get("poses"), r.get("ok"), flush=True)
    results.append(r)
    with open("/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-098-redock-2026-11-20.json", "w") as f:
        json.dump({"pdb_id": PDB, "center": CENTER, "results": results}, f, indent=1)

print("DONE", flush=True)
