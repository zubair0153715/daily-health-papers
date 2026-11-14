# Thymoquinone as a Putative Aldose Reductase Inhibitor for Diabetic Complications: A Computational Lead, a PAINS Caveat, and a Testable Assay Proposal

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2 November 2026 · **Paper #1 — Health track** (Daily Research Papers)

**Keywords:** thymoquinone; *Nigella sativa*; aldose reductase; polyol pathway; diabetic complications; molecular docking; PAINS; standardisation

---

## Abstract

Thymoquinone (TQ), the marker quinone of *Nigella sativa* (black seed, kalonji), is widely used in Pakistan as an adjunct for diabetes, yet meta-analyses report only a modest HbA1c reduction (~−0.54%) with very high heterogeneity (I² 94–99%). A major confounder is product quality: published assays show TQ content varying ~260-fold across commercial products (3.08–809.4 mg/100 g). We performed standardised AutoDock Vina docking of TQ against five diabetes-related targets, each against its reference drug under an identical protocol. TQ was weaker than the reference on four targets (DPP-4, PPAR-γ, PTP1B, pancreatic α-amylase) but outscored the reference drug epalrestat on aldose reductase (PDB 1US0): −7.27 vs −6.48 kcal/mol, consistent across all three top poses. Aldose reductase is the rate-limiting enzyme of the polyol (sorbitol) pathway and a driver of diabetic neuropathy, retinopathy and cataract — not of glucose lowering. We therefore reframe the hypothesis: if TQ has a specific antidiabetic action, it is more plausibly directed at diabetic *complications* than at glycaemic control. This interpretation is sharply limited by two facts: (i) the 0.79 kcal/mol margin lies inside Vina's ±1–2 kcal/mol scoring noise, so docking alone cannot confirm the lead; and (ii) TQ is a quinone and a classic PAINS (pan-assay interference) scaffold whose redox-cycling can generate false-positive activity in vitro. We propose a falsifiable two-stage validation: (1) HPLC standardisation of ten Pakistani-market kalonji oils, and (2) an in-vitro aldose-reductase inhibition (IC50) assay of the standardised samples against epalrestat, with redox controls (catalase, DTT) to expose PAINS artefacts. Either outcome — confirmation or refutation — is publishable.

---

## 1. Introduction

Pakistan carries one of the world's heaviest diabetes burdens: roughly 34.5 million adults live with diabetes, a prevalence near 30.8%, with an estimated 9.3 million cases undiagnosed. Diabetic complications — neuropathy, retinopathy, nephropathy and cataract — rather than hyperglycaemia itself, account for most of the morbidity, and their management remains inadequate in resource-constrained settings.

*Nigella sativa* (kalonji, black seed) is among the most widely used traditional adjuncts for diabetes in Pakistan. Its marker compound thymoquinone (2-isopropyl-5-methyl-1,4-benzoquinone; TQ) has reported antioxidant and anti-inflammatory activity, and a substantial in-vitro literature claims activity against a striking range of targets — diabetes, cancer, bacteria, inflammation. Yet the clinical literature is contradictory: meta-analyses of randomised trials report only a modest HbA1c reduction of ~−0.54%, with very high heterogeneity (I² 94–99%) and low certainty. Two under-examined confounders may explain the contradiction. First, product quality: a Swiss HPLC screening of commercial *N. sativa* products found TQ content ranging from 3.08 to 809.4 mg/100 g — a ~260-fold range — and a Malaysian survey found 0.07–1.88% TQ; most trials neither standardised nor even assayed TQ content, and no pharmacopeial monograph dose exists for diabetes. Second, chemistry: TQ is a quinone, a classic PAINS scaffold whose redox-cycling and Michael-acceptor reactivity can produce apparent activity against many targets in vitro without specific pharmacology.

This paper reports a standardised computational screen of TQ against five diabetes-related targets and uses the single positive signal — aldose reductase — to formulate a narrow, falsifiable hypothesis and a concrete validation plan. The aim is not to claim efficacy, but to redirect the research question from "does black seed lower sugar?" (weak evidence, wrong target class) to "does standardised TQ inhibit aldose reductase, and would that matter for complications?" (testable, specific, and consistent with the data).

## 2. Methods

### 2.1 Literature basis

The clinical and standardisation claims in this paper are drawn from a systematic review of 36 sources compiled 20 October 2026 (internal report: Black Seed — Kalonji: Hadith, Frequency Healing; full source list in the data-availability note). Key external sources are cited in the References.

### 2.2 Molecular docking

Docking was performed 20 October 2026 with AutoDock Vina 1.2.7 using the LeadForge pipeline protocol: for each target, TQ and the reference drug were docked into the same binding site with the same protocol (same PDB structure, same grid centre, same exhaustiveness). Structures were retrieved from the RCSB Protein Data Bank. Affinities are reported as the best of three poses (kcal/mol); the full pose lists are in the raw data files. Vina's scoring noise is approximately ±1–2 kcal/mol; differences smaller than this cannot be treated as significant on scores alone.

### 2.3 PAINS screen

TQ was screened with RDKit for PAINS (pan-assay interference) substructures. Quinone redox-cycling and Michael-acceptor reactivity were assessed against the PAINS literature (Baell & Holloway, 2010).

### 2.4 Honesty limits

This is a computational, hypothesis-generating study. No wet-lab data are presented. No clinical claim is made. Docking affinity is not enzyme inhibition, and a docking "win" is not evidence of efficacy.

## 3. Results

### 3.1 Docking: four losses, one lead

| Target | PDB (resolution) | Thymoquinone (kcal/mol) | Reference drug (kcal/mol) | Verdict |
|---|---|---|---|---|
| DPP-4 | 4A5S (1.62 Å) | −3.75 | Sitagliptin −5.85 | TQ far weaker |
| PPAR-γ | 9F7W (1.25 Å) | −6.47 | Pioglitazone −8.98 | ~2.5 kcal/mol behind |
| PTP1B | 9C66 (1.40 Å) | −5.42 | Ursolic acid −6.10 | Weaker, moderate |
| Pancreatic α-amylase | 5U3A (0.95 Å) | −5.80 | Acarbose −6.40 | Close but behind |
| **Aldose reductase** | **1US0 (0.66 Å)** | **−7.27** | **Epalrestat −6.48** | **TQ outscores reference — only win** |

The aldose-reductase result was consistent across poses: TQ's three top poses scored −7.27, −7.24 and −7.15 kcal/mol, while epalrestat's scored −6.48, −6.38 and −5.98 — every TQ pose beat every epalrestat pose. No other target showed this pattern.

### 3.2 Comparison with published docking

Published docking claims for TQ are weaker than our screen suggests for the glucose targets: literature reports TQ–PPAR-γ at −5.7 and TQ–DPP-IV at −6.3 kcal/mol, and a TQ PPAR-γ Ki of 7.43 µM versus 0.13 µM for pioglitazone (~57-fold weaker). Our DPP-4 result (−3.75) did **not** replicate the published −6.3 claim. Purified TQ at 50 µM was previously reported inactive against α-glucosidase. These comparisons reinforce that TQ is not a convincing direct inhibitor of the glucose-lowering targets.

### 3.3 PAINS alert

RDKit flags TQ as PAINS-positive. As a quinone, TQ redox-cycles and can react with proteins as a Michael acceptor. This predicts exactly the published picture — apparent activity against many unrelated targets in vitro — and means any in-vitro "hit" for TQ must be treated as guilty until proven innocent. Notably, berberine (a comparator in the same review) carries no PAINS alert, and its evidence base is pharmacologically cleaner. TQ's acute toxicity is strongly route-dependent (oral LD50 ~2.4 g/kg versus i.p. 57.5 mg/kg), consistent with reactive-quinone handling.

### 3.4 The standardisation problem

Commercial TQ content varies ~260-fold (3.08–809.4 mg/100 g; Malaysian survey 0.07–1.88%). Two capsules labelled identically can therefore deliver pharmacologically trivial or substantial TQ. No published study has characterised TQ content in Pakistani-market kalonji oils. Any trial that does not assay TQ content is, in effect, testing an unknown dose.

## 4. Discussion

### 4.1 The reframe: complications, not glucose

Aldose reductase catalyses the first, rate-limiting step of the polyol pathway, converting glucose to sorbitol; under hyperglycaemia its flux rises sharply, driving osmotic and oxidative injury in nerve, retina and lens. Its inhibitors (epalrestat is the marketed reference) are complication-directed drugs, not glucose-lowering agents. Our docking therefore points, if it points anywhere, at diabetic complications — neuropathy, retinopathy, cataract — and not at HbA1c. This reframe is consistent with TQ's established antioxidant profile (oxidative stress is central to polyol-pathway injury) and with the clinical observation that TQ's glucose effect is modest at best.

### 4.2 Why the "win" must not be over-read

The margin is 0.79 kcal/mol. Vina's noise is ±1–2 kcal/mol. On scores alone, the result is **not significant** — it is a lead, not a finding. What makes it worth pursuing is the conjunction of three things: (i) pose-level consistency (all TQ poses beat all epalrestat poses), (ii) target coherence (the one win is the one target whose biology matches TQ's antioxidant profile and the complications burden), and (iii) falsifiability (a single enzyme assay settles it). Docking is triage: it tells the laboratory which experiment to run first.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

A PAINS-positive compound can still be a real inhibitor — the alert means the assay must be designed to catch artefacts, not that the compound is inactive. The validation assay must therefore include redox controls (catalase, DTT) and detergent controls; a TQ effect that vanishes under those controls is an artefact, and reporting that is as valuable as a positive result.

### 4.4 Testable hypotheses

- **H1 (adjunct metabolic):** standardised TQ (≥95% purity, HPLC-verified), at a 2 g/day seed-equivalent dose alongside metformin, lowers HbA1c ≥0.4% more than placebo over 12–24 weeks. Falsified if the difference is <0.3% or non-significant.
- **H2 (mechanism is indirect):** TQ's glucose effect is not direct DPP-4/α-glucosidase inhibition but oxidative-stress reduction and beta-cell protection. Predicts in-vitro enzyme IC50 >100 µM for those targets, with Nrf2/ARE activation in cell models.
- **H3 (PAINS promiscuity):** TQ's in-vitro multi-target hits diminish or disappear when redox/detergent controls are added.
- **H4 (standardisation is the real problem):** the ~260-fold market TQ variance explains much of the contradiction in clinical trials. Test: HPLC assay of ten Pakistani-market kalonji oils.

### 4.5 Proposed validation (two stages, university-lab feasible, 8–12 weeks)

**Stage 1 — standardisation:** purchase ten kalonji oil products from the Pakistani market; quantify TQ by HPLC against a reference standard; report the range and the fraction below any plausible active threshold.
**Stage 2 — enzyme confirmation:** in-vitro aldose-reductase inhibition assay (IC50) of the standardised samples plus a TQ reference standard, with epalrestat as the positive control, replicates, and redox controls. **Confirmation** = reproducible IC50 in a plausible range with the effect surviving redox controls, tracking with measured TQ content. **Refutation** = no inhibition, or an effect abolished by redox controls. Either outcome is a publishable Pharm-D-level finding.

## 5. Limitations

1. Docking only; no experimental data. 2. The aldose-reductase margin is within Vina's noise. 3. No molecular-dynamics refinement or binding-free-energy calculation was performed. 4. The literature synthesis rests on the 36-source review of 20 October 2026 and inherits its limits (including the low certainty of the clinical meta-analyses). 5. No Pakistani-market TQ data exist yet — Stage 1 is itself an untested premise.

## 6. Conclusion

Standardised docking gives thymoquinone one lead and four losses. The lead — aldose reductase, the polyol-pathway enzyme of diabetic complications — reframes the black-seed question from glucose lowering, where the evidence is weak, to complication prevention, where a specific, falsifiable experiment exists. The PAINS alert and the 260-fold product variance do not kill the hypothesis; they dictate the assay design. The next step is not another review but a bench: standardise the product, run the enzyme assay, and let either answer stand.

---

## Acknowledgments

**AI assistance:** This manuscript was drafted with the assistance of an AI research assistant (Lapis, Meta Muse Spark), which also performed the literature searches and docking computations. The author takes responsibility for the content.

## References

1. Screening of thymoquinone content in commercial *Nigella sativa* products (TQ 3.08–809.4 mg/100 g). ResearchGate. https://www.researchgate.net/publication/362959334_Screening_of_Thymoquinone_Content_in_Commercial_Nigella_sativa_Products_to_Identify_a_Promising_and_Safe_Study_Medication
2. *Nigella sativa* safety, CYP interactions and regulatory status. PMC. https://pmc.ncbi.nlm.nih.gov/articles/PMC10886913/
3. *Nigella sativa* and thymoquinone: nutrition, bioactivity and safety review. *Frontiers in Nutrition* 2023;10:1126272. https://www.frontiersin.org/articles/10.3389/fnut.2023.1126272/full
4. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model.* 2021;61(8):3891–3898.
5. Baell JB, Holloway GA. New substructure filters for removal of pan assay interference compounds (PAINS) from screening libraries and for their exclusion in bioassays. *J Med Chem.* 2010;53(7):2719–2740.
6. RCSB Protein Data Bank entries 1US0 (aldose reductase), 4A5S (DPP-4), 9F7W (PPAR-γ), 9C66 (PTP1B), 5U3A (pancreatic α-amylase). https://www.rcsb.org/
7. Ali Z, et al. Black Seed (Kalonji): Hadith, Frequency Healing — systematic review of 36 sources. Internal report, 20 October 2026. (Clinical HbA1c and heterogeneity figures; market-variance synthesis.)
8. Ali Z. Diabetes in Pakistan: situation and solutions. Internal report, 26 October 2026. (Pakistan diabetes burden figures.)

## Data availability

Docking inputs, raw results and pose lists: `~/workspace/black-seed-project/dock_results.json`, `dock_results2.json` (AutoDock Vina 1.2.7, 20 Oct 2026). Hypothesis and experiment notes: `HYPOTHESIS-AND-EXPERIMENT.md` in the same directory. Concept note for the university-lab validation: `CONCEPT-NOTE-university-lab.md`. No new experimental data are presented in this draft.
