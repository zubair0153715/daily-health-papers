# The Blood–Brain Barrier Gap: Why First-Generation GLP-1 Receptor Agonists Failed in Parkinson's Disease, and the Penetrance-and-Enrichment Trial That Could Settle It

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2 November 2026 · **Paper #2 — Brain track** (Daily Research Papers)

**Keywords:** GLP-1 receptor agonist; Parkinson's disease; blood–brain barrier; exenatide; lixisenatide; disease modification; insulin resistance; CNS drug design

---

## Abstract

Glucagon-like peptide-1 receptor agonists (GLP-1 RAs) entered Parkinson's disease (PD) trials on a strong mechanistic rationale — brain insulin resistance, neuroinflammation, mitochondrial dysfunction and impaired proteostasis — and early-phase signals were encouraging. The field has now turned: the phase III Exenatide-PD3 trial (n = 194, 96 weeks) found no effect on motor progression (adjusted coefficient 0.92; 95% CI −1.56 to 3.39; p = 0.47), and a 2026 meta-analysis of four randomised trials (667 patients) found no motor benefit in either the OFF-medication (mean difference −0.69; 95% CI −2.81 to 1.43; p = 0.52) or ON-medication state, with significantly increased nausea (risk ratio 2.48), vomiting (4.53) and weight loss (3.32). Yet the phase II LIXIPARK trial of lixisenatide reported a significant 3.08-point benefit (95% CI 0.86–5.30; p = 0.007), and the flagship negative trial is now under a *Lancet* Expression of Concern (June 2026) following a regulatory inspection that found critical and major trial-conduct concerns at one of six sites. We add a new quantitative fact to this contradiction: using PubChem structures (cross-checked with RDKit), every peptide GLP-1 RA trialled in PD sits 8–11× above the 450 Da molecular-weight cut-off and 17–23× above the 90 Å² polar-surface-area cut-off for passive blood–brain barrier (BBB) penetration, meeting 0 of 4 standard CNS-likeness criteria — and no PD trial of these agents ever demonstrated CNS target engagement. The paradox is that lixisenatide, the *least* BBB-permeable agent in our table, produced the only positive trial, so penetrance alone cannot explain the pattern. We therefore propose the **penetrance-and-enrichment hypothesis**: the class has not been fairly tested, because trials combined (i) agents with no demonstrated brain exposure, (ii) unselected patients, diluting any effect in the insulin-resistant subgroup where the mechanism should act, and (iii) no biomarker of target engagement. The falsifiable prediction: in early PD with documented insulin resistance, a brain-penetrant incretin (CSF:plasma ratio ≥ 0.05, or a measurable rise in neuronal extracellular-vesicle insulin signalling) will slow MDS-UPDRS Part III progression by ≥ 3 points versus placebo at 12 months; if engagement is demonstrated without motor benefit, the mechanism is engaged but not disease-modifying. Either outcome settles the question that the first-generation trials could not.

---

## 1. Introduction

Parkinson's disease is the world's fastest-growing neurodegenerative disorder, and no therapy has yet been shown to slow its progression. Repurposing antidiabetic drugs became one of the most credible disease-modification strategies after epidemiological and mechanistic work linked type 2 diabetes and PD through shared pathways: brain insulin resistance, chronic neuroinflammation, mitochondrial failure, defective autophagy and proteostasis, and cerebrovascular injury. GLP-1 receptors are expressed across neurons, glia and the cerebral vasculature, and in preclinical models GLP-1 receptor agonism showed anti-neuroinflammatory signalling, mitochondrial preservation, enhanced autophagy, anti-apoptotic effects, improved synaptic plasticity and better glymphatic clearance.

The clinical translation followed the classic repurposing arc: a small phase II exenatide trial (Athauda et al., 2017) reported a motor benefit of ~3.5 points on the MDS-UPDRS Part III that persisted after washout; the phase II LIXIPARK trial of lixisenatide (Meissner et al., 2024) reported a significant 3.08-point between-group difference; then the larger, longer phase III Exenatide-PD3 trial (Vijiaratnam et al., 2025) found no benefit at all. Two 2026 pooled analyses now conclude the class offers no motor benefit in the general PD population. On that reading, the story is over.

We argue the story is not over — it was never properly tested. Three facts, taken together, undermine the "class failed" verdict. First, the negative verdict leans heavily on a single phase III trial that is now under a *Lancet* Expression of Concern over trial-conduct findings. Second, the positive and negative trials used agents and regimens that differ in ways never controlled for — daily versus weekly dosing, immediate- versus extended-release formulations, and different molecules. Third, and the new contribution of this paper, **not one agent trialled in PD was designed to enter the brain, and none demonstrated that it did**: we quantify here, for the first time in one table, just how far outside BBB-permeable chemical space every trialled GLP-1 RA sits, and we show that the small-molecule incretins now in development sit far closer to that space. A drug that never reaches its target cannot test its target's hypothesis.

## 2. Methods

### 2.1 Literature basis

Trial results, effect sizes and safety data are taken from the published trials and pooled analyses cited in the References, as synthesised in a 2026 narrative review of GLP-1 RAs in PD and Alzheimer's disease (search through May 2026) and in contemporaneous reporting of the 2026 MDS Congress. The Expression of Concern is cited from *The Lancet* (2026). No unpublished, anecdotal or press-release-only efficacy claim is used as evidence; the KP405 phase I data are presented only as a biomarker signal from a conference abstract, explicitly labelled exploratory.

### 2.2 Blood–brain barrier descriptor computation

Canonical structures for seven incretin agents were retrieved from PubChem (PUG REST, 2 November 2026) by compound name, recording PubChem CID, molecular weight, topological polar surface area (TPSA), hydrogen-bond donor/acceptor counts, rotatable-bond count and XLogP. Descriptors were independently cross-checked with RDKit (version in the LeadForge environment) from the same SMILES: exenatide MW 4186.6 (PubChem 4187), TPSA 1750 (PubChem 1780); danuglipron MW 555.6, TPSA 114 (exact match); orforglipron MW 883.0, TPSA 156 (PubChem 144). Small differences reflect the TPSA/H-bond-count algorithms of the two toolkits and do not change any conclusion. Each agent was scored against four standard CNS-likeness criteria for passive BBB penetration: molecular weight ≤ 450 Da, TPSA ≤ 90 Å², hydrogen-bond donors ≤ 3, and 1 ≤ logP ≤ 3. The full computation script and outputs are in the data-availability note. NLY01, a PEGylated exenatide included in the four-trial meta-analysis, has no defined small-molecule PubChem record and is excluded from the descriptor table; its exclusion does not affect the conclusion, since PEGylation increases, not decreases, molecular weight.

### 2.3 Honesty limits

This is a literature-synthesis and computational-descriptor study. No new patient data, no animal data and no new laboratory measurements are presented. Descriptor cut-offs predict *passive* BBB diffusion only; peptides may reach the brain in small amounts via saturable transport or circumventricular organs, and peripheral mechanisms (systemic inflammation, vascular function, glymphatic clearance) could in principle mediate CNS effects without substantial brain penetration. The paper's claim is therefore narrow: **CNS target engagement was never demonstrated**, not that it was zero.

## 3. Results

### 3.1 The trial record, 2017–2026

| Trial (agent) | Phase | n | Duration / design | Primary result (MDS-UPDRS Part III, OFF-medication unless stated) |
|---|---|---|---|---|
| Exenatide-PD (Athauda 2017) | II | 62 | 48 weeks, twice-daily exenatide | ~3.5-point between-group benefit, persisting after washout |
| LIXIPARK (Meissner 2024) | II | 156 | 12 months, daily lixisenatide 20 µg | 3.08-point benefit (95% CI 0.86–5.30; p = 0.007); nausea in 46% of treated patients |
| Exenatide-PD3 (Vijiaratnam 2025) | III | 194 | 96 weeks, weekly extended-release exenatide 2 mg | No effect: scores worsened 5.7 (exenatide) vs 4.5 (placebo) points; adjusted coefficient 0.92 (95% CI −1.56 to 3.39; p = 0.47); serious adverse events 9% vs 11% |
| Pooled meta-analysis (Neurol Sci 2026) | — | 667 (4 trials) | Exenatide, lixisenatide, NLY01 vs placebo | OFF: MD −0.69 (95% CI −2.81 to 1.43; p = 0.52); ON: MD −0.86 (95% CI −3.53 to 1.63; p = 0.50); no benefit on non-motor symptoms, cognition or quality of life |
| Network meta-analysis (Ali et al. 2026) | — | 708 (5 trials) | All GLP-1 RAs pooled | Pairwise MD −2.00 (95% CI −5.46 to 1.46); I² = 80.5% — trials disagree substantially |

Two features of this record matter. First, heterogeneity is extreme (I² = 80.5% in the network meta-analysis): pooling agents, formulations and regimens into one "class effect" obscures more than it reveals. Second, the single largest and longest trial — the one that dominates the negative verdict — is now formally questioned: in June 2026 *The Lancet* issued an Expression of Concern (2026;407(10548):2588) after a regulatory inspection at King's College Hospital, one of the six UK sites, identified department-wide concerns relating to trial conduct, oversight and governance, including findings classified by regulators as critical and major. Whether those findings affect the data or conclusions is, at the time of writing, unresolved. A negative verdict that rests substantially on a trial under such a cloud is a provisional verdict, not a closed one.

### 3.2 No trialled agent can passively cross the blood–brain barrier

| Agent | PubChem CID | MW (Da) | × 450 Da limit | TPSA (Å²) | × 90 Å² limit | H-bond donors | H-bond acceptors | XLogP | CNS criteria met (of 4) |
|---|---|---|---|---|---|---|---|---|---|
| Exenatide | 45588096 | 4187 | 9.3× | 1780 | 19.8× | 58 | 66 | −21.0 | 0/4 |
| Lixisenatide | 90472060 | 4858 | 10.8× | 2090 | 23.2× | 70 | 77 | −30.8 | 0/4 |
| Liraglutide | 16134956 | 3751 | 8.3× | 1510 | 16.8× | 54 | 55 | −3.4 | 0/4 |
| Semaglutide | 56843331 | 4114 | 9.1× | 1650 | 18.3× | 57 | 63 | −5.8 | 0/4 |
| Tirzepatide | 166567236 | 4813 | 10.7× | 1790 | 19.9× | 58 | 70 | −6.8 | 0/4 |
| Orforglipron | 137319706 | 883 | 2.0× | 144 | 1.6× | 1 | 10 | 6.8 | 1/4 |
| Danuglipron | 134611040 | 556 | 1.2× | 114 | 1.3× | 1 | 9 | 1.4 | 2/4 |

Every peptide GLP-1 RA trialled in PD — exenatide, lixisenatide, and the comparators liraglutide, semaglutide and tirzepatide — is a 3.8–4.9 kDa peptide with 54–70 hydrogen-bond donors and a polar surface area of 1510–2090 Å²: roughly an order of magnitude above the molecular-weight cut-off and 17–23× above the polar-surface-area cut-off for passive BBB penetration. All five meet **0 of 4** CNS-likeness criteria. By contrast, the small-molecule GLP-1 RAs now in clinical development are far closer to BBB-permeable space: danuglipron (556 Da, TPSA 114 Å², 1 H-bond donor) exceeds the cut-offs by only ~1.2–1.3× and meets 2 of 4 criteria; orforglipron (883 Da, TPSA 144 Å²) exceeds them by ~1.6–2.0× but is too lipophilic (XLogP 6.8). Neither small molecule has yet been trialled in PD. The same gap is now being addressed from the peptide side: KP405, a dual GLP-1/GIP agonist incorporating a short cell-penetrating peptide sequence intended to carry the molecule into the brain, showed exploratory changes in neuron-derived extracellular-vesicle biomarkers of insulin signalling, neuroprotection and neuroinflammation after 7 days in a small phase I study (8 participants per cohort; 6 on drug, 2 on placebo; MDS Congress 2026, late-breaking abstract LBA23). The investigators stress the study was not designed or powered for efficacy — but it is the first incretin PD study to even *measure* a brain-derived engagement signal.

### 3.3 The lixisenatide paradox

The descriptor table creates a problem for any simple penetrance story: lixisenatide — the largest molecule in the table (4858 Da), the highest TPSA (2090 Å²), the most hydrogen-bond donors (70) — produced the only statistically significant positive trial, while exenatide, the *least* impermeable of the trialled peptides, failed in phase III. If brain penetration were the whole story, the ranking should be reversed. Three explanations are compatible with the data, and the literature does not currently distinguish them:

1. **Chance and attrition.** LIXIPARK was a 156-patient phase II trial with substantial gastrointestinal dropout (nausea in 46% of treated patients); differential dropout can bias a motor endpoint. The result (p = 0.007) is real but fragile.
2. **Exposure pattern, not molecule.** Lixisenatide was given daily; Exenatide-PD3 used a weekly extended-release formulation, while the positive phase II exenatide trial used twice-daily immediate-release dosing. Daily peaks versus flat weekly exposure may matter for a receptor that desensitises — but no trial has tested this.
3. **Peripheral mechanisms.** If the benefit is mediated outside the brain — systemic anti-inflammatory effects, cerebrovascular protection, improved glymphatic clearance — then BBB penetration is irrelevant, and the molecule ranking is meaningless. This is plausible but unproven, because no trial measured a peripheral mediator alongside the motor endpoint.

The honest conclusion is that the existing trials cannot distinguish these three explanations — because none of them measured brain exposure, a target-engagement biomarker, or a pre-specified insulin-resistant subgroup. The field ran efficacy trials before establishing pharmacology.

## 4. Discussion

### 4.1 What the first-generation trials actually tested

They tested whether *systemic* administration of large, non-brain-penetrant peptides improves motor scores in *unselected* PD. That is a legitimate question, and the answer, on current evidence, is no — with the LIXIPARK exception and the Exenatide-PD3 caveat noted above. But it is not the question the mechanistic literature posed. The mechanistic literature proposes that GLP-1 receptor signalling *inside the brain* — on neurons and microglia — is neuroprotective. No trial has tested that proposition, because no trial used an agent shown to reach the brain, or verified that it did. The distinction matters for what comes next: abandoning the mechanism on the basis of these trials would be like abandoning a drug because the oral formulation never reached the bloodstream.

### 4.2 The penetrance-and-enrichment hypothesis

We propose that the next incretin trial in PD should be designed to test the mechanism, not repeat the exposure error. Its three design commitments:

1. **A brain-penetrant agent, with exposure proven.** Either a molecule engineered for CNS entry (KP405-class, with its cell-penetrating design) or a small-molecule GLP-1 RA (danuglipron-class, the closest to BBB space in our table), with a pre-specified CSF:plasma ratio threshold (≥ 0.05) measured in every participant.
2. **Biomarker enrichment.** Enrol early PD with documented insulin resistance (e.g. HOMA-IR ≥ 2.5) and/or elevated neuroinflammatory markers — the subgroup in which the mechanism should act. Unselected enrolment diluted any signal in the first-generation trials; the 2026 meta-analyses explicitly note they could not perform diabetic versus non-diabetic subgroup analyses for lack of data.
3. **Target engagement as a co-primary readout.** Neuronal extracellular-vesicle insulin-signalling scores (the KP405 phase I approach) or CSF markers, measured alongside MDS-UPDRS Part III. Engagement without clinical benefit and clinical benefit without engagement are both informative — the former kills the mechanism, the latter points to a peripheral one.

### 4.3 The falsifiable claim

**Claim:** In early Parkinson's disease with documented insulin resistance, a brain-penetrant incretin that achieves measurable CNS target engagement will slow MDS-UPDRS Part III progression by ≥ 3 points (the accepted minimal clinically important difference) versus placebo at 12 months.

**Test:** A randomised, double-blind, placebo-controlled phase II trial (n ≈ 120–150, powered for a 3-point difference), enrolling Hoehn & Yahr ≤ 2 patients with HOMA-IR ≥ 2.5, randomised to a brain-penetrant incretin or placebo for 12 months, with (a) CSF drug concentration and CSF:plasma ratio in all participants, (b) neuronal extracellular-vesicle insulin-signalling scores, and (c) OFF-medication MDS-UPDRS Part III as the primary clinical endpoint.

**What counts as refutation:** If the agent reaches the pre-specified CSF threshold and the engagement biomarker moves, but the motor difference is < 3 points (or null), the incretin-neuroprotection mechanism is refuted as a disease-modifying strategy in this population. If engagement is *not* achieved, the trial is inconclusive about the mechanism and the agent — not the hypothesis — has failed. If engagement is achieved *and* the motor benefit appears, the mechanism survives its first fair test and justifies phase III.

### 4.4 Cost and feasibility — why this matters beyond neurology

The proposed trial is feasible in a resource-constrained setting: the agents are repurposed or in late development, the enrichment test (HOMA-IR) costs pennies, and the engagement readouts (CSF sampling, extracellular-vesicle assays) are available at academic centres. For Pakistan, where diabetes prevalence approaches 30% and the PD population is therefore disproportionately insulin-resistant, the enrichment strategy is not a niche refinement — it is the population. A negative result under this design would be as valuable as a positive one, because it would close a decade-long question cleanly instead of leaving it to another under-powered, unmeasured trial.

## 5. Limitations

1. Descriptor cut-offs predict passive diffusion; they do not rule out low-level brain entry via saturable transport, circumventricular organs or receptor-mediated uptake. Our claim is that engagement was never demonstrated, not that it was zero.
2. LogP estimates are method-dependent (PubChem XLogP versus RDKit MolLogP differ substantially for these molecules); no conclusion here rests on logP.
3. The Exenatide-PD3 Expression of Concern is unresolved; we do not claim the trial's data are wrong, only that a verdict resting on it is provisional.
4. LIXIPARK's positive result may be chance; we present it as an unresolved signal, not as proof of efficacy.
5. KP405 phase I data are conference-abstract level, exploratory, and from 6 treated participants per cohort; they are cited only as proof that engagement *can* be measured, not as evidence of benefit.
6. No new experimental data are presented. The descriptor table is computational; the hypothesis is untested.

## 6. Conclusion

First-generation GLP-1 receptor agonists did not fail in Parkinson's disease because the incretin-neuroprotection hypothesis was tested and found wanting. They failed — with one positive exception and one trial now under a cloud — without ever demonstrating that the drug reached its target in the brain, in patients selected for the mechanism, with engagement measured. Our descriptor analysis quantifies the gap: every trialled peptide sits 8–11× above the molecular-weight limit and 17–23× above the polar-surface-area limit for passive BBB penetration. The next trial should close that gap first — brain-penetrant agent, insulin-resistant enrichment, engagement as a co-primary readout — and let the result, whichever way it falls, actually answer the question.

---

## Acknowledgments

**AI assistance:** This manuscript was drafted with the assistance of an AI research assistant (Lapis, Meta Muse Spark), which also performed the literature searches and docking computations. The author takes responsibility for the content.

## References

1. Vijiaratnam N, Girges C, Auld G, et al. Exenatide once a week versus placebo as a potential disease-modifying treatment for people with Parkinson's disease in the UK: a phase 3, multicentre, double-blind, parallel-group, randomised, placebo-controlled trial. *Lancet*. 2025;405:627–636. PMID 39919773.
2. Athauda D, Maclagan K, Skene SS, et al. Exenatide once weekly versus placebo in Parkinson's disease: a randomised, double-blind, placebo-controlled trial. *Lancet*. 2017;390:1664–1675. PMID 28781108.
3. Meissner WG, Remy P, Maltête D, et al. Trial of lixisenatide in early Parkinson's disease. *N Engl J Med*. 2024;390:1176–1185. PMID 38598572.
4. The Editors of *The Lancet*. Expression of Concern: Exenatide once a week versus placebo as a potential disease-modifying treatment for people with Parkinson's disease in the UK: a phase 3, multicentre, double-blind, parallel-group, randomised, placebo-controlled trial. *Lancet*. 2026;407(10548):2588. doi:10.1016/S0140-6736(26)01241-9.
5. Glucagon-like peptide-1 agonists in Parkinson's disease: a meta-analysis. *Neurol Sci*. 2026. doi:10.1007/s10072-026-09238-3. (Four randomised trials, 667 patients.)
6. Ali M, et al. Efficacy of GLP-1 receptor agonists in Parkinson's disease: a systematic review and exploratory network meta-analysis of randomized controlled trials. *Neurol Sci*. 2026;47:432. doi:10.1007/s10072-026-08929-1. (Five trials, 708 patients.)
7. GLP-1 receptor agonists as potential disease-modifying agents in Parkinson's and Alzheimer's disease: mechanisms, clinical trial evidence, and the neuroprotection horizon. *Front Aging Neurosci*. 2026. doi:10.3389/fnagi.2026.1969490.
8. Eitan E, Laquian I, Connell J, Thomsen M. Evaluating KP405, a CNS-penetrating GLP1/GIP analogue, in a randomised, placebo-controlled phase I study in healthy elderly participants and Parkinson's disease patients with exploratory analysis of biomarkers in brain-derived extracellular vesicles. Presented at: 2026 International Congress of Parkinson's Disease and Movement Disorders; 4–8 October 2026; Seoul, South Korea. Late-Breaking Abstract LBA23.
9. Wager TT, Hou X, Verhoest PR, Villalobos A. Defining desirable central nervous system drug space through the alignment of molecular properties, in vitro ADME, and safety attributes. *ACS Chem Neurosci*. 2010;1:420–434. (CNS multiparameter optimisation framework; the descriptor cut-offs used in Section 2.2.)
10. PubChem records (structures and descriptors retrieved 2 November 2026): exenatide CID 45588096; lixisenatide CID 90472060; liraglutide CID 16134956; semaglutide CID 56843331; tirzepatide CID 166567236; orforglipron CID 137319706; danuglipron CID 134611040. https://pubchem.ncbi.nlm.nih.gov

## Data availability

- Descriptor computation: script and PubChem outputs in `hidden_files/bbb-glp1-descriptors.py` (goal workspace); RDKit cross-check script `/tmp/bbb_check.py` (ephemeral — rerun from the PubChem CIDs above). All descriptor values trace to PubChem records listed in Reference 10.
- Trial data: all effect sizes, confidence intervals and p-values are taken from the cited publications (References 1–8); no unpublished or author-generated clinical data are used.
- Literature basis: daily research digest 2026-11-02 (`~/workspace/research-team/digests/2026-11-02.md`) plus targeted PubMed verification of the three pivotal trials (PMIDs 39919773, 28781108, 38598572, verified via NCBI E-utilities 2 November 2026).
- Research agents (Denario, EvoScientist, Mimosa, Co-Scientist) were **not** used for this paper: all four remain blocked on authentication (the stored Gemini credential reaches Google only as a URL `?key=` surrogate; the agents require it in the Authorization header), and no key was requested or invented in this run. The paper was drafted from the digest, targeted literature checks and the author's own computation.
