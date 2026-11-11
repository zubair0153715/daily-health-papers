import json, sys
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D
from app.discovery import chem as C

CENTER = [15.45, 8.23, 21.26]
named = {
    "vaborbactam": "B1(C(CCC(O1)CC(=O)O)NC(=O)CC2=CC=CS2)O",
    "relebactam": "C1CC(N2CC1N(C2=O)OS(=O)(=O)O)C(=O)NC3CCNCC3",
    "taniborbactam": "B1(C(CC2=C(O1)C(=CC=C2)C(=O)O)NC(=O)CC3CCC(CC3)NCCN)O",
    "avibactam-redock": "C1CC(N2CC1N(C2=O)OS(=O)(=O)O)C(=O)N",
}
results = []
for name, smi in named.items():
    desc = C.descriptors(smi) if hasattr(C, "descriptors") else None
    pains = C.pains_alerts(smi) if hasattr(C, "pains_alerts") else None
    r = D.dock(smi, "6TD0", CENTER, box_size=22.5)
    r["label"] = name
    r["smiles"] = smi
    r["descriptors"] = desc
    r["pains"] = pains
    results.append(r)
    print("DOCK:", name, r.get("affinity_kcal_mol"), r.get("ok"), r.get("error"), flush=True)
    print("   desc:", json.dumps(desc)[:300] if desc else None, "| pains:", pains, flush=True)
json.dump({"ok": True, "pdb_id": "6TD0", "resolution": 0.99,
           "pdb_title": "Crystal structure of vaborbactam bound to KPC-2",
           "co_crystallised_ligand": "4D6 (vaborbactam), centroid [15.45, 8.23, 21.26]; altloc A/B centroids within 0.08 A",
           "center": CENTER, "box_size": 22.5, "exhaustiveness": 8, "vina": "1.2.7",
           "note": "Named clinical comparators docked at the verified vaborbactam centroid; avibactam re-docked as a reproducibility check on the pipeline result.",
           "results": results},
          open("dock-HP-012-named-2026-11-08.json", "w"), indent=1)
print("SAVED")
