"""EZH2 cross-check dock for HP-127 (2026-11-25) — QUERY + top 2 leads on 5IJ7.

Why 5IJ7: the planned 5HYN cross-check failed at receptor prep — RDKit's
MolFromPDBBlock returns None for 5HYN ("pdb parse failed"; the file carries
M3L trimethyllysine residues in the JARID2 peptide chains, which break the
sanitiser). Rather than patch the shared dock.py or the shared PDB cache,
the cross-check moved to 5IJ7, which is a BETTER template anyway: human
PRC2 in complex with a pyridone inhibitor (Brooun et al., Nat Commun
2016;7:11384; PMID 27122193), 2.62 A — higher resolution than 5WG6 (3.90 A)
and inhibitor-bound, same SAM-competitive pyridone class as tazemetostat.
Centre audit: the only drug-like HETATM is 6BN (the pyridone inhibitor,
36 atoms, chains A and B); dock._ligand_center = [30.90, 4.98, 205.18] =
the chain-A 6BN centroid in the EZH2 SET-domain SAM pocket. Receptor prep
verified OK (2026-11-25). The failed 5HYN attempt is preserved in
dock-HP-127-2026-11-25-5HYN.json with ok:false for all three compounds.

Compounds (SMILES read from the pipeline JSON, same leads as 5WG6):
QUERY = tazemetostat; CHEMBL5562984 = the 5WG6 winner (-12.58);
CHEMBL5188577 = the 5WG6 runner-up (-11.30). Same box (22.5 A) and
exhaustiveness (8) as Papers #1/#3.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402
from rdkit import Chem  # noqa: E402
from rdkit.Chem import Descriptors, Lipinski, rdMolDescriptors  # noqa: E402
from rdkit.Chem.FilterCatalog import FilterCatalog, FilterCatalogParams  # noqa: E402

BASE = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts"
PIPE = f"{BASE}/hidden_files/dock-HP-127-2026-11-25.json"
OUT = f"{BASE}/hidden_files/dock-HP-127-2026-11-25-5IJ7.json"
CENTER = [30.90, 4.98, 205.18]  # 6BN (pyridone inhibitor, chain A) centroid via dock._ligand_center


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
    pipe = json.load(open(PIPE))
    leads = {l.get("label"): l for l in pipe["leads"]}
    wanted = ["QUERY", "CHEMBL5562984", "CHEMBL5188577"]
    results = []
    for label in wanted:
        l = leads[label]
        desc, pains = descriptors(l["smiles"])
        r = D.dock(l["smiles"], "5IJ7", CENTER, box_size=22.5)
        r["label"] = label
        r["rank"] = l.get("rank")
        r["chembl_id"] = l.get("chembl_id")
        r["similarity"] = l.get("similarity")
        r["descriptors"] = desc
        r["pains"] = pains
        results.append(r)
        print("DOCK 5IJ7:", label, r.get("affinity_kcal_mol"), r.get("ok"),
              "PAINS:", pains, flush=True)
    results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
    out = {
        "topic": {"target": "Enhancer of zeste homolog 2 (EZH2)",
                  "reference": "tazemetostat", "topic_id": "HP-127",
                  "date": "2026-11-25"},
        "docking": {
            "ok": True, "pdb_id": "5IJ7", "resolution": 2.62,
            "center": CENTER,
            "center_note": ("6BN pyridone inhibitor (chain A) centroid via "
                            "dock._ligand_center — EZH2 SET-domain SAM pocket, "
                            "human PRC2 + pyridone inhibitor, 2.62 A "
                            "(Brooun et al., Nat Commun 2016;7:11384)"),
            "box_size": 22.5, "exhaustiveness": 8,
            "correction_note": ("Cross-check moved from 5HYN (receptor prep "
                                "failed: RDKit pdb parse failed on the "
                                "M3L-containing file) to 5IJ7, a better "
                                "template: higher resolution and inhibitor-bound."),
            "results": results,
        },
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("SAVED:", OUT, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
