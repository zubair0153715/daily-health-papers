"""HP-041 redock: the pipeline's auto-picked PDB 7K93 is DENV2 NS1 + Fab
(NOT the protease), so its -6.97 kcal/mol score is discarded.
Re-dock the two published inhibitors on verified DENV NS2B-NS3 protease
structures, using dock._ligand_center (audited centre pick) on each:
  6MO2 - DENV-2 protease + allosteric inhibitor, 2.8 A (Yao et al., JACS 2019)
  3U1I - DENV protease + covalently bound peptide, 2.3 A (active site)
Compounds: NSC135618 (PubChem CID 282274) and ARDP0006 (CID 3378440).
Same protocol as the pipeline: box 22.5 A, exhaustiveness 8, 3 poses.
"""
import json
import sys
from collections import defaultdict

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D

COMPOUNDS = {
    "NSC135618": "C1=CC(=CC(=C1)Cl)NC(=O)C2=C(C=CC(=C2)N=NC3=C(C=C(C=C3)[N+](=O)[O-])Cl)O",
    "ARDP0006": "C1=CC(=C2C(=C1[N+](=O)[O-])C(=O)C3=C(C=CC(=C3C2=O)O)[N+](=O)[O-])O",
}

OUT = "/home/hatch/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/hidden_files/dock-HP-041-2026-11-11-redock.json"


def hetatm_groups(pdb_path):
    groups = defaultdict(list)
    with open(pdb_path) as f:
        for line in f:
            if line.startswith("HETATM"):
                res = (line[17:20].strip(), line[21].strip(), line[22:26].strip())
                groups[res].append((float(line[30:38]), float(line[38:46]), float(line[46:54])))
    return groups


def centroid(atoms):
    n = len(atoms)
    return [round(sum(c[i] for c in atoms) / n, 2) for i in range(3)]


def main():
    report = {"structures": {}, "docking": []}
    for pdb_id in ("6MO2", "3U1I"):
        path = D._pdb_path(pdb_id)
        groups = hetatm_groups(path)
        print(f"== {pdb_id} HETATM groups ==", flush=True)
        for res, atoms in groups.items():
            print(f"   {res} n={len(atoms)} centroid={centroid(atoms)}", flush=True)
        center = D._ligand_center(path)
        print(f"== {pdb_id} audited centre: {center}", flush=True)
        # identify which group the centre matches
        picked = None
        for res, atoms in groups.items():
            if centroid(atoms) == [round(c, 2) for c in center]:
                picked = {"residue": res, "n_atoms": len(atoms)}
        print(f"   picked group: {picked}", flush=True)
        report["structures"][pdb_id] = {"center": center, "picked_group": picked,
                                        "groups": {str(k): len(v) for k, v in groups.items()}}
        for label, smi in COMPOUNDS.items():
            r = D.dock(smi, pdb_id, center, box_size=22.5)
            r["label"] = label
            r["pdb_id"] = pdb_id
            print(f"  DOCK {label} on {pdb_id}: {r.get('affinity_kcal_mol')} poses={r.get('poses')} ok={r.get('ok')} {r.get('error','')}", flush=True)
            report["docking"].append(r)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=1)
    print("RAW_SAVED:", OUT, flush=True)


if __name__ == "__main__":
    main()
