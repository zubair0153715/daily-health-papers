"""Corrected docking for HP-069 (KRAS G12D / MRTX1133), 2026-11-15.

Why this exists: the standard pipeline run (dock-HP-069-2026-11-15.json)
resolved the target WRONG in two ways, and both numbers from that run are
DISCARDED (kept in that file for audit only):
1. ChEMBL target: UniProt A0ABF7PHA5 (a TrEMBL KRAS G12D entry) has no
   ChEMBL target mapping, so the pipeline's fallback picked cands[0] =
   CHEMBL2074 maltase-glucoamylase. The four "leads" are silylated
   iminosugars (alpha-glucosidase inhibitors, Ki 4-28 nM vs
   maltase-glucoamylase) -- not KRAS ligands at all.
2. Structure/centre: the pipeline picked 9S84 (KRAS G12D D38C, GDP-bound,
   1.64 A -- the protein is right) but _ligand_center fell back to the GDP
   centroid (GDP is the only HETATM group with >= 6 atoms once cofactors
   are excluded), i.e. the NUCLEOTIDE pocket. MRTX1133 binds the induced
   switch-II pocket, not the GDP pocket, so its -9.13 on 9S84 is meaningless.

Correction (documented fallback, HP-027 precedent):
- Structure 7RPZ: KRAS G12D in complex with MRTX1133, 1.3 A (Wang et al.
  J Med Chem 2022, 65:3123-3133, PMID 34889605). Centre =
  D._ligand_center (MRTX1133 centroid, switch-II pocket), audited against
  the Asp12 CA distance and against the GDP centroid distance.
- Compounds: MRTX1133 (reference; SMILES from the pipeline run, PubChem
  verified) + three Wang-series analogues whose co-crystal structures
  exist (compound 15 = 7RT1 ligand, compound 25 = 7RT2 ligand,
  compound 36 = 7RT5 ligand), SMILES from the RCSB chemical-component
  InChI (verified by molecular formula match -- the first attempt,
  MolFromPDBBlock on the deposited coordinates, produced wrong
  saturated structures and was discarded), + sotorasib (G12C
  covalent inhibitor) as the negative control -- it cannot bind G12D
  covalently (no Cys12) and has no measurable G12D activity.
- Measured potencies are all pERK AGS IC50s from Wang et al. 2022
  (same assay, same paper): MRTX1133 2 nM; 25: 24 nM; 36: 24 nM;
  15: 530 nM. Sotorasib carries NO measured G12D potency and is
  excluded from the rank correlation.
"""
import json
import math
import os
import sys
import urllib.request

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402
from rdkit import Chem  # noqa: E402
from rdkit.Chem import Descriptors, rdMolDescriptors  # noqa: E402

GOAL = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts"
OUT = os.path.join(GOAL, "hidden_files/dock-HP-069-2026-11-15-7RPZ.json")
PARTIAL = OUT + ".partial"
CACHE = os.path.join(GOAL, "hidden_files")
PDB = "7RPZ"

# (label, source, measured pERK AGS IC50 nM or None, notes)
COMPOUNDS = [
    ("MRTX1133-REF", "pipeline",
     2.0, "PubChem-verified MRTX1133 (reference drug); Wang 2022 Table 4: pERK AGS IC50 2 nM; KD ~0.0002 nM; 2D viability AGS 6 nM; MKN1 >3000 nM"),
    ("WANG-25", "chemcomp:7NL",
     24.0, "Wang 2022 compound 25 (eutomer of the 24/25 pair); pERK IC50 24 nM; co-crystal 7RT2; SMILES from RCSB chemcomp 7NL InChI"),
    ("WANG-36", "chemcomp:7OE",
     24.0, "Wang 2022 compound 36; biochemical activity <2 nM; pERK IC50 24 nM; co-crystal 7RT5; SMILES from RCSB chemcomp 7OE InChI"),
    ("WANG-15", "chemcomp:7L8",
     530.0, "Wang 2022 compound 15; SPR KD 0.8 nM, >200-fold selective vs KRAS WT (KD 182 nM); pERK IC50 0.530 uM; co-crystal 7RT1; SMILES from RCSB chemcomp 7L8 InChI"),
    ("SOTORASIB-NEG", "pubchem",
     None, "G12C covalent inhibitor (negative control): no Cys12 in G12D, no measurable G12D activity reported; excluded from rank correlation"),
]

MRTX1133_SMILES = "C#CC1=C(C=CC2=CC(=CC(=C21)C3=NC=C4C(=C3F)N=C(N=C4N5CC6CCC(C5)N6)OCC78CCCN7CC(C8)F)O)F"


def dl_pdb(pid):
    path = os.path.join(CACHE, f"{pid}.pdb")
    if not os.path.exists(path):
        req = urllib.request.Request(
            f"https://files.rcsb.org/download/{pid}.pdb",
            headers={"User-Agent": "LeadForge-research/1.0"})
        with urllib.request.urlopen(req, timeout=60) as r:
            open(path, "wb").write(r.read())
    return path


def rcsb_inchi_smiles(chemcomp_id):
    """SMILES for a PDB chemical component via the RCSB InChI (the
    PDB-coordinate extraction via MolFromPDBBlock produced wrong,
    saturated structures -- formulas did not match -- so it is NOT used)."""
    req = urllib.request.Request(
        f"https://data.rcsb.org/rest/v1/core/chemcomp/{chemcomp_id}",
        headers={"User-Agent": "LeadForge-research/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        d = json.loads(r.read().decode())
    inchi = d["rcsb_chem_comp_descriptor"]["InChI"]
    formula = d["chem_comp"]["formula"]
    mol = Chem.MolFromInchi(inchi)
    if mol is None:
        raise RuntimeError(f"MolFromInchi failed for {chemcomp_id}")
    smi = Chem.MolToSmiles(mol)
    got = rdMolDescriptors.CalcMolFormula(mol)
    if got.replace(" ", "") != formula.replace(" ", ""):
        raise RuntimeError(f"formula mismatch {chemcomp_id}: InChI {got} vs RCSB {formula}")
    return smi, formula


def pubchem_smiles(name):
    import urllib.parse
    url = ("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
           + urllib.parse.quote(name)
           + "/property/CanonicalSMILES,ConnectivitySMILES,MolecularFormula,Title/JSON")
    req = urllib.request.Request(url, headers={"User-Agent": "LeadForge-research/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        d = json.loads(r.read().decode())
    p = d["PropertyTable"]["Properties"][0]
    smi = p.get("CanonicalSMILES") or p.get("ConnectivitySMILES")
    if not smi:
        raise RuntimeError(f"no SMILES returned for {name}: {p}")
    return smi, p["MolecularFormula"]


def pains(smiles):
    from rdkit.Chem.FilterCatalog import FilterCatalog, FilterCatalogParams
    params = FilterCatalogParams()
    params.AddCatalog(FilterCatalogParams.FilterCatalogs.PAINS)
    cat = FilterCatalog(params)
    m = Chem.MolFromSmiles(smiles)
    return [e.GetDescription() for e in cat.GetMatches(m)]


def main():
    # --- resolve SMILES ---
    resolved = []
    for label, src, ic50, notes in COMPOUNDS:
        if label == "MRTX1133-REF":
            smi, formula = MRTX1133_SMILES, "C33H31F3N6O2"
        elif src == "pubchem":
            smi, formula = pubchem_smiles("sotorasib")
        elif src.startswith("chemcomp:"):
            cc = src.split(":", 1)[1]
            smi, formula = rcsb_inchi_smiles(cc)
            print(f"EXTRACT {label}: chemcomp {cc} formula {formula} SMILES {smi}", flush=True)
        m = Chem.MolFromSmiles(smi)
        assert m is not None, f"bad SMILES for {label}"
        dd = {"mw": round(Descriptors.MolWt(m), 2),
              "logp": round(Descriptors.MolLogP(m), 2),
              "hbd": rdMolDescriptors.CalcNumHBD(m),
              "hba": rdMolDescriptors.CalcNumHBA(m),
              "tpsa": round(rdMolDescriptors.CalcTPSA(m), 2),
              "rotatable": rdMolDescriptors.CalcNumRotatableBonds(m),
              "formula": rdMolDescriptors.CalcMolFormula(m)}
        resolved.append({"label": label, "smiles": smi, "formula_check": formula,
                         "descriptors": dd, "pains": pains(smi),
                         "measured_pERK_AGs_IC50_nM": ic50, "notes": notes})
        print(f"RESOLVED {label}: formula {dd['formula']} MW {dd['mw']} logP {dd['logp']} PAINS {resolved[-1]['pains']}", flush=True)

    # --- structure + centre audit ---
    pdb_path = dl_pdb(PDB)
    center = D._ligand_center(pdb_path)
    print("CENTRE 7RPZ:", center, flush=True)
    # audit: distance from centre to Asp12 CA and to GDP centroid
    asp12, gdp = None, []
    for ln in open(pdb_path):
        if ln.startswith("ATOM") and ln[17:20].strip() == "ASP" and ln[22:26].strip() == "12" and ln[12:16].strip() == "CA":
            asp12 = (float(ln[30:38]), float(ln[38:46]), float(ln[46:54]))
        if ln.startswith("HETATM") and ln[17:20].strip() == "GDP":
            gdp.append((float(ln[30:38]), float(ln[38:46]), float(ln[46:54])))
    def dist(a, b):
        return round(math.dist(a, b), 2)
    gdp_c = [sum(c[i] for c in gdp) / len(gdp) for i in range(3)] if gdp else None
    audit = {"centre": [round(c, 2) for c in center],
             "asp12_CA_distance_A": dist(center, asp12) if asp12 else None,
             "gdp_centroid_distance_A": dist(center, gdp_c) if gdp_c else None}
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
        r["measured_pERK_AGs_IC50_nM"] = c["measured_pERK_AGs_IC50_nM"]
        results.append(r)
        done[c["label"]] = r
        json.dump(done, open(PARTIAL, "w"), indent=1)
        print(f"DOCK {c['label']}: {r.get('affinity_kcal_mol')} ok={r.get('ok')} {r.get('error','')}", flush=True)
    results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))

    out = {"ok": True, "pdb_id": PDB, "resolution": 1.3, "center": audit["centre"],
           "centre_audit": audit, "compounds": resolved, "results": results,
           "correction_note": "Pipeline run dock-HP-069-2026-11-15.json is DISCARDED (wrong ChEMBL target CHEMBL2074 maltase-glucoamylase; GDP-pocket centre on 9S84). This file is the corrected docking on 7RPZ switch-II pocket."}
    json.dump(out, open(OUT, "w"), indent=1)
    print("SAVED:", OUT, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
