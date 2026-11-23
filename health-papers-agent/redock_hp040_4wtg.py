"""Re-dock for HP-040 (2026-11-22): sofosbuvir + 4 ChEMBL NS5B ligands on 4WTG.

CORRECTION — the pipeline resolved the target correctly (Q8JXU8 ->
CHEMBL5375, 52 bioactivities) but its PDB picker found NO structure for
Q8JXU8 (no_pdb_found), so docking was skipped. The benchmark structure is
4WTG: HCV NS5B genotype 2a JFH-1 in complex with sofosbuvir diphosphate
(GS-607596, ligand 6GS), Mn2+ and primer/template RNA, 2.9 A
(Appleby et al., Science 2015). Centre = centroid of the co-crystallised
6GS, computed with dock._ligand_center (audit) — the receptor prep keeps
the RNA primer/template ATOM records, so the nucleotide pocket is
realistic. Sofosbuvir is docked as the parent prodrug SMILES from PubChem;
the crystal holds its diphosphate metabolite (GS-607596), and the active
form in cells is the triphosphate GS-461203 — that distinction is stated
in the paper, not smoothed over. The four ChEMBL ligands have measured
EC50/IC50 but no annotated binding site in ChEMBL: most NS5B ligands are
either nucleosides (active site) or non-nucleoside inhibitors (thumb/palm
allosteric sites ~35 A away), so an active-site score for an NNI is a
screen result, not a mechanism claim — stated in the paper.
"""
import json
import sys
from collections import defaultdict

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

PDB = "4WTG"
OUT = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-040-4wtg-2026-11-22.json"

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
print("CENTRE (6GS centroid via dock._ligand_center):", CENTER)

pipe = json.load(open("/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-040-2026-11-22.json"))
by_label = {l["label"]: l for l in pipe["leads"]}

jobs = [
    ("sofosbuvir (reference)", by_label["QUERY"]["smiles"]),
    ("CHEMBL5799441 (EC50 330 nM)", by_label["CHEMBL5799441"]["smiles"]),
    ("CHEMBL109569 (IC50 2250 nM)", by_label["CHEMBL109569"]["smiles"]),
    ("CHEMBL6047888 (EC50 690 nM)", by_label["CHEMBL6047888"]["smiles"]),
    ("CHEMBL5815143 (EC50 53 nM)", by_label["CHEMBL5815143"]["smiles"]),
]

results = []
for label, smi in jobs:
    print("DOCKING:", label, flush=True)
    r = D.dock(smi, PDB, CENTER, box_size=22.5)
    r["label"] = label
    print("  ->", r.get("affinity_kcal_mol"), r.get("poses"), r.get("ok"),
          flush=True)
    results.append(r)
    with open(OUT, "w") as f:
        json.dump({"pdb_id": PDB, "center": CENTER, "resolution": 2.9,
                   "note": ("4WTG HCV NS5B genotype 2a JFH-1 + sofosbuvir "
                            "diphosphate GS-607596 (6GS) + RNA primer/template, "
                            "2.9 A; centre = 6GS centroid via "
                            "dock._ligand_center; sofosbuvir docked as parent "
                            "prodrug SMILES (crystal holds diphosphate, active "
                            "form is triphosphate GS-461203)"),
                   "results": results}, f, indent=1)
print("SAVED:", OUT)
