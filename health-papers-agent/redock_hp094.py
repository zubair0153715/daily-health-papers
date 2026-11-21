"""Re-dock for HP-094 (2026-11-21): TAM16 + 4 ChEMBL analogues on 5V3Y.

CORRECTION — the pipeline docked the WRONG DOMAIN. Its PDB picker chose
6C4Q, the Pks13 ACP domain (residues 1-100), 1.16 A, and returned scores
(-8.41 to -8.90 kcal/mol) for TAM16 binding a domain it never binds.
TAM16 inhibits the thioesterase (TE) domain. The 6C4Q run is discarded
in full. (Same failure class as the TYK2 JH1/JH2 error earlier today:
highest resolution is not the right domain.)

This re-dock uses PDB 5V3Y, the Mtb Pks13 thioesterase domain in complex
with TAM16 (ligand 5V8), 1.98 A (Aggarwal et al., Cell 2017). Centre =
centroid of the co-crystallised 5V8, computed with dock._ligand_center
(audit). TAM16 is therefore the self-dock control on its own structure.

Compounds (all from the I6X8D2 ChEMBL run, measured potencies attached):
- TAM16 (QUERY; ChEMBL4443524 in ChEMBL, IC50 190 nM)
- CHEMBL5070158 (IC50 330 nM), CHEMBL5074531 (IC50 180 nM),
  CHEMBL5270146 (IC50 290 nM)
NOTE: every compound in this set — including TAM16 itself — carries an
RDKit PAINS alert (the aminomethyl-phenol Mannich-base motif). The alert
is reported, not hidden; it changes the validation design (see paper).
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

CENTER = [4.796571428571428, 26.285714285714285, 7.4812142857142865]
PDB = "5V3Y"
OUT = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-094-redock-2026-11-21.json"

pipe = json.load(open("/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-094-2026-11-21.json"))
by_label = {l["label"]: l for l in pipe["leads"]}

jobs = [
    ("TAM16 (reference; ChEMBL4443524, IC50 190 nM)", by_label["QUERY"]["smiles"]),
    ("CHEMBL4443524 (TAM16 in ChEMBL, IC50 190 nM)", by_label["CHEMBL4443524"]["smiles"]),
    ("CHEMBL5070158 (IC50 330 nM)", by_label["CHEMBL5070158"]["smiles"]),
    ("CHEMBL5074531 (IC50 180 nM)", by_label["CHEMBL5074531"]["smiles"]),
    ("CHEMBL5270146 (IC50 290 nM)", by_label["CHEMBL5270146"]["smiles"]),
]

results = []
for label, smi in jobs:
    print("DOCKING:", label, flush=True)
    r = D.dock(smi, PDB, CENTER, box_size=22.5)
    r["label"] = label
    print("  ->", r.get("affinity_kcal_mol"), r.get("poses"), r.get("ok"), flush=True)
    results.append(r)
    with open(OUT, "w") as f:
        json.dump({"pdb_id": PDB, "center": CENTER, "resolution": 1.98,
                   "note": "5V3Y Mtb Pks13 TE domain + TAM16 (5V8); centre = 5V8 centroid via dock._ligand_center; all 5 compounds carry a PAINS alert (Mannich-base motif)",
                   "results": results}, f, indent=1)

print("DONE", flush=True)
