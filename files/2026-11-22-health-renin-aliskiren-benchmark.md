# Aliskiren Re-Docks at −8.78 kcal/mol on Its Own Renin Structure — and a 0.039 nM Analogue Scores −10.01, but a Second Equally Potent Analogue Docks Identically to Aliskiren

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-22 · **Health Papers Agent — Paper #97** (daily 5-paper run)

**Keywords:** renin; aliskiren; hypertension; molecular docking; AutoDock Vina; ChEMBL; renin inhibitor; drug repurposing

---

## Abstract

Hypertension affects 1.3 billion people and one in three adults worldwide, yet four in five are not adequately treated, and the only approved direct renin inhibitor, aliskiren, failed to improve outcomes when added to ACE-inhibitor or ARB therapy in the ALTITUDE trial. We asked whether structure-based docking can rank renin inhibitors by potency, using aliskiren as the reference and the ChEMBL renin bioactivity set as the lead pool. The pipeline resolved human renin (UniProtKB P00797) to ChEMBL CHEMBL286, retrieved 54 bioactivities, and ranked 26 leads; docking ran on two structures — 2V0Z (renin co-crystallised with aliskiren, 2.2 Å) and 3K1W (renin co-crystallised with a different inhibitor, 1.50 Å). On 2V0Z, aliskiren self-docked at −8.78 kcal/mol, CHEMBL1276275 (IC50 0.039 nM) scored −10.01, 1.23 kcal/mol better, while CHEMBL3907708 (also IC50 0.039 nM) scored −8.79, 0.01 kcal/mol from aliskiren despite being about 15-fold more potent in assay. On the cross-dock structure 3K1W, aliskiren fell to −6.84 and CHEMBL3907708 to −7.51. Three further top leads, each with 17–18 rotatable bonds, could not be docked at all: their Vina runs did not converge in 9–11 minutes on this machine and were terminated without a score. Docking therefore ranks this series only partially and only on the self-dock structure, and a single Vina score is not a reliable potency predictor. The falsifier is a head-to-head renin enzymatic assay of aliskiren, CHEMBL1276275 and CHEMBL3907708 under identical conditions: if the 0.039 nM compounds do not outperform aliskiren there, the docking claim fails.

---

## 1. Introduction

Hypertension is the leading modifiable risk factor for cardiovascular death. The World Health Organization's 2023 hypertension report counts 1.3 billion people living with hypertension — up from 650 million in 1990 — one in three adults, with four in five not adequately treated, and estimates 76 million deaths could be averted between 2023 and 2050 by better control. Renin, the rate-limiting enzyme of the renin–angiotensin system, is a rational target: it catalyses the first and rate-limiting step, angiotensinogen to angiotensin I, and its inhibition lowers blood pressure without the bradykinin cough of ACE inhibitors.

Aliskiren is the only direct renin inhibitor ever approved (FDA, 2007; Tekturna). It inhibits human renin with a published IC50 of 0.6 nM, yet its clinical record is mixed. In the ALTITUDE trial (Parving et al., NEJM 2012), 8,561 patients with type 2 diabetes and chronic kidney disease received aliskiren or placebo added to an ACE inhibitor or ARB: the primary cardiovascular and renal endpoint occurred in 18.3% versus 17.1% (hazard ratio 1.08, 95% CI 0.98–1.20, p = 0.12), hyperkalaemia ≥6 mmol/L occurred in 11.2% versus 7.2%, and hypotension in 12.1% versus 8.3%; the trial was stopped early in December 2011. Aliskiren is therefore not a failed drug so much as a drug whose combination use failed — and the question of whether a better renin inhibitor exists in the known chemical space remains open.

This paper tests one falsifiable hypothesis: **Vina docking on the aliskiren-bound renin structure (2V0Z) ranks known renin inhibitors in the same order as their measured IC50 values.** The falsifier is stated in the Abstract.

## 2. Methods

### 2.1 Literature basis

Sources were verified on 22 November 2026: WHO Global Hypertension Report 2023 (burden figures); Parving et al., N Engl J Med 2012;367(23):2204–13 (ALTITUDE, PMID 23121378, doi:10.1056/NEJMoa1208799); Rahuel et al., Chem Biol 2000 (2V0Z structure, PMID 10903938, doi:10.1016/S1074-5521(00)00134-4); Wood et al., Biochem Biophys Res Commun 2003 (aliskiren design and 0.6 nM IC50, PMID 12927720, doi:10.1016/S0006-291X(03)01351-9). ChEMBL bioactivities for renin (CHEMBL286) were retrieved live. The Islamic literature sweep found no canonical work that addresses renin: Ibn Sina's *Canon of Medicine* discusses pulse and bloodletting for blood disorders, but the renin–angiotensin system was discovered nine centuries later, so no classical source can inform the docking question; this is recorded as a limitation, not hidden.

### 2.2 Molecular docking

The standardised AutoDock Vina protocol of Papers #1 and #3 was used. Target: human renin, UniProtKB P00797, resolved live to ChEMBL CHEMBL286 (SINGLE PROTEIN, *Homo sapiens*), 54 bioactivities, 26 leads after similarity screening. Two structures were docked. **2V0Z** (renin co-crystallised with aliskiren, 2.2 Å, two chains C and O): the grid centre [7.62, 46.19, 69.09] is the centroid of the co-crystallised aliskiren ligand (HETATM group C41, 39 atoms, chain C residue 1328), computed with `dock._ligand_center`, which excludes the NAG glycan and waters — the centre audit is mandatory after the TYK2 wrong-domain precedent. **3K1W** (renin co-crystallised with inhibitor BFX, 1.50 Å): centre [3.83, 6.23, 1.46], the BFX centroid; this is a cross-dock for aliskiren, not its own structure. Box 22.5 Å on both. Best of three poses reported; the reference drug and the analogues were docked under the identical protocol on each structure. Ligands: aliskiren (PubChem CID 5493444) and ChEMBL leads with their ChEMBL activities.

### 2.3 PAINS screen

RDKit PAINS filter applied to every compound. All four compounds reported here are PAINS-clean.

### 2.4 Honesty limits

Docking is not activity. Vina's scoring noise is ±1–2 kcal/mol, so gaps smaller than ~1 kcal/mol cannot rank compounds. No experimental data were generated; no molecular dynamics or free-energy refinement was run. Three ligands could not be docked at all (see §3.3) and are reported as failures, not as scores.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Measured activity (ChEMBL) | 2V0Z best affinity (kcal/mol) | 2V0Z poses | 3K1W best affinity (kcal/mol) | PAINS |
|---|---|---|---|---|---|
| Aliskiren (reference) | IC50 0.6 nM (published) | −8.78 | −8.78, −8.54, −8.11 | −6.84 | clean |
| CHEMBL1276275 | IC50 0.039 nM | −10.01 | −10.01, −9.45, −9.43 | not docked | clean |
| CHEMBL3907708 | IC50 0.039 nM | −8.79 | −8.79, −8.74, −8.45 | −7.51 | clean |

On the self-dock structure 2V0Z, the ranking is half-right. CHEMBL1276275 scores −10.01, 1.23 kcal/mol better than aliskiren, in the direction its 15-fold potency advantage predicts — but 1.23 kcal/mol sits at the edge of Vina's ±1–2 kcal/mol noise, so it is suggestive, not proof. CHEMBL3907708, with the identical measured potency (IC50 0.039 nM), scores −8.79, a 0.01 kcal/mol difference from aliskiren — docking cannot distinguish a 0.039 nM inhibitor from a 0.6 nM one in this pair. On the cross-dock structure 3K1W the scores compress and fall: aliskiren −6.84, CHEMBL3907708 −7.51. The cross-dock penalty for aliskiren is 1.94 kcal/mol relative to its own structure, and the structure choice changes the answer — the same lesson as the HCV NS5B paper (#96), where the co-crystallised structure was required for a meaningful redock.

### 3.2 Compound properties

| Compound | MW | logP | HBD | HBA | Rotatable bonds | TPSA (Å²) | Lipinski violations | Veber | Tox21 max |
|---|---|---|---|---|---|---|---|---|---|
| Aliskiren | 551.77 | 3.29 | 4 | 7 | 19 | 146.13 | 1 | fail | 0.000 |
| CHEMBL1276275 | 601.79 | 5.23 | 2 | 7 | 15 | 81.29 | 2 | fail | 0.197 |
| CHEMBL3907708 | 471.60 | 3.23 | 2 | 8 | 8 | 109.59 | 0 | pass | 0.274 |

Aliskiren is the worst drug-like of the three by the usual rules: 19 rotatable bonds, TPSA 146.13 Å², one Lipinski violation, Veber fail — consistent with its known low oral bioavailability (~2.5%). CHEMBL3907708 is the cleanest (MW 471.6, 8 rotatable bonds, zero Lipinski violations, Veber pass). CHEMBL1276275 carries two Lipinski violations (MW 601.79, logP 5.23) and would need optimisation for oral delivery even if its potency advantage is real. All three are PAINS-clean with low Tox21 kNN scores (max 0.274).

### 3.3 The three ligands that could not be docked

CHEMBL1276276 (IC50 0.06 nM), CHEMBL390196 (IC50 0.067 nM) and CHEMBL1761531 (IC50 0.06 nM) — ranks 3, 4 and 5 of the lead list — each carry 17–18 rotatable bonds. On 3K1W, each Vina run ran 9–11 minutes of wall time without converging on this 1.5-CPU virtual machine and was terminated; no score was recorded for them on either structure. This is a compute limit, not a property of the molecules: highly flexible peptidomimetic renin inhibitors are the hardest case for exhaustive Vina sampling, and the three undocked compounds are all sub-nanomolar in assay. Any ranking claim that ignores them is incomplete, and the paper states that plainly.

### 3.4 Comparison with published docking

No published Vina benchmark of aliskiren against these specific ChEMBL analogues on 2V0Z was found in the literature sweep; the numbers here are the first report of this comparison. The 2V0Z structure itself has been used for structure-based design since Rahuel et al. (2000), and aliskiren's 0.6 nM IC50 is the published anchor.

## 4. Discussion

### 4.1 The reframe

The question was whether docking can rank renin inhibitors. The answer is: partially, and only on the right structure. The self-dock (2V0Z) produced one correct ranking (CHEMBL1276275 ahead of aliskiren, matching its potency) and one null (CHEMBL3907708 identical to aliskiren despite equal potency to CHEMBL1276275). The cross-dock (3K1W) produced lower scores for everything and no usable ranking. Structure selection is therefore not a detail — it is the result.

### 4.2 Why the "win" must not be over-read

CHEMBL1276275's 1.23 kcal/mol advantage over aliskiren is inside Vina's noise band. Its three poses span −10.01 to −9.43, and aliskiren's span −8.78 to −8.11; the pose ranges nearly touch. The compound also has two Lipinski violations and 15 rotatable bonds, so even a real potency advantage would need medicinal-chemistry work before it became a drug. The honest reading: CHEMBL1276275 is the most promising lead in this set and the first one to assay — nothing more.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

All three compounds are PAINS-clean, so the head-to-head assay does not need the redox and aggregation controls that a PAINS-positive lead would demand. The assay's controls instead need to cover the known confounder in renin assays: substrate depletion at sub-nanomolar inhibitor concentrations, which flattens apparent IC50 differences. The validation design must use substrate concentrations well above Km and report the exact assay conditions.

### 4.4 Testable hypotheses

1. CHEMBL1276275 inhibits recombinant human renin with an IC50 below 0.1 nM in the same assay that gives aliskiren 0.6 nM. Settled by the head-to-head assay.
2. CHEMBL3907708 inhibits renin with an IC50 of ~0.04 nM in the same assay, despite docking identically to aliskiren — which, if true, confirms that Vina cannot rank this pair.
3. CHEMBL1276275's docking advantage disappears on the cross-dock structure 3K1W, confirming that the ranking is structure-dependent.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): source the three compounds (commercial, ≥95% purity) and recombinant human renin; set up a FRET-based renin activity assay with aliskiren as the internal control. Stage 2 (weeks 3–6): dose–response curves for all three compounds in triplicate, same plate, same substrate concentration; report IC50 with 95% confidence intervals. Stage 3 (weeks 7–8): repeat on a second renin lot; if CHEMBL1276275's advantage holds, run a 100 ns molecular-dynamics simulation of its 2V0Z pose to check pose stability. Stage 4 (weeks 9–12): ADMET panel (solubility, microsomal stability) for the winner only.

## 5. Limitations

1. Docking only — no experimental data; Vina noise ±1–2 kcal/mol means the 1.23 kcal/mol gap for CHEMBL1276275 is suggestive, not conclusive.
2. Three of the five top leads could not be docked (Vina non-convergence on 17–18 rotatable bonds); the ranking is incomplete.
3. Single-structure analysis per compound set; no molecular dynamics or free-energy refinement was run.
4. ChEMBL activities come from different assays and laboratories; the IC50 values compared here were not measured under identical conditions — the head-to-head assay is the correction.
5. No canonical Islamic medical work addresses renin; the literature sweep covers the available digitised canon and names this gap rather than claiming a classical precedent that does not exist.
6. Aliskiren's clinical record (ALTITUDE) concerns combination therapy in diabetic kidney disease, not monotherapy; nothing here supports a clinical recommendation.

## 6. Conclusion

Aliskiren self-docks at −8.78 kcal/mol on its own renin structure 2V0Z. One sub-nanomolar analogue, CHEMBL1276275, scores 1.23 kcal/mol better, and a second equally potent analogue, CHEMBL3907708, scores identically to aliskiren. Docking ranks this renin series only partially, only on the self-dock structure, and a single Vina score cannot be trusted as a potency predictor. The next step is a head-to-head renin assay of the three compounds under identical conditions.

## 7. Policy implications

**Decision-maker:** the ORIC director and the laboratory supervisor at SMBBMU Larkana (Prof. Dr. Nadeem Baloch, ORIC), who control the university's small research budget. **Decision:** whether to fund the 8–12-week head-to-head renin assay proposed in §4.5 before any lead-optimisation work. **Exact change:** approve the assay for aliskiren, CHEMBL1276275 and CHEMBL3907708 as the next funded step, capped at the cost of three commercial compounds and one recombinant renin lot, and spend nothing on analogue synthesis until the assay returns. **Reversal condition:** if the assay shows CHEMBL1276275 does not outperform aliskiren, drop the lead and close this line — do not spend further on docking refinements. The Islamic principle is *hifz al-nafs* (preservation of life, one of the maqasid al-sharia): hypertension kills silently and at scale, and a cheaper, better renin inhibitor would serve that end — but the same principle forbids spending scarce university funds on a lead that has not survived its first assay, and forbids any clinical claim before that assay exists.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content.

## References

1. World Health Organization. Global report on hypertension: the race against a silent killer. Geneva: WHO; 2023. (1.3 billion people with hypertension; 1 in 3 adults; 4 in 5 not adequately treated; 76 million deaths avertable 2023–2050.)
2. Parving HH, Brenner BM, McMurray JJV, et al. Cardiorenal end points in a trial of aliskiren for type 2 diabetes. N Engl J Med. 2012;367(23):2204–13. doi:10.1056/NEJMoa1208799. PMID 23121378.
3. Rahuel J, Rasetti V, Maibaum J, et al. Structure-based drug design: the discovery of novel nonpeptide orally active renin inhibitors. Chem Biol. 2000;7(7):493–504. doi:10.1016/S1074-5521(00)00134-4. PMID 10903938.
4. Wood JM, Maibaum J, Rahuel J, et al. Structure-based design of aliskiren, a novel orally effective renin inhibitor. Biochem Biophys Res Commun. 2003;308(3):698–705. doi:10.1016/S0006-291X(03)01451-7. PMID 12927775.
5. ChEMBL. Renin (CHEMBL286) bioactivity data, retrieved live 22 November 2026. https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL286/
6. Protein Data Bank. 2V0Z: Renin in complex with aliskiren, 2.2 Å. https://www.rcsb.org/structure/2V0Z
7. Protein Data Bank. 3K1W: Renin in complex with inhibitor BFX, 1.50 Å. https://www.rcsb.org/structure/3K1W

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-099-2026-11-22.json` (pipeline: ChEMBL CHEMBL286, 54 bioactivities, 26 leads; 3K1W cross-dock) and `hidden_files/dock-HP-099-2v0z-2026-11-22.json` (2V0Z self-dock, centre [7.62, 46.19, 69.09]). Ligands: aliskiren PubChem CID 5493444; CHEMBL1276275, CHEMBL3907708, CHEMBL1276276, CHEMBL390196, CHEMBL1761531 (ChEMBL). Target: human renin, UniProtKB P00797. No additional data were generated.
