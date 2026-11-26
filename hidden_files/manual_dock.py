"""Manual docking on an explicitly chosen PDB (bypasses the auto-picker).

Usage (RDKit venv):
  ~/workspace/.venv-fc/bin/python manual_dock.py spec.json out.json

spec.json: {"pdb_id": "4ZUD", "ligands": [{"label": "losartan", "smiles": "..."}],
            "box_size": 22.5}
Centre is always dock._ligand_center (never hand-picked); the script fails
loudly if no ligand centre exists, so a centre-free structure is never
silently docked. One ligand takes ~30s-3min.
"""
import json
import os
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D


def main():
    spec = json.load(open(sys.argv[1], encoding="utf-8"))
    out_path = sys.argv[2]
    pdb_id = spec["pdb_id"]
    box = spec.get("box_size", 22.5)
    pdb_path = D._pdb_path(pdb_id)
    center = D._ligand_center(pdb_path)
    print("PDB:", pdb_id, "CENTER:", center, flush=True)
    if not center:
        print("FAIL: no drug-like ligand centre in", pdb_id, flush=True)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump({"ok": False, "pdb_id": pdb_id, "center": None,
                       "error": "no_ligand_site", "results": []}, f, indent=1)
        return 2
    # Resume: keep already-docked ligands from a partial output file.
    done = {}
    if os.path.exists(out_path):
        try:
            prev = json.load(open(out_path, encoding="utf-8"))
            for r in prev.get("results", []):
                if r.get("ok") and r.get("affinity_kcal_mol") is not None:
                    done[r["label"]] = r
            print("RESUME: %d ligands already done" % len(done), flush=True)
        except Exception:
            pass
    results = []

    def save(partial):
        res = {"ok": not partial, "partial": partial, "pdb_id": pdb_id,
               "center": [round(c, 2) for c in center],
               "results": sorted(results,
                                 key=lambda x: x.get("affinity_kcal_mol", 999))}
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(res, f, indent=1)

    for lig in spec["ligands"]:
        if lig["label"] in done:
            print("  SKIP (done):", lig["label"],
                  done[lig["label"]].get("affinity_kcal_mol"), flush=True)
            results.append(done[lig["label"]])
            continue
        r = D.dock(lig["smiles"], pdb_id, center, box_size=box)
        r["label"] = lig["label"]
        print("  DOCK:", lig["label"], r.get("affinity_kcal_mol"), r.get("ok"),
              r.get("error", ""), flush=True)
        results.append(r)
        save(partial=True)  # incremental: a restart loses at most one ligand
    save(partial=False)
    print("SAVED:", out_path, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
