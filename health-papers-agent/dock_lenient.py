"""Lenient receptor prep for PDBs whose charge annotation breaks RDKit.

Root cause (found 2026-11-24, HP-146/HP-140): RDKit's PDB parser reads the
charge field (cols 79-80, e.g. "1-" on ASP/GLU carboxylate oxygens) and
assigns formal charge -1 to the oxygen; its bond-order perception then
gives that oxygen a double bond, i.e. explicit valence 2 on O(-1), and
standard sanitization fails ("Explicit valence ... greater than permitted").
Structures affected so far: 8XFD (PKR) and 8HCQ (ETA). The fix is minimal
and coordinate-preserving: blank cols 79-80 of the ATOM lines before
parsing, so RDKit perceives the carboxylate normally. Standard sanitization
then succeeds WITH proper aromaticity (8XFD: 768 aromatic C; 8HCQ: 845) —
unlike the sanitize=False fallback, which perceives zero aromatic atoms
and would mistype every aromatic receptor carbon in Vina.

Usage: call install_charge_blanked_prep() before D.dock(); it monkeypatches
D._prep_receptor with an otherwise identical copy. Only the two correction
scripts that need it import this module.
"""
import os
import sys

sys.path.insert(0, "/home/hatch/workspace/clinic-demo")
from app.discovery import dock as D  # noqa: E402
from rdkit import Chem  # noqa: E402
from rdkit.Chem import AllChem  # noqa: E402


def _prep_receptor_charge_blanked(pdb_path, out_path):
    """Copy of dock._prep_receptor with cols 79-80 blanked before parsing."""
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
                l = line[:16] + " " + line[17:]
                # blank the charge field (cols 79-80) — see module docstring
                if len(l) > 80:
                    l = l[:78] + "  " + l[80:]
                lines.append(l)
            elif line.startswith("END"):
                break
    mol = Chem.MolFromPDBBlock("".join(lines) + "END\n", removeHs=False)
    if mol is None:
        raise RuntimeError("pdb parse failed")
    mol = Chem.AddHs(mol, addCoords=True)
    AllChem.ComputeGasteigerCharges(mol)
    conf = mol.GetConformer()
    with open(out_path, "w") as f:
        f.write("REMARK LeadForge receptor (RDKit Gasteiger, simplified AD types)\n")
        for i, atom in enumerate(mol.GetAtoms()):
            pos = conf.GetAtomPosition(i)
            try:
                chg = float(atom.GetProp("_GasteigerCharge"))
            except Exception:
                chg = 0.0
            if abs(chg) > 99:
                chg = 0.0
            name = atom.GetPDBResidueInfo().GetName().strip() if atom.GetPDBResidueInfo() else atom.GetSymbol()
            res = atom.GetPDBResidueInfo().GetResidueName().strip() if atom.GetPDBResidueInfo() else "UNK"
            chain = atom.GetPDBResidueInfo().GetChainId().strip() if atom.GetPDBResidueInfo() else "A"
            resseq = atom.GetPDBResidueInfo().GetResidueNumber() if atom.GetPDBResidueInfo() else 1
            el = atom.GetSymbol()
            f.write(f"ATOM  {i+1:5d} {name:^4s} {res:>3s} {chain:1s}{resseq:4d}    "
                    f"{pos.x:8.3f}{pos.y:8.3f}{pos.z:8.3f}{0.0:6.2f}{0.0:6.2f}    "
                    f"{chg:+7.3f} {D._ad_type(atom):<2s}\n")
        f.write("TER\nEND\n")
    return out_path


def install_charge_blanked_prep():
    D._prep_receptor = _prep_receptor_charge_blanked
