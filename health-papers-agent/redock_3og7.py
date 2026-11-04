"""Re-dock HP-029 leads + vemurafenib against the BRAF V600E kinase domain (PDB 3OG7).

The pipeline auto-picked 8VSO, which is a ternary 14-3-3 sigma / BRAF
phosphopeptide (pS365) / compound-78 complex — NOT the BRAF kinase domain, and
the grid was centred on a phosphoserine residue. Those scores are meaningless
and are discarded. 3OG7 is the BRAF V600E kinase domain (2.45 A) co-crystallised
with PLX4032 (vemurafenib, ligand code 032); grid centre is the 032 centroid,
same Vina protocol (box 22.5 A, exhaustiveness 8, 3 poses).
"""
import sys, json
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

src = json.load(open("../hidden_files/dock-HP-029-2026-11-04.json"))
leads = {l["label"]: l for l in src["leads"]}
order = ["CHEMBL3651664", "CHEMBL3651680", "CHEMBL2047875", "CHEMBL3752213", "CHEMBL3651701", "QUERY"]
center = [1.87, -2.64, -19.92]
results = []
for lab in order:
    l = leads[lab]
    r = D.dock(l["smiles"], "3OG7", center, box_size=22.5)
    r["label"] = lab
    r["rank"] = l.get("rank")
    results.append(r)
    print("DOCK", lab, r.get("affinity_kcal_mol"), r.get("poses"), r.get("ok"), flush=True)
results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
out = {"ok": True, "pdb_id": "3OG7", "resolution": 2.45,
       "pdb_title": "B-Raf Kinase V600E oncogenic mutant in complex with PLX4032",
       "co_crystallised_ligand": "032 (PLX4032 / vemurafenib)",
       "center": center, "box_size": 22.5,
       "exhaustiveness": 8, "vina": "1.2.7",
       "note": "Manual re-dock: pipeline auto-pick 8VSO is a 14-3-3/BRAF-phosphopeptide complex, not the kinase domain - its scores were discarded. Re-docked against the BRAF V600E kinase domain 3OG7, same protocol. Residue 600 is GLU in chain B, confirming the V600E mutant.",
       "results": results}
json.dump(out, open("../hidden_files/dock-HP-029c-2026-11-04.json", "w"), indent=1)
print("SAVED")
