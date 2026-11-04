"""HP-047 (COX-2 / celecoxib): pipeline + dual-isoform docking.

Why not plain run_docking.py: the pipeline's find_pdb_for_uniprot crashed on a
UniProt HTTP 500 for PTGS2, and its auto centre would have been the BOG
detergent centroid in 3LN1, not the celecoxib site. So: run the pipeline for
ligand ranking, then dock top-5 leads + celecoxib against BOTH isoforms with
hand-verified centres:
  COX-2: PDB 3LN1 (2.4 A, "Structure of celecoxib bound at the COX-2 active
         site"), CEL chain C centroid [65.25, -45.38, 45.42].
  COX-1: PDB 3KK6 (2.75 A, "Crystal Structure of Cyclooxygenase-1 in complex
         with celecoxib"), CEL chain A centroid [-32.41, 43.36, -5.62].
Same Vina protocol (box 22.5 A, exhaustiveness 8, 3 poses) for every ligand
on both structures, so the COX-2/COX-1 ratio is a like-for-like comparison.
"""
import sys, json
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery.pipeline import run_pipeline
from app.discovery import dock as D

res = run_pipeline("PTGS2", query_name="celecoxib", top_n=25, dock_top_n=0)
print("PIPELINE OK:", res.get("ok"), flush=True)
tgt = res.get("target") or {}
print("UNIPROT:", (tgt.get("uniprot") or {}).get("accession"),
      (tgt.get("uniprot") or {}).get("protein"), flush=True)
leads = res.get("leads") or []
print("LEADS:", len(leads), flush=True)
json.dump(res, open("../hidden_files/dock-HP-047-2026-11-04.json", "w"), indent=1)

by_label = {l["label"]: l for l in leads}
order = [l["label"] for l in leads[:5]] + ["QUERY"]
print("DOCK ORDER:", order, flush=True)

def dock_all(pdb_id, center):
    out = []
    for lab in order:
        l = by_label[lab]
        r = D.dock(l["smiles"], pdb_id, center, box_size=22.5)
        r["label"] = lab
        r["rank"] = l.get("rank")
        out.append(r)
        print("DOCK", pdb_id, lab, r.get("affinity_kcal_mol"), r.get("poses"), r.get("ok"), flush=True)
    out.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
    return out

cox2 = dock_all("3LN1", [65.25, -45.38, 45.42])
cox1 = dock_all("3KK6", [-32.41, 43.36, -5.62])
json.dump({"ok": True,
           "cox2": {"pdb_id": "3LN1", "resolution": 2.4,
                    "title": "Structure of celecoxib bound at the COX-2 active site",
                    "center": [65.25, -45.38, 45.42], "results": cox2},
           "cox1": {"pdb_id": "3KK6", "resolution": 2.75,
                    "title": "Crystal Structure of Cyclooxygenase-1 in complex with celecoxib",
                    "center": [-32.41, 43.36, -5.62], "results": cox1},
           "box_size": 22.5, "exhaustiveness": 8, "vina": "1.2.7",
           "note": "Dual-isoform dock: same ligands, same protocol on COX-2 (3LN1) and COX-1 (3KK6); selectivity = COX-1 minus COX-2 affinity."},
          open("../hidden_files/dock-HP-047c-2026-11-04.json", "w"), indent=1)
print("SAVED")
