"""Pipeline-only re-run for HP-005 (alpha-amylase / acarbose).

The full run_docking.py run was killed after the audit found its
auto-picked structure 5U3A is apo and its grid centre is the N-terminal
pyroglutamate (PCA) centroid [5.86, 82.81, 131.04] — ~19.5 A from the
catalytic triad centroid (9.09, 81.66, 150.49). Docking there is meaningless.
This script re-runs steps 1-6 only (UniProtKB -> ChEMBL -> PubChem -> RDKit
-> PAINS/ADMET -> ranking) and saves the raw JSON; the docking is done
separately by redock_hp005.py against a ligand-bound structure at the
co-crystallised ligand centroid.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery.pipeline import run_pipeline  # noqa: E402

res = run_pipeline("Human pancreatic alpha-amylase", query_name="acarbose",
                   top_n=25, dock_top_n=0)
print("PIPELINE OK:", res.get("ok"), flush=True)
for s in res.get("steps", []):
    print("STEP:", s, flush=True)
tgt = res.get("target") or {}
uni = tgt.get("uniprot") or {}
print("UNIPROT:", uni.get("accession"), uni.get("name"),
      uni.get("organism"), flush=True)
print("LEADS:", len(res.get("leads") or []), flush=True)
res["topic"] = {"target": "Human pancreatic alpha-amylase",
                "reference": "acarbose"}
with open("../hidden_files/dock-HP-005-2026-11-07.json", "w",
          encoding="utf-8") as f:
    json.dump(res, f, indent=1)
print("RAW_SAVED: ../hidden_files/dock-HP-005-2026-11-07.json", flush=True)
