# Nintedanib Tops a PknB Docking Rank That Matches Measured Potency Exactly: Two Approved Cancer Kinase Inhibitors and the Mitoxantrone Caveat

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-15 · **Health Papers Agent — Paper #62** (daily 5-paper run)

**Keywords:** PknB; Mycobacterium tuberculosis; nintedanib; sunitinib; mitoxantrone; molecular docking; AutoDock Vina; kinase inhibitor repurposing

---

## Abstract

PknB is an essential serine/threonine kinase of Mycobacterium tuberculosis, and no PknB inhibitor has reached the clinic: the best published inhibitors are nanomolar in vitro and only micromolar against whole cells. We docked five compounds with AutoDock Vina 1.2.7 on 3ORK, the 1.60 angstrom structure of the PknB kinase domain (L33D mutant) with an ATP-gamma-S analogue in the ATP site: nintedanib, two matched-pair aminopyrimidine/pyrazole inhibitors from the same series, sunitinib, and mitoxantrone, the literature PknB inhibitor. The docking rank matches the measured potency rank exactly (Spearman rho 1.0, n = 4): nintedanib, Kd 3.6 nM, docks at minus 9.70 kcal/mol; the matched pair, Ki 13 and 17 nM, at minus 8.66 and minus 8.30; sunitinib, Kd 87 nM, at minus 8.24. Mitoxantrone, which has no attached PknB potency number and is excluded from the correlation, docks worst at minus 7.19 and carries a PAINS alert with the maximum Tox21 read-across for the DNA-damage assays SR-ATAD5 and SR-p53. Two approved cancer kinase inhibitors top a tuberculosis kinase ranking, and the literature inhibitor is the weakest and the most toxic — a clean repurposing signal and a warning in the same table. The falsifiable next step is a single-assay PknB kinase comparison of the four ranked compounds with a whole-cell assay on Mycobacterium tuberculosis H37Rv: if nintedanib again measures most potent on the enzyme but fails on whole cells, the gap is confirmed as permeability, not potency.

---

## 1. Introduction

Tuberculosis killed more people than any other single infectious disease in 2024, and about 390,000 multidrug-resistant/rifampicin-resistant cases were estimated for that year (WHO Global Tuberculosis Report 2025). The pipeline of new tuberculosis drugs is thin, and repurposing approved kinase inhibitors is one of the few routes that can move fast, because the safety data already exist. PknB is the most attractive kinase target in Mycobacterium tuberculosis: it is essential for survival, it regulates cell growth, cell shape and cell division through substrates including GarA, GlmU and EmbR, and it phosphorylates the proteasome alpha-subunit PrcA. Its sibling kinases PknA and PknB are essential, while PknG drives virulence and persistence — which is why multitarget PknA/B/G inhibition is the current design goal, and why a 2026 study reported structural insights into multitargeting the Pkn kinases (Pollaniemi et al., Microbiol Spectr 2026;14:e0004926).

The history of PknB inhibitor discovery is a cautionary tale. A screen of more than 50,000 compounds found ATP-competitive inhibitors that were nanomolar in vitro but only micromolar against whole cells, and none prevented mycobacterial growth at submicromolar concentrations (Lougheed et al., Tuberculosis 2011;91:277–286, PMID 21482481). Mitoxantrone was identified in 2006 as a PknB inhibitor capable of preventing mycobacterial growth (Wehenkel et al., FEBS Lett 2006;580:3018–3022, PMID 16674948), with a co-crystal structure (2FUM) — but mitoxantrone is a DNA intercalator with well-known cardiotoxicity, and no potency number was ever attached to its PknB inhibition in that paper. The question this paper tests is whether a standard rigid-docking screen can rank PknB inhibitors at all, and whether the approved cancer kinase inhibitors nintedanib and sunitinib — both in the ChEMBL bioactivity record for PknB — are worth carrying forward.

**Hypothesis (falsifiable):** under one standardised protocol on the 3ORK ATP site, docking rank will track the measured PknB potency rank (nintedanib first, sunitinib last), and mitoxantrone will score worst, because it is the literature inhibitor with the weakest evidence. Falsified if the docking rank disagrees with the measured rank on any pair, or if mitoxantrone scores within Vina noise of the best compound.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-15 (web search; PubMed; the daily digest of 2026-11-14, which screened 722 candidates and selected 8 — none on PknB, so the digest's relevance here is methodological). Key sources: Lombana et al. 2010 (Structure 18:1667–1677) for the 3ORK structure; Wehenkel et al. 2006 (FEBS Lett 580:3018–3022, PMID 16674948, doi:10.1016/j.febslet.2006.04.046) for mitoxantrone as a PknB inhibitor and structure 2FUM; Lougheed et al. 2011 (Tuberculosis 91:277–286, PMID 21482481, PMCID PMC3158675) for the 50,000-compound screen; Pollaniemi et al. 2026 (Microbiol Spectr 14:e0004926, PMID 42446239) for the multitarget Pkn-kinase structural work; the WHO Global Tuberculosis Report 2025 for the 2024 MDR/RR-TB case estimate; and the 2025 SSRN in-silico PknB screen (doi:10.2139/ssrn.5954835) for the recent computational context. Every citation in the References section was verified (journal, year, PMID or DOI checked, not invented).

### 2.2 Computation

The standard LeadForge pipeline was run with target "Mycobacterium tuberculosis serine/threonine protein kinase B (PknB)" and reference drug mitoxantrone (run_docking.py, RDKit venv, NO_PROXY prefix). Unlike the KRAS and VIM-2 topics, this run was clean: UniProt P9WI81 (PknB, gene pknB, M. tuberculosis H37Rv, 626 amino acids) resolved to ChEMBL target CHEMBL1908385 (Serine/threonine-protein kinase PknB), which returned 57 bioactivities and 26 leads. The structure is 3ORK, 1.60 angstrom — the PknB kinase domain L33D mutant (crystal form 2) with the ATP-gamma-S analogue AGS in the ATP site (Lombana et al. 2010) — with the centre [13.05, 14.71, 12.04] from `D._ligand_center`, the centroid of the AGS analogue. The L33D mutation must be stated: every score in this paper is on the mutant kinase domain, not the wild type.

Five compounds were docked with the standardised protocol, exactly as Papers #1/#3: AutoDock Vina 1.2.7, one box (22.5 angstrom), exhaustiveness 8, best of three poses reported. The four measured compounds: nintedanib (CHEMBL502835; approved 2014), CHEMBL4177445, CHEMBL4172982 and sunitinib (CHEMBL535; approved 2006). Their measured potencies are the ChEMBL bioactivity values for target CHEMBL1908385: nintedanib Kd 3.6 nM; CHEMBL4177445 Ki 13 nM; CHEMBL4172982 Ki 17 nM; sunitinib Kd 87 nM. The two ChEMBL identifiers are a matched pair from one aminopyrimidine/pyrazole series — both MW 390.86, logP 2.79, TPSA 126.65, a 5-cyclopropyl-pyrazol-3-ylamino pyrimidine core, differing only in the sulfonamide phenyl substitution (meta vs para). Mitoxantrone (the query compound, PubChem-verified) carries no measured PknB potency number — Wehenkel et al. 2006 report it qualitatively as a PknB inhibitor that prevents mycobacterial growth — so it is excluded from the rank correlation and reported qualitatively.

### 2.3 PAINS and safety panel

RDKit PAINS filter and the ToxGuard Tox21 kNN read-across panel (12 assays) were applied to every compound. Four of the five are PAINS-clean; mitoxantrone carries a PAINS alert and fails Veber (TPSA 163.18, 12 rotatable bonds, 8 hydrogen-bond donors). Its Tox21 panel is in "measured" mode (maximum similarity 1.0 — the compound is in the Tox21 set) with the maximum values 1.0 for SR-ATAD5 and SR-p53, the two DNA-damage assays. Nintedanib and sunitinib show no decisive Tox21 signal (highest single values 0.239 for sunitinib NR-AhR and 0.084 for nintedanib SR-ARE).

### 2.4 Rank correlation

Spearman rank correlation was computed between the Vina scores and the measured PknB potencies for the four measured compounds (n = 4). The correlation mixes Kd and Ki values — two nintedanib/sunitinib Kd values against two matched-pair Ki values — which is stated here and in the Limitations rather than hidden. A correlation on four points is reported as a descriptive check, not as a validated ranking — the paper's real tests are the matched pair and the mitoxantrone negative control.

### 2.5 Honesty limits

Docking is not activity. Vina noise is ±1–2 kcal/mol; the gap between the first and last measured compounds (1.46 kcal/mol) is inside that noise, so the correlation is a rank match, not a magnitude match. The structure is the L33D mutant. The measured potencies mix Kd and Ki from the ChEMBL record, and the two matched-pair Ki values come from the same series while the two Kd values do not. No molecular dynamics or free-energy refinement was run. No compound was assayed, and no whole-cell data are reported here.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Measured PknB potency | Vina on 3ORK (kcal/mol) | PAINS |
|---|---|---|---|
| Nintedanib (CHEMBL502835) | Kd 3.6 nM | **−9.70** (−9.70, −8.89, −8.72) | clean |
| CHEMBL4177445 | Ki 13 nM | −8.66 (−8.66, −8.12, −7.77) | clean |
| CHEMBL4172982 | Ki 17 nM | −8.30 (−8.30, −8.27, −8.16) | clean |
| Sunitinib (CHEMBL535) | Kd 87 nM | −8.24 (−8.24, −7.94, −7.94) | clean |
| Mitoxantrone (query) | no PknB potency number | −7.19 (−7.19, −7.14, −6.92) | alert |

Scores in kcal/mol, best of three poses (all three poses in parentheses). Measured potencies are ChEMBL bioactivity values for target CHEMBL1908385. Mitoxantrone is excluded from the rank correlation.

The ranking is exact. Nintedanib is first by 1.04 kcal/mol over the matched pair, and the matched pair is ordered correctly (13 nM before 17 nM, by 0.36 kcal/mol), and sunitinib is last among the measured compounds by 0.06 kcal/mol behind CHEMBL4172982 — a gap that is nothing, and which the paper does not pretend is a difference. Mitoxantrone, the literature inhibitor, docks worst at −7.19, a full 2.51 kcal/mol behind nintedanib.

### 3.2 Rank correlation: perfect, and carried by the extremes

Against the measured potencies, Spearman rho is 1.0 (n = 4). The value is carried by nintedanib sitting first and sunitinib sitting last in both rankings; the middle pair is ordered correctly but separated by only 0.36 kcal/mol in docking against a 1.3-fold measured gap. A correlation of 1.0 on four points, with the bottom two separated by nothing, is not a validated ranking — it is a screen that got the order right and cannot separate the bottom two. The honest reading is the same as in Paper #60 (KRAS G12D): the extremes are reliable, the middle is not.

### 3.3 The matched pair: the screen's sharpest test

CHEMBL4177445 and CHEMBL4172982 are the same molecule except for the sulfonamide phenyl substitution — meta in one, para in the other — with identical molecular weight (390.86), logP (2.79) and TPSA (126.65), and measured Ki values of 13 and 17 nM. Docking separates them by 0.36 kcal/mol, in the right direction. That is a real discrimination, but it is a small one: 0.36 kcal/mol is well inside Vina noise, and the 1.3-fold measured gap is itself within assay noise. The pair shows the screen can order a matched pair correctly; it does not show the screen can measure the gap. A screening programme that used the 0.36 kcal/mol difference to choose between them would be choosing on noise.

### 3.4 Mitoxantrone: the literature inhibitor that should not be the lead

Mitoxantrone is the only compound in this set with published evidence of preventing mycobacterial growth (Wehenkel et al. 2006), and it is the weakest by docking (−7.19), the only one with a PAINS alert, the only one that fails Veber, and the only one with maximum Tox21 values on the DNA-damage assays (SR-ATAD5 1.0, SR-p53 1.0 — measured, not read-across). The Tox21 values are consistent with its mechanism: mitoxantrone is a DNA intercalator, and its cardiotoxicity is well documented in its clinical use. The paper's conclusion is not that mitoxantrone does not inhibit PknB — Wehenkel et al. showed that it does, and structure 2FUM shows it in the ATP site. The conclusion is that it is a poor drug candidate for tuberculosis, and that a screen which ranks it last is ranking it correctly on the property that matters for a lead: it should not be the starting point.

### 3.5 ADMET and safety panel

Nintedanib (MW 539.64, logP 3.62, one Lipinski violation by molecular weight) and sunitinib (MW 398.48, logP 3.33, no violations) are both approved drugs with established human safety profiles — that is the point of repurposing them. The matched pair passes Lipinski and Veber outright. No decisive Tox21 signal appears for any of the four measured compounds. The safety story that matters is the one in Section 3.4: the literature inhibitor is the toxic one, and the approved drugs are the clean ones.

## 4. Discussion

### 4.1 What the screen can and cannot say

The screen can say that nintedanib is the best PknB binder in this set, by both measurement and docking, and that sunitinib is the weakest of the measured four, by both. It can say that the matched pair is ordered correctly. It cannot say that CHEMBL4172982 is worse than sunitinib — the 0.06 kcal/mol gap is nothing, and the measured gap (17 vs 87 nM, 5-fold) is real but invisible to the screen at this resolution. And it cannot say anything about mitoxantrone's potency, because there is no measured number to compare against; it can only say that mitoxantrone is the worst by docking and the most toxic by every other measure, which is a reason to stop, not a reason to test it first.

### 4.2 Why this is the clean win of the day

Papers #60 and #61 in this run are both docking failures — a rank inversion on KRAS G12D and a total blindness on VIM-2. This paper is the control that shows the same protocol can work: same Vina version, same box, same exhaustiveness, same PAINS and Tox21 panels, and the ranking comes out exact. The difference is the target, not the method: PknB's ATP site is a well-formed kinase pocket with a hydrophobic back pocket and a hinge, the kind of site rigid docking was built for, while VIM-2's zinc site and KRAS's switch-II pocket are the kinds it was not. The lesson is not that docking works or that it does not — it is that it works on some targets and fails on others, and the only way to know which is to run the control: a set of compounds with known potencies, ranked before the screen is trusted.

### 4.3 The repurposing question

Nintedanib and sunitinib are approved cancer drugs with known human pharmacokinetics. Nintedanib's Kd of 3.6 nM on PknB is the strongest measured value in this set, and its docking score of −9.70 is the best by more than a kilocalorie. The next step is not more docking — it is the enzyme assay and the whole-cell assay, because the 2011 screen's lesson is that nanomolar in vitro potency does not survive the mycobacterial cell wall. If nintedanib measures nanomolar on the enzyme and micromolar on whole cells, the project becomes a permeability problem, and the matched pair — smaller (MW 390.86) and more polar (TPSA 126.65) — is the more promising starting point for optimisation. If nintedanib fails on the enzyme, the docking rank is a false positive and the paper's conclusion is revised.

### 4.4 Testable hypotheses

1. **Enzyme hypothesis.** In a single-assay PknB kinase comparison, nintedanib again measures most potent (IC50 below 10 nM) and sunitinib least potent (above 50 nM), with the matched pair between them. Falsified if any compound measures more than 5-fold from its ChEMBL value — in which case the ChEMBL record, not the screen, is the problem.
2. **Whole-cell hypothesis.** Nintedanib's MIC against M. tuberculosis H37Rv is above 10 µM despite nanomolar enzyme potency, reproducing the 2011 pattern. Falsified if the MIC is below 1 µM — in which case nintedanib is a genuine repurposing candidate and the permeability problem does not apply to it.
3. **Mitoxantrone hypothesis.** Mitoxantrone's PknB IC50, when measured, is above 1 µM — the weakest in the set, matching its docking rank. Falsified if it measures below 100 nM — in which case the docking rank is wrong and the literature inhibitor deserves a second look.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): obtain nintedanib, sunitinib, the matched pair and mitoxantrone; confirm identity and purity by LC-MS and NMR. Stage 2 (weeks 3–6): PknB kinase assay (recombinant PknB, ATP-competitive format), all five compounds on the same plates, in triplicate — the single-assay comparison this paper could not make, and the direct test of hypothesis 1 and 3. Stage 3 (weeks 7–10): MIC assay on M. tuberculosis H37Rv for the four measured compounds, plus cytotoxicity on a human cell line — the direct test of hypothesis 2 and the safety gate for any repurposing claim. Stage 4 (weeks 11–12): if any compound shows an MIC below 1 µM with a selectivity index above 10, dock its analogues and synthesise the best two; if all four are above 10 µM on whole cells, report the negative result and stop. Sample-size logic: three independent biological replicates per IC50 and per MIC determination is the minimum for a defensible potency claim; the nintedanib-versus-sunitinib comparison needs the same, because a false "nintedanib is best" call on a rank match is the error that matters.

## 5. Limitations

1. Docking only; no experimental data were generated, and no compound was assayed.
2. The structure is the L33D mutant kinase domain (3ORK); wild-type PknB may score differently, and the paper does not claim the ranking transfers to the wild type.
3. The measured potencies mix Kd (nintedanib, sunitinib) and Ki (matched pair) from the ChEMBL record; the correlation treats them as one ranking, which is a stated approximation.
4. Spearman rho is computed on four points; it is a descriptive check, not a validated ranking, and the bottom two compounds are separated by 0.06 kcal/mol — nothing.
5. Mitoxantrone carries no measured PknB potency number and is excluded from the correlation; its docking rank is a hypothesis, not a result.
6. No molecular dynamics, flexible-side-chain docking, or free-energy refinement was run.
7. The 2011 screen's whole-cell data are quoted from the literature, not reproduced here; the permeability gap is a hypothesis, not a measurement in this paper.
8. Nintedanib and sunitinib are approved for cancer, not for tuberculosis; repurposing requires the whole-cell and safety data in Section 4.5, and no clinical claim is made.
9. No Pakistan-specific TB burden or PknB prevalence numbers are cited beyond the global MDR-TB count; the paper's relevance to Pakistan is the tuberculosis burden and the repurposing logic — approved drugs are the fastest route a resource-limited setting has.

## 6. Conclusion

On 3ORK, nintedanib docks at −9.70 kcal/mol against a measured Kd of 3.6 nM, the matched pair at −8.66 and −8.30 against Ki values of 13 and 17 nM, and sunitinib at −8.24 against a Kd of 87 nM — a docking rank that matches the measured rank exactly (Spearman rho 1.0, n = 4), while mitoxantrone, the literature PknB inhibitor, docks worst at −7.19 with a PAINS alert and maximum Tox21 values on the DNA-damage assays. Two approved cancer kinase inhibitors top a tuberculosis kinase ranking, and the literature inhibitor is the weakest and the most toxic. The next step is the single-assay kinase and whole-cell comparison in Section 4.5 — and, as a standing rule, the control that makes this paper trustworthy is the one Papers #60 and #61 lacked a clean result from: a set of compounds with known potencies, ranked before the screen is trusted.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No human contributors. The author thanks the ChEMBL, UniProtKB, PubChem and RCSB PDB teams for the open data this work rests on.

## References

1. Lombana TN, Echols N, Good MC, et al. Allosteric activation mechanism of the Mycobacterium tuberculosis receptor protein kinase PknB. Structure. 2010;18(12):1667–1677. PMID: 21134645. doi:10.1016/j.str.2010.09.019.
2. Wehenkel A, Fernandez P, Bellinzoni M, et al. The structure of PknB in complex with mitoxantrone, an ATP-competitive inhibitor, suggests a mode of protein kinase regulation in mycobacteria. FEBS Lett. 2006;580(13):3018–3022. PMID: 16674948. doi:10.1016/j.febslet.2006.04.046.
3. Lougheed KEA, et al. Effective inhibitors of the essential kinase PknB and their potential as anti-mycobacterial agents. Tuberculosis (Edinb). 2011;91(4):277–286. PMID: 21482481. doi:10.1016/j.tube.2011.03.005.
4. Pollaniemi A, et al. Structural insights into multitargeting Mycobacterium tuberculosis Pkn kinases. Microbiol Spectr. 2026;14(8):e0004926. PMID: 42446239. doi:10.1128/spectrum.00049-26.
5. Saiki A, et al. In silico screening of PknB inhibitors against Mycobacterium tuberculosis: identification of Compound 5. SSRN. 2025. doi:10.2139/ssrn.5954835.
6. UniProtKB. Serine/threonine-protein kinase PknB, P9WI81. Accessed 2026-11-15. https://www.uniprot.org/uniprotkb/P9WI81/entry
7. RCSB Protein Data Bank. Structures 3ORK (PknB kinase domain L33D mutant, 1.60 A), 2FUM (PknB with mitoxantrone). Accessed 2026-11-15. https://www.rcsb.org/structure/3ORK
8. ChEMBL. Target CHEMBL1908385 (Serine/threonine-protein kinase PknB) — 57 bioactivities, 26 leads. Accessed 2026-11-15. https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1908385/
9. PubChem. Mitoxantrone, CID 4212; nintedanib, CID 135423438; sunitinib, CID 5329102. Accessed 2026-11-15. https://pubchem.ncbi.nlm.nih.gov/compound/4212
10. World Health Organization. Global Tuberculosis Report 2025. Geneva: WHO; 2025.

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-079-2026-11-15.json` (pipeline run: UniProt P9WI81, ChEMBL CHEMBL1908385, structure 3ORK). No correction was needed for this topic. PDB IDs 3ORK/2FUM and the ChEMBL target ID are given in the text. No additional data were generated.
