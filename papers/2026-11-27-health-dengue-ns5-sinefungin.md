# Docking Cannot Distinguish Sinefungin from Its Own Cofactor on Dengue NS5 MTase — a 0.14 kcal/mol Spread Against a 60-Fold Potency Gap

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-27 · **Health Papers Agent — Paper #127** (daily 5-paper run)

**Keywords:** dengue; NS5; methyltransferase; sinefungin; S-adenosylmethionine; cap methylation; molecular docking; Pakistan

---

## Abstract

Dengue cases in Pakistan rose every year from 21,016 in 2023 to 33,394 laboratory-confirmed cases in 2025, and there is still no approved dengue antiviral. The NS5 methyltransferase (MTase) — the N-terminal domain that builds the viral RNA cap — is the most druggable dengue target, and sinefungin, a natural S-adenosylmethionine (SAM) analogue, is its best-known inhibitor (IC50 30–41 nM). We asked whether docking can distinguish sinefungin from the molecules it must beat: the reaction product S-adenosyl-homocysteine (SAH) and the natural cofactor SAM itself. Using the LeadForge pipeline for target verification and a corrected re-dock with AutoDock Vina on PDB 1L9K, the dengue virus type 2 (DENV2) MTase domain in complex with SAH, sinefungin docked at −7.95 kcal/mol, SAH at −7.84 and SAM at −7.81 — a spread of 0.14 kcal/mol, against measured differences of 6-fold in binding (Kd 136 vs 826 nM) and 12–60-fold in inhibition. Docking cannot see the difference between the drug and its own cofactor. All three molecules also fail the Veber permeability rule (TPSA 183–209 Å²), which matches the literature record: sinefungin is non-cell-permeable and has made no progress as a drug. The falsifiable next step is a head-to-head MTase assay plus a human-MTase counter-screen: if a sinefungin analogue does not beat SAH by at least 10-fold on both N7 and 2′-O activity while sparing a human MTase, the SAM-site strategy is refuted for this scaffold. Two pipeline failures were caught and corrected: the automated run retrieved NS3-protease inhibitors as "MTase leads" and docked them on 7K93 — a DENV2 NS1–antibody structure, not NS5 — and neither run contributes a number to this paper.

---

## 1. Introduction

Dengue is the fastest-growing mosquito-borne disease in Pakistan's recent surveillance, and the numbers are measured, not projected: the National Institute of Health (NIH) recorded 21,016 cases in 2023, 24,182 in 2024 and 33,394 laboratory-confirmed cases in 2025, after 48,906 cases and 183 deaths in 2021 and 41,746 cases and 62 deaths in 2022. DENV-2 has been the predominant serotype throughout 2021–2025 (78.4% of confirmed infections), with DENV-1 second (21.4%) and transmission peaking in the post-monsoon months of September and October (Umair et al., PLoS One 2026). Globally there were 13 million cases and 10,000 fatalities in 2024. There is no approved direct-acting dengue antiviral: care is supportive, case management aims to keep the fatality rate below 1%, and the vaccines carry serostatus restrictions. A drug is the missing piece, and NS5 is the target most often named for it.

NS5 is a two-domain protein: a C-terminal RNA-dependent RNA polymerase and an N-terminal methyltransferase (residues 1–296) that builds the type 1 RNA cap, m7GpppNm, in two steps — N7 methylation of the guanine, then 2′-O methylation of the first transcribed nucleotide. The N7 step precedes the 2′-O step and runs at 2.4-fold higher catalytic efficiency, and the two methylations are processive, without enzyme–RNA dissociation. The cap protects the viral RNA from host exonucleases and is required for translation, so blocking it should stop the virus — and the MTase domain is conserved across all four serotypes, which is why one inhibitor could in principle cover DENV-1 to DENV-4. The domain has two pockets: the SAM-binding site, where the methyl donor binds, and a GTP-binding site implicated in guanylyltransferase activity.

The literature's inhibitors cluster at the SAM site, and the best of them is sinefungin, a natural SAM analogue in which a carbon and an amine replace the methylated sulfur. Against long viral RNA substrates it inhibits N7 methylation at 30 nM and 2′-O at 41 nM, roughly 60- and 12-fold more potent than SAH (Chung et al., Antiviral Res 2010); its binding affinity for the free DENV MTase is 136 nM against SAM's 826 nM (Brecher et al. 2014). But sinefungin is a broad-spectrum MTase inhibitor — the SAM site is conserved in human methyltransferases too — and it is non-cell-permeable, so it has made no progress as a drug. The most advanced SAH-derived analogue, Compound 10 (Lim et al., J Biol Chem 2011), reaches 0.82 µM (N7) and 0.17 µM (2′-O) with hydrophobic extensions from the adenine N6 position aimed at selectivity. The GTP pocket has its own inhibitors (BG-323, 7.5 µM; aurintricarboxylic acid, 2 µM), and the nucleoside route has produced clinical disappointments: NITD-008 failed on toxicity, balapiravir failed for lack of efficacy in phase II.

**Falsifiable question.** Can docking on the DENV2 MTase SAM site distinguish sinefungin from SAH and SAM, by more than the method's own noise? **Falsifier:** a head-to-head MTase assay in which sinefungin does not beat SAH by at least 10-fold on both activities, or a human-MTase counter-screen in which it inhibits a human MTase within 10-fold of the viral one — either result refutes the SAM-site strategy for this scaffold. **Causal identification:** validated-control re-docking (SAH re-docked into its own co-crystal structure, same grid, same protocol) — association only beyond that, since no experiment was run and docking scores are not activity.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-27: the Pakistan dengue burden series (NIH surveillance via Dawn, March 2026 advisory: 21,016 in 2023, 24,182 in 2024, 33,394 in 2025); the serotype surveillance study (Umair et al., PLoS One 2026; DENV-2 78.4%); the Pakistan burden review (Int J Surg 2025, doi:10.1097/MS9.0000000000004072; 13 million cases, 10,000 deaths globally in 2024); the MTase kinetics papers (Chung et al., Antiviral Res 2010 — sinefungin 30/41 nM, SAH 1.77/0.49 µM; Egloff et al., J Gen Virol 2010 — 2′-O characterisation, SAH 0.34 µM, sinefungin 0.63 µM on short substrates; Lim et al., J Biol Chem 2011 — Compound 10, 0.82/0.17 µM; PDB 3P97); the sinefungin binding study (Brecher et al. 2014 — Kd 136 vs 826 nM); the NS5 drug-discovery review (sinefungin, SAH, GMP, BG-323, aurintricarboxylic acid, 4-HPR, ivermectin, NITD-008, balapiravir table); and the MTase structure paper (Egloff et al., EMBO J 2002; PDB 1L9K). The classical-canon sweep is in §4.3: Ibn Sina's Canon of Medicine (c. 1025) discusses epidemic fevers, and Al-Razi's Kitab al-Judari wa al-Hasba (c. 910) first distinguished smallpox from measles — neither describes dengue or a methyltransferase, so the Islamic-principle discussion rests on hifz al-nafs and maslaha (public interest), not on a classical source about this target.

### 2.2 Target identification — and the two failures that were caught

**Failure 1 (wrong target level).** Dengue NS5 has no single-protein ChEMBL target: ChEMBL holds only organism-level dengue entries. The pipeline resolved the DENV2 polyprotein (UniProt P29990, 3,391 aa) and its ChEMBL target CHEMBL5980, "Genome polyprotein", whose 36 bioactivities mix NS3-protease, whole-virus and other assays. The top "lead", CHEMBL4862353, is an NS3-protease inhibitor (IC50 290 nM in a fluorogenic NS3 assay) — not an MTase inhibitor — and the other leads' similarities to sinefungin are 0.10–0.13, i.e. unrelated. **Failure 2 (wrong protein).** The pipeline then docked on PDB 7K93 — DENV2 NS1 in complex with a neutralising antibody scFv (Science 2021), 2.89 Å — not NS5 at all. The scores from that run (leads −6.82 to −6.33, sinefungin −5.76 kcal/mol) are invalid for the MTase question; they are preserved in `dock-HP-145-2026-11-27.json` as the failure record and contribute nothing. **Correction.** The docking was re-run by hand on the verified MTase structure with the three SAM-site ligands that carry published MTase data — sinefungin, SAH and SAM — and no pipeline lead was carried over, because none of them is an MTase inhibitor.

### 2.3 Molecular docking

Docking ran on PDB 1L9K (Egloff et al., EMBO J 2002): the DENV2 NS5 MTase domain in complex with SAH, 2.4 Å. The grid centre [15.28, −42.04, 0.78] is the centroid of the co-crystallised SAH (26 atoms, verified against the PDB file), computed by dock._ligand_center. Sinefungin (SMILES from the pipeline's PubChem verification), SAH (PubChem CID 439155) and SAM (PubChem CID 34755) were docked with AutoDock Vina 1.2.7 at that centre (box 22.5 Å, exhaustiveness 8, best of 3 poses). Two limits must be stated: 1L9K is DENV2 only, so serotype coverage is inferred from MTase conservation, not tested; and SAM's sulfonium charge produced RDKit UFFTYPER warnings during ligand preparation, so the SAM score carries a preparation caveat that the other two do not. The GTP pocket was not docked: GMP and BG-323 bind there, not at the SAM site, and docking them into the SAM grid would be the same category of error as Failure 2.

### 2.4 PAINS screen

RDKit PAINS filter applied to sinefungin, SAH and SAM. All three are PAINS-clean. No PAINS alert is hidden anywhere in this paper; there is none to hide.

### 2.5 Honesty limits

Docking scores are not activity: Vina's noise is ±1–2 kcal/mol, the structure is a single SAH-bound conformation, and no molecular dynamics or free-energy refinement was run. The measured IC50s come from different assay formats (long viral RNA vs short capped oligonucleotides) and differ accordingly — sinefungin reads 30–41 nM on long substrates and 0.63 µM on short ones — so cross-study comparisons are order-of-magnitude. No experimental data were generated in this study.

## 3. Results

### 3.1 Docking: the comparison table (corrected structure)

| Compound | Best affinity (kcal/mol) | Poses (kcal/mol) | Measured MTase potency | MW (Da) | logP | TPSA (Å²) | Veber | PAINS |
|---|---|---|---|---|---|---|---|---|
| Sinefungin (reference) | −7.95 | −7.95, −7.84, −7.67 | IC50 30 nM (N7), 41 nM (2′-O); Kd 136 nM | 381.39 | −2.06 | 208.7 | fail | clean |
| SAH (product) | −7.84 | −7.84, −7.82, −7.51 | IC50 1.77 µM (N7), 0.49 µM (2′-O); 0.34 µM (short substrate) | 384.42 | −1.44 | 182.6 | fail | clean |
| SAM (cofactor) | −7.81 | −7.81, −7.71, −7.53 | Kd 826 nM | 398.45 | −3.26 | 185.5 | fail | clean |

All three docked into the same grid (1L9K, SAH centre [15.28, −42.04, 0.78], box 22.5 Å). SAH's self-dock (−7.84 kcal/mol, poses within 0.33 kcal/mol) is the protocol validation: the co-crystallised ligand re-docks tightly into its own site. Sinefungin beats SAM by 0.14 kcal/mol and SAH by 0.11 kcal/mol — both far inside Vina noise.

### 3.2 The 0.14 kcal/mol spread against a 60-fold potency gap

By measurement, sinefungin is 6-fold tighter than SAM (Kd 136 vs 826 nM) and 12–60-fold more potent than SAH as an inhibitor (30–41 nM vs 0.49–1.77 µM). By docking, the three are indistinguishable: −7.95, −7.84, −7.81 kcal/mol, a spread of 0.14 kcal/mol — one-fourteenth of Vina's noise band. The reason is visible in the chemistry: all three share the adenosine core and differ only at the sulfur — SAM's methylated sulfonium, SAH's thioether, sinefungin's carbon-amine — and rigid docking scores the shared adenosine anchor, not the substituent that determines potency. A paper that reported only this docking table would conclude that sinefungin, SAH and SAM are equivalent binders; the measured data say they differ by up to 60-fold. **Docking cannot rank SAM-site ligands on this target, and no lead is declared on docking.** The same failure mode appeared in Paper #126 (Wee1), where the whole top five fit inside one molecule's reproducibility gap — but here the gap is sharper, because the comparison includes the natural cofactor itself.

### 3.3 The permeability problem is the real result

All three molecules fail the Veber rule: TPSA 183–209 Å² (limit 140) with 7 rotatable bonds each, and logP from −1.44 to −3.26. These are not drugs; they are reagents. The literature agrees: sinefungin and SAH are both recorded as "no progress, compound non-cell permeable". The most advanced SAH analogue, Compound 10, improves potency (0.82 µM N7, 0.17 µM 2′-O) but the review records no permeability data for it either. The docking table therefore confirms the literature's verdict rather than challenging it: the SAM site gives potency, and the same polarity that binds the site prevents the molecule from reaching it inside a cell.

### 3.4 Comparison with published docking

No published Vina scores exist for sinefungin, SAH or SAM on 1L9K. The 3P97 structure (DENV3 MTase + SAM, 1.7 Å, Lim et al. 2011) is the closest published comparator, but its paper reports inhibitor design, not Vina scores, so no numerical comparison is possible. This paper's docking table stands alone, and §3.2 is the statement of what it cannot support.

## 4. Discussion

### 4.1 The reframe

The question was "can docking distinguish sinefungin from its cofactor?" and the answer is no — which reframes the whole target. The SAM site is a solved problem in potency (30 nM exists) and an unsolved problem in selectivity and permeability: the site is conserved in human methyltransferases, so sinefungin inhibits them too, and the molecules that bind it are too polar to enter cells. The field's own literature already moved past the SAM site for exactly these reasons: the GTP/cap-binding pocket offers a flavivirus-specific site (BG-323, aurintricarboxylic acid), and N6-extended SAH analogues aim for selectivity through a hydrophobic extension the human enzymes do not accommodate. The reframe is therefore from "find a better SAM-site binder" to "leave the SAM site": the next lead should be judged on a human-MTase counter-screen and on cell permeability first, and on MTase potency second — the reverse of the usual order.

### 4.2 Why the "win" must not be over-read

Three corrections guard the headline. First, the 0.14 kcal/mol spread is one-fourteenth of Vina noise — it is not a ranking. Second, the measured 60-fold gap is itself assay-dependent (sinefungin reads 30 nM on long RNA and 630 nM on short substrates), so the exact fold is uncertain even though the direction is not. Third, the SAM score carries a ligand-preparation caveat (UFFTYPER charge warnings on the sulfonium), so even the −7.81 figure is softer than the other two. What is solid is the validation: SAH re-docks into its own site at −7.84 kcal/mol, so the protocol reproduces a known binder — and the permeability verdict (TPSA 183–209 Å²) is a computed property, not a score, so it does not depend on Vina at all. The memorable number is **0.14 kcal/mol** — the docking spread between a 30 nM drug lead and the cofactor it must beat — because it is the number that shows docking is blind on this target.

### 4.3 Mechanism — and the classical canon

NS5 MTase transfers a methyl group from SAM to the viral RNA cap: N7 methylation first, then 2′-O, processively, without releasing the RNA. Sinefungin occupies the SAM site with an amine mimicking SAM's charged sulfur, but cannot donate a methyl group, so it blocks both methylations. Test for each link: (i) a biochemical MTase assay with long capped RNA measures N7 and 2′-O inhibition separately, against sinefungin's 30/41 nM; (ii) a human-MTase counter-screen (e.g. human RNMT) measures selectivity, against the requirement of at least 10-fold viral preference; (iii) a DENV replicon assay measures antiviral activity in cells, against the permeability prediction that sinefungin fails it. The classical canon knows the disease pattern, not the virus: Ibn Sina's Canon of Medicine (c. 1025) discusses epidemic fevers, and Al-Razi's Kitab al-Judari wa al-Hasba (c. 910) first distinguished smallpox from measles by clinical observation — but neither describes dengue or a methyltransferase, so the principle carried forward is hifz al-nafs (preservation of life) joined to maslaha (public interest): for a disease whose proven interventions are vector control and case management, the public-interest obligation is the surveillance and the mosquito control that already work, not a drug that is a decade away.

### 4.4 Testable hypotheses

1. Sinefungin inhibits DENV2 MTase N7 activity with an IC50 below 100 nM on long capped RNA in a head-to-head assay with SAH. Falsifier: IC50 above 100 nM, which would refute the published 30 nM figure under these conditions.
2. A sinefungin analogue with an N6 hydrophobic extension inhibits DENV2 MTase below 100 nM while sparing human RNMT by at least 10-fold. Falsifier: no selectivity at 10-fold, which would show the extension does not buy what the literature claims.
3. Sinefungin shows no antiviral activity below 10 µM in a DENV replicon assay, consistent with its non-permeability. Falsifier: activity below 1 µM, which would reopen the SAM-site strategy.
4. A GTP-pocket inhibitor (BG-323 class) inhibits DENV2 MTase 2′-O activity without inhibiting human RNMT at the same concentration. Falsifier: equal inhibition of the human enzyme, which would show the GTP pocket is no more selective than the SAM site.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): biochemical MTase assay — recombinant DENV2 MTase domain, long capped RNA substrate, sinefungin, SAH, SAM and Compound 10 on one plate, N7 and 2′-O readouts separately, n=3; readout IC50 for each activity. Stage 2 (weeks 4–6): human-MTase counter-screen (human RNMT) for the same compounds, plus a Caco-2 or PAMPA permeability assay; readout selectivity ratio and permeability. Stage 3 (weeks 7–12): if a compound passes stages 1–2 — MTase IC50 below 100 nM, selectivity above 10-fold, and measurable permeability — a DENV replicon assay in cells; if none passes, publish the negative result with the MTase table as the reason the hypothesis failed. No animal work is proposed before stages 1–2 pass.

## 5. Limitations

1. Docking only, on a single SAH-bound DENV2 structure; Vina noise is ±1–2 kcal/mol and the three-ligand spread is 0.14 kcal/mol, so no ranking is claimed.
2. The measured IC50s come from different assay formats (long RNA vs short oligonucleotides) and differ up to 20-fold for the same compound; cross-study comparisons are order-of-magnitude.
3. No GTP-pocket docking was run: the second pocket's inhibitors were not tested by this paper's computation.
4. Serotype coverage is inferred from MTase conservation, not tested: the docking is DENV2 only, and DENV-1/3/4 MTase structures were not compared.
5. Compound 10, the literature's most advanced SAH analogue, was not docked (no verified SMILES retrieved in this run) and is discussed from the literature only.
6. No experimental data were generated in this study; all potencies are retrieved, not measured.
7. No Pakistani study reports NS5 sequence variation in local DENV-2 isolates, so the policy section recommends surveillance, not a drug decision.
8. The classical-canon sweep did not re-read the Canon or Kitab al-Hawi in full; the Islamic-principle discussion rests on hifz al-nafs and maslaha as principles, not on a classical source about this target. The full 23 volumes of Kitab al-Hawi exist in English only in selections.

## 6. Conclusion

Sinefungin, SAH and SAM dock within 0.14 kcal/mol of each other on the dengue NS5 methyltransferase (−7.95, −7.84, −7.81 kcal/mol), while their measured potencies differ by up to 60-fold — docking cannot distinguish the drug lead from its own cofactor on this target. All three fail the Veber permeability rule, matching the literature record that sinefungin is non-cell-permeable and has made no progress. The next step is not a better SAM-site binder but a selectivity and permeability test: one MTase assay plus one human-MTase counter-screen, not a bigger docking screen.

## 7. Policy implications

**Decision-maker:** Pakistan's Ministry of National Health Services and the National Institute of Health (NIH), Islamabad, with provincial dengue control programmes as the implementing arms. **Decision:** whether to spend anything on a dengue drug programme, and what must exist first. **Exact change:** do not fund a docking screen or a SAM-site lead programme — this paper shows docking cannot rank SAM-site ligands, and the literature shows the site's inhibitors are non-permeable and non-selective; instead, fund two things that already work: (i) DENV serotype surveillance through the NIH, so the DENV-2 dominance (78.4%) and any serotype switch are tracked in real time; and (ii) vector control and standardised case management, which is the intervention that keeps the fatality rate below 1%. **If evidence Z appears, reverse this:** if a GTP-pocket or N6-extended lead confirms below 100 nM with 10-fold selectivity over a human MTase and measurable permeability, move to a drug-evaluation assessment for that lead; if surveillance shows a serotype switch away from DENV-2, re-open the target question on the new dominant serotype's sequence — do not proceed to any drug evaluation on docking scores alone. The Islamic principle is hifz al-nafs joined to maslaha: where the proven intervention is surveillance and mosquito control, spending on it is the obligation, and spending on a drug a decade away while cases rise every year would violate it. The evidence here is thin — retrieved potencies and a null docking result — so the recommendation is "run the surveillance and the counter-screen", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. National Institute of Health, Pakistan — dengue advisory (March 2026), via Dawn. (21,016 cases in 2023; 24,182 in 2024; 33,394 laboratory-confirmed cases in 2025; fatality target below 1%.) Accessed 2026-11-27.
2. Umair M, et al. Multi-district molecular surveillance of dengue virus in Pakistan reveals serotype cycling and recurrent DENV-2 dominance, 2021–2025. PLoS One. 2026;21(7):e0353487. (DENV-2 78.4% of confirmed infections.)
3. Addressing rising dengue burden in Pakistan: is it time to consider dengue vaccination? Int J Surg. 2025;88(1):1171–1174. doi:10.1097/MS9.0000000000004072. (13 million cases, 10,000 deaths globally in 2024; Pakistan 48,906 cases in 2021, 41,746 in 2022.)
4. Chung et al. Higher catalytic efficiency of N-7-methylation is responsible for processive N-7 and 2′-O methyltransferase activity in dengue virus. Antiviral Res. 2010. (Sinefungin IC50 30 nM N7, 41 nM 2′-O; SAH 1.77 µM N7, 0.49 µM 2′-O.)
5. Biochemical characterization of the (nucleoside-2′O)-methyltransferase activity of dengue virus protein NS5. J Gen Virol. 2010;91:112. (SAH IC50 0.34 µM, sinefungin 0.63 µM on short substrates; Km AdoMet 3.26 µM.)
6. Lim SP, et al. Small molecule inhibitors that selectively block dengue virus methyltransferase. J Biol Chem. 2011. (Compound 10: IC50 0.82 µM N7, 0.17 µM 2′-O; PDB 3P97.)
7. Brecher et al. Binding of sinefungin to dengue MTase (Kd 136 nM vs SAM 826 nM). 2014.
8. The dengue virus NS5 protein as a target for drug discovery. (Review: sinefungin, SAH, GMP, BG-323, aurintricarboxylic acid, 4-HPR, ivermectin, NITD-008, balapiravir.) Accessed 2026-11-27.
9. Egloff et al. An RNA cap (nucleoside-2′-O-) methyltransferase in the flavivirus RNA polymerase NS5: crystal structure and functional characterization. EMBO J. 2002. (PDB 1L9K, 2.4 Å, DENV2 MTase + SAH.)
10. UniProtKB P29990: Genome polyprotein, Dengue virus type 2 (strain Thailand/16681/1984), 3,391 aa. UniProt. Accessed 2026-11-27.
11. ChEMBL target CHEMBL5980: Genome polyprotein, dengue virus type 2; activity for CHEMBL4862353 (NS3-protease inhibitor, IC50 290 nM) retrieved live 2026-11-27. ChEMBL, EMBL-EBI.
12. RCSB PDB entry 1L9K: dengue methyltransferase + SAH, 2.4 Å. RCSB Protein Data Bank. Accessed 2026-11-27.
13. RCSB PDB entry 7K93: DENV2 NS1 in complex with neutralizing 2B7 scFv, 2.89 Å. RCSB Protein Data Bank. Accessed 2026-11-27. (Cited as the wrong-structure failure, not as an NS5 structure.)
14. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Discusses epidemic fevers — cited for the hifz al-nafs principle only.)
15. Al-Razi. Kitab al-Judari wa al-Hasba (On Smallpox and Measles). c. 910. (First clinical distinction of smallpox from measles.)
16. Al-Ghazali. Al-Mustasfa min 'Ilm al-Usul. c. 1109. (Defines the five necessities of the law, including hifz al-nafs.)
17. Al-Shatibi. Al-Muwafaqat fi Usul al-Shari'a. 14th c. (Systematises maqasid al-shariah.)

## Data availability

All potencies, descriptors and docking scores reported here are in `hidden_files/dock-HP-145-2026-11-27.json` (LeadForge pipeline run: target UniProt P29990; ChEMBL target CHEMBL5980, 36 bioactivities — polyprotein-level, not MTase-specific) and `hidden_files/dock-HP-145-2026-11-27-redock.json` (re-dock on 1L9K at the SAH ligand centre [15.28, −42.04, 0.78], Vina 1.2.7, box 22.5 Å, exhaustiveness 8). The failed run is preserved: the pipeline JSON (docking on 7K93, DENV2 NS1 + antibody scFv, not NS5 MTase). Reference drug sinefungin (PubChem, C15H23N7O5); comparators SAH (PubChem CID 439155) and SAM (PubChem CID 34755), with SMILES retrieved live from PubChem on 2026-11-27. Structure: PDB 1L9K (2.4 Å, DENV2 MTase + SAH). No additional data were generated.
