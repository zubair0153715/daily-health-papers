# Five Triazolium Trypanothione Reductase Inhibitors Dock at −6.3 to −7.8 kcal/mol on Leishmania infantum TR: A Vina Benchmark, a Species Surrogate, and Two Pipeline Faults Caught

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-05 · **Health Papers Agent — Paper #2** (daily 5-paper run)

**Keywords:** trypanothione reductase; cutaneous leishmaniasis; molecular docking; AutoDock Vina; Leishmania infantum; antimonials; triazolium; ChEMBL

---

## Abstract

Cutaneous leishmaniasis is endemic in Pakistan — an estimated 59,255 cases in 2023 — and its only proven treatment in the country is still pentavalent antimonials, given as painful daily injections for 20 to 28 days, often unavailable in public facilities. Antimonials act in part by inhibiting trypanothione reductase (TR), the parasite-specific redox enzyme absent from the human host, so direct small-molecule TR inhibitors are the rational oral alternative. No standardised Vina benchmark for TR inhibitors existed, and this paper reports why the first two attempts to produce one failed. The LeadForge pipeline run on Leishmania major TR first mis-assigned the ChEMBL target to human maltase-glucoamylase (CHEMBL2074) — the same fault found in an earlier LpxH run — and no L. major TR target exists in ChEMBL and no L. major TR crystal structure exists. We therefore used Leishmania infantum TR as the surrogate (UniProt A4HSF7, ChEMBL CHEMBL1944501, 46 bioactivities) and docked five desalted triazolium inhibitors with AutoDock Vina 1.2.7 into L. infantum TR (PDB 6T95, 2.5 Å) at the centroid of the co-crystallised inhibitor MWT. The pipeline's first grid centre was the FAD cofactor centroid, 18.33 Å from the inhibitor site; all ligands were re-docked at the corrected centre. The five leads scored −6.34 to −7.79 kcal/mol: CHEMBL5414105 best at −7.79 kcal/mol despite the weakest measured potency (Ki 5.5 µM), while the most potent compound, CHEMBL5402846 (Ki 200 nM), scored only −7.18 kcal/mol — a ranking inversion that Vina cannot resolve. Sodium stibogluconate itself was not docked: it is a 13-fragment Sb(V) polymer whose active form is the Sb(III) ion, which Vina cannot represent. The falsifiable next step is a direct L. infantum TR enzyme inhibition assay of CHEMBL5402846 against CHEMBL5414105 under identical conditions, with a pre-registered rule that a docking margin under 2 kcal/mol predicts no measurable potency advantage.

---

## 1. Introduction

Cutaneous leishmaniasis (CL) is a skin infection caused by Leishmania parasites transmitted by phlebotomine sandflies, endemic in Pakistan — most in Balochistan and Khyber Pakhtunkhwa, but also in Sindh, Kashmir and Punjab. The World Health Organization estimates 600,000 to one million new CL cases occur globally each year, of which only around 200,000 are reported; in 2023, about 91% of reported cases came from just eleven countries, including Pakistan, which recorded an estimated 59,255 cases, with the true number likely much higher. Médecins Sans Frontières treated close to 12,000 CL patients in Pakistan in 2023 and over 51,000 since 2008, and has run a clinical trial since 2022 to find alternatives to the current drugs.

The current treatment is the problem. The first-line drugs, meglumine antimoniate and sodium stibogluconate, are pentavalent antimonials used for decades; treatment is daily injections for 20 to 28 days, painful, and the drugs are often unavailable in public health centres and unaffordable on the private market. Their mode of action is only partly understood: Sb(V) is a prodrug reduced to Sb(III), which interferes with thiol redox metabolism in two ways — inducing rapid efflux of intracellular trypanothione and glutathione, and inhibiting trypanothione reductase (TR) in intact cells, causing accumulation of the disulfide forms. Structural work on reduced L. infantum TR in complex with NADPH and Sb(III) showed the metal engaging the catalytic triad Cys52, Cys57 and His461′ (plus Thr335), blocking the enzyme. TR is the parasite's analogue of human glutathione reductase: it keeps trypanothione — N1,N8-bis(glutathionyl)spermidine — reduced, and the trypanothione/TR system replaces the glutathione and thioredoxin systems of the host. Because TR is essential for parasite survival and absent from mammalian cells, it is a validated, parasite-specific drug target, and a direct small-molecule TR inhibitor is the obvious route to an oral alternative to antimonials.

The question this paper asks is methodological: can a standardised, automated docking pipeline benchmark known TR inhibitors against each other on a TR crystal structure, and what fails when it tries? The falsifiable hypothesis is that five known triazolium TR inhibitors, docked under an identical protocol, will score in a narrow band consistent with their micromolar potencies — and that Vina will not rank them in potency order.

## 2. Methods

### 2.1 Literature basis

Sources were searched on 5 November 2026: the daily literature digest (2026-11-05), PubMed E-utilities and web search (verified references below), ChEMBL (EBI) and RCSB PDB. Key sources: Médecins Sans Frontières for the Pakistan CL burden and treatment-access figures; Wyllie et al. for the dual antimonial mechanism and TR inhibition in intact cells; de Lucio et al. for the triazolium inhibitor series and the 6T95 structure; and the Helmholtz-Zentrum Berlin summary for the Sb(III)–TR structural mechanism.

### 2.2 Compound selection (LeadForge pipeline) — and two faults caught

The LeadForge pipeline was run live on 5 November 2026 (UniProtKB → ChEMBL → PubChem → RDKit → PAINS/ADMET → Vina). Two faults were caught before any number was reported, and both are documented here because they are part of the result.

**Fault 1 — wrong ChEMBL target.** The first run, on "Leishmania major trypanothione reductase", resolved UniProt correctly (Q4QJG7, TRYR, L. major, 491 aa) but the ChEMBL target search returned CHEMBL2074 — human maltase-glucoamylase, a carbohydrate enzyme with no relation to TR — and its 55 bioactivities were ranked as if they were TR ligands. This is the same mis-assignment found in an earlier LpxH run, where the same CHEMBL2074 was attached to a bacterial target. A direct ChEMBL search confirms there is no L. major trypanothione reductase target in ChEMBL at all; the closest annotated targets are L. infantum (CHEMBL1944501), L. donovani (CHEMBL2176840) and L. amazonensis (CHEMBL1944500). The first run's leads were discarded in full; its raw JSON is preserved for audit.

**Correction — species surrogate.** The run was repeated on "Leishmania infantum trypanothione reductase": UniProt A4HSF7 (L. infantum TR), ChEMBL CHEMBL1944501 (single-protein, L. infantum), 46 bioactivities retrieved. Twenty-five compounds passed the Morgan-fingerprint similarity screen and 26 were ranked by composite score (similarity ×40 + Lipinski ×20 + Veber ×10 + PAINS ×10 + tox ×20). The species substitution is disclosed explicitly: L. infantum is the closest ChEMBL-annotated Leishmania TR, its TR is the standard structural surrogate for the genus, and every result below is about the L. infantum TR pocket, not L. major specifically. Cross-species extrapolation to L. major is a hypothesis, not a result.

**The lead set is thin.** Of the 26 ranked leads, 21 are giant peptidic compounds (MW 1,195–1,549, 32–58 rotatable bonds) — trypanothione analogues and substrate-like peptides that Vina cannot dock meaningfully. Only five leads are small enough to dock (MW 708–923, 11–13 rotatable bonds), and all five are salts of triazolium / triazole-phenyl-thiazole inhibitors from the de Lucio et al. 2022 series: CHEMBL5414105 (Ki 5.5 µM), CHEMBL5284653 (Kd 1.0 µM), CHEMBL5402846 (Ki 200 nM), CHEMBL5282990 (IC50 2.2 µM) and CHEMBL5266073 (IC50 2.1 µM). None has a preferred name, an approval, or a development phase in ChEMBL. Sodium stibogluconate was verified in PubChem (MW 908.88) but was not docked: its SMILES is a 13-fragment Sb(V) polymer with sodium counterions, RDKit cannot prepare it as a single molecule, and its active form is the Sb(III) ion, which Vina cannot represent at all. There is therefore no antimonial docking comparator in this paper — a limit, stated plainly.

### 2.3 Molecular docking

Docking was performed 5 November 2026 with AutoDock Vina 1.2.7, using the LeadForge protocol: the same structure, grid centre, box (22.5 Å cube), exhaustiveness (8) and pose count (3) for every ligand; best of three poses reported. The structure was L. infantum TR, PDB 6T95 (2.5 Å, "Trypanothione reductase from Leishmania infantum in complex with 4a", de Lucio et al. 2022), with the grid centred on the centroid of its co-crystallised ligand MWT — the triazolium inhibitor 4a: [24.84, −2.29, −69.97]. Receptor preparation used RDKit (Gasteiger charges, simplified AutoDock atom types); ligand preparation used meeko. Each lead was desalted before docking (largest fragment kept; iodide, trifluoroacetate and triflate counterions removed), because Vina's ligand preparation requires a single fragment. Vina's scoring noise is approximately ±1–2 kcal/mol; differences smaller than this cannot be treated as significant on scores alone.

**Fault 2 — grid centre 18.33 Å off.** The pipeline's automatic grid-centre picker takes the centroid of the first drug-like HETATM group in the PDB file. In 6T95 that group is the FAD cofactor (residue 501, 53 atoms), not the inhibitor; the centre it produced was [32.05, 3.50, −54.14]. The co-crystallised inhibitor MWT (residue 515, 39 atoms) sits 18.33 Å away at [24.84, −2.29, −69.97] — outside any reasonable interpretation of the binding site, and at the edge of the 22.5 Å box. An earlier docking attempt at the FAD centre ran for 17 minutes on a single giant peptidic ligand (110 rotatable bonds) before it was killed; no numbers from that run are reported. All five leads were docked at the corrected MWT centroid with the same protocol, and only the corrected numbers are reported. The raw JSON of every run is preserved (see Data availability), so the correction is auditable.

### 2.4 PAINS screen and toxicity read-across

Every test compound was screened with the RDKit PAINS filter: all five leads were PAINS-clean (no alerts). A ToxGuard Tox21 kNN read-across panel (12 assays) was run for each lead. The highest read-across probabilities were SR-MMP 0.253 for CHEMBL5284653, SR-ARE 0.199 for the same compound, and 0.108–0.180 for the others. These are similarity-based predictions, not measurements, and no lead carries a strong flag.

### 2.5 Honesty limits

What this paper cannot show: docking is not activity; Vina noise is ±1–2 kcal/mol; no experimental data are presented; no molecular-dynamics refinement or binding-free-energy calculation was performed; a single crystal structure (6T95, one TR conformation, L. infantum not L. major) was used; no antimonial comparator could be docked; the five leads are already-known TR inhibitors from one chemical series, so no novelty of chemistry is claimed; and the desalted cations were docked, not the salts as formulated.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | TR potency, ChEMBL | Best affinity (kcal/mol) | Poses (kcal/mol) | PAINS |
|---|---|---|---|---|
| CHEMBL5414105 | Ki 5.5 µM | **−7.79** | −7.79, −7.33, −7.28 | clean |
| CHEMBL5402846 | Ki 200 nM | −7.18 | −7.18, −7.04, −5.37 | clean |
| CHEMBL5284653 | Kd 1.0 µM | −6.96 | −6.96, −6.80, −6.80 | clean |
| CHEMBL5266073 | IC50 2.1 µM | −6.87 | −6.87, −6.81, −6.78 | clean |
| CHEMBL5282990 | IC50 2.2 µM | −6.34 | −6.34, −6.11, −6.03 | clean |

All docking on PDB 6T95 (L. infantum TR, 2.5 Å), grid centre [24.84, −2.29, −69.97] (MWT/4a centroid), box 22.5 Å, exhaustiveness 8, Vina 1.2.7, 5 November 2026, desalted cations. CHEMBL5414105: MW 728.62, logP 3.06, 1 Lipinski violation. CHEMBL5402846: MW 873.61, logP 5.93, 2 violations. CHEMBL5284653: MW 809.81, logP 3.98, 1 violation. CHEMBL5266073: MW 908.86, logP 5.58, 3 violations. CHEMBL5282990: MW 922.89, logP 5.97, 3 violations. All five are large, lipophilic, and Lipinski-marginal — none is an oral-drug candidate as drawn.

The headline is a ranking inversion, stated plainly: the best docking score belongs to the weakest compound by measured potency. CHEMBL5414105 (Ki 5.5 µM) scores −7.79 kcal/mol, while CHEMBL5402846 (Ki 200 nM — 27-fold more potent) scores only −7.18 kcal/mol, a 0.61 kcal/mol gap inside Vina's noise and in the wrong direction. The remaining three sit within 0.62 kcal/mol of each other (−6.34 to −6.96), statistically tied, against a 2.2-fold spread in measured IC50. Pose consistency is good for four of the five (within 0.51 kcal/mol across poses) but poor for CHEMBL5402846, whose third pose falls to −5.37 kcal/mol — the most potent compound has the least consistent pose set. The honest reading: Vina on 6T95 reproduces the micromolar band of this chemical series but cannot rank within it.

### 3.2 Comparison with published docking

The co-crystallised ligand 4a (MWT) is itself a member of this series, and de Lucio et al. reported the series' antileishmanial potency in cellulo, with compounds 4c and 4d — not the five docked here — as the most improved. No published Vina score for any of our five leads on 6T95 was found to benchmark against, which is itself a gap this paper fills: Vina 1.2.7 reference values for five triazolium TR inhibitors on 6T95 (−6.34 to −7.79 kcal/mol, with full pose lists) are now on record for others to reproduce. A re-dock of MWT itself into 6T95 (protocol self-validation, RMSD against the crystal pose) was not run and is listed as a hypothesis below.

### 3.3 The standardisation problem

Two of the pipeline's automated steps that could silently corrupt this result did corrupt it, and both were caught only because a human checked the ChEMBL target name and the PDB HETATM list before writing. The ChEMBL text-search fallback attached a human carbohydrate enzyme to a parasite target, and the grid-centre picker centred on the FAD cofactor 18.33 Å from the inhibitor site. Either error alone would have produced publishable-looking numbers for the wrong target or the wrong pocket. The fixes are cheap — verify the target organism and name, verify the co-crystallised ligand's identity and centroid — but they are not optional, and they must be applied per target, because neither failure is predictable from the input alone.

## 4. Discussion

### 4.1 The reframe

The result reframes the paper from a discovery claim into a benchmark plus a caution. First, a benchmark: five known triazolium TR inhibitors dock at −6.34 to −7.79 kcal/mol on 6T95 under a standardised protocol, with pose consistency good enough to reproduce. Second, a caution: Vina cannot rank this series — the most potent compound is not the best docker, and the spread of scores (1.45 kcal/mol) is inside the noise that separates a 200 nM inhibitor from a 5.5 µM one. Third, a data-quality finding: the ChEMBL record for this target is dominated by undockable peptidic compounds, and the only dockable leads are large, lipophilic, Lipinski-marginal salts from a single series. None of the five is an oral alternative to antimonials as drawn; they are a starting point for optimisation, not a treatment.

### 4.2 Why the "win" must not be over-read

Three reasons. First, the 0.61 kcal/mol gap between the best docker and the most potent compound is inside Vina's ±1–2 kcal/mol noise and points the wrong way. Second, pose inconsistency: CHEMBL5402846 loses 1.81 kcal/mol between its best and third pose, while the weaker compounds hold their scores — a genuine binder should hold its score across poses. Third, all five compounds are already-known TR inhibitors from one published series; there is no new chemistry here, only a new comparison, and the comparison is against each other, not against the antimonial that actually treats patients, because that drug cannot be docked.

### 4.3 The PAINS/tox picture is clean but thin

No PAINS alerts is good, but PAINS-clean is a low bar, and the Tox21 read-across flags (SR-MMP 0.253 at most) are predictions from neighbours, not data. The honest reading: nothing in the panel kills any lead, and nothing in it advances one either.

### 4.4 Testable hypotheses

1. CHEMBL5402846 inhibits recombinant L. infantum TR with an IC50 within 2-fold of its ChEMBL Ki (200 nM) under identical assay conditions, and inhibits it more potently than CHEMBL5414105 (Ki 5.5 µM) — the docking predicts no measurable advantage, so a >5-fold advantage for CHEMBL5402846 would refute the noise interpretation.
2. CHEMBL5402846 and CHEMBL5414105 show antileishmanial activity against intracellular L. infantum amastigotes at concentrations within 10-fold of their enzyme potencies, with a selectivity index over host macrophages > 10.
3. A Vina re-dock of the co-crystallised ligand MWT (compound 4a) into 6T95 reproduces its crystallographic pose within 2 Å RMSD (protocol self-validation; not yet run).

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): recombinant L. infantum TR enzyme inhibition assay (NADPH oxidation readout) for CHEMBL5402846, CHEMBL5414105 and CHEMBL5284653, same plate, n = 3, with a pre-registered 2-fold decision rule. Stage 2 (weeks 3–6): intracellular amastigote assay in THP-1-derived macrophages for any compound that clears Stage 1, with miltefosine as control and a host-cell cytotoxicity counter-screen. Stage 3 (weeks 7–12): aqueous solubility and microsomal stability for any compound that clears Stage 2, since all five leads are large and lipophilic and oral bioavailability is the binding constraint for an antimonial replacement. Total compound cost is the binding constraint; all five leads are commercially available research chemicals, not approved drugs, and none may be presented as a treatment.

## 5. Limitations

1. Docking only; no experimental data. 2. The species is L. infantum, not L. major — cross-species extrapolation is a hypothesis. 3. No antimonial comparator could be docked (Sb(V) polymer; active Sb(III) ion not representable in Vina). 4. Vina noise is ±1–2 kcal/mol; the 1.45 kcal/mol total spread across the five leads is not significant. 5. No molecular-dynamics refinement, binding-free-energy calculation, or re-docking validation of MWT was performed. 6. A single crystal structure (6T95, one TR conformation) was used; TR's dimer interface and active-site loop are flexible and induced-fit effects are not modelled. 7. All five leads are already-known TR inhibitors from one chemical series; no new chemical matter is proposed. 8. The pipeline's automated ChEMBL target selection and grid-centre selection both failed silently and required manual correction — other silent defaults in the same pipeline are not yet audited.

## 6. Conclusion

Five known triazolium TR inhibitors dock at −6.34 to −7.79 kcal/mol on L. infantum TR (PDB 6T95), but Vina cannot rank them: the most potent compound (CHEMBL5402846, Ki 200 nM) scores second, and the best docker (CHEMBL5414105, −7.79 kcal/mol) is the weakest by measured potency. The durable findings are the benchmark values themselves and the two pipeline faults caught before reporting — a human maltase-glucoamylase target attached to a parasite enzyme, and a grid centred on the FAD cofactor 18.33 Å from the inhibitor site. The next experiment is a head-to-head TR enzyme assay, not more docking.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author thanks the ChEMBL, UniProtKB, RCSB PDB and PubChem teams for free, open data.

## References

1. Médecins Sans Frontières. World NTDs Day: MSF calls for sustainable access to treatment for cutaneous leishmaniasis in Pakistan. 9 February 2026. https://www.msf.hk/en/latest/news-and-stories/news/world-ntds-day-msf-calls-for-sustainable-access-to-treatment-for-cutaneous-leishmaniasis-in-pakistan (accessed 5 November 2026).
2. Wyllie S, Cunningham ML, Fairlamb AH. Dual action of antimonial drugs on thiol redox metabolism in the human pathogen Leishmania donovani. *J Biol Chem.* 2004. https://www.jbc.org/article/S0021-9258(20)72801-2/fulltext (accessed 5 November 2026).
3. de Lucio H, Revuelto A, Carriles AA, de Castro S, Garcia-Gonzalez S, Garcia-Soriano JC, Alcon-Calderon M, Sanchez-Murcia PA, Hermoso JA, Gago F, Camarasa MJ, Jimenez-Ruiz A, Velazquez S. Identification of 1,2,3-triazolium salt-based inhibitors of Leishmania infantum trypanothione disulfide reductase with enhanced antileishmanial potency in cellulo and increased selectivity. *Eur J Med Chem.* 2022;244:114878. PMID: 36332553. doi:10.1016/j.ejmech.2022.114878.
4. Molecular basis of antimony treatment in leishmaniasis. Helmholtz-Zentrum Berlin, Structure of the Month, February 2010. https://www.helmholtz-berlin.de/forschung/oe/ps/macromolecular-crystallography/structures/structure-february2010_en.html (accessed 5 November 2026).
5. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model.* 2021;61(8):3891–3898. PMID: 34278794.
6. RCSB Protein Data Bank. Trypanothione reductase from Leishmania infantum in complex with 4a. PDB ID 6T95, 2.5 Å. https://www.rcsb.org/structure/6T95 (accessed 5 November 2026).
7. ChEMBL database, European Bioinformatics Institute. Target: trypanothione reductase, Leishmania infantum (CHEMBL1944501); bioactivities accessed 5 November 2026. https://www.ebi.ac.uk/chembl/.

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-052-2026-11-05.json` (discarded first run: UniProt Q4QJG7, wrong ChEMBL target CHEMBL2074 human maltase-glucoamylase, no PDB found), `hidden_files/dock-HP-052b-2026-11-05.json` (corrected pipeline run: UniProt A4HSF7, ChEMBL CHEMBL1944501, 26 ranked leads; docking at the FAD-cofactor centre retained for audit, QUERY sodium stibogluconate failed to prepare) and `hidden_files/dock-HP-052c-2026-11-05.json` (authoritative re-dock: PDB 6T95, 2.5 Å, MWT/4a centroid [24.84, −2.29, −69.97], desalted cations, Vina 1.2.7). ChEMBL IDs: CHEMBL5414105, CHEMBL5402846, CHEMBL5284653, CHEMBL5266073, CHEMBL5282990. PDB ID 6T95. No additional data were generated.
