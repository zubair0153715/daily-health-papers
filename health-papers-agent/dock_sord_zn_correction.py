"""Corrected SORD docking for HP-054 (2026-11-14).

Why: run_docking.py's auto-pick chose 1PL8 (human SORD/NAD+ complex,
1.90 A) — the best SORD structure available — but 1PL8 contains NO
drug-like ligand, only NAD+ (cofactor), Zn2+ and waters. The pipeline's
_ligand_center therefore fell back to its cofactor behaviour and centred
the box on the NAD+ centroid, 11.62 A from the catalytic Zn2+ — the
substrate/inhibitor pocket sits at the edge of that box. The correct
centre for inhibitor docking is the catalytic Zn2+ (chain A), next to
which the nicotinamide ring sits (6 NAD atoms within 8 A of Zn-A) and
where sorbitol binds. No inhibitor-bound SORD structure exists in the
PDB (only 1PL6/1PL7/1PL8, all NAD+ complexes, Pauly et al. 2003), so
there is no co-crystallised-ligand centre to use instead.

This script docks the same top-5 pipeline leads + CP-166572 (QUERY) on
1PL8 centred on Zn-A [94.58, 35.23, 36.71], box 22.5 A, and writes
dock-HP-054-2026-11-14-Zn.json. The NAD-centred run from
run_docking.py is kept for comparison. Limitation, stated in the paper:
the receptor prep drops HETATM records, so the catalytic Zn2+ itself
is NOT in the docked receptor — scores are for the apo-pocket shape
only, with no metal coordination modelled.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402

BASE = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts"
MAIN = f"{BASE}/hidden_files/dock-HP-054-2026-11-14.json"
OUT = f"{BASE}/hidden_files/dock-HP-054-2026-11-14-Zn.json"

# Catalytic Zn2+, chain A, from 1PL8 HETATM ZN A 402.
CENTER = [94.58, 35.23, 36.71]


def main():
    with open(MAIN, encoding="utf-8") as f:
        main_json = json.load(f)
    leads = main_json.get("leads") or []
    top = leads[:5]
    q = next((l for l in leads if l.get("label") == "QUERY"), None)

    results = []
    for l in top:
        r = D.dock(l["smiles"], "1PL8", CENTER, box_size=22.5)
        r["label"] = l.get("label")
        r["rank"] = l.get("rank")
        r["measured_potency"] = (l.get("known_activity") or {}).get("activity")
        r["pains"] = l.get("pains")
        results.append(r)
        print("DOCK 1PL8-Zn:", r["label"], r.get("affinity_kcal_mol"),
              r.get("ok"), flush=True)
    if q and "QUERY" not in {r.get("label") for r in results}:
        r = D.dock(q["smiles"], "1PL8", CENTER, box_size=22.5)
        r["label"] = "QUERY"
        r["rank"] = q.get("rank")
        r["measured_potency"] = (q.get("known_activity") or {}).get("activity")
        r["pains"] = q.get("pains")
        results.append(r)
        print("DOCK-QUERY 1PL8-Zn:", r.get("affinity_kcal_mol"), flush=True)
    results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
    out = {
        "topic": {"target": "Sorbitol dehydrogenase (SORD)",
                  "reference": "CP-166572",
                  "topic_id": "HP-054", "date": "2026-11-14"},
        "docking": {
            "ok": True, "pdb_id": "1PL8", "resolution": 1.90,
            "center": CENTER,
            "center_note": ("catalytic Zn2+, chain A (HETATM ZN A 402); "
                            "nicotinamide ring within 8 A; substrate pocket"),
            "box_size": 22.5, "exhaustiveness": 8,
            "correction_note": ("run_docking.py auto-pick centred on the "
                                "NAD+ cofactor centroid (11.62 A from Zn); "
                                "this is the corrected Zn-centred docking. "
                                "Receptor prep drops HETATM, so Zn2+ is NOT "
                                "in the docked receptor (no metal "
                                "coordination modelled). No inhibitor-bound "
                                "SORD structure exists in the PDB."),
            "results": results,
        },
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("SAVED:", OUT, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
