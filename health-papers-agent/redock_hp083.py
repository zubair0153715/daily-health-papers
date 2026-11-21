"""Re-dock for HP-083 (2026-11-21): belzutifan + 4 ChEMBL analogues on 7W80.

CORRECTION — the pipeline's first run docked the WRONG target twice:
1. Target name "Hypoxia-inducible factor 2-alpha" resolved to UniProt Q9NWT6
   (HIF1AN / FIH-1, the asparaginyl hydroxylase), ChEMBL CHEMBL5909 — not
   HIF-2alpha. That run's docking (PDB 7A1Q, a FIH structure) is discarded.
2. Re-run with gene name "EPAS1" resolved correctly to UniProt Q99814
   (human HIF-2alpha, ChEMBL CHEMBL1744522, 44 bioactivities) but the
   pipeline's PDB picker chose 7Q5V — PHD2/EGLN1 in complex with
   N-oxalylglycine and a 20-residue HIF-2alpha CODD peptide. That is a PHD2
   structure, not the HIF-2alpha PAS-B pocket, so every score came back
   positive (+10.95 to +12.21 kcal/mol): the ligands clash with the PHD2
   active site. Also discarded.

This re-dock uses the correct structure: PDB 7W80, the HIF-2alpha-ARNT
heterodimer in complex with belzutifan (Ren et al., Mol Pharmacol 2022,
PMID 36167425), 2.75 A. Centre = centroid of the co-crystallised
belzutifan (residue 72Q), computed with dock._ligand_center (audit).
Caveat stated in the paper: 7W80 is the MOUSE heterodimer; no human
belzutifan-bound HIF-2alpha structure exists.

Compounds (all from the EPAS1 ChEMBL run, measured potencies attached):
- belzutifan (QUERY; CHEMBL4585668 in ChEMBL, IC50 9.0 nM, pChEMBL 8.05)
- CHEMBL5723338 (IC50 16.0 nM), CHEMBL4453227 (EC50 4.0 nM — note: EC50,
  not IC50), CHEMBL4173075 (IC50 8.5 nM), CHEMBL5764181 (IC50 11.0 nM)
All are the same belzutifan scaffold (difluoro-indanol methylsulfone
series); the set tests scaffold variation, not chemotype diversity.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

CENTER = [-13.027269230769232, -22.76523076923077, 21.719923076923074]
PDB = "7W80"
OUT = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-083-redock-2026-11-21.json"

pipe = json.load(open("/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-083-2026-11-21.json"))
by_label = {l["label"]: l for l in pipe["leads"]}

jobs = [
    ("belzutifan (reference; ChEMBL4585668, IC50 9.0 nM)", by_label["QUERY"]["smiles"]),
    ("CHEMBL5723338 (IC50 16.0 nM)", by_label["CHEMBL5723338"]["smiles"]),
    ("CHEMBL4453227 (EC50 4.0 nM)", by_label["CHEMBL4453227"]["smiles"]),
    ("CHEMBL4173075 (IC50 8.5 nM)", by_label["CHEMBL4173075"]["smiles"]),
    ("CHEMBL5764181 (IC50 11.0 nM)", by_label["CHEMBL5764181"]["smiles"]),
]

results = []
for label, smi in jobs:
    print("DOCKING:", label, flush=True)
    r = D.dock(smi, PDB, CENTER, box_size=22.5)
    r["label"] = label
    print("  ->", r.get("affinity_kcal_mol"), r.get("poses"), r.get("ok"), flush=True)
    results.append(r)
    with open(OUT, "w") as f:
        json.dump({"pdb_id": PDB, "center": CENTER, "resolution": 2.75,
                   "note": "7W80 mouse HIF-2alpha-ARNT + belzutifan; centre = 72Q centroid via dock._ligand_center",
                   "results": results}, f, indent=1)

print("DONE", flush=True)
