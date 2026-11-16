"""Steroidal control docking for HP-074 (MR): the pipeline docked finerenone
(non-steroidal) and four ChEMBL leads on 4PF3 (MR LBD + compound 37a, a
non-steroidal antagonist, 1.1 A). Finerenone scored only -3.41 and pose spreads
were wide (up to 10.4 kcal/mol within one compound), so the screen's
reliability is in question. Control: dock the two steroidal MRAs,
spironolactone and eplerenone, on the SAME structure (4PF3), same centre
[-0.09, 30.97, 41.11], same Vina protocol (box 22.5, exhaustiveness 8, best of
3 poses). SMILES fetched live from PubChem PUG REST by name (key "SMILES").
Their literature MR potencies: spironolactone IC50 ~24.2 nM, eplerenone
weaker (~100-360 nM range in binding assays; report as literature range,
do not state a single value unless verified).
"""
import json
import sys
import urllib.request

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

CENTER = [-0.09, 30.97, 41.11]

def pubchem_smiles(name):
    url = ("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
           + urllib.parse.quote(name) + "/property/SMILES/JSON")
    with urllib.request.urlopen(url, timeout=60) as r:
        d = json.load(r)
    p = d["PropertyTable"]["Properties"][0]
    return p["CID"], p["SMILES"]

out = {"pdb_id": "4PF3", "center": CENTER, "box_size": 22.5,
       "exhaustiveness": 8, "results": []}
for name in ["spironolactone", "eplerenone"]:
    cid, smi = pubchem_smiles(name)
    print(name, "CID", cid, smi, flush=True)
    r = D.dock(smi, "4PF3", CENTER, box_size=22.5)
    r["label"] = name
    r["cid"] = cid
    out["results"].append(r)
    print("  DOCK:", name, r.get("affinity_kcal_mol"), r.get("poses"), r.get("ok"), flush=True)

with open("/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-074-steroidal-2026-11-16.json", "w") as f:
    json.dump(out, f, indent=1)
print("SAVED", flush=True)
