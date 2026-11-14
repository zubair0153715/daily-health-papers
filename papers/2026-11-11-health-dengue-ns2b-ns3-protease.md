# No Approved Dengue Drug, No Docking Winner: NSC135618 and ARDP0006 Are Indistinguishable by Vina on the DENV NS2B–NS3 Protease Allosteric and Active-Site Structures

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-11 · **Health Papers Agent — Paper #46** (daily 5-paper run)

**Keywords:** dengue virus; NS2B-NS3 protease; NSC135618; ARDP0006; molecular docking; AutoDock Vina; allosteric inhibitor; flavivirus

---

## Abstract

Dengue infected a record 14.6 million people reported to the World Health Organization in 2024, with more than 12,000 deaths, and there is still no approved antiviral drug: care is supportive only, and the single WHO-prequalified vaccine is licensed for narrow age groups in high-transmission settings. The viral NS2B-NS3 protease is the most studied dengue drug target, yet its two best-characterised published inhibitors were measured in assays that cannot be compared head-to-head: the allosteric inhibitor NSC135618 inhibits the DENV-2 protease with an IC50 of 1.8 micromolar, while the anthraquinone ARDP0006 was reported by cell-based titre reduction of more than 1 log PFU per millilitre at 1 micromolar. We asked whether standardised docking can rank them. The LeadForge pipeline (UniProtKB P29990, PubChem verification, RDKit ADMET and PAINS screen, AutoDock Vina 1.2.7) returned no ChEMBL lead set for this target, and its automatic structure pick was an NS1 complex, not the protease, so that score was discarded. We re-docked both inhibitors on two verified protease structures with grid centres exactly on the co-crystallised ligands: the allosteric structure 6MO2 (2.8 angstrom) and the closed active-site structure 3U1I (2.3 angstrom). On 6MO2, ARDP0006 scored minus 7.40 and NSC135618 minus 7.21 kilocalories per mole; on 3U1I, NSC135618 scored minus 6.84 and ARDP0006 minus 6.27. Every margin is under 1 kilocalorie per mole, inside Vina's plus-minus 1 to 2 kilocalorie per mole noise, and NSC135618 carries a PAINS alert from its azo group, so neither compound can be called better than the other by docking. The falsifiable next step is a single head-to-head DENV-2 protease inhibition assay for both compounds on the same plate, with redox and aggregation controls for the azo scaffold: if NSC135618's measured IC50 does not reproduce under those controls, its published potency is an artefact, not a lead.

---

## 1. Introduction

Dengue is the fastest-spreading mosquito-borne viral disease in the world. Cases reported to the World Health Organization rose from 505,430 in 2000 to a record 14.6 million in 2024, with more than 12,000 deaths, across more than 100 countries; from January to July 2025 alone, over 4 million cases and over 3,000 deaths were reported from 97 countries. One modelling estimate puts the true burden at 390 million infections per year, of which 96 million manifest clinically, and about half the world's population is now at risk. There is no specific treatment for dengue: management is fluids, paracetamol for fever, and careful monitoring. The only vaccine, QDenga (TAK-003), was prequalified by WHO in May 2024 but is recommended only for children aged 6–16 years in high-transmission settings. The most advanced small-molecule candidate, the NS3–NS4B interaction blocker JNJ-1802 (mosnodenvir), reached Phase II and was then halted for portfolio reprioritisation — and it does not target the protease at all.

Pakistan carries a rising share of this burden. National Institute of Health surveillance data show 21,016 confirmed cases in 2023, 24,182 in 2024 and 33,394 laboratory-confirmed cases in 2025, with transmission peaking in the post-monsoon months of September and October. Molecular surveillance of 1,162 confirmed infections in Pakistan between 2021 and 2025 found DENV-2 dominant overall (78.4%), which makes a DENV-2 protease structure the right starting point for structure-based work relevant to Pakistan.

The dengue NS2B–NS3 protease is a chymotrypsin-like serine protease (catalytic triad His51–Asp75–Ser135) that cleaves the viral polyprotein at four junctions; without it there is no infectious virus. It is the most studied dengue drug target, and at least 20 inhibitors have been reported in the literature — yet none has reached the clinic, and the two best-characterised leads were never compared head-to-head. NSC135618, found by a conformational-switch screen, is an allosteric inhibitor: it blocks the NS2B conformational change, inhibits the DENV-2 protease with an IC50 of 1.8 μM, reduces titres of DENV-2, Zika, West Nile and yellow fever viruses in cells with low-micromolar EC50 values, and has moderate cytotoxicity (CC50 48.8 μM on A549 cells). ARDP0006, an anthraquinone, was the most potent of 15 published NS2B–NS3 inhibitors tested in a human cell-based viral quantification assay: it reduced dengue viral titre by more than 1 log PFU/mL at 1 μM in HuH-7 and K562 cells and was non-cytotoxic at 1 μM over 3 days. One is a protease-assay number, the other a cell-assay number; they cannot be ranked against each other from the literature.

**Hypothesis (falsifiable):** under one standardised docking protocol, the published inhibitor with the stronger measured potency will also score better by Vina on verified DENV NS2B–NS3 protease structures. The test is the within-protocol ranking on two structures, not the best score.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-11 (web search; PubMed). The daily literature digest of 2026-11-11 screened 589 candidates and contained no dengue item, so the dengue evidence base comes from targeted searches. Key sources: the WHO dengue fact sheet (2024–2025 burden, no specific treatment); the Pakistan NIH surveillance figures reported in Dawn (18 March 2026); the Pakistan serotype study (Umair et al. 2026); Brecher et al. 2017 for NSC135618; Chu et al. 2015 for ARDP0006; Yao et al. 2019 for the allosteric structure 6MO2; Noble et al. 2012 for the active-site structure 3U1I; and Goethals et al. 2023 / Kaptein et al. 2021 for the NS4B-targeting JNJ-1802/JNJ-A07 series, which is excluded here because it does not inhibit the protease. Every citation in the References section was verified (journal, year, DOI or PMID checked, not invented).

### 2.2 Molecular docking

Standardised AutoDock Vina protocol, exactly as Papers #1/#3: Vina 1.2.7; target UniProt P29990 (DENV-2 genome polyprotein, strain Thailand/16681/1984); ligands verified in PubChem (NSC135618, CID 282274; ARDP0006, CID 3378440); box 22.5 Å, exhaustiveness 8, best of three poses reported; the same grid, box and exhaustiveness for every compound on each structure.

Two corrections to the pipeline's automatic run were necessary, and both are disclosed. **First, the ChEMBL lane failed.** The pipeline's ChEMBL target search for this target resolved to unrelated human targets (first hit CHEMBL2074, maltase-glucoamylase) and returned zero bioactivities, so no ChEMBL lead set exists for this paper. The ChEMBL API itself was verified healthy by direct query on 2026-11-11 (HTTP 200; activities served for the resolved target), so the failure is target resolution, not an outage. The paper therefore benchmarks the two published inhibitors directly, with no ChEMBL leads. **Second, the pipeline's automatic structure pick was wrong.** `find_pdb_for_uniprot` takes the highest-resolution X-ray structure cross-referenced to the whole 3,391-residue polyprotein, and it picked PDB 7K93 (2.89 Å) — which is DENV-2 NS1 in complex with a neutralising Fab, not the protease. Its −6.97 kcal/mol score for NSC135618 is therefore discarded and does not appear in the results. This is the same class of error as the 2026-11-11 centre audit (a hand-rolled pick landing on a phosphotyrosine residue in 3LXP): the fix is the same — verify the picked PDB is the target domain before trusting any score.

The corrected structures, both verified in RCSB before docking: **6MO2**, the DENV-2 NS2B–NS3 protease in complex with an allosteric inhibitor (2.8 Å; Yao et al. 2019), grid centre [−57.29, 22.88, 1.99] — exactly the centroid of the co-crystallised allosteric inhibitor JVM (chain A, 33 atoms), distance 0.00 Å, computed with the pipeline's audited `dock._ligand_center`; and **3U1I**, the DENV-3 protease in the closed, catalytically active conformation with the covalently bound peptide Bz-Nle-Lys-Arg-Arg-H (2.3 Å; Noble et al. 2012), grid centre [38.61, −42.44, 48.89] — the centroid of the co-crystallised peptide residue OAR (chain E, 11 atoms), i.e. the active-site pocket. Both compounds were docked on both structures (four docks, same protocol).

### 2.3 PAINS screen

RDKit PAINS filter applied to both compounds. NSC135618 carries a PAINS alert (its diazene/azo group); ARDP0006 carries none. The alert is reported, not hidden, and it changes the validation design (Section 4.3).

### 2.4 Honesty limits

Docking is not activity. Vina's scoring noise is ±1–2 kcal/mol, so differences smaller than that cannot rank compounds. Two rigid structures cannot represent the protease's open/closed conformational ensemble, and the allosteric pocket in 6MO2 holds the enzyme in an open, inactive conformation while 3U1I shows the closed, active one — a compound's score on one conformation says nothing certain about the other. No molecular dynamics or free-energy refinement was run. No experimental data were generated. The two published potencies come from different assay types (protease IC50 vs cell-based titre reduction) and are not head-to-head measurements.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Structure (site) | Vina best (kcal/mol) | Poses (kcal/mol) | Measured potency (published) | PAINS |
|---|---|---|---|---|---|
| ARDP0006 | 6MO2, allosteric (DENV-2) | −7.40 | −7.40, −7.37, −7.00 | >1 log titre reduction at 1 μM (HuH-7/K562 cells) | none |
| NSC135618 | 6MO2, allosteric (DENV-2) | −7.21 | −7.21, −7.18, −7.08 | IC50 1.8 μM (DENV-2 protease assay) | alert (azo) |
| NSC135618 | 3U1I, active site (DENV-3) | −6.84 | −6.84, −6.78, −6.77 | IC50 1.8 μM (DENV-2 protease assay) | alert (azo) |
| ARDP0006 | 3U1I, active site (DENV-3) | −6.27 | −6.27, −6.18, −6.11 | >1 log titre reduction at 1 μM (HuH-7/K562 cells) | none |

All four docks use the audited centres above (0.00 Å from the co-crystallised ligand centroids). Pose consistency is tight (top-three poses within 0.40 kcal/mol for every dock), which rules out a single lucky pose.

The ranking flips between structures and never escapes the noise. On the allosteric structure ARDP0006 leads by 0.19 kcal/mol; on the active-site structure NSC135618 leads by 0.57 kcal/mol. Both margins are under 1 kcal/mol — inside Vina's ±1–2 kcal/mol noise — so on scores alone neither compound can be called better than the other on either structure. Both compounds score better on 6MO2 than on 3U1I (by 0.37 and 1.13 kcal/mol respectively), which is consistent with the allosteric pocket being the more druggable, mostly hydrophobic cleft described by Yao et al., but that comparison is also within noise for NSC135618 and is a structure effect, not a compound effect.

NSC135618's drug-likeness is mixed: MW 431.24, logP 6.27 (one Lipinski violation), TPSA 117.19 Å², 5 rotatable bonds, Veber pass. Its Tox21 kNN read-across flags NR-AhR (0.767), SR-ARE (0.64) and SR-MMP (0.651) — predictions, not measurements, and not safety claims. ARDP0006 (C14H6N2O8, 1,8-dihydroxy-4,5-dinitroanthracene-9,10-dione) is a small, rigid anthraquinone with no PAINS alert; its two nitro groups and quinone core are the medicinal-chemistry liability to watch instead.

### 3.2 Comparison with published docking

No published Vina scores for NSC135618 or ARDP0006 on 6MO2 or 3U1I were found, so there is no external docking number to compare against. The published potencies are also incommensurable: a protease IC50 (NSC135618, 1.8 μM) and a cell-based titre reduction (ARDP0006, >1 log at 1 μM) measure different things, and the hypothesis — that the stronger measured compound would dock better — cannot be tested from the literature at all. That incommensurability is itself a finding: the field has two leads and no common yardstick.

### 3.3 The standardisation problem: the pipeline picked the wrong protein

The pipeline's automatic structure pick (7K93, DENV-2 NS1 + Fab) would have produced a clean-looking −6.97 kcal/mol "protease" score for a protein that is not the protease. It was caught only because the picked PDB's title was checked against the target domain before the manuscript was drafted. Any automated docking pipeline that resolves a polyprotein accession to a structure without a domain check can make this error silently — the centre was computed correctly by the audited picker, on the wrong protein. The ChEMBL lane failed in the same run for the same underlying reason (target resolution without a domain check). Both failures are reported here rather than silently corrected, because they are the kind of error that propagates into the literature when a pipeline is run at volume.

## 4. Discussion

### 4.1 The reframe

The question was whether docking can rank the two best-characterised dengue protease inhibitors. The answer is no — not because the setup was wrong (both grids sit exactly on co-crystallised ligands, poses are consistent, the structures are the right domains) but because the two compounds are within noise of each other on both structures and the ranking flips between them. The honest headline is therefore a negative result about the method and about the literature: there is no docking basis for preferring either lead, and no published head-to-head potency comparison exists to prefer one either.

### 4.2 Why the "win" must not be over-read

Three reasons. First, every margin is inside the ±1–2 kcal/mol noise. Second, the ranking reverses between the allosteric and active-site structures, so any claim of superiority would depend on which structure was picked. Third, the measured numbers being compared are from different assay types — a protease IC50 and a cell titre reduction — so even a large docking margin would not settle which compound is more potent. A paper reporting "ARDP0006 beats NSC135618 by Vina" from the 6MO2 numbers alone would be wrong in exactly the way the field keeps being wrong.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

NSC135618's azo group triggers a PAINS alert: azo compounds can act through redox cycling, aggregation or covalent reactivity rather than specific binding. That does not invalidate the published 1.8 μM IC50 — Brecher et al. supported the allosteric mechanism with binding, kinetics, mass spectrometry and mutagenesis — but it means any re-measurement must include the controls that expose artefacts: a detergent counter-screen for aggregation, a redox-cycling counter-screen, and a counter-screen against an unrelated serine protease. ARDP0006 has no PAINS alert, but its anthraquinone core (quinone + two nitro groups) carries its own redox and reactivity liabilities, so the same controls apply to it. The validation assay in Section 4.5 is designed around these controls.

### 4.4 Testable hypotheses

1. In a single head-to-head DENV-2 NS2B–NS3 protease inhibition assay (same plate, same substrate, FRET readout), NSC135618 and ARDP0006 will have IC50 values within one order of magnitude of each other — i.e. the docking tie is real. Refuted if either compound is more than 10-fold more potent than the other.
2. NSC135618's IC50 will reproduce within 2-fold in the presence of 0.01% Triton X-100 and a redox-cycling counter-screen, confirming the published potency is specific binding rather than a PAINS artefact. Refuted if the IC50 shifts more than 5-fold or the compound fails the counter-screens.
3. Re-docking both compounds on a DENV-2 closed-conformation active-site structure will preserve the 3U1I order (NSC135618 ahead), showing the active-site ranking is serotype-independent. Refuted if ARDP0006 leads on the DENV-2 closed structure.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): recombinant DENV-2 NS2B–NS3 protease expression and FRET-based inhibition assay for both compounds, 10-point dose–response in triplicate on the same plate, with detergent (0.01% Triton X-100), redox-cycling and unrelated-serine-protease counter-screens; aprotinin as a positive control. Stage 2 (weeks 4–6): DENV-2 antiviral assay in HuH-7 cells (viral titre by plaque assay) for the compound that survives stage 1, with cytotoxicity (CC50) measured in parallel on the same cells, so the selectivity index is computed from one experiment, not two papers. Stage 3 (weeks 7–12): for the surviving compound, a DENV-1/3/4 protease panel to test pan-serotype activity (the Yao et al. allosteric series is pan-flavivirus; NSC135618 already shows pan-flavivirus cell activity) plus a 100 ns molecular-dynamics rescoring of both docked poses to test hypothesis 3. Stop rule: if stage 1 shows either IC50 is a PAINS artefact (fails counter-screens), that compound is dropped and the project proceeds with the other one only.

## 5. Limitations

1. Docking only — no experimental data; neither compound is shown here to inhibit the protease in any new assay.
2. All Vina margins are inside the ±1–2 kcal/mol noise; no ranking claim survives that.
3. Two rigid structures only (6MO2 open/inactive, 3U1I closed/active); no MD, no free-energy refinement, no induced-fit treatment; the protease is conformationally flexible and neither structure is the full ensemble.
4. The two structures are different serotypes (6MO2 DENV-2, 3U1I DENV-3); serotype differences confound the structure comparison.
5. The ChEMBL lane failed (target resolution), so no ChEMBL lead set and no similarity screen exist for this paper; the comparison is two literature inhibitors only.
6. Measured potencies come from different assay types (protease IC50 vs cell titre reduction) and are not head-to-head; the hypothesis could not be tested against a common measured yardstick.
7. NSC135618 carries a PAINS alert and a logP of 6.27; ARDP0006 carries quinone/nitro liabilities; neither is a clean lead.
8. No local (Pakistan) pricing, access or formulation data were collected.

## 6. Conclusion

There is no approved dengue drug, and on the evidence here there is also no docking winner: NSC135618 and ARDP0006 score within noise of each other on both a verified allosteric structure (6MO2) and a verified active-site structure (3U1I), with the ranking flipping between them. The next step is a single head-to-head DENV-2 protease assay with PAINS controls, which will settle whether either compound's published potency is real and which, if either, deserves medicinal-chemistry effort.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received; all tools and data sources used are free and public (UniProtKB, ChEMBL, PubChem, RCSB PDB, AutoDock Vina). The author thanks the pipeline's centre-audit lesson of 2026-11-11, without which the 7K93 mis-pick in this run would have been reported as a protease result.

## References

1. World Health Organization. Dengue and severe dengue (fact sheet). https://www.who.int/news-room/fact-sheets/detail/dengue-and-severe-dengue (accessed 2026-11-11). Cases reported to WHO rose from 505,430 in 2000 to 14.6 million in 2024 with more than 12,000 deaths; January–July 2025: over 4 million cases and over 3,000 deaths from 97 countries; no specific treatment.
2. Bhatt S, Gething PW, Brady OJ, Messina JP, Farlow AW, Moyes CL, et al. The global distribution and burden of dengue. Nature. 2013;496(7446):504–507. doi:10.1038/nature12060
3. National Institute of Health, Pakistan. Advisory for the prevention and control of dengue fever. Reported in Dawn, 18 March 2026. https://www.dawn.com/news/1983155 — 21,016 cases in 2023; 24,182 in 2024; 33,394 laboratory-confirmed cases in 2025.
4. Umair M, Hakim R, Jamal Z, Ali Q, Salman M. Multi-district molecular surveillance of dengue virus in Pakistan reveals serotype cycling and recurrent DENV-2 dominance, 2021–2025. PLoS One. 2026;21(7):e0353487. doi:10.1371/journal.pone.0353487
5. Brecher M, Li Z, Liu B, Zhang J, Koetzner CA, Alifarag A, et al. A conformational switch high-throughput screening assay and allosteric inhibition of the flavivirus NS2B-NS3 protease. PLoS Pathog. 2017;13(5):e1006411. doi:10.1371/journal.ppat.1006411. PMID 28542603
6. Chu JJH, Lee RCH, Ang MJY, Wang W-L, Lim HA, Wee JLK, et al. Antiviral activities of 15 dengue NS2B-NS3 protease inhibitors using a human cell-based viral quantification assay. Antiviral Res. 2015;118:68–74. doi:10.1016/j.antiviral.2015.03.010. PMID 25823617
7. Yao Y, Huo T, Lin Y-L, Nie S, Wu F, Hua Y, Wu J, Kneubehl AR, Vogt MB, Rico-Hesse R, Song Y. Discovery, X-ray crystallography and antiviral activity of allosteric inhibitors of flavivirus NS2B-NS3 protease. J Am Chem Soc. 2019;141(17):6832–6836. doi:10.1021/jacs.9b02505. PMID 31017399
8. Noble CG, Seh CC, Chao AT, Shi PY. Ligand-bound structures of the dengue virus protease reveal the active conformation. J Virol. 2012;86(1):438–446. doi:10.1128/JVI.06225-11
9. Goethals O, Kaptein SJF, Kesteleyn B, Bonfanti J-F, Van Wesenbeeck L, Bardiot D, et al. Blocking NS3–NS4B interaction inhibits dengue virus in non-human primates. Nature. 2023;615:678–686. doi:10.1038/s41586-023-05790-6
10. Kaptein SJF, Goethals O, Kiemel D, Marchand A, Kesteleyn B, Bonfanti J-F, et al. A pan-serotype dengue virus inhibitor targeting the NS3–NS4B interaction. Nature. 2021;598:504–509. doi:10.1038/s41586-021-03990-6
11. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. J Chem Inf Model. 2021;61(8):3891–3898. doi:10.1021/acs.jcim.1c00203
12. Protein Data Bank. Structure of dengue virus protease with an allosteric inhibitor that blocks replication. PDB ID 6MO2, resolution 2.8 Å. https://www.rcsb.org/structure/6MO2
13. Protein Data Bank. Dengue virus protease covalently bound to a peptide. PDB ID 3U1I, resolution 2.3 Å. https://www.rcsb.org/structure/3U1I

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-041-2026-11-11-redock.json` (four docks on verified protease structures); the pipeline's original run, including the discarded 7K93 score, is in `hidden_files/dock-HP-041-2026-11-11.json`. Target: UniProt P29990 (DENV-2 polyprotein); compounds: NSC135618 (PubChem CID 282274), ARDP0006 (PubChem CID 3378440); structures: PDB 6MO2 and 3U1I. No additional data were generated.
