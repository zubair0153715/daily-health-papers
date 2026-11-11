import sys, json
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D
from rdkit import Chem
from rdkit.Chem import Descriptors, rdMolDescriptors
from rdkit.Chem.FilterCatalog import FilterCatalog, FilterCatalogParams

CENTER = [15.51, 20.21, 7.63]
PDB = "1RGZ"

leads = [
    ("CHEMBL212760", "O=C([O-])C1=CS[C@@H]2/C(=C\\c3cc4n(n3)CCSC4)C(=O)N12.[Na+]", 9.00, "IC50 1.0 nM"),
    ("CHEMBL222758", "O=C([O-])C1=CS[C@@H]2/C(=C\\c3cn4c(n3)sc3ccccc34)C(=O)N12.[Na+]", 9.00, "IC50 1.0 nM"),
    ("CHEMBL222375", "Cc1ccc2c(c1)sc1nc(/C=C3/C(=O)N4C(C(=O)[O-])=CS[C@H]34)cn12.[Na+]", 9.00, "IC50 1.0 nM"),
    ("CHEMBL378119", "O=C([O-])C1=CS[C@@H]2/C(=C\\c3cc4n(n3)CCS(=O)(=O)C4)C(=O)N12.[Na+]", 8.70, "IC50 2.0 nM"),
    ("CHEMBL425963", "O=C([O-])C1=CS[C@@H]2/C(=C\\c3cn4c(n3)CSCC4)C(=O)N12.[Na+]", 8.70, "IC50 2.0 nM"),
]
params = FilterCatalogParams()
params.AddCatalog(FilterCatalogParams.FilterCatalogs.PAINS)
catalog = FilterCatalog(params)
out = {"pdb_id": PDB, "center": CENTER, "box_size": 22.5, "desalted": True, "results": []}
for label, smi, pchembl, meas in leads:
    # desalt: keep largest fragment
    mol = Chem.MolFromSmiles(smi)
    frags = Chem.GetMolFrags(mol, asMols=True)
    main = max(frags, key=lambda m: m.GetNumAtoms())
    clean = Chem.MolToSmiles(main)
    pains = [e.GetDescription() for e in catalog.GetMatches(main)]
    desc = {
        "mw": round(Descriptors.MolWt(main), 2),
        "logp": round(Descriptors.MolLogP(main), 2),
        "hbd": rdMolDescriptors.CalcNumHBD(main),
        "hba": rdMolDescriptors.CalcNumHBA(main),
        "tpsa": round(rdMolDescriptors.CalcTPSA(main), 2),
        "rotatable": rdMolDescriptors.CalcNumRotatableBonds(main),
    }
    r = D.dock(clean, PDB, CENTER, box_size=22.5)
    r["label"] = label
    r["pchembl"] = pchembl
    r["measured"] = meas
    r["smiles_desalted"] = clean
    r["smiles_chembl"] = smi
    r["descriptors"] = desc
    r["pains"] = pains
    out["results"].append(r)
    print("DOCK:", label, r.get("affinity_kcal_mol"), r.get("poses"), "PAINS:", pains, "MW:", desc["mw"], "logP:", desc["logp"], flush=True)
json.dump(out, open("dock-HP-016-2026-11-11-desalted.json", "w"), indent=1)
print("SAVED", flush=True)
