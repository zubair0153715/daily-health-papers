"""Homologue docking for HP-024 (2026-11-14) — Leishmania TR.

Why: L. donovani trypanothione reductase (UniProt P39050) has NO
deposited crystal structure (no PDB cross-reference in UniProt), so
run_docking.py skipped docking. The closest experimental structure is
the L. infantum enzyme (UniProt A4HSF7, 491 aa, 87.2% ungapped
sequence identity to P39050; the two species are in the same
L. donovani complex). 4ADW (3.61 A) is the L. infantum TR structure
with the physiological substrate trypanothione bound (HETATM GCG,
chain A centroid [21.56, 41.03, -18.76]) — the substrate pocket is
the inhibitor binding site for the beta-carboline-quinazolinone
series. This script docks the pipeline's top-5 leads (miltefosine
QUERY + 4 ChEMBL TR inhibitors) on 4ADW centred on the substrate
centroid, box 22.5 A. Miltefosine is NOT a TR inhibitor — it is the
clinical reference drug for visceral leishmaniasis, acting by a
different mechanism — so its dock is a negative control: if it scores
as well as genuine TR inhibitors, the method cannot discriminate.
Limitation, stated in the paper: homologue structure (87.2%
identity), 3.61 A resolution, FAD/NADPH dropped from the receptor
(their HETATM records are removed by prep), rigid docking.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402

BASE = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts"
MAIN = f"{BASE}/hidden_files/dock-HP-024-2026-11-14.json"
OUT = f"{BASE}/hidden_files/dock-HP-024-2026-11-14-4ADW.json"

# Chain-A trypanothione (GCG) centroid, from 4ADW HETATM records.
CENTER = [21.56, 41.03, -18.76]


def main():
    with open(MAIN, encoding="utf-8") as f:
        main_json = json.load(f)
    leads = main_json.get("leads") or []
    top = leads[:5]

    results = []
    for l in top:
        r = D.dock(l["smiles"], "4ADW", CENTER, box_size=22.5)
        r["label"] = l.get("label")
        r["rank"] = l.get("rank")
        r["measured_potency"] = (l.get("known_activity") or {}).get("activity")
        r["pains"] = l.get("pains")
        results.append(r)
        print("DOCK 4ADW:", r["label"], r.get("affinity_kcal_mol"),
              r.get("ok"), flush=True)
    results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
    out = {
        "topic": {"target": "Trypanothione reductase (Leishmania donovani)",
                  "reference": "miltefosine",
                  "topic_id": "HP-024", "date": "2026-11-14"},
        "docking": {
            "ok": True, "pdb_id": "4ADW", "resolution": 3.61,
            "center": CENTER,
            "center_note": ("trypanothione (GCG) centroid, chain A — the "
                            "physiological substrate in the active site"),
            "box_size": 22.5, "exhaustiveness": 8,
            "homologue_note": ("No L. donovani TR structure exists in the "
                               "PDB. Homologue: L. infantum TR (UniProt "
                               "A4HSF7, 87.2% ungapped identity to P39050, "
                               "both 491 aa). FAD/NADPH dropped by receptor "
                               "prep. Miltefosine is a negative control — "
                               "not a TR inhibitor."),
            "results": results,
        },
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("SAVED:", OUT, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
