# Celecoxib Still Leads: A Dual-Isoform Vina Benchmark of Five COX-2 Inhibitors Shows Docking Selectivity Does Not Track Measured Selectivity

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-04 · **Health Papers Agent — Paper #6** (daily 5-paper run)

**Keywords:** COX-2; celecoxib; molecular docking; AutoDock Vina; selectivity; NSAID; cardiovascular risk; prostaglandin

---

## Abstract

Selective COX-2 inhibition was designed to relieve pain without the gastrointestinal injury of non-selective NSAIDs, but the class carries a cardiovascular question mark ever since rofecoxib was withdrawn in 2004. The PRECISION trial (24,081 patients) later showed celecoxib non-inferior to ibuprofen and naproxen for cardiovascular events (primary outcome 2.3% vs 2.7% vs 2.5%), yet the search for a more selective coxib continues. We asked whether standardised docking could rank five known potent COX-2 inhibitors against celecoxib on both isoforms, and whether docking selectivity tracks measured selectivity. Compounds came from ChEMBL bioactivities against human COX-2 (CHEMBL230), were screened with RDKit (Lipinski/Veber/PAINS) and a Tox21 kNN panel, and were docked with AutoDock Vina 1.2.7 into COX-2 (PDB 3LN1, 2.4 Å) and COX-1 (PDB 3KK6, 2.75 Å) at the co-crystallised celecoxib centroids, under an identical protocol. Celecoxib scored best on COX-2 (−12.28 kcal/mol); the closest lead, CHEMBL282093, scored −12.13 kcal/mol, within noise. Docking selectivity (COX-1 minus COX-2 affinity) ranged 0.47–2.17 kcal/mol and did not track measured selectivity: CHEMBL432945, measured only 5-fold selective (COX-2 IC50 1.0 nM vs COX-1 5.0 nM), had the second-best docking selectivity (2.00 kcal/mol), while CHEMBL186632, measured ~8,700-fold selective (0.44 nM vs 3,828 nM), had the worst (0.47 kcal/mol). The falsifiable next step is a paired COX-1/COX-2 enzyme inhibition assay for CHEMBL282093 and CHEMBL432945 under identical conditions: if docking selectivity predicted the ranking, CHEMBL432945 would out-select CHEMBL282093; the measured data already predict the opposite, and the assay would settle which signal to trust.

---

## 1. Introduction

Non-steroidal anti-inflammatory drugs (NSAIDs) relieve pain by blocking cyclooxygenase (COX) enzymes and prostaglandin synthesis, but blocking the constitutive isoform COX-1 injures the gastric mucosa, while blocking the inducible isoform COX-2 drives the anti-inflammatory effect. The coxibs were designed to exploit a single structural difference: at position 523, COX-1 carries a bulky isoleucine and COX-2 a smaller valine, opening a side pocket (lined by His90, Gln192, Leu352, Ser353, Tyr355, Arg513, Ala516, Phe518 and Val523) that the sulfonamide group of celecoxib occupies. Celecoxib — 4-[5-(4-methylphenyl)-3-(trifluoromethyl)-1H-pyrazol-1-yl]benzenesulfonamide (SC-58635) — was the first-in-class selective COX-2 inhibitor, identified by Penning et al. in 1997, and remains the only coxib on the market in most countries after rofecoxib (Vioxx) was withdrawn in 2004 for increased myocardial infarction and stroke.

The cardiovascular question was settled, as far as a trial can settle it, by PRECISION: 24,081 osteoarthritis and rheumatoid arthritis patients randomised to celecoxib 100–200 mg twice daily, ibuprofen 600–800 mg three times daily, or naproxen 375–500 mg twice daily. The primary composite outcome (cardiovascular death, non-fatal myocardial infarction, or non-fatal stroke) occurred in 2.3% of the celecoxib group, 2.5% of naproxen and 2.7% of ibuprofen (hazard ratio 0.93 vs naproxen and 0.85 vs ibuprofen, p < 0.001 for non-inferiority in both comparisons), while gastrointestinal events were 54% higher with ibuprofen and 41% higher with naproxen than with celecoxib. Celecoxib is therefore non-inferior on the heart and better on the gut — but a more selective coxib could, in principle, widen both margins, and the field still lacks a cheap computational screen that ranks selectivity correctly.

The hypothesis of this paper is that a standardised dual-isoform Vina docking protocol can rank COX-2 inhibitors by selectivity, with the docking selectivity (COX-1 minus COX-2 affinity) tracking the measured IC50 ratio. The paper tests that hypothesis against five known potent COX-2 inhibitors and reports the answer, which is negative.

## 2. Methods

### 2.1 Literature basis

Sources were searched on 4 November 2026: the daily literature digest (2026-11-04), PubMed E-utilities (verified PMIDs below), and ChEMBL (EBI). Key sources: Nissen et al. (PRECISION) for the cardiovascular numbers; Penning et al. for celecoxib's identification; Bello-Vargas et al. for the COX-1/COX-2 cavity comparison and the 3LN1/3KK6 crystal selection; the RCSB PDB entries for the two structures.

### 2.2 Compound selection (LeadForge pipeline)

The LeadForge pipeline was run live on 4 November 2026 (UniProtKB → ChEMBL → PubChem → RDKit → PAINS/ADMET → Vina). Target identification used the gene query "PTGS2" (UniProt P35354, prostaglandin G/H synthase 2, human, 604 aa); the ChEMBL target was CHEMBL230 (single-protein, human). Thirty-nine bioactivities (pChEMBL ≥ 5) were retrieved; celecoxib was verified in PubChem (CID 2662). Twenty-five compounds passed the similarity screen and 26 were ranked by composite score. The top five distinct leads were taken forward; the rank-2 entry, CHEMBL118, is celecoxib itself and is reported as the reference only. All five leads are known COX-2 inhibitors with published ChEMBL IC50 values of 0.02–1.0 nM against COX-2; none has a preferred name, an approval, or a development phase in ChEMBL.

### 2.3 Molecular docking

Docking was performed 4 November 2026 with AutoDock Vina 1.2.7, using the LeadForge protocol: the same grid centre, box (22.5 Å cube), exhaustiveness (8) and pose count (3) for every ligand on each structure; best of three poses reported. COX-2: PDB 3LN1 (2.4 Å, "Structure of celecoxib bound at the COX-2 active site"), grid centred on the centroid of co-crystallised celecoxib, chain C: [65.25, −45.38, 45.42]. COX-1: PDB 3KK6 (2.75 Å, "Crystal Structure of Cyclooxygenase-1 in complex with celecoxib"), grid centred on co-crystallised celecoxib, chain A: [−32.41, 43.36, −5.62]. Receptor preparation used RDKit (Gasteiger charges, simplified AutoDock atom types); ligand preparation used meeko. Vina's scoring noise is approximately ±1–2 kcal/mol; differences smaller than this cannot be treated as significant on scores alone.

Two pipeline failures were caught and corrected before reporting. First, the pipeline's automatic PDB lookup crashed on a UniProt HTTP 500 for PTGS2, so no structure was auto-selected at all. Second, the pipeline's automatic ligand-centre routine would have centred the COX-2 grid on the BOG detergent molecule in 3LN1, not on celecoxib — 3LN1 contains BOG, HEM, NAG and two celecoxib copies, and the first drug-like HETATM residue in file order is the detergent. Both centres used here were computed per-residue from the celecoxib records. Third, the 3KK6 receptor file contains a crystallographic close contact (VAL349 chain B carbonyl O within bonding distance of SER353 OG) that RDKit's distance-based bonding turns into a spurious bond, failing sanitisation ("Explicit valence for atom O, 3"). The single spurious bond was removed before sanitisation; coordinates were not changed, and sanitisation plus Gasteiger charges then succeeded. The raw JSON of every run is preserved (see Data availability).

### 2.4 PAINS screen and toxicity read-across

Every test compound was screened with the RDKit PAINS filter: all five leads and celecoxib were PAINS-clean. A ToxGuard Tox21 kNN read-across panel (12 assays) was run for each lead; the highest read-across probabilities were 0.08–0.34 across the five leads. Celecoxib itself carries a measured NR-ER flag (1.0) in the same panel, so a flag in this panel does not distinguish a lead from the approved reference drug.

### 2.5 Honesty limits

What this paper cannot show: docking is not activity; Vina noise is ±1–2 kcal/mol; no experimental data are presented; no molecular-dynamics refinement or binding-free-energy calculation was performed; one crystal structure per isoform was used; the five "leads" are already-known COX-2 inhibitors, so no novelty of chemistry is claimed; the COX-1/COX-2 selectivity ratio from docking is a difference of two noisy scores, so its own error is larger than either score's.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | COX-2 (3LN1) | COX-1 (3KK6) | Docking Δ (kcal/mol) | ChEMBL COX-2 IC50 (nM) | ChEMBL COX-1 IC50 (nM) | Measured ratio |
|---|---|---|---|---|---|---|
| Celecoxib (reference) | −12.28 | −10.33 | 1.95 | % inhibition only | % inhibition only | — |
| CHEMBL282093 | −12.13 | −9.96 | 2.17 | 0.45 | 17,800 | ~39,600× |
| CHEMBL432945 | −11.76 | −9.76 | 2.00 | 1.0 | 5.0 | 5× |
| CHEMBL502555 | −11.74 | −9.99 | 1.75 | 0.07 | — | — |
| CHEMBL186632 | −10.15 | −9.68 | 0.47 | 0.44 | 3,828 | ~8,700× |
| CHEMBL525247 | −9.05 | −7.41 | 1.64 | 0.02 | — | — |

All affinities in kcal/mol, best of three poses, Vina 1.2.7, 4 November 2026. Poses: celecoxib COX-2 −12.28/−10.64/−7.46; CHEMBL282093 COX-2 −12.13/−10.69/−10.02 (the most pose-consistent lead); CHEMBL525247 COX-2 −9.05/−6.35/−1.83 (the least consistent — its third pose is positive, i.e. non-binding). Celecoxib's drug-likeness: MW 381.38, logP 3.51, Lipinski pass. The five leads: MW 355.46–401.80, logP 3.11–4.46, all Lipinski pass, all PAINS-clean.

### 3.2 The headline is a negative result

No lead beats celecoxib on COX-2 affinity: the closest, CHEMBL282093, trails by 0.15 kcal/mol — inside noise. And docking selectivity does not track measured selectivity. The two compounds with measured COX-1 data that bracket the selectivity range behave oppositely to the docking prediction: CHEMBL432945 is measured only 5-fold selective yet has the second-best docking selectivity (2.00 kcal/mol), while CHEMBL186632 is measured ~8,700-fold selective yet has the worst docking selectivity (0.47 kcal/mol). The most selective compound by measurement, CHEMBL282093 (~39,600-fold), does have the best docking selectivity (2.17 kcal/mol) — but by 0.22 kcal/mol over celecoxib, inside noise, and the middle of the ranking is scrambled. A screen that cannot separate 5-fold from 8,700-fold selective cannot be used to rank selectivity.

### 3.3 Comparison with published docking

Published docking on the same structures exists: Bello-Vargas et al. (2023) validated a docking protocol on eight COX crystals including 3LN1 and 3KK6, achieving RMSD < 1 Å on binding-mode reproduction and R² > 0.70 against IC50 values across their compound set. Our celecoxib re-dock is consistent with that validation in the weak sense — celecoxib scores best on COX-2 and prefers COX-2 over COX-1 by 1.95 kcal/mol — but our six-compound set shows the correlation breaks down within a congeneric series of potent inhibitors, which the published validation did not test. The cavity volumes in that study (COX-2 269.31 Å³ vs COX-1 198.14 Å³ for the celecoxib crystals) explain why COX-2 accommodates the sulfonamide side pocket; they do not explain why Vina mis-ranks selectivity among analogues.

## 4. Discussion

### 4.1 The reframe

The paper's value is the negative result, stated plainly: within a set of already-potent COX-2 inhibitors, Vina docking on 3LN1/3KK6 reproduces the direction of celecoxib's selectivity but not the magnitude or the ranking. The most useful compound in the set may be CHEMBL282093 — not because its docking beats celecoxib (it does not), but because it is measured ~39,600-fold selective with a COX-2 IC50 of 0.45 nM, and its docking is the most pose-consistent of the leads. That is a literature finding, not a docking discovery, and it is reported as such.

### 4.2 Why the "wins" must not be over-read

CHEMBL282093's docking selectivity exceeds celecoxib's by 0.22 kcal/mol — a tenth of Vina's noise. CHEMBL432945's 2.00 kcal/mol looks respectable until the measured 5-fold selectivity is placed beside it. And CHEMBL525247, the most potent compound by measurement (COX-2 IC50 0.02 nM), is the worst by docking (−9.05 kcal/mol) with an incoherent pose series — either its binding mode differs from celecoxib's (possible: it is the least similar to celecoxib in the set, Tanimoto 0.333) or Vina mishandles its chemotype. Either way, docking alone would have discarded the most potent compound in the set.

### 4.3 The selectivity ratio is a difference of two noisy numbers

A docking selectivity is COX-1 affinity minus COX-2 affinity; if each score carries ±1–2 kcal/mol of noise, the difference carries roughly ±1.4–2.8 kcal/mol. The entire observed range of docking selectivities in this set (0.47–2.17 kcal/mol) fits inside that error bar. This is the structural reason the ranking fails, and it generalises: any selectivity claim from single-structure Vina docking needs an effect larger than ~3 kcal/mol to be believed, and none of the leads here approaches that.

### 4.4 Testable hypotheses

1. In a paired COX-1/COX-2 enzyme assay under identical conditions, CHEMBL432945 is less than 50-fold selective, while CHEMBL282093 is more than 1,000-fold selective — the measured ChEMBL values, not the docking order, predict the ranking.
2. CHEMBL525247 inhibits COX-2 with an IC50 under 1 nM in a fresh assay despite its poor docking score, confirming that its binding mode is not captured by the celecoxib-centred grid.
3. Re-docking celecoxib into 3LN1 reproduces the crystallographic pose within 2 Å RMSD (protocol self-validation; not yet run).

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): paired COX-1/COX-2 colorimetric or fluorometric enzyme inhibition assays for CHEMBL282093, CHEMBL432945, CHEMBL186632 and celecoxib, same plates, n = 3, with pre-registered selectivity-ratio decision rules. Stage 2 (weeks 3–6): COX-2 IC50 confirmation for CHEMBL525247, plus a wider grid or induced-fit re-dock if the assay confirms potency that docking missed. Stage 3 (weeks 7–12): whole-blood assay (COX-1: serum thromboxane B2; COX-2: lipopolysaccharide-induced prostaglandin E2) for the best compound from Stage 1 — the assay that actually predicts the clinical selectivity window. No compound here is a drug candidate; all are research chemicals.

## 5. Limitations

1. Docking only; no experimental data. 2. All margins discussed are inside Vina's ±1–2 kcal/mol noise, and selectivity differences carry roughly double that error. 3. No molecular-dynamics refinement, binding-free-energy calculation, or re-docking validation of celecoxib was performed. 4. One crystal structure per isoform; COX enzymes are homodimers and the second monomer's allosteric influence is not modelled (3KK6's coxib-bound monomer is the basis of the Rimon et al. finding that coxibs bind tightly to one monomer). 5. Two leads (CHEMBL502555, CHEMBL525247) have no published COX-1 IC50, so their measured selectivity is unknown. 6. All five leads are already-known COX-2 inhibitors; no new chemical matter is proposed. 7. The 3KK6 receptor required a one-bond correction to a crystallographic close contact; the correction is documented and coordinates were unchanged, but it is a deviation from the unmodified protocol. 8. No Pakistani-market or clinical data are presented.

## 6. Conclusion

Celecoxib remains the best-docked compound on COX-2 (−12.28 kcal/mol), and no lead beats it. More importantly, docking selectivity on 3LN1/3KK6 does not track measured selectivity: a 5-fold selective compound out-scores an 8,700-fold selective one. Single-structure Vina docking can confirm that a compound binds the COX-2 pocket; it cannot rank selectivity among potent analogues. The next experiment is a paired enzyme assay, not more docking.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author thanks the ChEMBL, UniProtKB, RCSB PDB and PubChem teams for free, open data.

## References

1. Nissen SE, Yeomans ND, Solomon DH, et al. Cardiovascular safety of celecoxib, naproxen, or ibuprofen for arthritis. *N Engl J Med.* 2016;375:2519–2529. doi:10.1056/NEJMoa1611593.
2. Penning TD, Talley JJ, Bertenshaw SR, et al. Synthesis and biological evaluation of the 1,5-diarylpyrazole class of cyclooxygenase-2 inhibitors: identification of 4-[5-(4-methylphenyl)-3-(trifluoromethyl)-1H-pyrazol-1-yl]benzenesulfonamide (SC-58635, celecoxib). *J Med Chem.* 1997;40(9):1347–1365. PMID: 9135032.
3. Bello-Vargas E, Leyva-Peralta MA, Gómez-Sandoval Z, Ordóñez M, Razo-Hernández RS. A computational method for the binding mode prediction of COX-1 and COX-2 inhibitors: analyzing the union of coxibs, oxicams, propionic and acetic acids. *Pharmaceuticals.* 2023;16(12):1688. PMID: 38139814.
4. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model.* 2021;61(8):3891–3898. PMID: 34278794.
5. RCSB Protein Data Bank. Structure of celecoxib bound at the COX-2 active site. PDB ID 3LN1, 2.4 Å. https://www.rcsb.org/structure/3LN1 (accessed 4 November 2026).
6. RCSB Protein Data Bank. Crystal structure of cyclooxygenase-1 in complex with celecoxib. PDB ID 3KK6, 2.75 Å. https://www.rcsb.org/structure/3KK6 (accessed 4 November 2026).
7. Understanding the selectivity of nonsteroidal anti-inflammatory drugs for cyclooxygenases using quantum crystallography and electrostatic interaction energy. PMCID: PMC11878451.
8. ChEMBL database, European Bioinformatics Institute. Target: prostaglandin G/H synthase 2 (CHEMBL230); prostaglandin G/H synthase 1 (CHEMBL221); bioactivities accessed 4 November 2026. https://www.ebi.ac.uk/chembl/.

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-047-2026-11-04.json` (pipeline run: UniProt P35354, ChEMBL CHEMBL230, 26 ranked leads) and `hidden_files/dock-HP-047c-2026-11-04.json` (authoritative dual-isoform dock: COX-2 PDB 3LN1, celecoxib centroid [65.25, −45.38, 45.42]; COX-1 PDB 3KK6, celecoxib centroid [−32.41, 43.36, −5.62]; Vina 1.2.7). ChEMBL IDs: celecoxib (CHEMBL118, query), CHEMBL282093, CHEMBL502555, CHEMBL525247, CHEMBL186632, CHEMBL432945. PDB IDs 3LN1, 3KK6. No additional data were generated.
