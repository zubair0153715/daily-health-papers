"""Corrected SORD docking for HP-054 (2026-11-14) — the 1PL6 run.

Why this run exists: run_docking.py auto-picked 1PL8 (1.90 A, the best
resolution) — but 1PL8 is an NAD+ complex with NO inhibitor. The
structurally correct choice is 1PL6 (2.00 A, "Human SDH/NADH/inhibitor
complex"): its ligand 572 is 4-[2-(hydroxymethyl)pyrimidin-4-yl]-N,N-
dimethylpiperazine-1-sulfonamide, formula C11H19N5O3S — i.e. CP-166572
itself, the reference compound of this paper, co-crystallised in the
substrate pocket 6.28 A from the catalytic Zn2+ (chain A). The pipeline
chose by resolution and missed the inhibitor-bound structure.

This script docks the same top-5 pipeline leads + CP-166572 (QUERY) on
1PL6 centred on the chain-A 572 centroid [102.75, 37.00, 35.25], box
22.5 A, and writes dock-HP-054-2026-11-14-1PL6.json. The QUERY dock is
the CP-166572 re-dock control (same molecule as the co-crystallised
ligand). Limitation, stated in the paper: the receptor prep drops
HETATM records, so the catalytic Zn2+ is NOT in the docked receptor —
no metal coordination is modelled, even on 1PL6.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402

BASE = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts"
MAIN = f"{BASE}/hidden_files/dock-HP-054-2026-11-14.json"
OUT = f"{BASE}/hidden_files/dock-HP-054-2026-11-14-1PL6.json"

# Chain-A ligand 572 (CP-166572) centroid, from 1PL6 HETATM records.
CENTER = [102.75, 37.00, 35.25]


def main():
    with open(MAIN, encoding="utf-8") as f:
        main_json = json.load(f)
    leads = main_json.get("leads") or []
    top = leads[:5]
    q = next((l for l in leads if l.get("label") == "QUERY"), None)

    results = []
    for l in top:
        r = D.dock(l["smiles"], "1PL6", CENTER, box_size=22.5)
        r["label"] = l.get("label")
        r["rank"] = l.get("rank")
        r["measured_potency"] = (l.get("known_activity") or {}).get("activity")
        r["pains"] = l.get("pains")
        results.append(r)
        print("DOCK 1PL6-572:", r["label"], r.get("affinity_kcal_mol"),
              r.get("ok"), flush=True)
    if q and "QUERY" not in {r.get("label") for r in results}:
        r = D.dock(q["smiles"], "1PL6", CENTER, box_size=22.5)
        r["label"] = "QUERY"
        r["rank"] = q.get("rank")
        r["measured_potency"] = (q.get("known_activity") or {}).get("activity")
        r["pains"] = q.get("pains")
        results.append(r)
        print("DOCK-QUERY 1PL6-572:", r.get("affinity_kcal_mol"), flush=True)
    results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
    out = {
        "topic": {"target": "Sorbitol dehydrogenase (SORD)",
                  "reference": "CP-166572",
                  "topic_id": "HP-054", "date": "2026-11-14"},
        "docking": {
            "ok": True, "pdb_id": "1PL6", "resolution": 2.00,
            "center": CENTER,
            "center_note": ("co-crystallised ligand 572 centroid, chain A; "
                            "ligand 572 IS CP-166572 (C11H19N5O3S), 6.28 A "
                            "from catalytic Zn2+ (chain A)"),
            "box_size": 22.5, "exhaustiveness": 8,
            "correction_note": ("run_docking.py auto-picked 1PL8 (1.90 A, "
                                "best resolution) — an NAD+ complex with no "
                                "inhibitor. 1PL6 is the inhibitor-bound "
                                "structure and the correct choice; the QUERY "
                                "dock is the CP-166572 re-dock control. "
                                "Receptor prep drops HETATM, so Zn2+ is NOT "
                                "in the docked receptor."),
            "results": results,
        },
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("SAVED:", OUT, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
