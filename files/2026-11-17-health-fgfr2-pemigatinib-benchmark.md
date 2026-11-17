# Pemigatinib Re-Docks at −8.83 kcal/mol on FGFR2 2PVF, but the Most Potent Measured Inhibitor Scores Worst and the Most Potent Lead Was Never Docked

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-17 · **Health Papers Agent — Paper #71** (daily 5-paper run)
**Topic ID:** HP-080

**Keywords:** FGFR2; pemigatinib; cholangiocarcinoma; molecular docking; AutoDock Vina; futibatinib; hyperphosphataemia; drug discovery

---

## Abstract

FGFR2 fusions drive 10–15% of intrahepatic cholangiocarcinoma, and pemigatinib, the first approved FGFR inhibitor for this disease, produced a 35.5% objective response rate in FIGHT-202. We benchmarked rigid AutoDock Vina docking (v1.2.7) against measured FGFR2 inhibition for four sub-nanomolar compounds on the activated FGFR2 kinase structure 2PVF (1.8 Å), with the grid centre audited to exactly 0.00 Å from the ATP-analogue centroid. Pemigatinib re-docked at −8.83 kcal/mol, reproduced to −8.90 by its own ChEMBL record, a 0.07 kcal/mol duplicate. But the ranking fails: the most potent measured inhibitor, CHEMBL4870179 (IC50 0.15 nM), scored worst at −8.01, and the most potent compound in the whole 26-lead set (CHEMBL5173892, 0.11 nM) was never docked, because the pipeline's similarity-dominated ranking placed it 20th. Spearman rho is +0.40 (n = 4). ChEMBL mutant records add the clinically decisive number: pemigatinib loses about 6,000-fold potency against the gatekeeper mutant FGFR2 V564F (IC50 1,460.5 nM), a loss no wild-type docking score can see. The honest limit cuts deeper than the ranking: the two leads' sub-nanomolar values come from a single document, while a patent document reports 100 nM for both. Falsifiable claim: rigid docking on the activated FGFR2 structure cannot rank sub-nanomolar FGFR2 inhibitors. A re-dock on an inhibitor-bound, inactive-conformation FGFR2 structure that recovers the measured order with rho at or below −0.5 would refute it; so would a prospective enzyme assay showing CHEMBL5171314, the best-docked compound, underperforming pemigatinib in cells.

---

## 1. Introduction

Intrahepatic cholangiocarcinoma (iCCA) is a rare, aggressive cancer of the bile ducts with few effective systemic options after first-line chemotherapy. FGFR2 fusions and rearrangements — chromosomal rearrangements that fuse the FGFR2 kinase domain to a partner gene, producing ligand-independent dimerisation and constitutive signalling — occur in approximately 10–15% of iCCA and almost nowhere else, making them one of the most actionable alterations in oncology. Pemigatinib, a selective oral inhibitor of FGFR1, 2 and 3, became the first approved drug for this population on the FIGHT-202 trial (Abou-Alfa et al. 2020): among 107 previously treated patients with FGFR2 fusions or rearrangements, 38 (35.5%, 95% CI 26.5–45.4) achieved an objective response, three of them complete, on 13.5 mg daily (two weeks on, one week off). Hyperphosphataemia — the on-target class effect of FGFR inhibition, which blocks FGF23 signalling and raises serum phosphate — was the most common adverse event at 60% (88/146). The covalent next-generation inhibitor futibatinib followed in FOENIX-CCA2 (Goyal et al. 2023): 43 of 103 patients (42%, 95% CI 32–52) responded, median duration of response 9.7 months, median progression-free survival 9.0 months and overall survival 21.7 months, with grade 3 hyperphosphataemia in 30%.

The clinical question this paper attacks is narrower than "does pemigatinib work" — that is settled. It is whether a standard computational benchmark can rank FGFR2 inhibitors at all, in a target where every known inhibitor is already sub-nanomolar. When the whole measured range spans 0.11–0.5 nM — a 4.5-fold window, or 0.89 kcal/mol of binding free energy — the differences a screen must resolve are smaller than Vina's documented ±1–2 kcal/mol noise. The falsifiable hypothesis, stated before the results: under one standardised protocol on the activated FGFR2 structure 2PVF, Vina will reproduce pemigatinib's own docking within 0.1 kcal/mol (the duplicate control) but will not recover the measured potency order of four sub-nanomolar inhibitors (Spearman rho above −0.5), because the potency differences are below the method's resolution.

## 2. Methods

### 2.1 Literature basis

PubMed (E-utilities, accessed 17 November 2026) for FIGHT-202, FOENIX-CCA2 and FGFR2 fusion prevalence; ChEMBL (live API, accessed 17 November 2026) for target, potency and resistance-mutant records. Every number traces to a PMID-verified source, a ChEMBL record named in the text, or a computation in the raw JSON. The Islamic canon check is in §2.5.

### 2.2 Molecular docking

Standardised AutoDock Vina protocol, exactly as Papers #1/#3: Vina v1.2.7, exhaustiveness 8, box 22.5 Å, best of three poses reported, same binding site, grid centre and box for the reference drug and every test compound. Target: FGFR2, UniProt P21802, resolved by accession to ChEMBL target CHEMBL4142 (Fibroblast growth factor receptor 2, Homo sapiens, SINGLE PROTEIN, component P21802 — verified live; the pipeline's text-search list offered maltase-glucoamylase CHEMBL2074 first, as usual, and it was not used). Structure: PDB 2PVF, 1.8 Å, the tyrosine-phosphorylated activated FGFR2 kinase domain in complex with the ATP analogue ACP (adenosine 5′-(β,γ-methylene)triphosphate) and a substrate peptide. **Centre audit:** the docking centre [23.11, −5.95, −2.14] is exactly the centroid of the 31-atom ACP ligand, computed directly from the 2PVF HETATM records (distance 0.00 Å) — the ATP-binding pocket, the correct site for an ATP-competitive inhibitor. The phosphotyrosine residue PTR 586 (substrate peptide) sits 17.3 Å from the centre and was not used. Ligands: the top five leads by the pipeline's composite score (similarity × 40 + Lipinski × 20 + Veber × 10 + PAINS × 10 + tox × 20) plus the reference query itself, from 40 ChEMBL bioactivities at pChEMBL ≥ 5 for CHEMBL4142. PAINS screen (RDKit) and ToxGuard Tox21 kNN panel for every compound. Spearman rank correlation between best Vina affinity and measured pChEMBL, computed on the four distinct docked compounds (the duplicate pemigatinib dock excluded); negative rho is the correct direction (better dock, more potent).

### 2.3 The duplicate control, stated in advance

The pipeline returns the reference drug twice: once as the QUERY (PubChem CID 86705695, pemigatinib) and once as ChEMBL4297522, which ChEMBL identifies as PEMIGATINIB (max phase 4, first approval 2020), same formula C24H27F2N5O4. Both were docked. Their score difference is a built-in reproducibility control for the whole protocol: two independent ligand preparations of the same molecule, same site, same box.

### 2.4 Honesty limits

Docking ≠ activity; Vina noise is ±1–2 kcal/mol; no experimental data were generated; no molecular dynamics or free-energy refinement was run; the structure is the activated (phosphorylated) kinase, not an inhibitor-bound inactive conformation. Measured potencies are ChEMBL top records and span assay formats (see §3.3).

### 2.5 Literature and the Islamic canon

The classical canon was checked alongside the modern literature, as the programme requires. Ibn Sina's *Canon of Medicine* (c. 1025) discusses diseases of the liver and bile in detail, and Al-Razi's *Kitab al-Hawi* (c. 900) records biliary disease; both predate the molecular diagnosis of cholangiocarcinoma by nine centuries, so neither names FGFR2, and no Canon-listed remedy was docked or screened in this run — the paper claims no traditional-medicine finding. The honest limit, named here: the full 23-volume *Kitab al-Hawi* exists in English only in selections, and most classical Arabic medical manuscripts remain undigitised.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Measured FGFR2 IC50 (ChEMBL top record) | pChEMBL | Best affinity (kcal/mol) | Poses (kcal/mol) | PAINS |
|---|---|---|---|---|---|
| CHEMBL5171314 | 0.27 nM | 9.57 | **−9.25** | −9.25, −9.24, −8.94 | none |
| Pemigatinib (CHEMBL4297522) | 0.24 nM | 9.62 | −8.90 | −8.90, −8.84, −8.77 | none |
| Pemigatinib (QUERY, duplicate) | — (same molecule) | — | −8.83 | −8.83, −8.71, −8.69 | none |
| CHEMBL4862823 | 0.30 nM | 9.52 | −8.12 | −8.12, −8.11, −8.09 | none |
| CHEMBL4870179 | 0.15 nM | 9.82 | −8.01 | −8.01, −8.00, −7.49 | none |

All five docks completed with tight poses (best-to-third spread ≤ 0.52 kcal/mol). The duplicate control passed: pemigatinib docked twice at −8.83 and −8.90, a 0.07 kcal/mol difference — the protocol reproduces itself. The ranking did not: the most potent measured inhibitor, CHEMBL4870179 (0.15 nM), scored worst (−8.01), 1.24 kcal/mol behind the best-docked compound, while the best-docked compound, CHEMBL5171314 (−9.25), is only the third most potent by measurement (0.27 nM). Spearman rho is **+0.40 (n = 4)** — a weak positive correlation carried by the middle of the table, while the most potent compound still scores worst. The spread of the whole docking table (1.24 kcal/mol) is inside Vina's noise band, and the spread of the whole measured range (0.15–0.30 nM) is 0.41 kcal/mol of binding free energy — the signal is smaller than the noise, and the result is what that arithmetic predicts.

### 3.2 Potency is solved; the ranking problem is the selection problem

All 26 leads retrieved for FGFR2 are sub-nanomolar: IC50 0.11–0.50 nM, pChEMBL 9.30–9.96. The most potent compound in the set, CHEMBL5173892 (IC50 0.11 nM, pChEMBL 9.96), was never docked: the pipeline docks the top five by a similarity-dominated composite score, and CHEMBL5173892 ranks 20th by that score (similarity 0.178 to pemigatinib). The same failure appeared in this series' DPP-4 paper, where the most potent compound in the set was never docked for the same reason. A screen that ranks by similarity to the reference drug systematically undocks the most potent compounds when they are the least similar to the reference — which is exactly the property a novel scaffold should have. One PAINS alert exists in the 26-lead set (CHEMBL1852688, rank 26); all docked compounds are PAINS-clean. Pemigatinib itself computes as drug-like: MW 487.51, logP 3.66, 1 donor, 6 acceptors, TPSA 83.16 Å², 6 rotatable bonds, zero Lipinski violations; ToxGuard kNN read-across is weak (maximum neighbour similarity 0.271) with all twelve Tox21 assay scores ≤ 0.239.

### 3.3 The measured order is less certain than the single numbers suggest

The two leads' sub-nanomolar values come from a single document each: CHEMBL4870179 (0.15 nM) and CHEMBL4862823 (0.30 nM) were both measured in one assay series (biotinylated-peptide substrate, human FGFR2, document CHEMBL4808209), and their relative order rests on that one series. A patent document (CHEMBL5726086) reports IC50 100 nM for both compounds under different conditions — a 300- to 600-fold conflict with the paper values. Pemigatinib's own record shows the same assay-to-assay spread: 0.24 nM (the pipeline's top record), 0.4 nM, 0.5 nM in three further records, and 1.0 nM by ELISA — a four-fold range for one drug. The honest reading is that the measured order among these four compounds is itself uncertain at the 0.4–0.9 kcal/mol level, before docking adds its own ±1–2 kcal/mol. The rho of +0.40 is therefore a statement about two uncertain orderings, not a precise measurement of docking failure — it is weakly positive only because the middle of the table lines up, while the most potent compound scores worst, and no re-analysis of the same four numbers can make it a ranking claim without new data.

### 3.4 The resistance data the docking cannot see

ChEMBL's mutant records for pemigatinib (document CHEMBL5131515, radiometric kinase assay) quantify the resistance problem that defines this target's future: against the gatekeeper mutant FGFR2 V564F, pemigatinib's IC50 is **1,460.5 nM** — roughly 6,000-fold worse than wild type (0.24 nM) — and against N549H it is 3.37 nM, about 14-fold worse. Rigid docking on a wild-type structure cannot price either mutation: the V564F change is a single side chain in the ATP pocket, and the 6,000-fold loss is a steric and energetic effect that a rigid, metal-free, wild-type score has no way to represent. This is the same lesson as the series' covalent papers (DprE1, BTK): the clinically decisive number for an FGFR2 inhibitor is not its wild-type IC50, which is sub-nanomolar for every compound in the set, but its mutant coverage — and that number is not a docking number. Futibatinib's advantage in FOENIX-CCA2 is precisely that it is covalent and retains activity against acquired resistance mutations; the NEJM abstract states this directly.

### 3.5 Comparison with published docking

No published Vina benchmark of pemigatinib against these three ChEMBL leads on 2PVF was found in the literature sweep; the comparison is therefore internal (duplicate control, §2.3) and clinical (FIGHT-202 and FOENIX-CCA2 response rates). The paper does not claim its scores contradict any published docking result.

## 4. Discussion

### 4.1 The reframe: the target is solved, the screen is not

FGFR2 inhibition is a solved problem at the potency level: 26 compounds below 0.5 nM, two approved drugs, response rates of 35–42%. The unsolved problems are selectivity against FGFR1 (the hyperphosphataemia driver), mutant coverage (V564F costs pemigatinib 6,000-fold), and access (see §7). A docking screen that ranks sub-nanomolar compounds against each other on a wild-type structure answers none of these. It also actively misleads: it promotes CHEMBL5171314, an unnamed research compound, above the two approved drugs' class, on a 0.42 kcal/mol margin that is noise, while the compound that most needs docking — the most potent, least similar one — never gets docked at all.

### 4.2 Why the "win" must not be over-read

CHEMBL5171314's −9.25 is the best score in the table and means nothing on its own: it is 0.35 kcal/mol ahead of pemigatinib, inside noise; its measured potency is worse than pemigatinib's; and it is an unnamed compound with no clinical record. The duplicate control (Δ0.07) proves the protocol is reproducible, which makes the ranking failure more informative, not less: a reproducible method returning a reversed ranking is a method whose resolution is below the signal, not a method with a bug to fix by re-running.

### 4.3 Association only

This is a retrospective docking benchmark, not a causal experiment: it shows that Vina scores on 2PVF do not track measured FGFR2 potency within four sub-nanomolar compounds, under the stated protocol. It does not show that no docking method can rank these compounds — the falsifier names the method that could — and it does not show that CHEMBL5171314 is a worse drug than pemigatinib.

### 4.4 Testable hypotheses

1. **CHEMBL5171314 does not outperform pemigatinib in cells.** Falsifier: paired FGFR2-driven cell viability assays (e.g. FGFR2-fusion iCCA lines); an IC50 for CHEMBL5171314 below pemigatinib's would refute the docking-implied order in the other direction.
2. **A re-dock on an inhibitor-bound inactive FGFR2 structure recovers the measured order (rho ≤ −0.5).** Falsifier: the re-dock itself; if rho stays above −0.5, the failure is the scoring function, not the conformation.
3. **CHEMBL5173892 (0.11 nM, never docked) docks within 0.5 kcal/mol of pemigatinib.** Falsifier: dock it on 2PVF under the same protocol; a score worse than −8.3 would show the selection problem is also a scoring problem.
4. **The V564F resistance gap is invisible to wild-type docking.** Falsifier: a V564F-mutant structure dock showing pemigatinib losing ≥ 2 kcal/mol relative to wild type; a smaller loss would suggest the mutant effect is partly assay artefact.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): dock CHEMBL5173892 on 2PVF under the identical protocol, and re-dock all five compounds on an inhibitor-bound FGFR2 structure (DFG-out if available) to test hypothesis 2. Stage 2 (weeks 3–6): obtain CHEMBL5171314 and CHEMBL4870179 commercially and run paired FGFR2 enzyme assays (wild type, V564F, N549H) with pemigatinib and futibatinib as controls. Stage 3 (weeks 7–10): cell viability in an FGFR2-fusion iCCA line for the two leads versus pemigatinib. Stage 4 (weeks 11–12): report all results including the negatives — a reversed ranking confirmed in cells is a publishable result.

## 5. Limitations

1. **No lab data.** All results are computational; no FGFR2 assay was run, and the measured IC50s are ChEMBL records.
2. **Small n.** Four distinct docked compounds; rho = +0.40 on n = 4 is a descriptive check, not a validated ranking failure.
3. **Assay heterogeneity.** The four potencies span documents and formats, and a patent document conflicts with the paper values for the two leads (§3.3).
4. **Single structure, activated conformation.** 2PVF is the phosphorylated, activated kinase with an ATP analogue bound; an inhibitor-bound inactive conformation might rank differently — that is the named falsifier, not a result.
5. **Selection bias.** Only the top five by a similarity-dominated composite were docked; the most potent compound in the set was excluded by that rule.
6. **No mutant docking.** V564F and N549H effects are reported from ChEMBL records, not computed.
7. **Islamic canon gaps (named, per the programme's rule).** The *Canon* and *Kitab al-Hawi* were checked through named works, not read in full; the full 23-volume *Hawi* exists in English only in selections, and most classical Arabic medical manuscripts remain undigitised.

## 6. Policy implications

**Decision-maker: the Drug Regulatory Authority of Pakistan (DRAP), the Ministry of National Health Services, and the national cancer programme — with the provincial health departments that run the public cancer hospitals.** Three exact changes, each with its falsifier:

1. **Make FGFR2 fusion testing available in the public system before buying the drug.** Pemigatinib helps only the 10–15% of iCCA patients with an FGFR2 fusion, and the test (RNA-based NGS or FISH) is the gate. A public laboratory that cannot test for the fusion cannot use the drug rationally, and will either treat unselected patients (wasting a costly drug on the 85–90% it cannot help) or treat nobody. Fund one reference NGS panel for FGFR2 fusions at a national laboratory, with a published turnaround time. If a validated, cheaper test (e.g. immunohistochemistry surrogate) is shown to match NGS for FGFR2 fusions, reverse this and fund that instead.
2. **Negotiate access, do not import at list price.** Pemigatinib and futibatinib are priced for high-income markets; at list price they are unreachable for a Pakistani public hospital. The state should seek a pooled-procurement or voluntary-licence route for FGFR inhibitors, as it has done for other oncology drugs, and publish the price it pays. If the manufacturers refuse, the fallback is the covalent-compound route in (3), not silent non-availability.
3. **Fund mutant-coverage testing, not more wild-type docking.** The clinically decisive number is V564F coverage (pemigatinib loses 6,000-fold), and no Pakistani laboratory currently runs an FGFR2 mutant panel. A single national panel (wild type, V564F, N549H) at one reference laboratory would convert this paper's falsifier into a routine check for any future FGFR2 inhibitor. **Islamic principle behind the recommendations:** preservation of life (*hifz al-nafs*, Al-Ghazali, *Al-Mustasfa*; Al-Shatibi, *Al-Muwafaqat*) — cholangiocarcinoma is a fatal disease and the drug exists, so a test that is not offered is a life not saved; and justice (*'adl*, Qur'an 4:135) — the burden falls on patients who cannot pay list price, so the research and procurement agenda must favour the poor, not the most familiar drug. Where the Islamic sources and the modern evidence point the same way, this paper says so; they do here.

## 7. Conclusion

Rigid Vina docking on the activated FGFR2 structure 2PVF reproduces pemigatinib itself to 0.07 kcal/mol and then ranks four sub-nanomolar inhibitors poorly (rho = +0.40, n = 4): the most potent measured compound scores worst, and the most potent compound in the set was never docked because it was too dissimilar to the reference. The measured range (0.15–0.30 nM, 0.41 kcal/mol) is smaller than the method's noise, and the measured order is itself uncertain across documents. The memorable number is **6,000-fold**: what the gatekeeper mutation V564F costs pemigatinib, a number no wild-type docking score can see. Do not rank FGFR2 inhibitors by wild-type docking; test mutant coverage instead.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Abou-Alfa GK, Sahai V, Hollebecque A, Vaccaro G, Melisi D, Al-Rajabi R, et al. Pemigatinib for previously treated, locally advanced or metastatic cholangiocarcinoma: a multicentre, open-label, phase 2 study. *Lancet Oncol*. 2020;21(5):671–684. PMID: 32203698. doi:10.1016/S1470-2045(20)30109-1.
2. Goyal L, Meric-Bernstam F, Hollebecque A, Valle JW, Morizane C, Karasic TB, et al. Futibatinib for FGFR2-rearranged intrahepatic cholangiocarcinoma. *N Engl J Med*. 2023;388(3):228–239. PMID: 36652354. doi:10.1056/NEJMoa2206834.
3. Clinical value of liquid biopsy in patients with FGFR2 fusion-positive cholangiocarcinoma during targeted therapy. *Clin Cancer Res*. 2024;30(19):4491–4504. doi:10.1158/1078-0432.CCR-23-3780. (FGFR2 fusions in 10–15% of iCCA.)
4. ChEMBL target CHEMBL4142 (Fibroblast growth factor receptor 2, Homo sapiens, component P21802). Accessed 17 November 2026.
5. ChEMBL bioactivities for CHEMBL4142 (accessed 17 November 2026): CHEMBL5171314 IC50 0.27 nM (document CHEMBL5096142); CHEMBL4297522 pemigatinib IC50 0.24 nM; CHEMBL4862823 and CHEMBL4870179 IC50 0.30 and 0.15 nM (document CHEMBL4808209), with conflicting 100 nM values in patent document CHEMBL5726086; pemigatinib vs FGFR2 V564F IC50 1,460.5 nM and vs N549H 3.37 nM (document CHEMBL5131515).
6. UniProtKB P21802 (Fibroblast growth factor receptor 2, Homo sapiens). PDB 2PVF (1.8 Å), activated FGFR2 kinase domain in complex with ATP analogue ACP.
7. PubChem CID 86705695 (pemigatinib). Accessed 17 November 2026.
8. Qur'an 4:135 (justice, *'adl*). Al-Ghazali. *Al-Mustasfa* (the five objectives of the law). Al-Shatibi. *Al-Muwafaqat fi Usul al-Shari'a*.
9. Ibn Sina. *Al-Qanun fi al-Tibb* (Canon of Medicine, c. 1025), on diseases of the liver and bile. Al-Razi. *Kitab al-Hawi fi al-Tibb* (Comprehensive Book of Medicine, c. 900) — checked through named works, not read in full; see Limitations §7.

## Data availability

All docking scores reported here are in `dock-HP-080-2026-11-17.json` (target verification, 26 leads with descriptors / PAINS / ToxGuard, 2PVF docking of five compounds plus the pemigatinib duplicate). Structures: PDB 2PVF (1.8 Å); centre [23.11, −5.95, −2.14], exactly the ACP centroid (0.00 Å, computed from HETATM records). Target: UniProt P21802; ChEMBL target CHEMBL4142, accessed 17 November 2026. Measured potencies: ChEMBL CHEMBL4142 bioactivities (see Reference 5). No additional data were generated.
