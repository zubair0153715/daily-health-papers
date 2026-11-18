"""Re-dock HP-065 ligands at the CORRECT site: 5BS8 moxifloxacin centroid.

Why: the pipeline auto-picked 3M4I (GyrB TOPRIM domain fragment, 1.95 A) and
centred on a small HETATM ion there. Moxifloxacin binds the DNA-cleavage
complex (GyrA + DNA + Mg2+), whose structure is 5BS8 (Blower et al., PNAS
2016) with moxifloxacin (MFX) co-crystallised. Docking a fluoroquinolone on
the TOPRIM fragment is a wrong-site dock (same class of error as the TYK2
JH1/JH2 audit, 2026-11-11). Centre = centroid of the first MFX copy via
dock._ligand_center (excludes cofactors/ions/waters). DNA chains are ATOM
records in 5BS8, so the receptor prep keeps them; Mg2+ HETATM ions are
dropped by the prep — a stated limitation (the FQ Mg2+-water bridge is
absent from rigid Vina scoring).
"""
import json, sys
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

src = "../hidden_files/dock-HP-065-2026-11-18.json"
pdb_id = "5BS8"
out = "../hidden_files/dock-HP-065c-2026-11-18.json"

d = json.load(open(src))
pdb_path = D._pdb_path(pdb_id)
center = D._ligand_center(pdb_path)
print("CENTER (MFX centroid, 5BS8):", center, flush=True)
labels = [r["label"] for r in d["docking"]["results"]]
by_label = {l["label"]: l for l in d["leads"]}
results = []
for lab in labels:
    lead = by_label[lab]
    r = D.dock(lead["smiles"], pdb_id, center, box_size=22.5)
    r["label"] = lab
    r["rank"] = lead.get("rank")
    results.append(r)
    print("REDOCK:", lab, r.get("affinity_kcal_mol"), r.get("ok"), r.get("error"), flush=True)
results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
res = {"ok": True, "pdb_id": pdb_id, "resolution": 2.4,
       "pdb_title": "Crystal structure and stability of gyrase-fluoroquinolone cleaved complexes from Mycobacterium tuberculosis",
       "co_crystallised_ligand": "MFX (moxifloxacin)",
       "center": center, "box_size": 22.5, "exhaustiveness": 8, "vina": "1.2.7",
       "note": ("Corrected centre: centroid of co-crystallised moxifloxacin in 5BS8. "
                "Pipeline first docked on 3M4I (GyrB TOPRIM domain fragment) — wrong site "
                "for a fluoroquinolone; those scores are discarded. Mg2+ ions dropped by "
                "receptor prep; DNA chains retained (ATOM records)."),
       "results": results}
json.dump(res, open(out, "w"), indent=1)
print("SAVED:", out)
