"""Fallback docking for HP-013 (MRSA PBP2a / ceftaroline), 2026-11-13.

Why this exists: ChEMBL API is DOWN across all endpoints on 2026-11-13
(target search, target-by-accession and activity endpoints all HTTP 500,
verified by direct pipeline calls, browser fetch and browser task on
2026-11-13 15:24-15:28 PKT). The standard pipeline therefore retrieved
0 ligands. Documented fallback (AGENTS.md, FLT3 precedent 2026-11-02,
HP-030 fallback 2026-11-11): PubChem-verified compounds + known
inhibitors with literature/ChEMBL-recorded potencies. No measured
potency is attached to any compound without a stated source.

Ligand set:
- 4 ChEMBL MecA ligands from the 2026-10-29 LeadForge run
  (run_pbp2a_corrected_raw.json, ChEMBL target CHEMBL6187 "MecA
  (Staphylococcus aureus)", retrieved when ChEMBL was live): Kd/IC50
  and pChEMBL as recorded then. SMILES copied verbatim from that file.
- Ceftaroline fosamil (PubChem CID 9852981, pipeline-verified today)
  and active ceftaroline (PubChem CID 74316801, SMILES per the
  2026-10-29 precedent, verified by PubChem SMILES lookup then).
- Ceftobiprole (CID 135413542) and L-695,256 (CID 9890833), SMILES
  verified live via PubChem PUG REST name lookup on 2026-11-13.

Structures (verified precedent, 2026-10-29):
- 1MWS: nitrocefin acyl-PBP2a, S. aureus strain 27r, 2.00 A X-ray.
  Centre = D._ligand_center (nitrocefin NC1 active-site centroid),
  audited below against the NC1 centroid computed from the file.
- 3ZG0 chain B: ceftaroline acyl-PBP2a co-crystal, 2.60 A X-ray.
  Chain A fails RDKit sanitization (1.81 A Gly402 O...Ser403 N contact
  misread as a bond), so the chain-B-only PDB is written to the cache
  and _prep_receptor is run on it into the standard 3ZG0_rec.pdbqt
  slot, which D.dock then reuses (its own cache check). Centre =
  chain-B AI8 (ceftaroline, bound form) centroid, audited below.

Caveat (carried into the paper): Vina scores here are NON-COVALENT
pose scores in acyl-enzyme structures -- they do NOT model the covalent
acylation step that is ceftaroline's actual mechanism, so they are
triage controls only. The allosteric trigger site (Otero 2014) is
discussed, not docked: the allosteric ceftaroline copy in 3ZG0 is a
non-covalent trigger ligand, and a second-molecule allosteric model is
beyond Vina's single-ligand protocol.
"""
import json
import math
import os
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402
from app.discovery import chem as C  # noqa: E402
from rdkit import Chem  # noqa: E402
from rdkit.Chem import Descriptors, rdMolDescriptors  # noqa: E402

CACHE = "/home/hatch/workspace/clinic-demo/app/discovery/data/pdb_cache"
OUT = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-013-2026-11-13.json"
PARTIAL = OUT + ".partial"

# Incremental-save + resume: the first run of this script was killed by the
# runtime (SIGTERM) at 14/16 docks with NO json saved, because dock() deletes
# its Vina outputs and results were only written at the end. This version
# saves after EVERY dock and resumes from PARTIAL, so a kill loses at most
# the dock in flight. Run detached (nohup/setsid) so a session kill cannot
# take the docking down again.

COMPOUNDS = [
    ("CEFTAROLINE-FOSAMIL", "CCON=C(C1=NSC(=N1)NP(=O)(O)O)C(=O)NC2C3N(C2=O)C(=C(CS3)SC4=NC(=CS4)C5=CC=[N+](C=C5)C)C(=O)[O-]",
     "PubChem CID 9852981 (pipeline-verified 2026-11-13; administered prodrug)",
     "MRSA MIC90 1 mg/L (Sader et al. 2025, AAC 69:e01402-24, Table 2)"),
    ("CEFTAROLINE-ACTIVE", "CCON=C(C1=NSC(=N1)N)C(=O)NC2C3N(C2=O)C(=C(CS3)SC4=NC(=CS4)C5=CC=[N+](C=C5)C)C(=O)[O-]",
     "PubChem CID 74316801 (active, dephosphorylated species)",
     "MRSA MIC90 1 mg/L (Sader et al. 2025, AAC 69:e01402-24, Table 2)"),
    ("CHEMBL4847813", "Cc1ccc(NC(=O)[C@H](Cc2c[nH]c3ccccc23)NC(=O)C2CCN(C(=O)CNC(=O)OC(C)(C)C)CC2)cc1",
     "ChEMBL CHEMBL6187 (MecA), retrieved 2026-10-29",
     "Kd 129 nM, pChEMBL 6.89"),
    ("CHEMBL4879273", "COc1cc2c(c(OC)c1OC)-c1ccc(NCC(=O)NCCc3c[nH]c4ccccc34)c(=O)cc1[C@@H](NC(C)=O)CC2",
     "ChEMBL CHEMBL6187 (MecA), retrieved 2026-10-29",
     "Kd 168 nM, pChEMBL 6.78"),
    ("CHEMBL4862632", "COc1ccc(-c2cc(=O)oc3c(C)c(OCC(=O)N[C@@H](Cc4c[nH]c5ccc(O)cc45)C(=O)O)ccc23)cc1",
     "ChEMBL CHEMBL6187 (MecA), retrieved 2026-10-29",
     "Kd 264 nM, pChEMBL 6.58"),
    ("CHEMBL520642", "Nc1nc(/C(=N/O)C(=O)N[C@@H]2C(=O)N3C(C(=O)O)=C(/C=C4\\CCN([C@@H]5CCNC5)C4=O)CS[C@H]23)ns1",
     "ChEMBL CHEMBL6187 (MecA), retrieved 2026-10-29",
     "IC50 1900 nM, pChEMBL 5.72"),
    ("CEFTOBIPROLE", "C1CNCC1N2CCC(=CC3=C(N4C(C(C4=O)NC(=O)C(=NO)C5=NSC(=N5)N)SC3)C(=O)O)C2=O",
     "PubChem CID 135413542 (verified 2026-11-13)",
     "MRSA MIC50/90 1/2 mg/L (Sader et al. 2025, AAC 69:e01402-24)"),
    ("L-695256", "CC(C1C2CC(=C(N2C1=O)C(=O)[O-])C3=CC4=C(C=C3)C(=O)C5=C4C=CC(=C5)CN6C=C[N+](=C6)C)O",
     "PubChem CID 9890833 (verified 2026-11-13)",
     "PBP2a-binding carbapenem analogue; no head-to-head MIC attached"),
]


def centroid(path, resname, chain=None):
    xs = []
    with open(path) as f:
        for line in f:
            if not line.startswith("HETATM"):
                continue
            if line[17:20].strip() != resname:
                continue
            if chain is not None and line[21] != chain:
                continue
            xs.append((float(line[30:38]), float(line[38:46]), float(line[46:54])))
    n = len(xs)
    if n == 0:
        return None, 0
    return [sum(c[i] for c in xs) / n for i in range(3)], n


def dist(a, b):
    return round(math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(3))), 2)


def load_partial():
    if os.path.exists(PARTIAL):
        try:
            with open(PARTIAL) as f:
                return json.load(f)
        except Exception as e:
            print(f"PARTIAL unreadable ({e}); starting fresh", flush=True)
    return {}


def save_partial(state):
    tmp = PARTIAL + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=1)
    os.replace(tmp, PARTIAL)


def dock_set(pdb_id, center, center_note, state, key):
    done = state.setdefault(key, {})
    results = []
    for label, smi, src, pot in COMPOUNDS:
        if label in done:
            print(f"RESUME {pdb_id} {label}: {done[label].get('affinity_kcal_mol')} (from partial)", flush=True)
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
        r = D.dock(smi, pdb_id, center, box_size=22.5)
        r["label"] = label
        r["source"] = src
        r["measured_potency"] = pot
        r["descriptors"] = desc
        r["pains"] = pa
        print(f"DOCK {pdb_id} {label}: {r.get('affinity_kcal_mol')} ok={r.get('ok')} pains={pa}", flush=True)
        done[label] = r
        save_partial(state)
        results.append(r)
    results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
    return {"pdb_id": pdb_id, "center": center, "center_note": center_note,
            "box_size": 22.5, "exhaustiveness": 8, "results": results}


def main():
    state = load_partial()
    # --- 1MWS chain A only ---
    # The full 1MWS file (two chains) makes Vina crawl (~7 min CPU per
    # ligand on this VM). The 2026-10-29 precedent used the chain-A-only
    # receptor (cached 1MWS_chainA.pdb / 1MWS_chainA_rec.pdbqt); the
    # centre is identical to the full-file _ligand_center.
    p1full = D._pdb_path("1MWS")
    c1full = D._ligand_center(p1full)
    nc1, n1 = centroid(p1full, "NC1")
    nc1a, n1a = centroid(p1full, "NC1", chain="A")
    # Chain-A file carries ATOM records only (no HETATM), so its centre is
    # taken from the verified 2026-10-29 precedent run, which used this
    # exact value for 1MWS_chainA; audit it against the full-file centre
    # and against the chain-A NC1 centroid (the two-chain NC1 average is
    # an 8.15 A artifact: chain-B NC1 is 6 atoms, 63.87 A away).
    c1 = [28.54851219512195, 29.220829268292686, 87.48758536585366]
    print(f"1MWS full-file _ligand_center: {c1full}; NC1 centroid all chains ({n1} atoms): {nc1}; "
          f"chain-A NC1 centroid ({n1a} atoms): {nc1a}; precedent chain-A centre {c1}; "
          f"distance to full-file centre {dist(c1, c1full)} A, to chain-A NC1 centroid {dist(c1, nc1a)} A, "
          f"to all-chain NC1 centroid {dist(c1, nc1)} A", flush=True)
    s1 = dock_set("1MWS_chainA", c1,
                  f"nitrocefin NC1 active-site centroid via dock._ligand_center; distance to chain-A NC1 centroid {dist(c1, nc1a)} A; chain A only (full 1MWS is two chains and Vina-crawls on this VM)",
                  state, "1MWS_chainA")

    # --- 3ZG0 chain B ---
    p3 = D._pdb_path("3ZG0")
    filt = os.path.join(CACHE, "3ZG0_chainB.pdb")
    with open(p3) as f, open(filt, "w") as g:
        for line in f:
            if line.startswith("ATOM") and line[21] == "B":
                g.write(line)
            elif line.startswith("END"):
                break
        g.write("END\n")
    rec = os.path.join(CACHE, "3ZG0_rec.pdbqt")
    if os.path.exists(rec):
        os.remove(rec)
    D._prep_receptor(filt, rec)
    print("3ZG0 chainB receptor prepped:", rec, os.path.getsize(rec), flush=True)
    c3, n3 = centroid(p3, "AI8", chain="B")
    print(f"3ZG0 chain-B AI8 centroid ({n3} atoms): {c3}", flush=True)
    s3 = dock_set("3ZG0", c3, f"chain-B AI8 (ceftaroline, bound form) centroid ({n3} atoms); chain A excluded (RDKit sanitization failure, 1.81 A Gly402 O...Ser403 N)",
                  state, "3ZG0_chainB")

    out = {
        "topic": {"target": "Penicillin-binding protein 2a (PBP2a), MRSA",
                  "reference": "ceftaroline", "topic_id": "HP-013", "date": "2026-11-13"},
        "target": {"uniprot": {"accession": "Q53707", "gene": "mecA",
                               "protein": "MecA PBP2' (penicillin binding protein 2')",
                               "organism": "Staphylococcus aureus"},
                   "chembl_target": "CHEMBL6187 (MecA, Staphylococcus aureus)",
                   "chembl_status": "ChEMBL API HTTP 500 on all endpoints 2026-11-13; "
                                    "ligand potencies from the 2026-10-29 ChEMBL retrieval "
                                    "(run_pbp2a_corrected_raw.json); docking re-run today"},
        "structures": {"1MWS_chainA": s1, "3ZG0_chainB": s3},
        "caveat": "Vina scores are NON-COVALENT pose scores in acyl-enzyme structures; "
                  "they do not model the covalent acylation step of beta-lactam action.",
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    try:
        os.remove(PARTIAL)
    except OSError:
        pass
    print("SAVED:", OUT, flush=True)


if __name__ == "__main__":
    main()
