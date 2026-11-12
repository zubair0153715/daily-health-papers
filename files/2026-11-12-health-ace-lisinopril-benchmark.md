# Vina Ranks Lisinopril Last on ACE: A Centre-Audited Benchmark of Enalaprilat and Two ChEMBL Leads Against Lisinopril on the C-Domain Structure 6H5W

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-12 · **Health Papers Agent — Paper #50** (daily 5-paper run)

**Keywords:** angiotensin-converting enzyme; lisinopril; enalaprilat; molecular docking; AutoDock Vina; hypertension; ACE inhibitor cough; bradykinin

---

## Abstract

Hypertension affected 1.4 billion people in 2024 and only about one in five had it controlled, yet the most prescribed drug class for it — ACE inhibitors — makes 5–15% of patients cough, because the same enzyme that converts angiotensin I also degrades bradykinin, and blocking it lets bradykinin accumulate in the airways. The gap this paper attacks is whether a standardised docking screen can find a better ACE binder than lisinopril, and whether that question is even the right one for a cough-free drug. We ran the LeadForge pipeline (UniProtKB P12821 → ChEMBL target CHEMBL1808, 45 bioactivities → PubChem → RDKit ADMET/PAINS → AutoDock Vina 1.2.7) and docked four ChEMBL ACE actives plus lisinopril into the 1.37 Å ACE C-domain structure 6H5W, with the grid centre audited to 0.005 Å from the co-crystallised inhibitor omapatrilat. All four leads out-scored lisinopril — CHEMBL80779 −8.86, enalaprilat −8.15 and −8.05 (duplicate ChEMBL records of one molecule), lisinopril's own ChEMBL record −7.88, against the PubChem lisinopril query at −7.62 kcal/mol — but the ranking is inverted against measured potency: lisinopril itself, the most potent measured binder at IC50 0.1 nM, docks worst, Spearman ρ = −0.5 on the three distinct molecules. Two reproducibility controls held: lisinopril docked twice 0.26 kcal/mol apart and enalaprilat twice 0.10 apart. The cough question is not answered by binding at all: bradykinin is cleaved by both ACE domains while angiotensin I is mainly cleaved by the C-domain, so a cough-sparing inhibitor must be C-domain-selective, which a single-domain docking score cannot measure. The falsifiable next step is a two-domain (N versus C) inhibition assay of the leads against lisinopril: if a lead inhibits the C-domain while sparing the N-domain, it is a candidate for the cough question; if it inhibits both like lisinopril, it is not, whatever its docking score.

---

## 1. Introduction

The World Health Organization's Global Hypertension Report 2025 put the number of people living with hypertension at 1.4 billion in 2024, with only about one in five having the condition under control, and uncontrolled high blood pressure claiming more than 10 million lives a year. ACE inhibitors are a first-line treatment, and lisinopril is among the most prescribed of them. Their efficacy is not the problem. Their tolerability is: a persistent dry cough that affects roughly 5–15% of patients on ACE inhibitors (with some studies reporting up to 35%), more often in women than in men (12.6% versus 4.4% in one lisinopril study), typically beginning weeks to months after starting treatment and resolving only 1–4 weeks after stopping the drug. It is the most common reason physicians switch a patient from an ACE inhibitor to an angiotensin-receptor blocker.

The mechanism is inseparable from the drug's action. ACE — kininase II — has two jobs: it converts angiotensin I to the vasoconstrictor angiotensin II, and it degrades bradykinin, a vasodilator peptide. Inhibiting the enzyme therefore does two things at once: blood pressure falls, and bradykinin (with substance P, which ACE also degrades) accumulates in the airways, sensitising the cough reflex. The cough is not an allergy and not an off-target effect; it is the on-target consequence of blocking bradykinin breakdown. Any ACE inhibitor that blocks the enzyme will raise bradykinin to some degree, which is why the "cough-free ACE inhibitor" is a harder problem than "a stronger ACE binder".

The one opening is that ACE is not one active site but two. Somatic ACE is a single polypeptide with two homologous catalytic domains, N and C, each with a zinc-containing active site, sharing about 55–60% sequence identity but with different substrate specificities. The C-domain is mainly responsible for converting angiotensin I in vivo; bradykinin is hydrolysed by both domains about equally; and several substrates, including the tetrapeptide AcSDKP, are cleaved essentially only by the N-domain. A C-domain-selective inhibitor would therefore lower angiotensin II while leaving the N-domain free to keep degrading bradykinin — the published rationale for pursuing domain-selective inhibitors as drugs with an improved side-effect profile. That is the precise question a docking screen must be judged against: not "does it bind ACE better than lisinopril?" but "does it bind the C-domain selectively?"

**Hypothesis (falsifiable):** under one standardised protocol, a Vina screen of ChEMBL ACE actives against lisinopril on a high-resolution ACE C-domain structure will rank compounds in the same order as their measured potencies, and the top-ranked lead will be a candidate for C-domain-selective inhibition. The test is the rank correlation, not the best score — and selectivity must be tested in a two-domain assay, not inferred from a single-domain docking score.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-12 (web search; PubMed/bioRxiv via the daily digest of 2026-11-12, which screened 840 candidates and selected 8, none on ACE — the digest's relevance is methodological, not topical, for this paper). Key sources: the WHO Global Hypertension Report 2025 for the burden numbers; Yilmaz 2019 for ACE-inhibitor cough incidence and mechanism; Taddei and Bortolotto 2016 for the bradykinin mechanism; Ehlers, Abrie and Sturrock 2013 for C-domain-selective inhibition. Every citation in the References section was verified (journal, year, DOI checked, not invented).

### 2.2 Molecular docking

Standardised AutoDock Vina protocol, exactly as Papers #1/#3: Vina 1.2.7; target UniProt P12821 (human angiotensin-converting enzyme, ACE, 1,306 aa); ChEMBL target CHEMBL1808 (verified: "Angiotensin-converting enzyme", SINGLE PROTEIN, Homo sapiens); 45 bioactivities retrieved, 25 leads after RDKit similarity screening and ranking, 26 including the reference query; the top 5 leads docked plus the reference query (lisinopril, PubChem CID 5362119, verified live). Structure: PDB 6H5W, the human ACE C-domain in complex with omapatrilat, resolution 1.37 Å. Grid centre [−6.89, 3.74, 14.52] — audited against the co-crystallised ligand omapatrilat (residue FT8, chain A, residue 711) centroid computed from the deposited coordinates with the pipeline's own `_ligand_center` function: distance 0.005 Å, i.e. the grid is exactly on the C-domain active site, at the catalytic zinc. Best of three poses reported per compound. The same grid, box (22.5 Å) and exhaustiveness (8) were used for every compound including lisinopril.

Two bookkeeping facts about the lead set, disclosed here because they change how the table reads. First, the ChEMBL record CHEMBL1237 is lisinopril itself: its SMILES has the same connectivity as the PubChem query SMILES, with stereochemistry specified, and identical descriptors (MW 405.5, logP 1.24). It was therefore docked twice — once as a lead, once as the query — which makes it a reproducibility control, not a second molecule. Second, CHEMBL577 and CHEMBL39538 are duplicate ChEMBL records of one molecule, enalaprilat: their SMILES differ only in stereochemistry specification, their descriptors are identical (MW 348.4, logP 1.13), and their measured potencies are the same within rounding (IC50 1.2 versus 1.202 nM). The comparison table therefore contains five entries but three distinct molecules, and the rank test is computed on the three distinct molecules.

Only the C-domain was docked. No N-domain structure was used, so nothing in this paper measures domain selectivity; the C-domain-selective question is posed, not tested.

### 2.3 PAINS screen

RDKit PAINS filter (the pipeline's own filter, classes A–C) applied to every docked compound. All five entries are PAINS-clean. The ToxGuard Tox21 kNN read-across panel was clean for lisinopril (measured data, no active assays) and for both enalaprilat records; CHEMBL80779 carries a single read-across flag (NR-AhR). A read-across flag is a similarity-based screen result, not a toxicity measurement, and it is reported as such.

### 2.4 Honesty limits

Docking is not activity, and a docking score on one domain cannot measure domain selectivity, which is the entire question this paper asks about cough. Vina's scoring noise is ±1–2 kcal/mol, so differences smaller than that cannot rank compounds; the 1.24 kcal/mol gap between the best lead and lisinopril sits inside that noise. A single rigid structure (6H5W, omapatrilat-bound C-domain) cannot represent the conformational ensemble of either ACE domain, and omapatrilat is a dual ACE/neprilysin inhibitor, not lisinopril, so the pocket conformation is not the lisinopril-bound one. No molecular dynamics or free-energy refinement was run. No experimental data were generated. Measured potencies come from heterogeneous ChEMBL assays (IC50 values from different assay conditions); pChEMBL values are not head-to-head measurements. No measured ACE potency for the PubChem lisinopril query was retrieved in this run; the reference enters the rank test through its ChEMBL record (CHEMBL1237, IC50 0.1 nM).

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Vina best (kcal/mol) | Poses (kcal/mol) | Measured potency (CHEMBL1808) | pChEMBL | PAINS |
|---|---|---|---|---|---|
| CHEMBL80779 | −8.86 | −8.86, −8.83, −8.65 | IC50 1.096 nM | 8.96 | none |
| CHEMBL577 (enalaprilat, record A) | −8.15 | −8.15, −7.76, −7.69 | IC50 1.2 nM | 8.92 | none |
| CHEMBL39538 (enalaprilat, record B) | −8.05 | −8.05, −8.02, −7.89 | IC50 1.202 nM | 8.92 | none |
| CHEMBL1237 (lisinopril, ChEMBL record) | −7.88 | −7.88, −7.71, −7.50 | IC50 0.1 nM | 10.00 | none |
| Lisinopril (query, PubChem) | −7.62 | −7.62, −7.23, −7.18 | — (not retrieved) | — | none |

All five entries are small (MW 348–406), Lipinski-clean (0 violations), with 3–4 hydrogen-bond donors and 4–5 acceptors. The reproducibility controls held: the two lisinopril dockings differ by 0.26 kcal/mol (−7.88 versus −7.62) and the two enalaprilat dockings by 0.10 kcal/mol (−8.15 versus −8.05), both well inside Vina's noise and consistent with the same molecule being placed twice. These are the tightest reproducibility controls in this paper series, and they make the ranking result harder to dismiss as setup error: the protocol is reproducible, and it reproducibly ranks the most potent binder last.

The rank test the hypothesis posed: on the three distinct molecules, the Vina order is CHEMBL80779 > enalaprilat > lisinopril, while the measured-potency order is lisinopril (0.1 nM) > CHEMBL80779 (1.096 nM) > enalaprilat (1.2 nM) — the Vina order is the exact reverse of the measured order for the top and bottom, Spearman ρ = −0.5 (n = 3). Every lead out-scores lisinopril (by 0.26–1.24 kcal/mol against the query), yet lisinopril is the most potent measured binder by a factor of eleven over the next compound. The "win" is therefore an artefact of the scoring function, not a lead: a screen that ranks a 0.1 nM binder below 1.2 nM binders cannot be used to prioritise ACE inhibitors on this structure.

### 3.2 Comparison with published docking

No published Vina benchmark of these ChEMBL compounds on 6H5W was found at drafting time, so there is no published docking comparison to make. The depositing study for 6H5W is a structural study of the ACE C-domain with omapatrilat; its own docking or affinity data for these compounds were not retrieved in this run and are not compared here. The absence of a published comparator is stated, not filled in.

### 3.3 The cough question is not a binding question

The screen's headline — four leads out-score lisinopril — is irrelevant to the cough problem for two independent reasons. First, the ranking is inverted against measured potency (Section 3.1), so the scores do not identify better binders. Second, and more fundamentally, cough is caused by bradykinin accumulation, and bradykinin is hydrolysed by both ACE domains about equally. A compound that binds the C-domain more tightly than lisinopril but inhibits the N-domain equally will raise bradykinin exactly as lisinopril does. The only escape is domain selectivity: inhibit the C-domain (which makes the angiotensin II that raises blood pressure) while sparing the N-domain (which keeps clearing bradykinin). This screen docked on the C-domain only, so it cannot distinguish a C-selective inhibitor from a non-selective one — the property that matters is precisely the one that was not measured. The paper's topic as posed ("cough-free alternatives") therefore cannot be answered by this screen; it can only be answered by a two-domain assay, proposed in Section 4.5.

## 4. Discussion

### 4.1 The reframe

The paper started as a search for a better ACE binder and became a demonstration that "better binder" is the wrong target twice over: the screen cannot rank binders correctly on this structure, and binding is not the property that causes or prevents cough. The useful result is the negative one — Vina on 6H5W ranks lisinopril last while it is the most potent measured binder — plus the precise statement of what would count as progress, which is a domain-selectivity measurement, not a docking score.

### 4.2 Why the "win" must not be over-read

Three distinct molecules is the smallest rank test this series has run, and the 1.24 kcal/mol gap between the best lead and lisinopril is inside Vina's ±1–2 kcal/mol noise. The measured potencies span only one order of magnitude (0.1–1.2 nM), so the test asks the scoring function to resolve differences it cannot resolve. CHEMBL80779, the top scorer, is identified by ChEMBL ID only; its chemotype and identity were not established in this run. And all four leads are already potent ACE inhibitors by their ChEMBL records — this is a screen among known nanomolar binders, not a discovery screen.

### 4.3 The PAINS problem does not apply here

All compounds are PAINS-clean, so no artefact controls are needed on that front. The design constraint this experiment imposes is different: any validation must measure both ACE domains, because a single-domain result cannot speak to the cough question, and it must include lisinopril on the same plates, because the docking comparison against it is inverted.

### 4.4 Testable hypotheses

1. **Rank hypothesis.** In a single-domain ACE inhibition assay, the potency order of the three distinct molecules matches their ChEMBL record order (lisinopril > CHEMBL80779 > enalaprilat), not the Vina order. Falsified if the measured order matches Vina — in which case the ChEMBL records, not the docking, are the problem.
2. **Selectivity hypothesis.** CHEMBL80779 inhibits the ACE C-domain more potently than the N-domain (selectivity ratio ≥ 10), while lisinopril inhibits both about equally. Falsified if CHEMBL80779 is non-selective — in which case it is not a cough-sparing candidate, whatever its docking score.
3. **Cough hypothesis.** A C-domain-selective inhibitor lowers blood pressure in vivo with less bradykinin accumulation than lisinopril at equi-effective doses. This is a later, animal-stage test; it is stated here so the assay in Section 4.5 is designed toward it, not as a claim this paper can test.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): obtain CHEMBL80779 and enalaprilat; confirm identity and purity by LC-MS and NMR; confirm lisinopril as the in-assay reference. Stage 2 (weeks 3–6): in vitro ACE inhibition assays on recombinant N-domain and C-domain separately (fluorogenic substrate, e.g. Abz-based), dose–response for all three distinct molecules plus lisinopril on the same plates, with domain-selective controls (RXP407 for the N-domain, RXPA380 for the C-domain, from the literature) and a vehicle control; read out IC50 per domain and the C/N selectivity ratio. Stage 3 (weeks 7–10): bradykinin-degradation assay in the same domain preparations, to test directly whether a C-selective lead spares bradykinin breakdown. Stage 4 (weeks 11–12): if a lead is C-selective, dock it into an N-domain structure and compare the poses to identify the selectivity determinants; if none is selective, report the negative result and stop. Sample-size logic: three independent biological replicates per dose–response curve, eight concentrations, is the minimum for a defensible IC50 and selectivity ratio; the bradykinin assay needs the same, because a false "sparing" call is the error that matters.

## 5. Limitations

1. Docking only; no experimental data were generated, and no compound was assayed.
2. Vina noise is ±1–2 kcal/mol; the 1.24 kcal/mol gap between the best lead and lisinopril cannot rank them.
3. The rank test is n = 3 distinct molecules, with measured potencies spanning only one order of magnitude (0.1–1.2 nM).
4. The lead set contains duplicate ChEMBL records (two of lisinopril, two of enalaprilat); the table has five entries but three distinct molecules.
5. Only the C-domain was docked; domain selectivity — the property the cough question turns on — was not measured.
6. A single rigid structure (6H5W, omapatrilat-bound C-domain) cannot represent the conformational ensemble of either ACE domain.
7. No molecular dynamics or free-energy refinement was run.
8. Measured potencies come from heterogeneous ChEMBL assays; pChEMBL values are not head-to-head measurements.
9. CHEMBL80779 is identified by ChEMBL ID only; its chemotype and identity were not established in this run.
10. The cough mechanism (bradykinin accumulation) is literature-based; this paper measures no cough endpoint.

## 6. Conclusion

Four ChEMBL ACE actives out-score lisinopril on the 1.37 Å C-domain structure 6H5W, but the ranking is inverted against measured potency (Spearman ρ = −0.5, n = 3 distinct molecules): lisinopril, the most potent measured binder at IC50 0.1 nM, docks worst. The screen is reproducible — lisinopril and enalaprilat each docked twice within 0.26 kcal/mol — and reproducibly wrong about the ranking. Separately, the cough question cannot be answered by binding at all: bradykinin is cleared by both ACE domains, so only a C-domain-selective inhibitor can spare it, and this screen measured no selectivity. The next step is the two-domain assay in Section 4.5.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No human contributors. The author thanks the ChEMBL, UniProtKB, PubChem and RCSB PDB teams for the open data this work rests on.

## References

1. World Health Organization. Global Hypertension Report 2025. Geneva: WHO; 2025.
2. Yilmaz I. Angiotensin-converting enzyme inhibitors induce cough. Turk Thorac J. 2019;20(1):36–42. doi:10.5152/TurkThoracJ.2018.18014.
3. Taddei S, Bortolotto L. Unraveling the pivotal role of bradykinin in ACE inhibitor activity. Am J Cardiovasc Drugs. 2016;16(5):309–321. doi:10.1007/s40256-016-0173-4.
4. Ehlers MR, Abrie JA, Sturrock ED. C domain-selective inhibition of angiotensin-converting enzyme. J Renin Angiotensin Aldosterone Syst. 2013. doi:10.1177/1470320313489206.
5. ChEMBL database, European Bioinformatics Institute. Angiotensin-converting enzyme, target CHEMBL1808. Accessed 2026-11-12. https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1808/
6. UniProtKB. Angiotensin-converting enzyme, human, P12821. Accessed 2026-11-12. https://www.uniprot.org/uniprotkb/P12821/entry
7. RCSB Protein Data Bank. Structure 6H5W, human ACE C-domain in complex with omapatrilat. Accessed 2026-11-12. https://www.rcsb.org/structure/6H5W
8. PubChem. Lisinopril, CID 5362119. Accessed 2026-11-12. https://pubchem.ncbi.nlm.nih.gov/compound/5362119

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-042-2026-11-12.json`. ChEMBL IDs, UniProt accession P12821, ChEMBL target CHEMBL1808, PDB ID 6H5W and PubChem CID 5362119 are given in the text. No additional data were generated.
