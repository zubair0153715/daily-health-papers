"""Re-dock for HP-063 (2026-11-23): avibactam + meropenem on 4WMC.

CORRECTION — the pipeline resolved the target correctly to UniProt
Q6XEC0 (OXA-48, K. pneumoniae) and ChEMBL CHEMBL1287604 (1
bioactivity), but its PDB picker selected 8PEB, verified live as
OXA-48_Q5 — a directed-evolution QUINTUPLE MUTANT (Frohlich et al.,
Nat Catal 2024; PMID 38828429), not wild-type OXA-48 — and the centre
it used is a malonate buffer ion (MLI, 9 atoms), the only drug-like
HETATM group in an apo structure. The pipeline's scores on 8PEB
(avibactam -6.27, meropenem -7.29) are therefore dockings into a mutant
enzyme centred on a buffer ion, and are reported here only as the
artefact, never as the control result.

The benchmark structure is 4WMC: the 2.3 A crystal structure of
wild-type OXA-48 in covalent complex with avibactam (Lahiri et al.,
ACS Chem Biol 2015; PMID 25406838; doi 10.1021/cb500703p). Centre =
centroid of the co-crystallised avibactam (ligand NXL, chain A res 301,
17 heavy atoms — C7H11N3O6S, matching avibactam), computed with
dock._ligand_center (audit). The file holds 8 OXA-48 chains, each with
its own NXL; the audit confirms _ligand_center returned chain A's NXL
centroid [42.21, 34.64, 52.56], not the group average.

HONEST LIMIT, stated up front: avibactam is a COVALENT inhibitor — it
acylates Ser70 and deacylates only slowly. Non-covalent Vina docking
cannot capture the covalent step; the scores here are a pre-acylation
encounter-complex proxy at best, and no non-covalent score can rank
covalent DBO inhibitors. Meropenem (CHEMBL127) is the carbapenem
SUBSTRATE, not an inhibitor — OXA-48 hydrolyses it — so its score is a
substrate-binding number, not an inhibition number.
"""
import json
import sys
from collections import defaultdict

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

PDB = "4WMC"
OUT = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-063-4wmc-2026-11-23.json"

# --- centre audit: which HETATM group does _ligand_center pick? ---
pdb_path = D._pdb_path(PDB)
groups = defaultdict(list)
with open(pdb_path) as f:
    for line in f:
        if line.startswith("HETATM"):
            res = (line[17:20].strip(), line[21].strip(), line[22:26].strip())
            groups[res].append((float(line[30:38]), float(line[38:46]),
                                float(line[46:54])))
print("HETATM groups (non-water):",
      {k: len(v) for k, v in groups.items() if k[0] != "HOH"})
CENTER = D._ligand_center(pdb_path)
print("CENTRE (NXL chain A centroid via dock._ligand_center):", CENTER)

pipe = json.load(open("/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-063-2026-11-23.json"))
by_label = {l["label"]: l for l in pipe["leads"]}

jobs = [
    ("avibactam (reference, covalent inhibitor)", by_label["QUERY"]["smiles"]),
    ("CHEMBL127 (meropenem, carbapenem substrate; Kd 850 nM)",
     by_label["CHEMBL127"]["smiles"]),
]

results = []
for label, smi in jobs:
    print("DOCKING:", label, flush=True)
    r = D.dock(smi, PDB, CENTER, box_size=22.5)
    r["label"] = label
    print("  ->", r.get("affinity_kcal_mol"), r.get("poses"), r.get("ok"),
          flush=True)
    results.append(r)

json.dump({
    "pdb_id": PDB,
    "resolution_A": 2.3,
    "center": CENTER,
    "discarded_pipeline_structure": {
        "pdb_id": "8PEB",
        "reason": "OXA-48_Q5 quintuple mutant, apo structure centred on a malonate buffer ion; pipeline scores avibactam -6.27 and meropenem -7.29 are dockings into a mutant enzyme, not wild-type OXA-48",
        "reference": "Frohlich et al., Nat Catal 2024;7:499-509; PMID 38828429",
    },
    "covalent_caveat": "avibactam acylates Ser70 covalently; non-covalent Vina scores are an encounter-complex proxy only and cannot rank covalent DBO inhibitors",
    "results": results,
}, open(OUT, "w"), indent=1)
print("SAVED:", OUT)
