"""P2Y12 re-dock for HP-138 (2026-11-28) — QUERY + top 4 leads on 4NTJ.

Why: the pipeline's auto-pick, 4PXZ, is P2Y12 in complex with 2MeSADP —
the AGONIST-bound, active-state structure. Ticagrelor is a reversible
antagonist; docking antagonists into the agonist-bound conformation gives
weak, misleading scores (ticagrelor itself only -6.06 kcal/mol, and the
largest lead CHEMBL567709 scored -3.70, i.e. essentially non-binding).
4NTJ is the correct template: human P2Y12 in complex with an antithrombotic
drug (AZD1283, a reversible antagonist of the same class), 2.62 A.
Centre audit: dock._ligand_center on 4NTJ picks the AZD1283 ligand
centroid (the largest drug-like HETATM group). Same box (22.5 A) and
exhaustiveness (8) as Papers #1/#3. Compounds (SMILES read from the
pipeline JSON, same leads as the 4PXZ run).
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402

BASE = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts"
PIPE = f"{BASE}/hidden_files/dock-HP-138-2026-11-28.json"
OUT = f"{BASE}/hidden_files/dock-HP-138-2026-11-28-4NTJ.json"


def main():
    pdb_path = D._pdb_path("4NTJ")
    center = D._ligand_center(pdb_path)
    print("CENTER 4NTJ:", center, flush=True)
    if not center:
        print("ERROR: no ligand centre in 4NTJ", flush=True)
        return 1
    pipe = json.load(open(PIPE))
    leads = {l.get("label"): l for l in pipe["leads"]}
    wanted = ["QUERY", "CHEMBL5181634", "CHEMBL251041", "CHEMBL249790",
              "CHEMBL567709"]
    results = []
    for label in wanted:
        l = leads[label]
        r = D.dock(l["smiles"], "4NTJ", center, box_size=22.5)
        r["label"] = label
        r["rank"] = l.get("rank")
        results.append(r)
        print("DOCK 4NTJ:", label, r.get("affinity_kcal_mol"), r.get("ok"),
              flush=True)
    results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
    out = {
        "topic": {"target": "P2Y12 ADP receptor", "reference": "ticagrelor",
                  "topic_id": "HP-138", "date": "2026-11-28"},
        "docking": {
            "ok": True, "pdb_id": "4NTJ", "resolution": 2.62,
            "center": [round(c, 2) for c in center],
            "center_note": ("AZD1283 antagonist centroid via "
                            "dock._ligand_center — human P2Y12 + AZD1283, "
                            "2.62 A"),
            "box_size": 22.5, "exhaustiveness": 8,
            "correction_note": ("Pipeline auto-pick 4PXZ was the wrong "
                                "conformation: P2Y12 + 2MeSADP, the "
                                "agonist-bound active state; ticagrelor "
                                "scored only -6.06 there and CHEMBL567709 "
                                "-3.70. Re-docked on 4NTJ, the "
                                "antagonist-bound template."),
            "results": results,
        },
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("SAVED:", OUT, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
