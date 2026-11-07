"""Re-dock HP-005 leads + acarbose + two flavonoids against human pancreatic
alpha-amylase (PDB 1XCX) at the CORRECT centre.

FAULT (caught by manual audit before any score was reported): the pipeline
auto-picked 5U3A, which is apo — its only non-water HETATM groups are the
N-terminal pyroglutamate PCA (residue 1) and a glycan NAG 501. Both are in
dock.py's _CENTRE_EXCLUDE, but _ligand_center's fallback ("first group with
>= 6 atoms") re-picked PCA, giving centre [5.86, 82.81, 131.04] — the
N-terminus, 19.5 A from the catalytic triad centroid (9.09, 81.66, 150.49).
The run_docking.py process was killed before Vina produced any output, so
no wrong-centre scores exist to discard; the pipeline-only results were
regenerated separately (run_pipeline_only.py).

CORRECTED PROTOCOL: PDB 1XCX (1.9 A, human pancreatic alpha-amylase in
complex with acarbose rearrangement products; Li et al., Biochemistry 2005,
PMID 15736945). Centre = centroid of the full co-crystallised ligand
(chain B: AC1 acarviosine core + BGC + GLC, 44 atoms) = [5.01, 16.45, 41.56].
The AC1 core centroid [9.96, 17.05, 43.65] sits 4.01 A from the catalytic
triad centroid (Asp197/Glu233/Asp300); the combined centre is 7.23 A from
the triad. Box 22.5 A, exhaustiveness 8, 3 poses — same Vina 1.2.7 protocol
as Papers #1/#3. Cross-check structure 1B2Y (3.2 A, acarbose complex):
AC1 centroid 3.88 A from its triad — the site is the same.

LIGANDS: QUERY acarbose + pipeline top leads that are dockable + two
literature flavonoids (luteolin, quercetin; PubChem-verified SMILES) added
for the dietary-adjunct angle. NOT docked: CHEMBL3616594 (rank 3, MW 1901,
31 rotatable bonds) and CHEMBL3616595 (rank 5, MW 2366, 39 rotatable bonds)
— far beyond Vina's reliable sampling range (39 torsions exceeds Vina's
32-torsion handling); reported as not docked, not as zero scores.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402
from app.discovery import chem as C  # noqa: E402

CENTER = [5.01, 16.45, 41.56]
PDB = "1XCX"

src = json.load(open("../hidden_files/dock-HP-005-2026-11-07.json"))
leads = {l["label"]: l for l in src["leads"]}

# PubChem-verified (fetched 2026-11-07, PUG REST):
# luteolin CID 5280445, C15H10O6; quercetin CID 5280343, C15H10O7.
extra = {
    "LUTEOLIN": {
        "smiles": "C1=CC(=C(C=C1C2=CC(=O)C3=C(C=C(C=C3O2)O)O)O)O",
        "note": "flavonoid; PubChem CID 5280445; Martinez-Gonzalez et al. 2019 "
                "found luteolin the best flavonoid inhibitor of pancreatic "
                "alpha-amylase in vitro, better than acarbose",
    },
    "QUERCETIN": {
        "smiles": "C1=CC(=C(C=C1C2=C(C(=O)C3=C(C=C(C=C3O2)O)O)O)O)O",
        "note": "flavonoid; PubChem CID 5280343; oral bioavailability <10%, "
                "free aglycone plasma levels in the low nanomolar range",
    },
}

order = ["QUERY", "CHEMBL1230193", "CHEMBL3618489", "CHEMBL1233515",
         "LUTEOLIN", "QUERCETIN"]
results = []
for lab in order:
    if lab in leads:
        smi = leads[lab]["smiles"]
        rank = leads[lab].get("rank")
        ka = leads[lab].get("known_activity")
        desc = leads[lab].get("descriptors", {})
        pains = leads[lab].get("pains", [])
    else:
        smi = extra[lab]["smiles"]
        rank = None
        ka = None
        desc = C.descriptors(smi) if hasattr(C, "descriptors") else {}
        pains = C.pains(smi)
    print(f"DOCKING {lab} (rank {rank}, MW {desc.get('mw')}, "
          f"rot {desc.get('rotatable')}, known {ka}) ...", flush=True)
    try:
        r = D.dock(smi, PDB, CENTER, box_size=22.5)
    except Exception as e:  # e.g. Vina 900 s timeout
        r = {"ok": False, "error": f"{type(e).__name__}: {e}"}
    r["label"] = lab
    r["rank"] = rank
    r["smiles"] = smi
    r["known_activity"] = ka
    r["descriptors"] = desc
    r["pains"] = pains
    if lab in extra:
        r["note"] = extra[lab]["note"]
    results.append(r)
    print("  ->", lab, r.get("affinity_kcal_mol"), r.get("poses"),
          r.get("ok"), r.get("error", ""), flush=True)

results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
out = {
    "ok": True,
    "pdb_id": PDB,
    "resolution": 1.9,
    "pdb_title": "Acarbose rearrangement mechanism implied by the kinetic and "
                 "structural analysis of human pancreatic alpha-amylase in "
                 "complex with analogues and their elongated counterparts",
    "co_crystallised_ligand": "chain B pseudo-pentasaccharide (AC1 + BGC + GLC)",
    "center": CENTER,
    "center_basis": "centroid of the full co-crystallised ligand (44 atoms); "
                    "AC1 core centroid [9.96, 17.05, 43.65] is 4.01 A from the "
                    "catalytic triad centroid (Asp197/Glu233/Asp300); combined "
                    "centre is 7.23 A from the triad; 22.5 A box covers subsites "
                    "-3 to +2",
    "box_size": 22.5,
    "exhaustiveness": 8,
    "vina": "1.2.7",
    "fault": "Pipeline auto-pick 5U3A (apo) centred on N-terminal PCA "
             "[5.86, 82.81, 131.04], 19.5 A from the catalytic triad — "
             "_ligand_center fallback re-picked an excluded modified residue. "
             "Run killed before any Vina output; no wrong-centre scores exist. "
             "Root cause: fallback ignores _CENTRE_EXCLUDE; fix owed in dock.py.",
    "not_docked": [
        {"label": "CHEMBL3616594", "rank": 3, "mw": 1901,
         "rotatable": 31, "known_activity": "Ki 14.3 nM",
         "reason": "MW 1901 Da / 31 rotatable bonds — beyond Vina's reliable "
                   "sampling range at exhaustiveness 8"},
        {"label": "CHEMBL3616595", "rank": 5, "mw": 2366,
         "rotatable": 39, "known_activity": "Ki 41.6 nM",
         "reason": "MW 2366 Da / 39 rotatable bonds — exceeds Vina's "
                   "32-torsion handling"},
    ],
    "results": results,
}
json.dump(out, open("../hidden_files/dock-HP-005c-2026-11-07.json", "w"),
          indent=1)
print("SAVED ../hidden_files/dock-HP-005c-2026-11-07.json", flush=True)
