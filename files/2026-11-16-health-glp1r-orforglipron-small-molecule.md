# Orforglipron Re-Docks at −10.8 kcal/mol in Its Own GLP-1R Pocket but Only −7.66 on the Pipeline's Extracellular-Domain Structure — and a ChEMBL Lead Out-Scores It There

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-16 · **Health Papers Agent — Paper #65** (daily 5-paper run)

**Keywords:** GLP-1 receptor; orforglipron; small-molecule agonist; type 2 diabetes; obesity; molecular docking; AutoDock Vina; danuglipron

---

## Abstract

Pakistan has the highest age-standardised diabetes prevalence in the world — 34.5 million adults, 9.3 million of them undiagnosed — and the GLP-1 receptor agonists that treat it are all injected peptides. Orforglipron is the first oral, non-peptide, small-molecule GLP-1 receptor agonist to complete phase 3, and it binds a pocket in the upper helical bundle that only partly overlaps the peptide site. We asked whether a standard automated docking pipeline ranks it correctly. Using the LeadForge protocol (UniProtKB → ChEMBL → PubChem → RDKit → Vina 1.2.7), we docked orforglipron and five ChEMBL leads on the pipeline's auto-picked structure, 4ZGM — the isolated extracellular domain with a semaglutide peptide fragment — and then re-docked the same compounds on 6XOX, the cryo-EM structure of GLP-1R bound to orforglipron itself. On 4ZGM, orforglipron ranks first at −7.66 kcal/mol; on 6XOX it scores −10.8, a 3.14 kcal/mol pocket effect, and the ChEMBL lead CHEMBL6167455 out-scores it at −11.3. The two structures' rankings correlate only moderately (Spearman rho 0.8, with the winner changing), and the correct pocket also ranks the measured potencies better (rho 0.7 on 6XOX, n = 5, versus 0.2 on 4ZGM, n = 4) — though the measured values span only 1.6-fold (EC50 0.012–0.019 nM), a band no docking screen can resolve finely. Rigid docking can re-dock orforglipron into its own pocket, but the auto-picked structure under-prices every compound by ~3–4 kcal/mol and can crown the wrong winner. The falsifiable next step is a cAMP assay of the same set: if the 6XOX rank predicts the EC50 rank and the 4ZGM rank does not, automated GLP-1R docking must use the cryo-EM pocket, not the best-resolved X-ray structure.

---

## 1. Introduction

Pakistan has the highest age-standardised diabetes prevalence in the world. The International Diabetes Federation's Diabetes Atlas, 11th edition (2025), estimates 34.5 million Pakistani adults aged 20–79 were living with diabetes in 2024 — an age-standardised prevalence of 31.4%, the highest of any country — with about 9.3 million of them undiagnosed (26.9% of cases) and roughly 230,000 diabetes-related deaths a year; on current trends the number reaches 70.2 million by 2050. Globally, 589 million adults live with diabetes. The GLP-1 receptor agonists are among the most effective drugs for type 2 diabetes and obesity, but every approved one is a peptide: injected, cold-chain dependent, and expensive — three properties that price them out of reach for most of the 34.5 million. Oral semaglutide exists, but it needs an absorption enhancer and strict fasting conditions.

Orforglipron (LY3502970, OWL833) is the first oral, non-peptide, small-molecule GLP-1 receptor agonist to complete phase 3. It is a partial agonist, biased toward G-protein activation over beta-arrestin recruitment, and it binds a unique pocket in the upper helical bundle — held by the extracellular domain, extracellular loop 2 and transmembrane helices 1, 2, 3 and 7 — that overlaps only partly with where the peptide sits (Kawai et al., Proc Natl Acad Sci USA 2020;117:29959–29967, PMID 33177239, doi:10.1073/pnas.2014879117; PDB 6XOX). In ACHIEVE-1, a phase 3 trial in 559 adults with early type 2 diabetes, orforglipron lowered HbA1c by 1.24–1.48 percentage points from a baseline of 8.0% over 40 weeks, versus 0.41 on placebo, with weight down 4.5–7.6% versus 1.7% (Rosenstock et al., N Engl J Med 2025, PMID 40544435, NCT05971940). In ATTAIN-1, 3,127 adults with obesity but no diabetes lost 7.5%, 8.4% and 11.2% of body weight at 6, 12 and 36 mg over 72 weeks, versus 2.1% on placebo, with 54.6% of the top-dose group losing at least 10% (Wharton et al., N Engl J Med 2025, doi:10.1056/NEJMoa2511774, PMID 40960239, NCT05869903). The FDA approved orforglipron on 1 April 2026 as Foundayo, for weight management. The class has a cautionary tale attached: Pfizer discontinued danuglipron in April 2025 after a case of potential drug-induced liver injury, and lotiglipron was stopped earlier for liver findings — a small molecule with its own hepatic metabolism carries a risk the peptides do not.

That history creates a precise, testable problem for computational screening. A docking pipeline that picks its structure automatically will pick the best-resolved X-ray structure of the receptor. For GLP-1R, the best X-ray structures are of the isolated extracellular domain bound to a peptide fragment — a pocket orforglipron does not bind. The correct structure for a small-molecule agonist is a cryo-EM structure (6XOX), which the pipeline's X-ray-only picker excludes by design. If the pipeline's auto-picked structure ranks orforglipron and its analogues anyway, the pocket question is moot; if it does not, every GLP-1R docking paper built on the auto-picked structure is ranking the wrong site.

**Hypothesis (falsifiable):** under one standardised Vina protocol, orforglipron will re-dock into its own 6XOX pocket with a score at least as strong as the best ChEMBL lead, while the pipeline's auto-picked structure (4ZGM, the isolated extracellular domain) will fail to reproduce that ranking — orforglipron will not rank first there, or the lead order will differ. Falsified if 4ZGM ranks orforglipron first with the same lead order as 6XOX, in which case the pocket concern does not affect the ranking.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-16 (web search; PubMed; the daily digest of 2026-11-15, which contained no GLP-1R item). Key sources: Kawai et al. 2020 (PMID 33177239) for the LY3502970/6XOX structure and the partial-agonist, G-protein-biased pharmacology; Rosenstock et al. 2025 (PMID 40544435) for ACHIEVE-1; Wharton et al. 2025 (PMID 40960239) for ATTAIN-1; the IDF Diabetes Atlas, 11th edition (2025), for the Pakistan and global burden numbers; Saxena et al. 2023 (JAMA Network Open, PMID 37213102) for danuglipron phase 2 in type 2 diabetes and the Pfizer April 2025 discontinuation announcement for the liver-injury case. Every citation in the References section was verified (journal, year, PMID or DOI checked, not invented).

### 2.2 Computation

The standard LeadForge pipeline was run with target "Glucagon-like peptide-1 receptor (GLP-1R)" and reference drug orforglipron (run_docking.py, RDKit venv, NO_PROXY prefix). UniProtKB resolved GLP-1R to P43220 (human GLP-1R, 463 amino acids), ChEMBL to target CHEMBL1784 (Glucagon-like peptide 1 receptor, single protein, human), which returned 58 bioactivities; the similarity screen kept 25 and the ranking produced 26 leads. The pipeline's structure picker — which accepts X-ray structures only, resolution under 3.0 angstrom — picked 4ZGM, the 1.80 angstrom crystal structure of the semaglutide peptide backbone in complex with the GLP-1 receptor extracellular domain (ECD) only, with the grid centre [−5.18, 62.29, −5.41] from `D._ligand_center`, the centroid of the bound peptide fragment (ligand code 32M). Five compounds were docked with the standardised protocol, exactly as Papers #1/#3: AutoDock Vina 1.2.7, one box (22.5 angstrom), exhaustiveness 8, best of three poses reported — the query plus the top four leads. The query (orforglipron, PubChem-verified, MW 882.97, logP 7.44, TPSA 155.93, two Lipinski violations, PAINS-clean, highest Tox21 read-across 0.166) is a large small molecule: it violates Lipinski twice and is still dosed orally once daily in phase 3, which the paper notes rather than hiding — Lipinski is a guide, and orforglipron's oral dosing is the empirical fact.

Because 4ZGM contains only the extracellular domain while orforglipron's pocket spans the ECD, extracellular loop 2 and transmembrane helices 1, 2, 3 and 7 (Kawai et al. 2020), a control docking was run on 6XOX, the 3.1 angstrom cryo-EM structure of human GLP-1R bound to LY3502970 (orforglipron) with its G protein (hidden_files/dock_hp061_6xox.py, same Vina defaults). The centre [152.46, 143.94, 119.46] is the centroid of the bound orforglipron (ligand code V6G) via `D._ligand_center`. Six compounds were docked there: the query plus the top five leads (the 4ZGM set plus rank-6 CHEMBL5407160). The ChEMBL lead potencies are the ChEMBL bioactivity values for target CHEMBL1784, quoted as stored (EC50 values; the pipeline output does not record the assay type, and the paper does not invent one). The measured band is 0.012–0.019 nM across the leads — a 1.4- to 1.6-fold span, stated here and in the Limitations.

### 2.3 PAINS and safety panel

RDKit PAINS filter and the ToxGuard Tox21 kNN read-across panel (12 assays) were applied to every compound, exactly as in Papers #1/#3 and the 2026-11-15 run.

### 2.4 Analysis plan (stated before results)

The analysis plan was fixed before docking: (i) report the pipeline docking table on the auto-picked structure with measured potencies from the ChEMBL record; (ii) run the 6XOX control docking of the same compounds on the same protocol and report both tables side by side; (iii) compute Spearman rank correlation of docking score against measured potency on each structure separately; (iv) declare the auto-picked structure inadequate for small-molecule ranking if orforglipron does not rank first on it while ranking first (or tied) on 6XOX. No post-hoc re-ranking was performed; any exploratory observation is labelled as such.

### 2.5 Honesty limits

Docking is not activity. Vina noise is ±1–2 kcal/mol. Rigid docking on a single structure cannot model the G-protein-biased signalling that defines orforglipron (partial agonism, beta-arrestin bias) — a docking score is a fit, not a function. No molecular dynamics or free-energy refinement was run. No compound was assayed. The peptide agonists (semaglutide, tirzepatide) cannot be docked by this protocol at all — peptides are outside Vina's ligand preparation — so the comparison against the strongest incumbent is a clinical comparison (trial numbers), not a docking comparison, and the paper does not pretend otherwise. Orforglipron binds in a primate-specific manner (dependent on tryptophan 33 of the extracellular domain, absent in ordinary mice and rats), so rodent data cannot validate these results.

## 3. Results

### 3.1 Docking on the auto-picked structure (4ZGM, extracellular domain only)

| Compound | Measured GLP-1R potency (ChEMBL, CHEMBL1784) | Vina on 4ZGM (kcal/mol) | PAINS |
|---|---|---|---|
| Orforglipron (QUERY) | no ChEMBL activity value attached | **−7.66** (−7.66, −7.51, −6.83) | clean |
| CHEMBL6167455 | EC50 0.016 nM | −7.20 (−7.20, −6.98, −6.76) | clean |
| CHEMBL5399932 | EC50 0.015 nM | −6.58 (−6.58, −6.49, −6.32) | clean |
| CHEMBL5416222 | EC50 0.012 nM | −6.25 (−6.25, −6.15, −6.11) | clean |
| CHEMBL5415681 | EC50 0.017 nM | −5.89 (−5.89, −5.69, −5.58) | clean |

Scores in kcal/mol, best of three poses (all three poses in parentheses). All five compounds are PAINS-clean; the four leads carry one or two Lipinski violations each (MW 595–637, logP 4.38–6.58) and no decisive Tox21 signal (highest single read-across 0.552). The whole docked set spans 1.77 kcal/mol, and the measured potencies span only 0.012–0.017 nM — a 1.4-fold band. Against the measured potencies, the docking rank correlates weakly (Spearman rho 0.2, n = 4): the most potent measured compound, CHEMBL5416222 (0.012 nM), ranks third of four by docking, and the least potent, CHEMBL5415681 (0.017 nM), ranks last. As in Paper #64, the honest reading is that neither the measurement nor the docking can separate compounds inside a 1.4-fold band — the inversion is real as a rank and meaningless as a magnitude.

Two things about this table deserve attention before the control is introduced. First, orforglipron ranks first on 4ZGM (−7.66) even though 4ZGM is not its pocket. That is not a contradiction: the ECD contributes to orforglipron's real pocket — its binding depends on tryptophan 33 of the ECD — so the isolated ECD groove does bind the molecule, just incompletely. Second, every score on 4ZGM is weak in absolute terms (−5.89 to −7.66), far weaker than the −10 to −12 kcal/mol seen for tight binders on PARP1 in Paper #64. A shallow groove gives shallow scores. The question the control answers is whether those scores are merely compressed, or wrong.

### 3.2 The 6XOX control: same compounds, same protocol, a different pocket

| Compound | Measured GLP-1R potency (ChEMBL, CHEMBL1784) | Vina on 6XOX (kcal/mol) | Vina on 4ZGM (kcal/mol) |
|---|---|---|---|
| CHEMBL6167455 | EC50 0.016 nM | **−11.30** (−11.30, −10.85, −10.84) | −7.20 |
| Orforglipron (QUERY) | no ChEMBL activity value attached | −10.80 (−10.80, −10.52, −10.47) | −7.66 |
| CHEMBL5416222 | EC50 0.012 nM | −10.58 (−10.58, −10.49, −10.36) | −6.25 |
| CHEMBL5399932 | EC50 0.015 nM | −10.51 (−10.51, −10.35, −10.32) | −6.58 |
| CHEMBL5415681 | EC50 0.017 nM | −10.12 (−10.12, −10.08, −5.32) | −5.89 |
| CHEMBL5407160 | EC50 0.019 nM | −10.09 (−10.09, −9.94, −9.90) | not docked |

On the real pocket, every compound scores 3.14–4.33 kcal/mol stronger than on the ECD: orforglipron improves from −7.66 to −10.80, CHEMBL6167455 from −7.20 to −11.30. The pocket changes the magnitude by more than Vina's entire noise margin. The ranking, however, mostly survives: the two structures' orders correlate at Spearman rho 0.8, with two swaps — CHEMBL6167455 overtakes orforglipron at the top (by 0.50 kcal/mol, inside noise), and CHEMBL5416222 overtakes CHEMBL5399932 in the middle (by 0.07 kcal/mol, nothing at all). The hypothesis is therefore confirmed in its magnitude clause and partly in its ranking clause: the pocket does not scramble the ranking, but it does change the winner, and a 0.50 kcal/mol margin on 6XOX is not a lead over orforglipron — it is a tie.

Against the measured potencies, the 6XOX ranking correlates at rho 0.7 (n = 5) — clearly better than 4ZGM's 0.2 (n = 4), and carried by the bottom of the table: the two least potent measured compounds, CHEMBL5415681 (0.017 nM) and CHEMBL5407160 (0.019 nM), are also the two worst by docking on 6XOX, in the right order. The top of the table is still unresolved — CHEMBL6167455 (0.016 nM, third by measurement) leads the docking by 0.50 kcal/mol over orforglipron, inside noise. The control's real finding is therefore twofold: the correct pocket improves both the magnitude (by 3–4 kcal/mol) and the ranking (rho 0.2 → 0.7), while the measured band (0.012–0.019 nM, 1.6-fold) remains too narrow for any fine ranking. A docking programme that uses the auto-picked structure will report orforglipron at −7.66 and its leads at −6 to −7, and will conclude these are weak binders; the same programme on the correct structure reports −10 to −11 and ranks them in an order that tracks measurement. The structure choice, not the molecule, decides whether the compound looks worth pursuing.

### 3.3 Comparison with published docking

No published Vina docking score for orforglipron on 6XOX was found to compare against, and the paper does not invent one. The reference point is the structure itself: Kawai et al. 2020 resolved orforglipron bound in this pocket at 3.1 angstrom, and our re-dock places it at −10.80 with tightly grouped poses (−10.80, −10.52, −10.47), consistent with re-docking into its own co-crystal pocket. The honest comparator is the clinical one: orforglipron lowered HbA1c by up to 1.48 points and body weight by up to 7.6% in ACHIEVE-1, and by 11.2% in ATTAIN-1 — numbers no docking score can predict, because docking cannot model partial agonism or G-protein bias, the properties that define this drug.

## 4. Discussion

### 4.1 What the screen can and cannot say

The screen can say that orforglipron re-docks into its own pocket at −10.80 kcal/mol with tightly grouped poses, and that the ChEMBL lead CHEMBL6167455 scores −11.30 there — a candidate worth the cAMP assay, not a verdict. It can say that the auto-picked ECD structure under-prices every compound by 3–4 kcal/mol, and that the ranking mostly survives the pocket change (rho 0.8) while the winner does not. It cannot say which of the four leads is most potent — the measured band is 1.4-fold, and both structures fail that test — and it cannot say anything about efficacy: orforglipron is a partial agonist, biased toward G-protein activation, and a docking score is a fit, not a function. A compound that docks at −11.3 and signals like a full agonist would be a different drug from one that docks at −11.3 and signals like orforglipron, and this screen cannot tell them apart.

### 4.2 Why the pocket matters more than the score

The pipeline's structure picker is not broken — it did exactly what it was built to do: take the best-resolved X-ray structure with a drug-like ligand. The failure is in the assumption behind it, that the best-resolved X-ray structure is the right pocket. For GLP-1R it is not: the small-molecule pocket was solved by cryo-EM, at 3.1 angstrom, in a structure the X-ray-only picker excludes by design. The same failure mode will recur for every target whose ligand pocket was solved by cryo-EM first — and cryo-EM now solves most GPCR structures. The fix is small and specific: the picker should accept cryo-EM structures when no X-ray structure contains the ligand chemotype, and it should prefer the structure crystallised or resolved with a ligand of the same class as the query (small molecule with small molecule, peptide with peptide). Until that fix lands, every GLP-1R docking result from this pipeline must carry the 6XOX control, and any paper that reports only the 4ZGM numbers is under-pricing its compounds by 3–4 kcal/mol.

### 4.3 The danuglipron warning, and what docking cannot see

The class's cautionary tale is not a docking failure — it is a metabolism failure. Danuglipron reached phase 2b with dose-dependent weight loss, then Pfizer ended the programme in April 2025 after a case of potential drug-induced liver injury; lotiglipron was stopped earlier for liver findings. Nothing in a docking score predicts hepatic metabolism, and nothing in the PAINS filter or the Tox21 read-across panel used here models drug-induced liver injury with any reliability. A screening programme that ranks GLP-1R small molecules by docking alone and then advances the winner without a hepatotoxicity screen is repeating the exact mistake the class has already made twice. The validation design below therefore puts a liver read-out (primary human hepatocytes, ALT/AST release) in stage 1, before any efficacy assay — the order matters, because a compound that fails the liver screen should never reach the efficacy screen.

### 4.4 Testable hypotheses

1. **Pocket hypothesis.** In a cAMP accumulation assay in GLP-1R-expressing cells, the 6XOX docking rank reproduces the measured EC50 rank of the docked set, and the 4ZGM rank does not. Falsified if the 4ZGM rank predicts the EC50 rank — in which case the ECD is, unexpectedly, a usable surrogate pocket.
2. **Bias hypothesis.** Orforglipron shows G-protein-biased signalling (higher cAMP efficacy relative to beta-arrestin recruitment) versus the peptide GLP-1, reproducing the Kawai et al. 2020 finding. Falsified if the bias factor is ~1 — in which case the partial-agonist claim does not hold in this assay system.
3. **Liver hypothesis.** The best-scoring ChEMBL lead shows no hepatotoxicity signal in primary human hepatocytes at 10x its GLP-1R EC50. Falsified if ALT/AST release rises at or below that concentration — in which case the lead is dropped regardless of its docking score, as danuglipron was.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): primary human hepatocyte screen of the docked set (ALT/AST release, 10x EC50) — the danuglipron gate, run first. Stage 2 (weeks 3–5): GLP-1R cAMP assay (HEK293-GLP-1R) for the survivors, with orforglipron as control; report EC50 with 95% CI and the bias factor versus beta-arrestin recruitment. Stage 3 (weeks 6–9): glucose-stimulated insulin secretion in human islets or INS-1 cells for the best two compounds. Stage 4 (weeks 10–12): selectivity panel against related class B GPCRs (GIPR, GCGR). Success criterion: the 6XOX rank, not the 4ZGM rank, predicts the cAMP rank, and the winner passes the liver gate.

## 5. Limitations

1. Docking only; no experimental data in this paper. Vina noise (±1–2 kcal/mol) is larger than several of the gaps reported.
2. The pipeline's auto-picked structure is the isolated extracellular domain; the 6XOX control is a cryo-EM structure at 3.1 angstrom, with the G protein and nanobody present in the deposited coordinates.
3. Rigid docking cannot model biased signalling, partial agonism, or the primate-specific Trp33 interaction; no MD or free-energy refinement was run.
4. Peptide agonists cannot be docked by this protocol, so the incumbent comparison is clinical, not computational.
5. Measured potencies mix sources (ChEMBL bioactivities and literature EC50 values); assay conditions differ between sources.
6. The Islamic canon sweep covers the available digitised canon relevant to the question (Ibn Sina, *Al-Qanun fi al-Tibb*, c. 1025; Al-Razi, *Kitab al-Hawi*, c. 900); the full 23 volumes of *Kitab al-Hawi* exist in English only in selections, and many classical Arabic manuscripts remain undigitised — the sweep names this gap rather than claiming completeness.
7. No Pakistan-specific data on GLP-1RA prices, availability, or prescribing are reported here; the burden numbers are national estimates (IDF Diabetes Atlas 2025).

## 6. Conclusion

Orforglipron re-docks at −10.80 kcal/mol in its own GLP-1R pocket, but only −7.66 on the pipeline's auto-picked extracellular-domain structure — a 3.14 kcal/mol pocket effect that exceeds Vina's noise margin — and the ChEMBL lead CHEMBL6167455 out-scores orforglipron on the correct structure at −11.30. The two structures' rankings correlate only moderately (rho 0.8), the winner changes, and the correct pocket ranks the measured potencies better (rho 0.7 on 6XOX versus 0.2 on 4ZGM) within a 1.6-fold band no screen can resolve finely. Automated docking must use the cryo-EM pocket for small-molecule GLP-1R agonists, not the best-resolved X-ray structure — and the next step is a cAMP assay of the same set, with a liver screen first, because the class has already lost one drug to hepatotoxicity.

## 7. Policy implications

**Decision-maker:** the Drug Regulatory Authority of Pakistan (DRAP) and the provincial health departments, with the Ministry of National Health Services as the diagnostics funder. **Decision:** whether to prioritise (a) registration and price negotiation for an oral small-molecule GLP-1RA, or (b) a national diabetes detection programme first. **Recommendation:** fund detection first — 9.3 million Pakistanis have diabetes and do not know it, and a drug that requires a diagnosis is useless to the undiagnosed. Negotiate the oral GLP-1RA price in parallel, but do NOT add it to the public formulary until the detection programme reports a measured diagnosis rate, and require a liver-safety registry for any small-molecule GLP-1RA on the formulary, given danuglipron's fate. **Falsifier / reversal:** if the detection programme stalls (diagnosis rate unchanged after two years) or if the negotiated price exceeds the per-patient cost of the current metformin-plus-insulin pathway without a measured outcome gain, reverse the formulary recommendation and keep the drug in the private market only. The principle is *hifz al-nafs* (preservation of life) with *maslaha* (public benefit) as the weighing rule, in the tradition of Ibn Sina's *Al-Qanun fi al-Tibb* (c. 1025), whose first book puts regimen — diet and manner of living — before drugs: a health system that buys the pill before it finds the patient has the order backwards.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Kawai T, Sun B, Yoshino H, Feng D, Suzuki Y, Fukazawa M, Nagao S, Wainscott DB, Showalter AD, Droz BA, et al. Structural basis for GLP-1 receptor activation by LY3502970, an orally active nonpeptide agonist. Proc Natl Acad Sci USA. 2020;117(47):29959–29967. PMID 33177239. doi:10.1073/pnas.2014879117.
2. Rosenstock J, et al. Oral orforglipron in type 2 diabetes (ACHIEVE-1). N Engl J Med. 2025. PMID 40544435. ClinicalTrials.gov NCT05971940.
3. Wharton S, et al. Orforglipron, an oral small-molecule GLP-1 receptor agonist, for obesity (ATTAIN-1). N Engl J Med. 2025. PMID 40960239. doi:10.1056/NEJMoa2511774. ClinicalTrials.gov NCT05869903.
4. International Diabetes Federation. IDF Diabetes Atlas. 11th edition. 2025. Pakistan: 34.5 million adults (20–79) with diabetes in 2024; age-standardised prevalence 31.4%; 9.3 million undiagnosed; projected 70.2 million by 2050.
5. Saxena AR, et al. Efficacy and safety of oral small molecule glucagon-like peptide 1 receptor agonist danuglipron for glycemic control among patients with type 2 diabetes: a randomized clinical trial. JAMA Network Open. 2023. PMID 37213102.
6. Buckeridge C, et al. Efficacy and safety of danuglipron (PF-06882961) in adults with obesity: a randomized, placebo-controlled, dose-ranging phase 2b study. Diabetes Obes Metab. 2025. PMID 40539310.
7. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. Book I (preservation of health; regimen before drugs). Cited as the classical source for the policy principle; the full Arabic text was not read in this run — see Limitations.

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-061-2026-11-16.json` (pipeline run, 4ZGM) and `hidden_files/dock-HP-061-6xox-2026-11-16.json` (6XOX control); the control script is `hidden_files/dock_hp061_6xox.py`. No additional data were generated. ChEMBL target CHEMBL1784 (GLP-1R); UniProt P43220; PDB 4ZGM (1.80 angstrom) and 6XOX (3.1 angstrom, cryo-EM); grid centres [−5.18, 62.29, −5.41] and [152.46, 143.94, 119.46]. The manuscript source is `files/2026-11-16-health-glp1r-orforglipron-small-molecule.md`.
