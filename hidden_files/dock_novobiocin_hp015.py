"""One-off: dock novobiocin (the true GyrB ATP-site reference) on 7P2M, same centre/box as the HP-015 run."""
import json, sys
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D
smi = "CC1=C(C=CC2=C1OC(=O)C(=C2O)NC(=O)C3=CC(=C(C=C3)O)CC=C(C)C)O[C@H]4[C@@H]([C@@H]([C@H](C(O4)(C)C)OC)OC(=O)N)O"
r = D.dock(smi, "7P2M", [-18.6, -15.05, 6.55], box_size=22.5)
r["label"] = "novobiocin"
r["smiles"] = smi
r["pubchem_cid"] = 54675769
print(json.dumps(r, indent=1))
json.dump(r, open("../hidden_files/dock-HP-015-novobiocin-2026-11-09.json", "w"), indent=1)
