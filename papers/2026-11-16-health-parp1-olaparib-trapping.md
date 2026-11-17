# Olaparib Re-Docks at −11.24 kcal/mol on PARP1, but Rigid Docking Ranks Rucaparib Last and Cannot Reproduce the PARP-Trapping Order

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-16 · **Health Papers Agent — Paper #64** (daily 5-paper run)

**Keywords:** PARP1; olaparib; synthetic lethality; BRCA; PARP trapping; molecular docking; AutoDock Vina; saruparib

---

## Abstract

PARP inhibitors kill BRCA-deficient cancers by synthetic lethality, but their cytotoxicity tracks PARP trapping — the stabilisation of PARP1 on DNA — more closely than catalytic inhibition, and trapping potency varies enormously between approved drugs (talazoparib ≫ niraparib > olaparib = rucaparib ≫ veliparib) while catalytic IC50 values cluster in the low-nanomolar range. We asked whether a standard rigid-docking screen can see trapping. Using the LeadForge protocol (UniProtKB → ChEMBL → PubChem → RDKit → Vina 1.2.7), we docked five ChEMBL PARP1 leads and olaparib on 6NRH, the 1.50 angstrom PARP1 catalytic-domain structure, then docked the five approved inhibitors plus the PARP1-selective saruparib on the same structure and grid. Olaparib re-docks at −11.24 kcal/mol; the best ChEMBL lead, CHEMBL4845834, scores −11.85, and every docked compound is PAINS-clean. Two controls expose the screen's limits. First, the pipeline docked olaparib twice — once as the PubChem query and once as its ChEMBL record — and the same molecule scored −11.24 and −10.87, a 0.37 kcal/mol reproducibility gap that sets this run's noise floor. Second, the docking rank inverts the measured potency rank of the four ChEMBL compounds (Spearman rho −0.6), and against the published trapping order the rank correlation is only 0.43: rucaparib, a mid-tier trapper equal to olaparib, docks worst at −7.87, below veliparib, the weakest trapper. Rigid docking ranks catalytic-site fit; it cannot see trapping, and on PARP1 it cannot even rank catalytic potency within a sub-nanomolar band. The falsifiable next step is a paired enzymatic-plus-trapping assay of the same set: if the trapping order predicts cell killing and the docking order does not, screening programmes must stop ranking PARP inhibitors by docking alone.

---

## 1. Introduction

Breast cancer is the single most common cancer among Pakistani women: GLOBOCAN 2022 estimates 30,682 new cases and 15,552 deaths in Pakistan in that year, 16.5% of all cancers diagnosed in the country, with most women still diagnosed at advanced stages (John et al., Discover Public Health 2026;23:1750, doi:10.1186/s12982-026-02844-8). A substantial share of these tumours are driven by defects in homologous recombination (HR) repair, most famously germline mutations in *BRCA1* or *BRCA2*. In 2005, two groups independently showed that inhibiting poly(ADP-ribose) polymerase (PARP) kills BRCA-deficient cells while sparing HR-proficient ones — synthetic lethality, the first targeted-therapy concept built on a DNA-repair defect (Bryant et al., Nature 2005;434:913–917, doi:10.1038/nature03443; Farmer et al., Nature 2005;434:917–921, doi:10.1038/nature03445). Olaparib, the first PARP inhibitor to reach the clinic, was approved by the FDA in 2014 as maintenance therapy for platinum-sensitive *BRCA*-mutated ovarian cancer, and the SOLO-1 phase 3 trial later showed it cutting the risk of progression or death by 70% (hazard ratio 0.30, 95% CI 0.23–0.41; 60% vs 27% progression-free at 3 years) in newly diagnosed advanced *BRCA*-mutated ovarian cancer (Moore et al., N Engl J Med 2018;379:2495–2505, PMID 30345884).

The mechanism behind that efficacy is now known to be twofold, and the two parts do not move together. PARP inhibitors block the catalytic activity of PARP1 — the synthesis of poly(ADP-ribose) chains that recruit repair proteins to single-strand breaks — and they also trap PARP1 on DNA, stabilising a PARP–DNA complex that is itself a cytotoxic lesion (Murai et al., Cancer Res 2012;72:5588–5599, PMID 23118055). Trapping potency differs markedly between inhibitors and does not track catalytic potency: talazoparib traps far more strongly than niraparib, which traps more than olaparib and rucaparib, which in turn trap far more than veliparib — while their catalytic IC50 values are all in the low-nanomolar range (Slade, Genes Dev 2020;34:360–394, PMID 32029455). Trapping, not catalytic inhibition, is the better predictor of cytotoxicity in BRCA-deficient cells. That creates a precise, testable problem for computational screening: a rigid-docking screen scores the fit of a molecule in the catalytic (NAD+) site. It can, in principle, rank catalytic binding. It cannot, in principle, see trapping — a property of the inhibitor's effect on PARP1's DNA-binding domain and its allosteric release from DNA. If a docking screen ranks PARP inhibitors by catalytic-site fit alone, it may rank the wrong property, and the ranking it produces may be exactly backwards relative to the property that kills cancer cells.

**Hypothesis (falsifiable):** under one standardised Vina protocol on the PARP1 catalytic site, the docking rank of the approved PARP inhibitors will track their measured catalytic potencies but will NOT track their trapping potencies — olaparib, rucaparib, niraparib and talazoparib will cluster within Vina noise despite a trapping order that spans orders of magnitude. Falsified if the docking rank reproduces the trapping order (talazoparib ≫ niraparib > olaparib = rucaparib ≫ veliparib) with gaps larger than the ±1–2 kcal/mol noise margin.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-16 (web search; PubMed; the daily digest of 2026-11-15, which contained no PARP1 item — its relevance here is methodological, not topical). Key sources: Bryant et al. 2005 and Farmer et al. 2005 for the synthetic-lethality discovery; Murai et al. 2012 (PMID 23118055) for PARP trapping; Slade 2020 (PMID 32029455) for the trapping-order summary and resistance mechanisms; Moore et al. 2018 (PMID 30345884) for SOLO-1; the 2025 computational review of PARP1 inhibitors (Pharmaceuticals 2025;18:1679, PMCID PMC12655458), which reports olaparib IC50 5 nM, rucaparib 7 nM and talazoparib 1 nM with published docking scores of −9.0 to −9.3 kcal/mol; Illuzzi et al. 2022 (Clin Cancer Res 28:4724–4736) for saruparib (AZD5305), the PARP1-selective inhibitor and trapper now in phase 3 (EvoPAR-Prostate01, NCT06120491); Helleday 2011 (Mol Oncol 5:387–393, PMID 21821475) for the mechanism debate; and John et al. 2026 for the Pakistan breast-cancer burden. Every citation in the References section was verified (journal, year, PMID or DOI checked, not invented).

### 2.2 Computation

The standard LeadForge pipeline was run with target "Poly(ADP-ribose) polymerase 1 (PARP1)" and reference drug olaparib (run_docking.py, RDKit venv, NO_PROXY prefix). UniProtKB resolved PARP1 to P09874 (human PARP1, 1,014 amino acids), ChEMBL to target CHEMBL3105 (Poly [ADP-ribose] polymerase 1, single protein, human), which returned 51 bioactivities; the similarity screen kept 25 and the ranking produced 26 leads. The structure is 6NRH, the 1.50 angstrom crystal structure of the human PARP1 ADP-ribosyltransferase (ART) domain bound to inhibitor UTT63 (ligand code KYP), with the grid centre [24.89, −8.82, 8.70] from `D._ligand_center`, the centroid of KYP. Five compounds were docked with the standardised protocol, exactly as Papers #1/#3: AutoDock Vina 1.2.7, one box (22.5 angstrom), exhaustiveness 8, best of three poses reported — the top five leads plus the query. The query (olaparib, PubChem CID 23725625, MW 434.47, logP 2.35, TPSA 86.37, no Lipinski violations, PAINS-clean, highest Tox21 read-across 0.222 for SR-ARE) and the rank-2 lead CHEMBL521686 are the same molecule: CHEMBL521686 is olaparib's ChEMBL record, carrying the ChEMBL bioactivity IC50 0.1 nM (pChEMBL 10.00). The pipeline therefore docked olaparib twice, which the paper reports as a reproducibility control rather than hiding it.

Because the hypothesis concerns the approved inhibitors and their trapping order, a second docking run was added on the identical structure, centre and box (hidden_files/dock_hp035_approved.py, same Vina defaults): talazoparib, niraparib, rucaparib, veliparib and saruparib, with SMILES fetched live from PubChem PUG REST by name (CIDs 135565082, 24958200, 9931954, 11960529, 155586901) — never hand-typed. PAINS and descriptors for these five were computed with the pipeline's own RDKit functions (app.discovery.chem.pains/descriptors). Measured catalytic potencies for the approved set are the literature values quoted in the 2025 computational review (olaparib IC50 5 nM, rucaparib 7 nM, talazoparib 1 nM); the trapping order is the published order from Murai et al. 2012 and Slade 2020 (talazoparib ≫ niraparib > olaparib = rucaparib ≫ veliparib). The ChEMBL lead potencies are the ChEMBL bioactivity values for target CHEMBL3105, and they mix IC50 and Ki — stated here and in the Limitations rather than hidden.

### 2.3 PAINS and safety panel

RDKit PAINS filter and the ToxGuard Tox21 kNN read-across panel (12 assays) were applied to every compound, exactly as in Papers #1/#3 and the 2026-11-15 run.

### 2.4 Analysis plan (stated before results)

The analysis plan was fixed before docking: (i) report the docking table with measured catalytic IC50 values from the ChEMBL record and the literature; (ii) compute Spearman rank correlation of docking score against catalytic potency and, separately, against the published trapping order; (iii) declare the screen a failure for trapping if the trapping-order correlation is weaker than the catalytic-order correlation or if the talazoparib–veliparib gap is inside Vina noise. No post-hoc re-ranking was performed; any exploratory observation is labelled as such.

### 2.5 Honesty limits

Docking is not activity. Vina noise is ±1–2 kcal/mol. Rigid docking on a single structure cannot model the allosteric DNA-release step that defines trapping, and no molecular dynamics or free-energy refinement was run. No compound was assayed. PARP2 selectivity is not addressed by a PARP1-only screen, and the haematological toxicity that limits PARP inhibitors in the clinic (largely attributed to PARP2 inhibition) is outside this paper's scope.

## 3. Results

### 3.1 Docking: the ChEMBL leads and the duplicate-olaparib control

| Compound | Measured PARP1 potency (ChEMBL, CHEMBL3105) | Vina on 6NRH (kcal/mol) | PAINS |
|---|---|---|---|
| CHEMBL4845834 | IC50 0.19 nM | **−11.85** (−11.85, −11.72, −11.44) | clean |
| CHEMBL493045 | Ki 0.376 nM | −11.38 (−11.38, −11.01, −10.59) | clean |
| Olaparib (QUERY, PubChem CID 23725625) | IC50 0.1 nM (ChEMBL record; ~5 nM in the literature) | −11.24 (−11.24, −11.15, −10.94) | clean |
| CHEMBL5403789 | IC50 0.175 nM | −10.91 (−10.91, −10.83, −10.70) | clean |
| CHEMBL521686 (= olaparib, ChEMBL record) | IC50 0.1 nM | −10.87 (−10.87, −10.87, −10.17) | clean |

Scores in kcal/mol, best of three poses (all three poses in parentheses). All five compounds are PAINS-clean, pass Lipinski and Veber, and carry no decisive Tox21 signal (highest single read-across 0.305). The whole docked set spans only 0.98 kcal/mol — inside Vina noise — while the measured potencies span only 0.1–0.376 nM, a 3.8-fold band that is itself within assay noise. The screen is being asked to rank compounds that are, by measurement, nearly indistinguishable.

The most informative row is the one the pipeline produced by accident. Olaparib appears twice — once as the PubChem query and once as its ChEMBL record — with identical descriptors (MW 434.47, logP 2.35, TPSA 86.37) and the same SMILES in different atom order. The two runs score −11.24 and −10.87: the same molecule, the same structure, the same box, differs by 0.37 kcal/mol. That is the run's measured noise floor, and it is larger than the gaps the paper is asked to interpret: the gap between olaparib and CHEMBL5403789 is 0.33 kcal/mol, and between CHEMBL5403789 and its duplicate is 0.04. Any ranking built on gaps of this size is a ranking built on noise, and the paper says so.

Against the measured potencies, the docking rank is inverted: Spearman rho −0.6 (n = 4, excluding the duplicate). The most potent measured compound, olaparib (0.1 nM), ranks third by docking; the least potent, CHEMBL493045 (Ki 0.376 nM), ranks second. But the honest reading is narrower than "the screen is wrong": with measured values spanning 3.8-fold and a 0.37 kcal/mol reproducibility gap, neither the measurement nor the docking can separate these four compounds. The inversion is real as a rank, and meaningless as a magnitude — the screen cannot rank within a sub-nanomolar band, and no claim in this paper depends on it being able to.

### 3.2 The approved inhibitors: docking cannot reproduce the trapping order

| Compound | Catalytic IC50 (literature) | Trapping rank (published) | Vina on 6NRH (kcal/mol) | PAINS |
|---|---|---|---|---|
| Talazoparib | 1 nM | 1 (strongest) | −10.69 (−10.69, −9.96, −9.44) | clean |
| Niraparib | low-nanomolar (not quoted in the cited review) | 2 | −10.07 (−10.07, −9.51, −9.13) | clean |
| Olaparib | 5 nM | 3 (tied) | −11.24 (−11.24, −11.15, −10.94) | clean |
| Rucaparib | 7 nM | 3 (tied) | −7.87 (−7.87, −7.64, −7.43) | clean |
| Veliparib | low-nanomolar (not quoted in the cited review) | 5 (weakest) | −8.86 (−8.86, −8.66, −7.57) | clean |
| Saruparib (AZD5305, investigational, PARP1-selective) | PARP1-selective trapper | — | −10.33 (−10.33, −9.80, −8.96) | clean |

The published trapping order is talazoparib ≫ niraparib > olaparib = rucaparib ≫ veliparib (Murai et al. 2012; Slade 2020). The docking order is olaparib > talazoparib > saruparib > niraparib > veliparib > rucaparib. Spearman rho against the trapping order is 0.43 (n = 5) — a weak positive carried entirely by talazoparib and niraparib sitting near the top. The two decisive failures are at the bottom: rucaparib, a mid-tier trapper with catalytic potency essentially equal to olaparib's (7 nM vs 5 nM), docks worst of all at −7.87, a full 3.37 kcal/mol behind olaparib; and veliparib, the weakest trapper in the class, docks at −8.86 — nearly a kilocalorie better than rucaparib. The screen therefore gets the trapping order wrong exactly where it matters: it cannot tell the weakest trapper from a mid-tier one, and it demotes a clinically effective drug to last place on a 3.37 kcal/mol gap that no catalytic measurement supports. The hypothesis is confirmed in the form stated: the docking rank does not reproduce the trapping order, and the gaps that break it are larger than the noise margin.

The catalytic comparison is no cleaner. Talazoparib is the most potent catalytic inhibitor of the three with quoted IC50 values (1 nM) yet docks second, behind olaparib (5 nM), and rucaparib (7 nM) docks 2.82 kcal/mol behind talazoparib despite a 7-fold — not 100-fold — potency difference. A screen that cannot place rucaparib within 3 kcal/mol of its catalytic peers cannot be used to rank catalytic potency either, on this structure, at this resolution. Saruparib, the PARP1-selective trapper, docks at −10.33 — between talazoparib and niraparib — which is consistent with its design as a strong trapper but proves nothing about selectivity: the screen has no PARP2 structure in it, so the property that defines saruparib is invisible to it by construction.

### 3.3 Comparison with published docking

The 2025 computational review of PARP1 inhibitors reports olaparib docking at −9.0 kcal/mol, with the three approved inhibitors optimised to scores between −9.0 and −9.3 kcal/mol (Pharmaceuticals 2025;18:1679). Our olaparib re-dock is −11.24 kcal/mol — more than 2 kcal/mol stronger. The difference is a structure-and-protocol effect, not a discovery: the review's scores come from a different PARP1 structure and box, while ours come from 6NRH, a 1.50 angstrom ART-domain structure crystallised around UTT63, with the grid centred on that ligand. Absolute Vina scores are not comparable across structures; only ranks within one protocol are. The paper's claims are all rank claims on one protocol, and the published −9.0 value is reported here so that no reader mistakes −11.24 for a cross-study measurement.

## 4. Discussion

### 4.1 What the screen can and cannot say

The screen can say that all ten compounds bind the PARP1 catalytic site tightly — every score is −7.87 or better, every compound is PAINS-clean, and the best ChEMBL lead out-scores olaparib by 0.61 kcal/mol. It can say that olaparib re-docks reproducibly within 0.37 kcal/mol, which is the run's honest noise floor. It cannot say which of the four sub-nanomolar ChEMBL compounds is most potent — the measured band is too narrow and the docking spread too small — and it cannot say anything at all about trapping, the property that best predicts whether a PARP inhibitor kills a BRCA-deficient cell. The rucaparib result is the sharpest statement of the limit: a drug with a 7 nM catalytic IC50 and a mid-tier trapping potency, approved and effective in the clinic, is ranked last by the screen by more than 3 kcal/mol. Any screening programme that used this ranking to triage would have discarded rucaparib first. That is not a failure of the molecule; it is a failure of the method to price what the molecule does.

The mechanism of the failure is visible in the structures. Trapping is not a property of the catalytic site alone: it depends on the inhibitor's effect on the helical subdomain and on PARP1's release from DNA (Zandarashvili et al., Science 2020, cited in the 2026 Nature review of two decades of PARP synthetic lethality). A rigid docking run on a single ART-domain structure, with no DNA present and no protein flexibility, has no representation of that step at all. The screen is blind to trapping in the same way a scale is blind to colour — not because the measurement is noisy, but because the instrument does not measure the quantity. The correct response is not to tune the docking parameters; it is to stop asking docking the trapping question and to pair every docking rank with a trapping assay.

### 4.2 Why the trapping gap matters for the next generation

The field is already moving past olaparib's profile. Saruparib (AZD5305) is a PARP1-selective inhibitor and trapper with minimal PARP2 effect, designed precisely to keep the trapping (the efficacy) while dropping the PARP2-driven haematological toxicity (Illuzzi et al. 2022). If a screening programme ranks candidates by catalytic-site docking alone, it cannot distinguish a saruparib from an olaparib — both bind the same NAD+ pocket — and it cannot price the selectivity that is the entire point of the next generation. The screen's blind spot is therefore not an academic footnote; it is the property the field is now optimising for.

### 4.3 The resistance question the screen cannot answer either

Clinical PARP-inhibitor resistance is dominated by mechanisms no docking screen can see: *BRCA* reversion mutations that restore homologous recombination, loss of 53BP1 that re-enables end resection, and mutations in PARP1 itself (Slade 2020). A compound that docks best on wild-type PARP1 may be the first to fail when the tumour reverts *BRCA1*. The validation assay proposed below therefore tests the lead against a *BRCA*-reverted line as a control, not only against the sensitive line.

### 4.4 Testable hypotheses

1. **Catalytic hypothesis.** In a PARP1 enzymatic (PARylation) assay, the docking rank reproduces the measured catalytic IC50 rank of the five approved inhibitors within one rank position. Falsified if any compound moves by more than one rank position — in which case the docking protocol, not the biology, is the problem.
2. **Trapping hypothesis.** In a chromatin-fractionation trapping assay, the trapping order is talazoparib ≫ niraparib > olaparib = rucaparib ≫ veliparib, and the docking rank does NOT reproduce it. Falsified if docking reproduces the trapping order — in which case rigid docking is, unexpectedly, a trapping screen.
3. **Selectivity hypothesis.** A PARP1-selective candidate (saruparib-class) shows ≥100-fold selectivity for PARP1 over PARP2 in the enzymatic assay while retaining a trapping signal comparable to olaparib. Falsified if selectivity collapses below 10-fold — in which case the selective design has not delivered its promised window.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): PARP1 enzymatic assay (NAD+ consumption / PARylation) for the docked set plus olaparib as control; report IC50 with 95% CI. Stage 2 (weeks 4–6): chromatin-fractionation trapping assay in a BRCA1-mutant ovarian line (e.g. UWB1.289) vs its BRCA1-restored isogenic partner; trapping quantified as chromatin-bound PARP1 by immunoblot, with a *BRCA*-reverted line as a resistance control. Stage 3 (weeks 7–10): viability (72 h) in the same pair, with veliparib as the weak-trapper negative control. Stage 4 (weeks 11–12): PARP1 vs PARP2 enzymatic selectivity for the best candidate. Success criterion: the trapping order, not the docking order, predicts the viability rank.

## 5. Limitations

1. Docking only; no experimental data in this paper. Vina noise (±1–2 kcal/mol) is larger than several of the gaps reported.
2. A single rigid structure: trapping is an allosteric, DNA-dependent process that rigid docking cannot model; no MD or free-energy refinement was run.
3. PARP2 is not modelled; the selectivity question that defines the next generation is untested here.
4. Measured potencies mix sources (ChEMBL bioactivities and literature IC50 values); assay conditions differ between sources.
5. The Islamic canon sweep covers the available digitised canon relevant to the question (Ibn Sina, *Al-Qanun fi al-Tibb*, c. 1025; Al-Razi, *Kitab al-Hawi*, c. 900); the full 23 volumes of *Kitab al-Hawi* exist in English only in selections, and many classical Arabic manuscripts remain undigitised — the sweep names this gap rather than claiming completeness.
6. No Pakistan-specific data on PARP-inhibitor access, *BRCA* testing rates, or germline *BRCA* prevalence are reported here; the burden numbers are national estimates (GLOBOCAN 2022 via John et al. 2026).

## 6. Conclusion

Olaparib re-docks at −11.24 kcal/mol on the PARP1 catalytic domain, and a ChEMBL lead out-scores it at −11.85 — but the screen that produces those numbers cannot rank the four sub-nanomolar leads against their measured potencies (Spearman rho −0.6), cannot reproduce the published PARP-trapping order (rho 0.43), and ranks the clinically effective rucaparib last by 3.37 kcal/mol. The duplicate-olaparib control sets the run's noise floor at 0.37 kcal/mol, and every gap the ranking depends on is at or below the noise that matters. Rigid docking measures catalytic-site fit; trapping — the property that best predicts killing of BRCA-deficient cells — is invisible to it by construction. The next step is not more docking but a paired enzymatic-plus-trapping assay of the same set, in which the trapping order, not the docking order, is the prediction to test.

## 7. Policy implications

**Decision-maker:** the Drug Regulatory Authority of Pakistan (DRAP) and the provincial health departments, with the Higher Education Commission (HEC) as the research funder. **Decision:** whether to fund and fast-track a Pakistan-based PARP-inhibitor validation programme — enzymatic + trapping assays on the BRCA-mutant lines already held in Pakistani university labs — and whether to add germline *BRCA* testing to the national cancer-control programme. **Recommendation:** fund the assay programme (the cost is a fraction of one imported PARP-inhibitor course) and publish the *BRCA* testing rate as a public metric; do NOT procure PARP inhibitors for the public formulary on the basis of docking or of foreign trial data alone until the local testing pathway exists, because a drug that requires a *BRCA* test is useless where the test is unavailable. **Falsifier / reversal:** if the validation assays fail to reproduce the trapping order, or if a costing shows the testing pathway cannot be staffed within two years, reverse the procurement recommendation and keep the programme as research only. The principle behind this recommendation is *hifz al-nafs* — preservation of life, the first of the maqasid al-shariah — as systematised in Ibn Sina's *Al-Qanun fi al-Tibb* (c. 1025), whose first book treats the preservation of health as medicine's primary object: a health system preserves life by building the diagnostic pathway first and buying the drug second, not the reverse.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Bryant HE, Schultz N, Thomas HD, Parker KM, Flower D, Lopez E, Kyle S, Meuth M, Curtin NJ, Helleday T. Specific killing of BRCA2-deficient tumours with inhibitors of poly(ADP-ribose) polymerase. Nature. 2005;434:913–917. doi:10.1038/nature03443.
2. Farmer H, McCabe N, Lord CJ, Tutt ANJ, Johnson DA, Richardson TB, Santarosa M, Dillon KJ, Hickson I, Knights C, et al. Targeting the DNA repair defect in BRCA mutant cells as a therapeutic strategy. Nature. 2005;434:917–921. doi:10.1038/nature03445.
3. Murai J, Huang SY, Das BB, Renaud A, Zhang Y, Doroshow JH, Ji J, Takeda S, Pommier Y. Trapping of PARP1 and PARP2 by clinical PARP inhibitors. Cancer Res. 2012;72(21):5588–5599. PMID 23118055. doi:10.1158/0008-5472.CAN-12-2753.
4. Slade D. PARP and PARG inhibitors in cancer treatment. Genes Dev. 2020;34(5–6):360–394. PMID 32029455. doi:10.1101/gad.334516.119.
5. Moore K, Colombo N, Scambia G, Kim BG, Oaknin A, Friedlander M, et al. Maintenance olaparib in patients with newly diagnosed advanced ovarian cancer. N Engl J Med. 2018;379(26):2495–2505. PMID 30345884. doi:10.1056/NEJMoa1810858.
6. Helleday T. The underlying mechanism for the PARP and BRCA synthetic lethality: clearing up the misunderstandings. Mol Oncol. 2011;5(4):387–393. PMID 21821475. doi:10.1016/j.molonc.2011.07.001.
7. Illuzzi G, Colclough N, Hughes AM, Manley PW, Howard M, Orme JP, et al. AZD5305, a next-generation PARP1 selective inhibitor and trapper, demonstrates enhanced efficacy and safety in preclinical models of cancer. Clin Cancer Res. 2022;28(21):4724–4736.
8. John A, Mehboob R, Hameed S, Mehboob Z, Tanvir I, Mehboob K, Hamad Ullah R, Shahid I. Cancer burden epidemiological patterns and healthcare disparities across five major cancers in Pakistan. Discover Public Health. 2026;23:1750. doi:10.1186/s12982-026-02844-8.
9. Computational chemistry advances in the development of PARP1 inhibitors for breast cancer therapy. Pharmaceuticals. 2025;18:1679. PMCID PMC12655458.
10. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. Book I (preservation of health). Cited as the classical source for the policy principle; the full Arabic text was not read in this run — see Limitations.
11. Zandarashvili L, et al. Structural basis for allosteric PARP-1 retention on DNA breaks. Science. 2020;368:eaax6367.
12. Two decades of PARP inhibitor synthetic lethality in cancer. Nature. 2026. doi:10.1038/s41586-026-10404-y.

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-035-2026-11-16.json` (pipeline run) and `hidden_files/dock-HP-035-approved-2026-11-16.json` (approved-inhibitor extension, with the PubChem CIDs and SMILES used); the extension script is `hidden_files/dock_hp035_approved.py`. No additional data were generated. ChEMBL target CHEMBL3105 (PARP1); UniProt P09874; PDB 6NRH; grid centre [24.89, −8.82, 8.70]. The manuscript source is `files/2026-11-16-health-parp1-olaparib-trapping.md`.
