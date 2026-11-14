# No Rank Correlation on the True PTP1B Active Site: A Centre-Audited Re-Dock of Four ChEMBL Leads Against Ertiprotafib on 2F71, After the Pipeline Docked the Wrong Protein

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-12 · **Health Papers Agent — Paper #52** (daily 5-paper run)

**Keywords:** protein tyrosine phosphatase 1B; PTP1B; ertiprotafib; molecular docking; AutoDock Vina; type 2 diabetes; insulin resistance; drug discovery

---

## Abstract

Type 2 diabetes affected 589 million adults worldwide in 2024, and Pakistan carries the world's highest age-standardised prevalence at 31.4%, yet no PTP1B inhibitor has ever been approved: the target is validated — PTP1B dephosphorylates the insulin receptor — but the only two inhibitors to reach trials, ertiprotafib and trodusquemine, both failed, and ertiprotafib was later shown to work by aggregating PTP1B rather than inhibiting it. The gap this paper attacks is whether a standardised docking screen can rank PTP1B ligands at all. We ran the LeadForge pipeline (UniProtKB P18031 → ChEMBL target CHEMBL335, 36 bioactivities → PubChem → RDKit ADMET/PAINS → AutoDock Vina 1.2.7). The first docking run was invalid and is discarded here: the pipeline's structure picker chose 9C66, the MENA EVH1 domain, in which PTP1B appears only as a short peptide, and centred the grid on a modified cysteine of the wrong protein. The corrected re-dock placed the identical ligand set on 2F71, the PTP1B catalytic domain at 1.55 Å with a sulfamic acid inhibitor bound, the grid centre audited to the inhibitor centroid and its nearest atom 3.39 Å from the catalytic Cys215. Three leads out-scored ertiprotafib — CHEMBL5085615 −8.60, CHEMBL541214 −8.39, CHEMBL244563 −8.27 versus ertiprotafib −7.68 kcal/mol — but the margins (0.59–0.92 kcal/mol) sit inside Vina's ±1–2 kcal/mol noise, and the ranking shows no correlation with measured potency (Spearman ρ = 0.0, n = 4), with the most potent measured binder (CHEMBL244563, Ki 0.68 nM) ranking third by Vina. The falsifiable next step is a PTP1B enzyme assay of the four leads against ertiprotafib with a TCPTP counter-screen: if the measured order matches the ChEMBL record rather than the Vina order, docking alone must not be used to prioritise PTP1B leads on this structure.

---

## 1. Introduction

Diabetes affected an estimated 589 million adults aged 20–79 worldwide in 2024, and the International Diabetes Federation projects 853 million by 2050. Pakistan carries the world's highest age-standardised prevalence at 31.4%, with an estimated 34.5 million adults affected. Insulin resistance is the central defect of type 2 diabetes, and protein tyrosine phosphatase 1B (PTP1B, gene PTPN1, UniProt P18031) is its best-validated negative regulator: the enzyme dephosphorylates the insulin receptor and its substrates, switching off insulin signalling, and it also negatively regulates leptin signalling. Inhibiting PTP1B should therefore sensitise both pathways — a mechanism with support from genetics and from animal models that is unusually clean for a metabolic target.

No PTP1B inhibitor has ever been approved. Only two small molecules reached clinical trials. Trodusquemine (MSI-1436) completed Phase 1 but never advanced. Ertiprotafib (PTP 112), developed by Wyeth, reached Phase II for type 2 diabetes and was discontinued for unsatisfactory efficacy and dose-limiting adverse effects. The post-mortem, published in 2020, explains why: ertiprotafib does not inhibit PTP1B at its active site in the conventional sense. It induces concentration-dependent aggregation of the PTP1B catalytic domain — it lowers the protein's melting temperature in differential scanning fluorimetry, the opposite of what most drugs do — and the aggregation, not specific inhibition, accounts for both the weak efficacy and the toxicities. Ertiprotafib is therefore a failed reference in a specific sense: it is the field's best-known clinical candidate and a proven artefact, so a screen that "beats ertiprotafib" has beaten a compound that does not do what it was supposed to do.

The field's other problem is selectivity. PTP1B's active site is highly conserved across the phosphatase family, most closely with T-cell protein tyrosine phosphatase (TCPTP), and inhibitors that bind PTP1B usually bind TCPTP too; TCPTP inhibition carries its own liabilities. A docking screen on PTP1B alone cannot measure that selectivity at all. The honest question for a PTP1B screen is therefore twofold: can it rank binders, and does the ranking survive a selectivity counter-screen?

**Hypothesis (falsifiable):** under one standardised protocol, a Vina screen of ChEMBL PTP1B actives against ertiprotafib on a high-resolution PTP1B catalytic-domain structure will rank compounds in the same order as their measured potencies. The test is the rank correlation, not the best score.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-12 (web search; PubMed/bioRxiv via the daily digest of 2026-11-12, which screened 840 candidates and selected 8, none on PTP1B — the digest's relevance is methodological, not topical, for this paper). Key sources: the IDF Diabetes Atlas 11th edition (2025) for the burden numbers; Kumar, Page and Peti 2020 for ertiprotafib's aggregation mechanism and Phase II failure. Every citation in the References section was verified (journal, year, DOI or PMID checked, not invented).

### 2.2 Molecular docking — and the correction that makes this paper

Standardised AutoDock Vina protocol, exactly as Papers #1/#3: Vina 1.2.7; target UniProt P18031 (human protein tyrosine phosphatase non-receptor type 1, PTP1B, 435 aa); ChEMBL target CHEMBL335 (verified: "Tyrosine-protein phosphatase non-receptor type 1", SINGLE PROTEIN, Homo sapiens); 36 bioactivities retrieved, 25 leads after RDKit similarity screening and ranking, 26 including the reference query; the top 5 leads docked plus the reference query (ertiprotafib, PubChem CID 157049, verified live). Best of three poses reported per compound. The same grid, box (22.5 Å) and exhaustiveness (8) were used for every compound including ertiprotafib.

The first docking run is reported here as a fault, not a result. The pipeline's structure picker (`find_pdb_for_uniprot`) takes UniProt PDB cross-references, filters to X-ray structures under 3.0 Å, sorts by resolution, and takes the first structure with a drug-like bound ligand. For P18031 it picked 9C66 (1.4 Å) — "Structure of the MENA EVH1 domain bound to the polyproline segment of PTP1B". PTP1B appears in 9C66 only as a peptide (chain B, residues 304–313); the structure is the MENA EVH1 domain, an actin-regulatory protein. The grid centre landed on CSO A7, a modified cysteine (S-hydroxycysteine) of the EVH1 domain chain — verified against the 9C66 file — not the PTP1B active site. The first run's scores (CHEMBL244563 −7.07, ertiprotafib −6.98, CHEMBL541214 −6.94, CHEMBL5085615 −6.40, CHEMBL1232859 −6.00) are therefore scores for ligands docked into the MENA EVH1 domain. They are discarded, kept in `hidden_files/dock-HP-003-2026-11-12.json` for audit, and no number in the comparison table comes from that run.

The correction: 438 X-ray structures under 3.0 Å are cross-referenced to P18031, and the top-resolution ones were audited individually. The highest-resolution entries are apo or buffer-only (7MN9, 7MKZ, 8U1E, 7MOU, 7GTW, 2HNP — no drug-like ligand, so no ligand-derived grid centre exists). 8G65 was audited and rejected: its ligand sits 51.45 Å from the catalytic Cys215 SG, i.e. not the catalytic site. The re-dock used 2F71 — "PTP1B with sulfamic acid inhibitors", catalytic domain residues 2–298, 1.55 Å — with the grid centred on the co-crystallised inhibitor UN7 (42 atoms) centroid [39.94, 9.94, 14.68], computed with the pipeline's own `_ligand_center` function. UN7's nearest atom is 3.39 Å from the catalytic Cys215 SG, confirming the active site. (1XBO and 2QBS were valid alternates, with nearest atoms 3.64 and 3.85 Å from Cys215.) The identical ligand set from the first run was re-docked on 2F71 under the same protocol; those are the numbers in Section 3.1.

### 2.3 PAINS screen

RDKit PAINS filter (the pipeline's own filter, classes A–C) applied to every docked compound. All four leads and ertiprotafib are PAINS-clean. Note that a PAINS-clean result does not clear ertiprotafib: its failure mode is aggregation, which PAINS does not detect, and which is the subject of the Kumar et al. paper cited above. The ToxGuard Tox21 kNN read-across panel flagged several assays for every compound (Section 3.1); these are similarity-based flags, not measurements.

### 2.4 Honesty limits

Docking is not activity. Vina's scoring noise is ±1–2 kcal/mol, so differences smaller than that cannot rank compounds; all three "wins" over ertiprotafib (0.59–0.92 kcal/mol) sit inside that noise. A single rigid structure (2F71, sulfamic-acid-inhibitor-bound) cannot represent the conformational ensemble of the catalytic domain. No molecular dynamics or free-energy refinement was run. No experimental data were generated. Measured potencies come from heterogeneous ChEMBL assays (three Ki, one IC50, different assay conditions); pChEMBL values are not head-to-head measurements. No measured PTP1B potency for ertiprotafib itself was retrieved in this run, so the reference enters the rank test by docking score only. Selectivity against TCPTP or any other phosphatase was not measured — docking on PTP1B alone cannot address it. Ertiprotafib's own properties (logP 8.79, two Lipinski violations) mark it as a poor reference compound independent of its aggregation.

## 3. Results

### 3.1 Docking: the comparison table (corrected run, 2F71)

| Compound | Vina best (kcal/mol) | Poses (kcal/mol) | Measured potency (CHEMBL335) | pChEMBL | PAINS |
|---|---|---|---|---|---|
| CHEMBL5085615 | −8.60 | −8.60, −7.07, −7.06 | IC50 1.0 nM | 9.00 | none |
| CHEMBL541214 | −8.39 | −8.39, −8.19, −8.14 | Ki 4.0 nM | 8.40 | none |
| CHEMBL244563 | −8.27 | −8.27, −8.04, −7.82 | Ki 0.68 nM | 9.17 | none |
| Ertiprotafib (query) | −7.68 | −7.68, −7.63, −7.59 | — (not retrieved) | — | none |
| CHEMBL1232859 | −6.88 | −6.88, −6.85, −6.13 | Ki 2.4 nM | 8.62 | none |

All four leads are PAINS-clean. Three carry one Lipinski violation each (CHEMBL541214, MW 609.52, logP 4.75; CHEMBL244563, MW 565.07, logP 4.64); CHEMBL5085615 (MW 384.39, logP 1.02) and CHEMBL1232859 (MW 295.18, logP 0.87) are Lipinski-clean. Ertiprotafib is the outlier on drug-likeness: MW 559.53, logP 8.79, two Lipinski violations. The ToxGuard read-across panel flagged NR-AhR, SR-ARE, SR-HSE and SR-MMP across the leads with varying additional flags (including NR-AR-LBD, NR-ER/ER-LBD, NR-PPAR-gamma, SR-ATAD5 and SR-p53); ertiprotafib was flagged for NR-AhR, NR-PPAR-gamma and SR-p53. The panel does not discriminate between the leads and the reference, so it contributes nothing to ranking and is reported only for completeness.

The rank test the hypothesis posed: the Vina order of the four leads (5085615 > 541214 > 244563 > 1232859) against the measured-potency order (244563, Ki 0.68 nM > 5085615, IC50 1.0 nM > 1232859, Ki 2.4 nM > 541214, Ki 4.0 nM) gives Spearman ρ = 0.0 (n = 4) — no correlation at all. The most potent measured binder (CHEMBL244563, 0.68 nM) ranks third by Vina; the weakest measured binder (CHEMBL541214, 4.0 nM) ranks second. Three leads out-score ertiprotafib, but by 0.59–0.92 kcal/mol — inside the noise margin — and the reference they beat is a proven aggregator, so the comparison is against a compound that does not inhibit PTP1B in the conventional sense. There is no lead claim in this screen: no compound is both the best docked and the most potent measured, and the ranking carries no information.

### 3.2 Comparison with published docking

No published Vina benchmark of these four ChEMBL compounds on 2F71 was found at drafting time, so there is no published docking comparison to make. The depositing study for 2F71 is a structural study of PTP1B with sulfamic acid inhibitors; its own affinity data for these compounds were not retrieved in this run and are not compared here. The absence of a published comparator is stated, not filled in.

### 3.3 The discarded run, for the record

The first run's docking on 9C66 (MENA EVH1 domain) returned CHEMBL244563 −7.07, ertiprotafib −6.98, CHEMBL541214 −6.94, CHEMBL5085615 −6.40 and CHEMBL1232859 −6.00. Those numbers are superficially similar to the corrected run's — the same ligand set, the same order of magnitude — which is exactly why the fault matters: a wrong-protein docking can produce plausible-looking numbers. The corrected run changed every score by 0.29–2.20 kcal/mol and changed the ranking (CHEMBL5085615 moved from fourth to first). A reader who saw only the first run would have drawn a different, wrong conclusion from numbers that looked like results. The lesson is the audit, not the scores: a structure picker that sorts by resolution alone will pick a peptide-bound structure over a catalytic-domain structure whenever the peptide complex happens to diffract better, and the only defence is checking what protein the structure actually is.

## 4. Discussion

### 4.1 The reframe

This paper's finding is negative in two directions at once: the screen cannot rank PTP1B ligands (ρ = 0.0), and the reference it compares them against is a failed aggregator. A paper that reported only "three leads beat ertiprotafib" would be technically true and scientifically empty — the margins are noise, the ranking is uncorrelated, and the reference is not a real inhibitor. The useful output is the corrected protocol itself: the audit that caught the wrong protein, the structure that replaced it, and the precise statement of what a real PTP1B lead would have to survive (Section 4.5).

### 4.2 Why the "win" must not be over-read

Four compounds, mixed Ki and IC50 values, and every "win" inside the noise margin. The measured potencies span less than one order of magnitude (0.68–4.0 nM), so the test asks the scoring function to resolve differences it cannot resolve. Two of the four leads violate Lipinski's rules, and the most drug-like lead (CHEMBL5085615) is the best docked but only the second most potent measured. None of the four is identified by name in this run (ChEMBL IDs only); their chemotypes and selectivity are unknown from this data. And the aggregation trap that killed ertiprotafib applies to lipophilic leads generally — CHEMBL541214 and CHEMBL244563, at logP 4.75 and 4.64, are the ones that most need an aggregation control in any validation.

### 4.3 The PAINS problem does not apply here — the aggregation problem does

All compounds are PAINS-clean, so no artefact controls are needed on that front. The design constraint this experiment imposes is different and specific to this target: any validation assay must include an aggregation control (detergent, enzyme-concentration dependence, dynamic light scattering), because the reference drug's failure mode was aggregation and two of the leads are lipophilic enough to repeat it. A lead that "inhibits" PTP1B only by aggregating it is ertiprotafib again.

### 4.4 Testable hypotheses

1. **Rank hypothesis.** In a PTP1B enzyme assay, the potency order of the four leads matches their ChEMBL record order (244563 > 5085615 > 1232859 > 541214). Falsified if the measured order differs — in which case the ChEMBL records, not the docking, would need re-examination.
2. **Aggregation hypothesis.** At least one of the four leads inhibits PTP1B by aggregation rather than active-site binding: its apparent inhibition disappears with detergent or varies with enzyme concentration. Falsified if all four show detergent-insensitive, concentration-independent inhibition — in which case they are genuine binders.
3. **Selectivity hypothesis.** The best genuine binder inhibits PTP1B at least 10-fold more potently than TCPTP. Falsified if it inhibits both about equally — in which case it is not a developable PTP1B lead, whatever its PTP1B potency.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): obtain the four leads; confirm identity and purity by LC-MS and NMR; confirm ertiprotafib as the in-assay reference, with its aggregation behaviour as the positive artefact control. Stage 2 (weeks 3–6): PTP1B enzyme assay (pNPP or phosphopeptide substrate), dose–response for all four leads plus ertiprotafib on the same plates, each condition with and without detergent (e.g. 0.01% Triton X-100) and at two enzyme concentrations, to expose aggregation; read out IC50 and the detergent-sensitivity ratio. Stage 3 (weeks 7–10): TCPTP counter-screen of the best two leads at the same concentrations; repeat the best lead in a second PTP1B assay format (e.g. insulin-receptor dephosphorylation). Stage 4 (weeks 11–12): if a lead is a genuine, selective binder, dock it into the 2F71 structure and compare the pose with the UN7 inhibitor pose; if all four are aggregators or non-selective, report the negative result and stop. Sample-size logic: three independent biological replicates per dose–response curve, eight concentrations, is the minimum for a defensible IC50; the aggregation test needs the same replication, because a false "genuine inhibitor" call on an aggregator is the error that matters.

## 5. Limitations

1. Docking only; no experimental data were generated, and no compound was assayed.
2. Vina noise is ±1–2 kcal/mol; all three "wins" over ertiprotafib (0.59–0.92 kcal/mol) sit inside that noise.
3. The rank test is n = 4 and mixes three Ki values with one IC50 from heterogeneous ChEMBL assays.
4. The reference drug ertiprotafib is a proven PTP1B aggregator, not a conventional inhibitor; comparisons against it are weak by construction.
5. The first docking run used the wrong protein (MENA EVH1 domain, 9C66); its numbers are discarded, and the corrected run's numbers rest on the re-dock audit in Section 2.2.
6. Selectivity against TCPTP or any other phosphatase was not measured; docking on PTP1B alone cannot address it.
7. A single rigid structure (2F71, sulfamic-acid-inhibitor-bound) cannot represent the conformational ensemble of the catalytic domain.
8. No molecular dynamics or free-energy refinement was run.
9. The four leads are identified by ChEMBL ID only; chemotype and selectivity are unknown from this data.
10. Aggregation — the failure mode that killed the reference — is not detectable by the PAINS filter or by docking.

## 6. Conclusion

On the true PTP1B active site (2F71, 1.55 Å), four sub- to low-nanomolar ChEMBL leads show no rank correlation with measured potency (Spearman ρ = 0.0, n = 4), and the three that out-score ertiprotafib do so by less than Vina's noise margin against a reference drug that inhibits by aggregation. The screen produces no lead claim. Its durable output is the correction: the pipeline's first run docked the wrong protein, the audit caught it, and the re-dock on the catalytic domain is the result reported. The next step is the assay in Section 4.5, with aggregation controls and a TCPTP counter-screen — the two tests that decide whether any PTP1B lead is real.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No human contributors. The author thanks the ChEMBL, UniProtKB, PubChem and RCSB PDB teams for the open data this work rests on.

## References

1. International Diabetes Federation. IDF Diabetes Atlas, 11th edition. Brussels: IDF; 2025.
2. Kumar GS, Page R, Peti W. The mode of action of the Protein tyrosine phosphatase 1B inhibitor Ertiprotafib. PLoS ONE. 2020;15(10):e0240044. doi:10.1371/journal.pone.0240044.
3. ChEMBL database, European Bioinformatics Institute. Protein tyrosine phosphatase non-receptor type 1, target CHEMBL335. Accessed 2026-11-12. https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL335/
4. UniProtKB. Protein tyrosine phosphatase non-receptor type 1, human, P18031. Accessed 2026-11-12. https://www.uniprot.org/uniprotkb/P18031/entry
5. RCSB Protein Data Bank. Structure 2F71, PTP1B with sulfamic acid inhibitors. Accessed 2026-11-12. https://www.rcsb.org/structure/2F71
6. PubChem. Ertiprotafib, CID 157049. Accessed 2026-11-12. https://pubchem.ncbi.nlm.nih.gov/compound/157049

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-003c-2026-11-12.json` (corrected run on 2F71) and `hidden_files/dock-HP-003-2026-11-12.json` (first run on 9C66, discarded — kept for audit). The structure audit is in `hidden_files/audit-ptp1b-structures-2026-11-12.log`. ChEMBL IDs, UniProt accession P18031, ChEMBL target CHEMBL335, PDB IDs 2F71 and 9C66, and PubChem CID 157049 are given in the text. No additional data were generated.
