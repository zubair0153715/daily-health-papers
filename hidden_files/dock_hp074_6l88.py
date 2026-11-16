"""Second-structure control for HP-074 (MR): on 4PF3, finerenone scored only
-3.41 while spironolactone scored -10.16, and every compound's three poses
spanned 5-12 kcal/mol (no convergence). Is the failure 4PF3-specific?
Control: dock finerenone, spironolactone and the best lead CHEMBL1215196 on
6L88, the MR LBD bound to esaxerenone (another non-steroidal antagonist),
3.0 A, Takahashi et al. 2020 FEBS Lett (mutations C808S, C910S). Centre from
the bound esaxerenone via D._ligand_center; same Vina protocol (box 22.5,
exhaustiveness 8, best of 3 poses). SMILES from the HP-074 pipeline JSON.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

LEADS = json.load(open("/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-074-2026-11-16.json"))["leads"]
by_label = {l["label"]: l for l in LEADS}

pdb_path = D._pdb_path("6L88")
center = D._ligand_center(pdb_path)
print("6L88 ligand centre:", center, flush=True)

out = {"pdb_id": "6L88", "center": center, "box_size": 22.5,
       "exhaustiveness": 8, "results": []}
for label in ["QUERY", "CHEMBL1215196"]:
    l = by_label[label]
    r = D.dock(l["smiles"], "6L88", center, box_size=22.5)
    r["label"] = label
    out["results"].append(r)
    print("  DOCK:", label, r.get("affinity_kcal_mol"), r.get("poses"), r.get("ok"), flush=True)

import urllib.request, urllib.parse
url = ("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
       + urllib.parse.quote("spironolactone") + "/property/SMILES/JSON")
with urllib.request.urlopen(url, timeout=60) as resp:
    smi = json.load(resp)["PropertyTable"]["Properties"][0]["SMILES"]
r = D.dock(smi, "6L88", center, box_size=22.5)
r["label"] = "spironolactone"
out["results"].append(r)
print("  DOCK: spironolactone", r.get("affinity_kcal_mol"), r.get("poses"), r.get("ok"), flush=True)

with open("/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-074-6l88-2026-11-16.json", "w") as f:
    json.dump(out, f, indent=1)
print("SAVED", flush=True)
