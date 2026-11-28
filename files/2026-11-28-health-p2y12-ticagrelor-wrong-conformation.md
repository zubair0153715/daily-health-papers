# Ticagrelor Scores −9.00 on the Right P2Y12 Structure and −6.06 on the Wrong One: the Antagonist Pocket Decides the Ranking

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-28 · **Health Papers Agent — Paper #129** (daily 5-paper run)

**Keywords:** P2Y12; ticagrelor; antiplatelet; acute coronary syndrome; bleeding; molecular docking; ChEMBL; Pakistan

---

## Abstract

Dual antiplatelet therapy — aspirin plus a P2Y12 inhibitor — is the cornerstone of acute coronary syndrome treatment, and ticagrelor beat clopidogrel in the 18,624-patient PLATO trial (Wallentin et al. 2009) without increasing overall major bleeding, yet at the cost of more non-CABG major bleeding and, in a 2025 meta-analysis of 16 studies, a 31% higher risk of gastrointestinal bleeding than clopidogrel (RR 1.31, 95% CI 1.15–1.49). A better P2Y12 antagonist must therefore win on bleeding, not on binding — every candidate in this screen already binds in the sub-nanomolar range. We re-screened P2Y12 with the standardised LeadForge protocol (UniProtKB Q9H244 → ChEMBL target CHEMBL2001, 52 bioactivities → PubChem → RDKit → PAINS/ADMET → AutoDock Vina 1.2.7) and docked the top five leads plus ticagrelor in the same grid. The pipeline's automatic structure pick was wrong — PDB 4PXZ is P2Y12 in complex with the agonist 2MeSADP, and ticagrelor scored only −6.06 kcal/mol there, with one lead at −3.70 — so we re-docked on PDB 4NTJ, P2Y12 in complex with the antagonist AZD1283 (2.62 Å). On the correct structure the headline result is a narrow one: CHEMBL249790, a close ticagrelor analogue (Tanimoto 0.844) with a measured Ki of 0.631 nM, out-docked ticagrelor by 0.57 kcal/mol (−9.57 vs −9.00 kcal/mol), and CHEMBL251041 (Ki 0.2512 nM) scored −9.22 kcal/mol. The 0.57 kcal/mol margin is inside Vina's ±1–2 kcal/mol noise, and all five molecules are sub-nanomolar measured binders, so docking cannot rank them and cannot say anything about bleeding. The falsifiable next step is a platelet assay, not more docking: CHEMBL249790 must inhibit ADP-induced platelet aggregation with IC50 at or below ticagrelor's and show faster offset (reversibility) in a washout experiment, or the docking rank is refuted. Until that assay exists, this paper is a triage signal only — no efficacy, safety or clinical claim follows.

---

## 1. Introduction

Platelets clot through ADP: released ADP binds the P2Y12 receptor, amplifies aggregation, and stabilises the thrombus. Blocking P2Y12 is therefore one of the most consequential interventions in cardiology — dual antiplatelet therapy (aspirin + a P2Y12 inhibitor) is the cornerstone of acute coronary syndrome (ACS) care. Three oral P2Y12 inhibitors dominate: clopidogrel (a prodrug, irreversible, CYP2C19-dependent), prasugrel (a prodrug, irreversible, more potent) and ticagrelor (direct-acting, reversible, cyclopentyl-triazolopyrimidine). The PLATO trial (18,624 ACS patients, Wallentin et al. 2009) showed ticagrelor superior to clopidogrel for the composite of vascular death, myocardial infarction or stroke, with no increase in overall major bleeding — but with more non-CABG major bleeding, dyspnoea and bradycardia. A 2025 network meta-analysis of 5 randomised trials (35,196 ACS patients) found the three drugs similar for major adverse cardiac events, with ticagrelor carrying significantly higher risks of non-CABG TIMI major bleeding and intracranial haemorrhage than clopidogrel, and a 2025 meta-analysis of 16 studies put the gastrointestinal-bleeding risk of the third-generation agents (ticagrelor, prasugrel) at 31% above clopidogrel (RR 1.31, 95% CI 1.15–1.49). The gap this paper attacks is therefore precise: the field does not need a tighter P2Y12 binder — it needs a reversible antagonist with a better bleeding profile, and the first question is whether docking can even rank the binders honestly.

**Falsifiable hypothesis (one sentence):** CHEMBL249790 inhibits ADP-induced human platelet aggregation with IC50 at or below ticagrelor's and reverses faster on washout.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-28: PubMed (ticagrelor, PLATO, P2Y12 bleeding meta-analyses), ClinicalTrials.gov (PLATO, NCT00391872, via the published report), RCSB PDB (4NTJ, 4PXZ), ChEMBL (target CHEMBL2001, live) and the 2025 network and gastrointestinal-bleeding meta-analyses. No Pakistan-specific ACS outcome or P2Y12 bleeding data was verified for this paper — that absence is recorded as a limitation, not filled with an estimate. The Islamic canon sweep (per the programme's standing rule) checked Ibn Sina's *Canon of Medicine* (Book III on the heart and blood; Book II materia medica) as a hypothesis source; no Canon-listed plant was docked in this run, and the classical literature is cited for the policy principle (hifz al-nafs, preservation of life), not as evidence for any molecule.

### 2.2 Molecular docking

Standardised AutoDock Vina protocol, exactly as Papers #1/#3: Vina 1.2.7, 22.5 Å cubic box, exhaustiveness 8, best of three poses reported, same grid for every compound. **Structure correction (this paper's central methods point):** the pipeline's automatic pick, PDB 4PXZ (2.5 Å), is P2Y12 in complex with 2MeSADP — the agonist-bound, active-state conformation. Ticagrelor is a reversible antagonist; docking antagonists into the agonist-bound structure gave weak, compressed scores (ticagrelor −6.06, CHEMBL567709 −3.70 kcal/mol). We therefore re-docked all five compounds on PDB 4NTJ (human P2Y12 in complex with the antagonist AZD1283, 2.62 Å; Zhang et al., *Nature* 2014), grid centred on the co-crystallised AZD1283 ligand at [16.96, 100.82, 50.75] via the pipeline's own `dock._ligand_center`. Both runs are preserved: the 4PXZ run in `dock-HP-138-2026-11-28.json` and the 4NTJ re-dock in `dock-HP-138-2026-11-28-4NTJ.json`. Only the 4NTJ results are reported as the paper's findings; the 4PXZ run is reported as the failure it was.

### 2.3 PAINS screen

RDKit PAINS filter applied to every test compound. All five docked compounds are PAINS-clean (zero alerts).

### 2.4 Honesty limits

Docking is not activity, and for P2Y12 it is not bleeding: nothing in a docking score predicts haemorrhage, reversibility or dyspnoea. Vina's scoring error is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No platelet assay, aggregation data or animal data were generated in this paper. The measured Ki values quoted are ChEMBL records from different source assays, not head-to-head measurements.

## 3. Results

### 3.1 Docking: the comparison table (PDB 4NTJ, correct antagonist pocket)

| Compound | Best affinity (kcal/mol) | Top-3 poses (kcal/mol) | Measured Ki vs P2Y12 (ChEMBL) | MW | logP | PAINS |
|---|---|---|---|---|---|---|
| CHEMBL249790 | **−9.57** | −9.57, −9.18, −9.01 | 0.631 nM (pChEMBL 9.20) | 576.55 | 2.56 | none |
| CHEMBL251041 | −9.22 | −9.22, −9.06, −8.35 | 0.2512 nM (pChEMBL 9.60) | 470.56 | 2.06 | none |
| Ticagrelor (QUERY, PubChem) | −9.00 | −9.00, −8.80, −8.66 | — (PLATO drug; Ki not in this ChEMBL set) | 522.58 | 2.01 | none |
| CHEMBL567709 | −8.87 | −8.87, −8.67, −8.65 | 0.71 nM (pChEMBL 9.15) | 654.77 | 2.56 | none |
| CHEMBL5181634 | −8.26 | −8.26, −7.78, −7.35 | 0.3 nM (pChEMBL 9.52) | 430.43 | 3.62 | none |

Ticagrelor and CHEMBL249790 each carry one Lipinski violation (molecular weight >500); CHEMBL251041 and CHEMBL5181634 pass with zero violations. Tox21 kNN read-across maxima are 0.142–0.508 across the set, highest for CHEMBL249790 (0.508) and ticagrelor itself (0.45). CHEMBL249790 is a close structural analogue of ticagrelor (Tanimoto similarity 0.844, same descriptors family: MW 576.55 vs 522.58, TPSA 138.44 for both).

### 3.2 The wrong-conformation run (PDB 4PXZ, reported as a failure)

On 4PXZ the same five compounds scored −7.54 (CHEMBL5181634), −7.22 (CHEMBL251041), −6.72 (CHEMBL249790), −6.06 (ticagrelor) and −3.70 (CHEMBL567709) — a ranking that put the reference drug fourth and the largest lead essentially non-binding. The correction moved every score by +0.7 to +5.2 kcal/mol and inverted the order. Had the 4PXZ run been reported without correction, the paper would have concluded that ticagrelor is a mediocre P2Y12 binder and that CHEMBL567709 does not bind at all — both false.

### 3.3 Comparison with published docking

No published Vina docking of these four ChEMBL compounds against P2Y12 was found. The reference re-dock is consistent with the structural literature: ticagrelor and AZD1283 occupy the same antagonist pocket, and the 4NTJ structure is the standard template for reversible antagonists. The clinical literature is unambiguous about what matters next: affinity is not the differentiator (all candidates are sub-nanomolar), bleeding is — and no docking study measures it.

## 4. Discussion

### 4.1 The reframe: the ranking is real now — and it does not matter much

The correction did its job: on 4NTJ the poses are tight (ticagrelor −9.00/−8.80/−8.66; CHEMBL249790 −9.57/−9.18/−9.01), the reference drug scores like a real binder, and the ranking is reproducible. But the margin that the ranking produces — 0.57 kcal/mol between the best lead and ticagrelor — is inside Vina noise, and every molecule in the table is already a sub-nanomolar measured binder. The honest conclusion is that this screen has nothing to say about which molecule is better; it has something to say about how to screen. The paper's contribution is the audit (agonist vs antagonist conformation) and a short list of molecules that are legitimate for the one assay that can separate them.

### 4.2 Why the "win" must not be over-read

Four reasons. First, the 0.57 kcal/mol margin is inside noise. Second, CHEMBL249790 is a close ticagrelor analogue (similarity 0.844) — an incremental change to a known drug, not a new scaffold, and it carries ticagrelor's own liabilities (one Lipinski violation, the highest Tox21 signal in the set). Third, CHEMBL567709 (MW 654.77, 15 rotatable bonds) is the largest molecule in the set and its −8.87 score on the correct structure shows that the 4PXZ −3.70 was a conformation artefact, not a property of the molecule — a warning against reading any single docking number. Fourth, and decisively: the clinical differentiator is bleeding, and docking is silent on it. A molecule that out-docks ticagrelor by 0.57 kcal/mol and bleeds like prasugrel is a worse drug, not a better one.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

All five compounds are PAINS-clean. The design constraint that does apply is functional: the validation assay must measure aggregation inhibition AND reversibility (washout) AND, in animals, bleeding time — three readouts, because affinity alone has already been maximised by every molecule in the table.

### 4.4 Testable hypotheses

1. CHEMBL249790 inhibits ADP-induced human platelet aggregation with IC50 ≤ ticagrelor's in the same assay (falsifier: IC50 > 2× ticagrelor's).
2. CHEMBL249790 reverses faster than ticagrelor on washout (falsifier: offset slower than or equal to ticagrelor's).
3. CHEMBL251041 (the smallest, cleanest lead: MW 470.56, zero Lipinski violations, Ki 0.2512 nM) matches ticagrelor's aggregation IC50 (falsifier: IC50 > 2× ticagrelor's — which would show that the tightest measured Ki does not translate to platelets).
4. CHEMBL567709 inhibits aggregation despite its size (falsifier: no activity at 10 µM — which would suggest the 4NTJ score is a docking artefact of a floppy ligand).
5. The best lead shows a longer bleeding time than ticagrelor in a mouse tail-bleed model at equi-effective doses (falsifier: equal or shorter bleeding time — which would end the "better bleeding" claim, the only claim that matters).

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): light-transmission aggregometry on human platelet-rich plasma — ADP-induced aggregation dose-response for CHEMBL249790, CHEMBL251041, CHEMBL567709 and ticagrelor in one run, triplicate, with washout reversibility at the IC50. Stage 2 (weeks 4–6): P2Y12-specific binding (radioligand or fluorescent displacement) to confirm the Ki values head-to-head. Stage 3 (weeks 7–9): HepG2 cytotoxicity and hERG screen (the class liability). Stage 4 (weeks 10–12): mouse tail-bleed and FeCl3 thrombosis models for the best lead, if stages 1–3 pass. The aggregometry plus washout is the only gate that matters for this paper's claim.

## 5. Limitations

1. Docking only: no platelet, binding or animal data were generated; the 0.57 kcal/mol margin is inside Vina's ±1–2 kcal/mol noise.
2. The pipeline's first structure pick was the wrong conformation (agonist-bound 4PXZ); the correction was manual. Other papers in this series should audit their auto-picked structures the same way.
3. Single structure: docking used one P2Y12 structure (4NTJ); no MD or free-energy refinement was run.
4. Bleeding is unmeasured: nothing in this paper predicts haemorrhage, the outcome that decides whether a new P2Y12 antagonist is useful.
5. Measured Ki values are ChEMBL records from different source assays, not head-to-head measurements; ticagrelor's own Ki is not in this ChEMBL set.
6. No Pakistan-specific ACS outcome or P2Y12 bleeding data was verified for this paper; the policy section is therefore framed on the global trial evidence, not local outcomes.
7. Islamic-canon sweep: the full 23 volumes of Al-Razi's *Kitab al-Hawi* exist in English only in selections, and Ibn al-Nafis's commentary survives as an Arabic manuscript with only partial English translation; those texts were not read in full. No classical work was used as evidence for any molecule.
8. No local-market data: ticagrelor generics are available in Pakistan, but the price and availability of the test compounds were not checked.

## 6. Conclusion

On the correct antagonist structure, CHEMBL249790 out-docks ticagrelor on P2Y12 by 0.57 kcal/mol — a margin inside docking noise, between two sub-nanomolar binders. The paper's durable result is the correction: docking antagonists into the agonist-bound structure gave ticagrelor −6.06 and a real binder −3.70, and auditing the conformation changed every number. Until the platelet assay runs, nothing here is a treatment claim — and no docking score can promise less bleeding.

## 7. Policy implications

**Decision-maker:** the Drug Regulatory Authority of Pakistan (DRAP) and the Pakistan Cardiac Society, with the provincial health departments that run cardiac units. **Decision:** whether to require local bleeding-outcome data for new antiplatelet agents, and whether to fund a national DAPT registry. **Exact change:** DRAP and the Pakistan Cardiac Society should establish a prospective registry of ACS patients on dual antiplatelet therapy recording major and minor bleeding (TIMI criteria) alongside ischaemic events, and require that any new P2Y12 antagonist seeking registration present head-to-head bleeding data against ticagrelor — instead of accepting affinity or platelet-inhibition data alone, which every candidate already passes. **If the evidence reverses this:** if the registry shows ticagrelor's bleeding rates in Pakistani practice are no higher than clopidogrel's, the registry should continue as surveillance but the registration bar should not be raised further. **Islamic principle:** hifz al-nafs (preservation of life), defined by Al-Ghazali in *Al-Mustasfa min 'Ilm al-Usul* (c. 1109) and systematised by Al-Shatibi in *Al-Muwafaqat* — a drug that prevents a heart attack but causes a fatal bleed has not preserved life, it has traded one death for another, and 'adl (justice, Qur'an 4:135) requires the trade-off to be measured in the population that will actually take the drug, not assumed from a foreign trial. Ibn Sina's *Canon* (Book III) treated the heart and blood as a single system to be observed whole — the classical precedent for measuring both benefit and harm together.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author thanks the open-data providers — UniProtKB, ChEMBL, PubChem and the RCSB Protein Data Bank — without which this work would not exist.

## References

1. Wallentin L, Becker RC, Budaj A, et al. Ticagrelor versus clopidogrel in patients with acute coronary syndromes. N Engl J Med. 2009;361(11):1045–1057. doi:10.1056/NEJMoa0904327. PMID: 19717846. (PLATO, 18,624 patients.)
2. Tseng HY, et al. Efficacy and safety of P2Y12 receptor antagonists in acute coronary syndrome: network meta-analysis of Asian and non-Asian randomized controlled trials. J Taiwan Cardiovasc Interv. 2025;16:11–30. (5 RCTs, 35,196 patients; ticagrelor higher non-CABG TIMI major bleeding and intracranial haemorrhage.)
3. The risk of gastrointestinal bleeding in patients taking third-generation P2Y12 inhibitors compared with clopidogrel: systematic review and meta-analysis. Ann Med Surg. 2025;87(10):6694–6701. doi:10.1097/MS9.0000000000003821. (16 studies; RR 1.31, 95% CI 1.15–1.49.)
4. Zhang K, et al. Structure of the human P2Y12 receptor in complex with an antithrombotic drug. Nature. 2014;509(7498):115–118. doi:10.1038/nature13083. PMID: 24670650.
5. RCSB PDB entry 4NTJ: structure of the human P2Y12 receptor in complex with an antithrombotic drug (AZD1283), 2.62 Å. RCSB Protein Data Bank. Accessed 2026-11-28.
6. RCSB PDB entry 4PXZ: crystal structure of P2Y12 receptor in complex with 2MeSADP, 2.5 Å. RCSB Protein Data Bank. Accessed 2026-11-28. (Cited as the wrong-conformation failure, not as an antagonist template.)
7. UniProtKB Q9H244: P2Y purinoceptor 12, Homo sapiens. UniProt. Accessed 2026-11-28.
8. ChEMBL target CHEMBL2001: P2Y purinoceptor 12, Homo sapiens; 52 bioactivities retrieved live 2026-11-28, including Ki values for CHEMBL249790 (0.631 nM), CHEMBL251041 (0.2512 nM), CHEMBL5181634 (0.3 nM) and CHEMBL567709 (0.71 nM). ChEMBL, EMBL-EBI.
9. Al-Ghazali. Al-Mustasfa min 'Ilm al-Usul. c. 1109. (Defines the five necessities of the law, including hifz al-nafs.)
10. Al-Shatibi. Al-Muwafaqat fi Usul al-Shari'a. 14th c. (Systematises maqasid al-shariah.)
11. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Book III on the heart and blood; cited for the hifz al-nafs principle only.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-138-2026-11-28-4NTJ.json` (re-dock on PDB 4NTJ) and `hidden_files/dock-HP-138-2026-11-28.json` (pipeline run, including the wrong-conformation 4PXZ run preserved as a failure record). Compound identifiers: ticagrelor (QUERY), CHEMBL249790, CHEMBL251041, CHEMBL567709, CHEMBL5181634. No additional data were generated.
