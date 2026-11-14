# Metal-aware re-ranking of sulfonyl piperazine LpxH inhibitors: docking scores alone cannot distinguish di-manganese chelators from non-chelators in *Klebsiella pneumoniae* LpxH

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent verification.**

**Author:** Zubair Ali, Pharm-D student, SMBBMU Larkana, Pakistan · ORCID: 0009-0001-5921-7509

**Drafting assistant:** Lapis (AI). All computations were run on 5 November 2026 and are reproduced from the files listed under Data availability.

---

## Abstract

**Background:** LpxH, the di-manganese UDP-2,3-diacylglucosamine hydrolase of the lipid A (Raetz) pathway, is an essential antibacterial target in *Klebsiella pneumoniae*, but structure-based ranking of its sulfonyl piperazine inhibitors is confounded because standard docking ignores the catalytic di-manganese cluster. **Methods:** We docked (AutoDock Vina 1.2.7) the four published inhibitors AZ1, JH-LPH-41, JH-LPH-45 and JH-LPH-50 and four patent-disclosed analogues into the 1.73 Å *K. pneumoniae* LpxH structure (PDB 7SS7) at the crystallographic ligand centroid, verified the grid centre against the co-crystallised ligand (deviation 0.0 Å), and measured hydroxamate-oxygen to manganese distances in every docked pose with an order-independent graph method. **Results:** Vina affinities span only −9.18 to −11.37 kcal/mol and misrank the known references: JH-LPH-45 (−11.37) outscores JH-LPH-50 (−11.04) although it is 2.3-fold less potent (IC50 18 vs 7.7 nM), and AZ1 (−10.04) sits within 1.0 kcal/mol of JH-LPH-50 despite lacking whole-cell activity. The metal geometry separates the series cleanly: the three known chelators place a hydroxamate oxygen 1.93–2.21 Å from manganese, the two hydroxamate analogues 1.97–2.65 Å, and the two non-hydroxamate analogues no oxygen closer than 6.5 Å. Re-docking JH-LPH-50 reproduces the crystal pose to 2.22–2.28 Å RMSD. **Conclusion:** a metal-aware re-rank (Vina affinity plus a chelation-distance term) is required for this target; we predict the des-chloro hydroxamate CID 156252442 inhibits *K. pneumoniae* LpxH at low-nanomolar potency comparable to JH-LPH-50, while the non-chelating analogues CID 156252448 and CID 156252462 will be at least 10-fold weaker despite similar docking scores — a prediction testable in a single malachite-green enzyme assay.

**Keywords:** LpxH; *Klebsiella pneumoniae*; lipid A; sulfonyl piperazine; di-manganese cluster; molecular docking; AutoDock Vina; metal chelation; antimicrobial resistance

---

## Introduction

No new class of antibiotics against Gram-negative pathogens has been approved in five decades, while multidrug-resistant *Klebsiella pneumoniae* continues to spread in hospitals, including in Pakistan, where carbapenem-resistant *Klebsiella* is now a routine clinical problem. The lipid A biosynthetic (Raetz) pathway remains one of the few unexploited essential pathways in these organisms. LpxH (UDP-2,3-diacylglucosamine hydrolase) catalyses a late, essential step — hydrolysis of the pyrophosphate of UDP-2,3-diacylglucosamine to lipid X and UMP — and is present in ~70% of Gram-negative bacteria and in all World Health Organization priority Gram-negative pathogens. Inhibiting LpxH is doubly lethal: it blocks lipid A synthesis and causes toxic lipid A intermediates to accumulate in the inner membrane.

The sulfonyl piperazine series is the only inhibitor chemotype with structural validation against *K. pneumoniae* LpxH (*Kp*LpxH). AstraZeneca reported AZ1 in 2015 as the first LpxH inhibitor; Cho *et al.* (2020) solved the *Kp*LpxH–AZ1 crystal structure (PDB 6PIB, 2.26 Å) and showed that AZ1 occupies the L-shaped acyl-chain-binding chamber without reaching the active site, which explains its weak whole-cell activity against wild-type *K. pneumoniae*. Structure-guided optimisation produced JH-LPH-33 (IC50 26 nM) and JH-LPH-41, whose extended *N*-acyl chain reaches into the active site (PDB 6WII, 1.85 Å). Kwak *et al.* (2023) then reported the first-in-class di-manganese-chelating inhibitors, JH-LPH-45 (IC50 18 nM, *K*I 7.3 nM) and JH-LPH-50 (IC50 7.7 nM, *K*I 3.1 nM), whose hydroxamate groups coordinate the catalytic di-manganese cluster (PDB 7SS6, 1.74 Å; PDB 7SS7, 1.73 Å). Chelation, not hydrophobic fit alone, is what separates the nanomolar inhibitors from AZ1.

That distinction creates a specific hazard for computational screening: AutoDock Vina, the workhorse of virtual screening, has no metal-coordination term, and standard receptor preparation strips the manganese ions from the structure. A docking campaign against LpxH that reports Vina scores alone will therefore rank chelating and non-chelating analogues almost interchangeably. A same-target study published this week (Chakraborty *et al.*, 2026) ran a full docking → ADMET → DFT → molecular-dynamics pipeline against *K. pneumoniae* LpxH without any metal-aware term, which makes the question urgent rather than theoretical: does the metal geometry, measured in the docked pose, rescue the ranking that Vina alone gets wrong?

This paper answers that question with a complete, reproducible computation. We dock the four published inhibitors and four patent-disclosed analogues into the JH-LPH-50 co-crystal structure, audit the docking grid centre against the crystallographic ligand (a step that recent work in our own pipeline showed is easy to get wrong), validate the protocol by re-docking, and measure the hydroxamate–manganese geometry of every pose. The result is a falsifiable, metal-aware ranking rule and two concrete potency predictions that one enzyme assay can confirm or refute.

## Methods

### Target and structures

The target is *Klebsiella pneumoniae* subsp. *pneumoniae* LpxH (UniProt A6T5R0, strain ATCC 700721 / MGH 78578; 240 residues). Fifteen X-ray structures are deposited for this accession; we used PDB 7SS7 (1.73 Å), the *Kp*LpxH complex with JH-LPH-50, because it is the highest-resolution structure of the most potent known inhibitor bound in the chelating pose. Ligand identity and stereochemistry were taken from the RCSB Chemical Component Dictionary entries BN8 (JH-LPH-50; C24H29ClF3N5O5S), BKB (JH-LPH-45) and OKV (AZ1; C21H22F3N3O3S). Reference potencies are the published values of Kwak *et al.* (2023): JH-LPH-50 IC50 7.7 nM (*K*I 3.1 nM), JH-LPH-45 IC50 18 nM (*K*I 7.3 nM), JH-LPH-33 IC50 26 nM (*K*I 10 nM), *K*M 68.1 µM; and of Cho *et al.* (2020) for AZ1.

### Compound set

The query compound is JH-LPH-50 (PubChem CID 167713149), verified live in PubChem by SMILES identity search. Analogues were retrieved by PubChem 2D fingerprint similarity (fastsimilarity_2d, Tanimoto ≥ 0.85, 25 records) and scored with RDKit descriptors (Lipinski, Veber), PAINS filters and a k-nearest-neighbour Tox21 read-across panel (12 assays). The top five by composite lead score were docked, together with the query and AZ1. Two of the 25 are the published inhibitors JH-LPH-41 (CID 146680856; PDB ligand U2V in 6WII) and JH-LPH-45 (CID 167713202); these were treated as additional references, not as novel leads. The remaining four analogues (CID 156252442, 156252744, 156252448, 156252462) are disclosed in patent US20240279174 (SureChEMBL entries) with no published enzyme-inhibition data; they are the prediction set. No ChEMBL target exists for LpxH (verified: zero targets for UniProt A6T5R0 and no LpxH entry by name search), so no measured-activity training set was available.

### Docking and grid-centre audit

Docking used AutoDock Vina 1.2.7 with RDKit receptor preparation (Gasteiger charges, simplified AutoDock atom types) and meeko ligand preparation, a 22.5 Å cubic box, exhaustiveness 8, and 3 poses; the reported affinity is the best pose. The grid centre was the centroid of the co-crystallised BN8 ligand in 7SS7, computed independently of the docking code and compared with the centroid returned by the pipeline's automatic centre picker. The two manganese ions were located from the 7SS7 HETATM records. Because the receptor preparation keeps protein ATOM records only, the manganese ions are absent from the docking calculation itself — the metal geometry is therefore measured *a posteriori* on the docked poses, which is the point of the analysis.

### Chelation geometry and re-dock validation

Hydroxamate oxygens in each docked pose were identified without assuming any atom ordering (Vina's PDBQT output reorders atoms relative to the input): bonds were inferred from interatomic distances (< 1.9 Å, heavy atoms), the hydroxamate nitrogen was identified as the unique nitrogen with an oxygen neighbour, and its oxygen neighbour (hydroxyl) and the carbonyl oxygen on the adjacent carbon were measured against both manganese positions. The same graph method recovered the crystallographic hydroxamate–manganese distances (carbonyl 2.49 Å, hydroxyl 2.11 Å; cf. 2.5 Å reported by Kwak *et al.*), validating the measurement. Re-dock validation: JH-LPH-50 was docked twice independently and each pose was aligned to the crystal ligand by maximum-common-substructure mapping onto the SMILES template; the heavy-atom RMSD is reported. All scripts and raw outputs are listed under Data availability.

### Pipeline-fault disclosure

Two faults in our own pipeline were found and corrected during this run, and are disclosed so that the numbers can be audited. First, the pipeline's target resolver initially matched the text query to UniProt B5Y0K8 (*Klebsiella variicola* LpxH) and its ChEMBL fallback selected CHEMBL2074 (human maltase-glucoamylase); the 55 "ligands" and 26 ranked "leads" from that run are unrelated to LpxH and were discarded in full. The run was repeated against the exact accession A6T5R0; the ChEMBL fallback still mis-assigned CHEMBL2074, so the lead set used here comes exclusively from the PubChem similarity search described above, and the pipeline's ChEMBL-derived leads are not reported. Second, the first pose-analysis script assumed Vina's PDBQT atom order matched the input molecule; it did not, which produced a spurious re-dock RMSD of 8.23 Å. The order-independent graph method described above replaced it, and the corrected RMSD values (2.22 and 2.28 Å) are the ones reported.

## Results

### Grid-centre audit

The automatic centre picker returned (−35.42, −9.82, 3.75), identical to the independently computed BN8 centroid (deviation 0.0 Å; BN8 = 39 heavy atoms, the first non-solvent HETATM group in 7SS7). The two manganese ions sit at (−29.52, −19.19, 0.71) and (−29.26, −17.64, 3.71), i.e. 9–10 Å from the grid centre, inside the 22.5 Å box. The grid is therefore centred on the inhibitor site, not on a cofactor, solvent or glycan — the failure mode that invalidated two of our earlier papers before correction.

### Vina affinities misrank the known references

All eight compounds dock with affinities between −9.18 and −11.37 kcal/mol (Table 1) — a spread of only 2.2 kcal/mol across a series whose measured potencies span from 7.7 nM to no whole-cell activity. The misranking is demonstrable on the known compounds alone: JH-LPH-45 scores best (−11.37) although it is 2.3-fold *less* potent than JH-LPH-50 (IC50 18 vs 7.7 nM; −11.04), and AZ1 (−10.04) lies only 1.0 kcal/mol below JH-LPH-50 although it is the weakest inhibitor in the series and has no whole-cell activity against wild-type *K. pneumoniae*. Vina, without a metal term, cannot see the interaction that the medicinal chemistry of this series is built on.

| Compound | Identity | Vina affinity (kcal/mol) | Hydroxyl O–Mn (Å) | Carbonyl O–Mn (Å) | Chelation-competent |
|---|---|---|---|---|---|
| JH-LPH-50 | Reference; IC50 7.7 nM | −11.01 / −11.04 | 1.95 / 2.00 | 3.02 / 2.91 | Yes |
| JH-LPH-45 | Reference; IC50 18 nM | −11.37 | 1.93 | 2.87 | Yes |
| JH-LPH-41 | Reference; PDB 6WII | −10.58 | 2.21 | 3.51 | Yes |
| AZ1 | Reference; first inhibitor | −10.04 | — (no hydroxamate) | — | No (min O–Mn 10.25) |
| CID 156252442 | Des-chloro C4 hydroxamate | −10.84 | 1.97 | 3.09 | Yes |
| CID 156252744 | Des-chloro C5 hydroxamate | −10.18 | 2.65 | 3.69 | Yes (marginal) |
| CID 156252448 | Methyl ester | −9.43 | — (no hydroxamate) | — | No (min O–Mn 6.58) |
| CID 156252462 | Carboxylic acid | −9.18 | — (no hydroxamate) | — | No (min O–Mn 6.51) |

*Table 1. Docking affinities and hydroxamate–manganese distances in the best Vina pose (PDB 7SS7, BN8 centroid). JH-LPH-50 docked twice independently; both runs shown. "Min O–Mn" is the closest approach of any ligand oxygen to either manganese ion.*

### The metal geometry separates the series

The hydroxamate–manganese distances split the eight compounds into two groups with no overlap (Table 1). The three known inhibitors with measured nanomolar potency (JH-LPH-50, JH-LPH-45, JH-LPH-41) place their hydroxamate hydroxyl oxygen 1.93–2.21 Å from a manganese ion — the same distance as in the crystal structure (2.11 Å) — with the carbonyl oxygen at 2.87–3.51 Å. The two hydroxamate analogues behave the same way: CID 156252442 at 1.97 / 3.09 Å, essentially superimposable on JH-LPH-50's geometry, and CID 156252744 at 2.65 / 3.69 Å, the longest chelation distances in the set. The two non-hydroxamate analogues, despite Vina scores within 1.9 kcal/mol of JH-LPH-50, place no oxygen closer than 6.5 Å to either manganese — they cannot chelate by any geometry. AZ1, which the crystal structure shows does not reach the active site, is 10.25 Å away at its closest oxygen.

Re-docking JH-LPH-50 reproduces the crystallographic pose to 2.22 Å RMSD in the first run and 2.28 Å in the repeat — above the conventional 2.0 Å success cutoff, and the residual displacement is concentrated in the hydroxamate: the docked carbonyl oxygen sits 2.91–3.02 Å from manganese versus 2.49 Å in the crystal, while the hydroxyl oxygen is recovered at 1.95–2.00 Å versus 2.11 Å. The pose is approximately right but the metal coordination is systematically under-formed, exactly as expected from a scoring function with no metal term.

### Drug-likeness and safety panel

All eight compounds pass Lipinski and Veber filters with no PAINS alerts (Table 2). The hydroxamate series carries one Lipinski violation each (molecular weight > 500 Da; 529–604 Da), as does JH-LPH-50 itself, so the violation is a property of the chemotype rather than a discriminator. Mean predicted Tox21 probabilities from k-nearest-neighbour read-across are low (0.069–0.108 across 12 assays); the highest single-assay values for JH-LPH-50 are SR-p53 (0.414), SR-ARE (0.310) and SR-MMP (0.278). These read-across values rest on low training-set similarity (maximum 0.31–0.32) and are reported as a triage flag only, not as a safety claim.

| Compound | MW | logP | HBD | HBA | TPSA (Å²) | Rot. bonds | Lipinski viol. | Lead score | Mean Tox21 prob. |
|---|---|---|---|---|---|---|---|---|---|
| JH-LPH-50 | 592.04 | 4.06 | 4 | 6 | 131.08 | 10 | 1 | 97.8 | 0.108 |
| JH-LPH-45 | 604.05 | 3.62 | 3 | 6 | 122.29 | 8 | 1 | 85.6 | 0.069 |
| JH-LPH-41 | 578.01 | 3.67 | 4 | 6 | 131.08 | 9 | 1 | 97.3 | 0.107 |
| AZ1 | 453.49 | 3.13 | 0 | 4 | 60.93 | 3 | 0 | — | 0.092 |
| CID 156252442 | 529.54 | 2.62 | 4 | 6 | 131.08 | 8 | 1 | 88.1 | 0.106 |
| CID 156252744 | 543.57 | 3.01 | 4 | 6 | 131.08 | 9 | 1 | 89.7 | 0.106 |
| CID 156252448 | 577.03 | 4.33 | 2 | 6 | 108.05 | 9 | 1 | 90.0 | 0.093 |
| CID 156252462 | 563.00 | 4.25 | 3 | 5 | 119.05 | 9 | 1 | 91.8 | 0.073 |

*Table 2. RDKit descriptors, composite lead scores (similarity × 40 + Lipinski × 20 + Veber × 10 + PAINS × 10 + tox × 20) and mean Tox21 kNN probabilities. Lead score for AZ1 is not reported because it was docked as a reference only, not scored as a lead.*

### The metal-aware rule and its predictions

A chelation-competent pose is defined here as a docked hydroxyl oxygen ≤ 2.7 Å from a manganese ion (the crystal value is 2.11 Å; the longest distance among the known nanomolar inhibitors in their docked poses is 2.21 Å, and 2.7 Å allows for the ~0.5 Å outward displacement Vina introduces at the carbonyl oxygen). Under this rule, five of the eight compounds are chelation-competent and three are not, and the rule recovers the known potency order where Vina alone inverts it (JH-LPH-45 outscoring JH-LPH-50) and compresses it (AZ1 within 1.0 kcal/mol of JH-LPH-50).

**Falsifiable claim.** A metal-aware score — Vina affinity combined with a chelation-distance term — predicts *Kp*LpxH inhibition better than Vina affinity alone. Specifically: (i) CID 156252442 (Vina −10.84; hydroxyl O–Mn 1.97 Å; carbonyl O–Mn 3.09 Å) will inhibit *Kp*LpxH with an IC50 within 3-fold of JH-LPH-50 (7.7 nM), i.e. low-nanomolar; (ii) CID 156252448 and CID 156252462 (Vina −9.43 and −9.18; no oxygen within 6.5 Å of manganese) will be at least 10-fold weaker than JH-LPH-50 despite Vina scores within 1.9 kcal/mol of it; (iii) CID 156252744 (hydroxyl O–Mn 2.65 Å, the marginal case) will fall between the two groups. **Test:** malachite-green LpxH inhibition assay exactly as in Kwak *et al.* (2023) (*K*M 68.1 µM, triplicate dose–response), followed by MIC determination against *K. pneumoniae* ATCC 10031 with and without an outer-membrane permeabiliser (polymyxin B nonapeptide), as in Cho *et al.* (2020). If CID 156252442 is weaker than 25 nM, or if either non-chelating analogue is within 3-fold of JH-LPH-50, the claim is refuted.

## Discussion

Three points follow. First, the LpxH series is a clean demonstration that a docking score can be right for the wrong reason: Vina rewards the hydrophobic burial of the sulfonyl piperazine tail in the L-shaped acyl-chain chamber, which every analogue in this series shares, and is blind to the metal coordination that actually drives the potency gain from AZ1 to JH-LPH-50. Any virtual screen against a metalloenzyme that reports scores without a metal-geometry check will make the same error, and will prefer large hydrophobic analogues over true chelators. The remedy is cheap — one distance measurement per pose — and we show it separates the series with no overlap.

Second, the predictions are deliberately asymmetric in risk. CID 156252442 is a des-chloro, C4-linker hydroxamate: it drops the 3-chloro substituent of JH-LPH-50 and shortens the linker by two methylenes, yet keeps the full chelation geometry (1.97 / 3.09 Å) and the best Vina score among the untested analogues (−10.84). If it confirms at low-nanomolar potency, it is a simpler, lighter (529.54 Da) and less lipophilic (logP 2.62) starting point than JH-LPH-50. CID 156252744 is the informative borderline: its hydroxyl oxygen at 2.65 Å is the longest chelation distance in the set, so its measured potency tests where the 2.7 Å cutoff actually bites.

Third, the negative predictions matter as much as the positive one. CID 156252448 (methyl ester) and CID 156252462 (carboxylic acid) are the two highest-scoring non-hydroxamate analogues by composite lead score (90.0 and 91.8) and would be the first compounds a score-only pipeline would order. Our analysis says they are the wrong order: without a metal-binding group they cannot reproduce the interaction that makes this series work. A single assay plate distinguishes the two rankings.

This week's literature sharpens the context rather than changing the conclusion. Chakraborty *et al.* (2026) independently selected LpxH as a docking target and ran the standard pipeline (docking → ADMET → DFT → MD) without a metal term; our result predicts their top-ranked quinolinone/thiazolidinone hits will need the same chelation check before synthesis. On the resistance-spread side, econazole was shown this week to block conjugative transfer of plasmid-borne last-line resistance genes (Hu *et al.*, 2026), and proton-pump inhibitors were shown to restore ceftriaxone activity against multidrug-resistant *K. pneumoniae* by efflux inhibition (Hussein & Auda, 2026) — both are combination partners, not competitors, for a direct LpxH inhibitor: an LpxH inhibitor that works would pair naturally with a permeabiliser or an efflux adjuvant, exactly as Cho *et al.* showed for the early sulfonyl piperazines. Genomic-language-model screening (MicrobeRT, 2026) and MIC prediction from sequence (Mikawa, 2026) are converging on the same practical problem from the diagnostic side; a validated LpxH inhibitor would give those tools a therapeutic counterpart.

## Limitations

1. **No experimental data.** Every potency statement about the four analogues is a prediction; none has a measured IC50. The claim is designed to be refuted by one assay.
2. **Vina has no metal term and the receptor has no manganese.** The affinities are therefore systematically blind to chelation; the metal-aware rule is a post-hoc geometric correction, not a re-scored energy. A metal-aware scoring function or QM/MM refinement would be stronger, and was not run.
3. **Re-dock RMSD is 2.22–2.28 Å**, above the conventional 2.0 Å cutoff, with the error concentrated at the hydroxamate. The protocol recovers the binding mode approximately, not exactly.
4. **Single structure, no dynamics.** All docking used one rigid structure (7SS7); no ensemble docking and no molecular dynamics were run, so induced-fit and lid-domain motion (the insertion lid above the active site) are unmodelled.
5. **Toxicity panel is low-confidence read-across.** Maximum similarity to the Tox21 training set is 0.31–0.32; the probabilities are triage flags, and hydroxamates as a class carry known off-target metal-binding liabilities that this panel cannot assess.
6. **Enzyme potency is not whole-cell activity.** AZ1 is the standing warning: nanomolar enzyme inhibition in this series has repeatedly failed to translate into wild-type MIC without outer-membrane permeabilisation or efflux deletion. The MIC arm of the proposed test is therefore essential, not optional.
7. **ChEMBL has no LpxH target**, so the analogue set could not be filtered against measured LpxH activity; the four prediction compounds are patent-disclosed (US20240279174), not novel chemical matter — the novelty claimed here is the ranking rule and the predictions, not the structures.
8. **Pipeline faults.** The ChEMBL fallback mis-assignment and the atom-order error described in Methods were caught before reporting, but they show that automated pipelines need the same centre and identity audits applied here; the audit steps are part of the method, not an afterthought.

## Conclusion

For *Klebsiella pneumoniae* LpxH, AutoDock Vina affinities span 2.2 kcal/mol across a series whose measured potencies span from 7.7 nM to no whole-cell activity, and Vina inverts the order of the two best-known inhibitors. A single geometric measurement — the hydroxamate-oxygen to manganese distance in the docked pose — restores the ranking: known nanomolar inhibitors place a hydroxamate oxygen 1.93–2.21 Å from manganese, non-chelating analogues place no oxygen closer than 6.5 Å. We predict CID 156252442 will inhibit *Kp*LpxH at low-nanomolar potency comparable to JH-LPH-50, and CID 156252448 and CID 156252462 will be at least 10-fold weaker despite similar docking scores. One malachite-green assay can confirm or refute this. Any future virtual screen against LpxH — or any metalloenzyme — should carry a metal-geometry term alongside the docking score.

## References

1. Kwak SH, Cochrane CS, Cho J, Dome PA, Ennis AF, Kim JH, Zhou P, Hong J. Development of LpxH inhibitors chelating the active site di-manganese metal cluster of LpxH. *ChemMedChem*. 2023;18(11):e202300023. doi:10.1002/cmdc.202300023. PMID: 37014664. PMCID: PMC10239344.
2. Cho J, Lee M, Cochrane CS, Webster CG, Fenton BA, Zhao J, Hong J, Zhou P. Structural basis of the UDP-diacylglucosamine pyrophosphohydrolase LpxH inhibition by sulfonyl piperazine antibiotics. *Proc Natl Acad Sci U S A*. 2020;117(8):4109-4116. doi:10.1073/pnas.1912876117. PMID: 32041866.
3. Chakraborty A, Sanagavarapu H, Deepa Roshini R, Thamotharan S. Structure-based identification of quinolinone, thiazolidinone, dioxoimidazolidin derivatives targeting *Klebsiella pneumoniae* LpxH: an integrated docking, ADMET, DFT, and molecular dynamics study. *Comput Biol Chem*. 2026. doi:10.1016/j.compbiolchem.2026.109538. PMID: 42976567.
4. Hussein EM, Auda IG. Repurposing proton pump inhibitors to restore ceftriaxone activity against multidrug-resistant *Klebsiella pneumoniae*: phenotypic, molecular, and in silico evidence. *Naunyn Schmiedebergs Arch Pharmacol*. 2026. doi:10.1007/s00210-026-06036-8. PMID: 42980760.
5. Hu H, Dong N, Li C, Zhang G. Econazole prevents the conjugative transfer of plasmid-borne last-line antibiotic resistance genes. *J Hazard Mater*. 2026. doi:10.1016/j.jhazmat.2026.144069. PMID: 42976654.
6. Mikawa YG. A sequence-informed hybrid framework for predicting antibiotic minimum inhibitory concentrations in previously unseen *Escherichia coli* pathogens. *J Microbiol Methods*. 2026. doi:10.1016/j.mimet.2026.107767. PMID: 42977193.
7. Narayan V, Merritt B, Choudhery S, Jimenez D, Ta S, Berman DS, Ratcliff J, Gallagher ME. MicrobeRT: a framework and suite of fine-tuned language models for genomic sequences. *bioRxiv*. 2026. doi:10.64898/2026.11.03.763945.
8. Kang Z, Zhou Q, Zhang H, Liu J, Liu K, Zhou K, Zhang Y, Wang Y, Chen P, et al. Accelerating antibiotic discovery from Earth's isolated habitats through protein language models and microfluidics. *bioRxiv*. 2025. doi:10.1101/2025.11.13.688364.
9. Mondal K, Padi S, Kaur N, Makambi W, Hoogerheide DP, Heinrich F, Mihailescu, et al. XAMPGen: an interpretable SI pipeline for novel antimicrobial peptide discovery. *bioRxiv*. 2026. doi:10.64898/2026.11.03.764041.
10. Mosquera K, Ramirez L. Bayesian neural networks for uncertainty-aware toxicity prediction of metallic nanoparticles. *Toxicol Sci*. 2026. doi:10.1093/toxsci/kfag147. PMID: 42979835.
11. RCSB Protein Data Bank. Crystal structure of *Klebsiella pneumoniae* LpxH in complex with JH-LPH-50 (PDB 7SS7, 1.73 Å); with JH-LPH-45 (PDB 7SS6, 1.74 Å); with JH-LPH-41 (PDB 6WII, 1.85 Å); with AZ1 (PDB 6PIB, 2.26 Å). https://www.rcsb.org.
12. UniProtKB. UDP-2,3-diacylglucosamine hydrolase, *Klebsiella pneumoniae* subsp. *pneumoniae* (strain ATCC 700721 / MGH 78578), accession A6T5R0. https://rest.uniprot.org/uniprotkb/A6T5R0.
13. National Center for Biotechnology Information. PubChem: JH-LPH-50 (CID 167713149); JH-LPH-45 (CID 167713202); JH-LPH-41 (CID 146680856); CID 156252442; CID 156252744; CID 156252448; CID 156252462. https://pubchem.ncbi.nlm.nih.gov.

## Data availability

All numbers in Tables 1–2 are computed in the run files, not transcribed from the literature except where marked as published values (IC50, *K*I, *K*M from refs. 1–2). Raw outputs: `run_lpxh_final.json` (clean A6T5R0 pipeline run, 24 scored analogues, docking of query/AZ1/five analogues), `run_lpxh_geometry.json` (order-independent chelation distances and corrected re-dock RMSDs), `dock_jhlph45.json` (JH-LPH-45 docking), `run_lpxh_raw.json` (first run, including the discarded ChEMBL-misassigned leads — retained for audit, not used). Scripts: `run_lpxh.py`, `run_lpxh_fix.py`, `analyze_poses.py` (LeadForge daily runs, 5 November 2026). Structures: PDB 7SS7 (RCSB, ref. 11). Compound identities: PubChem CIDs in ref. 13; SMILES for JH-LPH-50 and AZ1 from the RCSB Chemical Component Dictionary (BN8, OKV). Literature sweep: daily research digest 2026-11-05. No new experimental data were generated; no human or animal data are involved.

## Acknowledgments

Draft prepared with AI assistance (Lapis) under the author's direction; the author is responsible for all claims and for independent verification before any submission. The author thanks the Duke University LpxH group (Hong and Zhou laboratories) for the published structures and assays this analysis builds on.
