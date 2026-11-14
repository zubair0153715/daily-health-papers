# Rigid Docking Gets the Extremes Right on SARS-CoV-2 Mpro: the 0.04 nM Analogue Scores Best and Nirmatrelvir Ties for Last

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification.**

**Author:** Zubair Ali, Pharm-D student, Faculty of Pharmacy, SMBBMU, Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 14 November 2026
**Topic ID:** HP-037

## Abstract

Nirmatrelvir, the active component of Paxlovid, is a covalent inhibitor of the SARS-CoV-2 main protease (Mpro, nsp5). We benchmarked rigid AutoDock Vina docking against measured inhibition data for nirmatrelvir and four analogues (Ki 0.04–3.1 nM), docked into the nirmatrelvir-bound structure 7SI9 (2.0 Å). This is the first positive rank correlation in this series: Spearman ρ = +0.48 (n = 5). The most potent analogue (Ki 0.04 nM) scored best (−8.79 kcal/mol), nirmatrelvir itself (Ki 3.1 nM, consensus of ten ChEMBL records) tied for last (−8.22 kcal/mol), and the re-dock control worked — nirmatrelvir re-docked into its own crystal structure with tight poses (−8.22, −8.21, −7.93 kcal/mol). But the method compresses the differences: the measured potencies span 77-fold (~2.6 kcal/mol) while the docking scores span only 0.57 kcal/mol, so the middle of the ranking is noise. Two pipeline lessons are recorded: the first automated run used the wrong ChEMBL target (maltase-glucoamylase) and the wrong structure (the NSP3 macrodomain), with every dock failing; and the pipeline's top activity record for nirmatrelvir (Ki 0.26 nM) is an outlier against ten records at 3.0–3.11 nM. Rigid docking can rank Mpro analogues at the extremes, but not in the middle — and it cannot score the covalent bond that does much of the work.

**Keywords:** SARS-CoV-2; main protease; Mpro; nirmatrelvir; Paxlovid; molecular docking; AutoDock Vina; covalent inhibitor

## Introduction

COVID-19 has caused ~1.58 million confirmed cases and 30,656 deaths in Pakistan (National Institute of Health data, 2023), and the virus continues to circulate. The main protease (Mpro, also called 3CLpro, nsp5) cleaves the viral polyprotein at eleven sites and is essential for replication; it has no close human homologue, which makes it a selective antiviral target. Nirmatrelvir (PF-07321332) is a peptidomimetic nitrile that binds covalently to the catalytic Cys145 as a thioimidate; co-dosed with ritonavir — a CYP3A4 inhibitor that raises nirmatrelvir's plasma exposure — it is Paxlovid, the first oral antiviral for COVID-19 (Owen et al., *Science* 2021). Ritonavir's role is pharmacokinetic, not antiviral: it fixes nirmatrelvir's metabolism, not its target binding.

This paper benchmarks rigid docking for nirmatrelvir and four close analogues from a 2024 optimisation study (Ghosh et al., *Eur J Med Chem* 2024), and asks whether docking can rank a congeneric series of covalent inhibitors. The honest difficulty is stated up front: Vina scores non-covalent complementarity only, while these compounds' potency includes a covalent bond to Cys145. The comparison is fair in one respect — all five share the same nitrile warhead, so potency differences should track non-covalent interactions — and unfair in another, since the covalent contribution is invisible to the method.

## Methods

### 2.1 Target and compound selection

SARS-CoV-2 Mpro (nsp5, residues 3264–3569 of the replicase polyprotein 1ab, UniProt P0DTD1) was resolved to ChEMBL target CHEMBL4523582, which holds 6,220 IC50 activities. The reference compound was nirmatrelvir (PubChem CID 155903259; C23H32F3N5O4, MW 499.53). The pipeline ranked 26 leads; the docking set is nirmatrelvir plus four analogues. All five are PAINS-clean. One pipeline entry was deduplicated: CHEMBL4802135 is nirmatrelvir itself (verified pref_name), so it was excluded as a duplicate of the QUERY.

### 2.2 Structure: the first run used the wrong target and the wrong structure

The first automated run failed twice over. The ChEMBL text search returns an unfiltered list (the same irrelevant results for every query — maltase-glucoamylase first), and the pipeline picked CHEMBL2074 (human maltase-glucoamylase) as the target; its "Mpro leads" were α-glucosidase inhibitors. It then docked them into 8AZC — the SARS-CoV-2 NSP3 macrodomain in apo form (0.93 Å), not Mpro — and every dock failed ("pdb parse failed"). The run was discarded in full. The corrected run reached CHEMBL4523582 by querying the pipeline with the UniProt accession P0DTD1, and used 7SI9 (2.0 Å), the room-temperature Mpro structure in complex with nirmatrelvir (Kneller et al., *Nat Commun* 2022;13:2268; PMID 35477935). The docking centre was the co-crystallised nirmatrelvir adduct centroid (ligand 4WI, chain A, [−10.40, 39.82, −17.96]) — the active site, at Cys145. All docking used AutoDock Vina 1.2.7, exhaustiveness 8, box 22.5 Å.

### 2.3 Limitations of the docking model, stated in advance

**Covalent inhibition is unmodelled.** Nirmatrelvir and all four analogues carry the same nitrile warhead, which forms a covalent thioimidate with Cys145; Vina scores only the non-covalent pose. The crystal ligand 4WI is itself the covalent adduct (the imino form), so the re-dock is a shape check, not a binding-energy check. Rigid docking carries a documented ±1–2 kcal/mol noise band, and the docking spread here (0.57 kcal/mol) is inside it. The measured Ki values come from different assays: nirmatrelvir's consensus is 3.1 nM (ten ChEMBL records at 3.0–3.11 nM), but the pipeline's top record gave 0.26 nM and is treated as an outlier; CHEMBL5178656 has Ki records at both 0.44 nM and 7.0 nM, and an IC50 of 100 nM in its original 2022 paper. The rank correlation uses only five compounds.

### 2.4 Literature

Measured potencies were taken from ChEMBL (accessed 14 November 2026) and verified against the source documents. The 7SI9 structure, the nirmatrelvir mechanism and the ritonavir-boosting rationale are from the primary literature. Pakistan case figures are from National Institute of Health data (2023).

## Results

### 3.1 The compounds

The five compounds are a congeneric series: nirmatrelvir plus four P1/P4 analogues from Ghosh et al. (2024) (Table 1). CHEMBL5574604 replaces the P1 γ-lactam with a six-membered δ-lactam (Ki 0.04 nM, a single assay record). CHEMBL5589941 replaces the P4 trifluoroacetyl group with trichloroacetyl (Ki 0.2 nM). CHEMBL5178656 replaces the P4 trifluoroacetyl with acetyl (Ki 0.44 nM in the 2024 paper; 7.0 nM in a second record; IC50 100 nM in its 2022 paper). CHEMBL5590149 is a further P1/P4 analogue (Ki 1.1 nM). Their measured potencies span 0.04–3.1 nM, a 77-fold range equivalent to ~2.6 kcal/mol at 298 K.

**Table 1. Nirmatrelvir and four analogues docked on 7SI9 (Mpro–nirmatrelvir complex, 2.0 Å).**

| Compound | Measured Ki (nM) | Modification vs nirmatrelvir | Vina score (kcal/mol) | Top-3 poses |
|---|---|---|---|---|
| CHEMBL5574604 | 0.04 | P1 δ-lactam | −8.79 | −8.79, −8.21, −7.70 |
| CHEMBL5590149 | 1.1 | P1/P4 analogue | −8.52 | −8.52, −7.80, −7.32 |
| CHEMBL5178656 | 0.44 | P4 acetyl | −8.32 | −8.32, −7.53, −7.30 |
| Nirmatrelvir (QUERY) | 3.1 | — | −8.22 | −8.22, −8.21, −7.93 |
| CHEMBL5589941 | 0.2 | P4 trichloroacetyl | −8.22 | −8.22, −7.24, −7.17 |

### 3.2 The extremes are right; the middle is noise

The rank correlation was Spearman ρ = +0.48 (n = 5) — the first positive correlation in this series. The most potent analogue (0.04 nM) scored best (−8.79 kcal/mol), and the least potent, nirmatrelvir itself (3.1 nM), tied for last (−8.22 kcal/mol). But the ordering in between is wrong: the 1.1 nM compound ranked second (−8.52), ahead of the 0.44 nM (−8.32) and 0.2 nM (−8.22) compounds. And the whole docking spread is only 0.57 kcal/mol, against a 2.6 kcal/mol measured range: the method compresses the differences by a factor of four. The re-dock control worked — nirmatrelvir's three poses were tight (−8.22, −8.21, −7.93) — so the failure is not pose instability; it is that non-covalent scoring cannot resolve potency differences that depend partly on covalent-bond formation kinetics, which vary with the P1/P4 groups.

### 3.3 The discarded first run

The first run's failure is worth one paragraph because it is a pipeline failure, not a science failure. A text search that returns the same irrelevant list for every query will eventually pick the wrong target — here, maltase-glucoamylase for a viral protease — and a structure picker that trusts the target will then dock into whatever structure the wrong target suggests — here, the NSP3 macrodomain. Both errors were caught because the target name, the structure title and the dock failures were all checked by hand. Automated pipelines that do not check these will publish α-glucosidase inhibitors as Mpro inhibitors.

## Discussion

Two findings, one encouraging and one limiting.

**First, this is the best docking result in the series — and it is still weak.** A positive ρ (+0.48) with the extremes correct and a working re-dock control shows that rigid docking into a high-resolution, ligand-bound structure (2.0 Å, the native ligand's own pocket) carries real signal for Mpro. The 0.04 nM δ-lactam analogue scoring best is a genuine prediction worth testing. But a 0.57 kcal/mol spread for a 2.6 kcal/mol measured range means the method cannot rank the middle of the series: the 0.2, 0.44 and 1.1 nM compounds are indistinguishable to it, and two of the five are misordered. For analogue prioritisation, docking can shortlist the best candidate and discard the worst, but it cannot order the rest.

**Second, the covalent bond is the unmeasured variable.** All five compounds share the nitrile warhead, so in principle the Ki differences should track non-covalent fit — but covalent inhibition also depends on the warhead's reactivity and the geometry of attack, which the P1/P4 groups influence and Vina cannot see. The δ-lactam analogue's 77-fold advantage over nirmatrelvir (0.04 vs 3.1 nM) is far larger than its 0.57 kcal/mol docking advantage, which suggests much of its gain is in the covalent step or in interactions the rigid model misses. A covalent docking method (or a QM/MM estimate of the thioimidate formation) is the correct next step for this series, not more Vina runs.

For Pakistan, the practical point is that nirmatrelvir remains the available drug (as Paxlovid, with ritonavir boosting), and analogues like the δ-lactam compound are preclinical leads, not alternatives a clinician can use. The value of this benchmark is for the next round of analogue design: dock to shortlist, assay to rank, and model the covalent step explicitly.

## Limitations

1. **No lab data.** All results are computational; no Mpro assay was run.
2. **Covalent bond unmodelled.** Vina scores non-covalent complementarity only; the Cys145 thioimidate is invisible to it.
3. **Small n.** The rank correlation uses five compounds from one congeneric series; a single additional compound could change ρ substantially.
4. **Assay heterogeneity.** Ki values come from different papers and assays; CHEMBL5178656 has records at 0.44 nM, 7.0 nM and IC50 100 nM, and nirmatrelvir's pipeline record (0.26 nM) disagrees with ten records at 3.0–3.11 nM.
5. **Single-assay potencies.** The 0.04 nM and 0.2 nM values each rest on one assay record.
6. **Rigid docking, ±1–2 kcal/mol noise.** The 0.57 kcal/mol docking spread is inside the noise band.
7. **No RMSD for the re-dock.** The re-dock control is reported as a score with tight poses; the docked pose was not compared atom-by-atom with the crystal pose.

## Conclusion

Rigid docking into the nirmatrelvir-bound Mpro structure 7SI9 gives the first positive rank correlation in this series (Spearman ρ = +0.48, n = 5): the 0.04 nM analogue scores best (−8.79 kcal/mol), nirmatrelvir ties for last (−8.22 kcal/mol), and the re-dock control works. But the method compresses a 77-fold measured potency range into a 0.57 kcal/mol score range and misorders the middle of the series, and it cannot score the covalent bond that defines these inhibitors. Docking can shortlist Mpro analogues at the extremes; ranking them needs assays and covalent modelling. The discarded first run — wrong target, wrong structure, all docks failed — is a reminder that automated pipelines need a human check on the target and the structure before any score is believed.

## Acknowledgments

Manuscript drafted with AI assistance (Lapis). The author reviewed all computed values against the raw docking outputs and all citations against the primary sources. This is an AI-assisted draft, not a peer-reviewed publication; all claims require independent laboratory verification. No funding was received. The author declares no conflicts of interest.

## References

1. Owen DR, et al. An oral SARS-CoV-2 Mpro inhibitor clinical candidate for the treatment of COVID-19. *Science*. 2021;374(6575):1586–1593. PMID: 34726479. doi:10.1126/science.abl4784.
2. Ghosh AK, et al. Exploration of P1 and P4 modifications of nirmatrelvir: design, synthesis, biological evaluation, and X-ray structural studies of SARS-CoV-2 Mpro inhibitors. *Eur J Med Chem*. 2024;267:116132. PMID: 38335815. doi:10.1016/j.ejmech.2024.116132.
3. Kneller DW, et al. Covalent narlaprevir- and boceprevir-derived hybrid inhibitors of SARS-CoV-2 main protease. *Nat Commun*. 2022;13:2268. PMID: 35477935. doi:10.1038/s41467-022-29915-z.
4. Chia CSB, et al. Novel coronavirus main protease di- and tripeptide inhibitors for treating COVID-19. *ACS Med Chem Lett*. 2022;13(9):1388–1389. PMID: 36105347. doi:10.1021/acsmedchemlett.2c00332.
5. National Institute of Health, Pakistan. COVID-19 data, 2023. ~1.58 million confirmed cases; 30,656 deaths.

## Data Availability

All docking outputs are available from the author on request. Pipeline output: `dock-HP-037-2026-11-14.json` (corrected target, CHEMBL4523582 via UniProt P0DTD1); docking: `dock-HP-037-2026-11-14-7SI9.json` (7SI9, nirmatrelvir-centred). The discarded first run (wrong target CHEMBL2074, wrong structure 8AZC) is documented in the Methods and is not used. Structure: PDB 7SI9 (2.0 Å). Measured potencies: ChEMBL target CHEMBL4523582, accessed 14 November 2026 (documents CHEMBL5543094, CHEMBL5143762, CHEMBL5137053). Compound structures: nirmatrelvir (ChEMBL4802135); ChEMBL IDs CHEMBL5574604, CHEMBL5589941, CHEMBL5178656, CHEMBL5590149.
