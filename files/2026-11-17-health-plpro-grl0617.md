# Rigid Docking Cannot Rank the GRL0617 Series on SARS-CoV-2 PLpro: the 2.67 µM Reference Scores Best and the 42 µM Compound Beats Both Leads

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-17 · **Health Papers Agent — Paper #72** (daily 5-paper run)
**Topic ID:** HP-073

**Keywords:** SARS-CoV-2; papain-like protease; PLpro; GRL0617; molecular docking; AutoDock Vina; BL2 loop; antiviral drug discovery

---

## Abstract

SARS-CoV-2 papain-like protease (PLpro) cleaves the viral polyprotein and strips ubiquitin and ISG15 from host proteins, suppressing type-I interferon — a second viral protease with no approved inhibitor, unlike the main protease (Mpro), which has nirmatrelvir. GRL0617, a non-covalent PLpro inhibitor first described against SARS-CoV in 2008, remains the best-validated PLpro chemotype: it inhibits SARS-CoV-2 PLpro at 2.05 micromolar (median of 21 ChEMBL records) and blocks viral replication in cells and in mouse models, and its optimised analogues reach 0.11–0.67 micromolar. We benchmarked rigid AutoDock Vina docking on the GRL0617-bound structure 7JRN (2.48 angstrom) against five compounds from a single FRET assay (Ma et al. 2021): GRL0617 (2.67 micromolar in this assay) plus four analogues spanning 0.11–42 micromolar. The re-dock control worked — GRL0617 scored −9.90 kcal/mol in its own pocket — but the ranking failed: Spearman rho = +0.15 (n = 5). The weakest compound (42 micromolar) scored third-best (−9.14), beating both named leads Jun9-72-2 (−7.74) and Jun9-84-3 (−8.21), while the most potent analogue (0.11 micromolar) scored second (−9.74). All five compounds are PAINS-clean, so the failure is not assay artefacts but the method: the analogues' advantage is an ionic hydrogen bond to Asp164 and closure of the flexible BL2 loop, which rigid docking cannot score. Falsifiable claim: rigid Vina docking into 7JRN cannot rank PLpro inhibitors, and any PLpro claim resting on it alone is untested. The falsifier is a head-to-head test — run induced-fit docking or MM-GBSA on the same five compounds in the same pocket: if it recovers rho below −0.5 where rigid Vina gives +0.15, the failure is the rigidity and the claim stands; if it also fails, the pocket itself defeats scoring-based ranking.

---

## 1. Introduction

COVID-19 has caused nearly 780 million confirmed cases and more than 7.1 million reported deaths worldwide (WHO COVID-19 fact sheet, accessed November 2026), including about 1.58 million confirmed cases and 30,656 deaths in Pakistan (National Institute of Health, Pakistan, 2023). The virus still circulates, and the antiviral cupboard holds exactly one oral drug class: nirmatrelvir, which inhibits the main protease (Mpro, nsp5). The second viral protease has been left behind.

Papain-like protease (PLpro) is the nsp3 protease domain (replicase polyprotein 1ab residues 1564–1878; nsp3 residues 746–1060; EC 3.4.19.12; UniProt P0DTD1). It cuts the three N-terminal junctions of the replicase polyprotein, and it is also a deubiquitinase and deISGylase: it strips ubiquitin and ISG15 from host proteins, which shuts down type-I interferon signalling and lets the virus spread while the innate immune response is blind (Shin et al. 2020). A PLpro inhibitor is therefore two drugs in one — an antiviral and an immune-restoring agent — and that is why PLpro, not Mpro, is the underexploited target. It has no approved drug and no drug in late-stage trials.

GRL0617 is the reference compound for this target. Discovered against SARS-CoV PLpro in 2008 (IC50 0.6 µM; Ratia et al. 2008), it was repurposed for SARS-CoV-2, where it inhibits PLpro at 2.05 µM (median of 21 ChEMBL IC50 records, range 0.6–7.0 µM; 2.05 ± 0.12 µM in the Ma et al. 2021 FRET assay) and shows antiviral activity in Vero E6 cells (EC50 23.64 µM) and in Caco-2-hACE2 cells (19.96 µM). Structure-based optimisation from the GRL0617-bound structure produced the Jun9 series, with Jun9-75-4 (0.62 µM), Jun9-72-2 (0.67 µM) and Jun9-84-3 (0.67 µM) roughly threefold more potent than GRL0617 and threefold more active antivirally (EC50 6.6–8.3 µM; Ma et al. 2021). A 2025 invalidation study confirmed the field's central fact: most reported PLpro inhibitors act unspecifically (thiol-reactive or redox-active), and "GRL0617 and its derivatives remain the best-validated compounds with demonstrated antiviral activity in cells and in mouse models" (Kuzikov et al. 2025).

The companion paper in this series (HP-037) benchmarked the same rigid-docking method on Mpro and got the first positive rank correlation in the series (Spearman ρ = +0.48, n = 5): the most potent nirmatrelvir analogue scored best. This paper asks whether the same method works on the second protease, using the same protocol, the same reference-drug logic, and a cleaner test — five compounds from one assay, one paper, spanning 372-fold in potency.

**Falsifiable question (stated before the results):** can rigid AutoDock Vina docking into the GRL0617-bound PLpro structure 7JRN rank five GRL0617-series inhibitors in the order of their measured IC50 values? The claim is that it cannot, because the analogues' potency gain comes from an ionic interaction and a loop closure that a rigid receptor cannot represent. The claim is refuted if the docking scores rank the compounds in measured order (ρ ≤ −0.5), and confirmed in its strongest form if the ranking is inverted (ρ ≥ +0.5).

## 2. Methods

### 2.1 Literature basis

PubMed (E-utilities, accessed 17 November 2026) for GRL0617 + PLpro (65 hits), cross-checked against the ChEMBL bioactivity record and the full text of Ma et al. 2021 (PMC8265724) and Shin et al. 2020 (PMC7116779). Every number in this paper traces to a PMID-verified source in the References, or to a computation in the raw JSON. The Islamic canon check is in §2.7. The analysis plan — target, structure, docking set, and the Spearman test — was fixed before any docking score was seen; nothing in the Results is post-hoc except the mechanistic reading of the failure, which is labelled as such.

### 2.2 Target verification, and the discarded wrong-target run

PLpro was resolved by accession, not by text search: UniProt P0DTD1 (Replicase polyprotein 1ab, SARS-CoV-2, 7,096 aa); the PLpro (nsp3) domain is pp1ab residues 1564–1878, catalytic Cys111 (pp1ab Cys1674) and His272 (pp1ab His1835). The only ChEMBL target carrying component accession P0DTD1 as a single protein is CHEMBL4523582 (Replicase polyprotein 1ab). That target also holds Mpro activities, so PLpro potencies were filtered by assay description (contains "papain" or "PLpro"): 699 PLpro IC50 activities from 561 distinct molecules (ChEMBL, accessed 17 November 2026).

The standard pipeline run (`run_docking.py --target "SARS-CoV-2 papain-like protease" --ref GRL0617`) failed exactly as the series has seen before: its ChEMBL text search returned CHEMBL2074 (human maltase-glucoamylase) first, resolved UniProt to P0DTC1 (replicase polyprotein 1a), and docked 26 maltase ligands into 8AZC (the NSP3 macrodomain) with every dock failing. That run is discarded in full and preserved as `dock-HP-073-2026-11-17-WRONG-TARGET.json`. It is the paper's first finding, again: a text-search fallback manufactures a complete, plausible-looking, entirely wrong result, and only the accession check catches it.

### 2.3 Structure and centre audit

PDB 7JRN: wild-type SARS-CoV-2 PLpro in complex with GRL0617, 2.48 Å, X-ray (Ma et al. 2021, PMID 34341772). The docking centre is the co-crystallised GRL0617 centroid computed by the pipeline's own `dock._ligand_center` — never hand-rolled — and audited in the driver: the pick is residue TTT (GRL0617), chain A, 23 heavy atoms (C20H20N2O), centroid [9.82, −11.83, 32.76]. The second TTT copy (chain J, the symmetry-related copy) was not averaged in, because the picker groups by full residue identity. The catalytic Cys111 sits in the pocket; GRL0617 binds the BL2 groove adjacent to it, not the catalytic site itself.

### 2.4 Docking protocol

AutoDock Vina 1.2.7, exhaustiveness 8, box 22.5 Å, best of three poses reported, same centre and box for all five compounds. Docking set (all from Ma et al. 2021, one FRET assay, document CHEMBL5107976): GRL0617 (CHEMBL549695; IC50 2,670 nM in this assay; paper value 2.05 ± 0.12 µM) as the reference and re-dock control; CHEMBL5079592 (113 nM, the most potent compound in the series); Jun9-72-2 (CHEMBL5173886; 670 nM); Jun9-84-3 (CHEMBL5182315; 670 nM); CHEMBL5200289 (42,000 nM, the weakest in the set). The two Jun9 names were verified PubChem → InChIKey → ChEMBL → activity; the other two analogues are tabled by ChEMBL ID only, because the paper's text does not name them and no name is invented. Rank correlation: Spearman ρ between best Vina score and measured pIC50 (pIC50 = −log10(IC50 in M)), ties by average ranks; negative ρ is the correct direction (better dock, more potent). **Causal identification, named explicitly:** validated-control re-docking (GRL0617 into its own crystal structure) — the only causal claim is about the method's ranking ability, and it rests on that control; everything else in this paper is association.

### 2.5 PAINS screen and ToxGuard

RDKit PAINS filter for every compound; RDKit descriptors (Lipinski/Veber); ToxGuard Tox21 kNN read-across (k = 15) reported with its maximum neighbour similarity, so the reader can see how weak the coverage is.

### 2.6 Honesty limits

Docking ≠ activity; Vina noise is ±1–2 kcal/mol; the receptor is rigid and the BL2 loop is frozen in its GRL0617-bound closed conformation; no MD or free-energy refinement was run; no experiment was performed. The measured IC50s are single-assay values from one paper (n = 5 compounds), and two of them tie at 670 nM.

### 2.7 Literature and the Islamic canon

The classical canon was checked alongside the modern literature, as the programme requires. Ibn Sina's *Canon of Medicine* (c. 1025) classifies epidemic fevers (*humma*) and Al-Razi's *Kitab al-Hawi* (c. 900, 23 volumes) and *On Smallpox and Measles* (c. 910) record the clinical distinction of eruptive fevers — all centuries before the viral aetiology of COVID-19, so none names PLpro, and no Canon-listed remedy was docked or screened in this run; the paper claims no traditional-medicine finding. The honest limit, named here: the full 23-volume *Hawi* exists in English only in selections, and most classical Arabic medical manuscripts remain undigitised; the sweep covers the named canonical works, not every book ever written.

## 3. Results

### 3.1 The ChEMBL landscape for PLpro

ChEMBL holds 699 PLpro IC50 activities (561 molecules) against the polyprotein target — a target that is, on paper, well covered. The most potent records in the database are 1–3 nM, from two 2024 ACS Medicinal Chemistry Letters patent-disclosure papers (PMID 39140061, 39563803); those values are single rounded records and were not used in the docking set, because a rank test needs one assay, not the smallest numbers in the database. The usable benchmark is the Ma et al. 2021 series: 57 compounds in one FRET assay, IC50s from 113 nM to 56 µM.

### 3.2 The discarded run, in one paragraph

The standard pipeline resolved the target to human maltase-glucoamylase (CHEMBL2074), UniProt P0DTC1, and docked 26 maltase ligands into the NSP3 macrodomain (8AZC), all failing. It completed with "PIPELINE OK: True". Only the target line betrayed it. This is the sixth time in this series the maltase substitution has had to be caught by hand (after GyrB, DHFR, PTP1B, Mpro, PfPI4K); the rule stands: **no accession match, no benchmark**.

### 3.3 Docking: the comparison table

**Table 1. Five GRL0617-series inhibitors docked on 7JRN (PLpro–GRL0617 complex, 2.48 Å). IC50s are Ma et al. 2021 FRET assay values.**

| Compound | Measured IC50 (nM) | Vina score (kcal/mol) | Top-3 poses |
|---|---|---|---|
| GRL0617 (QUERY, re-dock) | 2,670 | −9.90 | −9.90, −9.51, −8.41 |
| CHEMBL5079592 (most potent) | 113 | −9.74 | −9.74, −9.25, −8.79 |
| CHEMBL5200289 (weakest in set) | 42,000 | −9.14 | −9.14, −8.71, −8.00 |
| Jun9-84-3 | 670 | −8.21 | −8.21, −7.76, −7.54 |
| Jun9-72-2 | 670 | −7.74 | −7.74, −7.74, −7.71 |

All five compounds are PAINS-clean. Properties: GRL0617 MW 304.39, logP 4.22, 2 H-bond donors, TPSA 55.12 Å², zero Lipinski violations; Jun9-72-2 MW 291.39, logP 4.74, zero violations; Jun9-84-3 MW 314.43, logP 5.51, one violation (logP > 5); CHEMBL5079592 MW 504.70, logP 4.60, 5 donors, one violation (MW > 500); CHEMBL5200289 MW 295.41, logP 4.70, zero violations.

### 3.4 The ranking fails

Spearman ρ = +0.15 (n = 5) between best Vina score and measured pIC50 — no correlation, slightly positive. The re-dock control worked: GRL0617 scored −9.90 in its own pocket with consistent poses. But the ranking is wrong in the ways that matter. The weakest compound in the set, CHEMBL5200289 (42 µM, 372-fold less potent than the best), scored third-best (−9.14) and beat both named leads. Jun9-72-2 and Jun9-84-3 — the paper's own leads, threefold more potent than GRL0617 in the enzyme assay and threefold more active against live virus — scored worst and second-worst (−7.74 and −8.21). The most potent compound (113 nM) did score second (−9.74), 0.16 kcal/mol behind GRL0617, which is inside the noise band: the top two are indistinguishable, and the bottom three are misordered. The docking spread is 2.16 kcal/mol against a 372-fold measured range (~3.5 kcal/mol), so the method compresses the differences as well as misordering them.

### 3.5 Comparison with published docking

There is no published Vina benchmark on this series to compare against. What exists is the mechanistic account from Ma et al. themselves: they docked Jun9-53-2, Jun9-72-2 and Jun9-75-4 into 7JRN and ran 100 ns molecular dynamics, showing that the analogues replace GRL0617's carboxamide with a trialkyl ammonium group, gaining a strong ionic hydrogen bond to Asp164 (plus Arg166) and a better fit in the S4 pocket, with the naphthalene ring π-stacking Tyr264 and contacting Pro247/Pro248. GRL0617's own binding closes the BL2 loop. None of that — the ionic bond, the loop closure, the induced fit — is visible to a rigid receptor and a Vina scoring function. The published MD result predicts exactly the failure observed here, which is why §4 reads the failure as a property of the method, not of the compounds.

### 3.6 ToxGuard read-across is too weak to quote

ToxGuard's kNN read-across found no close neighbour for any compound (maximum similarity 0.235–0.467). GRL0617's highest assay scores are NR-AhR 0.494 and SR-ARE 0.267 at maximum similarity 0.367. Read honestly, that is an admission that the model has almost nothing to read across from — not a safety assessment. The compounds' real safety signal is not computational: GRL0617 has animal and cell data behind it (Kuzikov et al. 2025), and the analogues have none yet.

## 4. Discussion

### 4.1 The reframe: the BL2 loop is the unmeasured variable

This paper's finding is the mirror image of the Mpro paper's. On Mpro, rigid docking got the extremes right (ρ = +0.48) because the potency differences tracked non-covalent fit in a rigid pocket. On PLpro it fails (ρ = +0.15) because the potency differences track something else: a charged interaction with Asp164 and the closure of a flexible loop. Ma et al.'s own MD shows the Jun9 compounds' advantage is precisely the part of binding that a rigid structure cannot represent — the receptor in 7JRN is frozen in the conformation GRL0617 induced, and the scoring function has no term for the ionic hydrogen bond that distinguishes the analogues. The re-dock control working (−9.90 for GRL0617) makes the failure sharper, not softer: the method can recognise the ligand the structure was solved with, and cannot rank anything else in that pocket. The honest reading is that 7JRN is a GRL0617-shaped hole, and Vina scores how well a molecule fills that hole — which is not the same as how well it inhibits the enzyme.

### 4.2 Why the "win" must not be over-read

GRL0617's −9.90 is a re-dock, not a discovery: it is the ligand the structure was solved with, scored in its own pocket, and a strong score there is the minimum a method must produce, not evidence that GRL0617 is the best inhibitor. The 0.16 kcal/mol gap to the most potent analogue is inside Vina's ±1–2 kcal/mol noise. And the strongest absolute scores in this table belong to the wrong compounds: a 42 µM compound at −9.14 would look like a lead to anyone who read the scores without the measured potencies beside them. That is the operational danger this paper documents — a screening campaign that ranked by Vina score alone would advance the weakest compound over the two leads.

### 4.3 Association only

This is a retrospective computational benchmark, not a causal experiment. It shows that rigid Vina docking into 7JRN does not rank five GRL0617-series inhibitors (ρ = +0.15, n = 5), that the re-dock control works, and that the published MD mechanism predicts the failure. It does not show that any compound is a drug, that PLpro inhibition works in patients, or that flexible methods will succeed — that is the falsifier's job, not this paper's.

### 4.4 Testable hypotheses

1. **Induced-fit docking (or MM-GBSA rescoring) on the same five compounds recovers ρ ≤ −0.5.** Falsifier: the same five compounds, same pocket, flexible receptor; ρ above −0.5 refutes the rigidity explanation and indicts the pocket or the scoring function instead.
2. **The Asp164 ionic hydrogen bond is the potency driver.** Falsifier: an Asp164→Ala PLpro mutant; if Jun9-72-2 and Jun9-84-3 lose their threefold advantage over GRL0617 against the mutant while GRL0617 is unaffected, the mechanism is confirmed; if they keep it, the MD explanation is wrong.
3. **CHEMBL5079592 (113 nM) is a better antiviral than Jun9-72-2 in cells.** Falsifier: Vero E6 antiviral assay; EC50 above Jun9-72-2's 6.62 µM would refute it despite the enzyme potency.
4. **A PLpro inhibitor that also restores interferon signalling beats a pure catalytic inhibitor in a cell model.** Falsifier: paired enzyme + interferon-reporter assays; if interferon restoration tracks catalytic inhibition 1:1, the dual-mechanism framing adds nothing.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): obtain GRL0617 and the four analogues commercially (all are in ChEMBL/PubChem with suppliers listed) and confirm identity and purity by LC-MS. Stage 2 (weeks 3–6): FRET-based PLpro enzyme assay (Z-RLRGG-AMC substrate, as in Ma et al. 2021) at 10 µM, 1 µM and 0.1 µM, with GRL0617 as control and a redox/thiol-artefact panel (DTT sensitivity, detergent control) following Kuzikov et al. 2025 — the artefact check is mandatory for this target, not optional. Stage 3 (weeks 7–10): FlipGFP cell assay for the compounds active below 1 µM, then Vero E6 antiviral assay for the best two. Stage 4 (weeks 11–12): induced-fit docking or MM-GBSA on the same five compounds, to test hypothesis 1. Report all five results, including the negatives.

## 5. Limitations

1. **No lab data.** All results are computational; no PLpro assay was run.
2. **Rigid docking, ±1–2 kcal/mol noise.** The 2.16 kcal/mol docking spread is barely outside the noise band, and the top-two gap (0.16) is inside it.
3. **Small n, one assay.** The rank correlation uses five compounds from one paper's FRET assay; two tie at 670 nM, and a single additional compound could change ρ substantially.
4. **Single structure.** One crystal structure (7JRN), one BL2-loop conformation; no ensemble, no MD, no free-energy refinement.
5. **No RMSD for the re-dock.** The re-dock control is reported as a score with consistent poses; the docked pose was not compared atom-by-atom with the crystal pose.
6. **Assay heterogeneity for the consensus value.** GRL0617's cross-assay median (2.05 µM, n = 21 records) spans 0.6–7.0 µM; the ranking test uses the single-assay value (2.67 µM) to avoid mixing assays, but the consensus is itself assay-dependent.
7. **ToxGuard coverage is weak.** Maximum neighbour similarity 0.235–0.467; the Tox21 scores must not be quoted as safety evidence.
8. **Islamic canon gaps (named, per the programme's rule).** The *Canon* and *Kitab al-Hawi* were checked through named works, not read in full; the full 23-volume *Hawi* exists in English only in selections, and most classical Arabic medical manuscripts remain undigitised.

## 6. Policy implications

**Decision-maker: the Drug Regulatory Authority of Pakistan (DRAP), the National Institute of Health, and the Higher Education Commission — and, for the method rule, every public funder of computational drug discovery in Pakistan.** Three exact changes, each with its falsifier:

1. **Fund one PLpro enzyme assay in Pakistan, at a single reference laboratory, and publish the protocol.** Pakistan has no domestic route from a computational PLpro claim to a measured number, and the country imports every antiviral it uses. One FRET assay (the Ma et al. 2021 protocol, Z-RLRGG-AMC substrate) plus the Kuzikov artefact panel would let any Pakistani group test a PLpro claim in weeks. If the assay shows the Jun9 leads inactive, the scaffold is closed and the money is still well spent — a dead end found in weeks beats a decade of untested docking. Reverse this only if a cheaper regional assay (e.g. through an international collaboration) becomes available to Pakistani groups.
2. **Require a re-dock control and an accession-verified target in every publicly funded computational screen.** Any screening proposal must state the UniProt accession and the ChEMBL target ID it resolved to, and must report the reference drug re-docked into its own structure before any lead is claimed. This paper's discarded maltase run and its failed ranking are the evidence: without that rule, public money can fund a complete benchmark of the wrong enzyme, or a ranking that inverts the truth. Reverse this only if a blinded test shows rigid docking ranking PLpro inhibitors correctly without those controls.
3. **Do not buy or prescribe GRL0617 analogues as COVID-19 treatments.** They are preclinical leads with enzyme and cell data only; the strongest evidence in this paper is a negative result about a computational method, not a positive result about a drug. The correct public position is to fund the assay in (1) and let the compounds decide. **Islamic principle behind the recommendations:** preservation of life (*hifz al-nafs*, Al-Ghazali, *Al-Mustasfa*; Al-Shatibi, *Al-Muwafaqat*) — a screening method that mis-ranks antivirals during a circulating pandemic is a failure to protect life, not a technical footnote; and stewardship (*khilafah*, Qur'an 2:30) — public research funds are a trust, and a steward does not spend a trust on a ranking that inverts the truth. Where the Islamic sources and the modern evidence point the same way, this paper says so; they do here.

## 7. Conclusion

Rigid docking into the GRL0617-bound PLpro structure 7JRN gives no rank correlation with measured potency (Spearman ρ = +0.15, n = 5): the reference re-docks well (−9.90 kcal/mol), the most potent analogue scores second (−9.74), and the weakest compound in the set (42 µM) beats both named leads. The method that ranked Mpro analogues at the extremes cannot rank PLpro inhibitors at all, because the analogues' advantage — an ionic bond to Asp164 and closure of the flexible BL2 loop — is invisible to a rigid receptor. Docking can confirm that a molecule fits the GRL0617 pocket; ranking PLpro inhibitors needs the enzyme assay, and the flexible method that the falsifier names. The memorable number is **+0.15**: the correlation between the score and the truth, on the target that most needs a second drug.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. World Health Organization. Coronavirus disease (COVID-19) fact sheet. Accessed November 2026. (Nearly 780 million confirmed cases; more than 7.1 million reported deaths worldwide.)
2. National Institute of Health, Pakistan. COVID-19 data, 2023. ~1.58 million confirmed cases; 30,656 deaths. (As cited in HP-037.)
3. Ratia K, Pegan S, Takayama J, Sleeman K, Coughlin M, Baliji S, et al. A noncovalent class of papain-like protease/deubiquitinase inhibitors blocks SARS virus replication. *Proc Natl Acad Sci USA*. 2008;105(42):16119–16124. PMID: 18852458. doi:10.1073/pnas.0805240105.
4. Shin D, Mukherjee R, Grewe D, Bojkova D, Baek K, Bhattacharya A, et al. Papain-like protease regulates SARS-CoV-2 viral spread and innate immunity. *Nature*. 2020;587:657–662. PMID: 32726803. doi:10.1038/s41586-020-2601-5.
5. Ma C, Sacco MD, Xia Z, Lambrinidis G, Townsend JA, Hu Y, et al. Discovery of SARS-CoV-2 papain-like protease inhibitors through a combination of high-throughput screening and a FlipGFP-based reporter assay. *ACS Cent Sci*. 2021;7:1245–1260. PMID: 34341772. doi:10.1021/acscentsci.1c00519. (7JRN structure; GRL0617 IC50 2.05 ± 0.12 µM; Jun9 series; BL2 mechanism; antiviral EC50s.)
6. Shen Z, Ratia K, Cooper L, Kong D, Lee H, Kwon Y, et al. Potent, novel SARS-CoV-2 PLpro inhibitors block viral replication in monkey and human cell cultures. *bioRxiv*. 2021. doi:10.1101/2021.02.13.431008. (HTS: only CPI-169 and GRL0617 IC50 < 10 µM; 2-phenylthiophene analogues; BL2 groove.)
7. Kuzikov M, Morasso S, Reinshagen J, Wolf M, Monaco V, Cozzolino F, et al. Thiol-reactive or redox-active: revising a repurposing screen led to a new invalidation pipeline and identified a true noncovalent inhibitor against papain-like protease from SARS-CoV-2. *ACS Pharmacol Transl Sci*. 2025;8(1):66–77. PMID: 39816795. doi:10.1021/acsptsci.4c00325.
8. Inhibitors targeting SARS-CoV-2 papain-like protease: screening, design, synthesis, and biological evaluation. *ChemMedChem*. 2026. PMID: 42104549.
9. Novel papain-like protease inhibitors for treating viral infections, in particular, coronavirus infections. *ACS Med Chem Lett*. 2024. PMID: 39140061. doi:10.1021/acsmedchemlett.4c00331.
10. Novel papain-like protease inhibitors for treating viral infections, in particular coronavirus infections. *ACS Med Chem Lett*. 2024. PMID: 39563803. doi:10.1021/acsmedchemlett.4c00474.
11. UniProtKB P0DTD1 (Replicase polyprotein 1ab, SARS-CoV-2). PLpro nsp3 domain, pp1ab residues 1564–1878; active-site residues pp1ab 1674 (Cys111) and 1835 (His272). Accessed 17 November 2026.
12. ChEMBL target CHEMBL4523582 (Replicase polyprotein 1ab); 699 PLpro IC50 activities, 561 molecules, filtered by assay description; GRL0617 (CHEMBL549695) median IC50 2,050 nM, n = 21 records. Accessed 17 November 2026.
13. RCSB PDB 7JRN. Crystal structure of the wild type SARS-CoV-2 papain-like protease (PLPro) with inhibitor GRL0617. 2.48 Å, X-ray. Accessed 17 November 2026.
14. Qur'an 2:30 (stewardship, *khilafah*). Al-Ghazali. *Al-Mustasfa* (the five objectives of the law). Al-Shatibi. *Al-Muwafaqat fi Usul al-Shari'a*.
15. Ibn Sina. *Al-Qanun fi al-Tibb* (Canon of Medicine, c. 1025), on epidemic fevers (*humma*). Al-Razi. *Kitab al-Hawi fi al-Tibb* (Comprehensive Book of Medicine, c. 900); *Kitab al-Judari wa al-Hasba* (On Smallpox and Measles, c. 910) — checked through named works, not read in full; see Limitations (§5, item 8).

## Data availability

All docking scores reported here are in `dock-HP-073-2026-11-17.json`: target verification (UniProt P0DTD1; ChEMBL CHEMBL4523582), GRL0617 measured IC50 records (median 2,050 nM, n = 21), the five compounds with descriptors / PAINS / ToxGuard values, the 7JRN centre audit (TTT chain A, 23 atoms, [9.82, −11.83, 32.76]), all docking poses, and Spearman ρ = +0.154 (n = 5). The discarded wrong-target run is preserved as `dock-HP-073-2026-11-17-WRONG-TARGET.json` (pipeline resolved the target to CHEMBL2074, human maltase-glucoamylase; 26 maltase ligands; all docks into 8AZC failed). Driver script: `~/workspace/leadforge-daily/dock_hp073_plpro_2026-11-17.py`. Structure: PDB 7JRN (2.48 Å). Measured potencies: Ma et al. 2021 (PMID 34341772; ChEMBL document CHEMBL5107976). No additional data were generated.
