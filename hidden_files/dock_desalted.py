"""Dock named leads after desalting (keep largest fragment); save 'c' file."""
import json, sys
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from rdkit import Chem
from rdkit.Chem import Descriptors
from app.discovery import dock as D

src, pdb_id, center, out = sys.argv[1], sys.argv[2], json.loads(sys.argv[3]), sys.argv[4]
labels = sys.argv[5].split(",")
note = sys.argv[6] if len(sys.argv) > 6 else ""
d = json.load(open(src))
by_label = {l["label"]: l for l in d["leads"]}
results = []
for lab in labels:
    lead = by_label[lab]
    smi = lead["smiles"]
    frags = smi.split(".")
    best, best_n = None, -1
    for f in frags:
        m = Chem.MolFromSmiles(f)
        if m is None:
            continue
        n = m.GetNumHeavyAtoms()
        if n > best_n:
            best, best_n = f, n
    if best is None:
        print("DESALT-FAIL:", lab, flush=True)
        continue
    print("DESALT:", lab, "frags:", len(frags), "kept", best_n, "heavy atoms;", best[:60], flush=True)
    r = D.dock(best, pdb_id, center, box_size=22.5)
    r["label"] = lab
    r["rank"] = lead.get("rank")
    r["desalted_smiles"] = best
    results.append(r)
    print("DOCK:", lab, r.get("affinity_kcal_mol"), r.get("ok"), r.get("error"), flush=True)
results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
res = {"ok": True, "pdb_id": pdb_id, "resolution": d["docking"].get("resolution"),
       "center": center, "box_size": 22.5, "exhaustiveness": 8, "vina": "1.2.7",
       "note": note, "results": results}
json.dump(res, open(out, "w"), indent=1)
print("SAVED:", out)
