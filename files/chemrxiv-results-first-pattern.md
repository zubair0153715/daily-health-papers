# ChemRxiv Results-First Pattern — standing template for Health papers

**One page. Follow this for every Health paper. Written 4 November 2026, after ChemRxiv rejected Papers #1 and #3 (3–4 Nov 2026) with the same reason: "ChemRxiv does not post proposed frameworks or hypotheses without presenting new research data alongside."**

## The 5 rules

### 1. Title + abstract LEAD WITH THE RESULT AND NUMBERS
The first sentence of the abstract states the measured/computed result with its numbers. The title names the result, not the topic. No "Putative / Predicted / Proposal / Case for / framework" framing in the title or abstract.
- Good (BRAF benchmark, 4 Nov 2026): "Vemurafenib Still Docks Best: Five Sub-nanomolar BRAF V600E Inhibitors Dock Worse Than the Drug They Outperform by ~300-Fold" — result + numbers in the title; abstract opens with the trial data and the docking outcome.
- Bad (Paper #1 v1): "Thymoquinone as a Putative Aldose Reductase Inhibitor…" — a hypothesis wearing a title.

### 2. Results is the spine
Docking tables (all poses, not just the best), ADMET tables, re-dock outcome tables, interaction contacts — in Results, before any interpretation. A paper with no Results tables is a proposal, and ChemRxiv rejects proposals. Negative results count as results: the BRAF paper's cleanest finding was that docking ranked the compounds backwards (Spearman ρ = −0.21), and the Paper #1 v2 correction — epalrestat beating TQ by 1.5 kcal/mol at the true site — is a result, not a failure.

### 3. Hypotheses, assay proposals, trial designs: ONE short "Future work" section near the end only
Never the abstract's closing point, never a full section. One short programme, in order, with falsification conditions. If the future work is longer than the Results, the paper is still a proposal — cut it.

### 4. Never write "No new experimental data are presented"
Replace it with what IS new: "This revision presents new computational data (list the files); no wet-lab data are included." Every submission must be able to point at new data generated for it — a repeat at higher exhaustiveness, an ADMET profile, an interaction analysis, a re-docking validation, a centre audit. If there is no new data, do not submit; generate some first.

### 5. References verified only; data availability cites the actual files
Reuse verified references; add nothing invented. Data availability must name the exact JSON/pose/script paths, including which run is superseded and which run did not complete. State validation failures plainly in Methods/Results/Limitations — never write "validated by re-docking" unless the RMSD is ≤2 Å, and never claim pose-level binding modes as established. Interaction analysis is reported only as observed contacts in the docked poses, labelled as such.

## Two hard lessons from 4 November 2026 (keep these attached to the pattern)

- **Audit the grid centre before believing any docking score.** The centre picker takes the first non-junk HETATM group in file order, and the junk list does not cover glycans, modified protein residues, or cofactors. In the Paper #1 screen, 3 of 5 centres were wrong (AR: NADP+ cofactor; DPP-4: a glycan sugar, 45.24 Å off; PTP1B: a MENA EVH1 residue in a non-PTP1B structure; α-amylase: an apo structure's N-terminus). Reproducibility across exhaustiveness does not validate a comparison — only a centre audit and a crystal-ligand re-dock do.
- **A correction is a paper.** When new data overturn your own lead, report the overturning as the result. ChemRxiv rejected the proposal framing, not the topic — a results-first correction with new numbers is submittable; a reworded proposal is not.

## Housekeeping (unchanged)

- Header "AI-assisted draft — NOT peer-reviewed, NOT published…" + AI-disclosure acknowledgment on every manuscript. Author Zubair Ali, SMBBMU Larkana; Lapis as drafting assistant. Abstract ≤2,500 characters, 8 keywords each. Subject: Medicinal Chemistry. Licence: CC BY 4.0. Final submit click is always the author's.
