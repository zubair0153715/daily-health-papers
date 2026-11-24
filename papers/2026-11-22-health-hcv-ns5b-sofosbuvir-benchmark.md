# Sofosbuvir Re-Docks at −9.23 kcal/mol on Its Own NS5B Structure — but the Most Potent Analogue and a 13-Fold Weaker One Dock Identically, and Docking Cannot Rank This Series

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-22 · **Health Papers Agent — Paper #96** (daily 5-paper run)

**Keywords:** hepatitis C virus; NS5B polymerase; sofosbuvir; molecular docking; ChEMBL; drug resistance; direct-acting antiviral; S282T

---

## Abstract

An estimated 50 million people live with chronic hepatitis C, which caused about 242,000 deaths in 2022, and Pakistan carries an estimated 12.6 million of the combined hepatitis B and C burden — yet the cure exists: direct-acting antivirals clear the virus in over 95% of patients in 8–12 weeks. Sofosbuvir, the nucleotide NS5B polymerase inhibitor at the centre of those regimens, was launched at US$84,000 for a 12-week course against an estimated manufacturing cost of US$68–136, and its only well-documented resistance substitution, S282T, confers just 2- to 18-fold reduced susceptibility. We asked whether any measured NS5B ligand binds the polymerase active site more strongly than sofosbuvir. Using the LeadForge pipeline (UniProtKB Q8JXU8 → ChEMBL CHEMBL5375 → PubChem/RDKit, PAINS and ADMET screen → AutoDock Vina 1.2.7), we re-docked sofosbuvir and four ChEMBL ligands with measured potency on the 2.9 Å sofosbuvir-diphosphate-bound NS5B structure 4WTG, centred exactly on the co-crystallised sofosbuvir diphosphate (centre audit via dock._ligand_center), with the RNA primer/template kept in the receptor. Sofosbuvir re-docked at −9.23 kcal/mol with tight pose consistency. No analogue beat it: the best analogue scored −8.94 kcal/mol, a 0.29 kcal/mol margin inside Vina's ±1–2 kcal/mol noise. The decisive failure is the ranking itself: the most potent analogue by assay (CHEMBL5815143, EC50 53 nM) and a 13-fold weaker one (CHEMBL6047888, EC50 690 nM) docked at −8.90 and −8.94 kcal/mol — 0.04 kcal/mol apart — while the weakest compound in the set (CHEMBL109569, IC50 2,250 nM) scored worst at −7.62 kcal/mol. Docking therefore cannot rank this series, and no analogue can be claimed to beat sofosbuvir on this evidence. The honest limit: the docked sofosbuvir is the parent prodrug, while the crystal holds its diphosphate metabolite and the active form in cells is the triphosphate GS-461203; and the ChEMBL ligands have no annotated binding site, so a non-nucleoside inhibitor in the set may bind the thumb or palm allosteric site ~35 Å away, where an active-site score means nothing. The claim that any analogue beats sofosbuvir would be refuted if an NS5B polymerase assay shows an IC50 worse than the analogue's published value. The falsifiable next step is an 8–12-week NS5B polymerase-plus-replicon assay of the two best-scoring analogues against sofosbuvir, including the S282T mutant.

---

## 1. Introduction

Chronic hepatitis C virus (HCV) infection is a disease with a cure that most patients cannot reach. The World Health Organization estimates that 50 million people were living with chronic HCV in 2022, with about 242,000 deaths that year, and that only a fraction have been diagnosed and treated. Pakistan is among the five countries — with China, India, Indonesia and Nigeria — that account for 55% of the combined global hepatitis B and C burden. The cure is real: pan-genotypic direct-acting antiviral (DAA) regimens clear the virus — sustained virological response — in over 95% of patients in 8–12 weeks of once-daily oral therapy, and even patients who have failed a previous DAA regimen are cured in 96–98% of cases by 12 weeks of sofosbuvir/velpatasvir/voxilaprevir. The barrier is not biology. It is price and access: sofosbuvir was priced at US$84,000 for a 12-week course in the United States at launch, against published estimates of US$68–136 for the manufacturing cost of the same course, and for years even wealthy health systems rationed it.

Sofosbuvir is a nucleotide prodrug. Inside the hepatocyte it is metabolised to the pharmacologically active uridine analogue triphosphate GS-461203, which the NS5B RNA-dependent RNA polymerase incorporates into the growing viral RNA chain, where it acts as a chain terminator. NS5B is the viral polymerase — the enzyme that copies the HCV genome — and it is the target that makes sofosbuvir pan-genotypic: the active site is conserved across all six HCV genotypes, and the only resistance substitution ever selected in cell culture, S282T, confers only 2- to 18-fold reduced susceptibility and carries a fitness cost, so it is rarely seen in the clinic and has never blocked a cure when sofosbuvir is combined with velpatasvir and voxilaprevir. The question this paper asks is the standard one for this series: among compounds with measured NS5B potency already in ChEMBL, does any bind the polymerase active site more strongly than sofosbuvir itself — and can docking even tell them apart when the reference drug is already a near-perfect active-site binder?

The classical medical canon knew the organ long before it knew the virus: Ibn Sina's Canon of Medicine (c. 1025) treats diseases of the liver (amrad al-kabid), including jaundice and chronic liver disease, with dietary and supportive management — the Canon knows the syndrome, not the target. These texts are hypothesis sources, not evidence, but they establish that the disease burden this paper addresses is centuries old in the region, and the Islamic principle behind acting on it is hifz al-nafs, preservation of life (see §7).

**Falsifiable question.** Do ChEMBL ligands with measured NS5B potency bind the polymerase active site of the sofosbuvir-diphosphate-bound structure (PDB 4WTG) at scores beyond re-docked sofosbuvir, and would that binding translate into stronger NS5B inhibition? **Falsifier:** an NS5B polymerase assay showing an IC50 worse than the analogue's published value, or a replicon assay showing no advantage over sofosbuvir, refutes the claim for that compound. **Causal identification:** validated-control re-docking — the approved drug re-docked on a co-crystal structure of its own target, with the co-crystallised metabolite as the centre — not a comparison against nothing. Association only beyond that: docking scores are not activity.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-22: the WHO Global Hepatitis Report 2024 and the 2022 global burden analysis (Cui et al., Lancet Gastroenterology & Hepatology 2026); the sofosbuvir–NS5B structural paper (Appleby et al., Science 2015; PMID 25678663); the non-nucleoside inhibitor thumb-site structures (Biswal et al., Journal of Molecular Biology 2006; PMID 16828488); the sofosbuvir/velpatasvir/voxilaprevir resistance analysis (Journal of Hepatology 2018); the FDA prescribing information for sofosbuvir/velpatasvir (Microbiology §12.4, mechanism and S282T); the launch-price and manufacturing-cost estimates (Monash Lens, 2024); the RCSB record for PDB 4WTG; and the Islamic-canon sweep (Ibn Sina, Al-Qanun fi al-Tibb, c. 1025 — consulted in the literature-map summaries, not in full Arabic text; see Limitations).

### 2.2 Target identification

The pipeline resolved the target correctly on the first run: UniProtKB Q8JXU8 (HCV NS5B RNA-dependent RNA polymerase) → ChEMBL CHEMBL5375, "Hepatitis C virus NS5B RNA-dependent RNA polymerase", SINGLE PROTEIN, 52 bioactivities, verified live 2026-11-22. This is the correct target — unlike Paper #95 in this same run, where the pipeline resolved HBV polymerase to a human helicase first. The accession-first query ("Q8JXU8") is what made the difference, and it is now the standing practice for viral targets in this series.

### 2.3 Molecular docking — the pipeline found no structure; the redock supplies one

The pipeline's docking step returned `no_pdb_found`: its PDB picker found no structure for accession Q8JXU8. That is a picker limitation, not a fact about the field — the benchmark structure exists. PDB 4WTG is the crystal structure of HCV NS5B genotype 2a JFH-1 in complex with sofosbuvir diphosphate (GS-607596, ligand 6GS), Mn²⁺ and a symmetrical RNA primer/template, 2.9 Å (Appleby et al., Science 2015). A targeted redock script (`health-papers-agent/redock_hp040_4wtg.py`) docked sofosbuvir and the four highest-ranked ChEMBL ligands with measured potency on 4WTG, using standardised AutoDock Vina 1.2.7, exactly as Papers #1/#3: grid centre the centroid of the co-crystallised 6GS, [40.95, −44.99, 5.43], verified by direct computation from the PDB file with `dock._ligand_center` (the centre audit confirmed 6GS, 26 atoms, is the largest drug-like HETATM group in the file); box 22.5 Å, exhaustiveness 8, best of 3 poses reported. The same centre, box and exhaustiveness were used for sofosbuvir and all four analogues. The receptor preparation keeps the RNA primer/template ATOM records, so the nucleotide pocket is realistic — the diphosphate sits against the primer 3′-end, and removing the RNA would have left a hole where the ligand actually binds. Sofosbuvir is therefore the self-dock control on its own structure: a method that could not recover strong binding for the drug in the pocket it was crystallised in would be broken. One caveat, stated not smoothed over: the docked sofosbuvir is the parent prodrug SMILES as returned by PubChem (CID 45375808); the crystal holds its diphosphate metabolite GS-607596, and the pharmacologically active form in cells is the triphosphate GS-461203. The heavy-atom scaffold is the same, but the phosphate count differs, and a prodrug docking score is not a metabolite docking score.

### 2.4 PAINS screen

RDKit PAINS filter applied to sofosbuvir and the four ligands. All five are PAINS-clean. No PAINS alert is hidden anywhere in this paper; there is none to hide.

### 2.5 ADMET and toxicity read-across

RDKit descriptors computed for sofosbuvir: molecular weight 529.46, logP 1.66, 3 hydrogen-bond donors, 9 acceptors, TPSA 158.18 Å², 10 rotatable bonds, 1 Lipinski violation, Lipinski pass (1 violation allowed) and Veber pass. ToxGuard Tox21 kNN read-across (12 assays) for sofosbuvir: maximum predicted probability 0.254 (NR-AhR), a weak read-across, not a measurement, and it does not clear the compound for development. The four ligands: CHEMBL5799441 (MW 365.40, logP 1.26, HBD 2, HBA 6, TPSA 116.64 Å², 6 rotatable bonds, 0 violations; max Tox21 probability 0.094), CHEMBL109569 (MW 228.16, logP 0.22, HBD 2, HBA 6, TPSA 114.04 Å², 3 rotatable bonds, 0 violations; max 0.133), CHEMBL6047888 (MW 367.37, logP 0.99, HBD 2, HBA 8, TPSA 137.74 Å², 6 rotatable bonds, 0 violations; max 0.199) and CHEMBL5815143 (MW 375.44, logP 2.58, HBD 3, HBA 5, TPSA 118.27 Å², 5 rotatable bonds, 0 violations; max 0.109). All four are drug-like by these counts — which is expected, because all four are variations on optimised NS5B-binder scaffolds, and which is itself a warning that these descriptor counts cannot rank this class.

### 2.6 Honesty limits

Docking ≠ activity. Vina noise is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No experimental data exist for any compound in this study beyond their published ChEMBL potencies. The four ligands' measured potencies are cell-based EC50/IC50 values (replicon assays), not enzyme IC50s, and their binding sites are not annotated in ChEMBL — a non-nucleoside inhibitor among them binds the thumb or palm allosteric site, ~35 Å from the active site, where an active-site docking score is meaningless. The docked sofosbuvir is the parent prodrug, not the active triphosphate.

## 3. Results

### 3.1 Docking: the comparison table (4WTG, 2.9 Å — the drug's own structure)

| Compound | Measured NS5B potency (ChEMBL) | Best affinity, 4WTG (kcal/mol) | Top-3 poses (kcal/mol) | Median pose | Margin vs sofosbuvir |
|---|---|---|---|---|---|
| Sofosbuvir (reference) | — (approved drug) | −9.23 | −9.23, −9.03, −9.00 | −9.03 | — |
| CHEMBL6047888 | EC50 690 nM | −8.94 | −8.94, −8.86, −8.71 | −8.86 | +0.29 |
| CHEMBL5815143 | EC50 53 nM | −8.90 | −8.90, −8.64, −8.61 | −8.64 | +0.33 |
| CHEMBL5799441 | EC50 330 nM | −8.10 | −8.10, −8.04, −7.99 | −8.04 | +1.13 |
| CHEMBL109569 | IC50 2,250 nM | −7.62 | −7.62, −7.38, −7.25 | −7.38 | +1.61 |

Sofosbuvir re-docks at −9.23 kcal/mol on its own structure, with tight pose consistency (−9.23, −9.03, −9.00): the method recovers strong binding for the drug in the pocket it was crystallised in, so the protocol is not broken. No analogue beats it: the best best-pose margin (CHEMBL6047888, +0.29 kcal/mol) lies inside Vina's ±1–2 kcal/mol noise, and the second-best (CHEMBL5815143, +0.33 kcal/mol) is the same. On median pose the order is the same and the margins are the same size.

The decisive check is the comparison with measured potency, and it fails. The most potent ligand by assay, CHEMBL5815143 (EC50 53 nM), docks at −8.90 kcal/mol. A compound 13-fold weaker by assay, CHEMBL6047888 (EC50 690 nM), docks at −8.94 kcal/mol — 0.04 kcal/mol apart, a difference smaller than the rounding of either number. The weakest compound in the set, CHEMBL109569 (IC50 2,250 nM, 42-fold weaker than the best), does score worst (−7.62 kcal/mol), so the method is not random — but between 53 nM and 690 nM it sees nothing at all. A scoring function that cannot distinguish a 53 nM inhibitor from a 690 nM inhibitor, inside one target on the reference drug's own structure, cannot rank this family. The honest reading of the table is therefore a null result: no analogue beats sofosbuvir beyond noise, and the method itself fails to resolve a 13-fold potency difference.

### 3.2 Comparison with published docking

No published Vina study of sofosbuvir or these four ligands on 4WTG was found in the sweep; the comparison here is internal (ligands vs re-docked reference drug on the same structure, same protocol). The crystal structure itself (4WTG, Appleby et al. 2015) is the published ground truth for the binding mode: it shows how the sofosbuvir diphosphate is positioned by the conserved active-site residues for in-line attack on the incoming nucleotide, with the β-loop and C-terminal linker retracting to enforce replication from the 3′ terminus. The structural literature also gives the paper its most useful context: the non-nucleoside inhibitors bind a common site in the thumb domain ~35 Å from the active site (Biswal et al. 2006), which is why an active-site docking score cannot be the whole story for any ligand in this set whose mechanism is allosteric.

### 3.3 The clinical confounder that docking cannot see

Sofosbuvir's clinical record is the paper's most important context, and docking cannot see any of it. The drug's >95% cure rate is not a binding problem — it binds at the conserved active site of a polymerase that cannot easily mutate around it: S282T, the only resistance substitution, costs the virus fitness, confers only 2- to 18-fold reduced susceptibility, and has never blocked a cure in the SOF/VEL/VOX salvage regimen (96–98% SVR12 even in DAA-experienced patients, with baseline resistance substitutions having no impact on outcome). The reason sofosbuvir does not cure more people is not its affinity; it is that most of the 50 million people with chronic HCV have never been diagnosed, and that the drug was launched at a price — US$84,000 for 12 weeks — that rationed it even in wealthy health systems. A compound that out-scores sofosbuvir here by 0.29 kcal/mol would still face the same access problem, and the generic sofosbuvir now available in Pakistan at a fraction of the launch price is the intervention that actually changes the cure rate. The docking order cannot explain why the drug cures 95% of treated patients and reaches fewer than 15% of infected ones. That is a limitation of the question, not of the execution.

## 4. Discussion

### 4.1 The reframe

The question this paper can ask has changed since sofosbuvir was approved. Before approval, the question was "can a nucleotide inhibitor cure hepatitis C at all?" — now it is "which molecule, if any, beats the approved drug, and by what mechanism?" The docking benchmark is therefore a screen for successors, not for proof of concept, and its bar is higher: a new compound must beat sofosbuvir on the target and then survive the clinical test that sofosbuvir has already passed — a pan-genotypic cure with a resistance barrier no other DAA class has matched. This paper's null result is useful precisely as a null: it says the next screen must be a polymerase assay plus a replicon assay, not a bigger docking set of the same scaffold.

### 4.2 Why the "win" must not be over-read

Three reasons. First, every margin in §3.1 lies inside Vina's ±1–2 kcal/mol noise. Second, the ranking contradicts measured potency in the decisive pair — a 53 nM compound and a 690 nM compound dock 0.04 kcal/mol apart. Third, the binding sites are not annotated: any non-nucleoside inhibitor in the set binds ~35 Å from the pocket it was docked into, so its score is a property of the wrong site.

### 4.3 The site-mismatch problem is the experiment's design constraint, not a reason to stop

The four ligands were chosen by pipeline rank, not by mechanism, and ChEMBL does not annotate which NS5B site each one binds. The honest handling is to report the active-site scores with the caveat attached, and to design the validation assay so the site question is answered by the experiment: a polymerase assay measures inhibition regardless of site, and a thumb-site competition assay (or a structure) would then place the mechanism. A compound that scores poorly at the active site but inhibits the enzyme is not a failure of the compound; it is a failure of the docking site, and the assay is what tells the two apart.

### 4.4 Mechanism

Sofosbuvir's active metabolite GS-461203 is incorporated by NS5B into the growing viral RNA chain and terminates it. Test for each link: (i) an NS5B polymerase assay (primer-extension, with GS-461203 as the comparator) measures IC50 directly against sofosbuvir's metabolite; (ii) a replicon assay in Huh-7 cells measures EC50 against sofosbuvir at matched concentration, with a cytotoxicity counter-screen; (iii) an S282T mutant replicon measures whether the analogue kept the resistance barrier that defines the class — loss of activity against S282T is the likeliest way a "better" NS5B binder becomes a worse drug, because S282T is the substitution the virus actually selects.

### 4.5 Testable hypotheses

1. The best-scoring analogue binds NS5B with an IC50 within 3-fold of its published ChEMBL value in a polymerase assay. Falsifier: IC50 > 3-fold worse than published.
2. The same analogue inhibits HCV replication in a replicon assay at least as strongly as sofosbuvir at matched concentration. Falsifier: no inhibition below 1 µM.
3. The analogue keeps activity against the S282T mutant replicon within 5-fold of wild-type. Falsifier: >10-fold loss against S282T.

### 4.6 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): NS5B polymerase primer-extension assay for the two candidate analogues — CHEMBL6047888 (best best-pose, −8.94) and CHEMBL5815143 (most potent by assay, EC50 53 nM) — plus sofosbuvir's active metabolite GS-461203 as control; readout IC50, n=3, with a known weak binder as a negative control. Stage 2 (weeks 4–8): replicon assay in Huh-7 cells for the same set, plus an S282T mutant replicon for the best compound from stage 1. Stage 3 (weeks 9–12): if any analogue passes stages 1–2, solubility and plasma-protein-binding measurement; if none passes, publish the negative result with the docking data as the reason the hypothesis failed. No animal work is proposed at this stage.

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol swallows every reported margin.
2. The ranking cannot resolve a 13-fold potency difference (53 nM vs 690 nM dock 0.04 kcal/mol apart), so the set cannot test ranking at all.
3. The binding sites of the four ChEMBL ligands are not annotated; any non-nucleoside inhibitor among them was docked into the wrong pocket.
4. The docked sofosbuvir is the parent prodrug; the crystal holds the diphosphate metabolite and the active form in cells is the triphosphate GS-461203.
5. One rigid structure was used (4WTG, genotype 2a JFH-1, with engineered mutations S15G/E86Q/E87Q/C223H/V321I and a β-hairpin deletion); the NS5B active site adapts to different chemotypes, so one structure under-samples the binding landscape.
6. The pipeline's PDB picker found no structure for Q8JXU8 and skipped docking; the redock had to be supplied by hand, which shows the picker's accession mapping needs independent verification every run.
7. No data on the clinical confounder: docking cannot distinguish the >95% of treated patients who are cured from the majority of infected people who are never diagnosed or cannot afford the drug.
8. The Islamic-canon sweep used the literature-map summaries of Ibn Sina's Canon; the full Arabic text was not read, and other classical works on liver disease were not individually consulted.

## 6. Conclusion

Sofosbuvir, the nucleotide NS5B inhibitor at the centre of the hepatitis C cure, re-docks at −9.23 kcal/mol on its own 2.9 Å structure 4WTG with tight pose consistency and no PAINS alert — a validated control, not a discovery. No analogue beats it: the best best-pose margin (CHEMBL6047888, +0.29 kcal/mol) lies inside Vina noise, and the method fails its own positive control in the decisive pair — the most potent analogue by assay (EC50 53 nM) and a 13-fold weaker one (EC50 690 nM) dock 0.04 kcal/mol apart. The docking verdict is a null result, and it is useful precisely as one: this series cannot be ranked by rigid Vina scoring on a single structure, the binding sites are not annotated so some ligands may have been docked into the wrong pocket, and the next screen must be a polymerase assay plus a replicon assay, not a bigger docking set. What the docking cannot do is resolve the access split: the same drug cures over 95% of the patients who receive it while most of the 50 million infected people never receive it at all. The next step is the cheap, decisive test — a polymerase assay plus a replicon assay for the best-scoring analogues against sofosbuvir, including the S282T mutant — not another docking run.

## 7. Policy implications

**Decision-maker:** Pakistan's Drug Regulatory Authority (DRAP) and the National Hepatitis Control Programme, with the SMBBMU ORIC office as the local route. **Decision:** whether to fund a small, targeted validation of NS5B inhibition as an academic drug-discovery exercise, and whether to prioritise generic sofosbuvir procurement and case-finding over any new-molecule programme. **Exact change:** commission the 8–12-week polymerase-plus-replicon screen proposed in §4.6 for the two best-scoring analogues against sofosbuvir, instead of funding another purely computational screen of the same target; and, in parallel, ask the hepatitis programme to note explicitly that the binding question is settled — sofosbuvir's barrier to resistance is the highest in its class — and that the remaining gap is diagnosis and price, not potency: every rupee spent searching for a molecule that beats sofosbuvir by 0.29 kcal/mol is a rupee not spent finding the undiagnosed. **If evidence Z appears, reverse this:** if the best analogue beats sofosbuvir's metabolite by >10-fold in the polymerase assay and keeps activity against S282T, drop the access-only framing and fund the analogue's development; if it loses >3-fold to its published value, drop this ligand set and redirect the same screen to the next NS5B chemotypes — do not proceed to any animal or clinical work on docking scores alone. The Islamic principle is hifz al-nafs (preservation of life, a maqsad of the Sharia): where a cheap test can distinguish a usable NS5B inhibitor from a useless one for a disease that kills about 242,000 people a year, running the test is the obligation; prescribing on an untested docking score would violate it. The evidence here is thin — docking only — so the recommendation is "run the trial", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. World Health Organization. Global hepatitis report 2024: action for access in low- and middle-income countries. Geneva: WHO; 2024.
2. Cui F, et al. The burden of chronic hepatitis B and C in 2022 and progress towards elimination: a global report. Lancet Gastroenterol Hepatol. 2026. doi:10.1016/S2468-1253(25)00375-9.
3. Appleby TC, Perry JK, Murakami E, Barauskas O, Feng J, Cho A, Fox D, Wetmore DR, McGrath ME, Ray AS, Sofia MJ, Swaminathan S, Edwards TE. Structural basis for RNA replication by the hepatitis C virus polymerase. Science. 2015;347(6223):771-775. doi:10.1126/science.1259210. PMID: 25678663.
4. Biswal BK, Wang M, Cherney MM, Chan L, Yannopoulos CG, Bilimoria D, Bedard J, James MNG. Nonnucleoside inhibitors binding to hepatitis C virus NS5B polymerase reveal a novel mechanism of inhibition. J Mol Biol. 2006;361(1):33-45. doi:10.1016/j.jmb.2006.05.074. PMID: 16828488.
5. No impact of resistance-associated substitutions on the efficacy of sofosbuvir, velpatasvir, and voxilaprevir for 12 weeks in HCV DAA-experienced patients. J Hepatol. 2018;69(6):1221-1230.
6. US Food and Drug Administration. Epclusa (sofosbuvir and velpatasvir) prescribing information: Microbiology (12.4) — mechanism of action and S282T resistance.
7. Monash Lens. Eliminating hepatitis C through collaborative public health strategies. Monash University; 2024. (Sofosbuvir launch price US$84,000 per 12-week course; estimated manufacturing cost US$68–136.)
8. RCSB PDB entry 4WTG: HCV NS5B genotype 2a JFH-1 in complex with sofosbuvir diphosphate GS-607596, 2.9 Å. RCSB Protein Data Bank. Accessed 2026-11-22.
9. ChEMBL target CHEMBL5375: Hepatitis C virus NS5B RNA-dependent RNA polymerase. ChEMBL database, European Bioinformatics Institute. Accessed 2026-11-22.
10. UniProtKB Q8JXU8: RNA-directed RNA polymerase, Hepatitis C virus. UniProt. Accessed 2026-11-22.
11. PubChem CID 45375808: sofosbuvir. National Library of Medicine. Accessed 2026-11-22.
12. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; diseases of the liver, amrad al-kabid.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-040-4wtg-2026-11-22.json` (sofosbuvir + four ChEMBL ligands on 4WTG) and `hidden_files/dock-HP-040-2026-11-22.json` (Q8JXU8 pipeline run, including the skipped docking step). Reference drug sofosbuvir (PubChem CID 45375808); analogues CHEMBL6047888, CHEMBL5815143, CHEMBL5799441, CHEMBL109569. Structure: PDB 4WTG (2.9 Å). Target: UniProtKB Q8JXU8; ChEMBL target CHEMBL5375. No additional data were generated.
