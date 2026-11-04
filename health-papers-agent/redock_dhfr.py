"""HP-014 re-dock: E. coli DHFR at the correct pocket.

The pipeline auto-picked PDB 9PWM (correct: E. coli DHFR + folate + NADP+,
0.89 A) but centred the grid on OCS, an oxidised-cysteine residue record
(9 atoms), 12 A from the folate site. Trimethoprim competes with
dihydrofolate, so the grid belongs on the folate centroid.
Re-dock the 5 distinct leads + trimethoprim at the FOL centroid
[-1.29, 3.27, -7.86], same Vina protocol (box 22.5 A, exhaustiveness 8,
3 poses). CHEMBL22 is trimethoprim itself and is reported as QUERY only.
"""
import sys, json
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

src = json.load(open("../hidden_files/dock-HP-014-2026-11-04.json"))
leads = {l["label"]: l for l in src["leads"]}
order = ["CHEMBL23609", "CHEMBL60069", "CHEMBL278345", "CHEMBL31891", "CHEMBL23338", "QUERY"]
center = [-1.29, 3.27, -7.86]
results = []
for lab in order:
    l = leads[lab]
    r = D.dock(l["smiles"], "9PWM", center, box_size=22.5)
    r["label"] = lab
    r["rank"] = l.get("rank")
    results.append(r)
    print("DOCK", lab, r.get("affinity_kcal_mol"), r.get("poses"), r.get("ok"), flush=True)
results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
out = {"ok": True, "pdb_id": "9PWM", "resolution": 0.89,
       "pdb_title": "Dihydrofolate Reductase Complexed with Folate and Nicotinamide Adenine Dinucleotide Phosphate (Oxidized Form)",
       "co_crystallised_ligand": "FOL (folate)",
       "center": center, "box_size": 22.5,
       "exhaustiveness": 8, "vina": "1.2.7",
       "note": "Re-dock: pipeline auto-centre was the OCS residue record, ~12 A from the folate/trimethoprim site. Re-docked at the folate centroid, same protocol. CHEMBL22 is trimethoprim itself, reported as QUERY only.",
       "results": results}
json.dump(out, open("../hidden_files/dock-HP-014c-2026-11-04.json", "w"), indent=1)
print("SAVED")
