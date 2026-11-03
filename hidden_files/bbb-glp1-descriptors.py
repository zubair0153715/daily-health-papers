# BBB-descriptor computation for the Brain paper (2026-11-02)
# Source: PubChem PUG REST, fetched 2026-11-02 ~19:40 PKT
#   https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/<name>/property/CanonicalSMILES,MolecularWeight,TPSA,HBondDonorCount,HBondAcceptorCount,RotatableBondCount,XLogP/JSON
# Cross-check: RDKit (LeadForge venv ~/workspace/.venv-fc/bin/python), bbb_check.py
#   exenatide RDKit: MW 4186.6, TPSA 1750, HBD 58, HBA 60, RotB 134 (PubChem TPSA 1780, HBA 66 - method difference, small)
#   danuglipron RDKit: MW 555.6, TPSA 114, HBD 1 (exact match to PubChem)
#   orforglipron RDKit: MW 883.0, TPSA 156, HBD 1 (PubChem TPSA 144 - method difference, small)
# BBB criteria used (standard CNS design cut-offs): MW <= 450 Da, TPSA <= 90 A^2, HBD <= 3, 1 <= logP <= 3
# LogP is method-dependent (PubChem XLogP vs RDKit MolLogP differ, e.g. danuglipron 1.4 vs 4.89) - conclusions do not rest on logP.
import json
rows = [
    # name, CID, MW, TPSA, HBD, HBA, RotB, XLogP, trial status
    ("exenatide",     45588096, 4187, 1780, 58, 66, 135, -21.0, "Exenatide-PD3 phase III (negative); Exenatide-PD phase II (signal)"),
    ("lixisenatide",  90472060, 4858, 2090, 70, 77, 170, -30.8, "LIXIPARK phase II (positive)"),
    ("liraglutide",   16134956, 3751, 1510, 54, 55, 132,  -3.4, "No PD RCT; peptide comparator"),
    ("semaglutide",   56843331, 4114, 1650, 57, 63, 151,  -5.8, "MOST-ABLE phase II ongoing (oral semaglutide)"),
    ("tirzepatide",  166567236, 4813, 1790, 58, 70, 163,  -6.8, "No PD RCT; dual GLP-1/GIP comparator"),
    ("orforglipron", 137319706,  883,  144,  1, 10,   7,   6.8, "Small-molecule GLP-1RA candidate; no PD trial"),
    ("danuglipron",  134611040,  556,  114,  1,  9,   9,   1.4, "Small-molecule GLP-1RA candidate; no PD trial"),
]
for name, cid, mw, tpsa, hbd, hba, rotb, logp, status in rows:
    criteria = sum([mw <= 450, tpsa <= 90, hbd <= 3, 1 <= logp <= 3])
    print(f"{name:14s} CID {cid:<10d} MW {mw:>6.1f} ({mw/450:4.1f}x limit)  TPSA {tpsa:>5.0f} ({tpsa/90:4.1f}x)  HBD {hbd:>2d}  HBA {hba:>2d}  XLogP {logp:>6.1f}  criteria {criteria}/4  | {status}")
print()
print("Peptide range: MW 3751-4858 Da = 8.3-10.8x the 450 Da cut-off; TPSA 1510-2090 A^2 = 16.8-23.2x the 90 A^2 cut-off.")
print("Danuglipron closest to BBB space: MW 1.23x, TPSA 1.27x over cut-offs; orforglipron MW 1.96x, TPSA 1.6x over, XLogP 6.8 (too lipophilic).")
