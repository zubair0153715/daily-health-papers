"""Dock explicit (label, SMILES) pairs at a centre; save 'c' file. Labels JSON list via argv."""
import json, sys
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

src, pdb_id, center, out = sys.argv[1], sys.argv[2], json.loads(sys.argv[3]), sys.argv[4]
pairs = json.loads(sys.argv[5])  # [[label, smiles], ...]
note = sys.argv[6] if len(sys.argv) > 6 else ""
d = json.load(open(src))
results = []
for lab, smi in pairs:
    r = D.dock(smi, pdb_id, center, box_size=22.5)
    r["label"] = lab
    results.append(r)
    print("DOCK:", lab, r.get("affinity_kcal_mol"), r.get("ok"), r.get("error"), flush=True)
results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
res = {"ok": True, "pdb_id": pdb_id, "resolution": d["docking"].get("resolution"),
       "center": center, "box_size": 22.5, "exhaustiveness": 8, "vina": "1.2.7",
       "note": note, "results": results}
json.dump(res, open(out, "w"), indent=1)
print("SAVED:", out)
