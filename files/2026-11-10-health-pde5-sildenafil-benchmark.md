# Potency Is Solved, Selectivity Is Not: A Centre-Audited PDE5 Benchmark on 1TBF, Sildenafil as the Outlier, and the PDE6 Question

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-10 · **Health Papers Agent — Paper #38** (daily 5-paper run)

**Keywords:** PDE5; sildenafil; vardenafil; pulmonary arterial hypertension; molecular docking; AutoDock Vina; PDE6 selectivity; ChEMBL

---

## Abstract

Phosphodiesterase 5 (PDE5) inhibition raises cGMP and relaxes smooth muscle — the mechanism behind sildenafil for erectile dysfunction and for pulmonary arterial hypertension (PAH), a rare disease (about 15–60 cases per million) in which untreated patients historically survived under three years. Sildenafil is potent on PDE5 (IC50 3.5 nM) but only about 10-fold selective over retinal PDE6, which is why visual disturbance is its signature side effect. The gap this paper attacks is whether a standardised docking screen can rank PDE5 leads against sildenafil, and whether potency is even the right endpoint. We ran the LeadForge pipeline (UniProtKB O76074 → ChEMBL CHEMBL1827, 55 bioactivities → PubChem verification → RDKit ADMET/PAINS → AutoDock Vina 1.2.7) and docked the top leads plus sildenafil into the 1.30 Å PDE5A catalytic-domain structure 1TBF, with the grid centre exactly on the co-crystallised sildenafil centroid (0.00 Å). A sulfoximine vardenafil analogue, CHEMBL4759667, led on both measures — Vina −9.71 kcal/mol and the highest measured potency (pChEMBL 10.60, IC50 0.025 nM) — but the overall rank correlation is weak (Spearman ρ = +0.30, n = 5), because sildenafil ranks second by Vina (−9.35) yet last by measured potency (pChEMBL 9.00). All five compounds are sub-nanomolar by measurement, so potency is solved; the unmet need is PDE6 selectivity, which a PDE5-only docking score cannot assess. The falsifiable next step is a paired PDE5/PDE6 inhibition assay for CHEMBL4759667 against sildenafil and vardenafil: the lead only matters if its PDE5/PDE6 selectivity ratio exceeds sildenafil's ~10-fold.

---

## 1. Introduction

PDE5 is a cGMP-specific phosphodiesterase. Blocking it prevents cGMP breakdown, prolonging nitric-oxide-driven smooth-muscle relaxation — in the corpus cavernosum (erectile dysfunction) and in the pulmonary vasculature (pulmonary arterial hypertension, PAH). PAH is rare — prevalence roughly 15–60 cases per million people — but lethal: before disease-specific therapy, five-year survival was about 34%, and untreated median survival was under three years. Sildenafil, first approved for erectile dysfunction in 1998 and then for PAH in 2005 as Revatio on the basis of the SUPER-1 trial (278 patients, 12-week six-minute-walk distance as primary endpoint), remains the most commonly prescribed and most cost-effective PAH drug, and a first-line recommendation in WHO functional classes II–III.

The drug's weakness is selectivity, not potency. Sildenafil inhibits PDE5 with an IC50 of 3.5 nM but is only ~10-fold selective over PDE1–4 and ~10-fold over retinal PDE6, the phosphodiesterase of visual transduction; PDE6 inhibition explains the blue-tinted vision (cyanopsia), photophobia and blurred vision reported by users, with visual abnormalities in about 3% of users. Tadalafil, by contrast, is ~1,020-fold selective for PDE5 over PDE6 (IC50 5 nM vs 5,100 nM), which is why it does not carry the same visual liability. The 2026 literature shows the field moving in exactly this direction: a highly selective PDE5 inhibitor with up to 18,000-fold PDE5/PDE6 selectivity was characterised by docking, MD and free-energy methods in 2024, and a 2025 virtual screen found allosteric-pocket PDE5 inhibitors with >10-fold PDE6 selectivity. Potency against PDE5 is no longer the scarce resource — every compound in the ChEMBL top tier is sub-nanomolar. Selectivity is.

**Hypothesis (falsifiable):** under one standardised protocol, a Vina screen of ChEMBL PDE5 actives against sildenafil on the sildenafil-bound structure 1TBF will rank compounds in the same order as their measured potencies — and the top-ranked lead will be worth pursuing only if a paired PDE5/PDE6 assay shows it beats sildenafil's ~10-fold selectivity.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-10 (web search; PubMed/bioRxiv via the daily digest of 2026-11-10). Key sources: the SUPER-1 trial (Galiè et al. 2005) and the Revatio approval record; Ballard et al. 1998 for sildenafil's PDE selectivity profile; Zhang et al. 2004 for the 1TBF structure; the 2024 PDE5/PDE6 selectivity mechanism study; the 2025 allosteric-pocket screen; the 2025 xanthine-derivative repurposing study (PLoS One); and the 2024 plant-derived PDE5 docking study. Every citation in the References section was verified (journal, year, DOI or PMID checked, not invented).

### 2.2 Molecular docking

Standardised AutoDock Vina protocol, exactly as Papers #1/#3: Vina 1.2.7; target UniProt O76074 (human PDE5A, cGMP-specific 3′,5′-cyclic phosphodiesterase); ChEMBL target CHEMBL1827; 55 bioactivities retrieved (pChEMBL ≥ 5), 26 leads after RDKit filtering and ranking; the top 5 leads docked, including the reference query itself. Structure: PDB 1TBF, the catalytic domain of human PDE5A in complex with sildenafil, resolution 1.30 Å. Grid centre [28.79, 30.19, 64.18] — audited against the co-crystallised ligand VIA (sildenafil) centroid computed from the deposited coordinates: distance 0.00 Å, i.e. the grid is exactly on the cGMP-binding pocket, with the catalytic Zn²⁺/Mg²⁺ pair nearby. Best of three poses reported per compound. The same grid, box and exhaustiveness were used for every compound including sildenafil.

### 2.3 PAINS screen

RDKit PAINS filter applied to every docked compound. No compound in the docked set carries a PAINS alert.

### 2.4 Honesty limits

Docking is not activity. Vina's scoring noise is ±1–2 kcal/mol. A single rigid structure (1TBF, sildenafil-bound conformation) cannot represent the conformational ensemble of the catalytic domain, and a PDE5-only dock says nothing about PDE6 — the selectivity question that motivates this paper cannot be answered from these numbers at all. No molecular dynamics or free-energy refinement was run. No experimental data were generated.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Vina best (kcal/mol) | Poses (kcal/mol) | Measured potency (ChEMBL, top record) | pChEMBL | PAINS |
|---|---|---|---|---|---|
| CHEMBL4759667 | −9.71 | −9.71, −9.57, −9.34 | IC50 0.025 nM | 10.60 | none |
| Sildenafil (query) | −9.35 | −9.35, −9.25, −9.07 | IC50 1.0 nM (top ChEMBL record; literature 3.5 nM) | 9.00 | none |
| Vardenafil (CHEMBL1520) | −9.30 | −9.30, −8.86, −8.85 | IC50 0.029 nM | 10.54 | none |
| CHEMBL298295 | −8.93 | −8.93, −8.62, −8.55 | IC50 0.1 nM | 10.00 | none |
| CHEMBL1094544 | −7.90 | −7.90, −7.72, −7.71 | IC50 0.07 nM | 10.15 | none |

All five docks are on 1TBF (1.30 Å), grid centre exactly on the co-crystallised sildenafil centroid (0.00 Å). CHEMBL4759667 is a sulfoximine analogue of the vardenafil scaffold; CHEMBL298295 is a sildenafil-like pyrazolopyrimidinone; CHEMBL1094544 is a structurally distinct pyrazolo-pyrimidine. All five are sub-nanomolar by their top ChEMBL record — the measured-potency spread is 1.6 log units (40-fold), while the Vina spread is 1.81 kcal/mol, barely outside the ±1–2 kcal/mol noise. Pose consistency is good across the set (top-three poses within ~0.4 kcal/mol for every compound except vardenafil at 0.45).

### 3.2 Comparison with published docking

Published sildenafil Vina scores on other PDE5 structures are weaker than ours (−8.1 kcal/mol on 6L6E in a 2024 study, where a plant-derived candidate scored −8.8), while our re-dock gives −9.35 kcal/mol on 1TBF. As in Paper #37, absolute Vina scores are protocol- and structure-dependent and cannot be compared across studies; only the within-protocol ranking in Table 3.1 is interpretable.

### 3.3 The standardisation problem: sildenafil is the outlier

The Vina order (best first) is CHEMBL4759667 > sildenafil > vardenafil > CHEMBL298295 > CHEMBL1094544. The measured-potency order (pChEMBL, best first) is CHEMBL4759667 > vardenafil > CHEMBL1094544 > CHEMBL298295 > sildenafil. Spearman ρ = +0.30 (n = 5) — a weak positive correlation carried entirely by the top compound: CHEMBL4759667 leads on both measures, but sildenafil, second by Vina, is last by measured potency, and CHEMBL1094544, last by Vina, is third by measurement. Two cautions sharpen the point. First, the "measured" column mixes heterogeneous ChEMBL assays: the top record for each compound is a single-assay extreme (sildenafil's top record is IC50 1.0 nM; the widely cited head-to-head value is 3.5 nM; vardenafil's top record is 0.029 nM against a head-to-head literature value of 0.14 nM). Rank orders built from single-assay maxima are fragile. Second, none of this touches PDE6: all five compounds could be potent PDE5 inhibitors and still fail the selectivity test that matters clinically. The 2025 xanthine repurposing study makes the same point from the other side — its best candidate, linagliptin, was advanced on binding stability and free energy, not on raw docking score.

Drug-likeness is unremarkable across the set: MW 357–509, logP 1.61–2.81, zero Lipinski violations except CHEMBL4759667 (MW 508.63, one violation). No Tox21 flags were predicted for any compound by kNN read-across — but that is a prediction, not a measurement, and must not be read as a safety claim, especially for a sulfoximine (CHEMBL4759667), a functional group with a thin clinical record.

## 4. Discussion

### 4.1 The reframe

The result is not "a new PDE5 inhibitor beats sildenafil" — it is that PDE5 potency is a solved problem and docking adds little to it. The best Vina scorer is also the best measured binder, which is encouraging, but the correlation across the set is weak (ρ = +0.30), the reference drug is the single biggest outlier, and the Vina spread barely exceeds noise. The paper's real contribution is the reframing: for PDE5, the endpoint that decides whether a lead matters is the PDE5/PDE6 selectivity ratio, and a PDE5-only docking screen cannot measure it. Any follow-up that assays PDE5 potency alone would be answering a question nobody needs answered.

### 4.2 Why the "win" must not be over-read

Three reasons. First, CHEMBL4759667 beats sildenafil by 0.36 kcal/mol — inside noise. Second, the compound is a close vardenafil analogue (sulfoximine in place of vardenafil's sulfonyl-piperazine), so it inherits the known scaffold's liabilities, including vardenafil's own poor PDE6 selectivity; there is no reason to expect it to be more selective. Third, the measured potencies are single-assay ChEMBL maxima, not head-to-head values — the ranking could change on a single plate.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

No PAINS alerts were found. The validation assay still needs a PDE6 counter-screen as its primary readout, plus standard detergent/aggregation controls, because the leads are lipophilic heterocycles and apparent potency without a counter-screen is uninterpretable for this target.

### 4.4 Testable hypotheses

1. In a paired PDE5/PDE6 inhibition assay on the same plate, CHEMBL4759667's PDE5/PDE6 selectivity ratio will not exceed sildenafil's ~10-fold. Refuted if it is ≥50-fold.
2. Head-to-head PDE5 IC50 values (same assay, same day) for the five compounds will correlate more strongly with the Vina ranking than the ChEMBL-maximum ranking does (ρ > 0.30). Refuted if ρ stays ≤ 0.30.
3. Docking the same five compounds into a PDE6 catalytic-domain model will rank sildenafil and vardenafil above CHEMBL4759667, i.e. the selectivity problem is visible in silico before any assay. Refuted if CHEMBL4759667 also leads on PDE6.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): paired PDE5 and PDE6 enzyme inhibition assays (commercial PDE assay kits, cGMP substrate) for CHEMBL4759667, sildenafil and vardenafil, 10-point dose–response in triplicate, same plate, same day — the deliverable is the selectivity ratio, not the PDE5 IC50. Stage 2 (weeks 4–6): if the ratio is <50-fold, stop — the lead is a potency me-too. If ≥50-fold, extend to a PDE selectivity panel (PDE1, PDE3, PDE4, PDE11) and a cGMP accumulation assay in pulmonary-artery smooth-muscle cells. Stage 3 (weeks 7–12): docking + short MD on a PDE6 homology model to test hypothesis 3, and a 6-minute-walk-equivalent functional readout only if a partner lab is available. Stop rule: a lead that is potent but not selective is a failure, not a publication.

## 5. Limitations

1. Docking only — no experimental data; no compound here is shown to inhibit PDE5 or PDE6 in any assay.
2. All Vina margins except the weakest compound are inside or near the ±1–2 kcal/mol noise; no ranking claim survives that.
3. Single rigid structure (1TBF, sildenafil-bound); no MD, no free-energy refinement, no induced-fit treatment.
4. "Measured" potencies are single-assay ChEMBL maxima from heterogeneous assays, not head-to-head values; the sildenafil and vardenafil figures differ from the widely cited head-to-head values (3.5 nM and 0.14 nM).
5. Rank correlation computed on n = 5 — fragile; one more compound could change it.
6. PDE6 selectivity — the paper's central question — was not measured or modelled here.
7. No local (Pakistan) market, pricing or access data were collected; sildenafil is off-patent and cheap, so a new PDE5 inhibitor needs a selectivity case, not a price case.

## 6. Conclusion

On the sildenafil-bound PDE5A structure 1TBF, a sulfoximine vardenafil analogue leads both the Vina ranking (−9.71 kcal/mol) and the measured-potency ranking (pChEMBL 10.60), but the overall correlation is weak (ρ = +0.30, n = 5) with sildenafil itself as the outlier, and every compound in the set is already sub-nanomolar. PDE5 potency is solved; the unmet need is PDE6 selectivity, which this screen cannot assess. The next step is a paired PDE5/PDE6 assay, and the lead only matters if its selectivity ratio beats sildenafil's ~10-fold.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received; all tools and data sources used are free and public (UniProtKB, ChEMBL, PubChem, RCSB PDB, AutoDock Vina).

## References

1. Galiè N, Ghofrani HA, Torbicki A, et al. Sildenafil citrate therapy for pulmonary arterial hypertension. N Engl J Med. 2005;353(20):2148–2157. doi:10.1056/NEJMoa050010
2. Ballard SA, Gingell CJ, Tang K, Turner LA, Price ME, Naylor AM. Effects of sildenafil on the relaxation of human corpus cavernosum tissue in vitro and on the activities of cyclic nucleotide phosphodiesterase isozymes. J Urol. 1998;159(6):2164–2171.
3. Zhang KYJ, Card GL, Suzuki Y, et al. A glutamine switch mechanism for nucleotide selectivity by phosphodiesterases. Mol Cell. 2004;15(2):279–286. PMID 15260978. doi:10.1016/j.molcel.2004.07.005
4. The molecular basis for the selectivity of tadalafil toward phosphodiesterase 5 and 6: a modeling study. J Chem Inf Model. doi:10.1021/ci400458z
5. Mechanism investigation of highly selective inhibitors toward phosphodiesterase 5 and 6 via the in vitro calculation and simulation. Front Chem. 2024. doi:10.3389/fchem.2024.1400886
6. Molecular dynamics-assisted discovery of novel phosphodiesterase-5 inhibitors targeting a unique allosteric pocket. Molecules. 2025;30(3):588. doi:10.3390/molecules30030588
7. Elzupir AO, Almahmoud SAJ. Unveiling of phosphodiesterase-5 hot residues binding to xanthine derivatives for erectile dysfunction therapy: a computational drug repurposing approach. PLoS One. 2025;20(11):e0336267. doi:10.1371/journal.pone.0336267
8. Molecular docking and dynamics simulation analysis of PDE5 inhibitor candidates for erectile dysfunction treatment. Eur Rev Med Pharmacol Sci. 2024. (Boesenbergin A −8.8 vs sildenafil −8.1 kcal/mol on PDB 6L6E.)
9. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. J Chem Inf Model. 2021;61(8):3891–3898. doi:10.1021/acs.jcim.1c00203
10. Protein Data Bank. Catalytic domain of human phosphodiesterase 5A in complex with sildenafil. PDB ID 1TBF, resolution 1.30 Å. https://www.rcsb.org/structure/1TBF

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-050-2026-11-10.json`. Target: UniProt O76074; ChEMBL target CHEMBL1827; structure PDB 1TBF; compounds: sildenafil (ChEMBL192, PubChem CID 5212), vardenafil (CHEMBL1520), CHEMBL4759667, CHEMBL298295, CHEMBL1094544. Sildenafil's ChEMBL top PDE5 record (pChEMBL 9.00, IC50 1.0 nM, assay CHEMBL4398716) was fetched separately because the pipeline records no measured activity for the query compound itself. No additional data were generated.
