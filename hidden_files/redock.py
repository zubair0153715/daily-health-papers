"""Re-dock named ligands at a corrected centre; save as a 'c' file like yesterday."""
import json, sys
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

src, pdb_id, center, out = sys.argv[1], sys.argv[2], json.loads(sys.argv[3]), sys.argv[4]
d = json.load(open(src))
labels = [r["label"] for r in d["docking"]["results"]]
by_label = {l["label"]: l for l in d["leads"]}
results = []
for lab in labels:
    lead = by_label[lab]
    r = D.dock(lead["smiles"], pdb_id, center, box_size=22.5)
    r["label"] = lab
    r["rank"] = lead.get("rank")
    results.append(r)
    print("REDOCK:", lab, r.get("affinity_kcal_mol"), r.get("ok"), flush=True)
results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
res = {"ok": True, "pdb_id": pdb_id, "resolution": d["docking"].get("resolution"),
       "pdb_title": "Structure of the enoyl-ACP reductase of Mycobacterium tuberculosis InhA, inhibited with the active metabolite of isoniazid",
       "co_crystallised_ligand": "ZID (isonicotinic-acetyl-NAD, the INH-NAD adduct)",
       "center": center, "box_size": 22.5, "exhaustiveness": 8, "vina": "1.2.7",
       "note": "Corrected centre: centroid of co-crystallised ZID adduct; pipeline first centred on NAD cofactor, 1.82 A away.",
       "results": results}
json.dump(res, open(out, "w"), indent=1)
print("SAVED:", out)
