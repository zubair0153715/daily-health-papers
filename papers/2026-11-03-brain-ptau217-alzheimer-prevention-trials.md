# The Preclinical Window Is Now Measurable: Plasma p-Tau217 Risk Stratification and the Design of Alzheimer's Prevention Trials

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan · ORCID 0009-0001-5921-7509
**Drafting assistant:** Lapis (AI)
**Date:** 3 November 2026 · **Paper #4 — Brain track** (Daily Research Papers)

**Keywords:** plasma p-tau217; Alzheimer's disease; preclinical Alzheimer's disease; cognitive impairment; risk stratification; prevention trial; trial enrichment; tau; diranersen

---

## Abstract

Alzheimer's disease prevention trials have been designed in the dark: they enrol cognitively unimpaired people with brain amyloid and then wait years to learn how many would ever have declined. A pooled analysis of 2,684 cognitively unimpaired older adults across six cohorts (Buckley et al., *JAMA* 2026) now attaches absolute numbers to that wait. Over five years, the risk of progression to cognitive impairment was 12% with low plasma phosphorylated tau 217 (p-tau217), 15% intermediate, 24% high and 38% very high (>2.5 SD above the amyloid-negative reference); at ten years the very-high group reached 78%. Each 1-SD rise in p-tau217 carried a hazard ratio of 1.38, and the association survived adjustment for amyloid PET burden. We translate these risks into trial arithmetic: for a five-year prevention trial powered to detect a 30% relative risk reduction, an unselected population needs 1,412 participants, a high-p-tau217 population 982, and a very-high-p-tau217 population only 526 — a 63% reduction in sample size, with the five-year number needed to treat falling from 18.7 to 8.8. The same numbers expose the limits of enrichment: two-year risks are 1–4% in every stratum, so a two-year prevention trial is futile by design; even the "low" group carries a 12% five-year and 40% ten-year risk; and the cohorts were selected, not population-representative. We propose the **enrichment-and-horizon hypothesis**: prevention trials should enrol the very-high p-tau217 stratum and run at least five years, testing a tau-lowering intervention of the diranersen class. The falsifiable prediction: the placebo arm will progress at 33–43% over five years and the trial will detect a 30% risk reduction with ≤650 participants; a placebo rate below 25% refutes the enrichment assumption. Until a prevention drug exists, these numbers are a trial-design tool, not a screening test — current guidelines explicitly recommend against testing asymptomatic people outside research.

---

## 1. Introduction

Alzheimer's disease (AD) begins a decade or more before symptoms. Amyloid plaques accumulate silently, tau pathology follows, and by the time memory fails, the brain has already lost substantial ground. Every disease-modifying drug approved so far — lecanemab and donanemab — is given to people who already have symptoms, and each slows decline by roughly a quarter to a third rather than stopping it. The field's open question is whether intervening earlier, before symptoms, can do better. The AHEAD 3-45 trial is testing exactly that with lecanemab in amyloid-positive but cognitively unimpaired adults over 216 weeks. But prevention trials face a structural problem: most cognitively unimpaired people with amyloid will not decline within the trial's window, so the trial must be large, long and expensive — or it must find the people most likely to decline soon.

Until 2026, the field could only guess at that likelihood. Plasma phosphorylated tau 217 (p-tau217) was known to reflect early AD brain pathology and to predict *relative* risk of progression, but no pooled estimate of *absolute* risk — the number a trial designer actually needs — existed across multiple cohorts. The first FDA-cleared blood test in this space (Lumipulse G pTau217/β-Amyloid 1-42 Plasma Ratio, cleared 16 May 2025) is indicated only for symptomatic adults, and guidelines recommend against testing asymptomatic people outside research. So the prognostic question and the clinical question are different, and this paper is about the first: what does a p-tau217 level mean for a cognitively unimpaired person's chance of declining, and what does that mean for the trials that must enrol them?

The answer arrived in September 2026. Buckley and colleagues pooled harmonised data from 2,684 cognitively unimpaired older adults in six cohorts (ADNI, A4/LEARN, Harvard Aging Brain Study, Health & Aging Brain Study–Health Disparities, and the Wisconsin Registry for Alzheimer's Prevention), followed for a median of 5.4 years, and reported model-based absolute risks of progression to cognitive impairment at 2, 5 and 10 years by p-tau217 stratum. The headline numbers — 38% five-year risk in the very-high group, 78% at ten years — were widely reported in November 2026. What has not been done, and what this paper does, is convert those risks into the concrete currency of trial design: sample sizes, numbers needed to treat, and the minimum trial duration that can possibly work. That conversion is our new contribution. It is arithmetic, not new data — but it changes the decision a trial designer faces from "enrich or not?" to "by how much, and at what cost?"

## 2. Methods

### 2.1 Literature basis

All prognostic numbers are taken from Buckley et al., *JAMA* 2026;336(11):950–959 (PMID 42449500; PMCID PMC13370474), read in full text, including Table 2 (absolute risks by stratum and time horizon) and the longitudinal PACC analysis. Context on prevention-trial screening comes from Molina-Henry et al., *JAMA Neurology* 2026, reporting the AHEAD 3-45 screening cohort (15,612 cognitively unimpaired adults at 106 sites). The tau-lowering intervention used as the worked example is diranersen, from the phase 2 CELIA data presented at the Alzheimer's Association International Conference, July 2026 (Ionis/Biogen press release, 14 July 2026; corroborated by contemporaneous Reuters and NeurologyLive reporting). Regulatory context is the FDA clearance of the Lumipulse p-tau217 test (16 May 2025). No unpublished, anecdotal or press-release-only efficacy claim is used as evidence; the CELIA efficacy figures are presented as conference-reported phase 2 results, explicitly labelled as such, and the paper's own claim does not depend on them.

### 2.2 Trial-arithmetic computation

Sample sizes use the standard two-proportion formula for a two-arm trial with a binary endpoint (progression to cognitive impairment within five years), two-sided α = 0.05, power = 80%:

n per arm = [Z₁₋α/₂·√(2p̄(1−p̄)) + Z₁₋β·√(p₁(1−p₁) + p₂(1−p₂))]² / (p₁ − p₂)²

where p₁ is the placebo-arm five-year event rate, p₂ = p₁ × (1 − RRR) is the treated-arm rate at the assumed relative risk reduction (RRR), and p̄ = (p₁ + p₂)/2. Placebo rates are the Buckley model-based five-year risks (low 12%, intermediate 15%, high 24%, very high 38%), plus an "unselected" reference taken as the observed overall proportion who progressed, 478/2,684 = 17.8%, over the median 5.4 years of follow-up — an approximate five-year rate, flagged as such wherever it is used. Number needed to treat over five years (NNT₅y) = 1/(p₁ − p₂). Sensitivity analyses use RRR = 25% and the 95% confidence bounds of the very-high stratum (33–43%). The full computation script is in the data-availability note; every number in the tables below is its direct output.

### 2.3 Honesty limits

This is a literature-synthesis and arithmetic study. No new patient data, no new laboratory measurements and no new trial are presented. The sample sizes are planning calculations, not trial results: they assume the published risks transport to a future trial population, that the treatment effect is a constant relative risk reduction, and that loss to follow-up is negligible. The Buckley risks are model-based standardised estimates from selected research cohorts, not raw counts, and the 10-year figures rest on sparse data. The paper's claim is therefore narrow: **enrichment by very-high p-tau217 makes a five-year prevention trial feasible at roughly one-third the size** — not that such a trial will succeed, and not that asymptomatic people should be tested in clinic.

## 3. Results

### 3.1 The prognostic numbers: risk is graded, not binary

| p-Tau217 group (definition) | ~Amyloid PET (Centiloid) | 2-year risk | 5-year risk (95% CI) | 10-year risk (95% CI) |
|---|---|---|---|---|
| Low (<−0.5 SD) | <10 | 1% (1–1) | 12% (9–15) | 40% (31–49) |
| Intermediate (−0.5 to <1.1 SD) | 10–24 | 1% (1–1) | 15% (12–17) | 45% (37–52) |
| High (1.1 to <2.5 SD) | 25–60 | 2% (1–3) | 24% (20–28) | 62% (52–69) |
| Very high (≥2.5 SD) | >60 | 4% (3–5) | 38% (33–43) | 78% (69–84) |

Table 1. Model-based absolute risk of progression to cognitive impairment, from Buckley et al. (JAMA 2026), Table 2. All figures are standardised risks from a Cox model adjusted for cohort, age, sex, APOE ε4 status and education. The 10-year estimates rest on sparse data — only 5% of participants were followed beyond 10 years, mostly in one cohort — and must be treated as indicative, not precise.

Three features of this table matter. First, the gradient is steep and monotonic: the very-high group carries 3.17× the five-year risk of the low group (38% vs 12%), and the hazard ratio for very-high versus low is 4.66 (95% CI 3.17–6.85); high versus low is 2.34 (1.60–3.44). Each 1-SD increase in p-tau217 carries a hazard ratio of 1.38 (1.30–1.46), and the association survives adjustment for amyloid PET Centiloids (HR 1.32; 1.24–1.41), while amyloid burden itself contributes less (per-SD HR 1.19; 1.05–1.34). The biomarker adds information beyond the scan. Second, the two-year risks are 1–4% in *every* stratum: nobody declines fast enough, in any group, for a two-year prevention trial to accumulate endpoints. Third, even the "low" group is not a no-risk group — 12% at five years, 40% at ten. These are selected research cohorts (many participants carry a family history or APOE ε4), so the absolute numbers almost certainly overstate risk in the general population; the gradient, not the level, is the transportable finding.

The cognitive-trajectory data tell the same story in continuous form. Over five years, the low group *improved* by 0.03 latent PACC units per year (practice effects), the intermediate group by 0.01, while the high group declined by 0.03 and the very-high group by 0.07 units per year. The very-high-versus-low gap is −0.10 units per year (95% CI −0.13 to −0.07), or −0.50 units over five years. People who progressed declined at −0.06 units per year on average. The model discriminates reasonably well (five-year AUC 0.80; 95% CI 0.77–0.83) with good calibration (Brier score 0.12). Risk also varies within the very-high stratum: five-year risk is 36% in women versus 43% in men, and 39% at age 65 rising to 47% at age 85.

### 3.2 The trial arithmetic: enrichment buys a threefold reduction in size

| Enrolment population (5-year placebo rate) | n per arm | Total N | NNT over 5 years |
|---|---|---|---|
| Unselected (observed 17.8%) | 706 | 1,412 | 18.7 |
| Low p-tau217 (12%) | 1,109 | 2,218 | 27.8 |
| Intermediate p-tau217 (15%) | 862 | 1,724 | 22.2 |
| High p-tau217 (24%) | 491 | 982 | 13.9 |
| Very high p-tau217 (38%) | 263 | 526 | 8.8 |

Table 2. Sample sizes for a five-year prevention trial with a binary progression endpoint, 30% relative risk reduction, two-sided α = 0.05, 80% power. Computed from the risks in Table 1 (script in the data-availability note). "Unselected" uses the observed overall progression proportion (478/2,684 over median 5.4 years) as an approximate five-year rate.

Enrolling only the very-high stratum cuts the required trial from 1,412 participants to 526 — **63% fewer participants** — and more than halves the number needed to treat (8.8 vs 18.7). The saving is robust to the assumed effect size: at a 25% relative risk reduction, the unselected trial needs 2,082 participants versus 770 enriched; and across the very-high stratum's 95% confidence interval, the enriched total ranges from 436 (at 43% risk) to 646 (at 33% risk) — still less than half the unselected size in the worst case. Per 1,000 people enrolled for five years, the very-high stratum yields 380 progression events against 178 unselected, 240 high and 120 low: the endpoint, which is what a prevention trial is starved of, more than doubles.

Two corollaries follow. First, the low stratum is a bad trial population on its own (2,218 participants for the same power), so a trial that enrols "amyloid-positive" people without further stratification is paying for its lowest-risk participants. Second, the arithmetic only works at a five-year horizon. At two years, with event rates of 1–4%, the same calculation returns sample sizes in the tens of thousands — which is why prevention trials are four-to-five-year commitments, and why the AHEAD 3-45 trial runs 216 weeks.

### 3.3 What the biomarker does not buy

Enrichment is not free, and the numbers quantify its costs too. First, the screening yield is unknown from the published sources used here: the Buckley paper reports risks by stratum but the group sizes appear only in its figure, which we did not extract, so the number of people who must be blood-tested to find one very-high candidate cannot be computed from the text. The AHEAD screening experience gives a sense of scale — 15,612 people screened across 106 sites to fill a trial — but that used %p-tau217 as a first pass for amyloid, not the ≥2.5 SD threshold. Any sponsor budgeting an enriched trial must obtain the stratum prevalences before the arithmetic in Table 2 can be turned into a screening budget.

Second, enrichment narrows the answer. A trial in the very-high stratum tests the drug where pathology is most advanced; a positive result there does not prove benefit in the high or intermediate strata, where most of the preclinical population sits and where a prevention drug would ultimately be used. The high stratum — 24% five-year risk, 62% at ten years — is arguably the more important population for a prevention claim, and it needs 982 participants, still 30% fewer than unselected.

Third, a blood test that can find the highest-risk people does not create a treatment for them. No drug is approved for cognitively unimpaired people, the FDA-cleared p-tau217 tests are indicated only for symptomatic adults, and current guidelines explicitly recommend against testing asymptomatic people outside research. The value of these numbers today is for trial design, not for clinic screening — a distinction the paper's own authors stress.

## 4. Discussion

### 4.1 From relative risk to absolute risk: why this paper changes the conversation

For years, p-tau217 was a *relative* risk marker: "higher is worse, hazard ratio 1.38 per SD." Relative risks cannot size a trial. The Buckley analysis converts the marker into absolute, time-specific risks — the form a trialist, a funder and a regulator can actually use. That conversion is the paper's real contribution to the field, and ours is the second step: turning absolute risks into sample sizes. The result reframes the prevention-trial debate. The question is no longer "can we afford a prevention trial?" — at 526 participants over five years, a very-high-stratum trial is smaller than many phase 2 symptomatic trials — but "can we afford *not* to enrich, and can we screen fast enough to fill it?"

### 4.2 The enrichment-and-horizon hypothesis

We propose that the next Alzheimer's prevention trial should be designed around two commitments:

1. **Enrol the very-high p-tau217 stratum** (≥2.5 SD, roughly >60 Centiloids of amyloid), with the high stratum (1.1–2.5 SD) as a pre-specified second cohort, so that both the highest-risk and the broader preclinical populations are tested in one protocol.
2. **Run at least five years with progression to cognitive impairment as the primary endpoint**, with the latent PACC slope as a co-primary continuous readout — the very-high group declines at −0.07 units per year against +0.03 in the low group, so a treatment that returns the slope toward zero is measurable within the trial's window.

The intervention to test first is a tau-lowering drug of the diranersen class. The July 2026 CELIA phase 2 data give the rationale: in 416 people with early symptomatic AD, the antisense oligonucleotide diranersen (60 mg intrathecally every six months) lowered CSF total tau by 50–65% across all doses, reduced tau PET signal in every brain region examined, and slowed decline by 26% on CDR-SB (0.54 points), 42% on ADAS-Cog13 and 50% on MMSE at 18 months — roughly the magnitude of the approved anti-amyloid antibodies — with no ARIA events. The trial missed its primary dose-response endpoint (higher doses did not do better), so the efficacy signal is provisional and Biogen's confirmatory phase 3, starting in 2027 with data expected 2030–2031, is the proper test in symptomatic disease. But the *mechanistic* case for testing tau-lowering before symptoms is now the strongest it has ever been: tau burden, not amyloid burden, tracks cognition, and p-tau217 is the blood read-out of that burden. A prevention trial that enriches on p-tau217 and intervenes on tau is the first trial in which the enrichment marker, the drug target and the outcome measure all point at the same biology.

### 4.3 The falsifiable claim

**Claim:** A five-year, randomised, placebo-controlled prevention trial enrolling cognitively unimpaired adults with very-high plasma p-tau217 (≥2.5 SD) and testing a tau-lowering intervention will (a) observe a placebo-arm progression rate of 33–43% (point estimate 38%), and (b) detect a 30% relative risk reduction with ≤650 total participants at 80% power.

**Test:** Enrol ~526 participants (263 per arm) with very-high p-tau217, randomise to a tau-lowering intervention or placebo for five years, with progression to cognitive impairment (MCI, dementia, or two consecutive global CDR scores ≥0.5 — the Buckley endpoint) as primary, and latent PACC slope as co-primary.

**What counts as refutation:** If the placebo-arm five-year progression rate falls below 25%, the enrichment assumption is refuted — the Buckley risks do not transport to a trial population, and the sample-size arithmetic in Table 2 is void. If the placebo rate is within 33–43% but the treated arm shows no risk reduction despite demonstrated tau lowering (CSF total tau down ≥50%, as in CELIA), the tau-lowering prevention hypothesis is refuted in this population. If the placebo rate holds *and* the risk reduction appears, the enrichment strategy is validated and justifies a phase 3 in the broader high stratum.

### 4.4 The ethics of knowing: patients-in-waiting

A test that can put a number on a healthy person's future creates a new kind of patient. A very-high p-tau217 result in a cognitively unimpaired person means a 38% chance of impairment within five years and 78% within ten — and no approved treatment to offer them. A JAMA Viewpoint in October 2026 warned that such results can turn healthy adults into "patients-in-waiting" with few legal protections, and the study authors themselves advise against clinical testing of asymptomatic people. This paper agrees, and draws the line sharply: **p-tau217 enrichment belongs in research, not in routine screening, until a prevention drug exists.** The ethical design of an enriched prevention trial must therefore include pre-test counselling, a right not to know one's stratum, and a plan for what participants are told when the trial ends. Enrichment that is scientifically efficient but ethically careless will destroy the trust on which prevention research depends.

### 4.5 Why this matters beyond wealthy health systems

For Pakistan and other low- and middle-income countries, the blood test matters more than the PET scan it replaces. Amyloid PET costs thousands of dollars per scan and exists in a handful of centres; a plasma p-tau217 assay is a blood draw. The AHEAD screening programme already uses %p-tau217 as the first pass before PET, across 106 sites on four continents, and showed the marker works across racial and ethnic groups (Molina-Henry et al., 2026). That makes p-tau217 the first AD biomarker that could plausibly be deployed at population scale in a country like Pakistan. But deployment without treatment is surveillance, not care: Pakistan has no prevention drug, no reimbursement pathway for one, and a dementia-care infrastructure that is largely family-based. The honest sequence is research participation first — Pakistani cohorts in global prevention trials, with the same counselling and protections — and clinical screening only after a prevention drug exists and is affordable. The numbers in this paper are offered as a design tool for that research, not as a reason to sell tests to healthy people.

## 5. Limitations

1. The Buckley risks are model-based standardised estimates from six selected research cohorts; participants were enriched for family history and APOE ε4, so absolute risks likely overstate those in the general population. The gradient between strata is more transportable than the levels.
2. The 10-year risks rest on sparse data (5% of participants followed beyond 10 years, mostly in one cohort) and are indicative only.
3. The "unselected" reference rate (17.8%) is the observed proportion progressed over a median 5.4 years, not a model-based five-year risk; it is an approximation, and the unselected sample size inherits that approximation.
4. Sample sizes assume a constant 30% relative risk reduction, no loss to follow-up, and no competing risks; real trials need inflation for attrition and for the fact that some participants will die of other causes before progressing.
5. Stratum prevalences (the fraction of screened people who are very-high) are not extracted here, so the number needed to screen — and therefore the screening cost of enrichment — is not computed. This is the largest practical gap in the paper.
6. The diranersen efficacy figures are conference-reported phase 2 results; the primary dose-response endpoint was missed, and the drug has not been tested in cognitively unimpaired people. It is used here as the worked example of a tau-lowering intervention, not as proven prevention therapy.
7. No new experimental data are presented. The trial arithmetic is computation from published risks; the hypothesis is untested.

## 6. Conclusion

A blood test can now put a number on an asymptomatic person's five-year risk of cognitive impairment: 12% if p-tau217 is low, 38% if it is very high. That number turns Alzheimer's prevention from an un-sizeable aspiration into a designable trial. Our arithmetic shows the scale of the change: a five-year prevention trial powered to detect a 30% risk reduction needs 1,412 unselected participants, 982 in the high stratum, and only 526 in the very-high stratum — with the number needed to treat falling from 18.7 to 8.8. The same numbers set the floor: no prevention trial can work in under five years, because two-year risks are 1–4% in every stratum. The next step is a trial that takes the numbers seriously — very-high p-tau217 enrichment, a five-year horizon, a tau-lowering intervention, and a pre-specified refutation rule. If the placebo arm progresses at the predicted rate and the drug does not slow it, the tau-prevention hypothesis fails cleanly; if it does, prevention becomes real. Either outcome is worth five years. What is not worth doing is testing healthy people in clinic before any of this exists.

---

## Acknowledgments

**AI assistance:** This manuscript was drafted with the assistance of an AI research assistant (Lapis, Meta Muse Spark), which performed the literature searches and the trial-arithmetic computations. The author takes responsibility for the content.

## References

1. Buckley RF, Townsend DL, Birkenbihl CJ, et al. Prognostic value of blood-based p-tau217 levels for progression to cognitive impairment. *JAMA*. 2026;336(11):950–959. doi:10.1001/jama.2026.12556. PMID 42449500; PMCID PMC13370474.
2. Molina-Henry DP, Liu A, Langford O, et al. Plasma phosphorylated tau 217 percentage by race and ethnicity in preclinical Alzheimer disease. *JAMA Neurol*. 2026. doi:10.1001/jamaneurol.2026.3598. (AHEAD 3-45 screening cohort: 15,612 cognitively unimpaired adults at 106 sites.)
3. van Dyck CH, Swanson CJ, Aisen P, et al. Lecanemab in early Alzheimer's disease. *N Engl J Med*. 2023;388:9–21. doi:10.1056/NEJMoa2212948.
4. Sims JR, Zimmer JA, Evans CD, et al. Donanemab in early symptomatic Alzheimer disease: the TRAILBLAZER-ALZ 2 randomized clinical trial. *JAMA*. 2023;330:512–525.
5. Ionis Pharmaceuticals and Biogen. Ionis and partner Biogen present Phase 2 CELIA data for diranersen at the Alzheimer's Association International Conference. Press release, 14 July 2026. https://ir.ionis.com/news-releases/news-release-details/ionis-partner-biogen-presents-phase-2-celia-data-aaic
6. AHEAD 3-45 Study: a study to evaluate efficacy and safety of treatment with lecanemab in participants with preclinical Alzheimer's disease and elevated amyloid and in participants with early preclinical Alzheimer's disease and intermediate amyloid. ClinicalTrials.gov NCT04468659.
7. U.S. Food and Drug Administration. FDA clears first blood test to aid in diagnosing Alzheimer's disease (Lumipulse G pTau217/β-Amyloid 1-42 Plasma Ratio, Fujirebio Diagnostics). News release, 16 May 2025.
8. Predicting risk of cognitive impairment with Alzheimer disease blood biomarkers. *JAMA*. 2026. doi:10.1001/jama.2026.13322. (Editorial accompanying Reference 1.)

## Data availability

- Trial-arithmetic computation: script and outputs in `hidden_files/ptau217-trial-sizes.py` (goal workspace). All input risks trace to Buckley et al. (Reference 1), Table 2 and abstract; the unselected reference rate is the observed 478/2,684 from the same paper.
- Prognostic data: all risk estimates, hazard ratios, confidence intervals and PACC slopes are taken from Buckley et al. (Reference 1), read in full text via PubMed Central (PMCID PMC13370474) on 3 November 2026.
- Screening context: AHEAD 3-45 screening figures from Molina-Henry et al. (Reference 2) and the trial record (Reference 6).
- Diranersen figures: Ionis/Biogen press release (Reference 5), corroborated by Reuters (14 July 2026) and NeurologyLive (14 July 2026) reporting of the AAIC 2026 presentation.
- Literature basis: daily research digest 2026-11-03 (`~/workspace/research-team/digests/2026-11-03.md`) plus targeted PubMed verification of the anchor paper (PMID 42449500, verified via NCBI E-utilities and PubMed Central, 3 November 2026).
- Research agents (Denario, EvoScientist, Mimosa, Co-Scientist) were **not** used for this paper: Mimosa's litellm auth patch is verified working, but its smoke run stalled in an MCP-discovery loop and the log records that it must not be re-run without the user's explicit word; Co-Scientist, Denario and EvoScientist remain blocked on authentication (the stored Gemini credential reaches Google only as a URL `?key=` surrogate; the agents require it in the Authorization header), and no key was requested or invented in this run. The paper was drafted from the digest, targeted literature checks and the author's own computation.
