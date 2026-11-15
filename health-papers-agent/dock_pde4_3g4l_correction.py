"""Corrected docking for HP-077 (PDE4, phosphodiesterase 4), 2026-11-15.

Why this exists: the standard pipeline run (dock-HP-077-2026-11-15.json)
failed and its numbers are DISCARDED (kept for audit):
1. Target: UniProt resolved to Q86H13 -- Dictyostelium discoideum PDE --
   and the ChEMBL fallback picked CHEMBL2074 maltase-glucoamylase again
   (the same wrong-target failure as HP-069). The 55 "ligands" are
   alpha-glucosidase inhibitors, not PDE4 ligands.
2. Docking: DOCK_LEADS False, no_pdb_found. Nothing was docked.

Correction (documented fallback, HP-027 precedent):
- Structure 3G4L: human PDE4D catalytic domain in complex with
  roflumilast, 2.5 A ("Crystal structure of human phosphodiesterase 4d
  with roflumilast"). Centre = D._ligand_center (roflumilast centroid),
  audited against the active-site Zn(II)/Mg(II) distances.
- Compounds: the three FDA-approved dermatologic PDE4 inhibitors that
  can be docked (roflumilast, apremilast, cilomilast), plus crisaborole
  as the measured-only reference -- crisaborole is a benzoxaborole
  (contains boron), so Vina rejects it exactly as it rejected
  taniborbactam in HP-064. Same tool limit, second demonstration.
- Measured potencies are the Wang et al. 2025 comparison set
  (J Invest Dermatol 2025;145(6):1471-1488.e1, PMID 39608668):
  roflumilast 0.7 nM; apremilast 0.14 uM; crisaborole 0.24 uM.
  Cilomilast 120 nM is from Hatzelmann & Schudt 2001 (J Pharmacol Exp
  Ther 297:267-279, PMID 11259554), the same paper that measured
  roflumilast at 0.8 nM. Ranges are stated in the manuscript:
  apremilast 74 nM (Schafer 2010, Br J Pharmacol 159:842-855) to
  0.14 uM; crisaborole 0.24 uM (Wang abstract) to 0.75 uM (same paper's
  text; J Clin Aesthet Dermatol 2025;18(7):18-21); cilomilast 11 nM
  (Card et al. PDE4D) to 120 nM (Hatzelmann). The ranking is unaffected
  by which end of any range is used, which is stated in the paper.
- PDE4D's active site holds Zn(II) and Mg(II); Vina treats them as
  static point charges and cannot price the metal-water network that
  the Wang paper's "3-2-1 rule" says drives potency. Stated, not hidden.
"""
import json
import math
import os
import sys
import urllib.parse
import urllib.request

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402
from rdkit import Chem  # noqa: E402
from rdkit.Chem import Descriptors, rdMolDescriptors  # noqa: E402

GOAL = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts"
OUT = os.path.join(GOAL, "hidden_files/dock-HP-077-2026-11-15-3G4L.json")
PARTIAL = OUT + ".partial"
CACHE = os.path.join(GOAL, "hidden_files")
PDB = "3G4L"

# (label, PubChem name, expected formula, measured PDE4 IC50 nM, notes)
COMPOUNDS = [
    ("ROFLUMILAST", "roflumilast", "C17H14Cl2F2N2O3", 0.7,
     "Wang 2025 JID comparison set: 0.7 nM; Hatzelmann & Schudt 2001: 0.8 nM. Re-dock control on its own structure 3G4L."),
    ("APREMILAST", "apremilast", "C22H24N2O7S", 140,
     "Wang 2025 JID comparison set: 0.14 uM. Schafer 2010 measured 74 nM -- range 74-140 nM; ranking unaffected."),
    ("CILOMILAST", "cilomilast", "C20H25NO4", 120,
     "Hatzelmann & Schudt 2001: 120 nM (human PDE4). Card et al.: PDE4D 11 nM, PDE4B 25 nM -- subtype-dependent; range 11-120 nM; ranking unaffected."),
]

CRISABOROLE_NOTE = ("NOT docked: benzoxaborole, contains boron; Vina PDBQT parser rejects "
    "atom type B (proven by the pipeline run on HP-064 taniborbactam). Measured reference only: "
    "0.24 uM (Wang 2025 JID abstract); 0.75 uM in the same paper's text and in "
    "J Clin Aesthet Dermatol 2025;18(7):18-21. Either value leaves it last by a wide margin.")


def pubchem_by_name(name):
    """Return (cid, smiles, formula) for a compound name via PUG REST."""
    url = ("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
           + urllib.parse.quote(name)
           + "/property/CanonicalSMILES,MolecularFormula/JSON")
    req = urllib.request.Request(url, headers={"User-Agent": "LeadForge-research/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        d = json.loads(r.read().decode())
    p = d["PropertyTable"]["Properties"][0]
    # PUG sometimes returns ConnectivitySMILES instead of CanonicalSMILES.
    smi = p.get("CanonicalSMILES") or p.get("ConnectivitySMILES")
    return p.get("CID"), smi, p.get("MolecularFormula")


def pains(smiles):
    from rdkit.Chem.FilterCatalog import FilterCatalog, FilterCatalogParams
    params = FilterCatalogParams()
    params.AddCatalog(FilterCatalogParams.FilterCatalogs.PAINS)
    cat = FilterCatalog(params)
    m = Chem.MolFromSmiles(smiles)
    return [e.GetDescription() for e in cat.GetMatches(m)]


def main():
    resolved = []
    for label, name, formula_expected, ic50_nM, notes in COMPOUNDS:
        cid, smi, formula = pubchem_by_name(name)
        print(f"{label}: PubChem CID {cid} formula {formula}", flush=True)
        assert formula == formula_expected, f"formula wrong for {label}: {formula} != {formula_expected}"
        m = Chem.MolFromSmiles(smi)
        assert m is not None, f"bad SMILES for {label}"
        dd = {"mw": round(Descriptors.MolWt(m), 2),
              "logp": round(Descriptors.MolLogP(m), 2),
              "hbd": rdMolDescriptors.CalcNumHBD(m),
              "hba": rdMolDescriptors.CalcNumHBA(m),
              "tpsa": round(rdMolDescriptors.CalcTPSA(m), 2),
              "rotatable": rdMolDescriptors.CalcNumRotatableBonds(m),
              "formula": rdMolDescriptors.CalcMolFormula(m)}
        resolved.append({"label": label, "smiles": smi, "pubchem_cid": cid,
                         "descriptors": dd, "pains": pains(smi),
                         "measured_PDE4_IC50_nM": ic50_nM, "notes": notes})

    # --- structure + centre audit ---
    pdb_path = os.path.join(CACHE, "3G4L.pdb")
    if not os.path.exists(pdb_path):
        req = urllib.request.Request("https://files.rcsb.org/download/3G4L.pdb",
                                     headers={"User-Agent": "LeadForge-research/1.0"})
        with urllib.request.urlopen(req, timeout=60) as r:
            open(pdb_path, "wb").write(r.read())
    center = D._ligand_center(pdb_path)
    print("CENTRE 3G4L:", center, flush=True)
    metals = []
    for ln in open(pdb_path):
        if ln.startswith("HETATM") and ln[17:20].strip() in ("ZN", "MG"):
            metals.append((ln[17:20].strip(),
                           (float(ln[30:38]), float(ln[38:46]), float(ln[46:54]))))
    audit = {"centre": [round(c, 2) for c in center],
             "metals": [{"element": e, "centre_distance_A": round(math.dist(center, xyz), 2)}
                        for e, xyz in metals]}
    print("AUDIT:", audit, flush=True)

    # --- docking (incremental save + resume) ---
    done = {}
    if os.path.exists(PARTIAL):
        done = json.load(open(PARTIAL))
    results = []
    for c in resolved:
        if c["label"] in done:
            results.append(done[c["label"]])
            print(f"RESUME {c['label']}: {done[c['label']]['affinity_kcal_mol']}", flush=True)
            continue
        r = D.dock(c["smiles"], PDB, center, box_size=22.5)
        r["label"] = c["label"]
        r["measured_PDE4_IC50_nM"] = c["measured_PDE4_IC50_nM"]
        results.append(r)
        done[c["label"]] = r
        json.dump(done, open(PARTIAL, "w"), indent=1)
        print(f"DOCK {c['label']}: {r.get('affinity_kcal_mol')} ok={r.get('ok')} {r.get('error','')}", flush=True)
    results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))

    out = {"ok": True, "pdb_id": PDB, "resolution": 2.5, "center": audit["centre"],
           "centre_audit": audit, "compounds": resolved, "results": results,
           "crisaborole_reference": CRISABOROLE_NOTE,
           "correction_note": "Pipeline run dock-HP-077-2026-11-15.json is DISCARDED (UniProt Q86H13 Dictyostelium PDE; ChEMBL CHEMBL2074 maltase-glucoamylase; no_pdb_found). This file is the corrected docking on 3G4L (human PDE4D + roflumilast)."}
    json.dump(out, open(OUT, "w"), indent=1)
    print("SAVED:", OUT, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
