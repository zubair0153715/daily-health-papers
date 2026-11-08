"""Corrected HP-053 (HCV NS5A) pipeline run, 2026-11-08.

FAULT in the first run (dock-HP-053-2026-11-08.json): the LeadForge
`uniprot_target` prefers HUMAN hits, so "Hepatitis C virus NS5A"
resolved to human BTBD1 (Q9H0C5) and the ChEMBL side picked
CHEMBL2074 = human maltase-glucoamylase. Every "lead" in that file
is an alpha-glucosidase inhibitor, NOT an NS5A inhibitor. That file
is discarded for the paper.

CORRECTION: HCV NS5A has no standalone reviewed UniProt entry (it is
cleaved from the genome polyprotein), so the pipeline cannot resolve
it. We monkeypatch the two source functions to the verified-correct
values and run the identical pipeline code:
  - UniProt record: the HCV genotype 1b genome polyprotein P26662
    (NS5A is residues ~1973-2420 of the polyprotein; the paper states
    this explicitly) -- used ONLY as the target identifier.
  - ChEMBL target: CHEMBL3307224 "Nonstructural protein 5A",
    Hepatitis C virus (verified live against the ChEMBL API 2026-11-08).
  - Docking: the accession is passed as a synthetic "NS5A-HCV" tag so
    dock_leads cannot silently pick a wrong polyprotein structure
    (e.g. an NS5B polymerase PDB). Docking is SKIPPED: no liganded
    NS5A structure exists for the daclatasvir site (PDB 1ZH1, NS5A
    domain I, is apo). The paper says so honestly.

Usage:
  NO_PROXY=... ~/workspace/.venv-fc/bin/python fix_ns5a.py
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import sources as S
from app.discovery.pipeline import run_pipeline

# --- patches: verified-correct target identity ---
_UNI = {
    "accession": "P26662",
    "entry": "POLG_HCVJA",
    "gene": "NS5A",
    "protein": "Genome polyprotein (NS5A region, residues 1973-2420), Hepatitis C virus genotype 1b",
    "organism": "Hepatitis C virus genotype 1b (isolate J)",
    "length": 3010,
    "function": "NS5A is a zinc-binding phosphoprotein essential for HCV replication and assembly; daclatasvir-class inhibitors bind the NS5A domain I dimer interface.",
    "uniprot_url": "https://www.uniprot.org/uniprotkb/P26662/entry",
}
_CHEMBL = [{
    "chembl_id": "CHEMBL3307224",
    "name": "Nonstructural protein 5A",
    "type": "SINGLE PROTEIN",
    "organism": "Hepatitis C virus",
    "components": 1,
}]


def _fake_uniprot(query):
    return {"ok": True, "data": dict(_UNI)}


def _fake_by_acc(accession):
    return {"ok": True, "data": [dict(_CHEMBL[0])]}


S.uniprot_target = _fake_uniprot
S.chembl_target_by_uniprot = _fake_by_acc

res = run_pipeline("Hepatitis C virus NS5A (corrected)", query_name="daclatasvir",
                   top_n=25, dock_top_n=0)
print("PIPELINE OK:", res.get("ok"), flush=True)
for s in res.get("steps", []):
    print("STEP:", s, flush=True)
print("CHEMBL TARGET:", (res.get("target") or {}).get("chembl_target"), flush=True)
print("LEADS:", len(res.get("leads") or []), flush=True)
# docking intentionally skipped: no liganded NS5A structure for the
# daclatasvir site; do NOT let dock_leads pick a polyprotein PDB.
res["docking"] = {"ok": False, "error": "skipped_no_liganded_ns5a_structure",
                  "note": "PDB 1ZH1 (NS5A domain I) is apo; no co-crystal with a daclatasvir-class inhibitor exists. Docking skipped honestly."}
res["correction"] = {
    "fault": "first run resolved to human BTBD1 (Q9H0C5) + CHEMBL2074 human maltase-glucoamylase; leads were alpha-glucosidase inhibitors, not NS5A inhibitors",
    "fix": "ChEMBL target forced to CHEMBL3307224 (Nonstructural protein 5A, HCV), verified live 2026-11-08; UniProt identifier P26662 (HCV polyprotein, NS5A region)",
    "discarded_file": "hidden_files/dock-HP-053-2026-11-08.json",
}
out = "../hidden_files/dock-HP-053c-2026-11-08.json"
with open(out, "w") as f:
    json.dump(res, f, indent=1)
print("RAW_SAVED:", out, flush=True)
