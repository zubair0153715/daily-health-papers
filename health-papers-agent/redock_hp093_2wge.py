"""Re-dock for HP-093 (2026-11-23): thiolactomycin on 2WGE.

CORRECTION — the pipeline resolved the target correctly to UniProt
P9WQD9 (M. tuberculosis KasA, H37Rv) but then resolved ChEMBL to
CHEMBL2074, verified live as human maltase-glucoamylase — the WRONG
target (the same fallback ID the pipeline returned for FtsZ in HP-090,
suggesting CHEMBL2074 is the pipeline's default when its ChEMBL search
fails) — so ChEMBL returned 0 bioactivities and there is no comparison
set. The pipeline's PDB picker selected 6P9K, verified live as Mtb
KasA in complex with O6G (JSF-3285, the preclinical indazole candidate;
Inoyama et al., Cell Chem Biol 2020; PMID 32197094) — the right
enzyme, but the co-crystallised ligand is a later, optimised indazole,
not thiolactomycin. The pipeline's -6.11 kcal/mol score for
thiolactomycin on 6P9K is a docking into the JSF-3285 pocket, not into
thiolactomycin's own pocket, and is reported here only as the artefact,
never as the control result.

The benchmark structure is 2WGE: the 1.80 A crystal structure of Mtb
KasA with bound thiolactomycin (TLM) (Luckner et al., Structure 2009;
PMID 19604480; doi 10.1016/j.str.2009.04.012). Centre = centroid of the
co-crystallised TLM, computed with dock._ligand_center (audit).
"""
import json
import sys
from collections import defaultdict

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

PDB = "2WGE"
OUT = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-093-2wge-2026-11-23.json"

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
print("CENTRE (TLM centroid via dock._ligand_center):", CENTER)

pipe = json.load(open("/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-093-2026-11-23.json"))
by_label = {l["label"]: l for l in pipe["leads"]}

results = []
label = "thiolactomycin (reference)"
print("DOCKING:", label, flush=True)
r = D.dock(by_label["QUERY"]["smiles"], PDB, CENTER, box_size=22.5)
r["label"] = label
print("  ->", r.get("affinity_kcal_mol"), r.get("poses"), r.get("ok"), flush=True)
results.append(r)

json.dump({
    "pdb_id": PDB,
    "resolution_A": 1.80,
    "center": CENTER,
    "discarded_pipeline_structure": {
        "pdb_id": "6P9K",
        "reason": "KasA in complex with O6G (JSF-3285), not thiolactomycin; pipeline score -6.11 kcal/mol is a docking into the JSF-3285 pocket, not thiolactomycin's own pocket",
        "reference": "Inoyama et al., Cell Chem Biol 2020;27:560; PMID 32197094",
    },
    "discarded_chembl_target": {
        "chembl_id": "CHEMBL2074",
        "reason": "human maltase-glucoamylase, not M. tuberculosis KasA; zero bioactivities returned (same fallback ID as HP-090)",
    },
    "results": results,
}, open(OUT, "w"), indent=1)
print("SAVED:", OUT)
