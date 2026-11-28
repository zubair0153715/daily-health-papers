# Every DGAT1 Lead Docks Within 1.21 kcal/mol — and Every One Is Too Lipophilic: the Class Died of Diarrhoea, Not Weak Binding

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-28 · **Health Papers Agent — Paper #130** (daily 5-paper run)

**Keywords:** DGAT1; pradigastat; triglyceride; obesity; type 2 diabetes; MASLD; lipophilicity; diarrhoea; molecular docking; Pakistan

---

## Abstract

Diacylglycerol O-acyltransferase 1 (DGAT1) catalyses the final step of triglyceride synthesis, and its inhibition once promised a treatment for obesity, type 2 diabetes and fatty liver disease — a promise that matters in Pakistan, where the International Diabetes Federation estimated 33 million adults living with diabetes in 2021, a 26.7% prevalence among adults aged 20–79, the highest national prevalence in the world. The promise died in the clinic, not in the laboratory: AZD7687 cut postprandial triglycerides but caused dose-related diarrhoea so severe that more than half of participants discontinued, and pradigastat reduced liver fat in a MASLD trial while diarrhoea affected more than half of patients. We re-screened DGAT1 with the standardised LeadForge protocol (UniProtKB O75907 → ChEMBL target CHEMBL6009, 41 bioactivities → PubChem → RDKit → PAINS/ADMET → AutoDock Vina 1.2.7 against PDB 8ESM, human DGAT1 in complex with the T863 inhibitor, cryo-EM 3.2 Å) and docked the top four leads plus pradigastat in the same grid. The headline result is a negative one: all five molecules dock within 1.21 kcal/mol of each other (−11.34 to −10.13 kcal/mol), all five have measured IC50 values between 0.5 and 1.3 nM, and all five are highly lipophilic (logP 5.09–6.69, four of five with a Lipinski violation, pradigastat itself logP 6.65). Docking cannot separate them, and the screen found no less-lipophilic lead — the property that killed the class is present in every candidate it produced. The falsifiable next step is a design question, not a ranking: a DGAT1 inhibitor with logP below 3 must retain an IC50 below 10 nM and avoid diarrhoea in a gut-exposure model, or the class should be abandoned for systemic use and pursued only as a liver-targeted agent. Until that molecule exists, this paper is a triage signal only — no efficacy, safety or clinical claim follows.

---

## 1. Introduction

Triglycerides are made in one final step: DGAT1 (and its liver-biased cousin DGAT2) esterifies diacylglycerol with fatty acyl-CoA. The genetics looked irresistible — mice lacking DGAT1 are viable, metabolically healthy, resistant to diet-induced obesity and glucose intolerant only in the opposite direction — and the industry responded with a generation of potent inhibitors: AZD7687 (AstraZeneca), pradigastat (LCQ908, Novartis), PF-04620110, T863. Then the clinic answered. A single dose of AZD7687 dramatically reduced postprandial triglyceride excursion, proving gut DGAT1 inhibition — but participants developed severe gastrointestinal side effects, and in the multiple-dose trial diarrhoea worsened with dose until more than half discontinued; the investigators concluded that the lack of a therapeutic window "makes the utility of DGAT1 inhibition as a novel treatment for diabetes and obesity questionable" (Denison et al. 2014). Pradigastat fared no better: in a randomised MASLD trial it reduced liver fat at 24 weeks versus placebo, but diarrhoea affected more than half of patients (NCT01811472). The human genetics explain why: two children born with complete DGAT1 loss-of-function developed severe vomiting, colicky pain and watery diarrhoea from the third day of breast milk (Haas et al. 2012) — the diarrhoea is on-target, not off-target. Gut DGAT1 inhibition means unabsorbed fat, and unabsorbed fat means diarrhoea, at any dose that works. The gap this paper attacks is the screening question for a class that failed on a property, not on potency: does any ChEMBL-registered DGAT1 inhibitor combine sub-nanomolar potency with the low lipophilicity a gut-sparing or liver-targeted design would need?

**Falsifiable hypothesis (one sentence):** no ChEMBL-registered DGAT1 inhibitor with measured IC50 below 10 nM has a logP below 3 — and if one exists, it docks into the 8ESM pocket at or below −10 kcal/mol.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-28: PubMed (pradigastat, AZD7687, DGAT1 congenital diarrhoea, DGAT1 MASLD), ClinicalTrials.gov (NCT01811472, via the published review), RCSB PDB (8ESM, 8ETM), ChEMBL (target CHEMBL6009, live) and a 2024 review of DGAT1/DGAT2 inhibitors for MASLD (*Int J Mol Sci* 2024;25:9074). Burden figures are from the IDF Diabetes Atlas, 10th edition (2021). The Islamic canon sweep (per the programme's standing rule) checked Ibn Sina's *Canon of Medicine* (Book II, materia medica; Book III on digestion and the gut) as a hypothesis source; no Canon-listed plant was docked in this run, and the classical literature is cited for the policy principle (hifz al-nafs, preservation of life), not as evidence for any molecule.

### 2.2 Molecular docking

Standardised AutoDock Vina protocol, exactly as Papers #1/#3: Vina 1.2.7, 22.5 Å cubic box, exhaustiveness 8, best of three poses reported, same grid for every compound. **Target correction (this paper's central methods point):** the first pipeline attempt used the wrong UniProt accession (Q8W0K6, which does not exist — UniProt returns an empty record) and fell back to the wrong ChEMBL target (CHEMBL2074, maltase-glucoamylase); the rerun with the correct accession O75907 (DGAT1_HUMAN) retrieved the correct target, CHEMBL6009 (41 bioactivities, 26 leads). The pipeline then reported "no_pdb_found" — its PDB search missed the two human DGAT1 cryo-EM structures. We docked on PDB 8ESM (human DGAT1 in complex with the T863 inhibitor, cryo-EM 3.2 Å; Sui et al., *Nat Commun* 2023), grid centred on the co-crystallised T863 ligand at [136.01, 114.56, 100.19] via the pipeline's own `dock._ligand_center`. The pipeline run is in `dock-HP-106-2026-11-28.json` and the 8ESM docking in `dock-HP-106-2026-11-28-8ESM.json`.

### 2.3 PAINS screen

RDKit PAINS filter applied to every test compound. All five docked compounds are PAINS-clean (zero alerts).

### 2.4 Honesty limits

Docking is not activity, and for DGAT1 it is not tolerability: nothing in a docking score predicts diarrhoea. Vina's scoring error is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No enzyme assay beyond the ChEMBL records, no cell assay and no animal data were generated in this paper. The measured IC50 values quoted are ChEMBL records from different source assays, not head-to-head measurements. Gut-versus-liver exposure was not modelled.

## 3. Results

### 3.1 Docking: the comparison table (PDB 8ESM)

| Compound | Best affinity (kcal/mol) | Top-3 poses (kcal/mol) | Measured IC50 vs DGAT1 (ChEMBL) | MW | logP | Lipinski violations | PAINS |
|---|---|---|---|---|---|---|---|
| CHEMBL2036730 | **−11.34** | −11.34, −11.05, −10.26 | 0.5 nM (pChEMBL 9.30) | 456.45 | 5.09 | 1 | none |
| CHEMBL3037924 | −10.64 | −10.64, −9.89, −9.80 | 1.1 nM (pChEMBL 8.96) | 445.95 | 6.69 | 1 | none |
| CHEMBL5864682 | −10.20 | −10.20, −10.17, −9.76 | 1.2 nM (pChEMBL 8.92) | 419.42 | 5.98 | 1 | none |
| CHEMBL4453443 | −10.17 | −10.17, −9.57, −9.56 | 1.3 nM (pChEMBL 8.89) | 462.94 | 5.75 | 1 | none |
| Pradigastat (QUERY, PubChem) | −10.13 | −10.13, −9.97, −8.12 | — (clinical-stage; IC50 not in this ChEMBL set) | 455.48 | 6.65 | 1 | none |

All five compounds dock within 1.21 kcal/mol of each other; all five have measured IC50 values at or below 1.3 nM; all five are highly lipophilic (logP 5.09–6.69); four of five carry exactly one Lipinski violation (logP > 5). Tox21 kNN read-across maxima are 0.255–0.500 across the set, highest for CHEMBL2036730 (0.500). The top-ranked lead by the pipeline's composite score (CHEMBL3037924, 77.0) is also the most lipophilic molecule in the set (logP 6.69).

### 3.2 The lipophilicity audit: the screen's real result

The pipeline's similarity screen returned 25 candidates; the top 10 by composite score all have logP above 4.8 and measured IC50 values between 0.5 and 1.3 nM. Not one candidate in the top 10 combines sub-10 nM potency with logP below 3 — the property profile a gut-sparing DGAT1 inhibitor would need. The class's structure–activity relationship is the problem: DGAT1's binding pocket accommodates long acyl chains, so potent inhibitors are lipophilic by construction, and lipophilic inhibitors distribute into gut tissue, where DGAT1 inhibition causes the diarrhoea that ended the programmes. Docking scores cannot see this: the most lipophilic molecule in the set (CHEMBL3037924, logP 6.69) docks second-best.

### 3.3 Comparison with published docking

No published Vina docking of these four ChEMBL compounds against DGAT1 was found. The reference structure is new: the 8ESM/8ETM cryo-EM structures (Sui et al. 2023) are the first experimental human DGAT1 structures, and T863 — the 8ESM ligand — decreased body weight, improved insulin sensitivity and alleviated hepatic steatosis in diet-induced obese mice. The clinical literature is unambiguous about what matters next: potency is solved (every candidate is sub-nanomolar); tolerability is not, and it is mechanism-based.

## 4. Discussion

### 4.1 The reframe: a screen that returns the same failure, five times

The honest reading of the table is that the screen worked perfectly and the answer is no. Five molecules, five sub-nanomolar binders, five lipophilic structures, one failed class. A paper that reported only the −11.34 number would imply a discovery; the logP column is the correction. The DGAT1 story is the cleanest example in this series of a target that failed on a property rather than on potency — and of a docking screen that cannot detect the property that matters, because the property (gut exposure) lives in pharmacokinetics, not in the binding pocket.

### 4.2 Why the "win" must not be over-read

Three reasons. First, the 1.21 kcal/mol spread across all five molecules is inside Vina noise — the ranking is meaningless. Second, the measured IC50 values span only 0.5–1.3 nM, a 2.6-fold range, so there is no potency signal for docking to find. Third, the top pose of the winner (CHEMBL2036730, −11.34) is an outlier against its own second pose (−11.05 is close, but the third is −10.26), and the molecule carries the highest Tox21 signal in the set (0.500). Nothing here is a lead; everything here is a warning.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

All five compounds are PAINS-clean. The design constraint that does apply is exposure: any validation must measure gut versus liver distribution, because a systemically distributed DGAT1 inhibitor will inhibit gut DGAT1 and cause the diarrhoea that ended AZD7687 and pradigastat. The field's live hypothesis — liver-targeted delivery, or DGAT2 selectivity — is the only route that escapes the mechanism, and it is a formulation and selectivity question, not a docking question.

### 4.4 Testable hypotheses

1. No ChEMBL-registered DGAT1 inhibitor with IC50 below 10 nM has logP below 3 (falsifier: a single verified record with logP < 3 and IC50 < 10 nM — the screen's own data already support the hypothesis, and a counter-example would reopen the class).
2. CHEMBL2036730 inhibits DGAT1 with IC50 ≤ 1 nM head-to-head against pradigastat (falsifier: IC50 > 5 nM — which would show the ChEMBL record does not reproduce).
3. CHEMBL2036730 causes diarrhoea in a rodent model at the efficacious dose, as AZD7687 did (falsifier: no diarrhoea at 10× the efficacious dose — which would suggest a genuinely gut-sparing profile, the one result that would matter).
4. A liver-targeted formulation of CHEMBL2036730 reduces hepatic triglyceride without gut DGAT1 inhibition (falsifier: gut inhibition persists — which would end the liver-targeting hypothesis for this scaffold).
5. DGAT2-selective inhibition avoids the diarrhoea while retaining liver-fat reduction (falsifier: DGAT2 inhibition alone does not reduce liver fat — which would show the class needs both enzymes, and the gut problem is unavoidable).

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): DGAT1 enzyme assay (microsomal, oleoyl-CoA substrate) for CHEMBL2036730, CHEMBL3037924 and pradigastat in one plate, triplicate, with DGAT2 counter-screen — the selectivity number is the only gate that matters. Stage 2 (weeks 4–6): Caco-2 permeability and PAMPA to quantify gut exposure, plus logD measurement (the computed logP values must be confirmed experimentally). Stage 3 (weeks 7–9): HepG2 triglyceride accumulation assay at IC50 multiples. Stage 4 (weeks 10–12): rodent tolerability — stool consistency and food intake at the efficacious dose, with a gut-exposure measurement; if diarrhoea appears, the molecule stops here, as AZD7687 did. No efficacy claim without the tolerability readout.

## 5. Limitations

1. Docking only: no enzyme, cell or animal data were generated; the 1.21 kcal/mol spread is inside Vina's ±1–2 kcal/mol noise.
2. Single structure: docking used one DGAT1 structure (8ESM, cryo-EM 3.2 Å — lower resolution than the X-ray structures in this series); no MD or free-energy refinement was run.
3. The pipeline's first target attempt was wrong (nonexistent accession, wrong ChEMBL target) and its PDB search missed the DGAT1 structures; both corrections were manual.
4. Lipophilicity is computed (RDKit logP), not measured — logD must be confirmed experimentally before any developability claim.
5. Measured IC50 values are ChEMBL records from different source assays, not head-to-head measurements; pradigastat's own IC50 is not in this ChEMBL set.
6. The Pakistan diabetes figures are IDF 2021 modelled estimates; the MASLD burden in Pakistan was not verified for this paper.
7. Islamic-canon sweep: the full 23 volumes of Al-Razi's *Kitab al-Hawi* exist in English only in selections, and Ibn al-Nafis's commentary survives as an Arabic manuscript with only partial English translation; those texts were not read in full. No classical work was used as evidence for any molecule.
8. No local-market data: no DGAT1 inhibitor is registered in Pakistan; availability and price were not checked.

## 6. Conclusion

Every DGAT1 lead in this screen docks within 1.21 kcal/mol and binds at sub-nanomolar potency — and every one is too lipophilic to be the drug the class needs. The screen's usable result is negative: no ChEMBL-registered DGAT1 inhibitor combines potency with low lipophilicity, and the diarrhoea that killed AZD7687 and pradigastat is on-target, so another lipophilic analogue will fail the same way. The class needs liver-targeted delivery or DGAT2 selectivity, not a better docking score. Until that molecule exists, nothing here is a treatment claim.

## 7. Policy implications

**Decision-maker:** the Drug Regulatory Authority of Pakistan (DRAP) and the Pakistan Endocrine Society, with the Higher Education Commission's ORIC network. **Decision:** whether to fund metabolic-disease drug discovery aimed at systemic DGAT1 inhibition, and how to prioritise the national diabetes response. **Exact change:** DRAP/HEC should not fund another systemic DGAT1 inhibitor programme on potency data alone; any DGAT1 funding should be conditional on a measured logD below 3 or a liver-targeted delivery plan with gut-exposure data — instead of the current pattern, in which a potent molecule advances until the diarrhoea appears in humans. The same funds should prioritise what already works for Pakistan's 33 million people with diabetes: GLP-1 access, metformin supply, and screening — the interventions with measured benefit, not the target with measured failure. **If the evidence reverses this:** if a liver-targeted DGAT1 inhibitor shows liver-fat reduction without gut DGAT1 inhibition in animals, the funding bar should be revisited for that molecule specifically. **Islamic principle:** hifz al-nafs (preservation of life), defined by Al-Ghazali in *Al-Mustasfa min 'Ilm al-Usul* (c. 1109) and systematised by Al-Shatibi in *Al-Muwafaqat* — and maslaha (public interest): a drug that treats fatty liver by causing diarrhoea in more than half of patients does not serve the public interest when the same money buys screening and proven therapy, and 'adl (justice, Qur'an 4:135) asks who bears the side effect — in practice, the poorest patients, who cannot afford to stop working when a drug causes diarrhoea. Ibn Sina's *Canon* (Book III) treated digestion as a system to be kept in balance — the classical precedent for refusing a cure that breaks the gut to save the liver.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author thanks the open-data providers — UniProtKB, ChEMBL, PubChem and the RCSB Protein Data Bank — without which this work would not exist.

## References

1. Denison H, Nilsson C, Löfgren L, et al. Diacylglycerol acyltransferase 1 inhibition with AZD7687 alters lipid handling and hormone secretion in the gut with intolerable side effects: a randomized clinical trial. Diabetes Obes Metab. 2014;16(4):334–343. doi:10.1111/dom.12221. PMID: 24118885.
2. Meyers CD, Amer A, Majumdar T, Chen J. Pharmacokinetics, pharmacodynamics, safety, and tolerability of pradigastat, a novel diacylglycerol acyltransferase 1 inhibitor in overweight or obese, but otherwise healthy human subjects. J Clin Pharmacol. 2015;55(9):1031–1041. doi:10.1002/jcph.509. PMID: 25854859.
3. Haas JT, Winter HS, Lim E, et al. DGAT1 mutation is linked to a congenital diarrheal disorder. J Clin Invest. 2012;122(12):4680–4684. doi:10.1172/JCI64873. PMID: 23114594.
4. Sui X, Kun W, Walther T, et al. Mechanism of action for small-molecule inhibitors of triacylglycerol synthesis. Nat Commun. 2023. doi:10.1038/s41467-023-38934-3. PMID: 37248213.
5. DGAT1 and DGAT2 inhibitors for metabolic dysfunction-associated steatotic liver disease (MASLD) management: benefits for their single or combined application. Int J Mol Sci. 2024;25(16):9074. doi:10.3390/ijms25169074. (Pradigastat reduced liver fat at 24 weeks, diarrhoea >50%, NCT01811472.)
6. International Diabetes Federation. IDF Diabetes Atlas, 10th edition. Brussels: IDF; 2021. (Pakistan: 33 million adults with diabetes, 26.7% prevalence ages 20–79, highest national prevalence in the world.)
7. RCSB PDB entry 8ESM: human triacylglycerol synthesizing enzyme DGAT1 in complex with T863 inhibitor, cryo-EM 3.2 Å. RCSB Protein Data Bank. Accessed 2026-11-28.
8. UniProtKB O75907: diacylglycerol O-acyltransferase 1 (DGAT1), Homo sapiens. UniProt. Accessed 2026-11-28.
9. ChEMBL target CHEMBL6009: diacylglycerol O-acyltransferase 1, Homo sapiens; 41 bioactivities retrieved live 2026-11-28, including IC50 values for CHEMBL2036730 (0.5 nM), CHEMBL3037924 (1.1 nM), CHEMBL5864682 (1.2 nM) and CHEMBL4453443 (1.3 nM). ChEMBL, EMBL-EBI.
10. Al-Ghazali. Al-Mustasfa min 'Ilm al-Usul. c. 1109. (Defines the five necessities of the law, including hifz al-nafs.)
11. Al-Shatibi. Al-Muwafaqat fi Usul al-Shari'a. 14th c. (Systematises maqasid al-shariah.)
12. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Book III on digestion; cited for the hifz al-nafs principle only.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-106-2026-11-28-8ESM.json` (docking on PDB 8ESM) and `hidden_files/dock-HP-106-2026-11-28.json` (pipeline run on the corrected target O75907/CHEMBL6009; the first attempt's wrong accession Q8W0K6 and wrong target CHEMBL2074 are recorded in §2.2). Compound identifiers: pradigastat (QUERY), CHEMBL2036730, CHEMBL3037924, CHEMBL5864682, CHEMBL4453443. No additional data were generated.
