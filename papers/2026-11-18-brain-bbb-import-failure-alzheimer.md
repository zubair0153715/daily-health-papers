# Import Failure Before Leak: The Blood–Brain Barrier as a Supply Line Whose Early Shutdown Initiates Alzheimer's Disease — a Falsifiable Model and a Re-Ranking of Brain-Delivery Strategies

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan · ORCID: 0009-0001-5921-7509
**Drafting assistant:** Lapis (AI)
**Date:** 18 November 2026 · **Paper #6 — Brain track** (Daily Research Papers, 5-field rotation)

**Keywords:** blood–brain barrier; Alzheimer's disease; apolipoprotein A1; APOA1; SR-B1; ABCA1; SERPINA1; CASS4; microglia; astrocytes; brain delivery; 5xFAD

---

## Abstract

For a century the blood–brain barrier (BBB) has been treated as a fortress whose failure in Alzheimer's disease (AD) is a leak: tight junctions break, albumin and fibrinogen flood in, neuroinflammation follows. A study published in *Cell* on 11 November 2026 (Zhou et al.) overturns the order of events. Using bioorthogonal proteomics, the authors tracked 861 plasma proteins in mice and found the healthy BBB samples 191 and permits only **92 (10.7%)** into the brain parenchyma — a selective import system, not a wall. The imported proteins home to specific cell types: liver-derived apolipoprotein A1 (APOA1) crosses via SR-B1 and engages astrocytic ABCA1, an Alzheimer's risk gene, driving cholesterol efflux that supports synapse integrity; alpha-1 antitrypsin (SERPINA1) homes to microglia. In early-stage 5xFAD mice, the barrier first *remodels transport* — APOA1 uptake falls, SERPINA1 uptake rises — before any leak; hepatic overexpression of APOA1 restores brain APOA1 and rescues astrocytic, synaptic and behavioural deficits. We add two new quantitative facts and a synthesis. First, from UniProt (P02647), human APOA1 is a 267-amino-acid, 30,778 Da protein — **68 times the 450 Da passive-diffusion cut-off** — so its brain entry is necessarily receptor-mediated, and any drug strategy that relies on passive entry cannot reproduce it. Second, the human observational record is consistent with, but does not prove, the import-first model: in the Amsterdam Dementia Cohort (n = 429 non-demented elderly, mean follow-up 2.5 years), lower plasma APOA1 predicted clinical progression in APOE ε4 carriers with subjective cognitive decline (hazard ratio 5.0; 95% CI 1.3–18.9), while higher cerebrospinal fluid (CSF) APOA1 predicted progression overall (HR 1.3 per standard deviation; 95% CI 1.0–1.6) — a pattern compatible with a disrupted plasma-to-brain gradient, but equally compatible with leak. **Falsifiable claim:** in preclinical AD, BBB import of liver-derived APOA1 falls before measurable barrier leak, and the CSF:plasma APOA1 ratio predicts clinical progression earlier than amyloid-PET positivity. **Falsifier:** a longitudinal human cohort in which the CSF:plasma APOA1 ratio does not fall before amyloid positivity, or in which gadolinium-measured leak precedes the import fall, refutes the import-first ordering; and a liver-targeted APOA1 intervention that raises brain APOA1 without slowing tau spread refutes the disease-modifying version of the claim while leaving the biomarker version intact. Causal identification for the human claim is **association only**; causality is established in mice only. We re-rank brain-delivery strategies against this model: receptor-mediated import restoration (endogenous SR-B1/APOA1 route; transferrin-receptor shuttles, with a company-reported >65-fold delivery gain in preclinical studies) outranks leak-sealing and passive-diffusion strategies, and we show why the peptide drugs that failed in Parkinson's trials could never have tested their own mechanism. Policy implication: Pakistan's health research funders should add the plasma/CSF APOA1 ratio to the national dementia cohort protocol and fund a liver-targeted APOA1 pilot before funding another leak-sealing trial — under the Islamic principle of *hifz al-nafs* (preservation of life), one of the five objectives of the Shariah.

---

## 1. Introduction

Alzheimer's disease affects more than 55 million people worldwide, and no therapy yet prevents its onset. The dominant mechanistic story of the last decade has been amyloid-first: amyloid-β accumulates, tau spreads, neurons die. The vascular story ran in parallel and in second place: the blood–brain barrier breaks down, toxic blood proteins leak in, and neuroinflammation accelerates decline. The leak story has real human evidence — Montagne et al. (*Neuron*, 2015) showed BBB breakdown in the aging human hippocampus, worsening with mild cognitive impairment — and it shaped drug design: if the barrier leaks, then either seal it, or exploit the leak.

The *Cell* paper of 11 November 2026 changes the sequence. Zhou and colleagues, led by Andrew C. Yang at the Gladstone Institutes and UCSF, mapped for the first time which circulating proteins actually cross an intact BBB. The result is a supply line, not a fortress: of 861 tracked plasma proteins, the healthy BBB samples 191 and admits 92 into the parenchyma, most of them made in distant organs — predominantly the liver — and each routed to a specific brain cell type by a molecular "ZIP code". The headline protein is APOA1, the main protein of high-density lipoprotein, made in the liver, crossing via the scavenger receptor SR-B1 and engaging astrocytic ABCA1 to drive cholesterol efflux and maintain synaptic density. The second is SERPINA1 (alpha-1 antitrypsin), routed to microglia. In early 5xFAD mice the transport system remodels first — APOA1 import falls, SERPINA1 import rises — while the barrier is still physically intact. Only later does the anatomy collapse and leak begin. And the causal arrow was tested, not merely observed: engineering the liver to overexpress human APOA1 raised brain APOA1 and rescued astrocytic, synaptic and behavioural deficits in the Alzheimer's mice.

Two independent November 2026 findings converge on the same picture from the immune side. Walsh et al. (*Journal of Experimental Medicine*, 2026) showed that CASS4, an Alzheimer's risk gene, controls microglial focal-adhesion biology: when CASS4 is ablated in 5xFAD mice, microglia fail to surround and compact amyloid plaques, amyloid load rises, and neurons near plaques are damaged. The brain's two defences — the vascular supply line and the microglial containment crew — are both gene-linked, both fail early, and both are peripheral in origin (liver proteins; a risk gene acting through immune cells). A third November finding, the APOE Christchurch (R136S) variant protecting against α-synuclein accumulation in mice (Soto-Faguás et al., *Cell Reports*, 2026; covered in our 13 November paper), points the same way: the lipid-transport axis, not the neuron alone, gates proteinopathy.

This paper does three things the *Cell* paper does not. First, it quantifies why APOA1's route matters for drug design: a 30.8 kDa protein cannot diffuse across the BBB, so any therapy that mimics or restores this supply line must use a receptor, and we rank the available receptor routes. Second, it tests the import-first model against the existing human record — the Amsterdam Dementia Cohort — and shows exactly where that record is ambiguous, turning the ambiguity into a specified, falsifiable human test. Third, it states the policy consequence for a low-resource health system: a blood test (plasma APOA1) is orders of magnitude cheaper than amyloid PET, and if import failure precedes amyloid positivity, the cheapest early-detection tool in dementia may already be sitting in a routine lipid panel.

## 2. Methods

### 2.1 Literature basis

The literature sweep for this paper was conducted on 18 November 2026. Note on sources: the daily research digest series ends at 14 November 2026 (the digest job was disabled on 14 November), so no fresh digest existed for this run; the sweep therefore used targeted checks instead — PubMed E-utilities (entry-date windows 15–18 November 2026), Crossref verification of the *Cell* DOI, and a news sweep of neuroscience reporting for 9–17 November 2026, which surfaced the *Cell* atlas, the CASS4 paper and the TXP1 shuttle announcement. Every citation below was verified against PubMed, Crossref or the publisher's record on the day of writing; no citation is taken from memory. The Islamic canon leg used the verified literature map in the programme files (Ibn Sina, *Al-Qanun fi al-Tibb*, c. 1025; Al-Ghazali, *Ihya Ulum al-Din*, c. 1096–1106; Al-Shatibi, *Al-Muwafaqat*, d. 1388), consulted through that map and secondary literature — the full Arabic text of the Canon was not re-read for this paper, and this is stated as a limitation.

### 2.2 Protein-size computation (own analysis)

Human APOA1 was retrieved from UniProt (accession P02647, reviewed entry APOA1_HUMAN) via the UniProt REST API on 18 November 2026. Recorded: 267 amino acids, molecular weight 30,778 Da (precursor; the mature circulating form is 243 amino acids, ~28.1 kDa). The passive BBB diffusion limit used is the standard CNS-likeness cut-off of 450 Da (the same criterion applied to GLP-1 receptor agonists in our 2 November paper). Ratio computed as 30,778 / 450 = 68.4. Import fractions were computed from the *Cell* paper's reported counts: 92 / 861 = 10.7% admitted; 191 / 861 = 22.2% sampled.

### 2.3 Analysis plan (stated before results)

The plan was fixed before the Results were written: (i) verify the *Cell* atlas and its numbers against Crossref and the published abstract; (ii) compute APOA1's size against the passive-diffusion cut-off; (iii) retrieve the best human APOA1–AD cohort study and record its effect sizes with confidence intervals, without selecting for a favourable direction; (iv) rank brain-delivery strategies by demonstrated brain gain, labelling company announcements as such; (v) state the falsifiable claim and its falsifier. No post-hoc analysis was added after seeing the results; the comparison with the Nov 2 GLP-1 paper was pre-planned as the "strongest incumbent" test.

### 2.4 Honesty limits

This is a literature-synthesis and computational-descriptor study plus a proposed test design. No new patient data, no animal data and no new laboratory measurements are presented. The *Cell* results are mouse results (5xFAD, a familial amyloid model); the human evidence is observational. The TXP1 figure is a company announcement, not a peer-reviewed result. The paper's claim is therefore narrow: the import-first *ordering* is established in mice and compatible with — not proven by — the human record, and the human test is specified here, not claimed as done.

## 3. Results

### 3.1 The atlas: a selective import system, not a wall

Zhou et al. (*Cell*, 2026; DOI 10.1016/j.cell.2026.10.039; 30 authors) used bioorthogonal click-chemistry labelling to tag the mouse plasma proteome and trace which proteins reach the brain parenchyma. The counts are the paper's core quantitative result:

| Step | Proteins (of 861 tracked) | Share |
|---|---|---|
| Sampled by the BBB | 191 | 22.2% |
| Admitted into brain parenchyma | 92 | **10.7%** |
| Excluded | 769 | 89.3% |

The 92 are enriched for carrier and metabolic functions and are mostly synthesised outside the nervous system, predominantly in the liver. They do not diffuse randomly: each homes to a designated cell type. APOA1 → astrocytes; SERPINA1 → microglia. The routing is receptor-mediated — a "BBB–parenchyma receptor hand-off": APOA1 crosses via SR-B1 (scavenger receptor class B type 1) and engages astrocytic ABCA1 (ATP-binding cassette transporter A1), which the *Cell* paper identifies as a key Alzheimer's risk gene, driving cholesterol efflux that supports synapse integrity.

**Our computation.** Human APOA1 (UniProt P02647) is 267 amino acids, 30,778 Da as a precursor (≈28.1 kDa mature). Against the 450 Da passive-diffusion cut-off, it is **68 times too large to cross passively**. This is not a marginal miss: it is the same order of magnitude as the GLP-1 peptides in our 2 November paper (8–11× over the cut-off, 0 of 4 CNS criteria met). The consequence is categorical — APOA1's brain entry *must* be active transport — and it reframes the drug-design question. A therapy that restores the APOA1 supply line cannot be a small molecule that diffuses; it must either raise the liver's own production (as the mouse experiment did), or ride a receptor (SR-B1, transferrin receptor, or an equivalent shuttle).

### 3.2 The ordering: import failure first, leak second

The decisive finding is temporal. In early-stage 5xFAD mice, the BBB shows *selective transport remodelling* — reduced APOA1 uptake and increased SERPINA1 uptake — while tight junctions are intact and there is no nonspecific leakage (contrast with lipopolysaccharide-induced leakage, which the paper used as a control). The sequence the paper establishes is:

1. **Early import shutdown.** The barrier stops importing neuroprotective proteins, notably liver-derived APOA1, before it physically degrades.
2. **Synaptic erosion.** Starved of peripheral signals, astrocytes fail to maintain synaptic integrity: dendritic spine loss, circuit dysfunction, early behavioural deficits.
3. **Late barrier breakdown.** Only after prolonged transport starvation does the anatomical structure collapse, permitting toxic peripheral influx (the albumin/fibrinogen leak described by Montagne et al., *Neuron*, 2015, in the aging human hippocampus).

The causal test in mice: hepatic overexpression of human APOA1 raised circulating APOA1, increased brain APOA1, and rescued astrocytic, synaptic and behavioural deficits in 5xFAD mice. The authors' own summary is that "Alzheimer's disease may not start entirely inside the brain; it may start when the brain's supply line from the body is severed."

### 3.3 The human record: compatible, ambiguous, and therefore testable

The best human study of APOA1 in pre-dementia is Slot et al. (*Journal of Alzheimer's Disease*, 2017; PMID 28035918; DOI 10.3233/JAD-151068), from the Amsterdam Dementia Cohort: 429 non-demented elderly (206 with subjective cognitive decline, 223 with mild cognitive impairment), mean follow-up 2.5 ± 1.6 years, 117 (27%) showing clinical progression. Adjusted Cox models (age, sex, MMSE, plasma cholesterol) found:

| Measure | Effect on clinical progression | 95% CI |
|---|---|---|
| CSF APOA1, per 1 SD increase | HR 1.3 | 1.0–1.6 |
| Lower plasma APOA1, APOE ε4 carriers with subjective cognitive decline | HR 5.0 | 1.3–18.9 |

The pattern — low plasma APOA1 predicting progression, high CSF APOA1 also predicting progression — is *compatible* with the import-first model (a failing import gradient: less arriving from plasma, more retained or produced intrathecally), but it is equally compatible with early leak (plasma proteins entering CSF through a degrading barrier). The study cannot distinguish the two mechanisms, because it did not measure leak (no gadolinium MRI) and did not measure import (no CSF:plasma ratio tracked against amyloid-PET timing). That ambiguity is precisely what our proposed test resolves (Section 4.3). Note also the width of the second confidence interval (1.3–18.9): the APOE ε4 subgroup estimate is imprecise, and we report it as such rather than as a precise "five-fold risk".

### 3.4 The second defence fails in parallel: CASS4 and microglial containment

Walsh et al. (*Journal of Experimental Medicine*, 2026; 223(12):e20260104; DOI 10.1084/jem.20260104; first author Adeline E. Walsh, senior author John Lukens, University of Virginia) established the function of CASS4, previously only a GWAS risk signal. CASS4 controls microglial focal-adhesion biology: when CASS4 is ablated in 5xFAD mice, microglia fail to gather around amyloid plaques and compact them, plaques grow and spread more aggressively, nearby nerve fibres are damaged, and the mice show cognitive decline. Microglia-specific deletion reproduces the effect. This matters for the import-first model in two ways. First, SERPINA1 — the protein whose import *rises* in early 5xFAD — homes to microglia, the very cells whose containment function CASS4 controls; the import remodelling and the containment failure are two faces of one early immune-vascular failure, not two separate stories. Second, it gives the model a second falsifiable handle: if import restoration rescues synapses but plaques still spread because microglial containment is independently broken, the therapy must fix both arms.

### 3.5 Re-ranking brain-delivery strategies against the import-first model

The strongest incumbent against which to judge any new delivery strategy is the current standard: anti-amyloid monoclonal antibodies (lecanemab, donanemab), which must cross the BBB from the blood, do so at roughly 0.1% of the plasma dose, and carry amyloid-related imaging abnormality (ARIA) risk. The import-first model re-ranks the alternatives:

| Strategy | Mechanism | Demonstrated brain gain | Status |
|---|---|---|---|
| Hepatic APOA1 raising | Restore the endogenous supply line (liver → SR-B1 → astrocyte) | Rescues astrocytic, synaptic, behavioural deficits in 5xFAD mice (Zhou et al., 2026) | Mouse, interventional |
| Transferrin-receptor shuttle (TXP1) | Receptor-mediated transcytosis via TfR1 | >65-fold increase in antibody brain delivery in preclinical studies incl. non-human primates | **Company announcement, 17 Nov 2026 (ProMIS/Ossianix) — not peer-reviewed** |
| Peptide GLP-1 receptor agonists | Passive diffusion (intended) | 0 of 4 CNS-likeness criteria; no demonstrated CNS target engagement (our 2 Nov 2026 paper) | Failed in phase III (Exenatide-PD3) |
| Leak-sealing (pericyte/tight-junction repair) | Fix the late leak | Targets the *third* step of the sequence | Conceptually late |
| Anti-amyloid antibodies | Cross BBB, clear plaque | ~0.1% brain entry; modest slowing, ARIA risk | Approved, incumbent |

The ranking is the paper's practical contribution: strategies that *use* a receptor (endogenous SR-B1 or an engineered TfR1 shuttle) align with how the brain actually receives proteins; strategies that rely on passive diffusion or on sealing a leak that appears late do not. The TXP1 figure (>65-fold) is the largest delivery gain reported in this window, but it is a company-reported preclinical number and must be treated as a claim to verify, not a fact — the paper's ranking holds even if TXP1's true gain is far smaller, because the endogenous APOA1 route is already demonstrated in mice.

## 4. Discussion

### 4.1 Mechanism: the supply-line model

The mechanism we propose, synthesising Zhou et al., Walsh et al. and the human cohort data, has four links, each with a test:

1. **Liver → blood.** Hepatocytes secrete APOA1 into plasma. *Test:* plasma APOA1 concentration tracks liver synthetic function; liver disease should predict faster cognitive decline (an existing, testable epidemiological prediction).
2. **Blood → brain.** SR-B1 mediates APOA1 transcytosis across the BBB endothelium; astrocytic ABCA1 receives it and drives cholesterol efflux that maintains synaptic density. *Test:* endothelial SR-B1 deletion should reproduce the synaptic phenotype without any amyloid manipulation.
3. **Import failure → synaptic erosion.** In early AD, transport remodels (APOA1 down, SERPINA1 up) before leak; astrocytes starved of APOA1 fail to maintain spines. *Test:* the longitudinal human cohort specified in Section 4.3.
4. **Parallel immune failure.** SERPINA1's microglial target and CASS4-dependent microglial containment fail together; plaques spread because the containment crew is impaired, not only because amyloid is overproduced. *Test:* combined APOA1 restoration + CASS4 boosting should outperform either alone in 5xFAD mice.

### 4.2 The Islamic canon as hypothesis ancestor

The supply-line model has a genuine ancestor in the Islamic medical tradition, and the programme's rule is to name it rather than to claim it as proof. Ibn Sina's *Al-Qanun fi al-Tibb* (Canon of Medicine, c. 1025) organised medicine around interacting organ systems and faculties: the liver as the seat of the natural faculty, producing the blood and nourishment on which the other organs depend, and the brain as the seat of the psychic faculty — sensation, imagination and reason. In that framework a disease of the brain can originate in the failure of a distant organ's supply, and treatment can act on the supplying organ rather than the suffering one. That is the structure of the Zhou et al. experiment — treat the liver, rescue the brain — stated nine centuries earlier as a system, not as a molecule. Al-Ghazali's *Ihya Ulum al-Din* (c. 1096–1106) makes the same structural point in moral psychology: the heart (*qalb*) rules the body, but its rule depends on the soundness of its members; a failure in one member corrupts the whole. Neither work proves anything about APOA1 — proof comes from the mouse and the cohort — but both show that the "brain disease as whole-body supply failure" framing is not a modern invention, and that the classical canon is a legitimate source of hypotheses, which is exactly how this programme uses it. The policy principle that follows is *hifz al-nafs*, preservation of life, one of the five objectives (*maqasid*) of the Shariah as defined by Al-Ghazali in *Al-Mustasfa* and systematised by Al-Shatibi in *Al-Muwafaqat* (d. 1388): a health system must preserve life by the most effective available means, and where a cheap blood test can detect a lethal disease earlier than an expensive scan, choosing the scan-first pathway fails that objective. The body as a trust (*amanah*, under the stewardship of *khilafah*, Qur'an 2:30) reinforces the same point: the liver–brain supply line is a trust to maintain, not a resource to exhaust.

### 4.3 The human test that would settle it (pre-specified design)

**Design.** A prospective longitudinal cohort of cognitively unimpaired adults aged 60–75 with a first-degree family history of AD or APOE ε4 carriership (n ≈ 1,000; powered on the Slot et al. progression rate of 27% over 2.5 years). At baseline and annually for 5 years: plasma APOA1, CSF APOA1 (CSF:plasma ratio as the import index), amyloid PET, and dynamic contrast-enhanced MRI for BBB leak (K<sup>trans</sup>). Primary analysis: does the CSF:plasma APOA1 ratio fall before amyloid-PET positivity, and does it predict clinical progression independently of amyloid? **Falsifier:** if the ratio does not fall before amyloid positivity, or if K<sup>trans</sup> leak precedes the ratio fall, the import-first ordering is refuted in humans. **Therapeutic test (phase II, contingent on the cohort result):** a randomised trial of a liver-targeted APOA1-raising intervention (e.g. an APOA1 mimetic peptide or a hepatocyte-targeted therapy) versus placebo in preclinical AD, with brain APOA1 (CSF) as the target-engagement readout and tau-PET spread as the outcome. **Falsifier:** if brain APOA1 rises without slowing tau spread, the disease-modifying version of the claim is refuted, and APOA1 remains a biomarker only. Either outcome is publishable; the design is written before the data exist, which is the point.

### 4.4 What this paper does not claim

It does not claim APOA1 therapy works in humans — no human interventional data exist. It does not claim the 92-protein atlas is complete in humans — it is a mouse atlas, and the human BBB proteome may differ. It does not claim plasma APOA1 alone diagnoses AD — the Slot et al. hazard ratios are modest and, in the APOE ε4 subgroup, imprecise. And it does not claim the classical Islamic physicians anticipated APOA1 — they anticipated the *structure* of the explanation, which is a different and smaller claim, stated as such.

## 5. Limitations

1. **Mouse-to-human gap.** The atlas and the rescue experiment are in 5xFAD mice, a familial amyloid model that does not reproduce sporadic human AD (no tau tangles, no human aging vasculature). The import-first ordering is established in mice; in humans it is a hypothesis with a specified test, not a finding.
2. **The human evidence is observational and ambiguous.** Slot et al. (2017) is a cohort study: **association only**. The low-plasma/high-CSF APOA1 pattern fits import failure *and* leak, and the APOE ε4 subgroup estimate (HR 5.0, 95% CI 1.3–18.9) is imprecise. No human study has yet measured import and leak in the same participants over time.
3. **The TXP1 figure is unverified.** The >65-fold delivery gain is a company announcement (ProMIS Neurosciences / Ossianix, 17 November 2026), not a peer-reviewed result; it is used here as a directional claim, and the paper's ranking does not depend on it.
4. **The atlas is a snapshot, not a census.** 861 proteins were tracked; the plasma proteome is larger, and the 92-protein set is a lower bound on import, not a complete inventory. Human BBB transport may route the same proteins differently.
5. **Classical canon consulted second-hand.** The Islamic works cited (Ibn Sina's *Canon*, Al-Ghazali's *Ihya*, Al-Shatibi's *Al-Muwafaqat*) were consulted through the programme's verified canon map and secondary literature, not by a fresh full-text reading of the Arabic originals. The full 23-volume *Kitab al-Hawi* of Al-Razi exists in English only in selections, and Ibn al-Nafis's *Sharh Tashrih al-Qanun* (the pulmonary-circulation commentary) survives in English only in partial translation; most classical Arabic manuscripts remain undigitised in libraries (Süleymaniye, Istanbul; Dar al-Kutub, Cairo; the British Library) with no online copy. These gaps are named, not hidden.
6. **No effect size for the mouse rescue.** The *Cell* paper's abstract reports rescue of astrocytic, synaptic and behavioural deficits without a single headline effect size; we therefore report the rescue qualitatively and do not invent a number for it.
7. **Publication-bias risk in the November window.** Both anchor papers appeared within eight days of this writing (10–11 November 2026); independent replication of the atlas has not yet had time to occur, and the history of BBB research (e.g. the Ontario checklist null replication cited in our method brief) warns that single-centre findings can shrink on replication.

## 6. Policy implications

**Decision-makers:** the Ministry of National Health Services, Regulations & Coordination (Pakistan), through the National Institute of Health (NIH) Islamabad; and the Higher Education Commission (HEC) for research funding. **Exact changes, in order:**

1. **Add the plasma/CSF APOA1 ratio to the national dementia cohort protocol** as a pre-amyloid early-detection marker, alongside — not instead of — amyloid testing, with the CSF:plasma ratio recorded as the import index. Cost: a routine immunoassay, orders of magnitude cheaper than amyloid PET, which is effectively unavailable outside a few centres in Pakistan.
2. **Fund a liver-targeted APOA1 pilot before funding another leak-sealing trial.** Until the human import-first test (Section 4.3) reports, public research money should prioritise the earlier step in the causal chain. If the cohort falsifies import-first, reverse this prioritisation — the falsifier is written into the policy, not added later.
3. **Require target-engagement evidence for publicly funded CNS drug trials:** any central-nervous-system drug seeking HEC/NIH funding must show a CSF:plasma ratio or equivalent brain-exposure measure, so that no trial repeats the error documented in our 2 November paper — testing a drug that never reached its target.

**Islamic principle:** *hifz al-nafs* (preservation of life), one of the five *maqasid al-shariah* (Al-Ghazali, *Al-Mustasfa*; Al-Shatibi, *Al-Muwafaqat*), with *maslaha* (public interest) as the balancing test: the policy counts benefit to the poor and the unborn, not only to those who can reach a PET scanner. Where the modern evidence and the classical principle point the same way — detect early, treat the supplying organ, spend public money on the earliest causal step — we say so; where they diverge, the evidence governs the science and the principle governs the spending priority, and both are stated.

## 7. Conclusion

The blood–brain barrier is not a wall that fails by leaking. It is a supply line that fails by closing: of 861 plasma proteins, only 92 (10.7%) are admitted, and in early Alzheimer's models the admission of liver-derived APOA1 stops before any leak begins. APOA1 is 68 times too large to cross passively, so its entry — and any therapy that restores it — must use a receptor. Restoring the liver's supply rescued the mouse brain. The human record is compatible with this story but cannot yet distinguish import failure from leak, and the paper specifies the cohort that would. The memorable number is **10.7%**: the brain admits one protein in ten from the blood, and Alzheimer's may begin the day that gate starts to close. If the human test confirms it, the cheapest early-detection tool in dementia is already in a routine blood sample, and the most promising therapy may be one that treats the liver to save the brain.

---

## References

1. Zhou H, Maynard JC, Pennacchio AJ, Apolonio A, Liu X, Yao L, Negahban M, Zhang Z, Ding B, Oberhauser J, Wen X, Yang MJ, Huang F, Chayama Y, Doddipalli S, Bernardi M, Domke L, Lo I, Simms J, Pan A, Du S, To NS, Wong PS, Duong D, Fox E, Seyfried NT, Cheung TH, Tracy TE, Burlingame AL, Yang AC. The blood-brain barrier imports diverse neuroprotective proteins through pathways impaired early in Alzheimer's disease models. *Cell*. 2026 Nov 11. doi:10.1016/j.cell.2026.10.039.
2. Walsh AE, Davis BA, Samuels JD, et al. Alzheimer's genetic risk factor CASS4 controls microglial focal adhesion biology and amyloidosis. *J Exp Med*. 2026;223(12):e20260104. doi:10.1084/jem.20260104.
3. Montagne A, Barnes SR, Sweeney MD, et al. Blood-brain barrier breakdown in the aging human hippocampus. *Neuron*. 2015;85(2):296–302. doi:10.1016/j.neuron.2014.12.032. PMID 25611508.
4. Slot RE, Van Harten AC, Kester MI, Jongbloed W, Bouwman FH, Teunissen CE, Scheltens P, Veerhuis R, van der Flier WM. Apolipoprotein A1 in cerebrospinal fluid and plasma and progression to Alzheimer's disease in non-demented elderly. *J Alzheimers Dis*. 2017;56(2):687–697. doi:10.3233/JAD-151068. PMID 28035918.
5. Soto-Faguás CM, et al. Mouse APOE Christchurch protects against Aβ-induced tau and α-synuclein aggregation. *Cell Reports*. 2026. doi:10.1016/j.celrep.2026.118301.
6. Ali Z. The blood–brain barrier gap: why first-generation GLP-1 receptor agonists failed in Parkinson's disease, and the penetrance-and-enrichment trial that could settle it. Daily Research Papers, Brain track, Paper #2. 2 Nov 2026. (Descriptor table: peptide GLP-1 RAs meet 0 of 4 CNS-likeness criteria.)
7. ProMIS Neurosciences Inc. ProMIS Neurosciences licenses next-generation TXP1 brain-selective shuttling technology from Ossianix. GlobeNewswire press release. 17 Nov 2026. (Company announcement; >65-fold preclinical brain-delivery gain — not peer-reviewed.)
8. UniProt Consortium. Apolipoprotein A-I, human (APOA1_HUMAN, P02647). Reviewed entry: 267 amino acids, 30,778 Da. Accessed 18 Nov 2026 via UniProt REST API. https://rest.uniprot.org/uniprotkb/P02647.txt
9. Ibn Sina (Avicenna). *Al-Qanun fi al-Tibb* (Canon of Medicine). c. 1025. Book I (general principles; the faculties and the interdependence of organs, liver as seat of the natural faculty, brain as seat of the psychic faculty). Consulted via the programme's verified canon map; full Arabic text not re-read for this paper.
10. Al-Ghazali. *Ihya Ulum al-Din* (Revival of the Religious Sciences). c. 1096–1106. (The heart as ruler of the body, dependent on the soundness of its members.) Consulted via the programme's verified canon map.
11. Al-Ghazali. *Al-Mustasfa*. (Definition of the five objectives of the Shariah, *maqasid*, including *hifz al-nafs*, preservation of life.)
12. Al-Shatibi. *Al-Muwafaqat fi Usul al-Shari'a*. d. 1388. (Systematisation of *maqasid al-shariah* and *maslaha*, public interest.)
13. Qur'an 2:30. (Human beings as stewards, *khilafah*, on earth — cited for the stewardship/trust framing of the body and its organs.)

## Data availability

All numbers in this paper trace to a real source: the *Cell* atlas counts (861 tracked, 191 sampled, 92 admitted) to Zhou et al. (2026), verified via Crossref on 18 Nov 2026; the human APOA1 effect sizes to Slot et al. (2017), abstract retrieved from PubMed (PMID 28035918); the CASS4 findings to Walsh et al. (2026), DOI 10.1084/jem.20260104; the leak-model citation to Montagne et al. (2015), PMID 25611508; the APOA1 size (267 AA, 30,778 Da) to UniProt P02647, retrieved 18 Nov 2026; the TXP1 >65-fold figure to the ProMIS/Ossianix press release of 17 Nov 2026, labelled as a company announcement. No new dataset was generated. The literature sweep log (PubMed E-utilities queries, Crossref check, news sweep) and the UniProt retrieval are retained with this paper's run record in the goal's hidden_files. The daily research digest series ends 14 Nov 2026, so no fresh digest was available for this run; the targeted checks above substitute for it and are disclosed here.

---

*AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent verification.*
