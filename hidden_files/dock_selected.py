"""Dock named lead labels from a pipeline JSON at a given centre/PDB; save 'c' file."""
import json, sys
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

src, pdb_id, center, out = sys.argv[1], sys.argv[2], json.loads(sys.argv[3]), sys.argv[4]
labels = sys.argv[5].split(",")
note = sys.argv[6] if len(sys.argv) > 6 else ""
d = json.load(open(src))
by_label = {l["label"]: l for l in d["leads"]}
results = []
for lab in labels:
    lead = by_label[lab]
    r = D.dock(lead["smiles"], pdb_id, center, box_size=22.5)
    r["label"] = lab
    r["rank"] = lead.get("rank")
    results.append(r)
    print("DOCK:", lab, r.get("affinity_kcal_mol"), r.get("ok"), r.get("error"), flush=True)
results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
res = {"ok": True, "pdb_id": pdb_id, "resolution": d["docking"].get("resolution"),
       "center": center, "box_size": 22.5, "exhaustiveness": 8, "vina": "1.2.7",
       "note": note, "results": results}
json.dump(res, open(out, "w"), indent=1)
print("SAVED:", out)
