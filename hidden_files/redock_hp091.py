"""Salvage dock for HP-091 (OXA-23, 4JF5):
ChEMBL OXA-23 has only 2 bioactivities: avibactam itself, and a 0.74 nM
boronate (CHEMBL4633785) that Vina cannot score (boron atom type
unsupported). Dock durlobactam - the approved DBO OXA inhibitor - on the
same 4JF5 centre as avibactam. SMILES fetched live from PubChem.
"""
import json, sys, urllib.request, urllib.parse
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

CENTER = [-26.15, -22.08, 8.55]
PDB = "4JF5"

def pubchem_smiles(name):
    q = urllib.parse.quote(name)
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{q}/property/SMILES,ConnectivitySMILES,IUPACName,MolecularFormula/JSON"
    with urllib.request.urlopen(url, timeout=60) as r:
        d = json.load(r)
    return d["PropertyTable"]["Properties"][0]

out = {"pdb_id": PDB, "center": CENTER, "box_size": 22.5, "exhaustiveness": 8, "results": []}
for name in ["durlobactam"]:
    p = pubchem_smiles(name)
    smi = p.get("SMILES") or p.get("ConnectivitySMILES")
    smi = max(smi.split("."), key=len)
    print("PUBCHEM:", name, "->", p.get("MolecularFormula"), smi, flush=True)
    r = D.dock(smi, PDB, CENTER, box_size=22.5)
    r["label"] = name
    r["smiles"] = smi
    r["formula"] = p.get("MolecularFormula")
    out["results"].append(r)
    print("  DOCK:", name, r.get("affinity_kcal_mol"), r.get("ok"), r.get("error"), flush=True)

with open("hidden_files/dock-HP-091b-2026-11-19.json", "w") as f:
    json.dump(out, f, indent=1)
print("RAW_SAVED: hidden_files/dock-HP-091b-2026-11-19.json")
