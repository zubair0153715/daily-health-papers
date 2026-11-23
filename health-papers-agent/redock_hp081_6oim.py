"""Re-dock for HP-081 (2026-11-22): sotorasib + 4 ChEMBL KRAS ligands on 6OIM.

The pipeline resolved the target correctly (P01116 -> CHEMBL2189121, 51
bioactivities) and docked on its auto-pick, 9IAY (0.953 A GDP-KRAS in
complex with compound "10") — a cross-dock for sotorasib, since 9IAY
holds a different inhibitor. The benchmark structure is 6OIM: human
KRAS G12C covalently bound to AMG 510 (sotorasib), 1.65 A. Centre =
centroid of the co-crystallised sotorasib (HETATM MOV, 41 atoms),
computed with dock._ligand_center (audit). Sotorasib is therefore the
self-dock control on its own structure. CAVEAT: sotorasib and the four
analogues are covalent G12C inhibitors (acrylamide warhead to Cys12);
Vina scores only the non-covalent pose, so these numbers cannot capture
the covalent contribution to potency and must be read as pose scores,
not as affinity.
"""
import json
import sys
from collections import defaultdict

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

PDB = "6OIM"
OUT = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-081-6oim-2026-11-22.json"

pdb_path = D._pdb_path(PDB)
groups = defaultdict(list)
with open(pdb_path) as f:
    for line in f:
        if line.startswith("HETATM"):
            res = (line[17:20].strip(), line[21].strip(), line[22:26].strip())
            groups[res].append((float(line[30:38]), float(line[38:46]),
                                float(line[46:54])))
print("HETATM groups:", {k: len(v) for k, v in groups.items()
                          if k[0] != "HOH"})
CENTER = D._ligand_center(pdb_path)
print("CENTRE (sotorasib centroid via dock._ligand_center):", CENTER)

pipe = json.load(open("/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-081-2026-11-22.json"))
by_label = {l["label"]: l for l in pipe["leads"]}
top = [l for l in pipe["leads"] if l["label"] != "QUERY"][:4]
jobs = [("sotorasib (reference)", by_label["QUERY"]["smiles"])]
for l in top:
    act = (l.get("known_activity") or {})
    jobs.append((f"{l['label']} ({act.get('activity') or 'no activity'})",
                 l["smiles"]))
    print("JOB:", jobs[-1][0])

results = []
for label, smi in jobs:
    print("DOCKING:", label, flush=True)
    r = D.dock(smi, PDB, CENTER, box_size=22.5)
    r["label"] = label
    print("  ->", r.get("affinity_kcal_mol"), r.get("poses"), r.get("ok"),
          flush=True)
    results.append(r)
    with open(OUT, "w") as f:
        json.dump({"pdb_id": PDB, "center": CENTER, "resolution": 1.65,
                   "note": ("6OIM KRAS G12C + sotorasib (AMG 510), 1.65 A; "
                            "centre = sotorasib centroid via "
                            "dock._ligand_center; sotorasib is the "
                            "self-dock control on its own structure; "
                            "Vina scores non-covalent pose only — covalent "
                            "Cys12 bond not modelled"),
                   "results": results}, f, indent=1)
print("SAVED:", OUT)
