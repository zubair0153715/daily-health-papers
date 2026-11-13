"""Fallback docking for HP-027 (EGFR L858R/T790M/C797S / osimertinib), 2026-11-13.

Why this exists: ChEMBL API is DOWN across all endpoints on 2026-11-13
(HTTP 500, verified multiple ways). The standard pipeline retrieved 0
ligands and its auto-picked structure 8A27 is WRONG for this question:
8A27 is the EGFR kinase domain bound to an ALLOSTERIC inhibitor
(Obst-Sander 2022), so the pipeline's osimertinib dock (-8.56) was at
the allosteric site, not the ATP site. That number is DISCARDED here
(kept in dock-HP-027-2026-11-13-PIPELINE-QUERY-ONLY.json for audit).

Correction (documented fallback, AGENTS.md FLT3 precedent):
- Structure 6LUB: EGFR L858R/T790M/C797S triple mutant in complex with
  CH7233163, 2.315 A X-ray (Kashima 2020, Mol Cancer Ther) -- the exact
  triple mutant the topic poses, ATP-site inhibitor bound. Centre =
  D._ligand_center, audited against the co-crystallised CH7233163
  centroid and against Ser797 CA distance.
- Compounds: reference osimertinib + known EGFR inhibitors, SMILES
  verified live via PubChem PUG REST name lookup on 2026-11-13, plus
  PubChem fastsimilarity_2d analogues of osimertinib (threshold 85).
  Measured potencies come from the cited literature only; analogues
  carry NO measured potency.
- Covalent caveat: osimertinib and afatinib bind covalently to Cys797;
  the C797S mutant removes the covalent anchor, so Vina's
  non-covalent pose score cannot capture their mechanism -- the scores
  are triage controls, and the resistance conclusion rests on the
  literature IC50s, not on the docking.
"""
import json
import math
import sys
import urllib.parse
import urllib.request

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402
from app.discovery import chem as C  # noqa: E402
from app.discovery import sources as S  # noqa: E402
from rdkit import Chem  # noqa: E402
from rdkit.Chem import Descriptors, rdMolDescriptors  # noqa: E402

OUT = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-027-2026-11-13.json"
PARTIAL = OUT + ".partial"
PDB = "6LUB"

# Incremental-save + resume (see dock_fallback_HP013.py): the HP-013 run was
# killed by the runtime (SIGTERM) at 14/16 docks with no JSON saved. This
# script saves after EVERY dock and resumes from PARTIAL. Run detached.

COMPOUNDS = [
    ("OSIMERTINIB-REF", "CN1C=C(C2=CC=CC=C21)C3=NC(=NC=C3)NC4=C(C=C(C(=C4)NC(=O)C=C)N(C)CCN(C)C)OC",
     "PubChem CID 71496458 (reference drug)",
     "BaF3 antiproliferative IC50 1.42 uM (Del19/T790M/C797S) / 1.44 uM (L858R/T790M/C797S) (Eur J Med Chem 2023, PMID 37839342)"),
    ("CH7233163", "CC(C)N1C2=CC(=NC=C2C3=C1C=C(C=C3OCC(F)(F)F)N4CCN(CC4)C)NC5=NC(=NC=C5)C6=CN(N=C6)S(=O)(=O)C7CC7",
     "PubChem CID 154701097 (co-crystallised ligand of 6LUB; re-dock control)",
     "Del19/T790M/C797S biochemical IC50 0.28 nM; cellular IC50 20 nM vs Del19/T790M/C797S NIH3T3, 1200 nM vs WT A431 (Kashima 2020)"),
    ("GEFITINIB", "COC1=C(C=C2C(=C1)N=CN=C2NC3=CC(=C(C=C3)F)Cl)OCCCN4CCOCC4",
     "PubChem CID 123631 (first-generation, reversible)",
     "HTRF IC50 185 ± 98 nM vs L858R/T790M double mutant (Chem Sci 2019, DOI 10.1039/C9SC03445E); no triple-mutant IC50 attached"),
    ("AFATINIB", "CN(C)CC=CC(=O)NC1=C(C=C2C(=C1)C(=NC=N2)NC3=CC(=C(C=C3)F)Cl)OC4CCOC4",
     "PubChem CID 10184653 (second-generation, covalent Cys797)",
     "Covalent anchor lost on C797S; no triple-mutant IC50 attached"),
    ("BRIGATINIB", "CN1CCN(CC1)C2CCN(CC2)C3=CC(=C(C=C3)NC4=NC=C(C(=N4)NC5=CC=CC=C5P(=O)(C)C)Cl)OC",
     "PubChem CID 68165256 (bound to T790M/C797S in 8H7X)",
     "bound to T790M/C797S in 8H7X (Suzuki et al. 2024, NPJ Precis Oncol); no head-to-head triple-mutant IC50 attached"),
]

OSIMERTINIB_SMILES = COMPOUNDS[0][1]


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


def ser797_ca(path):
    with open(path) as f:
        for line in f:
            if line.startswith("ATOM") and line[22:26].strip() == "797" and line[12:16].strip() == "CA":
                return [float(line[30:38]), float(line[38:46]), float(line[46:54])]
    return None


def dist(a, b):
    return round(math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(3))), 2)


def fetch_analogues(smiles, threshold=85, max_records=30, want=5):
    """PubChem fastsimilarity_2d analogues; returns [(cid, smiles)] for the
    first `want` single-component, non-duplicate CIDs (SMILES fetched by CID)."""
    r = S.pubchem_similar(smiles, threshold=threshold, max_records=max_records)
    data = r.get("data") or []
    cids = data.get("cids") if isinstance(data, dict) else data
    out = []
    seen = set()
    ref_canon = Chem.MolToSmiles(Chem.MolFromSmiles(smiles))
    seen.add(ref_canon)
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
        print(f"  {res} n={n} centroid={c}", flush=True)
    s797 = ser797_ca(p)
    print(f"_ligand_center: {CENTER}; Ser797 CA: {s797}; distance {dist(CENTER, s797) if s797 else 'n/a'} A", flush=True)

    todo = list(COMPOUNDS)
    for cid, smi in fetch_analogues(OSIMERTINIB_SMILES):
        todo.append((f"PUBCHEM-{cid}", smi,
                     f"PubChem CID {cid}, fastsimilarity_2d analogue of osimertinib (threshold 85)",
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
        "topic": {"target": "Epidermal growth factor receptor (EGFR), L858R/T790M/C797S triple mutant",
                  "reference": "osimertinib", "topic_id": "HP-027", "date": "2026-11-13"},
        "target": {"uniprot": {"accession": "P00533", "gene": "EGFR",
                               "protein": "Epidermal growth factor receptor",
                               "organism": "Homo sapiens"},
                   "chembl_target": "CHEMBL203 (not retrieved: ChEMBL API HTTP 500, 2026-11-13)",
                   "chembl_status": "ChEMBL API HTTP 500 on all endpoints 2026-11-13; "
                                    "fallback = PubChem-verified compounds + literature potencies"},
        "docking": {"ok": True, "pdb_id": PDB, "resolution": 2.315,
                    "center": CENTER,
                    "center_note": "co-crystallised CH7233163 centroid via dock._ligand_center; "
                                   f"Ser797 CA distance {dist(CENTER, s797) if s797 else 'n/a'} A (ATP site)",
                    "box_size": 22.5, "exhaustiveness": 8,
                    "results": results},
        "discarded": "Pipeline run dock-HP-027-2026-11-13-PIPELINE-QUERY-ONLY.json: "
                     "osimertinib -8.56 on 8A27 (allosteric-site structure) -- wrong site, discarded.",
        "caveat": "Osimertinib/afatinib are covalent Cys797 binders; C797S removes the "
                  "covalent anchor, so Vina non-covalent scores cannot capture their mechanism.",
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
