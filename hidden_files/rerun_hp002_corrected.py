"""Corrected re-run for Paper #45 (HP-002).

WHY: the standard run_docking.py run resolved the ChEMBL target wrong:
UniProt P37231 (PPARG) -> chembl_target CHEMBL2074 "Maltase-glucoamylase",
so its 55 bioactivities / 26 leads are MGAM (alpha-glucosidase) actives,
not PPAR-gamma actives (the docked leads are iminosugar polyols). The
docking itself was on the CORRECT protein (PDB 9F7W, human PPAR-gamma LBD,
centre audited 0.01 A from the co-crystallised BPA ligand), but the lead
set was mislabelled. This script re-runs ONLY the ligand-retrieval and
ranking steps with the ChEMBL target pinned to the verified PPAR-gamma
target CHEMBL235, reusing the pipeline's own functions (sources / chem /
tox / dock) and the identical docking protocol, so the corrected numbers
are directly comparable. The original (wrong-target) JSON is kept as-is
for the audit trail.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import sources as S  # noqa: E402
from app.discovery import chem as C  # noqa: E402
from app.discovery import tox as T  # noqa: E402
from app.discovery import dock as D  # noqa: E402
from app.discovery.pipeline import lead_score  # noqa: E402

CHEMBL_TARGET = "CHEMBL235"  # verified: "Peroxisome proliferator-activated receptor gamma"
ACC = "P37231"
CENTER = [47.1, 6.91, 1.39]  # audited BPA-501 centroid on 9F7W

bio = S.chembl_bioactivities(CHEMBL_TARGET, limit=60)
print("BIOACTIVITIES ok:", bio.get("ok"), "count:", len(bio.get("data") or []))
ligands = bio.get("data") or []
assert ligands, "no bioactivities for CHEMBL235 - abort, do not fake"

pc = S.pubchem_by_name("pioglitazone")
print("PUBCHEM ok:", pc.get("ok"), "cid:", (pc.get("data") or {}).get("cid"))
query = pc["data"]
q_smi = query["smiles"]

refs = [l["smiles"] for l in ligands if l.get("smiles")]
sims = C.similarity_to(q_smi, refs)
lig_by_smi = {l["smiles"]: l for l in ligands}
ranked = []
for rs, score in sims[:25]:
    lig = lig_by_smi.get(rs, {})
    ranked.append({
        "smiles": rs, "similarity": score,
        "chembl_id": lig.get("molecule_chembl_id"),
        "pchembl": lig.get("pchembl"),
        "activity": f"{lig.get('activity_type')} {lig.get('value')} {lig.get('units') or ''}".strip()})

leads = []
desc = C.descriptors(q_smi)
pa = C.pains(q_smi)
tx = T.predict(q_smi)
tox_probs = tx["assays"] if tx.get("ok") else None
score, detail = lead_score(1.0, desc, pa or [], tox_probs)
leads.append({"rank": 1, "label": "QUERY", "smiles": q_smi,
              "similarity": 1.0, "score": score, "score_detail": detail,
              "descriptors": desc, "pains": pa,
              "tox": {"mode": tx.get("mode"), "max_similarity": tx.get("max_similarity"),
                      "assays": tox_probs},
              "pubchem": {"cid": query.get("cid"), "url": query.get("url")},
              "known_activity": None})
for i, r in enumerate(ranked):
    desc = C.descriptors(r["smiles"])
    pa = C.pains(r["smiles"])
    tx = T.predict(r["smiles"])
    tox_probs = tx["assays"] if tx.get("ok") else None
    score, detail = lead_score(r["similarity"], desc, pa or [], tox_probs)
    leads.append({"rank": i + 2, "label": r["chembl_id"] or f"hit-{i+1}",
                  "smiles": r["smiles"], "similarity": r["similarity"],
                  "score": score, "score_detail": detail,
                  "descriptors": desc, "pains": pa,
                  "tox": {"mode": tx.get("mode"), "assays": tox_probs},
                  "known_activity": {"pchembl": r["pchembl"], "activity": r["activity"]}})
leads.sort(key=lambda x: x["score"], reverse=True)
for i, l in enumerate(leads):
    l["rank"] = i + 1
print("LEADS:", len(leads))
for l in leads[:8]:
    print("  ", l["rank"], l["label"], "sim", round(l["similarity"], 3),
          "score", l["score"], "pChEMBL", (l.get("known_activity") or {}).get("pchembl"),
          (l.get("known_activity") or {}).get("activity"), "PAINS", l["pains"])

docking = D.dock_leads(leads, ACC, top_n=5)
print("DOCK_LEADS:", docking.get("ok"), docking.get("pdb_id"),
      docking.get("center"), docking.get("error"))
for r in docking.get("results", []):
    print("  DOCK:", r.get("label"), r.get("affinity_kcal_mol"), r.get("ok"))
q = next((l for l in leads if l.get("label") == "QUERY"), None)
docked = {r.get("label") for r in docking.get("results", [])}
if docking.get("ok") and q and "QUERY" not in docked:
    r = D.dock(q["smiles"], docking["pdb_id"], docking["center"], box_size=22.5)
    r["label"] = "QUERY"
    r["rank"] = q.get("rank")
    docking["results"].append(r)
    docking["results"].sort(key=lambda x: x.get("affinity_kcal_mol", 999))
    print("  DOCK-QUERY:", r.get("label"), r.get("affinity_kcal_mol"))

res = {"ok": True,
       "correction_note": ("Standard run picked wrong ChEMBL target CHEMBL2074 "
                           "(Maltase-glucoamylase). This re-run pins CHEMBL235 "
                           "(Peroxisome proliferator-activated receptor gamma). "
                           "Same UniProt P37231, same PDB/centre, same protocol."),
       "chembl_target": CHEMBL_TARGET,
       "ligands_found": len(ligands),
       "leads": leads,
       "docking": docking,
       "topic": {"target": "Peroxisome proliferator-activated receptor gamma (PPAR-gamma)",
                 "reference": "pioglitazone"}}
with open("/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/"
          "hidden_files/dock-HP-002-2026-11-11-CORRECTED.json", "w", encoding="utf-8") as f:
    json.dump(res, f, indent=1)
print("RAW_SAVED")
