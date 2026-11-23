"""Re-dock for HP-088 (2026-11-23): doravirine on 7Z2G.

CORRECTION — the pipeline resolved the target to UniProt P03366 (Gag-Pol
polyprotein) and ChEMBL CHEMBL5823, but ChEMBL returned 0 bioactivities
for CHEMBL5823, so there is no comparison ligand set. Worse, the
pipeline's PDB picker then selected 2HS1 — verified live 2026-11-23 as
the ultra-high-resolution (0.84 A) crystal structure of HIV-1 PROTEASE
(V32I mutant) with darunavir (TMC114) (Kovalevsky et al., J Mol Biol
2006; PMID 16962136) — NOT reverse transcriptase. The pipeline's
doravirine score of -9.3 kcal/mol on 2HS1 is therefore a docking into
the protease active site and is MEANINGLESS for the RT question; it is
reported here only as the discarded artefact, never as a result.

The benchmark structure is 7Z2G: cryo-EM (3.65 A) structure of wild-type
HIV-1 RT with a DNA aptamer in complex with doravirine (Singh et al.,
PNAS 2022; PMID 35858448; doi 10.1073/pnas.2203660119). Centre = centroid
of the co-crystallised doravirine, computed with dock._ligand_center
(audit) — the receptor prep keeps the DNA aptamer ATOM records, so the
NNRTI pocket is realistic. Doravirine is docked as the parent SMILES
from PubChem (CID 58460047); the crystal holds the same molecule.
"""
import json
import sys
from collections import defaultdict

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

PDB = "7Z2G"
OUT = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-088-7z2g-2026-11-23.json"

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
print("CENTRE (doravirine centroid via dock._ligand_center):", CENTER)

pipe = json.load(open("/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-088-2026-11-23.json"))
by_label = {l["label"]: l for l in pipe["leads"]}

results = []
label = "doravirine (reference)"
print("DOCKING:", label, flush=True)
r = D.dock(by_label["QUERY"]["smiles"], PDB, CENTER, box_size=22.5)
r["label"] = label
print("  ->", r.get("affinity_kcal_mol"), r.get("poses"), r.get("ok"), flush=True)
results.append(r)

json.dump({
    "pdb_id": PDB,
    "resolution_A": 3.65,
    "center": CENTER,
    "discarded_pipeline_structure": {
        "pdb_id": "2HS1",
        "reason": "HIV-1 protease (V32I) + darunavir, not reverse transcriptase; pipeline score -9.3 kcal/mol on 2HS1 is invalid for the RT question",
        "reference": "Kovalevsky et al., J Mol Biol 2006;363:161-173; PMID 16962136",
    },
    "results": results,
}, open(OUT, "w"), indent=1)
print("SAVED:", OUT)
