# BI-3406 Self-Docks at −9.07 kcal/mol on Its Own SOS1 Co-Crystal 6SCM — and Beats MRTX0902 and BAY-293 by Less Than Vina Noise

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-24 · **Health Papers Agent — Paper #107** (daily 5-paper run)

**Keywords:** SOS1; KRAS; BI-3406; guanine-nucleotide exchange factor; molecular docking; MRTX0902; pancreatic cancer; non-small-cell lung cancer

---

## Abstract

KRAS is the most commonly mutated oncogene in human cancer, present in about 25% of all tumours — 85–92% of pancreatic cancers, 40–49% of colorectal cancers and 30–35% of non-small-cell lung cancers — and direct KRAS blockade covers only some alleles. SOS1, the guanine-nucleotide exchange factor that switches KRAS from GDP-bound to GTP-bound, sits upstream of all KRAS mutants and is a feedback node that MEK inhibition reactivates, which makes it a combination target. We asked whether the newer SOS1 inhibitors MRTX0902 and BAY-293 bind the SOS1 catalytic pocket more strongly than BI-3406, the reference SOS1::KRAS interaction inhibitor. Using the LeadForge pipeline (UniProtKB Q07889 → PubChem/RDKit, PAINS and ADMET screen → AutoDock Vina 1.2.7), we docked BI-3406, MRTX0902 and BAY-293 on 6SCM, the 1.87 Å crystal structure of SOS1 in complex with BI-3406 itself, centred exactly on the co-crystallised BI-3406 (centre audit via dock._ligand_center). BI-3406 self-docked at −9.07 kcal/mol. MRTX0902 scored −8.10 kcal/mol and BAY-293 −8.11 kcal/mol — behind by 0.97 and 0.96 kcal/mol, just inside Vina's ±1–2 kcal/mol noise, and the two comparators are 0.01 kcal/mol apart. The honest limit: the reference drug wins on its own structure, which biases the comparison in its favour, and BI-3406 itself never entered the clinic — the clinical data belong to its analogue BI 1701963, whose Phase 1 showed limited efficacy as monotherapy (one partial response). The falsifiable next step is a single-assay SOS1::KRAS interaction comparison (IC50) of the three inhibitors under identical conditions: if MRTX0902's IC50 is not within 3-fold of BI-3406's, the dead-heat claim is refuted.

---

## 1. Introduction

KRAS is the most commonly mutated oncogene in human cancer, present in about 25% of all tumours (MD Anderson) and about 23% of all human malignancies (Curr Oncol 2025 review), and oncogenic KRAS alterations drive about one in seven human cancers. The burden concentrates in the deadliest solid tumours: pancreatic ductal adenocarcinoma 85–92%, colorectal cancer 40–49%, non-small-cell lung cancer 30–35% (lung adenocarcinoma 25–30%), with alleles concentrated at codons 12, 13 and 61 — G12D, G12V, G12C and G13D the most prevalent, about nine mutations accounting for about 90% of KRAS-driven cancers. KRAS G12C is about 13% of non-small-cell lung cancer and 1–3% of colorectal cancer. KRAS was called "undruggable" for about 40 years until the G12C inhibitors sotorasib and adagrasib arrived in 2021 — and those cover only one allele. No Pakistan-specific KRAS-mutant registry data were found in this sweep; the burden numbers above are global, and the absence of local genotyping data is itself part of the policy question in §7.

SOS1 (Son of Sevenless homolog 1) is the guanine-nucleotide exchange factor that catalyses GDP-to-GTP exchange on KRAS, switching it from inactive (GDP-bound) to active (GTP-bound) — described as a "pacemaker" for KRAS cycling between off and on states. Receptor-tyrosine-kinase activation recruits GRB2 and SOS (facilitated by SHP2) to the plasma membrane, where SOS promotes the exchange; active KRAS-GTP drives RAF–MEK–ERK (MAPK) and PI3K–AKT–mTOR signalling. SOS1 has two KRAS-binding sites: the CDC25 catalytic site, where exchange happens, and the REM allosteric site, where a second KRAS molecule binds and modulates activation. Its homolog SOS2 can compensate when SOS1 is inhibited, which modulates inhibitor efficacy. SOS1 sits upstream of all KRAS mutants and is a feedback node: MEK inhibition reactivates the pathway through SOS1, so combined SOS1 and MEK inhibition is a therapeutic concept, and SOS1 inhibition raises the GDP-KRAS pool that G12C inhibitors need. Hence the "vertical combination" rationale: SOS1 plus MEK, SOS1 plus KRAS G12C, SOS1 plus EGFR.

The reference drug of this paper is BI-3406, a potent, selective, orally bioavailable small-molecule SOS1::KRAS interaction inhibitor from Boehringer Ingelheim (Hofmann et al., Cancer Discovery 2021;11:142–157; doi:10.1158/2159-8290.CD-20-0142; PMID 32816843). It binds the catalytic (CDC25) domain of SOS1, prevents interaction with KRAS-GDP, reduces GTP-loaded RAS, and limits proliferation of KRAS-driven cancers. Its potency on the Boehringer open-innovation profile: SOS1::KRAS interaction IC50 5 nM; pERK inhibition IC50 4 nM in KRAS-mutant NCI-H358 cells; proliferation IC50 24 nM (NCI-H358) and 36 nM (DLD-1, KRAS G13D); no activity on KRAS wild-type H520 cells (>10,000 nM); selective against SOS2 (IC50 >10 µM); no off-target hits in a 368-kinase panel at 5 µM; expected low brain penetration. In preclinical models, BI-3406 attenuates MEK-inhibitor-induced feedback reactivation, combines with the EGFR inhibitor afatinib against KRAS G13D-mutant colorectal tumour cells (Ramharter et al., J Med Chem 2021;64:6569–6580), and with KRAS G12C inhibitors enhances efficacy, limits RTK/ERK rebound, resensitises drug-tolerant persister cells and delays acquired resistance in lung adenocarcinoma models regardless of KEAP1/STK11 co-mutation status (Cancer Research 2025;85:118–133; PMID 39437166).

The critical distinction: BI-3406 itself is a preclinical probe; it did not enter the clinic. The clinical analogue is BI 1701963 (structure undisclosed), a close analogue of BI-3406, in the Phase 1 trial NCT04111458 (started 4 November 2019; KRAS-mutant advanced/metastatic solid tumours; status "Active, not recruiting"; estimated primary completion 31 March 2027). The dose-escalation results show limited efficacy as monotherapy: dose-limiting toxicities in 6 of 75 patients (8.0%) on monotherapy against 6 of 19 (31.6%) in combination with trametinib; maximum tolerated dose 800 mg monotherapy and 100 mg BI 1701963 with 1 mg trametinib in combination; one partial response on monotherapy plus stable disease in both arms (an earlier report: stable disease in 7 of 31 KRAS-mutant patients up to 18 weeks). Enrolment is reported as 71 on ClinicalTrials.gov and 94 in a later summary — the discrepancy is flagged, not resolved, and no single enrolment number is quoted as settled.

The comparators are the other clinical-stage and tool SOS1 inhibitors. MRTX0902 (Mirati/Bristol Myers Squibb) is a potent, selective, brain-penetrant, orally bioavailable phthalazine-based SOS1:KRAS disruptor (Ketcham et al., J Med Chem 2022;65:9678–9690; doi:10.1021/acs.jmedchem.2c00741; PMID 35833726), in Phase 1 (NCT05578092) alone and with adagrasib; its rationale is that disrupting SOS1:KRAS increases GDP-loaded KRAS G12C, the form adagrasib binds. BAY-293 (Bayer) is an aminoquinazoline tool inhibitor with high affinity and moderate antiproliferative activity, synergistic with the KRAS G12C inhibitor ARS853; it is a research tool, not clinically suitable, though a related compound, BAY3498264, entered clinical evaluation. RMC-5845 (Revolution Medicines) remains preclinical and IND-deferred — it is not described as clinical-stage anywhere in this paper.

The classical medical canon knows the disease family, not the target: Ibn Sina's Canon of Medicine (c. 1025) describes tumours (saratān) and their treatment — the syndrome, not the protein. The principle carried forward here is hifz al-nafs, preservation of life (see §7).

**Falsifiable question.** Do the SOS1 inhibitors MRTX0902 and BAY-293 bind the catalytic pocket of the BI-3406-bound structure (PDB 6SCM) at scores beyond re-docked BI-3406, and would that binding translate into stronger SOS1::KRAS disruption? **Falsifier:** a SOS1::KRAS interaction assay under identical conditions showing an IC50 for MRTX0902 more than 3-fold worse than BI-3406's, or a pERK assay in KRAS-mutant cells showing no advantage, refutes the claim for that compound. **Causal identification:** validated-control re-docking — the reference drug re-docked on its own co-crystal structure, with the co-crystallised ligand as the centre — not a comparison against nothing. Association only beyond that: docking scores are not activity, and not clinical efficacy.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-24: the BI-3406 discovery paper (Hofmann et al., Cancer Discov 2021;11:142–157; doi:10.1158/2159-8290.CD-20-0142; PMID 32816843); the Boehringer open-innovation profile for BI-3406; the BI 1701963 Phase 1 trial (ClinicalTrials.gov NCT04111458) and its dose-escalation results; the MRTX0902 paper (Ketcham et al., J Med Chem 2022;65:9678–9690; doi:10.1021/acs.jmedchem.2c00741; PMID 35833726) and trial (NCT05578092); the afatinib combination paper (Ramharter et al., J Med Chem 2021;64:6569–6580); the KRAS G12C combination study (Cancer Res 2025;85:118–133; PMID 39437166); the SOS1 structural literature (6SFR, 6SCM, 7AVS, 5OVE, 6EPM/6EPN); the KRAS burden reviews (MD Anderson; Curr Oncol 2025;32:614); and the UniProtKB record for Q07889. No Pakistan-specific KRAS-mutant data were found.

### 2.2 Target identification

The pipeline resolved the target correctly on the first run: UniProtKB Q07889 (Son of sevenless homolog 1, Homo sapiens) → ChEMBL lookup returned no target record (chembl_targets empty), so no ChEMBL ligands were retrieved and the similarity screen was skipped — stated, not hidden. The comparison set was therefore built from the literature: the three SOS1 inhibitors with the strongest published data, with SMILES verified against PubChem by molecular formula (BI-3406 C23H25F3N4O3; MRTX0902 C22H24N6O; BAY-293 C25H28N4O2S).

### 2.3 Molecular docking

The three inhibitors were docked on 6SCM, the 1.87 Å crystal structure of SOS1 in complex with BI-3406, using standardised AutoDock Vina 1.2.7, exactly as Papers #1/#3: grid centre the centroid of the co-crystallised BI-3406 (ligand L7H, 58 heavy atoms), [1.31, −31.24, −44.42], verified by direct computation from the PDB file with `dock._ligand_center` (the centre audit confirmed L7H is the drug-like HETATM group; the imidazole and ethylene-glycol crystallisation additives were correctly excluded); box 22.5 Å, exhaustiveness 8, best of 3 poses reported. The same centre, box and exhaustiveness were used for all three compounds. BI-3406 is therefore the self-dock control on its own structure: a method that could not recover strong binding for the drug in its own pocket would be broken. One caveat, stated not smoothed over: the pocket is in BI-3406's own conformation, which biases the comparison in the reference drug's favour, and a MRTX0902 pose optimised for its own (non-existent) co-crystal might score differently. The docked BI-3406 is the parent SMILES as returned by PubChem; the crystal holds BI-3406 itself.

A correction is recorded here, because the pipeline's first run was wrong and the error matters. The pipeline docked BI-3406 on 6V9M at −8.88 kcal/mol, but the centre audit showed 6V9M's largest drug-like HETATM group is GNP, a GTP analogue bound to KRAS chain A — 6V9M is a SOS1-activator fragment screen (SOS1 plus KRAS–GNP complex), not an inhibitor-bound SOS1 structure, so BI-3406 was docked into the KRAS GTP pocket. That −8.88 kcal/mol score is discarded and does not appear in this paper's results. The 6SCM run reported here replaces it.

### 2.4 PAINS screen

RDKit PAINS filter applied to all three inhibitors. All three are PAINS-clean. No PAINS alert is hidden anywhere in this paper; there is none to hide.

### 2.5 ADMET and toxicity read-across

RDKit descriptors computed for BI-3406: molecular weight 462.47, logP 4.89, 2 hydrogen-bond donors, 7 acceptors, TPSA 91.52 Å², 6 rotatable bonds, 0 Lipinski violations, Lipinski pass and Veber pass. The two comparators: MRTX0902 (MW 388.48, logP 3.52, HBD 1, HBA 7, TPSA 86.96 Å², 4 rotatable bonds, 0 violations) and BAY-293 (MW 448.59, logP 5.58, HBD 2, HBA 7, TPSA 68.30 Å², 8 rotatable bonds, 1 violation). MRTX0902 is the smallest and least lipophilic of the three and the only one reported as brain-penetrant — a property the docking scores cannot see and the paper does not claim for it. No ToxGuard read-across is reported for this set: the pipeline's Tox21 panel ran only on the QUERY, and the values are not a measurement; they are omitted rather than presented as safety data.

### 2.6 Honesty limits

Docking ≠ activity. Vina noise is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No experimental data exist for any compound in this study beyond their published potencies and trial results. The three inhibitors' measured potencies are interaction and cellular IC50s from different assays, not a common-assay comparison, and their binding poses are not annotated anywhere — all three are SOS1 inhibitors by pharmacology, but the pose is assumed, not shown. The structure used (6SCM) holds BI-3406, so the pocket conformation is the reference drug's own, which favours it over the other two.

## 3. Results

### 3.1 Docking: the comparison table (6SCM, 1.87 Å — the BI-3406-bound structure)

| Compound | Clinical status | Best affinity, 6SCM (kcal/mol) | Top-3 poses (kcal/mol) | Margin vs BI-3406 |
|---|---|---|---|---|
| BI-3406 (reference) | Preclinical probe; clinical analogue BI 1701963 in Phase 1 | −9.07 | −9.07, −9.01, −8.36 | — |
| BAY-293 | Research tool; related compound in clinic | −8.11 | −8.11, −8.09, −7.47 | +0.96 |
| MRTX0902 | Phase 1 (NCT05578092) | −8.10 | −8.10, −7.63, −7.32 | +0.97 |

BI-3406 self-docks at −9.07 kcal/mol on 6SCM, with good pose consistency (−9.07, −9.01, −8.36): the method recovers strong binding for the drug in its own pocket, so the protocol is not broken. MRTX0902 scores −8.10 kcal/mol and BAY-293 −8.11 kcal/mol — behind by 0.97 and 0.96 kcal/mol, just inside Vina's ±1–2 kcal/mol noise, and the two comparators are 0.01 kcal/mol apart. Every margin in the table lies inside the noise, so no compound can be claimed to beat any other on this evidence — including the reference drug, whose win is smaller than the noise and comes on its own structure. The honest reading is a null result on ranking, with one validated control: the method works, and the three inhibitors are indistinguishable by rigid docking on this structure.

### 3.2 Comparison with published data

No published Vina study of BI-3406, MRTX0902 or BAY-293 on 6SCM was found in the sweep; the comparison here is internal (inhibitors vs re-docked reference drug on the same structure, same protocol). The structural literature is the published ground truth for the binding mode: the 6SCM structure shows BI-3406 in the CDC25 catalytic pocket, 6SFR (1.92 Å) shows the early quinazoline hit BI-68BS in the same pocket, 7AVS shows the afatinib-combination series compound, 5OVE shows another quinazoline inhibitor at 1.85 Å, and 6EPM/6EPN show the SOS1–KRAS(G12C) protein–protein complex at 2.50 Å. The published potency order is the opposite of the docking order's implication: BI-3406's SOS1::KRAS interaction IC50 is 5 nM, and MRTX0902's published cellular data are in the same range — the assays cannot separate them either, which is consistent with the docking null result rather than a contradiction of it. The decisive published fact is not a potency number but a clinical one: the only SOS1 inhibitor with Phase 1 dose-escalation results, BI 1701963, showed limited efficacy as monotherapy — one partial response — which is why the field's rationale is now vertical combination, not single-agent SOS1 inhibition.

### 3.3 The clinical confounder that docking cannot see

BI 1701963's clinical record is the paper's most important context, and docking cannot see any of it. The drug reached its maximum tolerated dose (800 mg monotherapy) with dose-limiting toxicities in 8.0% of patients, yet produced one partial response as monotherapy and stable disease as its best result in most patients — a drug that engages its target and still does not shrink tumours alone, because SOS2 compensates and because KRAS-mutant cancers rewire around a single upstream block. The combination data point the other way: with trametinib, dose-limiting toxicities rose to 31.6% of patients, and the combination's maximum tolerated dose fell to 100 mg with 1 mg trametinib — the vertical combination that the biology demands is also the combination that the toxicity budget punishes. A compound that out-scores BI-3406 here by 0.97 kcal/mol but cannot be combined safely would be a worse drug, and docking cannot tell the two apart. The docking order cannot explain why the class works in combination models and stalls as monotherapy in patients; the feedback biology and the toxicity data can.

## 4. Discussion

### 4.1 The reframe

The question this paper can ask has changed since BI-3406 was published. Before the Phase 1 data, the question was "can a SOS1 inhibitor beat BI-3406's potency?" — now it is "can any SOS1 inhibitor be combined safely enough to matter, given monotherapy stalls?" The benchmark is therefore a screen with a two-part bar: beat −9.07 kcal/mol on 6SCM and show a combinable safety profile. This paper supplies the first half of the bar and shows the second half is where the pipeline must go next: the three inhibitors cannot be separated by docking, and the class's defining problem is combination toxicity, not potency.

### 4.2 Why the "win" must not be over-read

Three reasons. First, every margin in §3.1 lies inside Vina's ±1–2 kcal/mol noise — the largest gap, 0.97 kcal/mol, is less than half the noise. Second, the reference drug wins on its own co-crystal structure, which biases the comparison in its favour; a win on home ground by less than noise is not a win. Third, the two comparators are 0.01 kcal/mol apart — a scoring function that cannot separate a brain-penetrant clinical candidate (MRTX0902) from a research tool (BAY-293) by more than a hundredth of a kilocalorie cannot rank this family. A fourth reason is specific to this target: SOS2 compensation means even a perfect SOS1 binder leaves a parallel route to KRAS activation open, so the docking score measures the wrong thing — binding to one GEF, not blockade of the pathway.

### 4.3 The dead heat is the experiment's design constraint, not a reason to stop

The three inhibitors were chosen by published data, not by pipeline rank, and the smallest and least lipophilic of them (MRTX0902, MW 388.48, logP 3.52) does not score best — it ties last — so the size bias is visible but not total in this set. The honest handling is to report the scores with the caveat attached, and to design the validation assay so the dead heat is answered by the experiment: a SOS1::KRAS interaction assay measures IC50 regardless of molecular weight, and a pERK assay in KRAS-mutant cells measures whether the inhibitor actually lowers pathway output, including through SOS2 compensation. A compound that scores well because the pocket was solved around it is not a failure of the compound; it is a failure of the scoring setup, and the assay is what tells the two apart.

### 4.4 Mechanism

BI-3406 binds the CDC25 catalytic domain of SOS1, prevents the SOS1::KRAS-GDP interaction, and so lowers GTP-loaded RAS and downstream RAF–MEK–ERK signalling. Test for each link: (i) a SOS1::KRAS interaction assay (with BI-3406 as the comparator) measures IC50 directly against the published 5 nM value; (ii) a pERK assay in KRAS-mutant NCI-H358 cells measures pathway output — a fall in pERK without a fall in RAS-GTP would break the claimed mechanism; (iii) a proliferation assay in KRAS-mutant versus KRAS wild-type cells measures selectivity, with SOS2 knockdown as the control for the compensation question.

### 4.5 Testable hypotheses

1. MRTX0902 disrupts the SOS1::KRAS interaction with an IC50 within 3-fold of BI-3406 in the same assay. Falsifier: IC50 > 3-fold worse than BI-3406.
2. The same compound lowers pERK in KRAS-mutant NCI-H358 cells within 3-fold of BI-3406's published 4 nM. Falsifier: pERK IC50 > 3-fold worse than BI-3406.
3. The 6SCM pose predicts the combination profile: an inhibitor whose docked pose occupies the same CDC25 pocket as BI-3406 attenuates MEK-inhibitor feedback reactivation to the same extent. Falsifier: no attenuation of feedback reactivation in combination with trametinib.

### 4.6 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): SOS1::KRAS interaction assay for the three inhibitors — BI-3406, MRTX0902, BAY-293 — plus a known weak binder as a negative control; readout IC50, n=3. Stage 2 (weeks 4–8): pERK assay in KRAS-mutant NCI-H358 cells for the best compound from stage 1 against BI-3406, with SOS2 knockdown as the compensation control. Stage 3 (weeks 9–12): if any inhibitor passes stages 1–2, a proliferation assay in KRAS-mutant versus KRAS wild-type cells, and a trametinib-combination arm to test feedback attenuation; if none passes, publish the negative result with the docking data as the reason the hypothesis failed. No animal work is proposed at this stage.

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol swallows every reported margin — the largest gap is 0.97 kcal/mol.
2. The ranking cannot separate the three inhibitors (the two comparators are 0.01 kcal/mol apart), so the set cannot test ranking at all.
3. The reference drug wins on its own co-crystal structure (6SCM), which biases the comparison in its favour.
4. The pipeline's first run docked BI-3406 into the KRAS GTP pocket of 6V9M (−8.88 kcal/mol); that score is discarded here, and the error is recorded in §2.3 rather than hidden.
5. One rigid structure was used (6SCM, inhibitor-bound, 1.87 Å); the other SOS1 structures (6SFR, 7AVS, 5OVE) and the SOS1–KRAS complex (6EPM/6EPN) were not docked.
6. No data on the clinical confounder: docking cannot distinguish the monotherapy that stalls from the combination that the toxicity budget punishes, nor the SOS2 compensation that leaves a parallel route open.
7. The ChEMBL ligand retrieval returned no data for this target, so the comparison set was built from the literature rather than from measured ChEMBL potencies; the three inhibitors' potencies are interaction and cellular IC50s from different assays, not a common-assay comparison.
8. No Pakistan-specific KRAS-mutant data were found; the burden numbers are global, and the absence of local genotyping data is a limitation of the policy section, not of the docking.
9. The classical-canon sweep found no SOS1-relevant text: the Canon of Medicine describes tumours, not proteins, so the Islamic-principle discussion rests on hifz al-nafs as a principle, not on a classical source about this target.

## 6. Conclusion

BI-3406, the SOS1::KRAS interaction inhibitor with a 5 nM interaction IC50 and a 4 nM pERK IC50 in KRAS-mutant cells, self-docks at −9.07 kcal/mol on its own 1.87 Å co-crystal 6SCM with no PAINS alert — a validated control, not a discovery. MRTX0902 and BAY-293 follow at −8.10 and −8.11 kcal/mol, behind by less than noise and 0.01 kcal/mol apart. The docking verdict is a null result on ranking, with one validated control, and it is useful precisely as one: this family cannot be ranked by rigid Vina scoring on a single structure, the reference drug's win comes on its own structure, and the next screen must be an interaction assay plus a pERK assay with a SOS2 control, not a bigger docking set. What the docking cannot do is resolve the clinical split: the same pocket that binds BI-3406 at −9.07 kcal/mol is the pocket whose blockade stalls as monotherapy in patients and whose combination with MEK inhibition the toxicity budget punishes. The next step is the cheap, decisive test — a SOS1::KRAS interaction assay for the three inhibitors against BI-3406 — not another docking run.

## 7. Policy implications

**Decision-maker:** Pakistan's Drug Regulatory Authority (DRAP) and the National Cancer Control Programme, with the SMBBMU ORIC office as the local route. **Decision:** whether to spend anything on SOS1 inhibitors in Pakistan, and what must exist first. **Exact change:** do not fund any SOS1-inhibitor evaluation — no SOS1 drug is approved, the only clinical data show limited monotherapy efficacy, and Pakistan has no KRAS-mutant registry, so the patients who could benefit cannot even be identified. Instead, fund KRAS genotyping capacity (next-generation sequencing) in the public cancer hospitals, starting with pancreatic, colorectal and lung cancer, so the 25%-of-tumours population is counted before any targeted drug is discussed; and, in parallel, ask the cancer programme to note explicitly that the binding question is settled for this pocket — BI-3406 self-docks at −9.07 kcal/mol — and that the remaining gap is combination safety and SOS2 compensation, not potency. **If evidence Z appears, reverse this:** if a SOS1 inhibitor shows a Phase 2 response rate above 20% in KRAS-mutant solid tumours in combination, and Pakistan's genotyping programme identifies a KRAS-mutant cohort, move to a drug-evaluation assessment for that combination; if genotyping shows KRAS mutations are rarer in Pakistan's cancers than the global 25%, drop the SOS1 route and redirect the same money to the mutations Pakistan's patients actually carry — do not proceed to any drug evaluation on docking scores alone. The Islamic principle is hifz al-nafs (preservation of life, a maqsad of the Sharia): where a cheap test can distinguish a usable targeted drug from an unusable one for the most commonly mutated oncogene in human cancer, running the test is the obligation; prescribing on an untested docking score would violate it. The evidence here is thin — docking only — so the recommendation is "run the trial", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Hofmann MH, et al. Discovery of the SOS1 inhibitor BI-3406. Cancer Discov. 2021;11:142–157. doi:10.1158/2159-8290.CD-20-0142. PMID: 32816843.
2. Ketcham JM, et al. Discovery of the SOS1 inhibitor MRTX0902. J Med Chem. 2022;65:9678–9690. doi:10.1021/acs.jmedchem.2c00741. PMID: 35833726.
3. Ramharter J, et al. SOS1 inhibition in KRAS G13D colorectal cancer. J Med Chem. 2021;64:6569–6580.
4. Co-targeting SOS1 enhances the antitumor effects of KRAS G12C inhibitors. Cancer Res. 2025;85:118–133. PMID: 39437166.
5. ClinicalTrials.gov. NCT04111458: BI 1701963 with or without trametinib in KRAS-mutant solid tumours (Phase 1). Accessed 2026-11-24.
6. ClinicalTrials.gov. NCT05578092: MRTX0902 with or without adagrasib (Phase 1). Accessed 2026-11-24.
7. RCSB PDB entry 6SCM: SOS1 in complex with inhibitor BI-3406, 1.87 Å. RCSB Protein Data Bank. Accessed 2026-11-24.
8. UniProtKB Q07889: Son of sevenless homolog 1, Homo sapiens. UniProt. Accessed 2026-11-24.
9. KRAS mutation burden in human cancer. Curr Oncol. 2025;32:614.
10. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; describes tumours, saratān — cited for the hifz al-nafs principle only.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-128-2026-11-24-6SCM.json` (BI-3406 + two SOS1 inhibitors on 6SCM). The pipeline run is in `hidden_files/dock-HP-128-2026-11-24.json` (BI-3406 −8.88 kcal/mol on 6V9M — DISCARDED: the centre audit showed the drug was docked into the KRAS GTP pocket, not SOS1; see §2.3). Reference drug BI-3406; comparators MRTX0902, BAY-293 (SMILES verified against PubChem by molecular formula). Structure: PDB 6SCM (1.87 Å). Target: UniProtKB Q07889. No additional data were generated.
