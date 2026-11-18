"""Re-dock the published NfCYP51 conazoles on 5TL8 (NfCYP51-posaconazole, 1.71 A).

Why: the pipeline retrieved the WRONG ChEMBL target for this topic — no
ChEMBL target exists for UniProt A0A2H4A2U9 (verified: target_components
query returns 0), so the fallback grabbed CHEMBL2074 (human
maltase-glucoamylase; assay text confirms rice alpha-glucosidase) and its
"leads" are alpha-glucosidase inhibitors, not CYP51 ligands. Their 5TL8
scores (-7.58 to -5.98) are DISCARDED. This script docks the real
comparison set instead: the five conazoles from Debnath et al., PLoS NTD
2017 (posaconazole, itraconazole, fluconazole, isavuconazole,
ketoconazole) with their published anti-N. fowleri EC50s, all at the
co-crystallised posaconazole centroid in 5TL8. SMILES fetched live from
PubChem by name; no invented structures.
"""
import json, sys, urllib.request, urllib.parse
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

PDB = "5TL8"
CENTER = [6.25, 19.98, 47.66]  # co-crystallised posaconazole centroid (pipeline run)
OUT = "../hidden_files/dock-HP-078c-2026-11-18.json"
# published anti-N. fowleri EC50 (Debnath et al., PLoS Negl Trop Dis 2017)
EC50 = {
    "posaconazole": "0.01 uM",
    "itraconazole": "0.01 uM",
    "fluconazole": "13.9 uM",
    "isavuconazole": "equipotent to amphotericin B (Debnath 2017)",
    "ketoconazole": "equipotent to amphotericin B (Debnath 2017)",
}

def pubchem_smiles(name):
    url = ("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
           + urllib.parse.quote(name) + "/property/SMILES,ConnectivitySMILES/JSON")
    req = urllib.request.Request(url, headers={"User-Agent": "LeadForge-research/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        d = json.load(r)
    p = d["PropertyTable"]["Properties"][0]
    # NOTE: PUG returns keys "SMILES" (isomeric) and "ConnectivitySMILES";
    # "CanonicalSMILES"/"IsomericSMILES" are NOT returned here (2026-11-13
    # gotcha). Use connectivity SMILES, as the pipeline does.
    return p.get("ConnectivitySMILES") or p.get("SMILES"), p.get("CID")

results = []
for name in ["posaconazole", "itraconazole", "fluconazole", "isavuconazole", "ketoconazole"]:
    smi, cid = pubchem_smiles(name)
    r = D.dock(smi, PDB, CENTER, box_size=22.5)
    r["label"] = name
    r["pubchem_cid"] = cid
    r["published_ec50"] = EC50[name]
    results.append(r)
    print("DOCK:", name, "CID", cid, r.get("affinity_kcal_mol"), r.get("ok"), r.get("error"), flush=True)
results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
res = {"ok": True, "pdb_id": PDB, "resolution": 1.71,
       "pdb_title": "Naegleria fowleri CYP51-posaconazole complex",
       "co_crystallised_ligand": "X2N (posaconazole)",
       "center": CENTER, "box_size": 22.5, "exhaustiveness": 8, "vina": "1.2.7",
       "note": ("Corrected ligand set: pipeline ChEMBL target was CHEMBL2074 (human "
                "maltase-glucoamylase) — wrong target, no ChEMBL target exists for "
                "NfCYP51 (A0A2H4A2U9). Its 'leads' were alpha-glucosidase inhibitors; "
                "their scores are discarded. This file docks the five published "
                "conazoles instead, at the co-crystallised posaconazole centroid."),
       "results": results}
json.dump(res, open(OUT, "w"), indent=1)
print("SAVED:", OUT)
