"""One-off retry: SG85 on 1CQQ for HP-136 (2026-11-25).

First attempt timed out at the 1800 s Vina wall limit under heavy shared-CPU
contention (SG85 is the largest ligand in the set: 650.77 Da, 16 rotatable
bonds); the same compound completed on 6KU8 (-7.75). This script retries it
once on 1CQQ at the verified centre [6.19, -7.46, 29.24] and patches the
1CQQ JSON in place (adds the SG85 result, re-sorts). If it times out again,
the 1CQQ SG85 cell stays missing and the paper reports it honestly.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402

BASE = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts"
OUT = f"{BASE}/hidden_files/dock-HP-136-2026-11-25-1CQQ.json"
CENTER = [6.1899518072289155, -7.463915662650602, 29.243819277108436]
SMILES = "CCOC(=O)/C=C/[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC2=CC=CC=C2)NC(=O)[C@H](COC(C)(C)C)NC(=O)OCC3=CC=CC=C3"

r = D.dock(SMILES, "1CQQ", CENTER, box_size=22.5)
print("RETRY SG85 1CQQ:", r.get("affinity_kcal_mol"), r.get("ok"),
      r.get("error"), flush=True)
if r.get("ok"):
    with open(OUT, encoding="utf-8") as f:
        d = json.load(f)
    r["label"] = "SG85"
    r["note"] = ("Enterovirus 3C inhibitor; blocks rhinovirus replication, "
                 "NOT cross-resistant with rupintrivir (AAC 2015)")
    r["descriptors"] = {"mw": 650.77, "logp": 2.95, "hbd": 4, "hba": 8,
                        "tpsa": 161.16, "rotatable": 16,
                        "lipinski_violations": 1, "lipinski_pass": False,
                        "formula": "C35H46N4O8"}
    r["pains"] = []
    d["docking"]["results"] = [x for x in d["docking"]["results"]
                               if x.get("label") != "SG85"]
    d["docking"]["results"].append(r)
    d["docking"]["results"].sort(key=lambda x: x.get("affinity_kcal_mol", 999))
    d["docking"]["correction_note"] += (" SG85 retry succeeded on second "
                                        "attempt (first attempt hit the 1800 "
                                        "s Vina wall limit under CPU "
                                        "contention).")
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=1)
    print("PATCHED:", OUT, flush=True)
else:
    print("RETRY FAILED — 1CQQ SG85 cell stays missing (reported honestly).",
          flush=True)
