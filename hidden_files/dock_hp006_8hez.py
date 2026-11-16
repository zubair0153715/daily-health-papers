"""Control docking for HP-006 (SGLT2): the pipeline found NO X-ray structure
(X-ray only, <3.0 A), so pipeline docking was SKIPPED (no_pdb_found).
Control: dock on 8HEZ, the 2.8 A cryo-EM structure of human SGLT2-MAP17
bound to dapagliflozin itself (Nat Struct Mol Biol 2024;31:159-169).
Centre from the bound dapagliflozin via D._ligand_center, VERIFIED by
computing HETATM group centroids directly from the PDB file (the first
HETATM group may be NAG, not dapagliflozin -- see Paper #66 lesson).
Same Vina protocol (box 22.5, exhaustiveness 8, best of 3 poses).
Compounds: QUERY (dapagliflozin) + top 4 leads from the pipeline JSON.
CHEMBL429910 is dapagliflozin itself (same MW/logP, IC50 0.49 nM) -- a
duplicate-reproducibility check like Paper #64's olaparib pair.
Plus empagliflozin (SMILES from PubChem by name) as an approved-drug
comparison.
"""
import json
import sys
import urllib.request
import urllib.parse
from collections import defaultdict

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

LEADS = json.load(open("/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-006-2026-11-16.json"))["leads"]
by_label = {l["label"]: l for l in LEADS}

pdb_path = D._pdb_path("8HEZ")
center = D._ligand_center(pdb_path)
print("8HEZ D._ligand_center:", center, flush=True)

# Verify: group centroids from the PDB file itself.
groups = defaultdict(list)
with open(pdb_path) as f:
    for line in f:
        if line.startswith("HETATM"):
            res = line[17:20].strip()
            chain = line[21]
            resseq = line[22:26].strip()
            key = (res, chain, resseq)
            x, y, z = float(line[30:38]), float(line[38:46]), float(line[46:54])
            groups[key].append((x, y, z))
for key, pts in sorted(groups.items()):
    n = len(pts)
    c = [round(sum(p[i] for p in pts) / n, 2) for i in range(3)]
    print("  group", key, "atoms", n, "centroid", c, flush=True)

out = {"pdb_id": "8HEZ", "center": center, "box_size": 22.5,
       "exhaustiveness": 8, "results": []}
for label in ["QUERY", "CHEMBL429910", "CHEMBL3703792", "CHEMBL3703868", "CHEMBL5288495"]:
    l = by_label[label]
    r = D.dock(l["smiles"], "8HEZ", center, box_size=22.5)
    r["label"] = label
    out["results"].append(r)
    print("  DOCK:", label, r.get("affinity_kcal_mol"), r.get("poses"), r.get("ok"), flush=True)

url = ("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
       + urllib.parse.quote("empagliflozin") + "/property/SMILES/JSON")
with urllib.request.urlopen(url, timeout=60) as resp:
    smi = json.load(resp)["PropertyTable"]["Properties"][0]["SMILES"]
r = D.dock(smi, "8HEZ", center, box_size=22.5)
r["label"] = "empagliflozin"
out["results"].append(r)
print("  DOCK: empagliflozin", r.get("affinity_kcal_mol"), r.get("poses"), r.get("ok"), flush=True)

with open("/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-006-8hez-2026-11-16.json", "w") as f:
    json.dump(out, f, indent=1)
print("SAVED", flush=True)
