"""Manual dock for HP-020: pipeline auto-pick failed (no_pdb_found) because
find_pdb_for_uniprot only accepts X-ray <3.0 A, and the only Mtb ATP
synthase + bedaquiline structures are cryo-EM (8J0S/8J57, Zhang et al.
Nature 2024). Dock QUERY (bedaquiline) + top 5 pipeline leads on 8J57
(Mtb ATP synthase Fo + BDQ, 2.85 A cryo-EM), grid centred on the
co-crystallised BDQ copy at the a-c interface (chain 1 BQ1 centroid
[162.46, 186.93, 275.26]; closest contact to subunit a, 3.04 A).
Pipeline also resolved the WRONG UniProt entry (P9WPV1, epsilon chain,
gene atpC); the true AtpE/subunit-c entry is P9WPS1 (gene atpE, Rv1305).
"""
import json, sys
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

CENTER = [162.46, 186.93, 275.26]
PDB = "8J57"
OUT = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-020c-2026-11-07.json"
SRC = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-020-2026-11-07.json"

d = json.load(open(SRC))
by_label = {l["label"]: l for l in d["leads"]}
labels = ["QUERY", "CHEMBL3754673", "CHEMBL3751877", "CHEMBL3754231",
          "CHEMBL3752792", "CHEMBL4101131"]
results = []
for lab in labels:
    lead = by_label[lab]
    r = D.dock(lead["smiles"], PDB, CENTER, box_size=22.5)
    r["label"] = lab
    r["rank"] = lead.get("rank")
    results.append(r)
    print("DOCK:", lab, r.get("affinity_kcal_mol"), r.get("ok"), r.get("error"), flush=True)
results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
res = {
    "ok": True,
    "pdb_id": PDB,
    "resolution": 2.85,
    "method": "cryo-EM",
    "pdb_title": "Cryo-EM structure of Mycobacterium tuberculosis ATP synthase Fo in complex with bedaquiline (BDQ)",
    "citation": "Zhang et al., Nature 631, 409-414 (2024), DOI 10.1038/s41586-024-07605-8, PMID 38961288",
    "co_crystallised_ligand": "BQ1 (bedaquiline), chain 1 copy at the a-c interface",
    "center": CENTER,
    "center_note": "Centroid of co-crystallised BQ1 on chain 1 (a-c interface site); closest atom contact to subunit a chain 3.04 A. Other BQ1 copies (chains 4-9) are lagging/c-only sites 6-43 A from subunit a.",
    "box_size": 22.5,
    "exhaustiveness": 8,
    "vina": "1.2.7",
    "target_correction": "Pipeline resolved UniProt P9WPV1 (ATP synthase epsilon chain, gene atpC) for query 'ATP synthase subunit c AtpE'; correct AtpE/subunit-c entry is P9WPS1 (gene atpE, Rv1305, 81 aa). ChEMBL target CHEMBL2364166 (Mtb ATP synthase complex) was correct. Docking used 8J57, whose chains 1-9 ARE subunit c (P9WPS1).",
    "note": "Manual dock: pipeline PDB auto-pick accepts X-ray <3.0 A only, so cryo-EM 8J57 was skipped (no_pdb_found).",
    "results": results,
}
json.dump(res, open(OUT, "w"), indent=1)
print("SAVED:", OUT)
