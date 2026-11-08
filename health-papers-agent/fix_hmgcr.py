"""Corrected HP-010 (HMG-CoA reductase) docking for two salt leads, 2026-11-08.

FAULT (minor, in dock-HP-010-2026-11-08.json): two of the top-5 leads
failed ligand prep — "RDKit molecule has 2 fragments. Must have 1."
Their ChEMBL SMILES are salts (parent + counter-ion). The pipeline
docked the other three fine on the correct structure (2R4F, centre
verified = co-crystallised RIE inhibitor centroid [78.03, 9.09, -4.92]).

CORRECTION: desalt both SMILES (keep the largest fragment by heavy-atom
count — the parent drug) and dock them with the identical LeadForge
D.dock protocol on 2R4F at the same centre. Results appended to the
docking record; the salt SMILES are recorded so the fix is auditable.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D
from rdkit import Chem

CENTER = [78.03, 9.09, -4.92]
PDB = "2R4F"

src = json.load(open("../hidden_files/dock-HP-010-2026-11-08.json"))
leads = {l["label"]: l for l in src.get("leads") or []}
failed = ["CHEMBL161829", "CHEMBL394937"]
extra = []
for label in failed:
    smi = leads[label]["smiles"]
    frags = Chem.GetMolFrags(Chem.MolFromSmiles(smi), asMols=True)
    parent = max(frags, key=lambda m: m.GetNumHeavyAtoms())
    psmi = Chem.MolToSmiles(parent)
    print(f"{label}: salt SMILES -> parent {psmi}", flush=True)
    r = D.dock(psmi, PDB, CENTER, box_size=22.5)
    r["label"] = label
    r["rank"] = leads[label].get("rank")
    r["desalted_from"] = smi
    extra.append(r)
    print("  DOCK 2R4F:", label, r.get("affinity_kcal_mol"), r.get("ok"), flush=True)

dk = src.get("docking") or {}
results = [r for r in dk.get("results", []) if r.get("ok")]
results.extend([r for r in extra if r.get("ok")])
results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
dk["results"] = results
dk["desalted_redock"] = [r for r in extra]
src["docking"] = dk
src["correction"] = {
    "fault": ("two top-5 leads failed ligand prep (salt SMILES, 2 fragments): "
              "CHEMBL161829, CHEMBL394937"),
    "fix": ("desalted to the largest fragment (parent drug) and re-docked on "
            "2R4F at the verified RIE-inhibitor centre [78.03, 9.09, -4.92]"),
}
out = "../hidden_files/dock-HP-010c-2026-11-08.json"
with open(out, "w") as f:
    json.dump(src, f, indent=1)
print("RAW_SAVED:", out, flush=True)
