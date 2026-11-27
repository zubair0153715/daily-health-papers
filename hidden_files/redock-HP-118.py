"""HP-118 GlgE re-dock — corrected target structure.

Problem: the pipeline found no PDB for Mtb GlgE (P9WQ17) and ChEMBL
target CHEMBL3112377 has zero bioactivities, so no docking was done.
Verified facts (RCSB + literature, 2026-11-27):
  - 4U33 "Structure of Mtb GlgE bound to maltose" (3.29 A) exists but the
    asymmetric unit holds SIX maltose copies (chains G-L); no single
    validated donor-site centroid -> NOT used.
  - 4U31 "Sco GlgEI-V279S in Complex with maltose-C-phosphonate" (1.85 A):
    the V279S variant was engineered to emulate the Mtb GlgE M1P binding
    site (Lindenberger et al., Sci Rep 2015;5:12830). Centre = GPM
    (maltose-C-phosphonate) residue, chain C.
  - Ligands: M1P (substrate; PubChem CID 167489 isomeric SMILES),
    MCP = alpha-maltose-C-phosphonate (only known Mtb GlgE inhibitor,
    IC50 230 +/- 24 uM, Veleti et al. 2014; SMILES extracted from 4U31
    GPM C1 + GLC C2 via RDKit, phosphonate valence corrected to
    CP(=O)(O)O), DDGIM = 2,5-dideoxy-3-O-alpha-D-glucopyranosyl-2,5-
    imino-D-mannitol, oxocarbenium mimic (SMILES extracted from 4U2Y
    RZM A701 via RDKit).
Docking: Vina, box 22.5 A at the MCP centroid, same protocol as the
other 2026-11-27 papers.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D
from app.discovery import chem as C

PDB = "4U31"
CENTRE = [24.835, -31.255, 281.437]  # GPM (MCP) centroid, chain C, 4U31
BOX = 22.5

LIGANDS = {
    "M1P_substrate": {
        "smiles": "C([C@@H]1[C@H]([C@@H]([C@H]([C@H](O1)O[C@@H]2[C@H](O[C@@H]([C@@H]([C@H]2O)O)OP(=O)(O)O)CO)O)O)O)O",
        "name": "maltose-1-phosphate (substrate)",
        "measured": "substrate of GlgE (donor); no IC50 (not an inhibitor)",
    },
    "MCP": {
        "smiles": "OC[C@H]1O[C@H](O[C@H]2[C@H](O)[C@@H](O)[C@@H](CP(=O)(O)O)O[C@@H]2CO)[C@H](O)[C@@H](O)[C@@H]1O",
        "name": "alpha-maltose-C-phosphonate (MCP, Veleti 13)",
        "measured": "IC50 230 +/- 24 uM vs Mtb GlgE (Veleti et al. 2014)",
    },
    "DDGIM": {
        "smiles": "OC[C@H]1N[C@H](CO)[C@@H](O[C@H]2O[C@H](CO)[C@@H](O)[C@H](O)[C@H]2O)[C@@H]1O",
        "name": "DDGIM (oxocarbenium mimic, Lindenberger et al. 2015)",
        "measured": "structural mimic only; no published IC50 found",
    },
}

out = {
    "target": "GlgE (Sco GlgEI-V279S emulating Mtb GlgE M1P site)",
    "uniprot_mtb": "P9WQ17",
    "pdb": PDB,
    "pdb_title": "Sco GlgEI-V279S in Complex with maltose-C-phosphonate",
    "resolution_A": 1.85,
    "centre": CENTRE,
    "centre_source": "GPM (MCP) centroid, chain C, residue 1, 4U31",
    "box_A": BOX,
    "caveat": "Sco GlgE V279S, not Mtb GlgE: scores are site-emulation, not Mtb-native",
    "ligands": [],
}

for key, lig in LIGANDS.items():
    desc = C.descriptors(lig["smiles"])
    pains = C.pains(lig["smiles"])
    res = D.dock(lig["smiles"], PDB, CENTRE, box_size=BOX)
    entry = {
        "key": key,
        "name": lig["name"],
        "smiles": lig["smiles"],
        "measured": lig["measured"],
        "descriptors": desc,
        "pains": pains,
        "vina_kcal_mol": res.get("affinity_kcal_mol"),
        "vina_all": res.get("poses"),
        "dock_ok": res.get("ok", False),
        "dock_error": res.get("error"),
    }
    print(key, "->", res.get("affinity_kcal_mol"), "kcal/mol", "PAINS:", pains)
    out["ligands"].append(entry)

with open("/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-118-2026-11-27-redock.json", "w") as f:
    json.dump(out, f, indent=2)
print("saved redock json")
