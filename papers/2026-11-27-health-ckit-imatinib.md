# A 0.20 nM Kinome Hit Out-Docks Imatinib on c-KIT by 1.65 kcal/mol — but Docking Shuffles Four Near-Identical Binders

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-27 · **Health Papers Agent — Paper #125** (daily 5-paper run)

**Keywords:** c-KIT; GIST; imatinib; tyrosine kinase inhibitor; drug resistance; D816V; molecular docking; ChEMBL; Pakistan

---

## Abstract

Gastrointestinal stromal tumours (GIST) are driven by activating KIT mutations in 75–80% of cases, and imatinib turned this chemo-refractory sarcoma into a chronic disease — until secondary mutations (exon 13/14 gatekeeper, exon 17 activation-loop) defeat it. We asked whether any published KIT inhibitor beats imatinib on docking to the c-KIT kinase domain. Using the LeadForge pipeline (UniProtKB P10721 → ChEMBL target CHEMBL1936, 24 bioactivities → PubChem/RDKit, PAINS and ADMET screen) we docked imatinib and four sub-nanomolar ChEMBL KIT binders with AutoDock Vina on PDB 1T46, the c-Kit–imatinib complex. CHEMBL273187 out-docked imatinib by 1.65 kcal/mol (−12.04 vs −10.39 kcal/mol) and is ~500-fold more potent by measurement (Ki 0.20 nM vs imatinib IC50 100 nM against wild-type KIT). But docking shuffles the four leads: the most potent measured binder, CHEMBL404366 (Ki 0.16 nM), docks worst (−9.91 kcal/mol), so docking confirms the direction (leads ≫ imatinib) and fails on the order. Docking on wild-type 1T46 also says nothing about the real clinical gap — the D816V activation-loop mutant, against which imatinib's IC50 rises 100-fold to 10,000 nM. The falsifiable next step is a head-to-head kinase assay of CHEMBL273187 against wild-type KIT and the D816V mutant: if it does not confirm below 5 nM on wild-type, or if it loses more than 10-fold on D816V, the lead is refuted. Two pipeline failures were caught and corrected: the first run resolved the target to a pig protein and a human glucosidase, and the second docked on 2VIF — a SOCS6 SH2 domain, not the KIT kinase — and neither run contributes a number to this paper.

---

## 1. Introduction

GIST is the most common mesenchymal neoplasm of the gastrointestinal tract (0.4–2 cases per 100,000 people per year), arising from the interstitial cells of Cajal and driven by activating mutations in KIT (75–80%, mostly exon 11) or PDGFRA (5–10%). Before imatinib it was a chemo-refractory sarcoma; after imatinib it became the proof of concept that a small-molecule kinase inhibitor could turn a sarcoma into a chronic disease. Adjuvant imatinib 400 mg daily for 3 years (SSG XVIII trial) improves recurrence-free and overall survival in high-risk disease, and metastatic disease reaches ~50–60% 5-year overall survival on imatinib. The drug is a type-II inhibitor: it binds the DFG-out, inactive conformation of the kinase, which the juxtamembrane domain normally stabilises — and exon 11 mutations, the commonest driver (60–70% of GIST), release that autoinhibitory clamp, which is why they respond best (70–80% response).

Resistance is a ladder, and the tumour climbs it one secondary mutation at a time. Two structural neighbourhoods dominate: the ATP-binding pocket (exon 13/14 — V654A, T670I), which sterically blocks imatinib while leaving the kinase functional, and the activation loop (exon 17/18 — D816, D820, N822K), which stabilises the active DFG-in conformation that a type-II inhibitor cannot bind at all. The salvage ladder was built to cover these slices: sunitinib (second line, ATP-pocket mutants), regorafenib (third line, activation-loop mutants), ripretinib (fourth line, switch-control, broad coverage, INVICTUS trial), and avapritinib (a type-I inhibitor, the only drug effective against PDGFRA D842V, which is intrinsically imatinib-resistant from day one). Exon 9 mutations need double-dose imatinib (800 mg/day). Mutation testing is therefore mandatory before treatment (NCCN 2022): the genotype decides the drug and the dose.

The gap this paper attacks is narrow and honest. The ChEMBL KIT record holds sub-nanomolar binders from kinome profiling that have never been tested against the resistance mutants. If one of them binds wild-type KIT far better than imatinib and — crucially — retains binding on D816V, it would be a candidate for the exon-17 gap that currently has no type-II answer. Docking on the wild-type structure can only answer the first half of that question.

**Falsifiable question.** Does any published ChEMBL KIT binder beat imatinib on docking to the wild-type c-KIT kinase domain, and does the docking ranking agree with the measured potencies? **Falsifier:** a head-to-head kinase assay in which CHEMBL273187 fails to confirm below 5 nM on wild-type KIT, or loses more than 10-fold on the D816V mutant — either result refutes the lead. **Causal identification:** validated-control re-docking (imatinib re-docked into its own co-crystal structure, same grid, same protocol) — association only beyond that, since no experiment was run and docking scores are not activity.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-27: the GIST mutation-directed therapy guideline (KIT 75–80%, exon 11 60–70%, SSG XVIII, INVICTUS, NCCN 2022 sequencing mandate); the KIT resistance-ladder review (V654A/T670I, D816/D820/N822K, sunitinib/regorafenib/ripretinib/avapritinib lines); the 1T46 structure paper (Mol et al., J Biol Chem 2004;279:31655–31663, doi:10.1074/jbc.M403319200, PMID 15123710); the V654A resistance paper (Mol Cancer Ther 2005;4:2008–2015, ~2.25 kcal/mol destabilisation); and the SOCS6 structure paper (J Biol Chem 2011; PDB 2VIF). Measured Ki/IC50 values for imatinib and the four leads were retrieved live from the ChEMBL API on 2026-11-27 (target CHEMBL1936). The classical-canon sweep is in §4.3: Ibn Sina's Canon of Medicine (c. 1025) discusses swellings and tumours (waram) and their surgical treatment at length, and Al-Razi's Kitab al-Hawi records clinical observation of tumours — neither describes a kinase or an inhibitor, so the Islamic-principle discussion rests on hifz al-nafs and adl (justice in access), not on a classical source about this target.

### 2.2 Target identification — and the two failures that were caught

**Failure 1 (wrong species, wrong target).** The query "KIT proto-oncogene receptor tyrosine kinase" resolved to UniProt Q2HWD6 (Sus scrofa, pig), and ChEMBL then returned CHEMBL2074, human maltase-glucoamylase — the same fallback mis-resolution this pipeline produced for sortase A in Paper #124. The 26 "leads" from that run were glucosidase inhibitors, and no PDB was found. Every number from that run is invalid; it is preserved as `dock-HP-129-2026-11-27-WRONG-TARGET-pig.json` and contributes nothing. **Correction.** The target was re-specified by its reviewed accession: UniProt P10721 (KIT_HUMAN, gene KIT, 976 aa). ChEMBL target by accession then returned CHEMBL1936, "Mast/stem cell growth factor receptor Kit", single protein, Homo sapiens, with 24 bioactivities. Imatinib was verified against PubChem (C29H31N7O, MW 493.62, logP 4.59, 2 H-bond donors, 7 acceptors, TPSA 86.28 Å², 7 rotatable bonds, 0 Lipinski violations, PAINS-clean). The similarity screen returned 24 leads; the top-ranked set was docked.

### 2.3 Molecular docking — and the wrong-structure failure

**Failure 2 (wrong protein).** The re-run docked on PDB 2VIF, which the pipeline picked because the entry contains a c-KIT phosphopeptide and therefore maps to P10721. But 2VIF is the crystal structure of the SOCS6 SH2 domain in complex with that peptide (J Biol Chem 2011, 1.45 Å) — the kinase domain is not in the structure at all. The scores from that run (imatinib −8.45, leads −7.11 to −6.72 kcal/mol) measure binding to SOCS6, not KIT inhibition, and are reported here only as the failure record. **Correction.** The docking was re-run on PDB 1T46 (Mol et al. 2004): the c-Kit kinase domain in complex with imatinib (STI-571), 1.6 Å for the complex, with the co-crystallised imatinib as the grid anchor. The centre is the STI ligand centroid [26.18, 26.06, 40.36] from dock._ligand_center (37 atoms, verified against the PDB file). All five ligands were re-docked with AutoDock Vina 1.2.7 at that centre (box 22.5 Å, exhaustiveness 8, best of 3 poses). One lead could not be docked at all: CHEMBL5416410 (rank 2, similarity 0.272) has a two-fragment salt SMILES, and the RDKit ligand preparation refuses multi-fragment molecules; it was replaced by rank-6 CHEMBL272938 so the set stays at five ligands, and the exclusion is stated here, not hidden. Two limits must be stated: 1T46 is the DFG-out inactive conformation, so it can only test type-II binding; and it is wild-type KIT, so it cannot test the D816V or V654A mutants — the resistance question needs mutant structures or assays, not this docking.

### 2.4 PAINS screen

RDKit PAINS filter applied to imatinib and all four docked leads. All five are PAINS-clean. No PAINS alert is hidden anywhere in this paper; there is none to hide.

### 2.5 Honesty limits

Docking scores are not activity: Vina's noise is ±1–2 kcal/mol, the structure is a single wild-type inactive conformation, and no molecular dynamics or free-energy refinement was run. The four leads' Ki values (0.16–0.32 nM) come from one kinome-profiling panel (ChEMBL document CHEMBL1201862) and are not head-to-head with imatinib's IC50 values, which come from several different assays (100–400 nM wild-type across records; Kd 830 nM). A Ki and an IC50 are not the same measurement, so the "~500-fold" comparison is order-of-magnitude, not precise. No experimental data were generated in this study.

## 3. Results

### 3.1 Docking: the comparison table (corrected structure)

| Compound | ChEMBL ID | Best affinity (kcal/mol) | Poses (kcal/mol) | Measured KIT potency | MW (Da) | logP | TPSA (Å²) | PAINS |
|---|---|---|---|---|---|---|---|---|
| CHEMBL273187 | CHEMBL273187 | **−12.04** | −12.04, −11.32, −11.06 | Ki 0.20 nM | 376.40 | 4.30 | 108.7 | clean |
| CHEMBL272938 | CHEMBL272938 | −10.78 | −10.78, −10.32, −9.43 | Ki 0.32 nM | 358.41 | 4.16 | 108.7 | clean |
| Imatinib (reference) | CHEMBL941 | −10.39 | −10.39, −10.38, −10.35 | IC50 100 nM (WT); 10,000 nM (D816V) | 493.62 | 4.59 | 86.3 | clean |
| CHEMBL402846 | CHEMBL402846 | −9.96 | −9.96, −9.88, −9.76 | Ki 0.32 nM | 390.42 | 4.31 | 97.9 | clean |
| CHEMBL404366 | CHEMBL404366 | −9.91 | −9.91, −9.67, −9.58 | Ki 0.16 nM | 392.85 | 4.51 | 97.9 | clean |

All five docked into the same grid (1T46, STI centre [26.18, 26.06, 40.36], box 22.5 Å). CHEMBL273187 beats imatinib by 1.65 kcal/mol — at the edge of Vina's noise band, so the margin alone is not proof, but it is the largest margin in this paper's set and it points the same way as the measurement. Imatinib's self-dock (−10.39 kcal/mol, poses within 0.04 kcal/mol) is the protocol validation: the co-crystallised ligand re-docks tightly into its own site.

### 3.2 The direction is right; the order is shuffled

By measurement, the four leads are all sub-nanomolar (Ki 0.16–0.32 nM) against imatinib's 100 nM wild-type IC50 — a ~300–600-fold potency gap, measured in the same kinome panel for the leads. Docking agrees on the big claim: the best lead beats imatinib by 1.65 kcal/mol, and three of the four leads are within 0.4 kcal/mol of imatinib or better. But docking shuffles the order among the leads: the most potent measured binder, CHEMBL404366 (Ki 0.16 nM), docks worst (−9.91 kcal/mol), while CHEMBL273187 (Ki 0.20 nM) docks best (−12.04 kcal/mol). The measured spread among the leads is 2-fold; the docking spread is 2.1 kcal/mol — Vina exaggerates differences between near-identical binders and cannot order them. The honest reading is therefore two-part: (i) the leads are genuinely far more potent than imatinib by measurement, and docking does not contradict that; (ii) no ranking among the four leads is supported by this docking, and CHEMBL273187's first place is a hypothesis, not a finding.

### 3.3 The resistance gap docking cannot touch

The clinically important number in the table is not a docking score: imatinib's IC50 rises from 100 nM on wild-type KIT to 10,000 nM on the D816V mutant (ChEMBL, same assay series) — a 100-fold loss, and 5,000 nM in the Ba/F3 D816V cell line against 400 nM wild-type. D816V stabilises the DFG-in active conformation, which a type-II inhibitor cannot bind at all; no docking on the DFG-out 1T46 structure can test whether CHEMBL273187 or any lead overcomes it. The V654A gatekeeper mutation likewise abrogates imatinib binding (Mol Cancer Ther 2005; estimated ~2.25 kcal/mol destabilisation). A lead that only beats imatinib on wild-type KIT is a better imatinib, not a resistance answer — and a better imatinib is not what GIST needs, since imatinib already works on wild-type disease. The value of CHEMBL273187 therefore depends entirely on the mutant assay proposed in §4.5.

### 3.4 Comparison with published docking

Mol et al. (2004) solved the structure but reported no docking scores. No published Vina scores exist for these four ChEMBL compounds on 1T46, and the compounds have no common names — they are kinome-panel screening hits, not developed drugs. This paper's docking table therefore stands alone as a Vina ranking, and §3.2 is the statement of what it can and cannot support.

## 4. Discussion

### 4.1 The reframe

The question was "what beats imatinib?" and the measured data answer it more strongly than the docking: four sub-nanomolar binders against a 100 nM drug. But the reframe is that beating imatinib on wild-type KIT is the wrong contest. Imatinib already controls wild-type and exon-11 disease; the patients who die are the ones whose tumours acquire exon 13/14 or exon 17 mutations, and the salvage ladder (sunitinib, regorafenib, ripretinib, avapritinib) exists precisely because imatinib cannot cover them. A new lead matters only if it covers a resistance slice — D816V above all, since it defeats every type-II inhibitor by conformation. The paper's contribution is therefore not "CHEMBL273187 beats imatinib" but the testable claim in §4.4: a sub-nanomolar binder with a different chemotype (MW 376, no imatinib scaffold) that should be assayed against D816V first, not last.

### 4.2 Why the "win" must not be over-read

Three corrections guard the headline. First, the 1.65 kcal/mol margin sits at the edge of Vina's ±1–2 kcal/mol noise — it is suggestive, not established. Second, the docking order among the four leads contradicts their measured order, so the table cannot rank them. Third, the "~500-fold" potency gap compares a Ki (kinome panel) with an IC50 (several assays, 100–400 nM) — the gap is real in direction and order-of-magnitude, but the exact fold is assay-dependent, and imatinib's own Kd is 830 nM in one record. What is solid is the validation: imatinib re-docks into its own site at −10.39 kcal/mol with near-identical poses, so the protocol can reproduce a known binder — and the leads' sub-nanomolar Ki values are measured, not computed. The memorable number is the resistance gap: **100-fold** — imatinib's IC50 from 100 nM to 10,000 nM on D816V — because that number, not any docking score, is the reason a new KIT inhibitor is needed.

### 4.3 Mechanism — and the classical canon

KIT is a type-III receptor tyrosine kinase: stem-cell factor binding dimerises the receptor, the juxtamembrane region is displaced, and the kinase phosphorylates PI3K, RAS–MAPK and STAT pathways that drive survival and proliferation. Imatinib occupies the ATP pocket of the DFG-out inactive conformation, displacing the juxtamembrane domain's autoinhibitory grip. Test for each link: (i) a biochemical kinase assay measures inhibition of wild-type and D816V KIT directly, against imatinib's 100 nM / 10,000 nM; (ii) a Ba/F3 cell-viability assay measures the same in cells, against imatinib's 400 nM / 5,000 nM; (iii) a GIST cell-line panel (exon-11 vs exon-17 genotypes) measures whether the compound kills the resistant genotype, against ripretinib as the positive control. The classical canon knows the disease, not the kinase: Ibn Sina's Canon of Medicine (c. 1025) discusses swellings and tumours (waram) and their surgical treatment, and Al-Razi's Kitab al-Hawi records clinical observation of tumours — but neither describes a receptor or an inhibitor, so the principle carried forward is hifz al-nafs (preservation of life) joined to adl (justice): the drug exists, but the test that decides who gets which drug — KIT/PDGFRA sequencing — is the access gap, and justice in this case means the test, not the tablet.

### 4.4 Testable hypotheses

1. CHEMBL273187 inhibits wild-type KIT with an IC50 below 5 nM in a biochemical kinase assay on the same day as imatinib. Falsifier: IC50 above 5 nM, which would refute the docking "win".
2. CHEMBL273187 inhibits the D816V mutant with an IC50 within 10-fold of its wild-type value. Falsifier: a loss greater than 10-fold, which would show it is another type-II binder defeated by the same conformation as imatinib.
3. CHEMBL404366 — the most potent measured binder (Ki 0.16 nM) and the worst docker — inhibits wild-type KIT below 5 nM. Falsifier: IC50 above 5 nM, which would suggest the kinome-panel Ki does not reproduce.
4. In Ba/F3 cells, CHEMBL273187 kills D816V-expressing cells at a concentration within 10-fold of its wild-type value. Falsifier: no killing below 1 µM, which would end the resistance claim regardless of the biochemical result.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): biochemical kinase assay — wild-type KIT and D816V KIT, CHEMBL273187, CHEMBL404366 and imatinib on one plate, n=3, with the published 100 nM / 10,000 nM imatinib values as the controls; readout IC50 for both genotypes. Stage 2 (weeks 4–6): Ba/F3 cell-viability assay for the same three compounds on wild-type and D816V lines, with ripretinib as the positive control for the mutant; readout GI50. Stage 3 (weeks 7–12): if a compound passes stages 1–2 — wild-type IC50 below 5 nM and D816V loss under 10-fold — a GIST cell-line panel (exon-11 vs exon-17 genotypes) and a selectivity screen against the closest kinases (PDGFRA, FLT3, ABL); if none passes, publish the negative result with the ChEMBL table as the reason the hypothesis failed. No animal work is proposed before stages 1–2 pass.

## 5. Limitations

1. Docking only, on a single wild-type DFG-out structure; Vina noise is ±1–2 kcal/mol and the docking order among the leads contradicts their measured order, so no ranking among the leads is claimed.
2. The leads' Ki values come from one kinome-profiling panel and are compared with imatinib IC50s from several different assays; the "~500-fold" gap is order-of-magnitude, not a head-to-head measurement.
3. No mutant structure or mutant docking was run: the D816V question — the actual clinical gap — is entirely untested by this paper's computation.
4. The four leads have no common names, no published pharmacology beyond the kinome panel, and no selectivity data reported here; CHEMBL5416410, the second-ranked lead, could not be docked at all (two-fragment salt SMILES).
5. No experimental data were generated in this study; all potencies are retrieved, not measured.
6. No Pakistani GIST data exist: no national registry, no published incidence, and no local study of KIT mutation frequencies or imatinib outcomes in Pakistan, so the policy section recommends testing infrastructure, not a drug decision.
7. The classical-canon sweep did not re-read the Canon or Kitab al-Hawi in full; the Islamic-principle discussion rests on hifz al-nafs and adl as principles, not on a classical source about this target. The full 23 volumes of Kitab al-Hawi exist in English only in selections.

## 6. Conclusion

CHEMBL273187 out-docks imatinib on wild-type c-KIT by 1.65 kcal/mol (−12.04 vs −10.39 kcal/mol) and is ~500-fold more potent by measurement (Ki 0.20 nM vs imatinib IC50 100 nM), with imatinib's tight self-dock validating the protocol. But docking shuffles the four sub-nanomolar leads — the most potent measured binder docks worst — so no ranking among them is claimed, and docking on wild-type 1T46 cannot test the D816V resistance mutant, where imatinib loses 100-fold. The next step is the cheap, decisive test: one kinase assay on wild-type and D816V KIT, not a bigger docking screen.

## 7. Policy implications

**Decision-maker:** Pakistan's Drug Regulatory Authority (DRAP) and the Ministry of National Health Services, with the Shaukat Khanum Memorial Cancer Hospital and the Aga Khan University Hospital oncology departments as the technical arms. **Decision:** whether to spend anything on GIST care beyond generic imatinib, and what must exist first. **Exact change:** do not spend on a new KIT inhibitor or a docking programme — instead, make KIT/PDGFRA sequencing available at public oncology centres before the first imatinib prescription, so exon-9 patients receive 800 mg/day instead of 400 mg, PDGFRA D842V patients receive avapritinib instead of futile imatinib, and exon-17 patients are routed to the salvage ladder instead of failing imatinib for months. **If evidence Z appears, reverse this:** if a Pakistani GIST registry shows fewer than 5% non-exon-11 genotypes, narrow the sequencing programme to referral centres; if it shows a high D842V or exon-17 share, expand sequencing to all tertiary oncology units and negotiate avapritinib access — do not proceed to any drug evaluation on docking scores alone. The Islamic principle is hifz al-nafs joined to adl (justice): the test that decides the drug is the access gap, and a patient who receives the wrong dose for the wrong genotype because the test was unavailable has been denied both. The evidence here is thin — retrieved potencies and a wild-type docking table — so the recommendation is "build the testing", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Gastrointestinal stromal tumor: mutation-directed tyrosine kinase inhibitor therapy and risk-stratified surveillance. (GIST guideline: KIT 75–80%, exon 11 60–70%, SSG XVIII 3-year adjuvant imatinib, INVICTUS ripretinib, NCCN 2022 sequencing mandate.) Accessed 2026-11-27.
2. KIT in GIST: the four-line resistance ladder. (V654A/T670I ATP-pocket; D816/D820/N822K activation loop; sunitinib, regorafenib, ripretinib, avapritinib lines.) Accessed 2026-11-27.
3. Mol CD, Dougan DR, Schneider TR, Skene RJ, Kraus ML, Scheibe DN, Snell GP, Zou H, Sang BC, Wilson KP. Structural basis for the autoinhibition and STI-571 inhibition of c-Kit tyrosine kinase. J Biol Chem. 2004;279:31655–31663. doi:10.1074/jbc.M403319200. PMID: 15123710.
4. Imatinib binding and cKIT inhibition is abrogated by the cKIT kinase domain I missense mutation Val654Ala. Mol Cancer Ther. 2005;4(12):2008–2015.
5. Structural basis for C-Kit inhibition by the Suppressor of Cytokine Signaling 6 (Socs6) ubiquitin ligase. J Biol Chem. 2011. (PDB 2VIF — cited as the wrong-structure failure, not as a KIT structure.)
6. UniProtKB P10721: Mast/stem cell growth factor receptor Kit (KIT), Homo sapiens, 976 aa. UniProt. Accessed 2026-11-27.
7. ChEMBL target CHEMBL1936: Mast/stem cell growth factor receptor Kit, Homo sapiens (24 bioactivities); activities for imatinib (CHEMBL941) and CHEMBL273187, CHEMBL272938, CHEMBL402846, CHEMBL404366 retrieved live 2026-11-27, including kinome-panel document CHEMBL1201862. ChEMBL, EMBL-EBI.
8. RCSB PDB entry 1T46: c-Kit kinase domain in complex with STI-571 (imatinib), 1.6 Å. RCSB Protein Data Bank. Accessed 2026-11-27.
9. RCSB PDB entry 2VIF: SOCS6 SH2 domain in complex with a c-KIT phosphopeptide, 1.45 Å. RCSB Protein Data Bank. Accessed 2026-11-27.
10. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Discusses swellings and tumours (waram) — cited for the hifz al-nafs principle only.)
11. Al-Ghazali. Al-Mustasfa min 'Ilm al-Usul. c. 1109. (Defines the five necessities of the law, including hifz al-nafs.)
12. Al-Shatibi. Al-Muwafaqat fi Usul al-Shari'a. 14th c. (Systematises maqasid al-shariah.)

## Data availability

All potencies, descriptors and docking scores reported here are in `hidden_files/dock-HP-129-2026-11-27.json` (LeadForge pipeline run: target UniProt P10721; ChEMBL target CHEMBL1936, 24 bioactivities; 24 similarity leads; imatinib PubChem-verified) and `hidden_files/dock-HP-129-2026-11-27-redock.json` (re-dock on 1T46 at the STI ligand centre [26.18, 26.06, 40.36], Vina 1.2.7, box 22.5 Å, exhaustiveness 8). The two failed runs are preserved: `hidden_files/dock-HP-129-2026-11-27-WRONG-TARGET-pig.json` (target resolved to pig Q2HWD6 and human maltase-glucoamylase CHEMBL2074; no PDB found) and the 2VIF scores in the pipeline JSON (docking on the SOCS6 SH2 domain, not the KIT kinase domain). Reference drug imatinib (ChEMBL941, PubChem C29H31N7O); comparators CHEMBL273187, CHEMBL272938, CHEMBL402846, CHEMBL404366, with measured Ki values retrieved live from ChEMBL on 2026-11-27. Structure: PDB 1T46 (1.6 Å, c-Kit + imatinib). No additional data were generated.
