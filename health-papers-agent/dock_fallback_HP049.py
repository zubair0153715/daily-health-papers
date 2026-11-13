"""Fallback docking for HP-049 (JAK2 / ruxolitinib), 2026-11-13.

Why this exists: ChEMBL API is DOWN across all endpoints on 2026-11-13
(HTTP 500). The standard pipeline retrieved 0 ligands; it did dock the
reference ruxolitinib on 8BXH (-8.71), which is the CORRECT structure
(JAK2 JH1 + momelotinib, 1.3 A, Miao 2024) -- but with no comparators
the run is a single-compound result, not a benchmark. This script
re-docks ruxolitinib plus the other three approved myelofibrosis
JAKinibs and two JAK1-leaning comparators on the same structure and
centre, under one protocol (documented fallback, AGENTS.md FLT3
precedent).

Structure: 8BXH, JAK2 JH1 in complex with momelotinib, 1.3 A X-ray
(Miao et al. 2024, J Med Chem 67:10012-10024, PMID 38843875). Centre =
D._ligand_center (momelotinib centroid), audited below against the
largest HETATM group centroid.

Measured potencies: Miao et al. 2024 Table 1 (single head-to-head
assay, 1 mM ATP) -- JAK2 Kd / IC50: ruxolitinib 0.8 / 3.2 nM,
fedratinib 4.3 / 10 nM, momelotinib 6.7 / 11 nM, pacritinib 6.6 /
14 nM. Tofacitinib and baricitinib carry NO head-to-head value from
that table; they enter as selectivity comparators only.
"""
import json
import math
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402
from app.discovery import chem as C  # noqa: E402
from rdkit import Chem  # noqa: E402
from rdkit.Chem import Descriptors, rdMolDescriptors  # noqa: E402

OUT = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-049-2026-11-13.json"
PARTIAL = OUT + ".partial"
PDB = "8BXH"

# Incremental-save + resume (see dock_fallback_HP013.py): the HP-013 run was
# killed by the runtime (SIGTERM) at 14/16 docks with no JSON saved. This
# script saves after EVERY dock and resumes from PARTIAL. Run detached.

COMPOUNDS = [
    ("RUXOLITINIB-REF", "C1CCC(C1)C(CC#N)N2C=C(C=N2)C3=C4C=CNC4=NC=N3",
     "PubChem CID 25126798 (reference drug)",
     "JAK2 Kd 0.8 nM, IC50 3.2 nM (Miao 2024 Table 1)"),
    ("FEDRATINIB", "CC1=CN=C(N=C1NC2=CC(=CC=C2)S(=O)(=O)NC(C)(C)C)NC3=CC=C(C=C3)OCCN4CCCC4",
     "PubChem CID 16722836",
     "JAK2 Kd 4.3 nM, IC50 10 nM (Miao 2024 Table 1)"),
    ("MOMELOTINIB", "C1COCCN1C2=CC=C(C=C2)NC3=NC=CC(=N3)C4=CC=C(C=C4)C(=O)NCC#N",
     "PubChem CID 25062766 (co-crystallised ligand of 8BXH; re-dock control)",
     "JAK2 Kd 6.7 nM, IC50 11 nM (Miao 2024 Table 1)"),
    ("PACRITINIB", "C1CCN(C1)CCOC2=C3COCC=CCOCC4=CC(=CC=C4)C5=NC(=NC=C5)NC(=C3)C=C2",
     "PubChem CID 46216796",
     "JAK2 Kd 6.6 nM, IC50 14 nM (Miao 2024 Table 1)"),
    ("TOFACITINIB", "CC1CCN(CC1N(C)C2=NC=NC3=C2C=CN3)C(=O)CC#N",
     "PubChem CID 9926791 (JAK1/JAK3-leaning comparator)",
     "no head-to-head JAK2 value from Miao 2024 Table 1"),
    ("BARICITINIB", "CCS(=O)(=O)N1CC(C1)(CC#N)N2C=C(C=N2)C3=C4C=CNC4=NC=N3",
     "PubChem CID 44205240 (JAK1/JAK2 comparator)",
     "no head-to-head JAK2 value from Miao 2024 Table 1"),
]


def het_groups(path):
    from collections import defaultdict
    groups = defaultdict(list)
    with open(path) as f:
        for line in f:
            if line.startswith("HETATM"):
                res = (line[17:20].strip(), line[21].strip(), line[22:26].strip())
                groups[res].append((float(line[30:38]), float(line[38:46]), float(line[46:54])))
    out = []
    for res, xs in groups.items():
        n = len(xs)
        c = [sum(x[i] for x in xs) / n for i in range(3)]
        out.append((res, n, c))
    return out


def dist(a, b):
    return round(math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(3))), 2)


def load_partial():
    import os
    if os.path.exists(PARTIAL):
        try:
            with open(PARTIAL) as f:
                return json.load(f)
        except Exception as e:
            print(f"PARTIAL unreadable ({e}); starting fresh", flush=True)
    return {}


def save_partial(done):
    import os
    tmp = PARTIAL + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(done, f, indent=1)
    os.replace(tmp, PARTIAL)


def main():
    global CENTER
    p = D._pdb_path(PDB)
    CENTER = D._ligand_center(p)
    groups = het_groups(p)
    print("HETATM groups (res, n_atoms, centroid):", flush=True)
    for res, n, c in sorted(groups, key=lambda x: -x[1]):
        print(f"  {res} n={n} centroid={[round(v, 2) for v in c]}", flush=True)
    biggest = max(groups, key=lambda x: x[1])
    print(f"_ligand_center: {CENTER}; largest-group centroid: {biggest[2]}; "
          f"distance {dist(CENTER, biggest[2])} A", flush=True)

    done = load_partial()
    results = []
    for label, smi, src, pot in COMPOUNDS:
        if label in done:
            print(f"RESUME {label}: {done[label].get('affinity_kcal_mol')} (from partial)", flush=True)
            results.append(done[label])
            continue
        m = Chem.MolFromSmiles(smi)
        if m is None:
            print(f"SKIP {label}: unparseable SMILES", flush=True)
            continue
        desc = {
            "mw": round(Descriptors.MolWt(m), 2),
            "logp": round(Descriptors.MolLogP(m), 2),
            "hbd": rdMolDescriptors.CalcNumHBD(m),
            "hba": rdMolDescriptors.CalcNumHBA(m),
            "tpsa": round(rdMolDescriptors.CalcTPSA(m), 2),
            "rotatable": rdMolDescriptors.CalcNumRotatableBonds(m),
        }
        pa = C.pains(smi)
        r = D.dock(smi, PDB, CENTER, box_size=22.5)
        r["label"] = label
        r["source"] = src
        r["measured_potency"] = pot
        r["descriptors"] = desc
        r["pains"] = pa
        print(f"DOCK {label}: {r.get('affinity_kcal_mol')} ok={r.get('ok')} pains={pa}", flush=True)
        done[label] = r
        save_partial(done)
        results.append(r)
    results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))

    out = {
        "topic": {"target": "Janus kinase 2 (JAK2)", "reference": "ruxolitinib",
                  "topic_id": "HP-049", "date": "2026-11-13"},
        "target": {"uniprot": {"accession": "O60674", "gene": "JAK2",
                               "protein": "Tyrosine-protein kinase JAK2",
                               "organism": "Homo sapiens"},
                   "chembl_target": "not retrieved: ChEMBL API HTTP 500, 2026-11-13 (target ID not asserted)",
                   "chembl_status": "ChEMBL API HTTP 500 on all endpoints 2026-11-13; "
                                    "fallback = PubChem-verified compounds + Miao 2024 Table 1 potencies"},
        "docking": {"ok": True, "pdb_id": PDB, "resolution": 1.3,
                    "center": CENTER,
                    "center_note": "co-crystallised momelotinib centroid via dock._ligand_center; "
                                   f"distance to largest HETATM group centroid {dist(CENTER, biggest[2])} A (ATP site)",
                    "box_size": 22.5, "exhaustiveness": 8,
                    "results": results},
        "pipeline_note": "Pipeline run dock-HP-049-2026-11-13-PIPELINE-QUERY-ONLY.json docked "
                         "ruxolitinib alone (-8.71) on the same structure/centre; re-docked here "
                         "under the same protocol with comparators.",
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    import os
    try:
        os.remove(PARTIAL)
    except OSError:
        pass
    print("SAVED:", OUT, flush=True)


if __name__ == "__main__":
    main()
