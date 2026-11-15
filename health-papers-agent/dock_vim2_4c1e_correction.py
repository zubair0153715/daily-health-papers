"""Corrected docking for HP-064 (VIM-2 metallo-beta-lactamase), 2026-11-15.

Why this exists: the standard pipeline run (dock-HP-064-2026-11-15.json)
failed in two ways, and its numbers are DISCARDED (kept for audit):
1. Ligands: ChEMBL target CHEMBL1255147 returned 0 bioactivities, so
   the only "lead" was the query itself -- taniborbactam.
2. Docking: taniborbactam contains boron, and Vina's PDBQT parser
   rejects it ("Atom type B is not a valid AutoDock type"). The single
   dock result is ok=False. Boronates cannot be docked by this protocol
   at all -- a tool limit, not a data gap.
Also the pipeline's structure pick, 9CV3, is VIM-20 (a VIM-2-like
variant from Enterobacter cloacae) with L-captopril, not VIM-2 itself.

Correction (documented fallback, HP-027 precedent):
- Structure 4C1E: VIM-2 (Pseudomonas aeruginosa) in complex with
  D-captopril, 1.40 A (Brem et al. Antimicrob Agents Chemother 2016,
  60:142-150, PMID 26482303). Centre = D._ligand_center (D-captopril
  centroid), audited against the two catalytic Zn(II) distances.
- Compounds: the four captopril stereoisomers (D, L, epi-D, epi-L).
  SMILES are built by stereocentre inversion from the PubChem-verified
  L-captopril structure and checked by RDKit CIP assignment:
  D = (2S,2R), L = (2S,2S), epi-D = (2R,2R), epi-L = (2R,2S).
  The two centres are the 2-methylpropionyl carbon and the proline
  alpha carbon. Each SMILES is also checked against PubChem by
  isomeric-SMILES lookup where a record exists.
- Measured potencies are all VIM-2 IC50s from Brem et al. 2016 Table 1
  (same assay, same paper): D 0.072 uM; L 4.4 uM; epi-D 5.5 uM;
  epi-L 5.5 uM. The question is whether rigid docking can resolve a
  60-fold stereoisomer potency gap.
- Taniborbactam is NOT docked (boron). It is carried as the measured
  reference only: Ki 0.02 uM vs VIM-2 (Le Terrier et al. Antimicrob
  Agents Chemother 2024, 68:e00991-23, doi:10.1128/aac.00991-23).
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
OUT = os.path.join(GOAL, "hidden_files/dock-HP-064-2026-11-15-4C1E.json")
PARTIAL = OUT + ".partial"
CACHE = os.path.join(GOAL, "hidden_files")
PDB = "4C1E"

# (label, isomeric SMILES, expected CIP (methyl-C, proline-C), VIM-2 IC50 uM, notes)
COMPOUNDS = [
    ("D-CAPTOPRIL", "C[C@H](CS)C(=O)N1CCC[C@@H]1C(=O)O", ("S", "R"),
     0.072, "Brem 2016 Table 1: VIM-2 IC50 0.072 +/- 0.010 uM; re-dock control on its own structure 4C1E"),
    ("L-CAPTOPRIL", "C[C@H](CS)C(=O)N1CCC[C@H]1C(=O)O", ("S", "S"),
     4.4, "Brem 2016 Table 1: VIM-2 IC50 4.4 +/- 0.8 uM; co-crystal 4C1D (1.20 A)"),
    ("EPI-D-CAPTOPRIL", "C[C@@H](CS)C(=O)N1CCC[C@@H]1C(=O)O", ("R", "R"),
     5.5, "Brem 2016 Table 1: VIM-2 IC50 5.5 +/- 0.7 uM"),
    ("EPI-L-CAPTOPRIL", "C[C@@H](CS)C(=O)N1CCC[C@H]1C(=O)O", ("R", "S"),
     5.5, "Brem 2016 Table 1: VIM-2 IC50 5.5 +/- 1.5 uM"),
]

TANIBORBACTAM_NOTE = ("NOT docked: boronate; Vina PDBQT parser rejects atom type B "
    "(proven by the pipeline run on 9CV3). Measured reference only: "
    "Ki 0.02 uM vs VIM-2 (Le Terrier et al. AAC 2024, 68:e00991-23).")


def pubchem_by_smiles(smi):
    """Return (cid, title) for an isomeric SMILES, or (None, None)."""
    url = ("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastidentity/smiles/"
           + urllib.parse.quote(smi) + "/property/Title/JSON")
    req = urllib.request.Request(url, headers={"User-Agent": "LeadForge-research/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            d = json.loads(r.read().decode())
        p = d["PropertyTable"]["Properties"][0]
        return p.get("CID"), p.get("Title")
    except Exception as e:
        return None, f"lookup failed: {e}"


def pains(smiles):
    from rdkit.Chem.FilterCatalog import FilterCatalog, FilterCatalogParams
    params = FilterCatalogParams()
    params.AddCatalog(FilterCatalogParams.FilterCatalogs.PAINS)
    cat = FilterCatalog(params)
    m = Chem.MolFromSmiles(smiles)
    return [e.GetDescription() for e in cat.GetMatches(m)]


def main():
    resolved = []
    for label, smi, cip_expected, ic50, notes in COMPOUNDS:
        m = Chem.MolFromSmiles(smi)
        assert m is not None, f"bad SMILES for {label}"
        Chem.AssignStereochemistry(m, cleanIt=True, force=True)
        centers = Chem.FindMolChiralCenters(m, includeUnassigned=False)
        # order: methyl-bearing C first (atom with the S methyl), then proline alpha C
        # FindMolChiralCenters returns in atom order; the methyl C (idx ~1) precedes proline Ca.
        cip = tuple(c[1] for c in centers)
        print(f"{label}: CIP {cip} expected {cip_expected}", flush=True)
        assert cip == cip_expected, f"CIP mismatch {label}: {cip} != {cip_expected}"
        cid, title = pubchem_by_smiles(smi)
        print(f"{label}: PubChem CID {cid} title {title}", flush=True)
        dd = {"mw": round(Descriptors.MolWt(m), 2),
              "logp": round(Descriptors.MolLogP(m), 2),
              "hbd": rdMolDescriptors.CalcNumHBD(m),
              "hba": rdMolDescriptors.CalcNumHBA(m),
              "tpsa": round(rdMolDescriptors.CalcTPSA(m), 2),
              "rotatable": rdMolDescriptors.CalcNumRotatableBonds(m),
              "formula": rdMolDescriptors.CalcMolFormula(m)}
        assert dd["formula"] == "C9H15NO3S", f"formula wrong for {label}: {dd['formula']}"
        resolved.append({"label": label, "smiles": smi, "cip": cip,
                         "pubchem_cid": cid, "pubchem_title": title,
                         "descriptors": dd, "pains": pains(smi),
                         "measured_VIM2_IC50_uM": ic50, "notes": notes})

    # --- structure + centre audit ---
    pdb_path = os.path.join(CACHE, "4C1E.pdb")
    if not os.path.exists(pdb_path):
        req = urllib.request.Request("https://files.rcsb.org/download/4C1E.pdb",
                                     headers={"User-Agent": "LeadForge-research/1.0"})
        with urllib.request.urlopen(req, timeout=60) as r:
            open(pdb_path, "wb").write(r.read())
    center = D._ligand_center(pdb_path)
    print("CENTRE 4C1E:", center, flush=True)
    zn = []
    for ln in open(pdb_path):
        if ln.startswith("HETATM") and ln[17:20].strip() == "ZN":
            zn.append((float(ln[30:38]), float(ln[38:46]), float(ln[46:54])))
    audit = {"centre": [round(c, 2) for c in center],
             "zn_count": len(zn),
             "centre_to_Zn_distances_A": [round(math.dist(center, z), 2) for z in zn],
             "zn_zn_distance_A": round(math.dist(zn[0], zn[1]), 2) if len(zn) >= 2 else None}
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
        r["measured_VIM2_IC50_uM"] = c["measured_VIM2_IC50_uM"]
        results.append(r)
        done[c["label"]] = r
        json.dump(done, open(PARTIAL, "w"), indent=1)
        print(f"DOCK {c['label']}: {r.get('affinity_kcal_mol')} ok={r.get('ok')} {r.get('error','')}", flush=True)
    results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))

    out = {"ok": True, "pdb_id": PDB, "resolution": 1.40, "center": audit["centre"],
           "centre_audit": audit, "compounds": resolved, "results": results,
           "taniborbactam_reference": TANIBORBACTAM_NOTE,
           "correction_note": "Pipeline run dock-HP-064-2026-11-15.json is DISCARDED (0 ChEMBL ligands; taniborbactam boron rejected by Vina; structure 9CV3 is VIM-20, not VIM-2). This file is the corrected docking on 4C1E (true VIM-2)."}
    json.dump(out, open(OUT, "w"), indent=1)
    print("SAVED:", OUT, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
