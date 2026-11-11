"""Fallback docking for HP-030 (FLT3 / gilteritinib), 2026-11-11.

Why this exists: ChEMBL activity endpoint returned HTTP 500 on 2026-11-11
(verified by direct curl: simple + ordered queries both 500; target endpoint
healthy, CHEMBL1974 resolved). Pipeline runs 1-3 therefore retrieved 0
ChEMBL ligands. Documented fallback (AGENTS.md, FLT3 precedent 2026-11-02):
PubChem fastsimilarity_2d analogues of the reference drug + docked known
FLT3 inhibitors as comparators. No measured potency is attached to the
PubChem analogues; comparator potencies come from the cited literature.

Protocol (identical for every compound): AutoDock Vina 1.2.7 via
app.discovery.dock.dock, PDB 6JQR (FLT3 kinase domain in complex with
gilteritinib, 2.20 A), grid centre [-28.04, -10.36, -28.99] = co-crystallised
gilteritinib (C6F) centroid via dock._ligand_center, box 22.5 A,
exhaustiveness 8, best of 3 poses. Centre verified: 6JQR is the FLT3
kinase-domain structure bound to gilteritinib itself (Amano 2019), so the
domain and binding site match the drug.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402
from app.discovery import chem as C  # noqa: E402
from rdkit import Chem  # noqa: E402
from rdkit.Chem import Descriptors, rdMolDescriptors  # noqa: E402

PDB = "6JQR"
CENTER = [-28.04, -10.36, -28.99]
BOX = 22.5

# (label, smiles, source, measured potency note)
COMPOUNDS = [
    ("GILTERITINIB-REF", "CCC1=C(N=C(C(=N1)C(=O)N)NC2=CC(=C(C=C2)N3CCC(CC3)N4CCN(CC4)C)OC)NC5CCOCC5",
     "PubChem CID 49803313 (reference drug)", "FLT3 IC50 0.29 nM (Mori 2017)"),
    ("QUIZARTINIB", "CC(C)(C)C1=CC(=NO1)NC(=O)NC2=CC=C(C=C2)C3=CN4C5=C(C=C(C=C5)OCCN6CCOCC6)SC4=N3",
     "PubChem CID 24889392", "FLT3-ITD autophosphorylation IC50 1.1 nM (Zarrinkar 2009)"),
    ("MIDOSTAURIN", "CC12C(C(CC(O1)N3C4=CC=CC=C4C5=C6C(=C7C8=CC=CC=C8N2C7=C53)CNC6=O)N(C)C(=O)C9=CC=CC=C9)OC",
     "PubChem CID 9829523", "FLT3 Kd 7.9 nM (2020 selectivity panel)"),
    ("CRENOLANIB", "CC1(COC1)COC2=CC3=C(C=C2)N(C=N3)C4=NC5=C(C=CC=C5N6CCC(CC6)N)C=C4",
     "PubChem CID 10366136", "FLT3 Kd 0.74 nM (Galanis 2014)"),
    ("SORAFENIB", "CNC(=O)C1=NC=CC(=C1)OC2=CC=C(C=C2)NC(=O)NC3=CC(=C(C=C3)Cl)C(F)(F)F",
     "PubChem CID 216239", "FLT3 IC50 59 nM (Wilhelm 2004)"),
]

# PubChem fastsimilarity_2d analogues of gilteritinib (threshold 85, 2026-11-11)
ANALOGUES = [
    ("PUBCHEM-66642864", "CCC1=C(N=C(C(=N1)C(=O)N)NC2=CC(=C(C=C2)N3CCC(CC3)N4CCN(CC4)C)OC)NC5CCC(CC5)O",
     "PubChem CID 66642864, 4-hydroxycyclohexyl analogue"),
    ("PUBCHEM-124086185", "CCC1=NC(=C(C=C1NC2CCOCC2)NC3=CC(=C(C=C3)N4CCC(CC4)N5CCN(CC5)C)OC)C(=O)N",
     "PubChem CID 124086185"),
    ("PUBCHEM-166626288", "CCC1=C(N=C(C(=N1)C(=O)N)NC2=CC(=C(C=C2)N3CCC(CC3)N4CCNCC4)OC)NC5CCOCC5",
     "PubChem CID 166626288, N-desmethyl-piperazine analogue"),
    ("PUBCHEM-138319679", "CCC1=C(N=C(C(=N1)C(=O)N)NC2=CC(=C(C=C2)N3CCC(CC3)N4CCN(CC4)C)OC)NC5CCC(CC5)OC",
     "PubChem CID 138319679, 4-methoxycyclohexyl analogue"),
    ("PUBCHEM-155533199", "CCC1=C(N=C(C(=N1)C(=O)N)NC2=CC(=C(C=C2)N3CCC(CC3)N4CCN(CC4)C)OC)NC(C)C",
     "PubChem CID 155533199, isopropylamino analogue"),
    ("PUBCHEM-66642725", "CCC1=C(N=C(C(=N1)C(=O)N)NC2=C(C=C(C=C2)N3CCC(CC3)N4CCN(CC4)C)OC)NC5CCC(CC5)O",
     "PubChem CID 66642725, 2-methoxy regioisomer analogue"),
    ("PUBCHEM-150967523", "CN1CCN(CC1)C2=CC(=C(C=C2)NC3=NC(=C(C=C3)N4CCCCC4)OC5=CC=CC(=C5)NC(=O)C=C)OC",
     "PubChem CID 150967523, acrylamide scaffold analogue"),
]

OUT = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-030-2026-11-11.json"


def canon(smi):
    m = Chem.MolFromSmiles(smi)
    return Chem.MolToSmiles(m) if m else None


def main():
    ref_canon = canon(COMPOUNDS[0][1])
    seen = {ref_canon}
    todo = []
    for label, smi, src, pot in COMPOUNDS:
        todo.append((label, smi, src, pot))
    for label, smi, src in ANALOGUES:
        if "." in smi:
            print(f"SKIP {label}: multi-component (salt)", flush=True)
            continue
        c = canon(smi)
        if c is None:
            print(f"SKIP {label}: unparseable SMILES", flush=True)
            continue
        if c in seen:
            print(f"SKIP {label}: duplicate of an already-listed compound", flush=True)
            continue
        seen.add(c)
        todo.append((label, smi, src, "no measured potency (PubChem similarity analogue)"))

    results = []
    for label, smi, src, pot in todo:
        m = Chem.MolFromSmiles(smi)
        desc = {
            "mw": round(Descriptors.MolWt(m), 2),
            "logp": round(Descriptors.MolLogP(m), 2),
            "hbd": rdMolDescriptors.CalcNumHBD(m),
            "hba": rdMolDescriptors.CalcNumHBA(m),
            "tpsa": round(rdMolDescriptors.CalcTPSA(m), 2),
            "rotatable": rdMolDescriptors.CalcNumRotatableBonds(m),
        }
        pa = C.pains(smi)
        r = D.dock(smi, PDB, CENTER, box_size=BOX)
        r["label"] = label
        r["source"] = src
        r["measured_potency"] = pot
        r["descriptors"] = desc
        r["pains"] = pa
        print(f"DOCK {label}: {r.get('affinity_kcal_mol')} ok={r.get('ok')} pains={pa}", flush=True)
        results.append(r)

    results_sorted = sorted(results, key=lambda x: x.get("affinity_kcal_mol", 999))
    out = {
        "topic": {"target": "FMS-like tyrosine kinase 3 (FLT3)", "reference": "gilteritinib"},
        "target": {"uniprot": {"accession": "P36888", "gene": "FLT3",
                               "protein": "Receptor-type tyrosine-protein kinase FLT3",
                               "organism": "Homo sapiens"},
                   "chembl_target": "CHEMBL1974"},
        "chembl_status": "activity endpoint HTTP 500 on 2026-11-11 (verified by direct curl); "
                         "fallback = PubChem fastsimilarity_2d analogues + known FLT3 inhibitors",
        "docking": {"ok": True, "pdb_id": PDB, "resolution": 2.2,
                    "center": CENTER,
                    "center_note": "co-crystallised gilteritinib (C6F) centroid via dock._ligand_center; "
                                   "6JQR is the FLT3 kinase domain bound to gilteritinib itself",
                    "box_size": BOX, "exhaustiveness": 8,
                    "results": results_sorted},
        "pipeline_run1": "hidden_files/dock-HP-030-2026-11-11-RUN1-QUERY-ONLY.json "
                         "(gilteritinib re-dock -8.01 on 6JQR; ChEMBL target lookup failed then)",
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("SAVED:", OUT, flush=True)


if __name__ == "__main__":
    main()
