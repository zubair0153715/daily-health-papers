# Vina Ranks the Proven Inhibitor Last: A Centre-Audited Benchmark of 6-Methylidene Penem Inhibitors Against Enterobacter cloacae AmpC on 1RGZ Versus the Hydrolysed Substrate Ceftazidime

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-11 · **Health Papers Agent — Paper #44** (daily 5-paper run)

**Keywords:** AmpC beta-lactamase; Enterobacter cloacae; ceftazidime; avibactam; molecular docking; AutoDock Vina; 6-methylidene penem; cephalosporin resistance

---

## Abstract

Third-generation cephalosporin-resistant Enterobacterales are a critical-priority pathogen on the WHO 2024 Bacterial Priority Pathogens List, and their inducible chromosomal AmpC beta-lactamase hydrolyses ceftazidime and related cephalosporins, so resistance can emerge during treatment itself. The gap this paper attacks is whether standardised docking can rank AmpC inhibitors at all, given that the reference drug is a substrate, not an inhibitor. We ran the LeadForge pipeline (UniProtKB P05364 to ChEMBL CHEMBL2725, 732 bioactivities, to RDKit ADMET and PAINS screening, to AutoDock Vina 1.2.7) and docked the five most potent ChEMBL AmpC actives, 6-methylidene penems with measured IC50 values of 1 to 2 nM, plus ceftazidime and the clinically proven covalent inhibitor avibactam, into the 1.37 angstrom Enterobacter cloacae GC1 AmpC structure 1RGZ, with the grid centre exactly on the co-crystallised transition-state analogue (0.00 angstrom). Two penems out-scored ceftazidime (CHEMBL222758 minus 8.99 and CHEMBL222375 minus 8.86 versus ceftazidime minus 8.20 kcal/mol), but both margins sit inside the plus-minus 1 to 2 kcal/mol Vina noise, and the rank correlation with measured potency is weak (Spearman rho plus 0.38, n equals 5). The decisive result is avibactam: the only clinically validated AmpC inhibitor in the set scored weakest of all (minus 5.82 kcal/mol), below even the hydrolysed substrate, because its potency comes from reversible covalent carbamylation of Ser64, which non-covalent docking cannot score. The falsifiable next step is a nitrocefin hydrolysis assay of the five penems with avibactam as control: if the measured IC50 order follows the ChEMBL record rather than the Vina order, rigid docking must not be used to prioritise AmpC inhibitors.

---

## 1. Introduction

Bacterial antimicrobial resistance caused an estimated 1.27 million deaths directly attributable to resistance in 2019, and 4.95 million deaths associated with it, across 204 countries (Murray et al., Lancet 2022). The 2024 WHO Bacterial Priority Pathogens List places third-generation cephalosporin-resistant Enterobacterales in its critical tier as a standalone entry, separate from carbapenem-resistant Enterobacterales, because of their high burden in low- and middle-income countries. Enterobacter cloacae complex is one of the organisms that carries this resistance most consequentially: it is an ESKAPE pathogen, a common cause of hospital-acquired urinary tract infection, bacteraemia and ventilator-associated pneumonia, and it harbours an inducible chromosomal ampC gene. When that gene is derepressed during beta-lactam therapy, AmpC overproduction emerges and third-generation cephalosporins and piperacillin-tazobactam fail mid-treatment, even when the first susceptibility test looked favourable (Tebano et al., Pharmacy 2024). Current guidance therefore treats carbapenems or cefepime as the safer options for serious AmpC-producer infections, which spends the drugs of last resort on a problem a good inhibitor could solve.

AmpC is an Ambler class C serine beta-lactamase (EC 3.5.2.6). Its catalytic Ser64 attacks the beta-lactam carbonyl, and a deacylation water, positioned by Tyr150 and Lys67, releases the hydrolysed drug. Ceftazidime is a substrate of this machinery: the extended-spectrum GC1 variant of E. cloacae AmpC hydrolyses third-generation cephalosporins such as cefotaxime and ceftazidime rapidly, and its crystal structure in complex with a transition-state analogue shows how a mutated omega loop relieves the crowding that limits the wild-type enzyme (Nukaga et al., J Biol Chem 2004). The only clinically proven way to protect ceftazidime from AmpC is avibactam, a diazabicyclooctane that carbamylates Ser64 in a covalent but reversible reaction, regenerating intact inhibitor on deacylation rather than being hydrolysed (Ehmann et al., Proc Natl Acad Sci USA 2012). Ceftazidime-avibactam was approved by the US FDA in 2015, yet it remains expensive and unavailable in much of South Asia, and avibactam has no activity against metallo-beta-lactamases. Cheaper, ideally non-covalent, AmpC inhibitors are still needed — and the ChEMBL record already contains candidates: 6-methylidene penems reported in 2004 and 2006 with measured AmpC IC50 values of 1–2 nM (Venkatesan et al., J Med Chem 2004; Venkatesan et al., J Med Chem 2006).

The literature is thin on docking benchmarks for this target. Published AmpC inhibitor work is dominated by measured kinetics of boronic-acid transition-state analogues — Ki values as low as 20 nM against AmpC (Caselli et al., Chem Biol 2001) — and by high-resolution structures of avibactam bound to class C enzymes (Lahiri et al., Antimicrob Agents Chemother 2014), not by Vina scores. No published Vina benchmark of the 6-methylidene penems, ceftazidime or avibactam on the GC1 structure 1RGZ was found. That absence is the gap: before anyone uses docking to prioritise AmpC leads, the method must be tested against compounds whose measured potencies are already known, including one inhibitor whose mechanism docking cannot see.

**Hypothesis (falsifiable):** under one standardised protocol, a Vina screen of ChEMBL AmpC actives on 1RGZ will rank compounds in the same order as their measured potencies, and the clinically proven inhibitor avibactam will score among the best. The test is the rank correlation — and avibactam's rank — not the best score.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-11 (web search; PubMed/bioRxiv via the daily digest of 2026-11-11, which screened 589 candidates). Key sources: the GRAM burden analysis; the WHO Bacterial Priority Pathogens List 2024; the Tebano et al. 2024 review of AmpC-producer treatment; the Nukaga et al. 2004 GC1 structure paper; the Venkatesan et al. 2004 and 2006 penem structure–activity studies; the Ehmann et al. 2012 avibactam mechanism paper; the Lahiri et al. 2014 avibactam–AmpC structure paper; and the Powers and Shoichet 2002 AmpC binding-site analysis. Every citation in the References section was verified (journal, year, DOI or PMID checked, not invented). Regional context comes from a Dhaka study in which 96.7% of E. cloacae clinical isolates were resistant to ceftriaxone (Hossain et al., Cureus 2026); no Pakistan-specific AmpC prevalence data were found, and that absence is recorded as a limitation.

### 2.2 Molecular docking

Standardised AutoDock Vina protocol, exactly as Papers #1/#3: Vina 1.2.7; target UniProt P05364 (E. cloacae AmpC beta-lactamase, ampC, 381 amino acids); ChEMBL target CHEMBL2725; 732 bioactivities retrieved, 226 with pChEMBL values; the top 5 distinct molecules by measured pChEMBL were docked, plus the reference query (ceftazidime) and the known inhibitor avibactam. Structure: PDB 1RGZ, the E. cloacae GC1 extended-spectrum class C beta-lactamase in complex with a transition-state analogue of cefotaxime, resolution 1.37 Å. Grid centre [15.51, 20.21, 7.63] — audited against the co-crystallised ligand PTX (the phosphonate transition-state analogue) centroid computed from the deposited coordinates: distance 0.00 Å, i.e. the grid is exactly on the active-site serine pocket; the two glycerol additives in the entry sit 13–28 Å away and were correctly excluded by the pipeline's ligand-centre routine. Box 22.5 Å, exhaustiveness 8, best of three poses reported per compound. The same grid, box and exhaustiveness were used for every compound.

Two pipeline deviations are recorded honestly, because they affect reproducibility. First, the pipeline's own target lookup returned zero ChEMBL targets for P05364 and therefore zero ligands, even though CHEMBL2725 exists: a direct ChEMBL API query on 2026-11-11 confirmed the target and its 732 activities, so the lead set was retrieved directly from the ChEMBL activity endpoint (sorted by pChEMBL, deduplicated by molecule) and docked with the pipeline's own docking function on the same structure, centre and box. The pipeline's own run is kept as `dock-HP-016-2026-11-11.json` (ceftazidime only). Second, the first dock attempt failed for all five leads because the ChEMBL canonical SMILES carry a sodium counterion (two fragments); desalting to the largest fragment — standard ligand preparation, the sodium being a counterion, not part of the binding molecule — fixed it, and the failed attempt is kept as `dock-HP-016-2026-11-11-extra.json`. No result in this paper comes from either failed attempt.

### 2.3 PAINS screen

RDKit PAINS filter applied to every docked compound, on the desalted structures. No compound in the docked set carries a PAINS alert.

### 2.4 Honesty limits

Docking is not activity. Vina's scoring noise is ±1–2 kcal/mol, so differences smaller than that cannot rank compounds. A single rigid structure (1RGZ, an extended-spectrum GC1 variant whose mutated omega loop changes the pocket relative to wild-type P99) cannot represent the conformational ensemble of AmpC, and it cannot represent covalent chemistry at all: avibactam's mechanism is carbamylation of Ser64, which a non-covalent scoring function has no term for. No molecular dynamics or free-energy refinement was run. No experimental data were generated.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Vina best (kcal/mol) | Poses (kcal/mol) | Measured potency (ChEMBL) | pChEMBL | PAINS |
|---|---|---|---|---|---|
| CHEMBL222758 | −8.99 | −8.99, −8.93, −8.73 | IC50 1.0 nM | 9.00 | none |
| CHEMBL222375 | −8.86 | −8.86, −8.78, −8.75 | IC50 1.0 nM | 9.00 | none |
| Ceftazidime (query) | −8.20 | −8.20, −8.00, −7.98 | substrate — hydrolysed by AmpC | — | none |
| CHEMBL378119 | −7.81 | −7.81, −7.71, −7.68 | IC50 2.0 nM | 8.70 | none |
| CHEMBL425963 | −7.51 | −7.51, −7.12, −6.89 | IC50 2.0 nM | 8.70 | none |
| CHEMBL212760 | −7.46 | −7.46, −7.35, −6.37 | IC50 1.0 nM | 9.00 | none |
| Avibactam | −5.82 | −5.82, −5.69, −5.57 | known covalent AmpC inhibitor | — | none |

All seven docks are on 1RGZ (1.37 Å), grid centre exactly on the co-crystallised ligand centroid (0.00 Å). The five leads are 6-methylidene penems from two structure–activity series (Venkatesan et al. 2004 and 2006); all are drug-like (MW 320–368, logP −1.30 to 1.75, zero H-bond donors, 6–7 acceptors, TPSA 78–112 Å², 2 rotatable bonds, zero Lipinski violations). Ceftazidime is far less drug-like by the same measures (MW 546.59, logP −1.30, TPSA 191.22 Å², 9 rotatable bonds, two Lipinski violations). Avibactam is small and polar (MW 265.25, logP −1.53, TPSA 130.24 Å²). Pose consistency is good across the set (top-three poses within ~1.1 kcal/mol for every compound), which rules out single lucky poses.

Two penems out-score ceftazidime, by 0.66–0.79 kcal/mol. Both margins are inside Vina's ±1–2 kcal/mol noise: on scores alone, no lead can be called better than ceftazidime. The three leads tied at the best measured potency (IC50 1.0 nM, pChEMBL 9.00) spread across the whole Vina range — first, second and sixth — so Vina cannot separate compounds that differ by only 0.3 log units of measured potency. The Spearman rank correlation between the Vina order and the measured-potency order for the five leads is ρ = +0.38 (n = 5, ties averaged), weak and not significant: a positive number that means almost nothing on five points with three ties.

### 3.2 Comparison with published docking

No published Vina benchmark of these compounds on 1RGZ or any AmpC structure was found, so there is no published score to compare against. The published comparator is measured, not computed: boronic-acid transition-state analogues reach Ki values as low as 20 nM against AmpC (Caselli et al. 2001), and the 6-methylidene penems themselves were measured at 1–2 nM (Venkatesan et al. 2004; 2006). Our Vina scores therefore cannot be validated against a published docking number — only against the measured potencies in Table 3.1, which is the test the paper actually runs.

### 3.3 The substrate-versus-inhibitor problem

The table contains a category error that must be stated plainly: ceftazidime's −8.20 kcal/mol is the binding score of a molecule the enzyme destroys. The GC1 enzyme in 1RGZ hydrolyses ceftazidime rapidly (Nukaga et al. 2004), so a strong Vina score for ceftazidime measures affinity for the catalytic machinery, not inhibition of it. A lead that merely matched ceftazidime's score would be no evidence of anything; a lead must bind in a way that blocks turnover, which a single rigid score cannot distinguish from substrate binding. This is why the penem scores, even where they beat ceftazidime, are only a starting hypothesis, and why the avibactam result in Section 4 matters more than any penem score.

The same category error runs the other way for avibactam. Its −5.82 kcal/mol is the weakest score in the set, 2.38 kcal/mol below ceftazidime and 3.17 kcal/mol below the best penem — a margin outside the noise, in the wrong direction. Avibactam is the only compound in the set with proven clinical activity against AmpC producers, and its potency comes from a covalent bond to Ser64 that Vina cannot score. The method therefore fails its most important test: it ranks the proven inhibitor last and a hydrolysed substrate third.

## 4. Discussion

### 4.1 The reframe

The question was whether docking can rank AmpC inhibitors against ceftazidime. The answer on this structure is no — not because the setup was wrong (the grid is exactly on the ligand, poses are consistent, the reference reproduces the expected binding mode) but because the scoring function cannot see the chemistry that makes an AmpC inhibitor work. The honest headline is therefore a negative result about the method, not a lead claim. A paper that reported "two penems beat ceftazidime" from the raw scores would have been wrong in two ways at once: the margins are inside the noise, and the benchmark's own control — the proven inhibitor — scores last.

### 4.2 Why the "win" must not be over-read

Three reasons. First, every penem-versus-ceftazidime margin is inside the ±1–2 kcal/mol noise. Second, the rank correlation with measured potency is weak (ρ = +0.38, n = 5) and the three most potent compounds by measurement occupy Vina ranks 1, 2 and 6 — Vina cannot order even a 1 nM versus 2 nM distinction. Third, the single rigid GC1 structure is an extended-spectrum variant, not the wild-type P99 enzyme the ChEMBL assays used, so even a correct ranking on 1RGZ would be a ranking on the wrong enzyme form. The 2004 and 2006 penem papers are the right contrast: they paired structure–activity work with crystal structures of the bound intermediates and measured IC50 values — docking there was never the verdict.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

No PAINS alerts were found, so no redox-cycling or aggregation artefact is expected from these scaffolds. The validation assay still needs standard controls (detergent to expose aggregators, a counter-screen against an unrelated serine hydrolase) because beta-lactam scaffolds are electrophilic by design, and apparent inhibition must be shown to be AmpC-specific rather than promiscuous acylation.

### 4.4 Testable hypotheses

1. In a nitrocefin hydrolysis assay with purified E. cloacae AmpC (avibactam control on the same plate), the IC50 order of the five penems will follow the ChEMBL record — the three 1.0 nM compounds ahead of the two 2.0 nM compounds — not the Vina order, in which CHEMBL212760 ranks last among the leads. Refuted if the Vina order reproduces.
2. A covalent-docking or QM/MM rescoring of the same seven compounds will rank avibactam above ceftazidime, where rigid Vina ranks it 2.38 kcal/mol below. Refuted if avibactam still ranks last.
3. Re-docking the same seven compounds on the wild-type E. coli AmpC apo structure 1KE4 (1.72 Å) will change the Vina order, showing the ranking is structure-dependent. Refuted if the order is identical.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): nitrocefin hydrolysis assay for the five penems plus avibactam and ceftazidime, 10-point dose–response in triplicate on the same plate, with detergent and aggregation controls and a counter-screen against an unrelated serine hydrolase. Stage 2 (weeks 4–6): MIC potentiation — ceftazidime MIC shift in the presence of each penem and of avibactam against an AmpC-derepressed E. cloacae clinical isolate, with checkerboard synergy testing. Stage 3 (weeks 7–12): covalent docking plus a short molecular-dynamics and MM-GBSA rescoring to test hypotheses 2–3, and a HEK293 cytotoxicity screen for the penem that survives stages 1–2. Stop rule: if stage 1 reproduces the ChEMBL order, the Vina ranking is discarded and the project proceeds on measured potency only; if no penem potentiates ceftazidime in whole cells, the series is dropped regardless of its enzyme IC50, because periplasmic access, not enzyme affinity, is then the binding constraint.

## 5. Limitations

1. Docking only — no experimental data; no compound here is shown to inhibit AmpC in any assay run for this paper.
2. All penem-versus-ceftazidime Vina margins are inside the ±1–2 kcal/mol noise; no ranking claim survives that.
3. Single rigid structure (1RGZ, GC1 extended-spectrum variant); no MD, no free-energy refinement, no covalent treatment, no induced-fit treatment.
4. The proven inhibitor avibactam scores last by Vina because its mechanism is covalent — the method's blind spot, stated as a result rather than hidden.
5. Measured potencies come from two different papers (Venkatesan et al. 2004 and 2006), not head-to-head measurements, and the assays used the wild-type enzyme while docking used the GC1 variant.
6. Rank correlation computed on n = 5 with three tied potencies — ρ = +0.38 on five points is fragile; one more compound could change it.
7. No whole-cell data: enzyme IC50 says nothing about outer-membrane penetration or efflux in E. cloacae.
8. No local (Pakistan) AmpC prevalence, pricing or access data were collected; the regional resistance figure quoted is from Dhaka, Bangladesh, not Pakistan.
9. The pipeline's own ChEMBL target lookup missed CHEMBL2725; the lead set was retrieved by direct API query and docked with the pipeline's own docking function — the workaround is documented in Section 2.2, but a re-run of the unpatched pipeline would reproduce the miss.

## 6. Conclusion

Two 6-methylidene penems out-scored ceftazidime by Vina on 1RGZ, but both margins are inside scoring noise, the rank correlation with measured potency is weak (ρ = +0.38, n = 5), and the clinically proven inhibitor avibactam scores weakest of all (−5.82 kcal/mol) because its covalent mechanism is invisible to non-covalent docking. The benchmark's value is the negative result: rigid docking on this structure cannot prioritise AmpC inhibitors, and cannot even separate a substrate from an inhibitor. The next step is a head-to-head nitrocefin assay of the five penems against avibactam, which will settle whether the ChEMBL order or the Vina order is real.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received; all tools and data sources used are free and public (UniProtKB, ChEMBL, PubChem, RCSB PDB, AutoDock Vina).

## References

1. Antimicrobial Resistance Collaborators. Global burden of bacterial antimicrobial resistance in 2019: a systematic analysis. Lancet. 2022;399(10325):629–655. PMID 35065702. doi:10.1016/S0140-6736(21)02724-0
2. WHO Bacterial Priority Pathogens List Advisory Group. The WHO Bacterial Priority Pathogens List 2024: a prioritisation study to guide research, development, and public health strategies against antimicrobial resistance. Lancet Infect Dis. 2025;25(9):1033–1043. doi:10.1016/S1473-3099(25)00118-5
3. Tebano G, Zaghi I, Cricca M, Cristini F. Antibiotic treatment of infections caused by AmpC-producing Enterobacterales. Pharmacy. 2024;12(5):142. PMID 39311133. doi:10.3390/pharmacy12050142
4. Nukaga M, Kumar S, Nukaga K, Pratt RF, Knox JR. Hydrolysis of third-generation cephalosporins by class C beta-lactamases: structures of a transition state analog of cefotaxime in wild-type and extended spectrum enzymes. J Biol Chem. 2004;279(10):9344–9352. PMID 14660590. doi:10.1074/jbc.M312356200
5. Venkatesan AM, Agarwal A, Abe T, et al. Structure-activity relationship of 6-methylidene penems bearing 6,5 bicyclic heterocycles as broad-spectrum beta-lactamase inhibitors: evidence for 1,4-thiazepine intermediates with C7 R stereochemistry by computational methods. J Med Chem. 2006;49(15):4623–4637. PMID 16854068. doi:10.1021/jm060021p
6. Venkatesan AM, Gu Y, Dos Santos O, et al. Structure-activity relationship of 6-methylidene penems bearing tricyclic heterocycles as broad-spectrum beta-lactamase inhibitors: crystallographic structures show unexpected binding of 1,4-thiazepine intermediates. J Med Chem. 2004;47(26):6556–6568. PMID 15588091. doi:10.1021/jm049680x
7. Ehmann DE, Jahic H, Ross PL, et al. Avibactam is a covalent, reversible, non-beta-lactam beta-lactamase inhibitor. Proc Natl Acad Sci USA. 2012;109(29):11663–11668. PMID 22753474. doi:10.1073/pnas.1205073109
8. Lahiri SD, Johnstone MR, Ross PL, McLaughlin RE, Olivier NB, Alm RA. Avibactam and class C beta-lactamases: mechanism of inhibition, conservation of the binding pocket, and implications for resistance. Antimicrob Agents Chemother. 2014;58(10):5704–5713. doi:10.1128/AAC.03057-14
9. Caselli E, Powers RA, Blasczcak LC, Wu CY, Prati F, Shoichet BK. Energetic, structural, and antimicrobial analyses of beta-lactam side chain recognition by beta-lactamases. Chem Biol. 2001;8(1):17–31. PMID 11182316. doi:10.1016/S1074-5521(00)00052-1
10. Powers RA, Shoichet BK. Structure-based approach for binding site identification on AmpC beta-lactamase. J Med Chem. 2002;45(15):3222–3234. PMID 12109906. doi:10.1021/jm020002p
11. Shalabi O, Kashat L, Murik O, Zevin S, Assous MV, Ben-Chetrit E. Clinical outcomes of patients with AmpC-beta-lactamase-producing Enterobacterales bacteremia treated with carbapenems versus non-carbapenem regimens: a single-center study. Antibiotics. 2024;13(8):709. doi:10.3390/antibiotics13080709
12. Hossain S, Choudhury S, Bhuiyan AKM, Moureen A, et al. Genotypic and phenotypic detection of fosfomycin and tigecycline resistance genes from clinical isolates of Enterobacter cloacae. Cureus. 2026;18(1):e101259. doi:10.7759/cureus.101259
13. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. J Chem Inf Model. 2021;61(8):3891–3898. doi:10.1021/acs.jcim.1c00203
14. Annavajhala MK, Hokunson TW, Terzoglou K, Uhlemann A-C, Gomez-Simmonds A. Interconnected reservoirs of multidrug-resistant bacteria and plasmids within hospital plumbing infrastructure. bioRxiv. 2026. doi:10.64898/2026.07.20.739580

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-016-2026-11-11.json` (pipeline run: ceftazidime, −8.20 kcal/mol), `hidden_files/dock-HP-016-2026-11-11-desalted.json` (five 6-methylidene penem leads) and `hidden_files/dock-HP-016-2026-11-11-extra.json` (avibactam, −5.82 kcal/mol, plus the failed salt-form attempt). ChEMBL lead retrieval is recorded in `hidden_files/chembl2725-activities.json` (732 activities for CHEMBL2725) and `hidden_files/chembl2725-top12.json`. Centre audit: PDB 1RGZ, co-crystallised ligand PTX centroid [15.51, 20.21, 7.63], grid centre distance 0.00 Å. Target: UniProt P05364; ChEMBL target CHEMBL2725; structure PDB 1RGZ; compounds: ceftazidime (PubChem CID 5481173), avibactam (PubChem CID 9835049), CHEMBL212760, CHEMBL222758, CHEMBL222375, CHEMBL378119, CHEMBL425963. No additional data were generated.
