"""Corrected re-dock for HP-048 (TNF-alpha).

The pipeline auto-picked PDB 5UUI (1.4 A) — a spin-labelled TNF MONOMER whose
only ligand is the MTSL spin label MTN on Cys77. The small-molecule TNF
pocket is the trimer-interface cavity, which does not exist in a monomer, so
those scores were discarded (raw JSON kept as
dock-HP-048-WRONG-CENTRE-2026-11-09.json).

This script re-docks the same 5 leads with the identical Vina protocol
(Vina 1.2.7, 22.5 A box, exhaustiveness 8, best of 3 poses) on PDB 2AZ5
(TNF-alpha trimer + SPD304, 2.10 A), centre = SPD304 (ligand 307) centroid
[-13.87, 71.43, 26.91], verified 0.24 A from the oligomer CA centroid.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402

SRC = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-048-WRONG-CENTRE-2026-11-09.json"
OUT = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-048-CORRECTED-2026-11-09.json"

CENTER = [-13.87, 71.43, 26.91]
PDB = "2AZ5"

src = json.load(open(SRC))
leads = {l["label"]: l for l in src["leads"]}
labels = ["CHEMBL3642435", "CHEMBL3642496", "CHEMBL3642511", "CHEMBL3640299", "CHEMBL3640298"]

results = []
for lab in labels:
    r = D.dock(leads[lab]["smiles"], PDB, CENTER, box_size=22.5)
    r["label"] = lab
    r["rank"] = leads[lab]["rank"]
    results.append(r)
    print("DOCK:", lab, r.get("affinity_kcal_mol"), r.get("ok"), flush=True)

results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
out = dict(src)
out["docking"] = {
    "ok": True,
    "pdb_id": PDB,
    "resolution": 2.1,
    "center": CENTER,
    "center_audit": "SPD304 (ligand 307) centroid, 0.24 A from oligomer CA centroid; trimer-interface pocket",
    "results": results,
}
out["notes"] = (
    "CORRECTED re-dock on 2AZ5. First run on 5UUI discarded: monomer + spin-label "
    "centre (see dock-HP-048-WRONG-CENTRE-2026-11-09.json). Etanercept (150 kDa "
    "biologic) cannot be docked by Vina; it is the clinical reference only."
)
json.dump(out, open(OUT, "w"), indent=1)
print("SAVED:", OUT, flush=True)
