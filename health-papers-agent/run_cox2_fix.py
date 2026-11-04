"""HP-047 fix: complete dual-isoform docking with corrected ligand set.

Fixes vs run_cox2.py:
1. Ligand set: top 5 DISTINCT leads (QUERY=celecoxib is itself rank 1, and
   CHEMBL118 IS celecoxib) + QUERY. Distinct leads: CHEMBL282093,
   CHEMBL502555, CHEMBL525247, CHEMBL186632, CHEMBL432945.
2. COX-1 (3KK6) receptor prep: the PDB file has a crystallographic close
   contact (VAL349 chain B carbonyl O within bonding distance of SER353 OG)
   that RDKit's distance-based bonding turns into a spurious bond, so
   MolFromPDBBlock sanitisation fails ("Explicit valence for atom O, 3").
   Fix: parse with sanitize=False, drop any bond on an oxygen with degree
   > 2 (longest first), then sanitise. Verified: sanitise + Gasteiger OK.
   3LN1 (COX-2) uses the standard D.dock path (its file parses cleanly).
"""
import sys, json, os, stat, subprocess
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D
from rdkit import Chem
from rdkit.Chem import AllChem

src = json.load(open("../hidden_files/dock-HP-047-2026-11-04.json"))
leads = {l["label"]: l for l in src["leads"]}
order = ["CHEMBL282093", "CHEMBL502555", "CHEMBL525247", "CHEMBL186632", "CHEMBL432945", "QUERY"]
print("DOCK ORDER:", order, flush=True)


def prep_receptor_fixed(pdb_path, out_path):
    if os.path.exists(out_path) and os.path.getsize(out_path) > 1000:
        return out_path
    seen = set()
    lines = []
    with open(pdb_path) as f:
        for line in f:
            if line.startswith("ATOM"):
                alt = line[16]
                key = line[12:27]
                if alt not in (" ", "A"):
                    continue
                if key in seen:
                    continue
                seen.add(key)
                lines.append(line[:16] + " " + line[17:])
            elif line.startswith("END"):
                break
    mol = Chem.MolFromPDBBlock("".join(lines) + "END\n", removeHs=False, sanitize=False)
    if mol is None:
        raise RuntimeError("pdb parse failed")
    rw = Chem.RWMol(mol)
    conf = rw.GetConformer()
    # drop spurious bonds: any oxygen with degree > 2 loses its longest bond
    for a in list(rw.GetAtoms()):
        if a.GetSymbol() == "O" and a.GetDegree() > 2:
            nb = max(a.GetNeighbors(),
                     key=lambda n: conf.GetAtomPosition(a.GetIdx()).Distance(
                         conf.GetAtomPosition(n.GetIdx())))
            rw.RemoveBond(a.GetIdx(), nb.GetIdx())
            print("  fixed spurious bond on O idx", a.GetIdx(), "->", nb.GetIdx(), flush=True)
    mol = rw.GetMol()
    Chem.SanitizeMol(mol)
    mol = Chem.AddHs(mol, addCoords=True)
    AllChem.ComputeGasteigerCharges(mol)
    conf = mol.GetConformer()
    with open(out_path, "w") as f:
        f.write("REMARK LeadForge receptor (RDKit Gasteiger, simplified AD types; 3KK6 spurious-bond fix)\n")
        for i, atom in enumerate(mol.GetAtoms()):
            pos = conf.GetAtomPosition(i)
            try:
                chg = float(atom.GetProp("_GasteigerCharge"))
            except Exception:
                chg = 0.0
            if abs(chg) > 99:
                chg = 0.0
            info = atom.GetPDBResidueInfo()
            name = info.GetName().strip() if info else atom.GetSymbol()
            res = info.GetResidueName().strip() if info else "UNK"
            chain = info.GetChainId().strip() if info else "A"
            resseq = info.GetResidueNumber() if info else 1
            f.write(f"ATOM  {i+1:5d} {name:^4s} {res:>3s} {chain:1s}{resseq:4d}    "
                    f"{pos.x:8.3f}{pos.y:8.3f}{pos.z:8.3f}{0.0:6.2f}{0.0:6.2f}    "
                    f"{chg:+7.3f} {D._ad_type(atom):<2s}\n")
        f.write("TER\nEND\n")
    return out_path


def dock_fixed(smiles, pdb_id, center, box_size=22.5, exhaustiveness=8, n_poses=3):
    """D.dock but with the spurious-bond-tolerant receptor prep."""
    tag = abs(hash(smiles)) % 10**8
    rec_pdbqt = os.path.join(D._CACHE_DIR, f"{pdb_id}_rec.pdbqt")
    # force re-prep with the fixed routine (remove stale failed/empty file)
    if os.path.exists(rec_pdbqt):
        os.remove(rec_pdbqt)
    lig_pdbqt = os.path.join(D._CACHE_DIR, f"lig_{tag}.pdbqt")
    out_pdbqt = os.path.join(D._CACHE_DIR, f"out_{tag}.pdbqt")
    try:
        vina = D._vina_binary()
        pdb_path = D._pdb_path(pdb_id)
        prep_receptor_fixed(pdb_path, rec_pdbqt)
        D._prep_ligand(smiles, lig_pdbqt)
        cmd = [vina, "--receptor", rec_pdbqt, "--ligand", lig_pdbqt,
               "--center_x", str(center[0]), "--center_y", str(center[1]),
               "--center_z", str(center[2]),
               "--size_x", str(box_size), "--size_y", str(box_size),
               "--size_z", str(box_size),
               "--exhaustiveness", str(exhaustiveness),
               "--num_modes", str(n_poses), "--out", out_pdbqt]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
        if r.returncode != 0:
            return {"ok": False, "error": f"vina failed: {(r.stderr or '')[:150]}"}
        affs = []
        in_table = False
        for line in (r.stdout or "").splitlines():
            if "-----+------------" in line:
                in_table = True
                continue
            if in_table:
                parts = line.split()
                if len(parts) >= 2 and parts[0].isdigit():
                    try:
                        affs.append(float(parts[1]))
                    except ValueError:
                        pass
                elif line.strip().startswith("Writing"):
                    break
        if not affs:
            return {"ok": False, "error": "no poses parsed"}
        return {"ok": True, "affinity_kcal_mol": round(affs[0], 2),
                "poses": [round(a, 2) for a in affs], "pdb_id": pdb_id}
    except Exception as e:
        return {"ok": False, "error": str(e)[:200]}
    finally:
        for p in (lig_pdbqt, out_pdbqt):
            try:
                os.remove(p)
            except OSError:
                pass


def dock_all(pdb_id, center, fn):
    out = []
    for lab in order:
        l = leads[lab]
        r = fn(l["smiles"], pdb_id, center, box_size=22.5)
        r["label"] = lab
        r["rank"] = l.get("rank")
        out.append(r)
        print("DOCK", pdb_id, lab, r.get("affinity_kcal_mol"), r.get("poses"), r.get("ok"), flush=True)
    out.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
    return out

cox2 = dock_all("3LN1", [65.25, -45.38, 45.42], D.dock)
cox1 = dock_all("3KK6", [-32.41, 43.36, -5.62], dock_fixed)
json.dump({"ok": True,
           "cox2": {"pdb_id": "3LN1", "resolution": 2.4,
                    "title": "Structure of celecoxib bound at the COX-2 active site",
                    "center": [65.25, -45.38, 45.42], "results": cox2},
           "cox1": {"pdb_id": "3KK6", "resolution": 2.75,
                    "title": "Crystal Structure of Cyclooxygenase-1 in complex with celecoxib",
                    "center": [-32.41, 43.36, -5.62],
                    "prep_note": "3KK6 receptor prep: removed one spurious RDKit bond (VAL349B O - SER353B OG close contact) before sanitisation; coordinates unchanged.",
                    "results": cox1},
           "box_size": 22.5, "exhaustiveness": 8, "vina": "1.2.7",
           "note": "Dual-isoform dock: same 6 ligands, same protocol on COX-2 (3LN1) and COX-1 (3KK6); selectivity = COX-1 minus COX-2 affinity. CHEMBL118 is celecoxib itself and is reported as QUERY only."},
          open("../hidden_files/dock-HP-047c-2026-11-04.json", "w"), indent=1)
print("SAVED")
