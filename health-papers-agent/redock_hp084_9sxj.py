"""Convert 9SXJ.cif (RCSB mmCIF; the .pdb 404s) to PDB format for the
LeadForge dock module, then self-dock capmatinib + the best analogue
(CHEMBL3582305) on the wild-type c-MET + capmatinib structure.

9SXJ: wild-type c-MET bound by capmatinib (Russell et al., ACS Med Chem
Lett 2026, PMID 41847658). Capmatinib residue name A1JRF.
Centre = centroid of A1JRF via dock._ligand_center (audit).
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

# --- mmCIF atom_site -> PDB ---
cif = open("/tmp/9SXJ.cif").read().splitlines()
# find atom_site loop header
hdr = None
rows = []
i = 0
while i < len(cif):
    if cif[i].strip() == "loop_":
        # collect following _atom_site.* lines
        j = i + 1
        cols = []
        while j < len(cif) and cif[j].startswith("_atom_site."):
            cols.append(cif[j].strip()[len("_atom_site."):])
            j += 1
        if cols and "Cartn_x" in cols:
            hdr = cols
            k = j
            while k < len(cif) and cif[k].strip() and not cif[k].startswith("#") and not cif[k].startswith("loop_") and not cif[k].startswith("_"):
                rows.append(cif[k].split())
                k += 1
            break
    i += 1

assert hdr, "atom_site loop not found"
idx = {c: n for n, c in enumerate(hdr)}
print("atoms:", len(rows), "cols:", len(hdr))

def q(v):
    return v.strip("'\"")

out = []
serial = 0
for r in rows:
    if len(r) < len(hdr):
        continue
    group = q(r[idx["group_PDB"]])
    atom = q(r[idx["label_atom_id"]])
    comp = q(r[idx["label_comp_id"]])
    chain = q(r[idx["label_asym_id"]])
    seq = q(r[idx["label_seq_id"]]) if r[idx["label_seq_id"]] not in (".", "?") else ""
    x = float(r[idx["Cartn_x"]]); y = float(r[idx["Cartn_y"]]); z = float(r[idx["Cartn_z"]])
    occ = r[idx["occupancy"]] if "occupancy" in idx else "1.00"
    b = r[idx["B_iso_or_equiv"]] if "B_iso_or_equiv" in idx else "0.00"
    el = q(r[idx["type_symbol"]]) if "type_symbol" in idx else atom[0]
    serial += 1
    rec = "HETATM" if group == "HETATM" else "ATOM  "
    try:
        seqn = int(seq)
    except ValueError:
        seqn = 0
    # PDB residue names are max 3 chars: truncate (A1JRF -> A1J) so the
    # fixed columns stay aligned; _ligand_center reads cols 30-54.
    comp3 = comp[:3]
    out.append(f"{rec}{serial:5d} {atom:^4s} {comp3:>3s} {chain:1s}{seqn:4d}    {x:8.3f}{y:8.3f}{z:8.3f}{float(occ):6.2f}{float(b):6.2f}          {el:>2s}\n")
open("/tmp/9SXJ.pdb", "w").writelines(out + ["END\n"])
print("wrote /tmp/9SXJ.pdb")
# pre-place in the dock module's cache so _pdb_path() reuses it instead of
# downloading (files.rcsb.org/download/9SXJ.pdb 404s)
import shutil
cache = "/home/hatch/workspace/clinic-demo/app/discovery/data/pdb_cache/9SXJ.pdb"
shutil.copy("/tmp/9SXJ.pdb", cache)
print("cached at", cache, "size", len(out))

center = D._ligand_center("/tmp/9SXJ.pdb")
print("9SXJ capmatinib (A1JRF) centroid:", center)

pipe = json.load(open("/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-084-2026-11-21.json"))
by = {l["label"]: l for l in pipe["leads"]}
jobs = [
    ("capmatinib (reference; ChEMBL3188267, IC50 0.13 nM)", by["QUERY"]["smiles"]),
    ("CHEMBL3582305 (IC50 0.13 nM)", by["CHEMBL3582305"]["smiles"]),
]
results = []
for label, smi in jobs:
    print("DOCKING:", label, flush=True)
    r = D.dock(smi, "9SXJ", center, box_size=22.5)
    r["label"] = label
    print("  ->", r.get("affinity_kcal_mol"), r.get("poses"), r.get("ok"), flush=True)
    results.append(r)
    with open("/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-084-9sxj-2026-11-21.json", "w") as f:
        json.dump({"pdb_id": "9SXJ", "center": center, "resolution": None,
                   "note": "9SXJ wild-type c-MET + capmatinib (Russell 2026, PMID 41847658); CIF converted to PDB locally; centre = A1JRF centroid via dock._ligand_center",
                   "results": results}, f, indent=1)
print("DONE", flush=True)
