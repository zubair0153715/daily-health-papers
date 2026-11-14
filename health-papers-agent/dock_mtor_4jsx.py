"""mTOR kinase-domain docking for HP-058 (2026-11-14).

Why this run exists: run_docking.py's dock_leads hung on the PDB
lookup (find_pdb_for_uniprot iterates up to 12 candidate downloads
through the flaky proxy), and its resolution filter (<3.0 A) can never
pick a kinase-domain structure anyway — every mTOR structure better
than 3.0 A is an FRB-domain fragment (4DRI 1.45 A, 3FAP 1.85 A, ...),
while the kinase-domain structures are 3.3-3.5 A. The pipeline's top
leads are all ATP-competitive kinase inhibitors (IC50 0.1-0.2 nM), so
the correct structure is the Torin2-bound kinase domain, 4JSX
(3.5 A; Yang et al., Nature 2013), centred on the co-crystallised
Torin2 (HETATM 17G, chain A centroid [49.98, -1.37, -47.78]).
Everolimus (QUERY, rank 14) is an allosteric rapalog: it binds the
FRB domain via FKBP12, NOT the ATP site, so its dock here is a
negative control (as miltefosine was for TR in HP-024) — it should
score poorly in the ATP pocket. Limitation, stated in the paper:
3.5 A resolution, rigid docking, no Mg2+/ATPgammaS in the receptor
(HETATM dropped), everolimus is very large (MW 958, ~30 rotatable
bonds) and may be under-sampled.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402

BASE = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts"
MAIN = f"{BASE}/hidden_files/dock-HP-058-2026-11-14.json"
OUT = f"{BASE}/hidden_files/dock-HP-058-2026-11-14-4JSX.json"

# Chain-A Torin2 (17G) centroid, from 4JSX HETATM records.
CENTER = [49.98, -1.37, -47.78]


def main():
    with open(MAIN, encoding="utf-8") as f:
        main_json = json.load(f)
    leads = main_json.get("leads") or []
    top = leads[:5]
    q = next((l for l in leads if l.get("label") == "QUERY"), None)

    results = []
    for l in top:
        r = D.dock(l["smiles"], "4JSX", CENTER, box_size=22.5)
        r["label"] = l.get("label")
        r["rank"] = l.get("rank")
        r["measured_potency"] = (l.get("known_activity") or {}).get("activity")
        r["pains"] = l.get("pains")
        results.append(r)
        print("DOCK 4JSX:", r["label"], r.get("affinity_kcal_mol"),
              r.get("ok"), flush=True)
    if q and "QUERY" not in {r.get("label") for r in results}:
        r = D.dock(q["smiles"], "4JSX", CENTER, box_size=22.5)
        r["label"] = "QUERY"
        r["rank"] = q.get("rank")
        r["measured_potency"] = (q.get("known_activity") or {}).get("activity")
        r["pains"] = q.get("pains")
        results.append(r)
        print("DOCK-QUERY 4JSX:", r.get("affinity_kcal_mol"), flush=True)
    results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
    out = {
        "topic": {"target": "mTOR kinase domain",
                  "reference": "everolimus",
                  "topic_id": "HP-058", "date": "2026-11-14"},
        "docking": {
            "ok": True, "pdb_id": "4JSX", "resolution": 3.5,
            "center": CENTER,
            "center_note": ("co-crystallised Torin2 (17G) centroid, chain "
                            "A — the ATP-binding pocket"),
            "box_size": 22.5, "exhaustiveness": 8,
            "correction_note": ("dock_leads hung on PDB lookup; resolution "
                                "filter (<3.0 A) excludes all kinase-domain "
                                "structures. 4JSX (Torin2-bound, 3.5 A) is "
                                "the correct structure for ATP-competitive "
                                "leads. Everolimus is an allosteric FRB "
                                "binder — its ATP-site dock is a negative "
                                "control. HETATM (incl. Mg2+) dropped by "
                                "receptor prep."),
            "results": results,
        },
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("SAVED:", OUT, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
