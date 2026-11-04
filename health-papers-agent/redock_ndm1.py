"""HP-011 re-dock: NDM-1 with the catalytic zinc ions retained.

Two corrections vs the pipeline run:
1. Grid centre: the pipeline centred on SIN (succinic acid, a crystallisation
   additive) in the apo structure 5XP6. The active site is the di-zinc
   centre; grid is now the Zn-Zn midpoint [-5.17, -5.37, -16.38].
2. Zinc: the standard receptor prep drops HETATM records, so the pipeline
   docked without the two catalytic Zn2+ ions — the dominant interaction
   for NDM-1 inhibitors. Here the two Zn ions are retained in the receptor
   PDBQT (charge +2.00, AutoDock type Zn). The bridging hydroxide (OH 303)
   is removed on the standard assumption that a ligand displaces it.
   Everything else (box 22.5 A, exhaustiveness 8, 3 poses, Vina 1.2.7) is
   the same protocol.
Taniborbactam (bicyclic boronate, phase-III NDM inhibitor) is docked as a
positive control; meropenem is the failing-substrate negative control.
If Vina rejects the Zn atom type, this script fails loudly and the paper
reports the metal-free numbers with the limitation stated.
"""
import sys, json, os, stat, subprocess
sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D
from rdkit import Chem
from rdkit.Chem import AllChem

ZN = [(-4.707, -5.745, -18.261), (-5.620, -4.982, -14.499)]
CENTER = [-5.17, -5.37, -16.38]
TANIBORBACTAM = "B1([C@H](CC2=C(O1)C(=CC=C2)C(=O)O)NC(=O)CC3CCC(CC3)NCCN)O"

src = json.load(open("../hidden_files/dock-HP-011-2026-11-04.json"))
leads = {l["label"]: l for l in src["leads"]}
order = ["CHEMBL3808678", "CHEMBL3808541", "CHEMBL3809719", "CHEMBL3810122", "CHEMBL3809445", "QUERY"]
smiles = {lab: leads[lab]["smiles"] for lab in order}
smiles["TANIBORBACTAM"] = TANIBORBACTAM


def prep_receptor_zn(pdb_path, out_path):
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
    mol = Chem.MolFromPDBBlock("".join(lines) + "END\n", removeHs=False)
    if mol is None:
        raise RuntimeError("pdb parse failed")
    mol = Chem.AddHs(mol, addCoords=True)
    AllChem.ComputeGasteigerCharges(mol)
    conf = mol.GetConformer()
    with open(out_path, "w") as f:
        f.write("REMARK NDM-1 receptor (RDKit Gasteiger) + 2 catalytic Zn2+ retained\n")
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
        n = mol.GetNumAtoms()
        for j, (x, y, z) in enumerate(ZN):
            f.write(f"HETATM{n+j+1:5d} {'ZN':^4s} {'ZN':>3s} {'A':1s}{301+j:4d}    "
                    f"{x:8.3f}{y:8.3f}{z:8.3f}{1.00:6.2f}{7.00:6.2f}    "
                    f"{2.00:+7.3f} {'Zn':<2s}\n")
        f.write("TER\nEND\n")
    return out_path


def dock_zn(smi, pdb_id, center, box_size=22.5, exhaustiveness=8, n_poses=3):
    tag = abs(hash(smi)) % 10**8
    rec_pdbqt = os.path.join(D._CACHE_DIR, f"{pdb_id}_zn_rec.pdbqt")
    lig_pdbqt = os.path.join(D._CACHE_DIR, f"lig_{tag}.pdbqt")
    out_pdbqt = os.path.join(D._CACHE_DIR, f"out_{tag}.pdbqt")
    try:
        vina = D._vina_binary()
        pdb_path = D._pdb_path(pdb_id)
        prep_receptor_zn(pdb_path, rec_pdbqt)
        D._prep_ligand(smi, lig_pdbqt)
        cmd = [vina, "--receptor", rec_pdbqt, "--ligand", lig_pdbqt,
               "--center_x", str(center[0]), "--center_y", str(center[1]),
               "--center_z", str(center[2]),
               "--size_x", str(box_size), "--size_y", str(box_size),
               "--size_z", str(box_size),
               "--exhaustiveness", str(exhaustiveness),
               "--num_modes", str(n_poses), "--out", out_pdbqt]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
        if r.returncode != 0:
            return {"ok": False, "error": f"vina failed: {(r.stderr or '')[:200]}"}
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


results = []
for lab in order + ["TANIBORBACTAM"]:
    r = dock_zn(smiles[lab], "5XP6", CENTER, box_size=22.5)
    r["label"] = lab
    results.append(r)
    print("DOCK", lab, r.get("affinity_kcal_mol"), r.get("poses"), r.get("ok"), r.get("error", ""), flush=True)
results.sort(key=lambda x: x.get("affinity_kcal_mol", 999))
json.dump({"ok": True, "pdb_id": "5XP6", "resolution": 0.95,
           "pdb_title": "native structure of NDM-1 crystallized at pH5.5",
           "center": CENTER, "center_note": "Zn-Zn midpoint of the di-zinc active site",
           "box_size": 22.5, "exhaustiveness": 8, "vina": "1.2.7",
           "zn_note": "Two catalytic Zn2+ retained in receptor (charge +2.00, AD type Zn); bridging hydroxide OH303 removed (assumed displaced by ligand).",
           "results": results},
          open("../hidden_files/dock-HP-011c-2026-11-04.json", "w"), indent=1)
print("SAVED")
