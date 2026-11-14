# The Serotonin Dimmer: A Falsifiable Dip-and-Recovery Model of Visual Attention Across the First Six Weeks of SSRI Therapy

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan · ORCID 0009-0001-5921-7509
**Drafting assistant:** Lapis (AI)
**Date:** 10 November 2026 · **Paper #10 — Brain track** (Daily Research Papers; 4th Brain-track paper)

**Keywords:** serotonin; dorsal raphe; visual attention; selective serotonin reuptake inhibitors; SSRI; 5-HT1A autoreceptor; attention gain; depression; falsifiable hypothesis

---

## Abstract

Serotonin has been known for a century as a mood chemical; its control of attention was not. Lehnert et al. (*Nature Communications* 2026) showed that dorsal raphe serotonin neurons act as a gain control — a "dimmer switch" — on visual attention in mice: reducing serotonin activity improved detection of a faint visual target, increasing it impaired detection. Selective serotonin reuptake inhibitors (SSRIs), the most widely prescribed psychiatric drugs, raise synaptic serotonin, yet the literature on their cognitive effects is contradictory: a 2018 meta-analysis of 33 studies found modest positive effects on attention in depressed patients and no effect in non-depressed participants, a 2024 fluoxetine review found the effects inconsistent and often negative in healthy animals, and a 6-week paediatric sertraline trial found no attention harm at all. We propose that these three findings are one time-course, not three contradictions. The **serotonin-dimmer model** states that acute elevation of serotonergic tone transiently lowers visual-attention sensitivity, and that chronic exposure restores it to or above baseline as 5-HT1A autoreceptors desensitise — predicting a measurable dip-and-recovery in attention (d′) over the first six weeks of SSRI therapy. We specify the falsifying experiment: a prospective cohort of drug-naïve depressed adults tested on a low-contrast visual search task at baseline and on days 3, 7, 14, 28 and 42, powered at n = 32 (38 with attrition) for a medium within-subject effect. If d′ does not dip in week 1, or does not recover by week 6, the model fails. This is a hypothesis and trial-design paper, not a treatment recommendation: no human attention data under SSRI initiation are presented.

---

## 1. Introduction

Everyone has moments of sharp focus and moments of drift, but the biology that sets the moment-to-moment strength of attention has remained poorly understood. Attention is usually described through its cortical machinery — frontal-parietal networks, theta oscillations that organise frontal-cortex communication (Broschard et al., 2026), and the coordinate-like maps the ventromedial prefrontal cortex uses to organise even emotional knowledge (Ma & Kragel, 2026). What has been missing is a chemical gain control: a signal that dials attention up or down without switching it on or off.

Lehnert et al. (2026) supplied one. Working at McGill, PhD student Jonas Lehnert trained mice to find a faint hidden visual target — the rodent analogue of picking a face out of a crowd — while recording and manipulating serotonin-producing neurons of the dorsal raphe nucleus. When serotonin activity was reduced, the mice focused better; when it was increased, they focused worse. The effect was graded, not binary, leading the authors (co-led by Arjun Krishnaswamy and Erik Cook) to describe dorsal raphe serotonin as a "dimmer switch" on attention. The authors explicitly caution that their precise, circuit-level manipulation differs from how serotonergic drugs act in people — and that caution is exactly where this paper starts.

SSRIs are the natural human test of the dimmer. They raise synaptic serotonin within hours, yet their therapeutic effect takes two to six weeks, and their cognitive effects are famously inconsistent. A meta-analysis of 33 studies (1998–2017) found that antidepressants modestly improve divided attention, executive function, immediate memory, processing speed, recent memory and sustained attention in depressed participants — with SSRIs showing the greatest positive effect — but found no significant cognitive effect in non-depressed participants (Prado et al., 2018). A 2024 review of fluoxetine found the picture "inconsistent and elusive": cognitive improvements in patients with underlying disorders, but negative effects in healthy, non-diseased animals, with outcomes depending on gender, treatment duration, age, disease and the test used (Ampuero et al., 2024). And a 6-week randomised trial of sertraline (25–100 mg/day) in 28 children and adolescents with anxiety found no negative effect on attention at all — divided-attention response speed even improved (p = 0.02) — while verbal-memory interference worsened (p = 0.05) (Günther et al., 2005, as cited below).

No study has yet tested attention on the time course the mechanism predicts. If serotonin is a dimmer, then the first days of SSRI therapy — when synaptic serotonin rises but autoreceptors have not yet adapted — should transiently *worsen* fine visual attention, and the following weeks should restore it. The literature's inconsistency is then not noise: it is the same curve sampled at different times, in different populations, with different tests. This paper formalises that curve, states the four predictions that would confirm or refute it, and designs the study that tests it.

## 2. Methods

### 2.1 Literature basis

The literature sweep is the 2026-11-10 daily research digest (305 candidates screened: 50 PubMed, 0 arXiv q-bio, 255 bioRxiv; 8 selected — all antimicrobial-resistance or drug-discovery, none neuroscience) plus targeted searches on serotonin and attention, SSRI cognition, and November 2026 neuroscience. Every reference below was verified against its primary source on 10 November 2026: Lehnert et al. via Crossref (Nature Communications 2026, vol. 17, article 3464, published 18 March 2026; news coverage 9 November 2026) and the publisher's summary; Broschard et al. via Crossref and Cell Reports; Ma & Kragel via Crossref (PLOS Biology 2026, vol. 24, published 2 November 2026); Baker et al. via the Nature Neuroscience record (DOI 10.1038/s41593-026-02490-y); Kim et al. via NeuroImage; and the three SSRI-cognition sources via PubMed E-utilities (esummary article-IDs and DOIs). No unpublished, anecdotal or press-release-only efficacy claim is used as evidence; secondary reporting was used only to locate primary papers. This paper presents no new human data, no animal data and no simulation. Its results are a synthesis, a formal model, and a fully specified trial design.

### 2.2 The model (formal statement)

Let S(t) be effective serotonergic tone at the dorsal-raphe → visual-cortex pathway at time t after SSRI initiation, and A(t) be visual-attention sensitivity (signal-detection d′) on a low-contrast visual search task. The model asserts:

1. **Gain rule:** A is a decreasing function of S over the physiological range (the dimmer), i.e. dA/dS < 0, for fine-discrimination tasks.
2. **Acute phase:** S rises within days of SSRI initiation (reuptake blockade), before adaptation; therefore A dips in week 1.
3. **Adaptation phase:** over 2–6 weeks, somatodendritic 5-HT1A autoreceptors desensitise, raphe firing recovers, and net serotonergic signalling normalises; therefore A recovers to baseline or above by week 6.
4. **Task specificity:** the dip is largest for fine visual discrimination (low-contrast targets, as in Lehnert's task) and smallest or absent for simple sustained-attention tasks.

### 2.3 Proposed study (design, not a result)

**Population:** drug-naïve adults (18–55 years) with a new diagnosis of major depressive disorder, starting SSRI monotherapy (escitalopram or sertraline, clinician's choice, standard dosing). Exclusions: other psychotropics, substance use, neurological disease, uncorrected visual impairment, shift work.

**Task:** a computerised low-contrast visual search task modelled on Lehnert's faint-target paradigm (target present/absent, contrast titrated to ~75% baseline accuracy), plus a standard sustained-attention control task (continuous performance test). Primary endpoint: change in d′ on the visual search task at days 3–7 versus baseline. Secondary endpoints: d′ at days 14, 28 and 42; sustained-attention d′; depression severity (PHQ-9); plasma SSRI concentration at each visit.

**Schedule:** baseline (day 0, before first dose), day 3, day 7, day 14, day 28, day 42. A waitlist control group (depressed adults awaiting treatment, same schedule, no drug) separates drug effects from practice effects and spontaneous mood change.

**Analysis:** linear mixed model of d′ over time with group × time interaction; primary contrast day 3–7 versus baseline within the SSRI arm; pre-registered one-sided prediction of a dip followed by recovery (quadratic time term).

### 2.4 Power analysis (our computation)

Sample sizes use the normal approximation n = (Z₁₋α/₂ + Z₁₋β)² / dz² for a paired design (7.85/dz²) and n per arm = 2 × 7.85/d² for a parallel two-arm comparison, at 80% power and two-sided α = 0.05, with 15% attrition. The assumed effect is medium (dz = 0.5) — deliberately conservative, because the mouse effect direction is clear but its human magnitude is unknown. All numbers in §3.4 are computed from these stated formulas, not from data.

## 3. Results

### 3.1 The November 2026 neuroscience landscape (synthesis)

Five verified findings from October–November 2026 frame the model. None is our data; the synthesis is ours.

| Finding | Source | What was shown (verified) |
|---|---|---|
| Serotonin dims visual attention | Lehnert et al., *Nat Commun* 2026;17:3464 | Dorsal raphe serotonin neurons grade the strength of visual attention in mice; less serotonin → better faint-target detection, more → worse |
| Theta organises frontal cognition | Broschard et al., *Cell Rep* 2026 | Theta waves (4–10 Hz) organise information across frontal cortex during a dot-pattern categorisation task in non-human primates; theta phase couples to beta amplitude, beta phase to gamma amplitude |
| Emotions sit on a grid map | Ma & Kragel, *PLOS Biol* 2026;24 | Ventromedial prefrontal cortex maps emotional knowledge with sixfold (60°) grid-like symmetry, across two different stimulus types |
| Psilocybin remodels spines by brain state | Baker et al., *Nat Neurosci* 2026 | 5-HT2A receptors in layer 5 pyramidal neurons mediate psilocybin's neuroplastic (spine growth within 24 h) but not its hallucinogenic effects; chronically stressed mice show a larger spine surge and halted synapse loss, healthy mice return to baseline over three weeks |
| AI separates Parkinson's brain rhythms | Kim et al., *NeuroImage* 2026 | NONOS, a deep-learning separator of rhythmic from background brain activity, predicted the stepping foot in Parkinson's patients with accuracy 0.98 versus 0.54–0.79 for conventional methods, and detected the rapid beta-band fall after deep brain stimulation in mice |

Two patterns matter for this paper. First, serotonin is doing two different jobs through two different receptors in the same month's literature: 5-HT signalling *dims* attention via the raphe (Lehnert) while 5-HT2A signalling *rebuilds* synapses (Baker) — receptor and circuit, not the molecule alone, determine the effect. Second, the brain's timing systems (theta organisation, grid-like maps) are about *structure*, while serotonin is about *gain*: the dimmer sets how strongly a structured system attends. That division is what makes the model testable — gain changes should show up first and largest on fine-discrimination tasks, not on all cognition at once.

### 3.2 The four predictions (the paper's own contribution)

- **P1 — the dip:** visual-search d′ at days 3–7 is lower than baseline in the SSRI arm (predicted direction: down; predicted size: medium, dz ≈ 0.5).
- **P2 — the recovery:** visual-search d′ at day 42 is at or above baseline, and higher than at days 3–7.
- **P3 — task specificity:** the dip is larger on the low-contrast visual search task than on the sustained-attention control task (interaction between task type and time).
- **P4 — dose tracking:** the size of the week-1 dip correlates with plasma SSRI concentration at day 7 (higher exposure → larger dip), and the recovery tracks the 2–6-week adaptation window, not the plasma level alone.

### 3.3 Reconciliation: three "contradictory" literatures as one curve

Read against the model, the existing evidence stops contradicting itself:

- **Healthy animals get worse** (Ampuero et al., 2024): acute serotonergic elevation in a healthy brain, no depression to treat, no adaptation window sampled — the dip, observed alone.
- **Depressed patients get better** (Prado et al., 2018, 33 studies): measured after weeks of treatment, when adaptation has occurred and mood improvement itself lifts attention — the recovery, observed alone.
- **No effect at 6 weeks in children** (Günther et al., 2005, n = 28): measured at the recovery plateau, on tasks that mix sustained and divided attention rather than fine visual discrimination — the flat tail of the curve, on the least sensitive task.

Each literature sampled a different segment of the same dip-and-recovery curve. The model predicts that a single study sampling all six weeks, with the fine-discrimination task, will see the whole curve — and that is precisely what no published study has done.

### 3.4 Power analysis (our computation)

| Assumed effect (dz) | Paired n (80% power, α = 0.05) | +15% attrition | Parallel waitlist comparison (per arm) |
|---|---|---|---|
| 0.35 (small–medium) | 65 | 77 | 129 |
| **0.50 (medium — primary)** | **32** | **38** | **63** |
| 0.65 (medium–large) | 19 | 23 | 38 |

The primary design therefore enrols **38 drug-naïve patients** (32 completers) for the within-subject primary endpoint, with a waitlist control arm of 63 per arm (149 total with attrition) if the parallel comparison is funded. A pilot of n = 12, tested at baseline and day 7 only, would detect only a large effect (dz ≥ 0.8) and is recommended solely as a feasibility check for the task, not as a test of the model.

## 4. Discussion

**Why the dimmer matters clinically.** If P1 holds, the first week of SSRI therapy carries a transient, measurable cost to fine visual attention — the kind of attention used in driving, examinations and safety-critical work. Patients are currently counselled about nausea, sleep change and agitation in week 1; a transient attention dip, if real, belongs on the same counselling list, and it is testable in a single clinic visit with a 10-minute computerised task. If P1 fails, the counselling implication vanishes — which is itself a useful clinical answer.

**Why the recovery matters for trial design.** Antidepressant trials that measure cognition at a single post-treatment time point are sampling one point on a moving curve. A trial that tests attention at week 2 can conclude SSRIs impair cognition; the same trial at week 6 can conclude they improve it. Both can be right about their time point and wrong about the drug. Future cognition endpoints in antidepressant trials should be time-coursed, not single-point.

**Mechanistic grounding and its limits.** The 2–6-week delay in SSRI therapeutic onset is conventionally attributed to desensitisation of somatodendritic 5-HT1A autoreceptors, which initially suppress raphe firing and then adapt, permitting increased serotonergic transmission. Our model borrows that established pharmacological account for the *timing* of the recovery, and Lehnert's circuit result for the *direction* of the acute effect. The link between the two is inference, not measurement: no study has yet recorded raphe activity, autoreceptor sensitivity and attention in the same human across SSRI initiation. The proposed study does not measure autoreceptors either — it tests the behavioural curve the mechanism predicts. A follow-up using PET 5-HT1A imaging would test the mechanism itself.

**Relation to the wider 2026 findings.** The Baker et al. psilocybin result is a useful contrast: a serotonergic drug that *rebuilds* synapses through cortical 5-HT2A receptors, with effects that depend on the brain's prior state (stressed versus healthy). Serotonin pharmacology is therefore not one effect but a set of receptor- and circuit-specific effects with different time courses — acute gain reduction (raphe, days), structural remodelling (cortical 5-HT2A, 24 hours to weeks), and mood recovery (weeks). Any claim of the form "serotonin improves/worsens cognition" that does not specify receptor, circuit, task and time is underspecified. The NONOS result (Kim et al., 2026) shows the measurement side is ready: modern signal separation can resolve rapid, previously invisible changes in brain rhythms — the same temporal resolution the dip-and-recovery curve needs.

**ADHD and comorbidity.** Lehnert et al.'s authors note the relevance to ADHD. The model adds a pharmacological prediction: in patients with comorbid depression and ADHD, SSRI initiation should transiently worsen attentional symptoms in week 1 before any mood-mediated improvement — a pattern clinicians anecdotally report and no trial has pre-registered. The proposed study's task battery could be extended to an ADHD symptom scale as a secondary endpoint.

## 5. Limitations

1. **Mouse to human.** Lehnert's result is in mice, on a visual detection task, with precise circuit manipulation. Human SSRIs raise serotonin globally and bluntly; the dimmer may not translate, or may translate only for some tasks.
2. **Depression confounds attention.** Depression itself impairs attention, and mood improves over six weeks. The within-subject dip (P1) is protected from this confound — mood does not worsen in week 1 while attention dips — but the recovery (P2) is not: recovery could reflect mood improvement rather than autoreceptor adaptation. The waitlist control and the plasma-level correlation (P4) are the design's answers, and they are partial.
3. **No data are presented.** This is a hypothesis and design paper. The model is falsifiable, not confirmed.
4. **The 5-HT1A mechanism is inferred.** Autoreceptor desensitisation is the standard account of SSRI onset delay, but it is not measured in the proposed study; a PET follow-up is needed to test the mechanism rather than its behavioural shadow.
5. **Publication timing.** Lehnert et al. was published 18 March 2026; the November 2026 date attached to it in news coverage is the coverage date, not the publication date. The model is built on a March finding, synthesised in November — the synthesis is new, the anchor is eight months old, and any newer replication would supersede it.

## 6. Conclusion

Serotonin is a dimmer on attention, not a switch — and the most prescribed serotonergic drugs in medicine have never been tested against that dimmer on its own time course. The serotonin-dimmer model predicts a dip in fine visual attention in the first week of SSRI therapy and a recovery by week six, explains three apparently contradictory literatures as three segments of one curve, and fails cleanly if the dip does not appear. The experiment needs 38 drug-naïve patients, a 10-minute computerised task, and six weeks. Until it is run, no clinician should counsel a patient that SSRIs will either help or harm their attention in week 1 — because the honest answer, today, is that nobody has looked at the right time, with the right task.

---

## References

1. Lehnert J, Cha S, Forestell A, Yang Y, Ma C, Shariff S, Britt JP, Khadra A, Cook EW, Krishnaswamy A. Rapid dynamics of dorsal raphe serotonin neurons regulate the strength of visual attention. *Nature Communications*. 2026;17:3464. doi:10.1038/s41467-026-70658-y.
2. Broschard MB, Brincat SL, Loonis RF, Miller EK. Theta-based organization of information in the frontal cortex. *Cell Reports*. 2026. doi:10.1016/j.celrep.2026.118262.
3. Ma Y, Kragel PA. Emotion knowledge is structured in a grid-like coordinate system in the human ventromedial prefrontal cortex. *PLOS Biology*. 2026;24. doi:10.1371/journal.pbio.3003795.
4. Baker JJ, Kogan E, Ma S, Lu J, Zuo Y. 5-HT2A receptors in layer 5 pyramidal neurons mediate the neuroplastic but not the hallucinogenic effects of psilocybin. *Nature Neuroscience*. 2026. doi:10.1038/s41593-026-02490-y.
5. Kim J, et al. Neural oscillation and non-oscillation separator for highly time-resolved decomposition of beta band activity. *NeuroImage*. 2026. doi:10.1016/j.neuroimage.2026.122280.
6. Ampuero E, Luarte A, Flores FS, Soto AI, Pino C, Silva V, et al. The multifaceted effects of fluoxetine treatment on cognitive functions. *Frontiers in Pharmacology*. 2024;15:1412420. doi:10.3389/fphar.2024.1412420. PMID: 39081952.
7. Prado CE, Watt S, Crowe SF. A meta-analysis of the effects of antidepressants on cognitive functioning in depressed and non-depressed samples. *Neuropsychology Review*. 2018;28:32–72. doi:10.1007/s11065-018-9369-5. PMID: 29446012.
8. Günther T, Holtkamp K, Jolles J, Herpertz-Dahlmann B, Konrad K. The influence of sertraline on attention and verbal memory in children and adolescents with anxiety disorders. *Journal of Child and Adolescent Psychopharmacology*. 2005;15(4):608–618. doi:10.1089/cap.2005.15.608. PMID: 16190792.

*Reference notes: reference 6 — first six authors listed; full author list via the DOI. Reference 7 — the meta-analysis included 33 studies published January 1998–January 2017. Reference 8 — n = 28, ages 8–17, sertraline 25–100 mg/day for 6 weeks; divided-attention response speed improved (p = 0.02), verbal-memory interference worsened (p = 0.05).*

---

## Data availability

No new data were generated. All numbers in §3 trace to the cited primary sources (verified 10 November 2026 via Crossref and PubMed E-utilities) or to the power calculations in §2.4, which are reproducible from the formulas stated there. The literature sweep is the 2026-11-10 daily research digest (305 candidates screened; 8 selected, none neuroscience) plus the targeted searches described in §2.1. Analysis code: the power calculations were run in Python 3 (normal approximation; statsmodels not installed). Correspondence: Zubair Ali, SMBBMU Larkana, Pakistan.

## AI-assistance disclosure

AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent verification. Drafting assistant: Lapis (AI). The author reviewed the manuscript and takes responsibility for its content. This manuscript has not been submitted to any journal or preprint server.
