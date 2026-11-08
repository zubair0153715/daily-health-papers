"""Corrected HP-026 (S. mansoni TGR) docking, 2026-11-08.

FAULT in the first run (dock-HP-026-2026-11-08.json): PDB 8PDD (SmTGR,
1.25 A) holds NO drug-like ligand — only the FAD cofactor, Mg ions and
glycerols. _ligand_center's fallback (first >=6-atom group when nothing
survives exclusions) landed on the FAD cofactor centroid
[7.30, -2.84, 57.31] — 5.22 A from the catalytic site. The original
box still covered the redox site (22.5 A box), but the centre was the
cofactor, not the drug site.

CORRECTION: re-dock the identical ligand set (top 5 pipeline leads +
praziquantel query) on 8PDD with the grid centred on the catalytic
redox site — the midpoint between the FAD isoalloxazine-ring centroid
[6.23, -4.20, 52.39] and the Cys154-Cys159 disulfide SG midpoint
[10.33, -4.84, 50.80] = [8.28, -4.52, 51.60]. Both points verified
against the 8PDD PDB file (Cys154 SG 4.59 A and Cys159 SG 3.22 A from
FAD). Same LeadForge D.dock protocol (Vina 1.2.7, 22.5 A box,
exhaustiveness 8, 3 poses).

Praziquantel is NOT a TGR inhibitor (different target) — it is docked
as a negative control and the paper states this.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

CENTER = [8.28, -4.52, 51.60]
PDB = "8PDD"

src = json.load(open("../hidden_files/dock-HP-026-2026-11-08.json"))
leads = src.get("leads") or []
q = next((l for l in leads if l.get("label") == "QUERY"), None)
top = [l for l in leads if l.get("label") != "QUERY"][:5]
dock_set = top + ([q] if q else [])
print("DOCK SET:", [l["label"] for l in dock_set], flush=True)
print("CENTRE: catalytic redox site (isoalloxazine/Cys154-Cys159 midpoint)",
      CENTER, flush=True)

results = []
for l in dock_set:
    r = D.dock(l["smiles"], PDB, CENTER, box_size=22.5)
    r["label"] = l["label"]
    r["rank"] = l.get("rank")
    results.append(r)
    print("  DOCK 8PDD:", l["label"], r.get("affinity_kcal_mol"), r.get("ok"),
          flush=True)
results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))

src["docking_corrected"] = {"ok": True, "pdb_id": PDB, "center": CENTER,
                            "results": results}
src["correction"] = {
    "fault": ("first run centred the grid on the FAD cofactor centroid "
              "[7.30, -2.84, 57.31] (8PDD has no drug-like ligand; "
              "_ligand_center fallback picked FAD)"),
    "fix": ("re-docked identical ligand set at the catalytic redox site "
            "[8.28, -4.52, 51.60], midpoint of FAD isoalloxazine centroid "
            "and Cys154-Cys159 disulfide, both verified in the 8PDD file"),
    "original_docking_kept_for_audit": "docking field in dock-HP-026-2026-11-08.json",
}
out = "../hidden_files/dock-HP-026c-2026-11-08.json"
with open(out, "w") as f:
    json.dump(src, f, indent=1)
print("RAW_SAVED:", out, flush=True)
