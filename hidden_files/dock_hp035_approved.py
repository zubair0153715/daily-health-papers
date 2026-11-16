"""Dock the approved PARP inhibitors + saruparib on the same PARP1 structure
(6NRH, centre from D._ligand_center) as run_docking.py used for HP-035,
so the paper can test the trapping-order hypothesis on one protocol.

SMILES are fetched live from PubChem PUG REST by name (never hand-typed).
Docking uses app.discovery.dock.dock with the same defaults as run_docking:
box 22.5, exhaustiveness 8, best of 3 poses.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D
from app.discovery.sources import _get

NAMES = ["talazoparib", "niraparib", "rucaparib", "veliparib", "saruparib"]
CENTER = [24.89, -8.82, 8.70]
PDB = "6NRH"

out = {"pdb_id": PDB, "center": CENTER, "box_size": 22.5,
       "exhaustiveness": 8, "results": []}
for name in NAMES:
    try:
        d = _get("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
                 + name + "/property/IsomericSMILES,CanonicalSMILES/JSON")
        props = d["PropertyTable"]["Properties"][0]
        smiles = (props.get("IsomericSMILES") or props.get("SMILES")
                  or props.get("CanonicalSMILES")
                  or props.get("ConnectivitySMILES"))
        cid = props.get("CID")
    except Exception as e:
        print("PUBCHEM FAIL:", name, e, flush=True)
        out["results"].append({"label": name, "ok": False,
                               "error": "pubchem_fetch_failed: %s" % e})
        continue
    print("SMILES:", name, "CID", cid, smiles, flush=True)
    r = D.dock(smiles, PDB, CENTER, box_size=22.5)
    r["label"] = name
    r["pubchem_cid"] = cid
    r["smiles"] = smiles
    out["results"].append(r)
    print("  DOCK:", name, r.get("affinity_kcal_mol"), r.get("ok"), flush=True)

with open("/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-035-approved-2026-11-16.json", "w") as f:
    json.dump(out, f, indent=1)
print("SAVED", flush=True)
