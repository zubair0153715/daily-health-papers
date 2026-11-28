# A 1.3 nM ChEMBL Ligand Out-Docks TNO155 on SHP2 by 2.01 kcal/mol — after the Pipeline Docked the Wrong Structure First

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-28 · **Health Papers Agent — Paper #128** (daily 5-paper run)

**Keywords:** SHP2; PTPN11; TNO155; allosteric inhibitor; RAS-MAPK; KRAS; molecular docking; ChEMBL; Pakistan

---

## Abstract

SHP2, encoded by PTPN11, is the first validated oncogenic tyrosine phosphatase and a central node downstream of receptor tyrosine kinases in the RAS–MAPK pathway; its allosteric inhibitors are in Phase I/II trials, but no SHP2 inhibitor is approved and monotherapy has so far produced stable disease at best. Pakistan recorded an estimated 185,748 new cancer cases in 2022 (GLOBOCAN), including 9,464 lung and 9,447 colorectal cancers — the tumour types where SHP2 combinations are being tested. We re-screened SHP2 with the standardised LeadForge protocol (UniProtKB Q06124 → ChEMBL target CHEMBL3864, 43 bioactivities → PubChem → RDKit → PAINS/ADMET → AutoDock Vina 1.2.7) and docked the top five leads plus TNO155 (batoprotafib, IC50 11 nM) in the same grid. The pipeline's automatic structure pick was wrong — PDB 9EIK is the isolated N-SH2 domain bound to a GAB1 phosphopeptide, with no allosteric pocket, and TNO155 scored only −5.75 kcal/mol there — so we re-docked on PDB 5EHR, full-length human SHP2 in complex with the allosteric inhibitor SHP099 (1.7 Å). On the correct structure the headline result is: CHEMBL4789817, an unnamed ChEMBL ligand with a measured Kd of 1.3 nM, out-docked TNO155 by 2.01 kcal/mol (−9.93 vs −7.92 kcal/mol), while CHEMBL4858291, the most potent molecule in the set by measurement (IC50 0.017 nM, ~650-fold more potent than TNO155), docked only third (−8.46 kcal/mol). Docking therefore compresses a 650-fold measured potency range into 0.54 kcal/mol and cannot rank these inhibitors. The falsifiable next step is a head-to-head phosphatase assay: CHEMBL4789817 must inhibit SHP2 with IC50 at or below TNO155's and show at least 10-fold selectivity over the closest phosphatase SHP1, or the docking rank is refuted. Until that assay exists, this paper is a triage signal only — no efficacy, safety or clinical claim follows.

---

## 1. Introduction

SHP2 (Src homology 2 domain-containing phosphatase 2, encoded by *PTPN11*) is the first identified oncogenic tyrosine phosphatase: it transmits signals from receptor tyrosine kinases into the RAS–MAPK cascade, it is overexpressed in colorectal cancer, and germline *PTPN11* mutations cause Noonan syndrome while somatic mutations drive leukaemias and solid tumours. For decades phosphatases were considered undruggable — the catalytic site is highly conserved and charged — until allosteric inhibition changed the field: SHP099, reported by Chen et al. in *Nature* (2016), locks SHP2 in its autoinhibited conformation by binding a pocket at the interface of the N-SH2, C-SH2 and PTP domains, and showed antitumour activity in RTK-driven models. TNO155 (batoprotafib, Novartis), identified by LaMarche et al. (*J Med Chem* 2020, IC50 11 nM), is the clinical successor: its first-in-human Phase I trial (NCT03114319, 227 patients with advanced solid tumours) reported stable disease as the best monotherapy response and was terminated for business reasons, not safety, while combination trials with KRAS G12C, EGFR and PD-1 inhibitors continue. RMC-4630, BBP-398, JAB-3312 and JAB-3068 are in parallel development. The gap this paper attacks is the screening question for this target: can a docking screen rank allosteric SHP2 inhibitors at all — and does the pipeline even pick the right structure?

**Falsifiable hypothesis (one sentence):** CHEMBL4789817 inhibits SHP2 with an IC50 at or below TNO155's and at least 10-fold selectivity over SHP1.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-28: PubMed (TNO155, SHP099, SHP2 clinical trials), ClinicalTrials.gov (NCT03114319), RCSB PDB (5EHR, 9EIK), ChEMBL (target CHEMBL3864, live) and a 2025 review of SHP2 targeting in colorectal cancer (*World J Gastrointest Oncol* 2025;17:107380). Burden figures are GLOBOCAN 2022 estimates for Pakistan. The Islamic canon sweep (per the programme's standing rule) checked Ibn Sina's *Canon of Medicine* (Book II, materia medica; Book IV on swellings and tumours, waram) as a hypothesis source; no Canon-listed plant was docked in this run, and the classical literature is cited for the policy principle (hifz al-nafs, preservation of life), not as evidence for any molecule.

### 2.2 Molecular docking

Standardised AutoDock Vina protocol, exactly as Papers #1/#3: Vina 1.2.7, 22.5 Å cubic box, exhaustiveness 8, best of three poses reported, same grid for every compound. **Structure correction (this paper's central methods point):** the pipeline's automatic pick, PDB 9EIK (1.25 Å), is the isolated N-SH2 domain of SHP2 (T42A mutant) bound to a GAB1 phosphopeptide — it contains no allosteric pocket, and the reference drug TNO155 scored only −5.75 kcal/mol there, which is inconsistent with an 11 nM inhibitor. We therefore re-docked all five compounds on PDB 5EHR (full-length human SHP2 in complex with the allosteric inhibitor SHP099, 1.7 Å), grid centred on the co-crystallised SHP099 ligand at [22.42, 41.19, 4.70] via the pipeline's own `dock._ligand_center` (largest drug-like HETATM group, excluding cofactors and modified residues). Both runs are preserved: the 9EIK run in `dock-HP-126-2026-11-28.json` and the 5EHR re-dock in `dock-HP-126-2026-11-28-5EHR.json`. Only the 5EHR results are reported as the paper's findings; the 9EIK run is reported as the failure it was.

### 2.3 PAINS screen

RDKit PAINS filter applied to every test compound. All five docked compounds are PAINS-clean (zero alerts).

### 2.4 Honesty limits

Docking is not activity. Vina's scoring error is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No phosphatase assay, cell assay or animal data were generated in this paper. Phosphatase selectivity (SHP2 vs SHP1/PTP1B) was neither computed nor measured — it is the known failure mode of this target class. The measured IC50/Kd values quoted are ChEMBL records from different source assays, not head-to-head measurements.

## 3. Results

### 3.1 Docking: the comparison table (PDB 5EHR, correct allosteric pocket)

| Compound | Best affinity (kcal/mol) | Top-3 poses (kcal/mol) | Measured potency (ChEMBL) | MW | logP | PAINS |
|---|---|---|---|---|---|---|
| CHEMBL4789817 | **−9.93** | −9.93, −9.01, −7.88 | Kd 1.3 nM (pChEMBL 8.89) | 454.00 | 3.68 | none |
| CHEMBL5882319 | −8.96 | −8.96, −8.38, −7.62 | IC50 1.0 nM (pChEMBL 9.00) | 445.98 | 2.84 | none |
| CHEMBL4858291 | −8.46 | −8.46, −7.75, −7.10 | IC50 0.017 nM (pChEMBL 10.77) | 420.97 | 2.78 | none |
| TNO155 (QUERY, PubChem) | −7.92 | −7.92, −7.67, −7.54 | IC50 11 nM (LaMarche et al. 2020) | 421.96 | 2.17 | none |
| CHEMBL5792033 | −7.64 | −7.64, −7.56, −7.25 | IC50 0.9 nM (pChEMBL 9.05) | 436.97 | 2.08 | none |

All five compounds pass Lipinski's rule with zero violations. Tox21 kNN read-across maxima are low (0.097–0.344 across the set). All four ChEMBL compounds are unnamed (no preferred name, no development phase).

### 3.2 The wrong-structure run (PDB 9EIK, reported as a failure)

On 9EIK the same five compounds scored −6.40 (CHEMBL5882319), −6.12 (CHEMBL4789817), −5.93 (CHEMBL5792033), −5.75 (TNO155) and −5.44 (CHEMBL4858291) — compressed into a 0.96 kcal/mol band, with the reference drug fourth. An 11 nM inhibitor scoring −5.75 kcal/mol is the signature of a missing pocket, not a weak molecule. Had this run been reported without the correction, the paper would have concluded that no ChEMBL ligand beats TNO155 — the opposite of the corrected result. The correction changed the winner, the margin and the conclusion.

### 3.3 Comparison with published docking

No published Vina docking of these four ChEMBL compounds against SHP2 was found. The reference re-dock is consistent with the literature: TNO155 and SHP099 share the allosteric pocket, and the 5EHR structure is the standard template for this class. The 2025 colorectal-cancer review records the clinical state accurately: allosteric SHP2 inhibitors are in multicentre Phase I/II trials, monotherapy activity is modest, and the field has moved to combinations.

## 4. Discussion

### 4.1 The reframe: two failures, one paper

This paper contains two findings, and the second is more important than the first. First, on the correct structure, CHEMBL4789817 out-docks TNO155 by 2.01 kcal/mol — a margin just at the edge of Vina's noise band, with a top pose (−9.93) that is an outlier against its own second and third poses (−9.01, −7.88), so the margin should be read as ~1 kcal/mol, not 2. Second, and more useful: docking cannot rank these inhibitors at all. The measured potencies span 0.017 nM to 11 nM — a 650-fold range — while the docking scores span −9.93 to −7.64, and the most potent molecule by measurement (CHEMBL4858291, 0.017 nM) docks third. A screen that ranks by docking alone would promote the wrong lead and demote the best-measured binder. The paper's contribution is therefore a validated ranking procedure (correct structure + head-to-head assay) rather than a molecule.

### 4.2 Why the "win" must not be over-read

Four reasons. First, the 2.01 kcal/mol margin is at the edge of Vina noise, and the top pose is not reproduced by the second pose. Second, all five compounds are already sub- to low-nanomolar measured binders; the screen found no molecule that is both novel and dramatically better on measurement. Third, phosphatase selectivity is untested: the allosteric pocket is the reason SHP2 is druggable at all, but a molecule that also hits SHP1 (PTPN6, the immune brake) would be toxic in exactly the combinations now in trials. Fourth, TNO155's own clinical record — stable disease as best monotherapy response — warns that SHP2 inhibition alone is a weak lever; any lead here is a combination partner, not a monotherapy.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

All five compounds are PAINS-clean. The design constraint that does apply is selectivity: the validation assay must run SHP2, SHP1 and PTP1B side by side in the same plate, with SHP099 as the control, or the paper's claim is untested where it matters most.

### 4.4 Testable hypotheses

1. CHEMBL4789817 inhibits SHP2 with IC50 ≤ TNO155's in the same assay (falsifier: IC50 > 2× TNO155's).
2. CHEMBL4789817 is ≥10-fold selective for SHP2 over SHP1 and PTP1B (falsifier: selectivity <3-fold).
3. CHEMBL4858291's 0.017 nM IC50 reproduces head-to-head against TNO155 (falsifier: IC50 > 1 nM on re-measurement — the ChEMBL record may be an assay artefact).
4. CHEMBL4789817 suppresses ERK phosphorylation in a KRAS-mutant cell line at ≤100 nM (falsifier: no pERK suppression at 1 µM).
5. CHEMBL4789817 synergises with a KRAS G12C inhibitor in that cell line (falsifier: antagonism or additivity only — which would reframe it as a monotherapy candidate, not a combination partner).

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): recombinant SHP2, SHP1 and PTP1B phosphatase assays (DiFMUP substrate); IC50 for CHEMBL4789817, CHEMBL4858291, CHEMBL5882319 and TNO155 in one plate, triplicate, with SHP099 as control. Stage 2 (weeks 4–6): pERK western blot / HTRF in KRAS-mutant (H358, G12C) and EGFR-mutant cell lines at IC50 multiples. Stage 3 (weeks 7–9): combination matrix with a KRAS G12C inhibitor (synergy scoring) and HepG2 cytotoxicity. Stage 4 (weeks 10–12): mouse xenograft pilot only if stages 1–3 pass with selectivity ≥10-fold. The enzyme assay plus the selectivity panel is the only gate that matters for this paper's claim.

## 5. Limitations

1. Docking only: no phosphatase, cell or animal data were generated; the 2.01 kcal/mol margin is at the edge of Vina's ±1–2 kcal/mol noise and the top pose is an outlier.
2. The pipeline's first structure pick was wrong (9EIK); the correction was manual. Other papers in this series should audit their auto-picked structures the same way.
3. Single structure: docking used one SHP2 structure (5EHR); no MD or free-energy refinement was run.
4. Selectivity unknown: SHP1/PTP1B binding was neither computed nor measured — the first safety gate is untested.
5. Measured potencies are ChEMBL records from different source assays, not head-to-head measurements; the 0.017 nM record for CHEMBL4858291 in particular needs re-measurement.
6. The Pakistan burden figures are GLOBOCAN 2022 modelled estimates, not a complete count from a unified national registry (Pakistan has no unified national cancer registry).
7. Islamic-canon sweep: the full 23 volumes of Al-Razi's *Kitab al-Hawi* exist in English only in selections, and Ibn al-Nafis's commentary survives as an Arabic manuscript with only partial English translation; those texts were not read in full. No classical work was used as evidence for any molecule.
8. No local-market data: no SHP2 inhibitor is registered in Pakistan; availability and price were not checked.

## 6. Conclusion

On the correct allosteric structure, CHEMBL4789817 out-docks TNO155 on SHP2 by 2.01 kcal/mol — but the measured potencies show docking cannot rank these inhibitors, and the most potent measured binder docks third. The paper's durable result is the correction itself: the pipeline's first structure was the wrong domain, and auditing the structure changed the conclusion. Until the head-to-head phosphatase assay runs, nothing here is a treatment claim.

## 7. Policy implications

**Decision-maker:** the Drug Regulatory Authority of Pakistan (DRAP) and the Shaukat Khanum Memorial Cancer Hospital research office, with the Higher Education Commission's ORIC network. **Decision:** whether to fund a university-lab phosphatase assay panel for RAS-pathway targets, and whether to seek expanded-access or trial participation for SHP2 combinations. **Exact change:** DRAP/HEC should fund a 12-week head-to-head SHP2/SHP1/PTP1B assay panel for the four molecules in this paper, run at a university lab with the results published whether positive or negative — instead of waiting for a foreign sponsor's combination trial to reach Pakistan, which for a drug with no local registration is the default and means no access. **If the evidence reverses this:** if all four leads fail the selectivity gate (SHP2/SHP1 <3-fold), the panel should stop and the funds should move to KRAS-pathway trial access, not to more docking. **Islamic principle:** hifz al-nafs (preservation of life), defined by Al-Ghazali in *Al-Mustasfa min 'Ilm al-Usul* (c. 1109) and systematised by Al-Shatibi in *Al-Muwafaqat* — a cancer patient in Larkana has the same claim on a life-preserving assay as a patient in a trial centre abroad, and 'adl (justice, Qur'an 4:135) tests the policy by who it leaves out: a validation pipeline that only runs where the drug is already registered leaves Pakistan out by design. Ibn Sina's *Canon* (Book IV) discussed swellings and tumours (waram) as a category of disease to be observed and distinguished — the classical precedent for the method: observe, distinguish, and test.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author thanks the open-data providers — UniProtKB, ChEMBL, PubChem and the RCSB Protein Data Bank — without which this work would not exist.

## References

1. Chen YN, LaMarche MJ, Chan HM, et al. Allosteric inhibition of SHP2 phosphatase inhibits cancers driven by receptor tyrosine kinases. Nature. 2016;535(7610):148–152. doi:10.1038/nature18621. PMID: 27362227.
2. LaMarche MJ, Acker M, Argintaru A, et al. Identification of TNO155, an allosteric SHP2 inhibitor for the treatment of cancer. J Med Chem. 2020;63(22):13578–13594. doi:10.1021/acs.jmedchem.0c01170. PMID: 32910655.
3. Liu P, Chen J. Targeting SHP2: dual breakthroughs in colorectal cancer therapy — from signaling pathway modulation to immune microenvironment remodeling. World J Gastrointest Oncol. 2025;17(7):107380. doi:10.4251/wjgo.v17.i7.107380.
4. ClinicalTrials.gov. Dose finding study of TNO155 in adult patients with advanced solid tumors. NCT03114319. (Phase I, 227 patients; terminated for business reasons, not safety.)
5. Cancer burden epidemiological patterns and healthcare disparities across five major cancers in Pakistan. Discov Public Health. 2026. doi:10.1186/s12982-026-02844-8. (GLOBOCAN 2022: 185,748 new cases, 118,631 deaths; lung 9,464; colorectal 9,447.)
6. RCSB PDB entry 5EHR: non-receptor protein tyrosine phosphatase SHP2 in complex with allosteric inhibitor SHP099, 1.7 Å. RCSB Protein Data Bank. Accessed 2026-11-28.
7. RCSB PDB entry 9EIK: crystal structure of N-SH2 domain of SHP2 with T42A mutation bound to GAB1 tyrosine phosphorylated peptide, 1.25 Å. RCSB Protein Data Bank. Accessed 2026-11-28. (Cited as the wrong-structure failure, not as an allosteric template.)
8. UniProtKB Q06124: tyrosine-protein phosphatase non-receptor type 11 (SHP2/PTPN11), Homo sapiens. UniProt. Accessed 2026-11-28.
9. ChEMBL target CHEMBL3864: tyrosine-protein phosphatase non-receptor type 11, Homo sapiens; 43 bioactivities retrieved live 2026-11-28, including Kd 1.3 nM for CHEMBL4789817, IC50 1.0 nM for CHEMBL5882319, IC50 0.017 nM for CHEMBL4858291 and IC50 0.9 nM for CHEMBL5792033. ChEMBL, EMBL-EBI.
10. Al-Ghazali. Al-Mustasfa min 'Ilm al-Usul. c. 1109. (Defines the five necessities of the law, including hifz al-nafs.)
11. Al-Shatibi. Al-Muwafaqat fi Usul al-Shari'a. 14th c. (Systematises maqasid al-shariah.)
12. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Book IV on swellings and tumours; cited for the hifz al-nafs principle only.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-126-2026-11-28-5EHR.json` (re-dock on PDB 5EHR) and `hidden_files/dock-HP-126-2026-11-28.json` (pipeline run, including the wrong-structure 9EIK run preserved as a failure record). Compound identifiers: TNO155 (QUERY), CHEMBL4789817, CHEMBL5882319, CHEMBL4858291, CHEMBL5792033. No additional data were generated.
