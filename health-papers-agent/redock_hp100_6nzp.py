"""Self-dock for HP-100 (2026-11-21): deucravacitinib + 4 ChEMBL ligands on 6NZP.

6NZP is the TYK2 JH2 (pseudokinase) domain in complex with compound-11,
which IS deucravacitinib (BMS-986165; ligand LB7; Wrobleski et al.,
J Med Chem 2019, PMID 31318208) — 2.35 A. Centre = centroid of the
co-crystallised LB7, computed with dock._ligand_center (audit).
This is the self-dock control the 6NZH cross-dock lacked: deucravacitinib
re-docked on its own structure. The 6NZH run (compound_40 pocket) is
reported alongside as the confirmation.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

CENTER = D._ligand_center("/tmp/6NZP.pdb")
print("6NZP deucravacitinib (LB7) centroid:", CENTER)
PDB = "6NZP"
OUT = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-100-6nzp-2026-11-21.json"

pipe = json.load(open("/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-100-2026-11-21.json"))
by_label = {l["label"]: l for l in pipe["leads"]}

jobs = [
    ("deucravacitinib (reference)", by_label["QUERY"]["smiles"]),
    ("CHEMBL4435170 (Ki 0.02 nM)", by_label["CHEMBL4435170"]["smiles"]),
    ("CHEMBL5419627 (Kd 0.028 nM)", by_label["CHEMBL5419627"]["smiles"]),
    ("CHEMBL4789639 (Ki 0.02 nM)", by_label["CHEMBL4789639"]["smiles"]),
    ("CHEMBL5424497 (Kd 0.019 nM)", by_label["CHEMBL5424497"]["smiles"]),
]

results = []
for label, smi in jobs:
    print("DOCKING:", label, flush=True)
    r = D.dock(smi, PDB, CENTER, box_size=22.5)
    r["label"] = label
    print("  ->", r.get("affinity_kcal_mol"), r.get("poses"), r.get("ok"), flush=True)
    results.append(r)
    with open(OUT, "w") as f:
        json.dump({"pdb_id": PDB, "center": CENTER, "resolution": 2.35,
                   "note": "6NZH->6NZP: 6NZP is TYK2 JH2 + deucravacitinib (compound-11, LB7); centre = LB7 centroid via dock._ligand_center",
                   "results": results}, f, indent=1)

print("DONE", flush=True)
