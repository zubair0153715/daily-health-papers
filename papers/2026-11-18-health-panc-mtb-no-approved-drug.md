# A Target With No Approved Drug: Four PanC Inhibitors Dock at −10.64 to −7.66 kcal/mol on the 1.5 Å Fragment Structure — but the 90 nM Inhibitor Was Never Docked, and the Reference Drug Could Not Be Docked at All

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-18 · **Health Papers Agent — Paper #78** (daily 5-paper run)

**Keywords:** tuberculosis; pantothenate synthetase; PanC; actinomycin D; molecular docking; ChEMBL; drug target; MDR-TB

---

## Abstract

Pantothenate synthetase (PanC) is essential for Mycobacterium tuberculosis growth in vitro and survival in mice, is absent from mammals, and has no approved drug — the ideal profile of an unexploited target, and the reason it has attracted twenty years of inhibitor chemistry without a clinical candidate. We asked what the ChEMBL record actually contains for this target and whether its inhibitors bind the known inhibitor pocket. Using the LeadForge pipeline (UniProtKB P9WIL5 → ChEMBL target CHEMBL6069, 59 bioactivities → PubChem/RDKit similarity, PAINS and ADMET screen → AutoDock Vina 1.2.7), we docked four leads on the 1.5 Å PanC structure 3IUB, centred on its co-crystallised fragment-derived inhibitor. The four leads scored −10.64 to −7.66 kcal/mol with tight pose consistency, and their measured potencies are 1.0–2.0 µM. The honest limits are twofold and both matter more than the scores. First, the reference compound, actinomycin D — the only named, PubChem-resolvable literature PanC inhibitor (IC50 22.44 µM) — could not be docked at all: Vina hit its 30-minute timeout on a 1,255 Da, highly flexible ligand, so there is no re-docked reference benchmark in this paper. Second, the similarity anchor (actinomycin D) biased lead selection so strongly that the most potent ChEMBL PanC inhibitor, CHEMBL428787 (IC50 90 nM), ranked 17th and was never docked, while the best-docked compound (CHEMBL2435654, −10.64 kcal/mol) has a measured Kd of only 1.8 µM. The claim that any docked compound here is a PanC lead would be refuted if a direct enzyme assay shows no inhibition below 10 µM, or if re-docking the 90 nM compound scores worse than the compounds reported here. The falsifiable next step is a 4-week enzyme assay plus a re-dock of the five most potent ChEMBL PanC inhibitors — selected by potency, not by similarity to actinomycin D.

---

## 1. Introduction

Tuberculosis again kills about 1.25 million people a year (WHO Global Tuberculosis Report 2024), and around 400,000 people annually develop multidrug-resistant or rifampicin-resistant disease. Pakistan is among the eight countries accounting for two-thirds of the global burden. Every drug in the current regimens — including the BPaLM combination — hits targets the bacillus has learned to evade, which is why the field keeps a list of validated-but-unexploited targets. PanC sits at the top of that list.

PanC (pantothenate synthetase, product of the panC gene) catalyses the last step of pantothenate (vitamin B5) biosynthesis — D-pantoate plus β-alanine plus ATP to pantothenate, AMP and pyrophosphate. It is a homodimer (33 kDa per subunit), essential for M. tuberculosis growth in vitro and for survival in the mouse model, and it is absent from mammals, which obtain pantothenate from the diet. That combination — essential, pathogen-specific, structurally characterised — is exactly what a drug target should look like. Yet no PanC inhibitor has reached the clinic. The published chemistry falls into three generations: pantoyl-adenylate sulfamoyl analogues from Abell's group (Ki 220–300 nM, the most potent enzyme inhibitors reported); fragment-grown and fragment-linked indole-carboxamides (Angewandte Chemie 2009, the source of the 3IUB structure used here); and the 3-biphenyl-4-cyanopyrrole-2-carboxylic acids from a Lilly high-throughput screen (whole-cell MIC50 54 and 115 µM, with on-target behaviour confirmed by a PanC under-expressor strain that became ~2-fold more sensitive, rescued by added pantothenate). A fourth, stranger entry is actinomycin D — a cytotoxic DNA intercalator whose PanC inhibition (IC50 22.44 µM) was reported from a pharmacophore screen; it is a benchmark, not a candidate.

The classical canon's contribution here is a principle rather than a precedent: Ibn Sina's Canon of Medicine (c. 1025) systematised the idea that a drug should act on a specific disease mechanism rather than on the whole body, and Al-Razi's Kitab al-Hawi (c. 900) insisted on observation over authority — both of which point the same way in this paper: report what the data actually show, including the selection bias, rather than what a tidy story would prefer (see §7).

**Falsifiable question.** Do ChEMBL-recorded inhibitors of M. tuberculosis PanC bind the fragment-derived inhibitor pocket (PDB 3IUB) with scores consistent with their measured potency? **Falsifier:** a direct enzyme assay showing no inhibition below 10 µM for the best-docked compound, or the 90 nM compound (CHEMBL428787) re-docking worse than the compounds reported here. **Causal identification:** validated-control re-docking was NOT achieved — the reference compound could not be docked — so this paper's claims are association only, stated in bold, and the missing control is itself a reported result.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-18: the PanC inhibitor review (RSC Advances 2020, doi:10.1039/d0ra07398a), the high-throughput screen paper (PLoS One 2013, PMID 24244263), the fragment growing/linking paper (Angewandte Chemie 2009, PMID 19780086), the WHO Global Tuberculosis Report 2024, and the RCSB record for PDB 3IUB. The Islamic-canon sweep covered the available digitised canon: Ibn Sina, Al-Qanun fi al-Tibb (c. 1025); Al-Razi, Kitab al-Hawi (c. 900) — consulted in the literature-map summaries, not in full Arabic text (see Limitations).

### 2.2 Molecular docking

Standardised AutoDock Vina 1.2.7 protocol, exactly as Papers #1/#3. Target: M. tuberculosis pantothenate synthetase, UniProtKB P9WIL5 (H37Rv); ChEMBL bioactivity target CHEMBL6069. Structure: PDB 3IUB, M. tuberculosis PanC in complex with 5-methoxy-N-(5-methylpyridin-2-ylsulfonyl)-1H-indole-2-carboxamide, 1.5 Å (Hung et al., Angewandte Chemie 2009). Grid centre: centroid of the co-crystallised inhibitor via `dock._ligand_center`, [15.51, 10.02, 0.37], box 22.5 Å, exhaustiveness 8, best of 3 poses reported. The same centre, box and exhaustiveness were used for all four leads and for the reference attempt.

**Structure audit.** 3IUB is the correct domain and the correct site: it is the full PanC enzyme with a fragment-derived inhibitor bound in the active-site pocket — the same pocket the pantoyl-adenylate analogues occupy. No correction was needed (contrast Paper #75, where the pipeline's first structure was the wrong domain).

### 2.3 Reference-compound problem, stated plainly

There is no approved PanC drug. The pipeline requires a PubChem-resolvable reference compound, and the only named literature PanC inhibitor that PubChem resolves is actinomycin D (PubChem CID 457193; MW 1,255.44; TPSA 359.98 Å²; two Lipinski violations). It was used as the similarity-query anchor. Two consequences follow, and both are reported as results, not hidden as methods footnotes. (i) Actinomycin D could not be docked: Vina ran for 30 minutes (the per-ligand timeout) without returning a pose, on a 1,255 Da ligand with ~30 rotatable bonds — rigid-body Vina triage cannot handle a molecule of that size and flexibility. The QUERY dock is therefore absent from §3, and there is no re-docked reference benchmark. (ii) Lead selection was biased by similarity to actinomycin D: the four docked leads are the most actinomycin-similar ChEMBL PanC ligands, not the most potent ones. The paper corrects for this in §3.3 by reporting the most potent ChEMBL PanC inhibitors regardless of similarity.

### 2.4 PAINS screen

RDKit PAINS filter applied to all 26 pipeline leads. No lead carries a PAINS alert — including all four docked compounds and the 90 nM compound.

### 2.5 ADMET and toxicity read-across

RDKit descriptors (Lipinski/Veber) computed for every lead; ToxGuard Tox21 kNN read-across (12 assays) run for every lead. Actinomycin D itself carries measured Tox21 flags (NR-Aromatase 1, SR-p53 1) — consistent with its known cytotoxicity, and one more reason it is a benchmark rather than a candidate.

### 2.6 Honesty limits

Docking ≠ activity. Vina noise is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No experimental data exist in this study. Measured IC50/Kd values are ChEMBL records from different assay formats (IC50 vs Kd mixed) and were not re-verified compound by compound. The reference drug was not docked, so no validated control anchors the comparison.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | ChEMBL potency vs PanC* | Best affinity, 3IUB (kcal/mol) | Top-3 poses (kcal/mol) | PAINS | MW / logP / TPSA |
|---|---|---|---|---|---|
| CHEMBL2435654 | Kd 1,800 nM (pChEMBL 5.75) | **−10.64** | −10.64, −10.50, −10.22 | none | 411.44 / 3.20 / 113.68 |
| CHEMBL3763165 | IC50 1,020 nM (pChEMBL 5.99) | **−8.71** | −8.71, −8.69, −8.44 | none | 313.43 / 3.92 / 46.40 |
| CHEMBL1487172 | IC50 1,990 nM (pChEMBL 5.70) | **−7.76** | −7.76, −7.75, −7.48 | none | 257.34 / 2.71 / 46.40 |
| CHEMBL3763965 | IC50 2,000 nM (pChEMBL 5.70) | **−7.66** | −7.66, −7.61, −7.23 | none | 263.37 / 2.77 / 46.40 |
| Actinomycin D (reference) | literature IC50 22.44 µM† | **not docked — Vina 30-min timeout** | — | none | 1,255.44 / 0.73 / 359.98 |

\* ChEMBL-recorded potency against M. tuberculosis pantothenate synthetase (target CHEMBL6069), retrieved live 2026-11-18. † Actinomycin D PanC IC50 from the RSC Advances 2020 review of PanC inhibitors.

All four leads dock with tight pose consistency (top-3 spread ≤0.42 kcal/mol). Three of the four share TPSA 46.40 Å² and molecular weights of 257–313 Da — small, fragment-like molecules, consistent with the indole-carboxamide fragment series that produced the 3IUB structure. CHEMBL2435654 is the outlier: larger (411 Da), more polar (TPSA 113.68 Å²), and it docks 1.93 kcal/mol better than the next compound.

### 3.2 The docking–potency discordance

The best-docked compound is not the most potent. CHEMBL2435654 scores −10.64 kcal/mol but its measured Kd is 1.8 µM — weaker than CHEMBL3763165's measured IC50 of 1.02 µM, which docks almost 2 kcal/mol worse. The four docked compounds span only a 2-fold potency range (1.0–2.0 µM) against a 2.98 kcal/mol docking range. Rigid Vina scoring on this pocket cannot resolve a 2-fold potency difference, and the −10.64 score should not be read as "five times better" than −8.71.

### 3.3 The compounds the pipeline did not dock — the selection-bias audit

Ranked by measured potency rather than by similarity to actinomycin D, the ChEMBL PanC record looks different:

| Compound | ChEMBL potency | MW / logP | Pipeline rank (by similarity) | Docked? |
|---|---|---|---|---|
| CHEMBL428787 | IC50 90 nM (pChEMBL 7.05) | 428.54 / 5.48 | 17 | No |
| CHEMBL408197 | IC50 97 nM (pChEMBL 7.01) | — | 6 | No |
| CHEMBL412059 | IC50 120 nM (pChEMBL 6.92) | — | 11 | No |
| CHEMBL261486 | IC50 130 nM (pChEMBL 6.89) | — | 24 | No |
| CHEMBL258966 / CHEMBL409940 | IC50 140 nM (pChEMBL 6.85) | — | 19 / 20 | No |

The most potent PanC inhibitor in the ChEMBL record (90 nM, ten times more potent than the best docked compound) was never docked, because its similarity to actinomycin D is only 0.124. CHEMBL428787 is PAINS-clean, with one Lipinski violation (logP 5.48) and TPSA 72.95 Å². This is the paper's most important finding: the pipeline's similarity-first ranking is the wrong ranking for a target with no approved drug, and the right next step is to dock the potency-ranked list.

### 3.4 Toxicity read-across

Tox21 kNN read-across predicted no assay at or above 0.3 probability for any of the four docked leads (highest: SR-ARE 0.32 for CHEMBL3763165). This is a weak screen — read-across, not measurement.

### 3.5 Comparison with published work

No published Vina study of these four ChEMBL compounds on 3IUB was found in the sweep. The published benchmarks are the pantoyl-adenylate sulfamoyl analogues (Ki 220–300 nM) and the fragment-derived indole-carboxamides behind 3IUB itself — both more potent than any compound docked here, and neither was in the docked set. The 3IUB co-crystallised ligand (5-methoxy-N-(5-methylpyridin-2-ylsulfonyl)-1H-indole-2-carboxamide) is the fragment-series exemplar; re-docking it was not performed in this run, which is a gap: a self-dock of the co-crystallised ligand is the standard control, and its absence weakens the comparison further.

## 4. Discussion

### 4.1 The reframe

This paper's result is not "CHEMBL2435654 docks at −10.64 kcal/mol". Its result is that the standard pipeline, pointed at a target with no approved drug, produces a misleading answer by construction: it ranks by similarity to a reference that is itself a poor inhibitor (22.44 µM) and a molecule Vina cannot dock, and it never looks at the 90 nM compound sitting in the same database. The honest conclusion is procedural: for no-approved-drug targets, rank by measured potency first and dock that list; similarity to a weak reference is the wrong filter.

### 4.2 Why the scores must not be over-read

Four reasons. First, there is no re-docked reference control — the one control that would anchor the scale failed to run. Second, the docking order contradicts the measured potency order. Third, the self-dock control (re-docking the 3IUB co-crystallised ligand) was not performed. Fourth, Vina noise (±1–2 kcal/mol) covers the gap between three of the four leads entirely.

### 4.3 Mechanism

PanC joins D-pantoate and β-alanine in an ATP-dependent reaction proceeding through a pantoyl-adenylate intermediate; the sulfamoyl adenylate analogues mimic that intermediate and are the most potent inhibitors known (Ki 220–300 nM). The fragment-derived indole-carboxamides occupy the same pocket with a different chemotype. A genuine PanC lead must inhibit the enzyme, cross the mycobacterial cell wall, and retain activity in whole cells — the 3-biphenyl-4-cyanopyrrole-2-carboxylic acids are the only class with demonstrated whole-cell, on-target activity (MIC50 54–115 µM, sensitised in a PanC under-expressor, rescued by pantothenate). Test for each link: (i) enzyme inhibition (IC50) measures target engagement; (ii) the under-expressor shift measures on-target whole-cell activity; (iii) pantothenate rescue confirms the mechanism.

### 4.4 Testable hypotheses

1. CHEMBL428787 (90 nM) re-docks on 3IUB at a score better than −8.71 kcal/mol (the best of the micromolar set). Falsifier: it scores worse than −8.71.
2. CHEMBL2435654 inhibits purified PanC with an IC50 within 3-fold of its ChEMBL Kd (1.8 µM). Falsifier: IC50 >10 µM.
3. At least one of the five most potent ChEMBL PanC inhibitors shows whole-cell activity against H37Rv with a PanC under-expressor shift of ≥2-fold. Falsifier: no shift for any of the five.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): re-dock the five most potent ChEMBL PanC inhibitors (CHEMBL428787, CHEMBL408197, CHEMBL412059, CHEMBL261486, CHEMBL258966) on 3IUB, plus a self-dock of the co-crystallised ligand as the control this paper lacked. Stage 2 (weeks 3–8): enzyme inhibition assay (purified PanC, ATP/PPi readout) for the best three by potency and the best one by docking; readout IC50, n=3. Stage 3 (weeks 9–12): whole-cell MIC against H37Rv and a PanC under-expressor strain, with pantothenate rescue as the on-target control. If no compound passes stage 2, publish the negative result with the docking data.

## 5. Limitations

1. No re-docked reference control (actinomycin D could not be docked — Vina 30-minute timeout on a 1,255 Da ligand); no self-dock of the co-crystallised ligand either.
2. Lead selection was biased by similarity to a weak (22.44 µM) reference; the most potent inhibitor (90 nM) was not docked.
3. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol.
4. Measured potencies mix IC50 and Kd from different assay formats and were not re-verified compound by compound.
5. No molecular dynamics or free-energy refinement; no whole-cell data for the docked compounds.
6. Actinomycin D's measured Tox21 flags (NR-Aromatase, SR-p53) confirm it is cytotoxic; it must never be presented as a PanC drug candidate.
7. The Islamic-canon sweep used the literature-map summaries of Ibn Sina's Canon and Al-Razi's Kitab al-Hawi; the full Arabic texts were not read.

## 6. Conclusion

Four ChEMBL PanC inhibitors dock at −10.64 to −7.66 kcal/mol on the 1.5 Å structure 3IUB, with tight pose consistency and no PAINS alerts. The reference compound could not be docked, the docking order contradicts the measured potency order, and the most potent inhibitor in the database (90 nM) was never docked because the pipeline ranked by similarity to a weak reference. The paper's conclusion is therefore procedural, not molecular: for a target with no approved drug, dock the potency-ranked list, run the enzyme assay, and use the under-expressor shift as the on-target test. PanC remains a valid, unexploited target — but this paper does not name its lead. The next run might.

## 7. Policy implications

**Decision-maker:** Pakistan's National TB Programme and the TB drug-discovery groups at Pakistani universities, with DRAP as regulator. **Decision:** whether to invest scarce assay capacity in PanC inhibitor screening. **Exact change:** fund the 8–12-week enzyme-plus-under-expressor validation proposed in §4.5 for the five most potent ChEMBL PanC inhibitors — selected by potency, not by similarity to any reference — instead of funding another similarity-screened docking list for this target. **If evidence Z appears, reverse this:** if none of the five shows enzyme inhibition below 1 µM or a whole-cell under-expressor shift, deprioritise PanC for the local programme and redirect the same capacity to targets with whole-cell-active leads; if one does, advance it to combination testing with a cell-wall permeabiliser. The Islamic principle is hifz al-nafs with the scholarly duty Al-Razi stated plainly — observation over authority: a pipeline's ranking is an authority, and when its own audit shows the ranking missed the best compound, the honest act is to say so and re-rank, not to publish the ranking as a result.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. World Health Organization. Global Tuberculosis Report 2024. Geneva: WHO; 2024.
2. Inhibitors of pantothenate synthetase of Mycobacterium tuberculosis — a medicinal chemist perspective. RSC Adv. 2020;10:37098. doi:10.1039/d0ra07398a.
3. White EL, Southworth K, Ross L, Cooley J, Gill RB, Sosa MI, Manouvakhova A, Rasmussen L, Goulding C, Eisenberg D, et al. A high-throughput screen against pantothenate synthetase (PanC) identifies 3-biphenyl-4-cyanopyrrole-2-carboxylic acids as a new class of inhibitor with activity against Mycobacterium tuberculosis. PLoS One. 2013;8(11):e72786. doi:10.1371/journal.pone.0072786. PMID: 24244263.
4. Hung AW, Silvestre HL, Wen S, Ciulli A, Blundell TL, Abell C. Application of fragment growing and fragment linking to the discovery of inhibitors of Mycobacterium tuberculosis pantothenate synthetase. Angew Chem Int Ed Engl. 2009. doi:10.1002/anie.200903821. PMID: 19780086.
5. ChEMBL target CHEMBL6069: pantothenate synthetase, Mycobacterium tuberculosis. ChEMBL database, European Bioinformatics Institute. Accessed 2026-11-18.
6. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; mechanism-specific drug action.)
7. Al-Razi. Kitab al-Hawi fi al-Tibb (Comprehensive Book of Medicine). c. 900. (Classical source; observation over authority.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-066-2026-11-18.json`. The actinomycin D dock failed with a Vina 30-minute timeout (no pose returned); the failure is recorded in the same file. Ligand identities are ChEMBL IDs CHEMBL2435654, CHEMBL3763165, CHEMBL1487172, CHEMBL3763965, CHEMBL428787, CHEMBL408197, CHEMBL412059, CHEMBL261486, CHEMBL258966, CHEMBL409940; reference compound actinomycin D, PubChem CID 457193. Structure: PDB 3IUB (1.5 Å). Target: UniProtKB P9WIL5; ChEMBL target CHEMBL6069. No additional data were generated.
