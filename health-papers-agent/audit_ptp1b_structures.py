"""Audit top-resolution PTP1B (P18031) X-ray structures for the HP-003 re-dock.

FAULT in the first run (dock-HP-003-2026-11-12.json): the pipeline's
structure picker (find_pdb_for_uniprot, resolution-sorted UniProt PDB
xrefs) picked 9C66 (1.4 A) — the MENA EVH1 domain bound to a PTP1B
polyproline peptide (chain B = residues 304-313 only). The grid centre
landed on CSO A7, a modified cysteine of the EVH1 domain, not the
PTP1B active site. The docking scores (-6.0 to -7.07) are for ligands
docked into the MENA EVH1 domain and are INVALID for PTP1B.

This script audits the top-resolution candidates: for each, download the
PDB, report the title, the chain coverage of P18031, and the ligand
group _ligand_center picks (residue, atom count, centroid). A valid
re-dock structure needs: (a) a PTP1B chain covering the catalytic
domain (residues ~1-300), (b) a drug-like co-crystallised ligand in
the active site (not a buffer/cryoprotectant/modified residue).
"""
import json
import sys
import urllib.request

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

CANDS = ["7MN9", "7MKZ", "8U1E", "8G65", "7MNA", "7MOU", "2CM2", "5QGF",
         "7GTW", "2F71", "1XBO", "2HNP", "1PTV", "2QBS"]

for pid in CANDS:
    try:
        p = D._pdb_path(pid)
    except Exception as e:
        print(pid, "DOWNLOAD FAIL:", str(e)[:100], flush=True)
        continue
    title = ""
    compnd = []
    with open(p) as f:
        for line in f:
            if line.startswith("TITLE"):
                title += line[10:].strip() + " "
            if line.startswith("COMPND"):
                compnd.append(line[10:].strip())
    c = D._ligand_center(p)
    # largest HETATM group
    from collections import defaultdict
    groups = defaultdict(list)
    with open(p) as f:
        for line in f:
            if line.startswith("HETATM"):
                res = (line[17:20].strip(), line[21].strip(), line[22:26].strip())
                groups[res].append(1)
    big = sorted(((len(v), k) for k, v in groups.items()), reverse=True)[:3]
    print(pid, "| centre:", [round(x, 2) for x in c] if c else None,
          "| title:", title.strip()[:90], flush=True)
    print("    largest HETATM groups:", big, flush=True)
    print("    compnd:", " ".join(compnd)[:160], flush=True)
