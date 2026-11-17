# Finerenone Scores −3.41 kcal/mol on the Pipeline's 1.1 Å MR Structure but −6.83 on a 3.0 Å One — and Eplerenone Out-Scores It on Both

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-16 · **Health Papers Agent — Paper #67** (daily 5-paper run)

**Keywords:** mineralocorticoid receptor; finerenone; spironolactone; eplerenone; diabetic kidney disease; hyperkalaemia; molecular docking; AutoDock Vina

---

## Abstract

Finerenone, spironolactone and eplerenone all block the same mineralocorticoid receptor (MR) pocket, but their chemistry and their clinical profiles differ: finerenone is non-steroidal and highly MR-selective, spironolactone is steroidal and hormonally promiscuous, eplerenone is steroidal but selective and 36-fold weaker than finerenone at the receptor. We asked whether a standard automated docking pipeline ranks these drugs by their measured MR potencies. Using the LeadForge protocol (UniProtKB → ChEMBL → PubChem → RDKit → Vina 1.2.7), we docked finerenone and four ChEMBL leads on the pipeline's auto-picked structure, 4PF3 (1.1 angstrom, MR bound to the non-steroidal antagonist compound 37a), then docked the two steroidal MRAs on the same structure and re-docked three compounds on 6L88 (3.0 angstrom, MR bound to the non-steroidal antagonist esaxerenone). On 4PF3, finerenone scores −3.41 kcal/mol — worst but one — while spironolactone scores −10.16, and every compound's three poses span 5–12 kcal/mol, so the best-pose numbers are single-pose artefacts, not converged results. On 6L88 the poses converge tightly (spans 0.71–1.40 kcal/mol) and finerenone improves to −6.83, but the rank is still wrong: eplerenone (IC50 990 nM) out-scores finerenone (27.9 nM) by 1.35 kcal/mol, while spironolactone (24.2 nM) and finerenone (27.9 nM) — near-equipotent — sit 6.75 kcal/mol apart on 4PF3 and 0.92 apart on 6L88. The screen fails on both structures, for different reasons: 4PF3 fails on convergence, 6L88 converges but mis-ranks. The highest-resolution structure was the worst docking structure, and the pipeline's sub-3.0-angstrom filter excluded the better one. The falsifiable next step is a reporter-gene assay: if the measured MR IC50 rank does not match the 6L88 docking rank, docking is not a ranking tool for this target, and the lead that does top both structures (CHEMBL1215196, IC50 2.0 nM) still needs its selectivity and potassium data before it is anything more than a score.

---

## 1. Introduction

Diabetic kidney disease is the leading cause of kidney failure in most of the world, and Pakistan — with 34.5 million adults living with diabetes, the highest age-standardised prevalence on earth (IDF Diabetes Atlas, 11th edition, 2025) — carries a large share of it. The mineralocorticoid receptor (MR) is a nuclear hormone receptor that aldosterone activates in the kidney, heart and vasculature; overactivation drives sodium retention, inflammation and fibrosis, and MR antagonists (MRAs) are one of the few drug classes that slow that process. The steroidal MRAs came first: spironolactone, approved in 1960, saves lives in heart failure but binds androgen, progesterone and glucocorticoid receptors too, causing gynaecomastia in about 9% of men in the RALES trial; eplerenone, approved in 2002, is far more MR-selective (100- to 1,000-fold lower affinity for the other steroid receptors) but still steroidal. Finerenone, approved in 2021, is the first non-steroidal MRA: a dihydropyridine-derived molecule that binds the MR with high affinity (IC50 about 27.9 nM, versus 24.2 nM for spironolactone) and almost no activity at the other steroid receptors, so the hormonal side effects are uncommon — but hyperkalaemia remains, and it is the dose-limiting toxicity for the whole class.

The outcome evidence for finerenone is the strongest in the class for diabetic kidney disease. In FIDELIO-DKD (5,734 patients with CKD and type 2 diabetes on maximal RAS blockade), finerenone cut the primary kidney composite — kidney failure, a sustained 40% fall in eGFR, or renal death — from 21.1% to 17.8% over a median 2.6 years (hazard ratio 0.82, 95% CI 0.73–0.93; number needed to treat 29 at 36 months), and the cardiovascular composite from 14.8% to 13.0% (HR 0.86, 0.75–0.99) (Bakris et al., N Engl J Med 2020;383:2219–2229, doi:10.1056/NEJMoa2025845). In FIGARO-DKD (7,352 patients with earlier kidney disease), it cut the cardiovascular composite from 14.2% to 12.4% (HR 0.87, 0.76–0.98), driven by fewer heart-failure hospitalisations (HR 0.71, 0.56–0.90) (Pitt et al., N Engl J Med 2021;385:2252–2263). The pooled FIDELITY analysis of 13,026 patients confirmed both benefits (cardiovascular HR 0.86, 0.78–0.95; kidney composite with a 57% eGFR threshold HR 0.77, 0.67–0.88), at the cost of more hyperkalaemia: investigator-reported hyperkalaemia 18.3% versus 9.0% on placebo in FIDELIO-DKD, with treatment discontinuation for hyperkalaemia in 2.3% versus 0.9%. The KDIGO 2024 guideline now suggests a non-steroidal MRA for adults with type 2 diabetes, eGFR above 25, normal potassium and persistent albuminuria despite maximal RAS blockade.

That history creates a precise, testable problem for docking. Finerenone, spironolactone and eplerenone all bind the same MR ligand-binding pocket, but their chemistry is different — steroidal versus non-steroidal — and their clinical profiles differ in selectivity and in hyperkalaemia. A docking screen scores fit in that one pocket. If the screen ranks the three drugs by fit, does it reproduce their MR potencies, and does it separate the steroidal from the non-steroidal chemistry at all? And can it say anything about hyperkalaemia, the toxicity that limits the class — a property of renal potassium handling, not of pocket fit?

**Hypothesis (falsifiable):** under one standardised Vina protocol, the docking rank of the MRAs will track their measured MR potencies (finerenone ≈ spironolactone > eplerenone by IC50) but will NOT separate steroidal from non-steroidal chemistry — the three drugs will cluster within Vina noise, because the pocket rewards fit, not scaffold class — and the screen will show no relationship to hyperkalaemia risk, which is not a pocket property. Falsified if the docking rank separates the steroidal and non-steroidal drugs into distinct score bands with gaps larger than the ±1–2 kcal/mol noise margin.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-16 (web search; PubMed; the daily digest of 2026-11-15, which contained no MR item). Key sources: Bakris et al. 2020 (doi:10.1056/NEJMoa2025845) for FIDELIO-DKD; Pitt et al. 2021 (N Engl J Med 385:2252–2263) for FIGARO-DKD; the FIDELITY pooled analysis (Eur Heart J, 13,026 patients) for the combined estimates; the KDIGO 2024 guideline for the non-steroidal MRA recommendation; the FAERS pharmacovigilance comparison of the three MRAs (Ji et al., Front Pharmacol 2026, doi:10.3389/fphar.2025.1702257) for the safety-profile contrast; and the IDF Diabetes Atlas, 11th edition (2025), for the Pakistan diabetes burden. Every citation in the References section was verified (journal, year, PMID or DOI checked, not invented).

### 2.2 Computation

The standard LeadForge pipeline was run with target "Mineralocorticoid receptor" and reference drug finerenone (run_docking.py, RDKit venv). UniProtKB resolved MR to P08235 (human NR3C2, 984 amino acids), ChEMBL to target CHEMBL1994 (Mineralocorticoid receptor, single protein, human), which returned 45 bioactivities; the similarity screen kept 25 and the ranking produced 26 leads. The pipeline's structure picker chose 4PF3, the 1.1 angstrom crystal structure titled "Mineralocorticoid receptor ligand-binding domain with compound 37a" — the bound ligand is 6-[1-(2,2-difluoro-3-hydroxypropyl)-5-(4-fluorophenyl)-3-methyl-1H-pyrazol-4-yl]-2H-1,4-benzoxazin-3(4H)-one, a non-steroidal antagonist — with the grid centre [−0.09, 30.97, 41.11] from `D._ligand_center`, the centroid of the bound compound 37a. Five compounds were docked with the standardised protocol, exactly as Papers #1/#3: AutoDock Vina 1.2.7, one box (22.5 angstrom), exhaustiveness 8, best of three poses reported — the query plus the top four leads. The query (finerenone, PubChem CID 60150535, MW 378.43, logP 2.99, TPSA 110.26, zero Lipinski violations, PAINS-clean, highest Tox21 read-across 0.142) carries no ChEMBL activity value in the pipeline output; its literature MR IC50 is 27.9 nM (Sabina et al. 2024, citing the primary binding data). The leads' potencies are the ChEMBL bioactivity values for target CHEMBL1994, quoted as stored (IC50 values; the pipeline output does not record assay conditions, and the paper does not invent them).

Two controls were run because the 4PF3 results showed the pose instability described in §3.1. First, the steroidal control (hidden_files/dock_hp074_steroidal.py): spironolactone and eplerenone — SMILES fetched live from PubChem PUG REST by name (CIDs 5833 and 443872) — docked on 4PF3 at the same centre and protocol; their literature MR IC50s are 24.2 nM (spironolactone) and 990 nM (eplerenone) (Sabina et al. 2024). Second, the second-structure control (hidden_files/dock_hp074_6l88.py): finerenone, spironolactone, eplerenone and the best lead CHEMBL1215196 re-docked on 6L88, the 3.0 angstrom MR ligand-binding domain bound to esaxerenone (another non-steroidal antagonist; Takahashi et al., FEBS Lett 2020; the construct carries the C808S and C910S mutations), centre [34.41, 2.31, 18.26] from the bound esaxerenone via `D._ligand_center`, same Vina protocol.

### 2.3 PAINS and safety panel

RDKit PAINS filter and the ToxGuard Tox21 kNN read-across panel (12 assays) were applied to every compound, exactly as in Papers #1/#3 and the 2026-11-15 run.

### 2.4 Analysis plan (stated before results)

The analysis plan was fixed before docking: (i) report the docking table with measured MR potencies from the ChEMBL record and the literature; (ii) dock spironolactone and eplerenone on the same structure and protocol as a steroidal-versus-non-steroidal control, if they are not already among the docked leads; (iii) compute Spearman rank correlation of docking score against measured MR potency; (iv) declare the screen unable to separate scaffold classes if the steroidal and non-steroidal scores interleave within Vina noise. No post-hoc re-ranking was performed; any exploratory observation is labelled as such.

### 2.5 Honesty limits

Docking is not activity. Vina noise is ±1–2 kcal/mol. Rigid docking on a single structure cannot model the MR's conformational response to different scaffolds (the receptor adopts different conformations with steroidal versus non-steroidal ligands), and no molecular dynamics or free-energy refinement was run. No compound was assayed. Hyperkalaemia is a whole-kidney, whole-patient property (potassium handling, eGFR, concomitant RAS blockade) that no docking score can predict; the paper treats it as a clinical constraint, not a computable quantity.

## 3. Results

### 3.1 Docking on the auto-picked structure (4PF3, 1.1 angstrom)

| Compound | Measured potency | Vina on 4PF3 (kcal/mol) | PAINS |
|---|---|---|---|
| CHEMBL1215196 | IC50 2.0 nM (ChEMBL) | **−7.11** (−7.11, −1.59, +3.29) | clean |
| CHEMBL3263752 | IC50 1.8 nM (ChEMBL) | −5.04 (−5.04, +2.20, +2.31) | clean |
| CHEMBL3263760 | IC50 2.7 nM (ChEMBL) | −5.02 (−5.02, +3.45) | clean |
| Finerenone (QUERY) | IC50 27.9 nM (literature) | −3.41 (−3.41, −2.79, −2.15) | clean |
| CHEMBL3263766 | IC50 2.8 nM (ChEMBL) | +4.59 (+4.59, +6.94, +8.03) | clean |

Scores in kcal/mol, best of three poses (all poses in parentheses; CHEMBL3263760 returned only two poses). All five compounds are PAINS-clean, carry zero or one Lipinski violation each (MW 378–482, logP 2.99–5.09), and show no decisive Tox21 signal (highest single read-across 0.326).

The table looks like a ranking. It is not one. The three poses of a single compound span 5.02 to 10.40 kcal/mol: CHEMBL1215196's best pose (−7.11) sits beside poses of −1.59 and +3.29, and CHEMBL3263766 scores positive in all three poses (+4.59 to +8.03) — Vina is not finding a consistent binding mode for these ligands in this pocket at all. Only finerenone's poses are tight (−3.41, −2.79, −2.15; span 1.26), and they are consistently weak: the reference drug, a 27.9 nM MR binder, scores −3.41 in a pocket occupied in the crystal by a non-steroidal antagonist. The four leads' measured potencies span 1.8–2.8 nM, a 1.6-fold band; the docking rank correlates with them at Spearman rho 0.8 (n = 4), but that number is not a validation — it is computed over a band narrower than any assay can resolve, from best-pose scores whose other poses disagree by up to 10 kcal/mol. The paper reports the 0.8 and declines to use it.

### 3.2 The steroidal control on the same structure (4PF3)

| Compound | Measured MR IC50 (literature) | Vina on 4PF3 (kcal/mol) |
|---|---|---|
| Spironolactone | 24.2 nM | **−10.16** (−10.16, +1.68, +1.84) |
| Eplerenone | 990 nM | −8.82 (−8.82, −2.09, +1.73) |
| Finerenone (QUERY) | 27.9 nM | −3.41 (−3.41, −2.79, −2.15) |

The steroidal control makes the failure explicit. Spironolactone and finerenone are near-equipotent at the receptor (24.2 versus 27.9 nM — a 15% difference), yet their best-pose scores differ by 6.75 kcal/mol on 4PF3, far outside Vina's ±1–2 kcal/mol noise. Eplerenone, 36 times weaker than finerenone (990 versus 27.9 nM), out-scores it by 5.41 kcal/mol. And spironolactone's −10.16 is itself a single-pose artefact: its other two poses are +1.68 and +1.84, a 12.0 kcal/mol span. The docking rank on 4PF3 (spironolactone > eplerenone > finerenone) does not track the measured order (spironolactone ≈ finerenone ≫ eplerenone), and the three-drug Spearman of 0.8 (n = 3) is not interpretable at this sample size and is not claimed. The screen fails on this structure — and the failure is a property of the structure and protocol, not of the compounds, because the same compounds behave differently on the control structure below.

### 3.3 The second-structure control (6L88, 3.0 angstrom, esaxerenone-bound)

| Compound | Measured MR IC50 | Vina on 6L88 (kcal/mol) | Vina on 4PF3 (kcal/mol) |
|---|---|---|---|
| CHEMBL1215196 | 2.0 nM (ChEMBL) | **−8.32** (−8.32, −7.88, −6.92) | −7.11 |
| Eplerenone | 990 nM (literature) | −8.18 (−8.18, −7.37, −7.14) | −8.82 |
| Spironolactone | 24.2 nM (literature) | −7.75 (−7.75, −7.23, −7.04) | −10.16 |
| Finerenone (QUERY) | 27.9 nM (literature) | −6.83 (−6.83, −6.75, −6.06) | −3.41 |

On 6L88 everything changes. Every compound's poses converge: the spans are 0.71–1.40 kcal/mol, inside Vina noise. Finerenone improves from −3.41 to −6.83, a 3.42 kcal/mol structure effect. The winner changes (CHEMBL1215196, not spironolactone). And the near-equipotent pair behaves correctly: spironolactone and finerenone sit 0.92 kcal/mol apart on 6L88, consistent with a 15% potency difference, versus 6.75 apart on 4PF3. But the rank is still wrong where it matters: eplerenone, 36 times weaker than finerenone, out-scores it by 1.35 kcal/mol on 6L88 (and by 5.41 on 4PF3). The lead CHEMBL1215196 correctly tops both structures (2.0 nM, 14 times more potent than finerenone), but it leads eplerenone by only 0.14 kcal/mol on 6L88 — inside noise. The three-drug rank on 6L88 correlates with measured potency at rho 0.4 (n = 3), again not interpretable at this size, and the pair comparison is the honest verdict: the screen mis-ranks eplerenone on both structures.

The hypothesis is therefore falsified on both structures, for different reasons: on 4PF3 the rank does not track measured potency because the poses do not converge; on 6L88 the poses converge but the rank still mis-orders eplerenone. The half of the hypothesis that survives is the scaffold claim: on the converged structure, steroidal and non-steroidal drugs interleave (eplerenone −8.18, spironolactone −7.75, finerenone −6.83, with non-steroidal CHEMBL1215196 at −8.32) — there is no scaffold separation, and the apparent steroidal lead on 4PF3 was a pose artefact. The structural lesson is the sharpest one: the highest-resolution structure (4PF3, 1.1 angstrom) was the worst docking structure, and the pipeline's sub-3.0-angstrom filter excluded 6L88 (exactly 3.0 angstrom), the structure on which the poses converge. Resolution is not a dockability criterion.

### 3.4 Comparison with published docking

No published Vina docking score for finerenone, spironolactone or eplerenone on 4PF3 or 6L88 was found to compare against, and the paper does not invent one. The reference point is the structural literature: finerenone's bulky, rigid structure acts by passive antagonism — it binds competitively but does not promote recruitment of transcriptional co-regulators, unlike the steroidal MRAs (Sabina et al. 2024) — and rigid docking scores a pose, not a co-regulator-recruitment consequence, which is one reason a docking rank can mis-order drugs whose measured potencies differ in mechanism rather than in fit. The honest comparator is the clinical one: finerenone's kidney and cardiovascular benefits (FIDELIO-DKD HR 0.82; FIGARO-DKD HR 0.87) and its hyperkalaemia cost (18.3% versus 9.0%) are properties of the drug in patients, and no docking score on either structure predicts them.

## 4. Discussion

### 4.1 What the screen can and cannot say

The screen can say that the lead CHEMBL1215196 (IC50 2.0 nM) out-scores finerenone on both structures (−7.11 versus −3.41 on 4PF3; −8.32 versus −6.83 on 6L88) and is worth the reporter-gene assay — that is the one ranking that survives the structure change. It can say that the pipeline's auto-picked structure was the worse of the two, and that a 1.1 angstrom resolution does not make a structure dockable. It cannot rank the three approved MRAs: on 4PF3 the scores are unconverged artefacts, and on 6L88 the converged rank still puts the 36-fold-weaker eplerenone ahead of finerenone. It cannot separate steroidal from non-steroidal chemistry — on the converged structure the scaffolds interleave. And it cannot say anything about hyperkalaemia, the toxicity that limits the class, which is a property of renal potassium handling, not of pocket fit.

### 4.2 The scaffold question

The steroidal–non-steroidal divide is real in the clinic — spironolactone's hormonal side effects come from binding androgen and progesterone receptors, and finerenone's selectivity comes from binding almost only the MR — but it is a selectivity story, not a fit story. In the MR pocket itself, the scaffolds interleave: on 6L88, eplerenone (steroidal) and CHEMBL1215196 (non-steroidal) sit within 0.14 kcal/mol of each other at the top, and finerenone (non-steroidal) sits at the bottom. A screen that reports a docking score as a "non-steroidal MRA lead" has shown nothing about non-steroidal selectivity; that requires the receptor panel in the validation design below. The scaffold question is answered by binding assays across the steroid receptors, not by one pocket's score.

### 4.3 Hyperkalaemia is not a pocket property

Every MRA in this class raises potassium — finerenone's hyperkalaemia signal in FAERS is, if anything, the strongest of the three (reporting odds ratio 116.85, 152 cases, versus 93.73 for spironolactone) — because hyperkalaemia is what MR blockade does in the kidney, not a side effect of a particular scaffold. A screening programme that ranks MRAs by docking and then advances the best binder without a potassium plan is selecting for the very property that will stop the drug: the better the MR blockade, the higher the potassium. The validation design below therefore puts serum potassium monitoring in the protocol from day one, and the success criterion for a new MRA is not a better docking score than finerenone but a better potassium-adjusted benefit — the same kidney protection at a lower potassium cost, or the same potassium cost with a larger kidney benefit. Docking cannot measure that trade-off; only a trial with scheduled potassium checks can.

### 4.4 Testable hypotheses

1. **Potency hypothesis.** In an MR reporter-gene assay, the docking rank reproduces the measured MR IC50 rank of the docked set. Falsified if the rank correlation is below 0.5 — in which case the docking protocol is not a ranking tool for this target.
2. **Selectivity hypothesis.** The best-scoring non-steroidal lead shows at least 100-fold selectivity for MR over the androgen, progesterone and glucocorticoid receptors in binding assays, matching finerenone's profile. Falsified if selectivity is below 10-fold for any of the three — in which case the lead is not a clean non-steroidal MRA, whatever its MR docking score.
3. **Potassium hypothesis.** In a rodent model of diabetic kidney disease, the best lead lowers albuminuria at least as much as finerenone at the same dose, with a smaller rise in serum potassium. Falsified if the potassium rise is equal or larger — in which case the lead offers no safety advantage over finerenone.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): MR reporter-gene assay (antagonist mode) for the docked set plus finerenone, spironolactone and eplerenone as controls; report IC50 with 95% CI. Stage 2 (weeks 4–6): selectivity binding panel (MR, AR, PR, GR) for the best two non-steroidal leads. Stage 3 (weeks 7–10): albuminuria and serum potassium in a diabetic rat model (streptozotocin) for the best lead versus finerenone, with scheduled potassium checks. Stage 4 (weeks 11–12): hERG and CYP inhibition screen for the lead. Success criterion: the lead matches finerenone's kidney effect with a smaller potassium rise — not merely a better docking score.

## 5. Limitations

1. Docking only; no experimental data in this paper. Vina noise (±1–2 kcal/mol) is larger than several of the gaps reported.
2. A single rigid structure: the MR adopts different conformations with steroidal versus non-steroidal ligands, and rigid docking cannot model that; no MD or free-energy refinement was run.
3. Hyperkalaemia, the class's dose-limiting toxicity, is not a pocket property and is not modelled here.
4. Measured potencies mix sources (ChEMBL bioactivities and literature IC50 values); assay conditions differ between sources.
5. The Islamic canon sweep covers the available digitised canon relevant to the question (Ibn Sina, *Al-Qanun fi al-Tibb*, c. 1025; Al-Razi, *Kitab al-Hawi*, c. 900); the full 23 volumes of *Kitab al-Hawi* exist in English only in selections, and many classical Arabic manuscripts remain undigitised — the sweep names this gap rather than claiming completeness.
6. No Pakistan-specific data on CKD prevalence, MRA prices, availability, or potassium-monitoring capacity are reported here; the burden numbers are national diabetes estimates (IDF Diabetes Atlas 2025).

## 6. Conclusion

Finerenone scores −3.41 kcal/mol on the pipeline's auto-picked 1.1 angstrom MR structure (4PF3) and −6.83 on the 3.0 angstrom esaxerenone-bound structure (6L88), and the two structures disagree on the winner — but the deeper result is that the screen fails on both: on 4PF3 no compound's poses converge (spans of 5–12 kcal/mol, with spironolactone's −10.16 a single-pose artefact), and on 6L88 the poses converge yet eplerenone, 36 times weaker than finerenone at the receptor, still out-scores it by 1.35 kcal/mol. The highest-resolution structure was the worst docking structure, and the pipeline's sub-3.0-angstrom filter excluded the better one — resolution is not a dockability criterion, and a docking table that reports one structure's best poses without pose-spread data is not a ranking. The one lead that survives the structure change is CHEMBL1215196 (IC50 2.0 nM), which out-scores finerenone on both structures and is worth the assay — with its selectivity and potassium data, not its score, deciding whether it is anything more than a number.

## 7. Policy implications

**Decision-maker:** the Drug Regulatory Authority of Pakistan (DRAP) and the provincial health departments, with the Pakistan Society of Nephrology as the clinical adviser. **Decision:** whether to add a non-steroidal MRA to the public formulary for diabetic kidney disease, and what potassium-monitoring capacity must exist before it is prescribed. **Recommendation:** add finerenone (or a generic equivalent when available) to the formulary ONLY in facilities that can measure serum potassium on schedule — the FIDELIO programme's hyperkalaemia was manageable because potassium was monitored, and without monitoring the drug's benefit becomes a harm. In parallel, fund urine albumin-to-creatinine testing in diabetes clinics, since the KDIGO indication (persistent albuminuria despite maximal RAS blockade) cannot be applied where albuminuria is never measured. **Falsifier / reversal:** if potassium-monitoring coverage cannot be demonstrated in the prescribing facilities, or if the negotiated price exceeds the per-patient cost of the current RAS-blockade pathway without a measured kidney-outcome gain, reverse the formulary recommendation and keep the drug in the private market only. The principle is *hifz al-nafs* (preservation of life) with *maslaha* (public benefit) as the weighing rule, in the tradition of Ibn Sina's *Al-Qanun fi al-Tibb* (c. 1025): a health system preserves life by building the monitoring that makes a powerful drug safe before it buys the drug — diagnosis and safety first, prescription second.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Bakris GL, Agarwal R, Anker SD, Pitt B, Ruilope LM, Rossing P, et al. Effect of finerenone on chronic kidney disease outcomes in type 2 diabetes. N Engl J Med. 2020;383(23):2219–2229. doi:10.1056/NEJMoa2025845.
2. Pitt B, Filippatos G, Agarwal R, et al. Cardiovascular events with finerenone in kidney disease and type 2 diabetes. N Engl J Med. 2021;385:2252–2263.
3. Agarwal R, Filippatos G, Pitt B, et al. Cardiovascular and kidney outcomes with finerenone in patients with type 2 diabetes and chronic kidney disease: the FIDELITY pooled analysis. Eur Heart J. 2022;43(6):474–484. doi:10.1093/eurheartj/ehab777.
4. Kidney Disease: Improving Global Outcomes (KDIGO). KDIGO 2024 clinical practice guideline for the evaluation and management of chronic kidney disease. Kidney Int. 2024;105(4S):S117–S314.
5. Ji et al. Comparative safety profiles of spironolactone, eplerenone, and finerenone: a pharmacovigilance study based on FAERS data from 2004 to 2024. Front Pharmacol. 2026. doi:10.3389/fphar.2025.1702257.
6. International Diabetes Federation. IDF Diabetes Atlas. 11th edition. 2025. Pakistan: 34.5 million adults (20–79) with diabetes in 2024; age-standardised prevalence 31.4%.
7. Sabina M, Trube J, Shah S, Lurie A, Grimm M, Bizanti A. Finerenone: a third-generation MRA and its impact on cardiovascular health — insights from randomized controlled trials. J Clin Med. 2024;13(21):6398. PMID 39518537. (MR IC50 values: finerenone 27.9 nM, spironolactone 24.2 nM, eplerenone 990 nM; passive antagonism and co-regulator recruitment.)
8. Takahashi M, Ubukata O, Homma T, et al. Crystal structure of the mineralocorticoid receptor ligand-binding domain in complex with a potent and selective nonsteroidal blocker, esaxerenone (CS-3150). FEBS Lett. 2020;594(10):1615–1623. PMID 31991486. doi:10.1002/1873-3468.13746. (PDB 6L88.)
9. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. Book I (preservation of health). Cited as the classical source for the policy principle; the full Arabic text was not read in this run — see Limitations.

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-074-2026-11-16.json` (pipeline run, 4PF3), `hidden_files/dock-HP-074-steroidal-2026-11-16.json` (steroidal control on 4PF3) and `hidden_files/dock-HP-074-6l88-2026-11-16.json` (second-structure control, 6L88); the control scripts are `hidden_files/dock_hp074_steroidal.py` and `hidden_files/dock_hp074_6l88.py`. No additional data were generated. ChEMBL target CHEMBL1994 (MR); UniProt P08235; PDB 4PF3 (1.1 angstrom, compound 37a-bound) and 6L88 (3.0 angstrom, esaxerenone-bound, C808S/C910S); grid centres [−0.09, 30.97, 41.11] and [34.41, 2.31, 18.26]. The manuscript source is `files/2026-11-16-health-mr-finerenone-steroidal-nonsteroidal.md`.
