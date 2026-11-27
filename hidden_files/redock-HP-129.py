"""Re-dock HP-129 leads on the CORRECT c-KIT structure.

Why: run_docking.py's find_pdb_for_uniprot picked 2VIF — the SOCS6 SH2
domain in complex with a c-KIT phosphopeptide, NOT the KIT kinase domain —
because the peptide maps to P10721. Docking on 2VIF scored binding to
SOCS6, not KIT inhibition. This script re-docks on 1T46 (Mol et al. 2004,
c-Kit kinase domain + imatinib/STI, 1.6 A complex) at the STI ligand
centroid [26.18, 26.06, 40.36] from dock._ligand_center. Same protocol:
box 22.5 A, exhaustiveness 8, best of 3 poses. Rank-2 lead CHEMBL5416410
excluded: its SMILES has 2 fragments (salt), RDKit prep refuses it;
replaced by rank-6 CHEMBL272938 so the set is still 5 ligands.
"""
import json, sys
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

CENTER = [26.18, 26.06, 40.36]
PDB = "1T46"

d = json.load(open("../hidden_files/dock-HP-129-2026-11-27.json"))
by_label = {l["label"]: l for l in d["leads"]}
wanted = ["QUERY", "CHEMBL404366", "CHEMBL402846", "CHEMBL273187", "CHEMBL272938"]
results = []
for lab in wanted:
    l = by_label[lab]
    r = D.dock(l["smiles"], PDB, CENTER, box_size=22.5)
    r["label"] = l.get("label")
    r["rank"] = l.get("rank")
    results.append(r)
    print("DOCK:", r.get("label"), r.get("affinity_kcal_mol"), r.get("poses"), flush=True)
results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
out = {"ok": True, "pdb_id": PDB, "resolution": 1.6,
       "center": CENTER,
       "center_basis": "centroid of co-crystallised imatinib (STI, 37 atoms) in 1T46 via dock._ligand_center; 1T46 is the c-Kit kinase domain + STI-571 complex (Mol et al. 2004)",
       "box_size": 22.5, "exhaustiveness": 8,
       "excluded": "CHEMBL5416410 (rank 2): SMILES has 2 fragments (salt), RDKit ligand prep refuses it; replaced by rank-6 CHEMBL272938",
       "note": "1T46 is the DFG-out inactive conformation with the juxtamembrane domain displaced; imatinib is a type-II inhibitor. Docking cannot test exon-17/D816V resistance — that mutant is DFG-in and imatinib cannot bind it at all.",
       "results": results}
json.dump(out, open("../hidden_files/dock-HP-129-2026-11-27-redock.json", "w"), indent=1)
print("SAVED ../hidden_files/dock-HP-129-2026-11-27-redock.json")
