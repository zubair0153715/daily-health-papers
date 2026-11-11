import sys, json
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

CENTER = [15.51, 20.21, 7.63]
PDB = "1RGZ"

leads = [
    ("CHEMBL212760", "O=C([O-])C1=CS[C@@H]2/C(=C\\c3cc4n(n3)CCSC4)C(=O)N12.[Na+]", 9.00, "IC50 1.0 nM"),
    ("CHEMBL222758", "O=C([O-])C1=CS[C@@H]2/C(=C\\c3cn4c(n3)sc3ccccc34)C(=O)N12.[Na+]", 9.00, "IC50 1.0 nM"),
    ("CHEMBL222375", "Cc1ccc2c(c1)sc1nc(/C=C3/C(=O)N4C(C(=O)[O-])=CS[C@H]34)cn12.[Na+]", 9.00, "IC50 1.0 nM"),
    ("CHEMBL378119", "O=C([O-])C1=CS[C@@H]2/C(=C\\c3cc4n(n3)CCS(=O)(=O)C4)C(=O)N12.[Na+]", 8.70, "IC50 2.0 nM"),
    ("CHEMBL425963", "O=C([O-])C1=CS[C@@H]2/C(=C\\c3cn4c(n3)CSCC4)C(=O)N12.[Na+]", 8.70, "IC50 2.0 nM"),
    ("AVIBACTAM", "C1C[C@H](N2C[C@@H]1N(C2=O)OS(=O)(=O)O)C(=O)N", None, "known AmpC inhibitor; PubChem CID 9835049"),
]
out = {"pdb_id": PDB, "center": CENTER, "box_size": 22.5, "results": []}
for label, smi, pchembl, meas in leads:
    r = D.dock(smi, PDB, CENTER, box_size=22.5)
    r["label"] = label
    r["pchembl"] = pchembl
    r["measured"] = meas
    out["results"].append(r)
    print("DOCK:", label, r.get("affinity_kcal_mol"), r.get("poses"), r.get("ok"), flush=True)
json.dump(out, open("dock-HP-016-2026-11-11-extra.json", "w"), indent=1)
print("SAVED dock-HP-016-2026-11-11-extra.json", flush=True)
