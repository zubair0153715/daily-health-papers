"""Corrected HP-003 (PTP1B / ertiprotafib) docking, 2026-11-12.

FAULT in the first run (dock-HP-003-2026-11-12.json): the pipeline's
structure picker (find_pdb_for_uniprot, resolution-sorted UniProt PDB
xrefs, X-ray <3.0 A) picked 9C66 (1.4 A) — "Structure of the MENA EVH1
domain bound to the polyproline segment of PTP1B". PTP1B appears in
9C66 only as a peptide (chain B, residues 304-313); the structure is
the MENA EVH1 domain. The grid centre landed on CSO A7, a modified
cysteine of the EVH1 domain (verified against the 9C66 file), not the
PTP1B active site. The first run's docking scores (-6.0 to -7.07) are
for ligands docked into the MENA EVH1 domain and are INVALID for
PTP1B; they are kept in the original JSON for audit and discarded.

CORRECTION: re-dock the IDENTICAL ligand set (top 5 pipeline entries:
QUERY ertiprotafib + the 4 leads) on 2F71 — "PTP1B with sulfamic acid
inhibitors", catalytic domain residues 2-298, 1.55 A — with the grid
centred on the co-crystallised inhibitor UN7 (42 atoms) centroid
[39.94, 9.94, 14.68], verified with the pipeline's own _ligand_center
(distance 0.005 A from the reported centre). UN7's nearest atom is
3.39 A from the catalytic Cys215 SG, confirming the active site.
Same LeadForge D.dock protocol (Vina 1.2.7, 22.5 A box,
exhaustiveness 8, 3 poses). 8G65 was audited and rejected (its YW9
ligand sits 51.45 A from Cys215 SG, i.e. not the catalytic site);
1XBO and 2QBS were valid alternates (nearest atoms 3.64 / 3.85 A).
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

CENTER = [39.94, 9.94, 14.68]
PDB = "2F71"

src = json.load(open("../hidden_files/dock-HP-003-2026-11-12.json"))
leads = src.get("leads") or []
dock_set = leads[:5]  # QUERY + top 4 leads, exactly as the first run docked
print("DOCK SET:", [l["label"] for l in dock_set], flush=True)
print("CENTRE: UN7 (sulfamic acid inhibitor) centroid in 2F71,", CENTER,
      flush=True)

results = []
for l in dock_set:
    r = D.dock(l["smiles"], PDB, CENTER, box_size=22.5)
    r["label"] = l["label"]
    r["rank"] = l.get("rank")
    results.append(r)
    print("  DOCK 2F71:", l["label"], r.get("affinity_kcal_mol"),
          r.get("ok"), flush=True)
results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))

src["docking_corrected"] = {"ok": True, "pdb_id": PDB,
                            "resolution": 1.55, "center": CENTER,
                            "results": results}
src["correction"] = {
    "fault": ("first run docked on 9C66 (MENA EVH1 domain; PTP1B only "
              "as a peptide, chain B residues 304-313); grid centre was "
              "CSO A7, a modified cysteine of the EVH1 domain, not the "
              "PTP1B active site"),
    "fix": ("re-docked identical ligand set on 2F71 (PTP1B catalytic "
            "domain 2-298, 1.55 A) at the UN7 inhibitor centroid "
            "[39.94, 9.94, 14.68]; UN7 nearest atom 3.39 A from "
            "catalytic Cys215 SG"),
    "original_docking_kept_for_audit": "docking field in dock-HP-003-2026-11-12.json",
}
out = "../hidden_files/dock-HP-003c-2026-11-12.json"
with open(out, "w") as f:
    json.dump(src, f, indent=1)
print("RAW_SAVED:", out, flush=True)
