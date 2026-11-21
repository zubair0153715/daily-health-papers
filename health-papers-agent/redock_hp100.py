"""Re-dock for HP-100 (2026-11-21): deucravacitinib + 4 ChEMBL ligands on 6NZH.

CORRECTION — the pipeline docked the WRONG DOMAIN. Its PDB picker chose
3LXP, the TYK2 JH1 ATP-site structure (chains 888-1182), and returned
scores (-8.37 to -9.26 kcal/mol) for deucravacitinib binding a pocket it
never binds. Deucravacitinib is a JH2 allosteric inhibitor: it binds the
pseudokinase domain, not the JH1 ATP site. The 3LXP run is discarded in
full. This is the exact error the TYK2 centre audit in ~/AGENTS.md warns
about (JH2 = 6NZH chains 575-869; JH1 = 3LXP chains 888-1182).

This re-dock uses PDB 6NZH, the TYK2 JH2 (pseudokinase) domain in complex
with compound_40 (ligand L9A), 2.73 A. Centre = centroid of the
co-crystallised L9A, computed with dock._ligand_center (audit).
Caveat stated in the paper: 6NZH is NOT the deucravacitinib structure —
no public deucravacitinib-bound TYK2 crystal structure exists — so
deucravacitinib's score here is a cross-dock into the compound_40 pocket,
and there is no self-dock control for this paper.

Compounds (all from the P29597 ChEMBL run, measured potencies attached):
- deucravacitinib (QUERY; non-deuterated SMILES as returned by PubChem —
  the approved drug carries a trideuteriomethyl group, MW 425.5 vs 422.45
  here; heavy-atom structure identical, docking unaffected)
- CHEMBL4435170 (Ki 0.02 nM), CHEMBL5419627 (Kd 0.028 nM),
  CHEMBL4789639 (Ki 0.02 nM), CHEMBL5424497 (Kd 0.019 nM)
Note the endpoint mix (Ki vs Kd) and the near-identical potencies
(0.019-0.028 nM): the set cannot test ranking by measured potency.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

CENTER = [13.305595744680852, -2.7754042553191485, 29.741042553191487]
PDB = "6NZH"
OUT = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-100-redock-2026-11-21.json"

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
        json.dump({"pdb_id": PDB, "center": CENTER, "resolution": 2.73,
                   "note": "6NZH TYK2 JH2 + compound_40 (L9A); centre = L9A centroid via dock._ligand_center; deucravacitinib cross-docked (no public deucravacitinib-bound TYK2 structure exists)",
                   "results": results}, f, indent=1)

print("DONE", flush=True)
