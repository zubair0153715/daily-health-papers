"""Corrected T315I docking for HP-032 (2026-11-14).

Why: run_docking.py resolved "BCR-ABL1 T315I" to mouse Abl1 P00520 and
its auto-pick (best resolution + drug-like ligand) chose 3KFA, a WILD-TYPE
Abl kinase domain. The paper's question is the T315I gatekeeper mutant,
whose experimental structure is 3OY3 (murine Abl1 kinase domain, T315I,
1.95 A, bound to the ponatinib analogue AP24589; Zhou et al. 2011,
PMID 21118377). The kinase-domain construct is the same murine Abl1
residues 229-511 used in the ponatinib structural-mechanism literature;
the gatekeeper numbering (Thr315) is identical.

This script docks the same top-5 pipeline leads + ponatinib (QUERY) on
3OY3, centre = AP24589 centroid via dock._ligand_center, plus an AP24589
re-dock control (SMILES from PubChem). It writes
dock-HP-032-2026-11-14-T315I.json and prints a one-line summary.
The WT 3KFA run from run_docking.py is kept as the wild-type control.
"""
import json
import sys
import urllib.parse
import urllib.request

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402

BASE = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts"
MAIN = f"{BASE}/hidden_files/dock-HP-032-2026-11-14.json"
OUT = f"{BASE}/hidden_files/dock-HP-032-2026-11-14-T315I.json"


def pubchem_smiles(name):
    url = ("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
           + urllib.parse.quote(name) + "/property/CanonicalSMILES/JSON")
    req = urllib.request.Request(url, headers={"User-Agent": "LeadForge-research/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        d = json.loads(resp.read().decode())
    props = d["PropertyTable"]["Properties"][0]
    return props.get("CanonicalSMILES") or props.get("ConnectivitySMILES")


def main():
    with open(MAIN, encoding="utf-8") as f:
        main_json = json.load(f)
    leads = main_json.get("leads") or []
    top = leads[:5]
    q = next((l for l in leads if l.get("label") == "QUERY"), None)

    pdb_path = D._pdb_path("3OY3")
    center = D._ligand_center(pdb_path)
    print("CENTER 3OY3 (AP24589 centroid):", center, flush=True)

    results = []
    for l in top:
        r = D.dock(l["smiles"], "3OY3", center, box_size=22.5)
        r["label"] = l.get("label")
        r["rank"] = l.get("rank")
        r["measured_potency"] = l.get("measured_potency")
        r["pains"] = l.get("pains")
        results.append(r)
        print("DOCK 3OY3:", r["label"], r.get("affinity_kcal_mol"), r.get("ok"), flush=True)
    if q:
        r = D.dock(q["smiles"], "3OY3", center, box_size=22.5)
        r["label"] = "QUERY"
        r["rank"] = q.get("rank")
        r["measured_potency"] = q.get("measured_potency")
        r["pains"] = q.get("pains")
        results.append(r)
        print("DOCK-QUERY 3OY3:", r.get("affinity_kcal_mol"), flush=True)
    try:
        smi = pubchem_smiles("AP24589")
        r = D.dock(smi, "3OY3", center, box_size=22.5)
        r["label"] = "AP24589-REDOCK"
        r["source"] = "PubChem AP24589 (co-crystallised ligand of 3OY3; re-dock control)"
        results.append(r)
        print("DOCK-REDOCK 3OY3:", r.get("affinity_kcal_mol"), flush=True)
    except Exception as e:  # noqa: BLE001 - control is nice-to-have, never blocks
        print("REDOCK SKIP:", e, flush=True)
    results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
    out = {
        "topic": {"target": "BCR-ABL1 T315I", "reference": "ponatinib",
                  "topic_id": "HP-032", "date": "2026-11-14"},
        "docking": {
            "ok": True, "pdb_id": "3OY3", "resolution": 1.95,
            "center": [round(c, 2) for c in center],
            "center_note": ("co-crystallised AP24589 centroid via "
                            "dock._ligand_center; T315I mutant kinase domain"),
            "box_size": 22.5, "exhaustiveness": 8,
            "correction_note": ("run_docking.py auto-picked wild-type 3KFA; "
                                "this is the corrected T315I-mutant docking. "
                                "3OY3 is murine Abl1 kinase domain residues "
                                "229-511, T315I, bound to AP24589."),
            "results": results,
        },
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("SAVED:", OUT, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
