"""Corrected HP-038 (influenza N1 neuraminidase) pipeline run, 2026-11-08.

FAULTS in the first run (dock-HP-038-2026-11-08.json) — discard it entirely:
  Fault 1 (ChEMBL target): the pipeline's step-2 ranking prefers
    SINGLE PROTEIN + Homo sapiens, so it picked CHEMBL1862 =
    human ABL1 tyrosine kinase. Every "lead" is an ABL1 inhibitor
    (Ki 0.02-0.07 nM), NOT a neuraminidase inhibitor.
  Fault 2 (structure): PDB 1NMB is an N9 neuraminidase + antibody
    Fab complex with NO drug-like ligand. _ligand_center's fallback
    (return first >=6-atom group when nothing survives exclusions)
    landed on NAG residue 1 chain A — a GLYCAN on the Fab — centroid
    [47.83, 66.36, 38.63]. ABL1 inhibitors were docked at a glycan.
  Fault 3 (subtype): 1NMB is N9, the paper is about N1/H274Y.

CORRECTION:
  - UniProt: P03468, neuraminidase, Influenza A (A/Puerto Rico/8/1934
    H1N1) — verified live 2026-11-08.
  - ChEMBL target: CHEMBL2051, "Neuraminidase", Influenza A virus
    (A/Puerto Rico/8/1934(H1N1)) — verified live 2026-11-08.
  - Docking, manual, on TWO verified N1 structures, each centred on
    its co-crystallised oseltamivir (G39) centroid, computed from the
    PDB file and printed for the record:
      3TI6 — 2009 pandemic H1N1 NA + oseltamivir (wild type)
      3CL0 — N1 NA H274Y + oseltamivir (resistance mutant; H274Y in
             N2 numbering = H275Y in N1 numbering)
    Top 5 pipeline leads + oseltamivir docked on BOTH structures with
    the identical LeadForge D.dock protocol (Vina 1.2.7, 22.5 A box,
    exhaustiveness 8, 3 poses).

Usage:
  NO_PROXY=... ~/workspace/.venv-fc/bin/python fix_na.py
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import sources as S
from app.discovery.pipeline import run_pipeline
from app.discovery import dock as D

_UNI = {
    "accession": "P03468",
    "entry": "NRAM_I34A1",
    "gene": "NA",
    "protein": "Neuraminidase, Influenza A virus (strain A/Puerto Rico/8/1934 H1N1)",
    "organism": "Influenza A virus (strain A/Puerto Rico/8/1934 H1N1)",
    "length": 454,
    "function": "Neuraminidase cleaves sialic acid from host glycans, releasing new virions; the target of oseltamivir, zanamivir and peramivir.",
    "uniprot_url": "https://www.uniprot.org/uniprotkb/P03468/entry",
}
_CHEMBL = [{
    "chembl_id": "CHEMBL2051",
    "name": "Neuraminidase",
    "type": "SINGLE PROTEIN",
    "organism": "Influenza A virus (A/Puerto Rico/8/1934(H1N1))",
    "components": 1,
}]


def _fake_uniprot(query):
    return {"ok": True, "data": dict(_UNI)}


def _fake_by_acc(accession):
    return {"ok": True, "data": [dict(_CHEMBL[0])]}


S.uniprot_target = _fake_uniprot
S.chembl_target_by_uniprot = _fake_by_acc

res = run_pipeline("Influenza A neuraminidase N1 (corrected)", query_name="oseltamivir",
                   top_n=25, dock_top_n=0)
print("PIPELINE OK:", res.get("ok"), flush=True)
for s in res.get("steps", []):
    print("STEP:", s, flush=True)
print("CHEMBL TARGET:", (res.get("target") or {}).get("chembl_target"), flush=True)
print("LEADS:", len(res.get("leads") or []), flush=True)

# --- manual docking on 3TI6 (WT) and 3CL0 (H274Y) ---
def g39_centroid(pdb_id):
    path = D._pdb_path(pdb_id)
    pts = []
    for line in open(path):
        if line.startswith("HETATM") and line[17:20].strip() == "G39":
            pts.append((float(line[30:38]), float(line[38:46]), float(line[46:54])))
    if not pts:
        raise RuntimeError(f"no G39 in {pdb_id}")
    return [sum(p[i] for p in pts) / len(pts) for i in range(3)], len(pts)


leads = res.get("leads") or []
q = next((l for l in leads if l.get("label") == "QUERY"), None)
top = [l for l in leads if l.get("label") != "QUERY"][:5]
dock_set = top + ([q] if q else [])
print("DOCK SET:", [l["label"] for l in dock_set], flush=True)

docking = {}
for pdb_id, label in [("3TI6", "wildtype_2009_H1N1"), ("3CL0", "H274Y_mutant")]:
    center, n = g39_centroid(pdb_id)
    print(f"CENTRE {pdb_id} ({label}): G39 n={n} centroid "
          f"[{center[0]:.2f}, {center[1]:.2f}, {center[2]:.2f}]", flush=True)
    results = []
    for l in dock_set:
        r = D.dock(l["smiles"], pdb_id, center, box_size=22.5)
        r["label"] = l["label"]
        r["rank"] = l.get("rank")
        results.append(r)
        print(f"  DOCK {pdb_id}:", l["label"], r.get("affinity_kcal_mol"),
              r.get("ok"), flush=True)
    results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
    docking[label] = {"ok": True, "pdb_id": pdb_id, "center": center,
                      "results": results}

res["docking"] = docking
res["correction"] = {
    "fault": ("first run picked CHEMBL1862 human ABL1 kinase as the ChEMBL target "
              "(human-preferring rank) and PDB 1NMB (N9 NA + Fab, no drug-like ligand); "
              "_ligand_center fallback landed on a Fab glycan (NAG 1 chain A)"),
    "fix": ("ChEMBL target forced to CHEMBL2051 (N1 neuraminidase, PR8 H1N1), verified live "
            "2026-11-08; UniProt P03468; manual docking on 3TI6 (WT) and 3CL0 (H274Y), "
            "each centred on co-crystallised oseltamivir (G39)"),
    "discarded_file": "hidden_files/dock-HP-038-2026-11-08.json",
}
out = "../hidden_files/dock-HP-038c-2026-11-08.json"
with open(out, "w") as f:
    json.dump(res, f, indent=1)
print("RAW_SAVED:", out, flush=True)
