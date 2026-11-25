"""EZH2 correction dock for HP-127 (2026-11-25) — leads vs tazemetostat on 5WG6 + 5HYN.

CENTRE AUDIT — why this run exists (same failure class as TYK2/3LXP, 2026-11-11):
the pipeline's find_pdb_for_uniprot(Q15910) auto-picked 5U5T (1.60 A, first by
resolution) and docked tazemetostat + leads into it. 5U5T is EED — the
NON-catalytic PRC2 subunit — in complex with an EED-binder (Lingel et al.,
J Med Chem 2017;60:415-427). Tazemetostat is a SAM-competitive inhibitor of
the EZH2 SET domain; docking it into EED's H3K27me3 pocket answers nothing.
The run was killed before it saved anything (EXIT 143, no JSON written).
UniProt Q15910 xref_pdb lists 5U5T first (1.60 A) because the EED-binder
series (5U5T, 5U62, 5H14, 5H19, 7QK4, 7QJG, 7QJU) is cross-referenced to
EZH2; the auto-pick trusts UniProt xrefs and resolution, so it lands on the
wrong subunit. The <3.0 A filter also excludes the correct structure 5WG6
(3.90 A).

CORRECT STRUCTURES (verified by direct PDB inspection, 2026-11-25):
- PRIMARY 5WG6 (Bratkowski et al., Sci Rep 2018;8:9092): human PRC2 in
  complex with GSK126, a SAM-competitive pyridone EZH2 inhibitor of the same
  class as tazemetostat. Only drug-like HETATM is A9G (GSK126, chain A,
  39 atoms); dock._ligand_center = [-81.71, 2.47, -54.66] = the GSK126
  centroid in the EZH2 SET-domain SAM pocket. Resolution 3.90 A (stated as a
  limit); EZH2 is an EZH2-SUZ12 chimera, SET domain is EZH2's.
- CROSS-CHECK 5HYN (2.95 A): human PRC2 with H3K27M peptide + SAH in the
  SAM pocket. NOTE: dock._ligand_center(5HYN) returns [79.59, -82.35, 23.29],
  the M3L trimethyllysine of the JARID2 peptide in EED's pocket — WRONG for
  a SAM-competitive inhibitor. The correct centre is the SAH chain A
  centroid [81.25, -98.86, 2.65] (the SAM pocket), computed directly from the
  PDB file; ~28 A from the M3L centroid. 4MI5 (2.0 A, isolated EZH2
  catalytic domain + SAH) was rejected: Antonysamy et al. (PLoS One 2013)
  show its cofactor site is only partially formed (post-SET displaced).

This script re-runs the LeadForge pipeline (UniProtKB Q15910 -> ChEMBL
CHEMBL2189110 -> PubChem -> RDKit -> ADMET/PAINS -> ranking) to recover the
lead set, then docks the top 5 leads + the QUERY (tazemetostat) on 5WG6, and
the QUERY + top 2 leads on 5HYN, same box (22.5 A) and exhaustiveness (8)
as Papers #1/#3.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery.pipeline import run_pipeline  # noqa: E402
from app.discovery import dock as D  # noqa: E402
from rdkit import Chem  # noqa: E402
from rdkit.Chem import Descriptors, Lipinski, rdMolDescriptors  # noqa: E402
from rdkit.Chem.FilterCatalog import FilterCatalog, FilterCatalogParams  # noqa: E402

BASE = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts"
PIPE_OUT = f"{BASE}/hidden_files/dock-HP-127-2026-11-25.json"
OUT_5WG6 = f"{BASE}/hidden_files/dock-HP-127-2026-11-25-5WG6.json"
OUT_5HYN = f"{BASE}/hidden_files/dock-HP-127-2026-11-25-5HYN.json"

CENTER_5WG6 = [-81.71, 2.47, -54.66]   # GSK126 (A9G, chain A) centroid via dock._ligand_center
CENTER_5HYN = [81.25, -98.86, 2.65]    # SAH chain A centroid (SAM pocket); NOT _ligand_center (M3L/EED)


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


def dock_set(leads, pdb_id, center, note):
    results = []
    for l in leads:
        desc, pains = descriptors(l["smiles"])
        r = D.dock(l["smiles"], pdb_id, center, box_size=22.5)
        r["label"] = l.get("label")
        r["rank"] = l.get("rank")
        r["chembl_id"] = l.get("chembl_id")
        r["similarity"] = l.get("similarity")
        r["descriptors"] = desc
        r["pains"] = pains
        results.append(r)
        print(f"DOCK {pdb_id}:", l.get("label"), r.get("affinity_kcal_mol"),
              r.get("ok"), "PAINS:", pains, flush=True)
    results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
    return {"ok": True, "pdb_id": pdb_id, "center": center,
            "center_note": note, "box_size": 22.5, "exhaustiveness": 8,
            "results": results}


def main():
    res = run_pipeline("Enhancer of zeste homolog 2 (EZH2)",
                       query_name="tazemetostat", top_n=25, dock_top_n=0)
    print("PIPELINE OK:", res.get("ok"), flush=True)
    leads = res.get("leads") or []
    print("LEADS:", len(leads), flush=True)
    for l in leads[:6]:
        print("  LEAD:", l.get("rank"), l.get("label"), l.get("chembl_id"),
              "sim:", l.get("similarity"), flush=True)
    q = next((l for l in leads if l.get("label") == "QUERY"), None)
    top5 = [l for l in leads if l.get("label") != "QUERY"][:5]
    dock_list = top5 + ([q] if q else [])
    if not q:
        print("WARNING: no QUERY lead in pipeline output — tazemetostat "
              "docked from PubChem SMILES fallback", flush=True)
    res["topic"] = {"target": "Enhancer of zeste homolog 2 (EZH2)",
                    "reference": "tazemetostat", "topic_id": "HP-127",
                    "date": "2026-11-25"}
    res["docking"] = None
    res["docking_note"] = ("Pipeline docking skipped by design (dock_top_n=0); "
                           "corrected docking is in dock-HP-127-2026-11-25-5WG6.json "
                           "and dock-HP-127-2026-11-25-5HYN.json. The first auto-pick "
                           "(5U5T, EED subunit) was wrong and that run was killed "
                           "before saving; see the correction script header.")
    with open(PIPE_OUT, "w", encoding="utf-8") as f:
        json.dump(res, f, indent=1)
    print("PIPELINE SAVED:", PIPE_OUT, flush=True)

    # Primary: 5WG6, top 5 leads + query
    d6 = dock_set(dock_list, "5WG6", CENTER_5WG6,
                  "GSK126 (A9G, chain A) centroid via dock._ligand_center — "
                  "EZH2 SET-domain SAM pocket, human PRC2 + GSK126, 3.90 A "
                  "(Bratkowski et al., Sci Rep 2018;8:9092)")
    d6["topic"] = res["topic"]
    d6["resolution"] = 3.9
    d6["correction_note"] = ("Auto-pick 5U5T was EED, not EZH2 — killed before "
                             "saving. 5WG6 is the inhibitor-bound human PRC2 "
                             "structure; GSK126 is a SAM-competitive pyridone "
                             "of the same class as tazemetostat.")
    with open(OUT_5WG6, "w", encoding="utf-8") as f:
        json.dump({"topic": res["topic"], "docking": d6}, f, indent=1)
    print("SAVED:", OUT_5WG6, flush=True)

    # Cross-check: 5HYN, query + top 2 leads
    cross = ([q] if q else []) + top5[:2]
    dh = dock_set(cross, "5HYN", CENTER_5HYN,
                  "SAH chain A centroid (SAM pocket), computed directly from "
                  "the PDB file — dock._ligand_center(5HYN) returns the M3L "
                  "trimethyllysine in EED's pocket, ~28 A away, and is WRONG "
                  "for a SAM-competitive inhibitor")
    dh["topic"] = res["topic"]
    dh["resolution"] = 2.95
    dh["correction_note"] = ("Cross-check on the higher-resolution active PRC2 "
                             "(2.95 A). Centre is SAH, not the _ligand_center "
                             "M3L pick.")
    with open(OUT_5HYN, "w", encoding="utf-8") as f:
        json.dump({"topic": res["topic"], "docking": dh}, f, indent=1)
    print("SAVED:", OUT_5HYN, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
