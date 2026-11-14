# Daclatasvir-Class NS5A Inhibitors Are All Picomolar and All Beyond the Rule of Five: A Corrected Ligand Screen, and Why Docking Was Skipped

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-08 · **Health Papers Agent — Paper #2** (daily 5-paper run)

**Keywords:** daclatasvir; NS5A; hepatitis C; Pakistan; genotype 3a; direct-acting antiviral; drug resistance; Y93H

---

## Abstract

Pakistan carries the world's largest hepatitis C burden — about 9 million people chronically infected in 2024, about 88,000 new infections that year, and about 48,700 hepatitis deaths — and genotype 3a, the hardest genotype to cure with first-generation regimens, accounts for roughly 55–80% of Pakistani infections. Daclatasvir, the first-in-class NS5A inhibitor, blocks the viral NS5A protein at picomolar concentrations, but a single substitution, Y93H, raises its EC50 by thousands of fold, and the whole drug class is large and lipophilic. We ran the LeadForge pipeline live on 8 November 2026 (UniProtKB → ChEMBL → PubChem → RDKit → PAINS/ADMET) against the verified hepatitis C NS5A target (ChEMBL CHEMBL3307224; 48 bioactivities) and ranked daclatasvir plus 25 known NS5A inhibitors. The top five leads are indistinguishable by potency — all EC50 0.010–0.013 nM — and indistinguishable by drug-likeness: every one carries two Lipinski violations and fails Veber's rules, exactly like daclatasvir itself. Docking was skipped, honestly and deliberately: the only NS5A domain I crystal structure (PDB 1ZH1, 2.5 Å) is apo, and no co-crystal of any daclatasvir-class inhibitor with NS5A exists, so there is no experimental binding site to dock into. The falsifiable next step is a defined docking run on 1ZH1 at the modelled dimer-interface site plus a genotype 3a replicon assay of the best-ranked lead against daclatasvir on wild-type and Y93H NS5A, with a pre-registered rule that a lead must keep picomolar potency on Y93H to count as an advance; a lead that loses potency on Y93H like daclatasvir would confirm that this class has no resistance advantage to offer.

---

## 1. Introduction

Hepatitis C virus (HCV) infects about 47 million people worldwide, and Pakistan carries more of that burden than any other country: according to the World Health Organization's Global Hepatitis Report 2026, about 9.06 million Pakistanis — 3.6% of the population — were chronically infected with HCV in 2024, with about 88,199 new infections that year and about 48,715 deaths from hepatitis B and C combined. Only about 1.94 million Pakistanis had ever been diagnosed with hepatitis C by 2024, and about 2.47 million had ever started curative treatment — leaving roughly two thirds of the infected population untreated. Prevalence is highest in Punjab (8.9%), followed by Khyber Pakhtunkhwa (6.5%), Sindh (6.2%) and Balochistan (5.2%), and transmission is driven largely by unsafe healthcare injections and unscreened blood.

The genotype mix makes the Pakistani problem harder than the global average. Genotype 3a is the dominant genotype in Pakistan — a 2023 meta-analysis of studies from 1996–2020 put genotype 3 at 65.35% of isolates and subtype 3a at 55.15%, and several large Pakistani series report 3a at 76–80%. Genotype 3a matters because it was the hardest genotype for first-generation direct-acting antivirals: it responds worse to daclatasvir than genotype 1b does, and its signature resistance substitution, Y93H, confers high-level resistance.

Daclatasvir (Daklinza, BMS-790052) was the first-in-class NS5A inhibitor, approved in 2014–2015. NS5A is a 447-amino-acid zinc-binding phosphoprotein, active as a homodimer organised into three domains, essential for viral RNA replication and virion assembly. Daclatasvir binds the N-terminal region of domain I and disrupts NS5A function at picomolar concentrations: the FDA label reports EC50 values of 0.001–0.009 nM against genotype 1b and 0.003–0.050 nM against genotype 1a. Its weakness is a low barrier to resistance: substitutions at M28, Q30, L31 and Y93 in the N-terminal 100 amino acids of NS5A. Y93H alone raises the genotype 1b EC50 from 0.009 nM to 24 nM (about 2,700-fold), and in genotype 3a Y93H raises it beyond 10,000 nM; the L31V + Y93H double mutant exceeds 14,000 nM. Because daclatasvir-class drugs are the backbone of the cheapest curative regimens available in Pakistan, a successor that keeps picomolar potency on Y93H — or a cheaper way to make the existing drugs — would matter more than a marginally more potent analogue.

The question this paper asks is methodological: can a standardised, automated pipeline rank known NS5A inhibitors against daclatasvir, and what can it honestly say when the target has no liganded structure to dock into? The falsifiable hypothesis is that the top-ranked leads will be indistinguishable from daclatasvir by measured potency and by drug-likeness, and that the only meaningful differentiator in this class is the resistance profile — which no docking score on an apo structure can measure.

## 2. Methods

### 2.1 Literature basis

Sources were searched on 8 November 2026: the daily literature digest at `~/workspace/research-team/digests/2026-11-08.md` (no HCV item that day), PubMed and web search, ChEMBL (EBI), RCSB PDB and UniProtKB. Key sources: the WHO Global Hepatitis Report 2026 and WHO Pakistan hepatitis factsheet for burden figures; the 2023 meta-analysis of HCV genotypes in Pakistan (Infectious Medicine, DOI 10.1016/j.imj.2023.11.007) for the genotype 3a share; the daclatasvir FDA label for EC50 values and the resistance-substitution table; the NS5A domain I structure paper (Tellinghuisen et al., Nature 2005) for the docking decision; and the Barakat refined model of NS5A bound to daclatasvir for the proposed binding site. All ChEMBL potency values quoted were re-checked live against the ChEMBL API on 8 November 2026 for the target "Nonstructural protein 5A" (CHEMBL3307224).

### 2.2 Molecular docking — skipped, and why

The LeadForge pipeline was run live on 8 November 2026 (UniProtKB → ChEMBL → PubChem → RDKit → PAINS/ADMET). The first run was discarded after a target-resolution fault was caught and is documented here because it is part of the result.

**Fault — wrong target.** The pipeline's `uniprot_target` prefers human hits, so "Hepatitis C virus NS5A" resolved to human BTBD1 (UniProt Q9H0C5), and the ChEMBL side picked CHEMBL2074, human maltase-glucoamylase. Every "lead" in that run is an alpha-glucosidase inhibitor (iminosugar), not an NS5A inhibitor. The file `dock-HP-053-2026-11-08.json` is discarded and must not be used.

**Correction.** HCV NS5A has no standalone reviewed UniProt entry (it is cleaved from the genome polyprotein), so the pipeline cannot resolve it. The corrected run forced the verified values: ChEMBL target **CHEMBL3307224** ("Nonstructural protein 5A", Hepatitis C virus, SINGLE PROTEIN), confirmed live against the ChEMBL API, and the UniProt identifier of the HCV genotype 1b genome polyprotein **P26662** (NS5A is residues ~1973–2420 of the polyprotein), used only as the target identifier. The corrected run retrieved 48 bioactivities and ranked 26 leads with the identical pipeline code (similarity, descriptors, PAINS, ToxGuard Tox21 kNN panel).

**Docking was skipped.** The only experimental structure of NS5A domain I is PDB **1ZH1** (Tellinghuisen et al., Nature 2005), 2.5 Å, and it is apo — no inhibitor bound. Daclatasvir binds at the NS5A domain I dimer interface, a site defined only by a computational model (Barakat et al.), and no co-crystal of any daclatasvir-class inhibitor with NS5A exists. Docking into the apo structure at a modelled site would produce a number with no experimental anchor, and the template rule for this series is explicit: if no experimental structure exists for the drug site, docking is skipped and the paper says so. No docking scores are reported in this paper. The proposed docking experiment is specified in §4.5 instead.

### 2.3 PAINS screen

Every test compound was screened with the RDKit PAINS filter: daclatasvir and all 25 leads were PAINS-clean (no alerts). A ToxGuard Tox21 kNN read-across panel (12 assays) was run for each lead. The highest read-across probabilities were SR-MMP 0.376 for CHEMBL4473049 and NR-AhR up to 0.26; daclatasvir itself scored highest on SR-p53 (0.077) and NR-AhR (0.084). These are similarity-based predictions, not measurements.

### 2.4 Honesty limits

What this paper cannot show: no docking was performed, so there is no structure-based ranking at all; no experimental data are presented; the potency values are ChEMBL replicon EC50/IC50 values measured by others, not by us, and they come from different assay formats (EC50 vs IC50) that are not strictly comparable; the leads are already-known NS5A inhibitors, so no novelty of chemistry is claimed; the genotype coverage of the leads (in particular genotype 3a, which dominates in Pakistan) was not measured — the ChEMBL activities are mostly genotype 1b replicon data; and cost, the variable that decides whether a drug reaches a Pakistani patient, was not modelled.

## 3. Results

### 3.1 The ranked list: potency cannot separate the class

| Compound | Measured potency, ChEMBL | MW | logP | Lipinski violations | Veber | PAINS | Similarity to daclatasvir | Composite score |
|---|---|---|---|---|---|---|---|---|
| Daclatasvir (reference, query) | EC50 0.001–0.009 nM (GT1b, label) | 738.9 | 6.22 | 2 | fail | clean | 1.000 | 69.7 |
| CHEMBL3765311 | EC50 0.010 nM | 778.9 | 6.97 | 2 | fail | clean | 0.761 | 59.7 |
| CHEMBL4466693 | EC50 0.013 nM | 788.9 | 6.25 | 2 | fail | clean | 0.742 | 58.9 |
| CHEMBL3360472 | EC50 0.010 nM | 780.9 | 5.81 | 2 | fail | clean | 0.714 | 56.6 |
| CHEMBL4787353 | IC50 0.0116 nM | 817.8 | 5.85 | 2 | fail | clean | 0.671 | 56.4 |
| CHEMBL4756850 | IC50 0.012 nM | 817.8 | 5.85 | 2 | fail | clean | 0.671 | 56.4 |

Potencies are ChEMBL replicon values for the NS5A target (CHEMBL3307224), re-checked live on 8 November 2026; daclatasvir's EC50 is from the FDA label (genotype 1b replicon). Composite score: similarity×40 + Lipinski×20 + Veber×10 + PAINS×10 + tox×20, as in the LeadForge pipeline. All five leads are daclatasvir-class NS5A inhibitors (biphenyl-bis-imidazole analogues); none has a published common name in ChEMBL.

The headline, stated honestly: **nothing separates the class**. The top five leads span EC50 0.010–0.013 nM — a 1.3-fold range, smaller than the run-to-run variation of a replicon assay — and every one of them carries exactly the same drug-likeness profile as daclatasvir: molecular weight 769–818 Da, logP 5.8–7.0, two Lipinski violations, Veber fail (11 rotatable bonds, TPSA 174.6 Å² for daclatasvir). The composite ranking is therefore a ranking by structural similarity to daclatasvir, not by any property that would make a drug better: the most similar compound wins, and similarity to a drug is not an advantage. The whole class sits far outside the Rule of Five and succeeds anyway — daclatasvir is the proof that a 739 Da, logP 6.2 molecule can be a curative drug — which means the pipeline's Lipinski and Veber components actively penalise the exact chemistry that works on this target. A screen that ranks by drug-likeness would discard the class it is trying to improve.

### 3.2 Comparison with published work

No published Vina or Glide score for daclatasvir or any of these leads on NS5A domain I was found to benchmark against, because there is no liganded structure to dock into — which is the same reason this paper reports no docking. The nearest published structure-based work is the Barakat refined model of NS5A bound to daclatasvir, a molecular-dynamics model built on the apo 1ZH1 dimer that places the drug at the dimer interface and explains the resistance mutations (M28, Q30, L31, Y93) as contacts with the drug. That model is a hypothesis, not a structure, and it is the correct starting point for the docking experiment proposed in §4.5 — but it cannot be cited as a docking benchmark, because it reports no Vina score.

### 3.3 The standardisation / quality problem

Two things that could silently corrupt this result did occur, and one was caught. The pipeline's target-resolution fault did occur: left uncorrected, the paper would have been written about human maltase-glucoamylase inhibitors while claiming to target HCV NS5A, and the task brief's own suggested target string produced the fault. The same human-preferring ranking caused the same day's neuraminidase run to pick human ABL1 kinase. The deeper problem is structural, not procedural: the most useful number for a Pakistani clinician — the EC50 against genotype 3a, which causes most Pakistani infections — is the number the ChEMBL record does not contain. The potencies in the table are genotype 1b replicon values, and genotype 3a is precisely where daclatasvir is weakest (EC50 0.120–0.870 nM wild-type, and Y93H beyond 10,000 nM). A ranking built on genotype 1b numbers cannot answer the Pakistani question.

## 4. Discussion

### 4.1 The reframe

The result reframes the paper from a discovery claim into a negative benchmark with a useful control. There is no lead here: five compounds with EC50s of 0.010–0.013 nM are the same drug five times over by any measure that matters, and all five fail the same drug-likeness rules that daclatasvir itself fails. The durable findings are the corrected target record (CHEMBL3307224, with the BTBD1/maltase-glucoamylase fault documented so the next run does not repeat it), the demonstration that similarity-based ranking collapses when the class is uniformly potent, and the explicit statement that docking was skipped for lack of a liganded structure — a decision that protects the paper from a fabricated binding site. The most actionable negative is that the next experiment is not more similarity screening: it is a genotype 3a replicon assay against Y93H, the mutation that actually defeats the drug in the population that needs it.

### 4.2 Why the ranking must not be over-read

Three reasons. First, the potency range (1.3-fold) is smaller than assay noise, so the ranking order is arbitrary. Second, the composite score is dominated by similarity to daclatasvir (40 of 100 points), so the ranking rewards being daclatasvir-like — and the resistance profile of a daclatasvir-like molecule is daclatasvir's resistance profile. Third, the potencies are genotype 1b numbers, while the Pakistani burden is genotype 3a, where the same molecules are 10- to 100-fold less potent and where Y93H is a treatment-ending mutation. A ranking that ignores genotype and resistance is a measurement of the scoring function, not of the molecules.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

All leads are PAINS-clean, which removes one artefact class from the validation design — but PAINS-clean is a low bar, and the Tox21 read-across flags (up to SR-MMP 0.376) are predictions from neighbours, not data. The honest reading: nothing in the panel kills any lead, and nothing in it advances one either. The validation assay must still include redox controls and a counter-screen, because a clean PAINS filter does not rule out assay interference. The larger safety question — drug–drug interactions through CYP3A4 and P-glycoprotein, which matter for daclatasvir-class drugs in patients on other medicines — is not addressed by PAINS at all and needs a dedicated interaction screen for any lead that advances.

### 4.4 Testable hypotheses

1. The best-ranked lead inhibits a genotype 1b replicon with an EC50 within 2-fold of its ChEMBL value under identical assay conditions; a measured EC50 worse than daclatasvir's would confirm that the ranking is only a similarity ranking, while a better one would refute it.
2. A lead that ranks well on genotype 1b keeps picomolar potency on a genotype 3a replicon, where daclatasvir's EC50 is 0.120–0.870 nM; loss of potency on genotype 3a would show the ranking does not transfer to the Pakistani genotype.
3. A lead that ranks well keeps its potency on Y93H NS5A (genotype 1b EC50 ≤ 1 nM on the mutant, versus 24 nM for daclatasvir); loss of potency on Y93H would show the lead shares daclatasvir's resistance profile and offers no advance.
4. Docking the same six compounds on the 1ZH1 dimer at the Barakat modelled interface site, with the grid centred on the Y93 side chain, reproduces the resistance order (Y93H-sensitive compounds score worse on the mutant structure than on wild-type); failure to do so would show the modelled site cannot rank this class.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): genotype 1b replicon EC50 assay for the best-ranked lead and daclatasvir, same plate, n = 3, with a pre-registered 2-fold decision rule. Stage 2 (weeks 3–6): the same assay on genotype 3a replicon and on Y93H mutant replicons (genotypes 1b and 3a) for any compound that clears Stage 1, to test whether the lead survives the mutation that defeats daclatasvir in the Pakistani genotype. Stage 3 (weeks 7–12): docking on the 1ZH1 dimer at the Barakat modelled interface site (grid centred on Y93, 22.5 Å box, Vina 1.2.7) for any compound that clears Stage 2, plus a CYP3A4/P-glycoprotein interaction screen, since drug interactions are the safety question a replicon assay cannot see. Total compound cost is the binding constraint; all leads are commercially available research chemicals, not approved drugs, and none may be presented as a treatment.

## 5. Limitations

1. No docking was performed; no experimental data are presented. 2. The potency range of the top leads (1.3-fold) is smaller than replicon assay noise, so the ranking order is arbitrary. 3. Potencies are genotype 1b replicon values from ChEMBL; genotype 3a potency — the value that matters in Pakistan — was not measured and is not in the ChEMBL record. 4. EC50 and IC50 values from different assay formats are mixed in the table and are not strictly comparable. 5. The composite score rewards similarity to daclatasvir, which biases the ranking toward daclatasvir's own resistance profile. 6. All leads are already-known NS5A inhibitors; no new chemical matter is proposed. 7. The pipeline's target resolution picked the wrong protein (human BTBD1/maltase-glucoamylase) on the first run — other silent defaults in the same pipeline are not yet audited. 8. Cost and access, the variables that decide whether a drug reaches a Pakistani patient, were not modelled. 9. The resistance analysis is literature-based: no mutant replicon was assayed and no EC50 was measured.

## 6. Conclusion

No NS5A inhibitor in this set separates from daclatasvir: the top five leads span EC50 0.010–0.013 nM, carry the same two Lipinski violations and the same Veber failure as daclatasvir, and the ranking among them is a ranking by similarity to daclatasvir, not by any property that would make a drug better. Docking was skipped because the only NS5A domain I structure is apo and no daclatasvir co-crystal exists — and the next experiment is a genotype 3a replicon assay against Y93H, the mutation that defeats daclatasvir in the genotype that causes most Pakistani infections, not more similarity screening.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author thanks the ChEMBL, UniProtKB, RCSB PDB and PubChem teams for free, open data.

## References

1. World Health Organization. Global Hepatitis Report 2026. Geneva: WHO; 2026. (Pakistan about 9.06 million people chronically infected with HCV in 2024, 3.6% of the population; about 88,199 new HCV infections and about 48,715 hepatitis B and C deaths in 2024; 47 million HCV infections worldwide.)
2. Molecular evolution, virology and spatial distribution of HCV genotypes in Pakistan: a meta-analysis. *Infect Dis Med.* 2023. DOI: 10.1016/j.imj.2023.11.007. (Genotype 3: 65.35% of isolates; subtype 3a: 55.15%; genotype 1: 5.1%.)
3. Daclatasvir (Daklinza) prescribing information. US Food and Drug Administration. (EC50: genotype 1b 0.001–0.009 nM, genotype 1a 0.003–0.050 nM, genotype 3a 0.120–0.870 nM; resistance-associated substitutions M28, Q30, L31, Y93; Y93H genotype 1b EC50 24 nM, genotype 3a >10,000 nM; L31V + Y93H >14,000 nM.)
4. Tellinghuisen TL, Marcotrigiano J, Rice CM. Structure of the zinc-binding domain of an essential component of the hepatitis C virus replicase. *Nature.* 2005;435(7040):374–379. PMID: 15902263. DOI: 10.1038/nature03580. (NS5A domain I, PDB 1ZH1, 2.5 Å, apo; 447-amino-acid NS5A, homodimer, three domains.)
5. Barakat KH, Anwar-Mohamed A, Tuszynski JA, Robins MJ, Tyrrell DL, Houghton M. A refined model of the HCV NS5A protein bound to daclatasvir explains drug-resistant mutations and activity against divergent genotypes. *J Chem Inf Model.* 2015;55(2):362–373. DOI: 10.1021/ci400631n. (Daclatasvir modelled at the NS5A domain I dimer interface; resistance mutations M28, Q30, L31, Y93 as drug contacts.)
6. Sun JH, O'Boyle DR 2nd, Fridell RA, et al. Resensitizing daclatasvir-resistant hepatitis C variants by allosteric modulation of NS5A. *Nature.* 2015;527(7577):245–248. PMID: 26536115. DOI: 10.1038/nature15711. (Daclatasvir picomolar to low-nanomolar in vitro; NS5A-to-drug ratio about 47,000:1 at half-maximal inhibition.)
7. Wang C, Jia L, O'Boyle DR 2nd, et al. Comparison of daclatasvir resistance barriers on NS5A from hepatitis C virus genotypes 1 to 6: implications for cross-genotype activity. *Antimicrob Agents Chemother.* 2014. PMID: 24936600. PMCID: PMC4135806. (Resistance barrier rank order 1b > 4a ≥ 5a > 6a ≅ 1a > 2a JFH > 3a > 2a M31; Y93H the dominant genotype 3a resistance variant.)
8. UniProtKB. Genome polyprotein, Hepatitis C virus genotype 1b (isolate J): P26662 (3,010 aa; NS5A region residues ~1973–2420). https://www.uniprot.org/uniprotkb/P26662/entry (accessed 8 November 2026).
9. ChEMBL database, European Bioinformatics Institute. Target: Nonstructural protein 5A, Hepatitis C virus (CHEMBL3307224, single protein); bioactivities and compound potencies accessed 8 November 2026. https://www.ebi.ac.uk/chembl/.

## Data availability

All ligand-screen values reported here are in `hidden_files/dock-HP-053c-2026-11-08.json` (corrected run; the first run `hidden_files/dock-HP-053-2026-11-08.json` is discarded — it screened human maltase-glucoamylase inhibitors, not NS5A inhibitors). ChEMBL IDs: daclatasvir (query, PubChem CID 25154714), CHEMBL3765311, CHEMBL4466693, CHEMBL3360472, CHEMBL4787353, CHEMBL4756850. Target: ChEMBL CHEMBL3307224; UniProt identifier P26662 (HCV polyprotein, NS5A region). PDB 1ZH1 (apo, not docked). No additional data were generated.
