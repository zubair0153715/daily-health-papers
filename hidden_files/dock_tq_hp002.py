"""Extra dock for Paper #45 (HP-002): thymoquinone on the same 9F7W protocol.

Thymoquinone was NOT in the pipeline's ChEMBL top-26 (similarity screen vs
pioglitazone), so it is docked here separately, with the identical grid
centre [47.1, 6.91, 1.39] and box 22.5 used for the pioglitazone comparison,
plus an RDKit PAINS screen. PubChem CID verified live before docking.
"""
import json
import sys
import urllib.request

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402

TQ_SMILES = "CC(C)C1=CC(=O)C(C)=CC1=O"

# Verify identity via PubChem PUG REST (CID 10281 should be Thymoquinone).
with urllib.request.urlopen(
    "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/10281/property/"
    "Title,IUPACName,MolecularFormula/JSON",
    timeout=30,
) as r:
    props = json.load(r)["PropertyTable"]["Properties"][0]
print("PUBCHEM:", props)
assert "hymoquinone" in props["Title"], props

r = D.dock(TQ_SMILES, "9F7W", [47.1, 6.91, 1.39], box_size=22.5)
r["label"] = "THYMOQUINONE"
print("TQ DOCK:", r)

# PAINS screen via the pipeline's own helper (same filter as the leads).
from app.discovery.chem import pains as pains_fn

hits = pains_fn(TQ_SMILES)
print("TQ PAINS:", hits)

out = {
    "compound": "thymoquinone",
    "pubchem_cid": 10281,
    "smiles": TQ_SMILES,
    "pdb_id": "9F7W",
    "center": [47.1, 6.91, 1.39],
    "box_size": 22.5,
    "dock": r,
    "pains": hits,
}
with open(
    "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/"
    "hidden_files/dock-HP-002-2026-11-11-TQ.json",
    "w",
    encoding="utf-8",
) as f:
    json.dump(out, f, indent=1)
print("SAVED")
