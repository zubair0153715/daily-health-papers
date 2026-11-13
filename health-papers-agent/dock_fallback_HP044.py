"""Fallback docking for HP-044 (Factor Xa / rivaroxaban), 2026-11-13.

Why this exists: ChEMBL API is DOWN across all endpoints on 2026-11-13
(HTTP 500). The standard pipeline retrieved 0 ligands, and its
auto-picked structure 9I24 is WRONG for this question: 9I24 is Factor
Xa in complex with an a2-loop peptide and a covalent chloromethyl
ketone inhibitor (EGRCK, 0GJ) in the active site (Ustok 2026, Blood
147:573-583) -- the pipeline's rivaroxaban dock (-5.7) was against a
covalently blocked active site. That number is DISCARDED here (kept in
dock-HP-044-2026-11-13-PIPELINE-QUERY-ONLY.json for audit).

Correction (documented fallback, AGENTS.md FLT3 precedent):
- Structure 2W26: human Factor Xa in complex with BAY 59-7939
  (rivaroxaban itself), J Med Chem 2005, PMID 16161994 -- the
  reference drug's own co-crystal. Centre = D._ligand_center,
  audited against the rivaroxaban centroid and Ser195 CA distance.
- Compounds: rivaroxaban + three other approved direct fXa
  inhibitors, SMILES verified live via PubChem PUG REST name lookup
  on 2026-11-13, plus PubChem fastsimilarity_2d analogues of
  rivaroxaban (threshold 85). Measured Ki values from the cited
  literature only; analogues carry NO measured potency.
"""
import json
import math
import sys
import urllib.request

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402
from app.discovery import chem as C  # noqa: E402
from app.discovery import sources as S  # noqa: E402
from rdkit import Chem  # noqa: E402
from rdkit.Chem import Descriptors, rdMolDescriptors  # noqa: E402

OUT = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-044-2026-11-13.json"
PARTIAL = OUT + ".partial"
PDB = "2W26"

# Incremental-save + resume (see dock_fallback_HP013.py): the HP-013 run was
# killed by the runtime (SIGTERM) at 14/16 docks with no JSON saved. This
# script saves after EVERY dock and resumes from PARTIAL. Run detached.

COMPOUNDS = [
    ("RIVAROXABAN-REF", "C1COCC(=O)N1C2=CC=C(C=C2)N3CC(OC3=O)CNC(=O)C4=CC=C(S4)Cl",
     "PubChem CID 9875401 (reference drug; co-crystallised ligand of 2W26)",
     "Ki 0.4 nM, IC50 0.7 nM, prothrombinase IC50 2.1 nM (Perzborn et al. 2005, J Thromb Haemost 3:514-521, PMID 15748242)"),
    ("APIXABAN", "COC1=CC=C(C=C1)N2C3=C(CCN(C3=O)C4=CC=C(C=C4)N5CCCCC5=O)C(=N2)C(=O)N",
     "PubChem CID 10182969",
     "Ki 0.08 nM human fXa (Pinto et al. 2007, J Med Chem 50:5339-5356, PMID 17914785)"),
    ("EDOXABAN", "CN1CCC2=C(C1)SC(=N2)C(=O)NC3CC(CCC3NC(=O)C(=O)NC4=NC=C(C=C4)Cl)C(=O)N(C)C",
     "PubChem CID 10280735",
     "Ki 0.56 nM free fXa (Furugohri et al. 2008, J Thromb Haemost 6:1542-1549)"),
    ("BETRIXABAN", "CN(C)C(=N)C1=CC=C(C=C1)C(=O)NC2=C(C=C(C=C2)OC)C(=O)NC3=NC=C(C=C3)Cl",
     "PubChem CID 10275777",
     "no head-to-head Ki attached in this run"),
]

RIVAROXABAN_SMILES = COMPOUNDS[0][1]


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


def ser195_ca(path):
    with open(path) as f:
        for line in f:
            if line.startswith("ATOM") and line[22:26].strip() == "195" and line[12:16].strip() == "CA":
                return [float(line[30:38]), float(line[38:46]), float(line[46:54])]
    return None


def dist(a, b):
    return round(math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(3))), 2)


def fetch_analogues(smiles, threshold=85, max_records=30, want=4):
    r = S.pubchem_similar(smiles, threshold=threshold, max_records=max_records)
    data = r.get("data") or []
    cids = data.get("cids") if isinstance(data, dict) else data
    out = []
    seen = {Chem.MolToSmiles(Chem.MolFromSmiles(smiles))}
    for cid in cids:
        if len(out) >= want:
            break
        try:
            url = (f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/"
                   "property/CanonicalSMILES/JSON")
            req = urllib.request.Request(url, headers={"User-Agent": "LeadForge-research/1.0"})
            with urllib.request.urlopen(req, timeout=25) as resp:
                d = json.loads(resp.read().decode("utf-8"))
            smi = (d["PropertyTable"]["Properties"][0].get("CanonicalSMILES")
                   or d["PropertyTable"]["Properties"][0].get("ConnectivitySMILES")
                   or d["PropertyTable"]["Properties"][0].get("IsomericSMILES"))
            if not smi:
                print(f"ANALOGUE {cid}: no SMILES property in response", flush=True)
                continue
        except Exception as e:
            print(f"ANALOGUE {cid}: SMILES fetch failed: {e}", flush=True)
            continue
        if "." in smi:
            continue
        m = Chem.MolFromSmiles(smi)
        if m is None:
            continue
        c = Chem.MolToSmiles(m)
        if c in seen:
            continue
        seen.add(c)
        out.append((cid, smi))
        print(f"ANALOGUE CID {cid}: {smi[:80]}", flush=True)
    return out


def dock_one(label, smi, src, pot):
    m = Chem.MolFromSmiles(smi)
    if m is None:
        print(f"SKIP {label}: unparseable SMILES", flush=True)
        return None
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
    return r


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
    s195 = ser195_ca(p)
    print(f"_ligand_center: {CENTER}; Ser195 CA: {s195}; distance {dist(CENTER, s195) if s195 else 'n/a'} A", flush=True)

    todo = list(COMPOUNDS)
    for cid, smi in fetch_analogues(RIVAROXABAN_SMILES):
        todo.append((f"PUBCHEM-{cid}", smi,
                     f"PubChem CID {cid}, fastsimilarity_2d analogue of rivaroxaban (threshold 85)",
                     "no measured potency (PubChem similarity analogue)"))

    done = load_partial()
    results = []
    for label, smi, src, pot in todo:
        if label in done:
            print(f"RESUME {label}: {done[label].get('affinity_kcal_mol')} (from partial)", flush=True)
            results.append(done[label])
            continue
        r = dock_one(label, smi, src, pot)
        if r is not None:
            done[label] = r
            save_partial(done)
            results.append(r)
    results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))

    out = {
        "topic": {"target": "Coagulation factor Xa", "reference": "rivaroxaban",
                  "topic_id": "HP-044", "date": "2026-11-13"},
        "target": {"uniprot": {"accession": "P00742", "gene": "F10",
                               "protein": "Coagulation factor X",
                               "organism": "Homo sapiens"},
                   "chembl_target": "not retrieved: ChEMBL API HTTP 500, 2026-11-13 (target ID not asserted)",
                   "chembl_status": "ChEMBL API HTTP 500 on all endpoints 2026-11-13; "
                                    "fallback = PubChem-verified compounds + literature Ki values"},
        "docking": {"ok": True, "pdb_id": PDB,
                    "center": CENTER,
                    "center_note": "co-crystallised rivaroxaban (BAY 59-7939) centroid via "
                                   f"dock._ligand_center; Ser195 CA distance {dist(CENTER, s195) if s195 else 'n/a'} A (active site)",
                    "box_size": 22.5, "exhaustiveness": 8,
                    "results": results},
        "discarded": "Pipeline run dock-HP-044-2026-11-13-PIPELINE-QUERY-ONLY.json: "
                     "rivaroxaban -5.7 on 9I24 (covalently blocked active site) -- wrong structure, discarded.",
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
