"""HRV 3C correction dock for HP-136 (2026-11-25) — rupintrivir + AG7404 + SG85.

Why this run exists: the pipeline's target resolution was WRONG. It
resolved "Human rhinovirus 3C protease" to UniProt Q9BYX4 (IFIH1/MDA5, a
HUMAN innate-immune helicase, gene IFIH1, 1025 aa) and ChEMBL returned
unrelated human targets (maltase-glucoamylase etc.). Its auto-picked
structure 3GA3 is the C-terminal domain of human MDA5 (1.45 A, Zn ion
only) — NOT a viral protease — and dock_leads failed with no_ligand_site.
Nothing from that run is used for docking; only the QUERY SMILES
(rupintrivir, verified by PubChem in pipeline step 3) is carried over.

Correct structures (verified by search + RCSB/PDBj records):
- 1CQQ: HRV2 3C protease + AG7088 (= rupintrivir), 1.85 A (Matthews et al.,
  PNAS 1999) — the reference drug's own co-crystal, PRIMARY.
- 6KU8: HRV-C15 3C protease + rupintrivir, 2.05 A (Yuan et al., Virol Sin
  2020) — cross-species check (HRV-C, the species with no vaccine and
  the most severe lower-airway disease).

Centres: computed with dock._ligand_center (largest drug-like HETATM
group, excludes cofactors/modified residues) — never hand-rolled.
Compounds: rupintrivir (reference, QUERY), AG7404 (modified rupintrivir
derivative; Lee et al., IUCrJ 2026 — HRV-B14 3C IC50 0.046 uM, EC50
0.108-0.191 uM), SG85 (enterovirus 3C inhibitor, not cross-resistant
with rupintrivir; Antimicrob Agents Chemother 2015). SMILES for AG7404
(CID 5280053, C26H29N5O7) and SG85 (CID 52914324, C35H46N4O8) verified
via PubChem PUG REST 2026-11-25; rupintrivir SMILES from the pipeline
QUERY (PubChem-verified).

HONEST LIMIT: rupintrivir and AG7404 are COVALENT irreversible
inhibitors (Michael acceptor binds the catalytic Cys). Vina scores only
non-covalent complementarity — the covalent bond energy is NOT modelled,
so these scores UNDERESTIMATE the reference drug's true binding. The
table is a non-covalent ranking, not a potency ranking.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402
from rdkit import Chem  # noqa: E402
from rdkit.Chem import Descriptors, Lipinski, rdMolDescriptors  # noqa: E402
from rdkit.Chem.FilterCatalog import FilterCatalog, FilterCatalogParams  # noqa: E402

BASE = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts"

# Rupintrivir SMILES carried over from the pipeline QUERY (PubChem-verified).
COMPOUNDS = [
    ("rupintrivir (QUERY, reference)", "CCOC(=O)C=CC(CC1CCNC1=O)NC(=O)C(CC2=CC=C(C=C2)F)CC(=O)C(C(C)C)NC(=O)C3=NOC(=C3)C",
     "Reference drug; irreversible HRV 3C inhibitor (AG7088); clinical development stopped after natural-infection trials failed"),
    ("AG7404", "CCOC(=O)/C=C/[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC#C)N2C=CC=C(C2=O)NC(=O)C3=NOC(=C3)C",
     "Modified rupintrivir derivative; oral; HRV-B14 3C IC50 0.046 uM (Lee et al., IUCrJ 2026)"),
    ("SG85", "CCOC(=O)/C=C/[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC2=CC=CC=C2)NC(=O)[C@H](COC(C)(C)C)NC(=O)OCC3=CC=CC=C3",
     "Enterovirus 3C inhibitor; blocks rhinovirus replication, NOT cross-resistant with rupintrivir (AAC 2015)"),
]

STRUCTURES = [
    ("1CQQ", 1.85, "HRV2 3C protease + AG7088 (rupintrivir), Matthews et al., PNAS 1999"),
    ("6KU8", 2.05, "HRV-C15 3C protease + rupintrivir, Yuan et al., Virol Sin 2020"),
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
    for pdb_id, resolution, note in STRUCTURES:
        pdb_path = D._pdb_path(pdb_id)
        center = D._ligand_center(pdb_path)
        print("CENTER", pdb_id, center, note, flush=True)
        if center is None:
            print("  NO CENTRE — skipping", pdb_id, flush=True)
            continue
        results = []
        for label, smiles, cnote in COMPOUNDS:
            desc, pains = descriptors(smiles)
            r = D.dock(smiles, pdb_id, center, box_size=22.5)
            r["label"] = label
            r["note"] = cnote
            r["descriptors"] = desc
            r["pains"] = pains
            results.append(r)
            print("DOCK", pdb_id, ":", label, r.get("affinity_kcal_mol"),
                  r.get("ok"), "PAINS:", pains, flush=True)
        results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
        out = {
            "topic": {"target": "Human rhinovirus 3C protease",
                      "reference": "rupintrivir (AG7088)",
                      "topic_id": "HP-136", "date": "2026-11-25"},
            "docking": {
                "ok": True, "pdb_id": pdb_id, "resolution": resolution,
                "center": center,
                "center_note": ("co-crystallised rupintrivir centroid — "
                                "verified by dock._ligand_center; " + note),
                "box_size": 22.5, "exhaustiveness": 8,
                "correction_note": ("Pipeline resolved the target to human "
                                    "IFIH1/MDA5 (Q9BYX4) and auto-picked 3GA3 "
                                    "(human MDA5 C-terminal domain, Zn only) "
                                    "— wrong protein entirely; dock_leads "
                                    "failed no_ligand_site. This run uses "
                                    "the real viral 3C structures. "
                                    "COVALENT LIMIT: rupintrivir/AG7404 bind "
                                    "the catalytic Cys irreversibly; Vina "
                                    "scores non-covalent complementarity "
                                    "only, so the reference score "
                                    "underestimates true binding."),
                "results": results,
            },
        }
        out_path = f"{BASE}/hidden_files/dock-HP-136-2026-11-25-{pdb_id}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(out, f, indent=1)
        print("SAVED:", out_path, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
