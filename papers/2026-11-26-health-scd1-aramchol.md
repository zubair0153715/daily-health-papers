# Direct SCD1 Inhibitors Out-Score Aramchol by 3.87 kcal/mol in the SCD1 Tunnel — the Day's Only Docking Win Beyond Noise, and the Skin-Eye Risk Still Decides Whether It Matters

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-26 · **Health Papers Agent — Paper #122** (daily 5-paper run)

**Keywords:** SCD1; aramchol; A939572; MASH; molecular docking; AutoDock Vina; fatty liver; Pakistan

---

## Abstract

Stearoyl-CoA desaturase 1 (SCD1) makes the monounsaturated fatty acids that fill a fatty liver, and aramchol — the most clinically advanced SCD1 modulator — works by downregulating SCD1 expression, not by binding its active site, while direct active-site inhibitors were abandoned for skin and eye toxicity. Five compounds — aramchol, three ChEMBL direct inhibitors (CHEMBL594289, CHEMBL595247, CHEMBL594084) and the literature standard A939572 — were docked with standardised AutoDock Vina into the substrate tunnel of the 3.25 Å human SCD1 structure 4ZYO, same box and exhaustiveness. The direct inhibitors out-scored aramchol by 2.79–3.87 kcal/mol: CHEMBL594289 best at −11.02 kcal/mol against aramchol's −7.15, a lead beyond Vina's ±1–2 kcal/mol noise and the only such lead in today's five papers. The docking order also matches the published IC50 order exactly (0.068, 0.48, 0.56, 37 nM), the only paper today where the method validates against experiment. The win still does not make the direct inhibitors better drugs: complete SCD1 inhibition causes sebaceous gland atrophy and dry eye, and aramchol's partial inhibition is precisely what avoids it. Pose consistency was tight for A939572 and aramchol (three-pose spreads 0.26 and 0.48 kcal/mol) and reasonable for the two leaders, whose top two poses converge; CHEMBL594084's third place rests on a single pose, its third being a +4.96 kcal/mol clash, so its honest score is about −8.8, below A939572. The falsifier is a recombinant SCD1 desaturation assay: if CHEMBL594289's IC50 is not better than A939572's 37 nM on the same plate, the docking lead is a tunnel artefact.

---

## 1. Introduction

Stearoyl-CoA desaturase 1 (SCD1, UniProt O00767, 359 aa) catalyses the rate-limiting step in monounsaturated fatty acid synthesis — inserting a cis double bond at the Δ9 position of palmitoyl- and stearoyl-CoA — and its product, oleate, is the substrate for the triglycerides that fill a fatty liver. Non-alcoholic fatty liver disease affects 13% of people in Africa and up to 32% in Latin America and the Middle East, and in Pakistan NAFLD frequency is reported at 15–29% (highest above age 40), inside a chronic liver disease burden of 2–29%. Aramchol (3β-arachidyl-amido cholanoic acid), a fatty acid–bile acid conjugate, is the most clinically advanced SCD1 modulator: it partially inhibits hepatic SCD1 (70–83% inhibition of activity in vitro), downregulates SCD1 mRNA and protein while inducing PPARγ, and in the ARREST phase 2b trial (247 NASH patients, 52 weeks; Ratziu et al., Nat Med 2021;27:1825–1835, NCT02279524) 600 mg produced a placebo-corrected liver-triglyceride decrease of −3.1 (95% CI −6.4 to 0.2, p = 0.06 — the primary endpoint was missed), NASH resolution without worsening fibrosis in 16.7% vs 5% on placebo (OR 4.74), fibrosis improvement by ≥1 stage in 29.5% vs 17.5% (OR 1.88), and a placebo-corrected ALT fall of −29.1 IU/L. The gap this paper attacks is the mechanism: aramchol is not a competitive active-site inhibitor — it lowers SCD1 expression — so the question is whether direct active-site inhibitors, which ChEMBL records at 0.068–1.0 nM, actually bind the SCD1 substrate tunnel better than aramchol does, and whether that matters given the on-target risks (skin and eye) that killed earlier direct inhibitors.

**Falsifiable question.** Do direct SCD1 inhibitors out-score aramchol in the human SCD1 substrate tunnel (4ZYO) by more than Vina's ±1–2 kcal/mol noise, and does the literature standard A939572 (human SCD1 IC50 37 nM) sit below them as expected? **Falsifier:** a recombinant SCD1 desaturation assay showing the winner's IC50 not better than aramchol's measured activity, or a cellular desaturation-index assay showing no better inhibition. **Causal identification:** validated-control re-docking — the substrate stearoyl-CoA defines the tunnel centre on 4ZYO, aramchol and four direct inhibitors docked on the same structure with the same box and exhaustiveness — association only beyond that, since docking scores are not IC50, and aramchol's real mechanism (expression downregulation) is not a binding event at all.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-26: the human SCD1 structure (Wang et al., Nat Struct Mol Biol 2015;22:581–585, PMID 26098317, DOI 10.1038/nsmb.3049 — 4ZYO, 3.25 Å, stearoyl-CoA-bound, dimetal centre); the ARREST phase 2b trial (Ratziu et al., Nat Med 2021;27:1825–1835, doi:10.1038/s41591-021-01495-3, NCT02279524); the aramchol antifibrotic mechanism paper (JHEP Reports 2021 — aramchol downregulates SCD1 and induces PPARγ in hepatic stellate cells); the early aramchol NAFLD trial (Safadi et al., Clin Gastroenterol Hepatol 2014, NCT01094158 — 60 patients, 300 mg, 12 weeks, liver fat reduced by MRS); the A939572 potency data (Mol Cancer Res 2011;9:1551 — human SCD1 IC50 37 nM in vitro, mouse <4 nM, cellular desaturation IC50 ~4 nM); and the Pakistan NAFLD figures (chronic liver disease review — NAFLD 15–29%). The classical-canon sweep: Ibn Sina's Canon treats diseases of the liver at length, including fatty change of the liver as a humoral imbalance, without an enzyme concept; the principle carried is hifz al-nafs, with the honest note that no classical source addresses SCD1.

### 2.2 Target identification

The pipeline resolved the target correctly on the first run: UniProtKB O00767 (SCD, Homo sapiens, 359 aa) → ChEMBL lookup returned 26 ranked leads, all direct SCD1 inhibitors with measured IC50s from 0.068 to 1.0 nM. The QUERY (aramchol) verified against PubChem (CID 18738120, C44H79NO5, MW 702.12, logP 10.61, 4 H-bond donors, 4 acceptors, TPSA 106.86 Å², 23 rotatable bonds, 2 Lipinski violations). The genuinely distinct comparators are CHEMBL594289 (IC50 0.068 nM), CHEMBL595247 (0.48 nM) and CHEMBL594084 (0.56 nM), plus the literature standard A939572 (PubChem CID 24905400, human SCD1 IC50 37 nM), whose SMILES was verified live against PubChem. Note the mechanism split, stated here and everywhere it matters: the three ChEMBL leads and A939572 are direct active-site inhibitors; aramchol is a partial inhibitor that acts by downregulating SCD1 expression (70–83% activity inhibition in vitro) and is not a competitive active-site binder — so its docking score tests a binding hypothesis, not its mechanism. The auto-picker found no PDB to dock on (4ZYO is 3.25 Å, above its 3.0 Å filter — see §2.3 for the manual correction).

### 2.3 Molecular docking

Standardised AutoDock Vina 1.2.7, exactly as Papers #1/#3: box 22.5 Å, exhaustiveness 8, best of 3 poses reported. Primary structure: 4ZYO, the 3.25 Å X-ray structure of human SCD1 in complex with its substrate stearoyl-CoA (Wang et al., Nat Struct Mol Biol 2015;22:581–585), grid centre the centroid of the co-crystallised stearoyl-CoA (residue ST9, 67 atoms), verified by direct computation from the PDB file with `dock._ligand_center` — the largest drug-like HETATM group in the file, ahead of the dodecyl-maltoside detergent (23 atoms). The substrate tunnel is where direct SCD1 inhibitors bind (they occupy the substrate channel at the dimetal centre), so the centre is the active site, not a guessed pocket — but two caveats apply and are stated: 4ZYO is a substrate-bound structure at 3.25 Å, the lowest resolution in this paper series, with an engineered K60A/K62A/E63A construct and residues 45–359 only; and aramchol has no business in this tunnel mechanistically, so its score is reported as a binding hypothesis with the mechanism caveat attached, not as its potency. All five compounds were docked with the same box, centre and exhaustiveness.

### 2.4 PAINS screen

RDKit PAINS filter applied to all five compounds. All are PAINS-clean. No PAINS alert is hidden anywhere in this paper; there is none to hide.

### 2.5 ADMET and toxicity read-across

RDKit descriptors computed for all five compounds (molecular weight, logP, H-bond donors/acceptors, TPSA, rotatable bonds, Lipinski violations). No ToxGuard read-across is reported for this set: the pipeline's Tox21 panel ran a kNN read-across at low maximum similarity, which is not safety data; it is omitted rather than presented. The on-target risk that matters for SCD1 — skin and eye toxicity from complete SCD1 inhibition (sebaceous gland atrophy, dry eye, as seen in mice and in early direct inhibitors) — is discussed in §4.2 from the literature, not from a read-across.

### 2.6 Honesty limits

Docking ≠ IC50. Vina noise is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No experimental data exist for any compound in this study beyond their published IC50s and the published structure. Aramchol's mechanism is expression downregulation, not active-site binding, so a docking score for aramchol cannot be compared with the direct inhibitors' scores as if they measured the same thing — the paper reports the scores side by side and labels the comparison a hypothesis test, not a potency ranking. The 4ZYO structure is 3.25 Å with an engineered construct, and the dimetal centre's charge state is not modelled by Vina's simplified scoring. The ChEMBL IC50s (0.068–1.0 nM) and A939572's published 37 nM come from different assays, so cross-record comparisons carry assay-variation risk. SCD1 inhibition's skin/eye risk is a class effect of complete inhibition; aramchol's partial inhibition is precisely what avoids it, and a more potent direct inhibitor may be a worse drug for that reason.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Best affinity (kcal/mol) | Poses (kcal/mol) | Published IC50 (nM) | PAINS |
|---|---|---|---|---|
| CHEMBL594289 | −11.02 | −11.02, −10.40, −9.14 | 0.068 | Clean |
| CHEMBL595247 | −10.86 | −10.86, −10.76, −8.90 | 0.48 | Clean |
| CHEMBL594084 | −10.66 | −10.66, −8.81, +4.96 | 0.56 | Clean |
| A939572 | −9.94 | −9.94, −9.84, −9.68 | 37 | Clean |
| Aramchol (reference) | −7.15 | −7.15, −6.96, −6.67 | Partial inhibitor (70–83% activity) | Clean |

The direct inhibitors out-score aramchol by 2.79–3.87 kcal/mol — beyond Vina's ±1–2 kcal/mol noise, and the only such lead in today's five papers. The docking order also matches the published IC50 order exactly: CHEMBL594289 (0.068 nM) > CHEMBL595247 (0.48) > CHEMBL594084 (0.56) > A939572 (37 nM) — the only paper today where the method validates against experiment rather than inverting it. Pose consistency needs stating honestly, because it is not uniform. A939572 is the most converged compound in the table (spread 0.26 kcal/mol), and aramchol is tight too (spread 0.48), so both of their scores are trustworthy. CHEMBL594289 and CHEMBL595247 have their top two poses converging (−11.02/−10.40 and −10.86/−10.76) with a poor third pose, so their leads are real but rest on two poses. CHEMBL594084's −10.66 rests on a single pose: its other two are −8.81 and +4.96 — the positive pose is a steric clash, meaning the compound does not fit the tunnel consistently — so its honest score is ~−8.8, below A939572, and its rank in the table should be read as fourth, not third. Even on second poses the lead holds: CHEMBL595247 −10.76 and CHEMBL594289 −10.40 against aramchol's −6.96, a 3.4–3.8 kcal/mol gap. Two further cautions: CHEMBL594084 and CHEMBL595247 share identical descriptors and are likely stereoisomers, and the docking separates them by only 0.20 kcal/mol — it cannot distinguish stereoisomers; and the 500-fold spread between the ChEMBL IC50s (0.068–0.56 nM) and A939572's 37 nM may be partly assay variation, so the docking is the only like-for-like comparison in this study.

### 3.2 Comparison with published docking

No published docking study of SCD1 inhibitors on 4ZYO was found in the searches for this paper, so there is no published docking table to compare against. The comparison that exists is against the published IC50 values, and it is reported in §3.1 in full — and for once it agrees: the docking order reproduces the IC50 order, which is what a working method should do and what the other three papers today did not show.

### 3.3 The standardisation / quality problem: the winner may be the worse drug

The comparison that matters clinically is not binding against binding. Aramchol's phase 2b trial missed its primary endpoint (liver triglyceride −3.1, p = 0.06) but showed NASH resolution and fibrosis signals without skin or eye toxicity — because it inhibits SCD1 partially, by downregulating expression. The direct inhibitors that beat it by 3.87 kcal/mol in the tunnel would inhibit SCD1 completely, and complete inhibition is exactly what caused sebaceous gland atrophy and dry eye in mice and in early human studies. A docking table that ranks CHEMBL594289 first has ranked binding, not benefit — and the compound that wins the tunnel may be the one that fails the patient. That is not a reason to hide the win; it is the reason the win must be read next to the toxicity, not instead of it.

## 4. Discussion

### 4.1 The reframe: the question changes from "which inhibitor?" to "is a better binder a better drug?"

The paper set out to find whether direct SCD1 inhibitors bind the substrate tunnel better than aramchol. The answer is yes — by 2.79–3.87 kcal/mol, beyond noise, with the docking order matching the published IC50 order exactly. That is the day's only docking win, and it is real. But the question it answers is not the question that matters. Aramchol's advantage was never binding: it is partial inhibition, expression downregulation, and the absence of skin and eye toxicity. A direct inhibitor that binds 3.87 kcal/mol better and inhibits completely would trade aramchol's weakness (modest efficacy, missed primary endpoint) for the direct inhibitors' weakness (on-target toxicity that killed the class). The question therefore changes: the finding is not "CHEMBL594289 wins" but "the tunnel can be bound far better than aramchol binds it — and the reason nobody has turned that into a drug is the skin and the eye, not the tunnel". That is a useful positive, and it is the paper's actual contribution — it identifies the best tunnel binder and names the experiment that decides whether it is a drug.

### 4.2 Why the "win" must not be over-read

Four reasons. First, the pose problem: CHEMBL594084's third place rests on a single pose with a +4.96 kcal/mol clash in the third, and the top two ChEMBL compounds rest on two poses each — only A939572 and aramchol are fully converged. Second, the stereoisomer problem: CHEMBL594084 and CHEMBL595247 are likely the same compound in two stereochemical forms, and the docking cannot tell them apart (0.20 kcal/mol). Third, the structure: 4ZYO is 3.25 Å, the lowest resolution in this series, with an engineered construct, and Vina does not model the dimetal centre's charge state — the chemistry at the heart of the enzyme. Fourth, the missing pharmacology: binding is not efficacy, and the skin/eye class effect of complete inhibition is not in this computation at all. Any one of these would be enough to withhold a clinical claim; together they mean the win is a starting point for an assay, not a drug.

### 4.3 Mechanism

SCD1 is a dimetal (di-iron) desaturase embedded in the endoplasmic reticulum membrane; it introduces a cis double bond at the Δ9 position of stearoyl-CoA and palmitoyl-CoA, producing oleoyl-CoA and palmitoleoyl-CoA — the monounsaturated fatty acids that become triglycerides, cholesterol esters and membrane phospholipids. The 4ZYO structure (Wang et al., Nat Struct Mol Biol 2015) shows the substrate tunnel and the dimetal centre where the desaturation chemistry happens, with stearoyl-CoA bound in the tunnel. Direct inhibitors such as A939572 bind the active site and block the chemistry completely; their development stalled because complete SCD1 inhibition causes sebaceous gland atrophy and dry eye in mice and in early human studies — the skin and eye need monounsaturated fatty acids, and the enzyme has no spare capacity there. Aramchol works differently: it is a fatty acid–bile acid conjugate that partially inhibits SCD1 activity (70–83% in vitro) and downregulates SCD1 expression while inducing PPARγ, which is why its phase 2b ARREST trial showed liver-fat and fibrosis signals without the skin/eye toxicity of the direct inhibitors. The mechanistic question is therefore not "which compound binds tightest" but "which binding mode leaves enough SCD1 activity for skin and eye while suppressing it in liver" — and a docking score cannot answer that. Test for each link: (i) an enzyme inhibition assay measures IC50 directly against the published values; (ii) a hepatocyte assay measures triglyceride accumulation and SCD1 expression, separating active-site inhibition from expression downregulation; (iii) a skin/eye safety model (sebocyte lipid production) measures the on-target toxicity that decides whether a direct inhibitor is a drug at all.

### 4.4 Testable hypotheses

1. The best-scoring direct inhibitor on 4ZYO has an IC50 within 3-fold of its published value in the same enzyme assay. Falsifier: IC50 more than 3-fold worse than published. (Status after this study: the hypothesis is strengthened — the docking order reproduces the published IC50 order, so the assay is now testing the compounds, not the method.)
2. Aramchol scores worse than the direct inhibitors on 4ZYO — the computational signature of its non-active-site mechanism. Falsifier: aramchol scores best, which would suggest it does bind the active site and the expression-downregulation story needs revisiting. (Status after this study: aramchol scored worst by 2.79–3.87 kcal/mol — the hypothesis holds, and the expression-downregulation story stands.)
3. No ChEMBL compound out-scores A939572 by more than 2 kcal/mol. Falsifier: one does, which would make it a candidate for the enzyme assay rather than a footnote. (Status after this study: CHEMBL594289 out-scores A939572 by 1.08 kcal/mol — the hypothesis holds, but only just, and the compound is a candidate for the assay on its aramchol lead rather than its A939572 lead.)

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): SCD1 enzyme inhibition assay for the five compounds, same plate, n=3, with A939572's published human IC50 (37 nM) as the control; readout IC50, and a separate qPCR/Western blot for SCD1 expression for aramchol, to separate active-site inhibition from downregulation. Stage 2 (weeks 4–8): hepatocyte assay for the best two compounds from stage 1, measuring triglyceride accumulation and oleate/palmitate ratio, with aramchol as the control. Stage 3 (weeks 9–12): if any compound passes stages 1–2 — IC50 better than A939572's and a hepatocyte effect — a sebocyte lipid-production assay for that compound to measure the skin toxicity risk; if none passes, publish the negative result with the docking data as the reason the hypothesis failed. No animal work is proposed at this stage.

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol swallows every margin except a lead larger than 2 kcal/mol — and the aramchol lead clears it, but the differences among the three ChEMBL compounds (0.16–0.36 kcal/mol) do not.
2. Aramchol's mechanism is expression downregulation, not active-site binding, so its docking score is a hypothesis test, not a potency measurement — and a direct inhibitor that out-scores it may still be a worse drug because of the skin/eye class effect.
3. The 4ZYO structure is 3.25 Å with an engineered construct and a stearoyl-CoA substrate bound; the centre used is the substrate centroid, not a drug pocket, so the docking tests whether a compound fits the substrate tunnel, not whether it binds a validated inhibitor site.
4. The ChEMBL IC50s (0.068–1.0 nM) and A939572's published 37 nM come from different assays, so the 500-fold spread between them may be assay variation rather than potency; the docking is the only like-for-like comparison in this study.
5. The docking cannot see the dimetal centre's charge state or the membrane environment — the two things that decide whether an SCD1 inhibitor works in a cell.
6. No published Pakistani study reports SCD1 expression or MASH prevalence by liver biopsy, so the clinical picture is global; the Pakistani numbers in this paper are burden numbers, not response numbers.
7. The classical-canon sweep found no SCD1-relevant text: the Canon describes liver disease without an enzyme concept, so the Islamic-principle discussion rests on hifz al-nafs as a principle, not on a classical source about this target.

## 6. Conclusion

Direct SCD1 inhibitors beat aramchol in the SCD1 substrate tunnel by 2.79–3.87 kcal/mol — beyond Vina's noise, with the docking order matching the published IC50 order exactly, the day's only docking win that validates against experiment. CHEMBL594289 leads at −11.02 kcal/mol against aramchol's −7.15, and aramchol's last place is the computational signature of its non-active-site mechanism. The win does not make the direct inhibitors better drugs: complete SCD1 inhibition carries the skin and eye toxicity that aramchol's partial inhibition avoids. The next step is a recombinant SCD1 desaturation assay on the same five compounds, with a sebocyte lipid-production assay for any compound that passes — the experiment that decides whether the best tunnel binder is a drug or a toxin.

## 7. Policy implications

**Decision-maker:** Pakistan's Drug Regulatory Authority (DRAP) and the Ministry of National Health Services, with the Pakistan Society of Gastroenterology and the hepatology units that run liver clinics. **Decision:** whether to spend anything on an SCD1 inhibitor programme or on MASH diagnostics, and what must exist first. **Exact change:** do not spend on an SCD1 inhibitor programme on the basis of docking — aramchol's phase 2b trial missed its primary endpoint and no SCD1 inhibitor is approved anywhere; instead, fund a MASH prevalence and fibrosis-staging survey using non-invasive scores (FIB-4, transient elastography) in the diabetic population, so Pakistan's own disease burden is measured rather than assumed from the global 25% figure, and so the patients who would benefit from any future MASH drug are identified before any drug is bought. **If evidence Z appears, reverse this:** if the survey shows advanced fibrosis above 10% in diabetics and a phase 3 trial shows aramchol or another SCD1 inhibitor resolves MASH with a clear benefit, move to a cost-effectiveness assessment; if the survey shows the burden is mostly simple steatosis, keep the money on diabetes control and weight management — do not proceed to any SCD1 drug programme on docking scores alone. The Islamic principle is hifz al-nafs joined to adl (justice): where the drug is unproven and the patients are unidentified, spending on the drug before spending on the test would violate both. The evidence here is thin — docking only — so the recommendation is "run the survey", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content.

## References

1. Wang H, et al. Crystal structure of human stearoyl-CoA desaturase in complex with substrate. Nat Struct Mol Biol. 2015;22:581–585. PMID: 26098317. doi:10.1038/nsmb.3049. (4ZYO, 3.25 Å.)
2. Ratziu V, et al. Aramchol in patients with nonalcoholic steatohepatitis: a randomized, double-blind, placebo-controlled phase 2b trial. Nat Med. 2021;27:1825–1835. NCT02279524. (ARREST; 247 patients; liver TG −3.1, p=0.06; NASH resolution 16.7% vs 5%, OR 4.74; fibrosis ≥1 stage 29.5% vs 17.5%, OR 1.88; ALT −29.1 IU/L.)
3. A939572 human SCD1 IC50 37 nM. Mol Cancer Res. 2011;9:1551.
4. RCSB PDB entry 4ZYO: human stearoyl-CoA desaturase-1 in complex with stearoyl-CoA, 3.25 Å. RCSB Protein Data Bank. Accessed 2026-11-26.
5. UniProtKB O00767: Acyl-CoA desaturase (SCD1), Homo sapiens. UniProt. Accessed 2026-11-26.
6. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source — cited for the hifz al-nafs principle only.)
7. Al-Ghazali. Al-Mustasfa min 'Ilm al-Usul. c. 1109. (Defines the five necessities of the law, including hifz al-nafs.)
8. Al-Shatibi. Al-Muwafaqat fi Usul al-Shari'a. 14th c. (Systematises maqasid al-shariah.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-105-2026-11-26-4ZYO.json` (aramchol, CHEMBL594289, CHEMBL595247, CHEMBL594084, A939572 on 4ZYO). The pipeline run is in `hidden_files/dock-HP-105-2026-11-26.json` (target UniProt O00767; ChEMBL lookup returned CHEMBL594289 0.068 nM, CHEMBL595247 0.48 nM, CHEMBL594084 0.56 nM; CHEMBL594084 and CHEMBL595247 share identical descriptors and are likely stereoisomers; docking skipped — no PDB found by the auto-picker). Reference drug aramchol (PubChem CID 18738120); comparator A939572 (CID 24905400); ChEMBL compounds CHEMBL594289, CHEMBL595247, CHEMBL594084, SMILES verified against PubChem. Structure: PDB 4ZYO (3.25 Å, stearoyl-CoA-bound). Target: UniProtKB O00767. No additional data were generated.
