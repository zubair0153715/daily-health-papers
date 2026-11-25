"""M2 correction dock for HP-133 (2026-11-25) — amantadine, rimantadine,
M2WJ332 on 3C9J (WT, amantadine-bound) and 2LY0 (S31N, M2WJ332-bound).

Why this run exists: the pipeline (dock-HP-133-2026-11-25.json) resolved
the target correctly (UniProt Q0HD59, Matrix protein 2, Influenza A) but
its ChEMBL target lookup mismatched to CHEMBL2074 (maltase-glucoamylase),
so the 55 "known ligands" are glucosidase inhibitors, not M2 ligands, and
the similarity screen (Tanimoto 0.10-0.13 vs amantadine) is meaningless for
this target. The auto-picked structure 5TTC then had no ligand site, so
docking was SKIPPED. The comparison set is therefore built from the
literature, with SMILES verified live against PubChem by name/CID:
  amantadine  CID 2130  C10H17N  (reference; WT-active, S31N-resistant)
  rimantadine CID 5071  C12H21N  (WT-active, S31N-resistant)
  M2WJ332     CID 70680222 C18H22N2OS (S31N inhibitor; Wang et al. PNAS
              2013, PMID 23302696: TEVC IC50 16 uM vs S31N; plaque EC50
              153 nM vs S31N, vs amantadine 328 nM vs WT)
M2WJ379 and M2WJ352 were NOT added: neither resolves in PubChem by name
(404), and no SMILES is invented here.

Centre audit (never hand-rolled):
  3C9J — 3.5 A X-ray, M2 TM (22-46) + amantadine, Stouffer et al. Nature
    2008, PMID 18235504. HETNAM/HETSYN confirm residue 308 IS amantadine.
    dock._ligand_center = [-14.94, 13.97, -4.63] (11 heavy atoms).
    Caveat: the construct is the G34A mutant, not WT.
  2LY0 — solution NMR, M2-S31N (19-49) + M2WJ332, Wang et al. PNAS 2013.
    dock._ligand_center (pooled over 22 models) = [0.14, 7.60, 0.83];
    model-1-only centroid = [0.13, 7.25, 0.74] — agrees within 0.4 A,
    so the pooled centre is used. Receptor prep uses model 1 only.
Box 22.5 A, exhaustiveness 8, best of 3 poses — same protocol as Papers
#1/#3. M2 is a small membrane channel; the pore is narrow, so poses are
reported with the membrane/pose caveat in the manuscript.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402
from rdkit import Chem  # noqa: E402
from rdkit.Chem import Descriptors, Lipinski, rdMolDescriptors  # noqa: E402
from rdkit.Chem.FilterCatalog import FilterCatalog, FilterCatalogParams  # noqa: E402

BASE = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts"
OUT = f"{BASE}/hidden_files/dock-HP-133-2026-11-25-3C9J.json"
OUT2 = f"{BASE}/hidden_files/dock-HP-133-2026-11-25-2LY0.json"

COMPOUNDS = [
    ("amantadine (QUERY, reference)", "C1C2CC3CC1CC(C2)(C3)N",
     "PubChem CID 2130, C10H17N; WT-active, S31N-resistant; approved 1966"),
    ("rimantadine", "CC(C12CC3CC(C1)CC(C3)C2)N",
     "PubChem CID 5071, C12H21N; WT-active, S31N-resistant; approved 1993"),
    ("M2WJ332", "C1C2CC3CC1CC(C2)(C3)NCC4=NOC(=C4)C5=CC=CS5",
     "PubChem CID 70680222, C18H22N2OS; S31N inhibitor, PNAS 2013 PMID 23302696"),
]

STRUCTURES = [
    ("3C9J", [-14.94, 13.97, -4.63],
     "3.5 A X-ray, M2 TM + amantadine (residue 308, HETNAM-confirmed), "
     "Stouffer et al. Nature 2008 PMID 18235504; G34A mutant construct",
     OUT),
    ("2LY0", [0.14, 7.60, 0.83],
     "solution NMR, M2-S31N (19-49) + M2WJ332 (A2Y), Wang et al. PNAS 2013 "
     "PMID 23302696; centre pooled over 22 models, model-1 centroid agrees "
     "within 0.4 A; receptor = model 1",
     OUT2),
]


def descriptors(smiles):
    m = Chem.MolFromSmiles(smiles)
    params = FilterCatalogParams()
    params.AddCatalog(FilterCatalogParams.FilterCatalogs.PAINS)
    cat = FilterCatalog(params)
    pains = [e.GetDescription() for e in cat.GetMatches(m)]
    mw = Descriptors.MolWt(m)
    logp = Descriptors.MolLogP(m)
    hbd = Lipinski.NumHDonors(m)
    hba = Lipinski.NumHAcceptors(m)
    tpsa = rdMolDescriptors.CalcTPSA(m)
    rot = Lipinski.NumRotatableBonds(m)
    viol = sum([mw > 500, logp > 5, hbd > 5, hba > 10])
    return {"mw": round(mw, 2), "logp": round(logp, 2), "hbd": hbd, "hba": hba,
            "tpsa": round(tpsa, 2), "rotatable": rot,
            "lipinski_violations": viol,
            "lipinski_pass": viol == 0,
            "formula": rdMolDescriptors.CalcMolFormula(m)}, pains


def main():
    for pdb_id, center, center_note, out_path in STRUCTURES:
        results = []
        for label, smiles, note in COMPOUNDS:
            desc, pains = descriptors(smiles)
            r = D.dock(smiles, pdb_id, center, box_size=22.5)
            r["label"] = label
            r["note"] = note
            r["descriptors"] = desc
            r["pains"] = pains
            results.append(r)
            print("DOCK", pdb_id, ":", label, r.get("affinity_kcal_mol"),
                  r.get("ok"), "PAINS:", pains, flush=True)
        results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
        out = {
            "topic": {"target": "Influenza A M2 proton channel",
                      "reference": "amantadine",
                      "topic_id": "HP-133", "date": "2026-11-25"},
            "docking": {
                "ok": True, "pdb_id": pdb_id,
                "center": center, "center_note": center_note,
                "box_size": 22.5, "exhaustiveness": 8,
                "correction_note": (
                    "Pipeline ChEMBL lookup mismatched to CHEMBL2074 "
                    "(maltase-glucoamylase); its 55 ligands are glucosidase "
                    "inhibitors, not M2 ligands. Auto-picked 5TTC had no "
                    "ligand site, so pipeline docking was skipped. This run "
                    "docks the literature set (PubChem-verified SMILES) on "
                    "the amantadine-bound WT structure and the "
                    "M2WJ332-bound S31N structure."),
                "results": results,
            },
        }
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(out, f, indent=1)
        print("SAVED:", out_path, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
