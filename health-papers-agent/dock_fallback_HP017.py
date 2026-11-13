"""Fallback docking for HP-017 (H. pylori urease / clarithromycin), 2026-11-13.

Why this exists: ChEMBL API is DOWN across all endpoints on 2026-11-13
(HTTP 500). The standard pipeline retrieved 0 ligands, found no PDB,
and -- worse -- resolved the WRONG target: UniProt Q09068 is UreI, the
acid-activated urea CHANNEL, not urease. That run is DISCARDED
(dock-HP-017-2026-11-13-PIPELINE-QUERY-ONLY.json for audit).

Correction (documented fallback, AGENTS.md FLT3 precedent):
- Target: H. pylori urease, UniProt P14916 (UreA, alpha subunit,
  strain 26695; verified live on rest.uniprot.org 2026-11-13).
  The holoenzyme is (UreA-UreB)3; the active site with two Ni2+ ions
  sits in UreB.
- Structure 1E9Z: H. pylori urease, 3.00 A X-ray (Ha et al. 2001,
  Nat Struct Biol 8:480, PMID 11373617). The deposited asymmetric
  unit is one catalytic unit (chains A/B) with exactly two Ni ions
  in chain B. Centre = the Ni-pair centroid, computed from the file
  below -- there is no drug-like co-crystallised ligand to centre on.
- Compounds: literature urease inhibitors + clarithromycin as the
  regimen (non-urease-inhibitor) control, SMILES verified live via
  PubChem PUG REST name lookup on 2026-11-13, plus PubChem
  fastsimilarity_2d analogues of acetohydroxamic acid (threshold 85).
  Measured potencies from the cited literature only; analogues carry
  NO measured potency.
- Metal caveat: Vina cannot model Ni2+ coordination, and the receptor
  prep drops HETATM ions, so the Ni ions are ABSENT from the docking.
  Scores are pose-only triage against the apo active-site cavity, not
  metal-binding predictions. The paper states this plainly.
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

OUT = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-017-2026-11-13.json"
PARTIAL = OUT + ".partial"
PDB = "1E9Z"

# Incremental-save + resume (see dock_fallback_HP013.py): the HP-013 run was
# killed by the runtime (SIGTERM) at 14/16 docks with no JSON saved. This
# script saves after EVERY dock and resumes from PARTIAL. Run detached.

COMPOUNDS = [
    ("ACETOHYDROXAMIC-ACID", "CC(=O)NO",
     "PubChem CID 1990 (sole FDA-approved urease inhibitor; Lithostat)",
     "H. pylori urease IC50 ~2.5 mM (secondary technical guide); jack-bean IC50 42 uM (Modi 2023, Molecules 28:2697)"),
    ("FLUROFAMIDE", "C1=CC(=CC=C1C(=O)NP(=O)(N)N)F",
     "PubChem CID 51173",
     "~1000x more potent than AHA in intact P. mirabilis cells; min. urease inhibitory conc. <=2 uM vs Ureaplasma (secondary source)"),
    ("THIOUREA", "C(=S)(N)N",
     "PubChem CID 2723790 (classic weak urease inhibitor)",
     "no head-to-head IC50 attached in this run"),
    ("HYDROXYUREA", "C(=O)(N)NO",
     "PubChem CID 3657",
     "jack-bean urease IC50 100 uM (Modi 2023, Molecules 28:2697)"),
    ("CLARITHROMYCIN-REGIMEN", "CCC1C(C(C(C(=O)C(CC(C(C(C(C(C(=O)O1)C)OC2CC(C(C(O2)C)O)(C)OC)C)OC3C(C(CC(O3)C)N(C)C)O)(C)OC)C)C)O)(C)O",
     "PubChem CID 84029 (pipeline-verified 2026-11-13; regimen drug, NOT a urease inhibitor)",
     "not a urease inhibitor -- regimen control; no urease IC50 exists"),
]

AHA_SMILES = COMPOUNDS[0][1]


def ni_pair_centroid(path):
    ni = []
    with open(path) as f:
        for line in f:
            if line.startswith("HETATM") and line[17:20].strip() == "NI":
                ni.append((line[21], line[22:26].strip(),
                           float(line[30:38]), float(line[38:46]), float(line[46:54])))
    assert len(ni) == 2, f"expected 2 Ni ions, found {len(ni)}: {ni}"
    c = [sum(x[i + 2] for x in ni) / 2 for i in range(3)]
    return ni, [round(v, 2) for v in c]


def dist(a, b):
    return round(math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(3))), 2)


def fetch_analogues(smiles, threshold=85, max_records=30, want=3):
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
    ni, CENTER = ni_pair_centroid(p)
    print(f"Ni ions: {ni}; Ni-pair centroid (centre): {CENTER}", flush=True)

    todo = list(COMPOUNDS)
    for cid, smi in fetch_analogues(AHA_SMILES):
        todo.append((f"PUBCHEM-{cid}", smi,
                     f"PubChem CID {cid}, fastsimilarity_2d analogue of acetohydroxamic acid (threshold 85)",
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
        "topic": {"target": "Helicobacter pylori urease (UreA/UreB)",
                  "reference": "clarithromycin (regimen drug, not a urease inhibitor)",
                  "topic_id": "HP-017", "date": "2026-11-13"},
        "target": {"uniprot": {"accession": "P14916", "gene": "ureA",
                               "protein": "Urease subunit alpha",
                               "organism": "Helicobacter pylori (strain ATCC 700392 / 26695)"},
                   "chembl_target": "not retrieved: ChEMBL API HTTP 500, 2026-11-13 (target ID not asserted)",
                   "chembl_status": "ChEMBL API HTTP 500 on all endpoints 2026-11-13; "
                                    "fallback = PubChem-verified compounds + literature potencies"},
        "docking": {"ok": True, "pdb_id": PDB, "resolution": 3.0,
                    "center": CENTER,
                    "center_note": "Ni-pair centroid from the deposited 1E9Z coordinates "
                                   f"(Ni ions {ni}); no drug-like co-crystallised ligand exists in 1E9Z",
                    "box_size": 22.5, "exhaustiveness": 8,
                    "results": results},
        "discarded": "Pipeline run dock-HP-017-2026-11-13-PIPELINE-QUERY-ONLY.json resolved "
                     "the WRONG target (Q09068, UreI urea channel) and found no PDB -- discarded.",
        "caveat": "Vina cannot model Ni2+ coordination and the receptor prep drops HETATM "
                  "ions, so the two Ni ions are ABSENT from the docking. Scores are pose-only "
                  "triage against the apo active-site cavity, not metal-binding predictions.",
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
