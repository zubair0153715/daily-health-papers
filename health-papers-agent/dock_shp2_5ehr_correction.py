"""SHP2 re-dock for HP-126 (2026-11-28) — QUERY + top 4 leads on 5EHR.

Why: the pipeline's auto-pick, 9EIK, is the WRONG structure for an
allosteric inhibitor: it is the isolated N-SH2 domain of SHP2 (T42A mutant)
bound to a GAB1 phosphopeptide — there is no allosteric pocket in it.
Proof: TNO155, an 11 nM allosteric inhibitor, docked at only -5.75
kcal/mol there. 5EHR is the correct template: full-length human SHP2 in
complex with the allosteric inhibitor SHP099 (1.7 A), same allosteric
pocket TNO155 binds (interface of N-SH2 / C-SH2 / PTP domains).
Centre audit: dock._ligand_center on 5EHR picks the SHP099 ligand
centroid (the largest drug-like HETATM group). Same box (22.5 A) and
exhaustiveness (8) as Papers #1/#3. Compounds (SMILES read from the
pipeline JSON, same leads as the 9EIK run).
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402

BASE = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts"
PIPE = f"{BASE}/hidden_files/dock-HP-126-2026-11-28.json"
OUT = f"{BASE}/hidden_files/dock-HP-126-2026-11-28-5EHR.json"


def main():
    pdb_path = D._pdb_path("5EHR")
    center = D._ligand_center(pdb_path)
    print("CENTER 5EHR:", center, flush=True)
    if not center:
        print("ERROR: no ligand centre in 5EHR", flush=True)
        return 1
    pipe = json.load(open(PIPE))
    leads = {l.get("label"): l for l in pipe["leads"]}
    wanted = ["QUERY", "CHEMBL5882319", "CHEMBL4789817", "CHEMBL5792033",
              "CHEMBL4858291"]
    results = []
    for label in wanted:
        l = leads[label]
        r = D.dock(l["smiles"], "5EHR", center, box_size=22.5)
        r["label"] = label
        r["rank"] = l.get("rank")
        results.append(r)
        print("DOCK 5EHR:", label, r.get("affinity_kcal_mol"), r.get("ok"),
              flush=True)
    results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
    out = {
        "topic": {"target": "SHP2/PTPN11", "reference": "TNO155",
                  "topic_id": "HP-126", "date": "2026-11-28"},
        "docking": {
            "ok": True, "pdb_id": "5EHR", "resolution": 1.7,
            "center": [round(c, 2) for c in center],
            "center_note": ("SHP099 allosteric inhibitor centroid via "
                            "dock._ligand_center — full-length human SHP2 + "
                            "SHP099, 1.7 A"),
            "box_size": 22.5, "exhaustiveness": 8,
            "correction_note": ("Pipeline auto-pick 9EIK was the wrong "
                                "structure: isolated N-SH2 domain + GAB1 "
                                "phosphopeptide, no allosteric pocket; "
                                "TNO155 (11 nM) docked only -5.75 there. "
                                "Re-docked on 5EHR, the correct allosteric "
                                "template."),
            "results": results,
        },
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("SAVED:", OUT, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
