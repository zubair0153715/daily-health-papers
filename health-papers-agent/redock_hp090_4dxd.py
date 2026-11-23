"""Re-dock for HP-090 (2026-11-23): PC190723 on 4DXD.

CORRECTION — the pipeline resolved the target correctly to UniProt
P0A029 (S. aureus FtsZ, Mu50) but then resolved ChEMBL to CHEMBL2074,
verified live as human maltase-glucoamylase — the WRONG target — so
ChEMBL returned 0 bioactivities and there is no comparison set. Worse,
the pipeline's PDB picker selected 3VOA, verified live as the GDP-form
of SaFtsZ (Matsui et al., Acta Crystallogr D 2012; PMID 22948918): the
centre it used is the GDP nucleotide site, NOT the PC190723 interdomain
cleft. PC190723 binds the cleft between the N- and C-terminal
subdomains (the taxol-site equivalent in tubulin), ~25 A from the GTP
site. The pipeline's -8.83 kcal/mol score on 3VOA is therefore a docking
into the nucleotide pocket and is discarded here as a measurement of
the wrong site; it is reported only as the artefact, never as a result.

The benchmark structure is 4DXD: the 2.0 A crystal structure of S.
aureus FtsZ in complex with PC190723 (Tan et al., Sci Transl Med 2012;
PMID 22440737; doi 10.1126/scitranslmed.3003592). Centre = centroid of
the co-crystallised PC190723, computed with dock._ligand_center (audit).
"""
import json
import sys
from collections import defaultdict

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

PDB = "4DXD"
OUT = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-090-4dxd-2026-11-23.json"

# --- centre audit: which HETATM group does _ligand_center pick? ---
pdb_path = D._pdb_path(PDB)
groups = defaultdict(list)
with open(pdb_path) as f:
    for line in f:
        if line.startswith("HETATM"):
            res = (line[17:20].strip(), line[21].strip(), line[22:26].strip())
            groups[res].append((float(line[30:38]), float(line[38:46]),
                                float(line[46:54])))
print("HETATM groups:", {k: len(v) for k, v in groups.items()})
CENTER = D._ligand_center(pdb_path)
print("CENTRE (PC190723 centroid via dock._ligand_center):", CENTER)

pipe = json.load(open("/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-090-2026-11-23.json"))
by_label = {l["label"]: l for l in pipe["leads"]}

results = []
label = "PC190723 (reference)"
print("DOCKING:", label, flush=True)
r = D.dock(by_label["QUERY"]["smiles"], PDB, CENTER, box_size=22.5)
r["label"] = label
print("  ->", r.get("affinity_kcal_mol"), r.get("poses"), r.get("ok"), flush=True)
results.append(r)

json.dump({
    "pdb_id": PDB,
    "resolution_A": 2.0,
    "center": CENTER,
    "discarded_pipeline_structure": {
        "pdb_id": "3VOA",
        "reason": "GDP-form SaFtsZ; centre used was the GDP nucleotide site, not the PC190723 interdomain cleft; pipeline score -8.83 kcal/mol is a docking into the wrong site",
        "reference": "Matsui et al., Acta Crystallogr D Biol Crystallogr 2012;68:1175-1188; PMID 22948918",
    },
    "discarded_chembl_target": {
        "chembl_id": "CHEMBL2074",
        "reason": "human maltase-glucoamylase, not S. aureus FtsZ; zero bioactivities returned",
    },
    "results": results,
}, open(OUT, "w"), indent=1)
print("SAVED:", OUT)
