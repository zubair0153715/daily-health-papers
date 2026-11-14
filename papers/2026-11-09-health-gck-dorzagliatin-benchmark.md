# The Only Approved Drug Scores Worst: Dorzagliatin Binds Weakest on Human Glucokinase 3F9M While Four Nanomolar Activators Lead — A Vina Benchmark That Separates Affinity from Activation

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-09 · **Health Papers Agent — Paper #3** (daily 5-paper run)

**Keywords:** glucokinase; GCK; dorzagliatin; glucokinase activator; type 2 diabetes; molecular docking; AutoDock Vina; allosteric site

---

## Abstract

Type 2 diabetes affected 537 million adults in 2021 and is projected to reach 643 million by 2030, yet glucokinase activators (GKAs) — a mechanistically attractive class — failed repeatedly in trials through hypoglycaemia, hypertriglyceridaemia and fading efficacy, leaving dorzagliatin, approved only in China in 2022, as the sole survivor. We asked whether docking affinity at the glucokinase allosteric site explains that survival, benchmarking dorzagliatin against four nanomolar ChEMBL activators on human glucokinase (PDB 3F9M, 1.5 Å) with AutoDock Vina 1.2.7 under one protocol. The approved drug scored worst: dorzagliatin −6.82 kcal/mol, against −8.47 for CHEMBL3217925 (Kd 2.16 nM), −8.25 for CHEMBL3577729, −7.85 for CHEMBL3577715 and −7.50 for CHEMBL3580737 (Kd 2.93 nM). The 1.65 kcal/mol gap to the best lead sits inside Vina's ±1–2 kcal/mol noise, and the rank correlation between measured potency and docking score was weak (Spearman rho = 0.35, n = 4), with the second-most-potent measured binder ranking last in docking. Affinity therefore does not explain dorzagliatin's clinical success; its published advantage is glucose-dependent activation kinetics, not maximal binding. The falsifiable next step is a recombinant glucokinase activation assay at 3, 5 and 10 mmol/L glucose comparing EC50 and Vmax of CHEMBL3217925 with dorzagliatin: if the lead activates at low glucose like the failed MK-0941, affinity is a liability, not a lead.

---

## 1. Introduction

Diabetes affected an estimated 537 million adults aged 20–79 in 2021, projected to rise to 643 million by 2030 (IDF Diabetes Atlas, 10th edition). In Pakistan the burden is among the highest in the world, with roughly one in four adults living with diabetes, and most patients are treated with drugs that do not restore the body's own glucose sensing. Glucokinase (GCK, hexokinase-4) is the glucose sensor of the pancreatic beta cell and a rate-limiting step in hepatic glucose metabolism: its low affinity for glucose (S0.5 ~7 mmol/L) sets the threshold at which insulin is released. Human genetics proves the target matters in both directions — inactivating GCK mutations cause maturity-onset diabetes of the young (GCK-MODY), while activating mutations cause hyperinsulinaemic hypoglycaemia.

Small-molecule glucokinase activators (GKAs) therefore looked like a rational, disease-modifying therapy. Instead the class became a cautionary tale. Most GKAs failed in clinical trials because of clinically significant hypoglycaemia, raised blood triglycerides, or a decline in HbA1c-lowering efficacy within 30 weeks. A 2023 meta-analysis of 13 randomised trials (2,748 GKA-treated and 2,681 control participants) found only a modest HbA1c advantage (weighted mean difference −0.339%) against a significant triglyceride rise (+0.322 mmol/L, p = 0.001) and a non-significant hypoglycaemia signal (odds ratio 1.448). Merck's MK-0941, the best-characterised failure, lost glycaemic efficacy after 12 weeks and accumulated hypoglycaemia and hypertriglyceridaemia by 30 weeks.

Dorzagliatin (HMS5552, HuaTangNing) is the single exception: a dual-acting, allosteric, full glucokinase activator targeting pancreatic and hepatic enzyme, approved in China in September 2022 as monotherapy and as add-on to metformin — the first GKA approved anywhere. In the 52-week SEED phase 3 trial (463 drug-naive patients, NCT03173391) it reduced HbA1c by 1.07% at 24 weeks with no severe hypoglycaemia; in DAWN (767 patients inadequately controlled on metformin, NCT03171545) the HbA1c reduction was −1.02% versus −0.36% on placebo (estimated treatment difference −0.66%). Its observational extension, DREAM, reported a 65.2% diabetes remission rate (95% CI 53.4–77.0) after 52 weeks drug-free in 69 patients who had achieved control on dorzagliatin. A 2025 mechanistic study showed why: dorzagliatin binds preferentially to the closed form of glucokinase, interacting mainly with Arg63, and only mildly stimulates insulin secretion at low glucose — whereas MK-0941 is 10- to 100-fold more potent at 3–5 mmol/L glucose, maximally stimulates secretion at low glucose, and stresses the beta cell.

That mechanism raises a sharp, testable question: does binding affinity at the allosteric site predict anything about a GKA at all? **Hypothesis: dorzagliatin's Vina docking affinity at the glucokinase allosteric site will be weaker than that of more potent measured ChEMBL activators, because its clinical advantage is kinetic (glucose-dependent activation), not affinity.**

## 2. Methods

### 2.1 Literature basis

PubMed, ChEMBL and the daily research digest were searched on 2026-11-09 for dorzagliatin, glucokinase activators, SEED/DAWN/DREAM, MK-0941 and GKA meta-analyses. Only verified sources are cited; every trial number, HbA1c value and mechanistic claim below traces to a named publication or registry record.

### 2.2 Molecular docking

Target identification used UniProtKB (human glucokinase, P35557, hexokinase-4, 465 amino acids) and ChEMBL (CHEMBL3820, hexokinase-4, single protein, human; 45 bioactivities retrieved, 26 leads ranked by a composite of Morgan-fingerprint similarity to dorzagliatin, Lipinski/Veber drug-likeness, PAINS cleanliness and a Tox21 k-nearest-neighbour read-across panel). The reference drug dorzagliatin was verified against PubChem (CID 57920094; C22H27ClN4O5; MW 462.93; logP 2.05). Docking used AutoDock Vina 1.2.7 against the experimental structure PDB 3F9M (human pancreatic glucokinase in complex with glucose and an allosteric activator, 1.5 Å), with a 22.5 Å box, exhaustiveness 8, and the best of three poses reported for each compound. The grid centre was audited from the PDB file itself: centre [−9.53, 2.78, 20.65] lies 0.01 Å from the centroid of the co-crystallised allosteric activator MRK (23 atoms) and 19.63 Å from the glucose centroid — the grid is on the allosteric pocket, not the glucose site. The top four ChEMBL leads by composite score plus dorzagliatin were docked under the identical protocol.

### 2.3 PAINS screen

All five docked compounds were screened with the RDKit PAINS filter. Dorzagliatin and all four leads were PAINS-clean.

### 2.4 Honesty limits

Docking estimates binding free energy at one static structure; it does not measure enzyme activation, which is the pharmacology that matters for a GKA. Vina carries ±1–2 kcal/mol noise, so differences below ~2 kcal/mol are not claims of superiority. No molecular dynamics, no free-energy refinement and no laboratory data were generated. ChEMBL potency values mix Kd and EC50 assay types and are compared as reported pChEMBL values.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Measured potency (ChEMBL) | Best Vina affinity (kcal/mol) | Poses (kcal/mol) | PAINS |
|---|---|---|---|---|
| CHEMBL3217925 | Kd 2.16 nM (pChEMBL 8.67) | **−8.47** | −8.47, −8.37, −8.35 | none |
| CHEMBL3577729 | EC50 6.0 nM (pChEMBL 8.22) | −8.25 | −8.25, −8.25, −7.46 | none |
| CHEMBL3577715 | EC50 6.0 nM (pChEMBL 8.22) | −7.85 | −7.85, −7.81, −6.90 | none |
| CHEMBL3580737 | Kd 2.93 nM (pChEMBL 8.53) | −7.50 | −7.50, −7.15, −7.09 | none |
| Dorzagliatin (QUERY) | Approved drug; no ChEMBL-registered GCK EC50 in the retrieved set | −6.82 | −6.82, −6.76, −6.54 | none |

Dorzagliatin scored worst of the five, 1.65 kcal/mol behind the best lead — a gap inside Vina noise. All four leads are drug-like (MW 427.5–515.7; logP 2.98–4.38; 0–1 Lipinski violations; all Veber-pass) and share a pyrazole-carboxamide core. Their Tox21 read-across maxima were low (0.17–0.40 across 12 assays; highest single value NR-ER 0.40 for CHEMBL3580737); dorzagliatin's maximum was 0.283 (NR-ER). Pose consistency was tight for dorzagliatin (spread 0.28 kcal/mol) and for the best lead (0.12 kcal/mol), so the ranking is not a single-pose artefact.

The rank correlation between measured potency and docking score across the four ChEMBL leads was weak (Spearman rho = 0.35, n = 4). The sharpest inversion: CHEMBL3580737, the second-most-potent measured binder (Kd 2.93 nM, pChEMBL 8.53), ranked last in docking (−7.50), while CHEMBL3217925, the most potent measured binder (Kd 2.16 nM), ranked first (−8.47).

### 3.2 Comparison with published docking

No published Vina benchmark of dorzagliatin against ChEMBL glucokinase activators on 3F9M was found; the comparison here is original. The structural literature instead explains the result mechanistically: dorzagliatin's advantage is that it binds the closed form of glucokinase with a low open-to-closed energy barrier and only mildly stimulates secretion at low glucose, while MK-0941 binds the hinge pocket, interacts strongly with the Tyr214 phenyl ring, creates a high-energy barrier, and maximally stimulates secretion at low glucose.

### 3.3 The standardisation / quality problem

The DREAM remission figure (65.2%) is the most over-readable number in the dorzagliatin literature: it comes from a 69-patient observational, non-interventional extension of SEED, in Chinese patients only, with diet and exercise adherence required and no control arm. It is a hypothesis about disease modification, not proof of it. Likewise, all phase 3 efficacy data are from Chinese populations; no FDA or EMA approval exists, and the class-wide triglyceride signal (+0.322 mmol/L in meta-analysis) has not been excluded for dorzagliatin over longer horizons.

## 4. Discussion

### 4.1 The reframe

The benchmark reframes the GKA lead-optimisation question. If the only approved drug in the class is also the weakest binder in its own benchmark, then maximising allosteric-site affinity is the wrong objective function. Dorzagliatin is a full activator — it raises Vmax — and its clinical edge is kinetic selectivity: mild stimulation at 3 mmol/L glucose, real stimulation at 10 mmol/L. A lead that binds tighter but activates at low glucose repeats MK-0941, whose 10- to 100-fold potency advantage at low glucose was precisely what made it fail. CHEMBL3217925, the best binder here, is therefore a candidate for a kinetic test, not a victory lap.

### 4.2 Why the "win" must not be over-read

No lead beats dorzagliatin beyond Vina noise: the largest gap, 1.65 kcal/mol, is inside the ±1–2 kcal/mol band, and the other three gaps (0.68–1.43 kcal/mol) are smaller still. The Spearman correlation of 0.35 on four compounds is weak and underpowered; with n = 4 it is descriptive, not inferential. The structure is a single closed, activator-bound conformation (3F9M), which should, if anything, favour dorzagliatin's closed-form binding — and it still scored worst, which strengthens the qualitative point but does not quantify it. ChEMBL potencies mix Kd and EC50 readouts from different assay designs.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

All five compounds are PAINS-clean, so no redox-cycling or aggregation artefact is expected to contaminate the proposed activation assay. The real artefact risk for GKAs is different: hepatic lipogenesis. Preclinical GKAs induced hepatic steatosis in diabetic mice within days at pharmacological doses, a target-mediated class warning. Any validation of CHEMBL3217925 must therefore read out triglyceride synthesis alongside glucose lowering, or it will repeat the class's blind spot.

### 4.4 Testable hypotheses

1. CHEMBL3217925 activates recombinant human glucokinase with a lower EC50 than dorzagliatin at 10 mmol/L glucose but a higher activation ratio at 3 mmol/L glucose (i.e. it behaves like MK-0941, not dorzagliatin) — measurable in the NADP+-coupled assay at 3, 5 and 10 mmol/L glucose.
2. Dorzagliatin's Vmax increase exceeds that of CHEMBL3217925 despite weaker binding — measurable as the maximal activity ratio in the same assay.
3. CHEMBL3580737, the docking worst-performer among the leads despite Kd 2.93 nM, shows the weakest functional activation of the four — testing whether Vina or the binding assay is the misleading readout.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): recombinant wild-type human glucokinase NADP+/glucose-6-phosphate-dehydrogenase coupled assay at 3, 5 and 10 mmol/L glucose for dorzagliatin, MK-0941 (positive control for low-glucose over-activation) and CHEMBL3217925; readouts EC50, S0.5 shift and Vmax change. Stage 2 (weeks 4–7): human or rat islet perifusion, glucose-stimulated insulin secretion at 3 and 16.7 mmol/L glucose, comparing the same three compounds. Stage 3 (weeks 8–12): rat hepatocyte glycogen synthesis and triglyceride accumulation, to test the lipogenesis warning before any animal efficacy work. A lead passes only if it matches dorzagliatin's glucose-dependence and does not raise hepatocyte triglycerides.

## 5. Limitations

1. Docking only: no enzyme, islet or animal data; affinity is not activation.
2. Vina noise ±1–2 kcal/mol exceeds every gap reported; no lead is claimed superior to dorzagliatin.
3. Single structure (3F9M, closed conformation); no apo or open-form comparison, no molecular dynamics.
4. Spearman correlation on n = 4 is descriptive; no p-value is claimed.
5. No ChEMBL-registered GCK EC50 for dorzagliatin was present in the retrieved activity set, so dorzagliatin enters the correlation only as the clinical reference, not as a data point.
6. ChEMBL potencies mix Kd and EC50 assay types.
7. All phase 3 data are from Chinese populations; no FDA/EMA approval; no Pakistan-specific data.
8. The DREAM remission figure is observational (n = 69) and must not be quoted as efficacy.

## 6. Conclusion

On human glucokinase 3F9M, dorzagliatin — the only approved glucokinase activator — docked weakest (−6.82 kcal/mol) while four nanomolar ChEMBL activators led, the best by 1.65 kcal/mol, inside Vina noise and with only weak rank agreement to measured potency (Spearman rho = 0.35). The result supports the published mechanistic account that dorzagliatin's success is kinetic, not affinity-driven, and it sets the validation bar for any new lead: glucose-dependent activation at 3, 5 and 10 mmol/L glucose, with a triglyceride readout, before any claim of improvement over dorzagliatin.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received; all computation used free-tier public resources.

## References

1. International Diabetes Federation. IDF Diabetes Atlas, 10th edition. Brussels: IDF; 2021. 537 million adults with diabetes in 2021, projected 643 million by 2030.
2. Dorzagliatin in drug-naive patients with type 2 diabetes: a randomized, double-blind, placebo-controlled phase 3 trial (SEED). Nat Med. 2022;28(5):965–973. ClinicalTrials.gov NCT03173391.
3. Dorzagliatin as add-on therapy to metformin in type 2 diabetes (DAWN). ClinicalTrials.gov NCT03171545. HbA1c −1.02% vs −0.36% placebo at 24 weeks; estimated treatment difference −0.66%.
4. Dorzagliatin diabetes remission study (DREAM), extension of SEED. ClinicalTrials.gov NCT03141073. 65.2% remission (95% CI 53.4–77.0) after 52 weeks drug-free, n = 69.
5. Roman et al. Functional and mechanistic explanation for the unique clinical success of the glucokinase activator dorzagliatin in the treatment of type 2 diabetes. Diabetes. 2025;74(8). doi:10.2337/db25-0066. PMCID: PMC12278794.
6. Glucokinase activators: a humbling lesson in drug development. Diabetes. 2025;74(8):1339–1341.
7. Evaluation of efficacy and safety of glucokinase activators — a systematic review and meta-analysis. Front Endocrinol. 2023;14:1175198. doi:10.3389/fendo.2023.1175198. PMCID: PMC10200948.
8. Advances in treatments for type 2 diabetes: first China and then the rest of the world. Nature. 2025. Dorzagliatin approved in China September 2022; included in China's National Reimbursement Drug List from 1 January 2024.
9. Dorzagliatin, a dual-acting glucokinase activator, increases insulin secretion and glucose sensitivity in glucokinase maturity-onset diabetes of the young and recent-onset type 2 diabetes. Diabetes. 2023. PMID: 36342518.
10. Effects of dorzagliatin, a glucokinase activator, on alpha- and beta-cell function in individuals with impaired and normal glucose tolerance. Diabetes. 2025;74(11):2111–2122. doi:10.2337/db24-1130. PMID: 40896829.
11. Safety, tolerability, pharmacokinetics, and pharmacodynamics of novel glucokinase activator HMS5552: results from a first-in-human single ascending dose study. Drug Des Devel Ther. 2016. doi:10.2147/dddt.s105021. PMID: 27274195.
12. Glaser et al. Familial hyperinsulinism caused by an activating glucokinase mutation. N Engl J Med. 1998;338:226–230.
13. RCSB Protein Data Bank. 3F9M: Human pancreatic glucokinase in complex with glucose and activator showing a mobile flap. Deposited 14 November 2008; resolution 1.5 Å.
14. ChEMBL. Hexokinase-4 (CHEMBL3820) bioactivities and compound records (CHEMBL3217925, CHEMBL3577715, CHEMBL3577729, CHEMBL3580737). Accessed 2026-11-09. https://www.ebi.ac.uk/chembl
15. PubChem. Dorzagliatin, CID 57920094. https://pubchem.ncbi.nlm.nih.gov/compound/57920094

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-007-2026-11-09.json`; no additional data were generated. Target: UniProt P35557, ChEMBL CHEMBL3820. Structure: PDB 3F9M. Reference drug: dorzagliatin, PubChem CID 57920094. Docking centre [−9.53, 2.78, 20.65] audited against the 3F9M PDB file (0.01 Å from the MRK activator centroid).
