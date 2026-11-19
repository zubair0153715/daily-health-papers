"""Re-dock for HP-101 (RIPK1) on the KINASE domain structure 7FD0.
The pipeline auto-picked 6AC5 (RIPK1 DEATH DOMAIN, GlcNAcylated) and docked
GSK2982772-class kinase inhibitors onto a sugar - meaningless scores.
7FD0 is the human RIPK1 kinase domain (2.0 A) in complex with a
benzoxazepinone-triazole inhibitor of the same chemotype as GSK2982772.
Centre = co-crystallised ligand centroid via D._ligand_center.
"""
import json, sys
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

PDB = "7FD0"
src = json.load(open("hidden_files/dock-HP-101-2026-11-19.json"))
leads = {l["label"]: l for l in src["leads"]}
labels = [r["label"] for r in src["docking"]["results"]]
print("RE-DOCKING:", labels, flush=True)

pdb_path = D._pdb_path(PDB)
center = D._ligand_center(pdb_path)
print("PDB:", PDB, "center:", center, flush=True)
# verify the structure is the kinase domain
with open(pdb_path) as f:
    for line in f:
        if line.startswith(("HEADER", "TITLE", "COMPND")):
            print("  ", line.rstrip(), flush=True)
        if line.startswith("TITLE") and "2" in line[:10]:
            pass

out = {"pdb_id": PDB, "center": center, "box_size": 22.5, "exhaustiveness": 8, "results": []}
for lab in labels:
    smi = leads[lab]["smiles"]
    r = D.dock(smi, PDB, center, box_size=22.5)
    r["label"] = lab
    r["rank"] = leads[lab].get("rank")
    out["results"].append(r)
    print("  DOCK:", lab, r.get("affinity_kcal_mol"), r.get("ok"), r.get("error"), flush=True)

out["results"].sort(key=lambda x: x.get("affinity_kcal_mol", 999))
with open("hidden_files/dock-HP-101b-2026-11-19.json", "w") as f:
    json.dump(out, f, indent=1)
print("RAW_SAVED: hidden_files/dock-HP-101b-2026-11-19.json")
