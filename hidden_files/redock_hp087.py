"""Salvage dock for HP-087 (influenza PA endonuclease, 5IEQ):
ChEMBL PA ligands are all >1686 Da and failed conformer generation, so
dock two literature comparators on the same 5IEQ centre as baloxavir acid:
L-742,001 (diketo-acid PA endonuclease inhibitor) and EBSI-747 (the
co-crystallised fragment, 1CI). SMILES fetched live from PubChem.
"""
import json, sys, urllib.request, urllib.parse
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

CENTER = [-29.61, -45.19, 62.49]
PDB = "5IEQ"

def pubchem_smiles(name):
    q = urllib.parse.quote(name)
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{q}/property/SMILES,ConnectivitySMILES,IUPACName,MolecularFormula/JSON"
    with urllib.request.urlopen(url, timeout=60) as r:
        d = json.load(r)
    p = d["PropertyTable"]["Properties"][0]
    return p

out = {"pdb_id": PDB, "center": CENTER, "box_size": 22.5, "exhaustiveness": 8, "results": []}
for name in ["174605-64-2", "1-(4-chlorophenyl)-1H-imidazole"]:
    p = pubchem_smiles(name)
    smi = p.get("SMILES") or p.get("ConnectivitySMILES")
    # desalt: keep the largest fragment (drops e.g. ".Cl" from an HCl salt)
    smi = max(smi.split("."), key=len)
    print("PUBCHEM:", name, "->", p.get("MolecularFormula"), smi, flush=True)
    r = D.dock(smi, PDB, CENTER, box_size=22.5)
    r["label"] = {"174605-64-2": "L-742,001"}.get(name, name)
    r["smiles"] = smi
    r["formula"] = p.get("MolecularFormula")
    out["results"].append(r)
    print("  DOCK:", name, r.get("affinity_kcal_mol"), r.get("ok"), r.get("error"), flush=True)

with open("hidden_files/dock-HP-087b-2026-11-19.json", "w") as f:
    json.dump(out, f, indent=1)
print("RAW_SAVED: hidden_files/dock-HP-087b-2026-11-19.json")
