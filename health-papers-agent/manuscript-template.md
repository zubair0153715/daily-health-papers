# [Title: the claim in one line — molecule/target/disease, no hype words]

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** YYYY-MM-DD · **Health Papers Agent — Paper #N** (daily 5-paper run)

**Keywords:** [keyword 1]; [keyword 2]; [keyword 3]; [keyword 4]; [keyword 5]; [keyword 6]; [keyword 7]; [keyword 8]

---

## Abstract

[One paragraph, plain text, 1,500–2,500 characters. Structure: the problem in one sentence → the gap/confounder → what was computed (method + targets + reference drug, same protocol) → the single headline result with the number → the honest limit (Vina noise ±1–2 kcal/mol, PAINS if present) → the falsifiable next step (assay or trial design). Must end with what would confirm or refute the claim. No citations inside the abstract.]

---

## 1. Introduction

[The health problem: burden numbers with real sources (Pakistan + global). What the reference drug does and where it fails. The specific gap this paper attacks. The falsifiable hypothesis, stated in one sentence.]

## 2. Methods

### 2.1 Literature basis

[What was searched, where (PubMed / bioRxiv / ChEMBL / daily digest date), and the key sources the claim rests on. Real references only — every citation in the References section must have been verified (PMID/DOI checked, not invented).]

### 2.2 Molecular docking

[Standardised AutoDock Vina protocol, exactly as Papers #1/#3: Vina version, PDB ID, same binding site/grid centre/box for test compound and reference drug, same exhaustiveness, best of three poses reported. If no experimental structure exists, say so plainly and skip docking — never substitute a made-up structure. Ligand sources: ChEMBL/PubChem IDs.]

### 2.3 PAINS screen

[RDKit PAINS filter result for every test compound. A PAINS alert is reported, never hidden; it changes the validation design (redox controls).]

### 2.4 Honesty limits

[What this paper cannot show: docking ≠ activity; Vina noise ±1–2 kcal/mol; no experimental data; no MD/free-energy refinement unless actually run.]

## 3. Results

### 3.1 Docking: the comparison table

[Table: compound | target (PDB) | best affinity (kcal/mol) | pose consistency | PAINS. Reference drug in the same table, same protocol. State wins AND losses — a paper that only reports wins is not honest.]

### 3.2 Comparison with published docking

[How the numbers compare with published docking on the same target, if any exists. If none exists, say so.]

### 3.3 The standardisation / quality problem (if applicable)

[Any real-world confounder that affects the claim (product variability, resistance mutations, assay variability) with real numbers.]

## 4. Discussion

### 4.1 The reframe (if the result changes the question)

[What the result means — and what it does not mean.]

### 4.2 Why the "win" must not be over-read

[The noise margin, the PAINS caveat, the single-structure limit.]

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

[How the validation assay is designed to expose artefacts (e.g. redox controls).]

### 4.4 Testable hypotheses

[Numbered, falsifiable, each with the measurement that would settle it.]

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

[Concrete stages: what assay, what controls, what readout, what sample size logic.]

## 5. Limitations

[Numbered, blunt: docking only; noise margin; no experimental data; no MD; literature limits; any missing data (e.g. no local-market data yet).]

## 6. Conclusion

[Two to four sentences: the claim, the limit, the next experiment. No cure claims, no clinical recommendations.]

## Acknowledgments

[AI assistance disclosure — REQUIRED in every paper: "This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content." Plus any human contributors.]

## References

[Numbered, real only. Each entry verified: authors, year, journal, PMID or DOI that resolves. No invented references — if a reference cannot be verified, it does not go in.]

## Data availability

[Where the raw numbers live: docking raw JSON file name in hidden_files/, ChEMBL/PubChem IDs, PDB IDs. "All docking scores reported here are in [file]; no additional data were generated."]
