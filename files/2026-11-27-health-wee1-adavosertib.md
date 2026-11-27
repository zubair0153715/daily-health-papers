# Nothing Beats Adavosertib on Wee1 Docking: the Top Five Sit Inside One Molecule's 0.44 kcal/mol Reproducibility Gap

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-27 · **Health Papers Agent — Paper #126** (daily 5-paper run)

**Keywords:** Wee1; adavosertib; AZD1775; G2/M checkpoint; TP53; synthetic lethality; myelosuppression; molecular docking; ChEMBL; Pakistan

---

## Abstract

Wee1 kinase guards the G2/M checkpoint by phosphorylating CDK1 at Tyr15, and TP53-mutant cancers — which have lost the G1/S checkpoint — depend on it, making Wee1 inhibition a synthetic-lethal strategy. Adavosertib (AZD1775/MK-1775) is the first-in-class Wee1 inhibitor, but its single-agent response rate is 3.8% and its dose-limiting toxicity is myelosuppression. We asked whether any published Wee1 inhibitor beats adavosertib on docking to the Wee1 kinase domain. Using the LeadForge pipeline (UniProtKB P30291 → ChEMBL target CHEMBL5491, 60 bioactivities → PubChem/RDKit, PAINS and ADMET screen) we docked adavosertib and four ChEMBL Wee1 actives with AutoDock Vina on PDB 8BJU, a 1.53 Å Wee1–inhibitor complex. Nothing beats adavosertib by any meaningful margin: the whole top five spans 0.45 kcal/mol (−11.07 to −10.62 kcal/mol), and adavosertib docked twice — once as the query and once as its duplicate ChEMBL record — differs by 0.44 kcal/mol from itself. Docking cannot distinguish these five compounds at all. By measurement the leads are ~10-fold more potent than adavosertib (IC50 0.2–0.3 nM vs Kd 3.2 nM), but two of them are PAINS-clean while adavosertib itself carries the anil_di_alk PAINS alert — and a more potent Wee1 inhibitor may simply be more myelosuppressive, since the 8BJU paper's own title reports that Wee1 inhibition correlates with myelosuppression. The falsifiable next step is a head-to-head kinase assay plus a bone-marrow progenitor assay: if a lead does not confirm below 1 nM, or if its potency gain comes with equal myelosuppression, the lead is refuted as a therapeutic advance. No pipeline failure occurred on this target — the structure, the centre and the target all verified — which makes the null docking result a property of the compounds, not of the method.

---

## 1. Introduction

The cell cycle has two checkpoints that matter for cancer therapy, and TP53-mutant tumours have already lost one of them. Wee1 is a nuclear serine/threonine kinase that phosphorylates cyclin-dependent kinase 1 (CDK1) at the inhibitory Tyr15 residue, holding the CDK1–cyclin B complex inactive and pausing the cell at the G2/M boundary until DNA damage is repaired. In a TP53-mutant cell the G1/S checkpoint is gone, so the tumour relies almost entirely on Wee1-mediated G2 arrest; remove Wee1 and the cell enters mitosis with broken DNA, collapsing replication forks and fragmenting chromosomes — mitotic catastrophe. That is synthetic lethality: the drug kills the cancer cell not because the target is cancer-specific, but because the cancer has already discarded its backup.

Adavosertib (AZD1775, MK-1775) is the first-in-class ATP-competitive Wee1 inhibitor, and its clinical record is a study in a narrow therapeutic index. In a phase Ib trial (175 mg twice daily, days 1–3 and 8–10 of a 21-day cycle) the overall response rate was 3.8% with a disease control rate of 63.8%, and the commonest toxicities were diarrhoea (56.3%), nausea (42.5%) and fatigue (36.3%) (Bauer et al., Target Oncol 2023). A phase I once-daily study set the recommended phase II dose at 300 mg (days 1–5 and 8–12) and saw 6 confirmed partial responses in 42 patients (14%, four ovarian, two endometrial), with grade 4 haematologic toxicity as the dose-limiting event and CCNE1 (cyclin E1) overexpression emerging as a candidate predictive biomarker (Clin Cancer Res 2021;27:3834). In TP53-mutated uterine carcinosarcoma the response rate was 22.2% with median progression-free survival of 2.7 months, and the trial was terminated early after the sponsor discontinued monotherapy development. The structural basis is known: the Wee1–adavosertib complex (PDB 5V5Y, 1.90 Å, Zhu et al., J Med Chem 2017) — which also showed that adavosertib is an equally potent inhibitor of polo-like kinase PLK1, an off-target that complicates every claim about its selectivity. And the class limit is stated in the title of the newest structure paper: selective Wee1 inhibitors show antitumour activity in vitro that correlates with myelosuppression (ACS Med Chem Lett 2023; PDB 8BJU).

The gap this paper attacks is therefore not "find a more potent Wee1 inhibitor" — potency exists — but whether docking can rank the potent ones, and whether a more potent molecule is even the right goal when the dose-limiting toxicity tracks the same target.

**Falsifiable question.** Does any published ChEMBL Wee1 inhibitor beat adavosertib on docking to the Wee1 kinase domain, by more than the method's own reproducibility? **Falsifier:** a head-to-head kinase assay in which no lead confirms below 1 nM, or a progenitor assay in which the most potent lead suppresses bone-marrow progenitors at the same concentration as adavosertib — either result refutes the lead as a therapeutic advance. **Causal identification:** validated-control re-docking (adavosertib re-docked into a Wee1–inhibitor complex, same grid, same protocol, plus its duplicate-record re-dock as an internal reproducibility control) — association only beyond that, since no experiment was run and docking scores are not activity.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-27: the adavosertib phase Ib study (Bauer et al., Target Oncol 2023;18); the once-daily phase I study (Clin Cancer Res 2021;27:3834); the TP53-mutated uterine carcinosarcoma phase 2 report (ORR 22.2%, mPFS 2.7 months, early termination); the Wee1 structure–function paper (Zhu et al., J Med Chem 2017;60:7863–7875, doi:10.1021/acs.jmedchem.7b00996, PMID 28792760; PDB 5V5Y); and the selective-Wee1-inhibitor paper (ACS Med Chem Lett 2023; PDB 8BJU). Measured IC50/Kd values for adavosertib and the four leads were retrieved live from the ChEMBL API on 2026-11-27 (target CHEMBL5491). The classical-canon sweep is in §4.3: Ibn Sina's Canon of Medicine (c. 1025) discusses swellings and tumours (waram) and their surgical treatment, and Al-Razi's Kitab al-Hawi records clinical observation of tumours — neither describes a kinase or an inhibitor, so the Islamic-principle discussion rests on hifz al-nafs and la darar (no harm), not on a classical source about this target.

### 2.2 Target identification

No failure occurred on this target, and the absence of failure is stated because the previous two papers in this run both needed corrections. The target was specified directly by its reviewed accession: UniProt P30291 (WEE1_HUMAN, gene WEE1, 646 aa). ChEMBL target by accession returned CHEMBL5491, "Wee1-like protein kinase", single protein, Homo sapiens, with 60 bioactivities. Adavosertib was verified against PubChem (C27H32N8O2, MW 500.61, logP 2.89, 2 H-bond donors, 8 acceptors, TPSA 104.34 Å², 7 rotatable bonds, 1 Lipinski violation, PAINS alert — see §2.4). The similarity screen against the 60 ChEMBL Wee1 actives returned 25 leads; the top four by composite score were docked alongside adavosertib.

### 2.3 Molecular docking

Docking ran on PDB 8BJU (1.53 Å, human Wee1 kinase in complex with inhibitor QT9, an adavosertib analogue; ACS Med Chem Lett 2023). The grid centre [−14.10, −11.12, 19.32] is the centroid of the co-crystallised QT9 ligand (42 atoms, verified against the PDB file — the only non-water HETATM group), computed by dock._ligand_center. All five ligands were docked with AutoDock Vina 1.2.7 at that centre (box 22.5 Å, exhaustiveness 8, best of 3 poses). Two structural facts must be stated: 8BJU is a Wee1–inhibitor complex, so the grid is ligand-validated (unlike the apo structures in Papers #124–125); and the QT9 inhibitor is an adavosertib analogue, so the pocket is the adavosertib pocket — the docking tests fit into adavosertib's own site, which favours adavosertib-like molecules and is a bias, not a neutral test.

### 2.4 PAINS screen

RDKit PAINS filter applied to adavosertib and all four leads. The result is reported, not hidden: adavosertib carries the alert `anil_di_alk_A(478)` — the dialkyl-aniline substructure (its 4-(4-methylpiperazin-1-yl)aniline moiety) — and so do its duplicate record CHEMBL1976040 and CHEMBL6172478, which share the same anilino group. CHEMBL5761564 and CHEMBL6065998 are PAINS-clean. A PAINS alert is a screening flag, not a verdict: adavosertib is a clinically tested drug that carries it, which shows the filter's limits — but it also means the anilino group is a known assay-interference risk, and the validation assay in §4.5 includes the detergent and redox controls that would expose it. The two PAINS-clean leads are therefore the more interesting compounds on this axis, not the more potent ones.

### 2.5 Honesty limits

Docking scores are not activity: Vina's noise is ±1–2 kcal/mol, the structure is a single inhibitor-bound conformation, and no molecular dynamics or free-energy refinement was run. The leads' IC50s (0.2–0.3 nM) and adavosertib's Kd (3.2 nM) come from different assay formats (kinase activity vs binding) and different documents, so the "~10-fold" comparison is order-of-magnitude, not head-to-head. Adavosertib's own potency varies by assay (Kd 3.2 nM recombinant, 12 nM Kinobeads). No experimental data were generated in this study.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | ChEMBL ID | Best affinity (kcal/mol) | Poses (kcal/mol) | Measured Wee1 potency | MW (Da) | logP | TPSA (Å²) | PAINS |
|---|---|---|---|---|---|---|---|---|
| CHEMBL5761564 | CHEMBL5761564 | −11.07 | −11.07, −10.75, −10.05 | IC50 0.3 nM | 469.96 | 3.92 | 107.1 | clean |
| CHEMBL1976040 (= adavosertib) | CHEMBL1976040 | −11.06 | −11.06, −10.54, −10.27 | Kd 3.2 nM | 500.61 | 2.89 | 104.3 | anil_di_alk_A(478) |
| CHEMBL6065998 | CHEMBL6065998 | −11.04 | −11.04, −10.71, −10.21 | IC50 0.2 nM | 453.50 | 3.41 | 107.1 | clean |
| CHEMBL6172478 | CHEMBL6172478 | −10.75 | −10.75, −10.60, −10.58 | IC50 0.3 nM | 499.62 | 3.01 | 111.1 | anil_di_alk_A(478) |
| Adavosertib (reference) | — (PubChem) | −10.62 | −10.62, −10.03, −10.02 | Kd 3.2 nM | 500.61 | 2.89 | 104.3 | anil_di_alk_A(478) |

All five docked into the same grid (8BJU, QT9 centre [−14.10, −11.12, 19.32], box 22.5 Å). The "best" lead beats adavosertib by 0.45 kcal/mol — a quarter of Vina's noise band, and therefore not a win.

### 3.2 The same molecule, docked twice, spans the whole ranking

The table contains an internal control that the pipeline did not plan: CHEMBL1976040 is adavosertib itself under a duplicate ChEMBL record (identical formula C27H32N8O2, identical descriptors to the last decimal, Tanimoto similarity 1.0 to the query). It docked at −11.06 kcal/mol; adavosertib as the query docked at −10.62 kcal/mol. The same molecule, docked twice by the same protocol, differs by 0.44 kcal/mol — Vina's stochasticity on this target, measured directly. The entire top-five spread is 0.45 kcal/mol. The ranking is therefore indistinguishable from noise: the "best" lead and the reference differ by less than the method differs from itself. This is the paper's result, and it is a null result: **docking cannot rank these five Wee1 inhibitors, and no lead is declared.** The measured data tell a different, cleaner story — the three non-adavosertib leads are 0.2–0.3 nM against adavosertib's 3.2 nM Kd, roughly 10-fold more potent — but that story comes from the assays, not from the docking, and it is the assays that must confirm it.

### 3.3 The duplicate-record correction

CHEMBL1976040 and the query are the same molecule, and the paper treats them as such: the 0.3 nM-class potency belongs to adavosertib, not to a new lead, and the "−11.06 kcal/mol lead" is adavosertib re-docked. A paper that reported "CHEMBL1976040 beats adavosertib" without checking the structures would be reporting a database artefact as a discovery — the same error Paper #118 caught for tenapanor. The check took one RDKit comparison and it is stated here, not buried.

### 3.4 Comparison with published docking

Zhu et al. (2017) solved the Wee1–adavosertib structure but reported no docking scores, and no published Vina scores exist for these four ChEMBL compounds on 8BJU. The compounds have no common names. This paper's docking table therefore stands alone as a Vina ranking, and §3.2 is the statement that the ranking is noise.

## 4. Discussion

### 4.1 The reframe

The question was "what beats adavosertib?" and the honest answer is that docking cannot answer it for this target — and that the question itself may be wrong. Adavosertib's problem was never potency: at 3.2 nM it is already potent, and the leads at 0.2–0.3 nM are only 10-fold better. Its problem is the therapeutic index: single-agent response 3.8%, dose-limiting myelosuppression, and a sponsor that discontinued monotherapy development. A 10-fold more potent Wee1 inhibitor that suppresses bone marrow 10-fold more strongly is not an advance; it is the same drug with a smaller dose. The 8BJU paper's title says the quiet part aloud — Wee1 inhibition correlates with myelosuppression — because Wee1 also guards the G2/M checkpoint in healthy haematopoietic progenitors. The reframe is therefore from "find a more potent Wee1 inhibitor" to "find a Wee1 inhibitor with a wider index, or a biomarker that picks the patients who respond": TP53 mutation plus CCNE1 overexpression, the two markers the phase I study flagged, are the selection tools, and the leads' value depends on whether they spare progenitors, not on whether they dock 0.45 kcal/mol better.

### 4.2 Why the "win" must not be over-read

Three corrections guard the headline. First, the 0.45 kcal/mol margin is inside the method's own 0.44 kcal/mol reproducibility gap — it is not a win by any definition. Second, the reference drug carries a PAINS alert, so the docking scores for the anilino compounds (including adavosertib itself) carry an assay-interference caveat that the two PAINS-clean leads do not. Third, the measured 10-fold potency gap is across assay formats (IC50 vs Kd) and documents, so it is order-of-magnitude. What is solid is the validation: the grid is ligand-anchored on a 1.53 Å inhibitor complex, the target and structure both verified, and the duplicate-molecule control quantifies the noise — which is exactly why the null result is trustworthy rather than a failure to look. The memorable number is **0.44 kcal/mol** — the same molecule docked twice differs by as much as the whole top five — because it is the number that kills the ranking.

### 4.3 Mechanism — and the classical canon

Wee1 phosphorylates CDK1 at Tyr15, holding the CDK1–cyclin B complex inactive; adavosertib competes with ATP, Tyr15 phosphorylation falls, CDK1 activates early, and the TP53-deficient cell enters mitosis with unrepaired breaks — mitotic catastrophe. Test for each link: (i) a biochemical kinase assay measures Wee1 inhibition directly, against the published 3.2 nM Kd; (ii) a pY15-CDK1 Western blot in TP53-mutant cells measures target engagement in cells, against the phase I study's paired-biopsy readout; (iii) a colony-forming-unit assay on healthy bone-marrow progenitors measures the myelosuppression that defines the index, against adavosertib as the comparator. The classical canon knows the disease, not the kinase: Ibn Sina's Canon of Medicine (c. 1025) discusses swellings and tumours (waram) and their surgical treatment, and Al-Razi's Kitab al-Hawi records clinical observation of tumours — but neither describes a cell-cycle checkpoint, so the principle carried forward is hifz al-nafs (preservation of life) joined to la darar (no harm): a drug whose benefit is measured in months and whose harm is measured in bone marrow must be selected by a biomarker, not prescribed to all comers, because the harm is certain and the benefit is not.

### 4.4 Testable hypotheses

1. CHEMBL6065998 inhibits recombinant Wee1 with an IC50 below 1 nM in a head-to-head kinase assay on the same day as adavosertib. Falsifier: IC50 above 1 nM, which would refute the ChEMBL record and remove the lead.
2. CHEMBL6065998 suppresses healthy bone-marrow progenitor colony formation at a concentration at least 10-fold higher than its Wee1 IC50 (a therapeutic index of 10). Falsifier: suppression within 3-fold of the IC50, which would show the potency gain buys no safety.
3. In TP53-mutant, CCNE1-overexpressing ovarian cancer cells, CHEMBL5761564 reduces pY15-CDK1 by at least 50% at its IC50 and induces γ-H2AX accumulation. Falsifier: no pY15 reduction at the IC50, which would show the compound does not engage the target in cells.
4. Adavosertib's PAINS alert (`anil_di_alk_A(478)`) does not produce aggregation artefacts in the kinase assay (detergent control changes the IC50 by less than 2-fold). Falsifier: a detergent-sensitive IC50, which would suggest the published potency is partly artefactual.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): biochemical kinase assay — recombinant Wee1, CHEMBL6065998, CHEMBL5761564 and adavosertib on one plate, n=3, with detergent and redox controls to expose PAINS artefacts; readout IC50. Stage 2 (weeks 4–6): cellular target engagement — pY15-CDK1 Western blot and γ-H2AX in TP53-mutant ovarian cancer cells (CCNE1-overexpressing), plus a colony-forming-unit assay on healthy bone-marrow progenitors for the same compounds; readout pY15 reduction and progenitor IC50. Stage 3 (weeks 7–12): if a compound passes stages 1–2 — Wee1 IC50 below 1 nM and a progenitor index of at least 10 — a TP53-mutant xenograft pilot against adavosertib; if none passes, publish the negative result with the ChEMBL table as the reason the hypothesis failed. No animal work is proposed before stages 1–2 pass.

## 5. Limitations

1. Docking only, on a single inhibitor-bound conformation; Vina noise is ±1–2 kcal/mol and the measured same-molecule reproducibility gap is 0.44 kcal/mol, so no ranking is claimed.
2. The leads' IC50s and adavosertib's Kd come from different assay formats and documents; the "~10-fold" gap is order-of-magnitude, not head-to-head.
3. The pocket is adavosertib's own site (QT9 is an adavosertib analogue), so the docking favours adavosertib-like molecules — a bias, not a neutral test.
4. Adavosertib's PLK1 off-target activity (equally potent, Zhu et al. 2017) is not modelled here; a lead's selectivity against PLK1 is untested.
5. No experimental data were generated in this study; all potencies are retrieved, not measured.
6. No Pakistani data exist on TP53 or CCNE1 frequencies in ovarian or endometrial cancer, and no local study reports Wee1-inhibitor outcomes, so the policy section recommends testing infrastructure, not a drug decision.
7. The classical-canon sweep did not re-read the Canon or Kitab al-Hawi in full; the Islamic-principle discussion rests on hifz al-nafs and la darar as principles, not on a classical source about this target. The full 23 volumes of Kitab al-Hawi exist in English only in selections.

## 6. Conclusion

Nothing beats adavosertib on Wee1 docking: the top five span 0.45 kcal/mol, and adavosertib docked twice differs from itself by 0.44 kcal/mol, so the ranking is noise and no lead is declared. By measurement the leads are ~10-fold more potent (IC50 0.2–0.3 nM vs Kd 3.2 nM), and two of them are PAINS-clean where adavosertib carries the anil_di_alk alert — but a more potent Wee1 inhibitor may simply be more myelosuppressive, and the therapeutic index, not the potency, is the bottleneck. The next step is the cheap, decisive test: one kinase assay plus one bone-marrow progenitor assay, not a bigger docking screen.

## 7. Policy implications

**Decision-maker:** Pakistan's Drug Regulatory Authority (DRAP) and the Ministry of National Health Services, with the Shaukat Khanum Memorial Cancer Hospital and the Aga Khan University Hospital oncology departments as the technical arms. **Decision:** whether to spend anything on a Wee1 programme for ovarian and endometrial cancer, and what must exist first. **Exact change:** do not fund a docking screen or import a Wee1 inhibitor on a docking score — this paper shows the docking ranking is noise, and the class's dose-limiting toxicity is myelosuppression; instead, fund TP53 and CCNE1 testing in ovarian and endometrial cancer, so the patients who respond (TP53-mutant, CCNE1-overexpressing) are identified before any drug is considered. **If evidence Z appears, reverse this:** if local testing shows CCNE1 overexpression is common in Pakistani ovarian cancer and a lead confirms a progenitor index above 10, move to a drug-evaluation assessment for that lead; if CCNE1 overexpression is rare, or if the progenitor assay shows no index, drop the programme — do not proceed to any drug evaluation on docking scores alone. The Islamic principle is hifz al-nafs joined to la darar: where a biomarker can distinguish the patient who benefits from the patient who is only harmed, running the test is the obligation; prescribing a myelosuppressive drug without it would violate it. The evidence here is thin — retrieved potencies and a null docking result — so the recommendation is "build the testing", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Bauer TM, et al. Adavosertib (AZD1775) in advanced solid tumors: phase Ib study. Target Oncol. 2023;18. (175 mg BID days 1–3, 8–10; ORR 3.8%, DCR 63.8%; diarrhoea 56.3%, nausea 42.5%, fatigue 36.3%.)
2. Safety, antitumor activity, and biomarker analysis in a phase I trial of the once-daily Wee1 inhibitor adavosertib (AZD1775) in patients with advanced solid tumors. Clin Cancer Res. 2021;27(14):3834. (RPh2D 300 mg QD; 6/42 partial responses; CCNE1 overexpression; grade 4 haematologic dose-limiting toxicity.)
3. Adavosertib in TP53-mutated uterine carcinosarcoma: phase 2 trial. (ORR 22.2%, mPFS 2.7 months; terminated early after sponsor discontinued monotherapy development.) Accessed 2026-11-27.
4. Zhu JY, et al. Structural basis of Wee kinases functionality and inactivation by diverse small molecule inhibitors. J Med Chem. 2017;60:7863–7875. doi:10.1021/acs.jmedchem.7b00996. PMID: 28792760. (PDB 5V5Y; MK-1775 equally potent against PLK1.)
5. Selective Wee1 inhibitors led to antitumor activity in vitro and correlated with myelosuppression. ACS Med Chem Lett. 2023. (PDB 8BJU, 1.53 Å, Wee1 + QT9.)
6. UniProtKB P30291: Wee1-like protein kinase (WEE1), Homo sapiens, 646 aa. UniProt. Accessed 2026-11-27.
7. ChEMBL target CHEMBL5491: Wee1-like protein kinase, Homo sapiens (60 bioactivities); activities for adavosertib (duplicate record CHEMBL1976040) and CHEMBL6172478, CHEMBL5761564, CHEMBL6065998 retrieved live 2026-11-27. ChEMBL, EMBL-EBI.
8. RCSB PDB entry 8BJU: human Wee1 kinase in complex with inhibitor QT9, 1.53 Å. RCSB Protein Data Bank. Accessed 2026-11-27.
9. RCSB PDB entry 5V5Y: human Wee1 kinase domain in complex with MK1775, 1.90 Å. RCSB Protein Data Bank. Accessed 2026-11-27.
10. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Discusses swellings and tumours (waram) — cited for the hifz al-nafs principle only.)
11. Al-Ghazali. Al-Mustasfa min 'Ilm al-Usul. c. 1109. (Defines the five necessities of the law, including hifz al-nafs.)
12. Al-Shatibi. Al-Muwafaqat fi Usul al-Shari'a. 14th c. (Systematises maqasid al-shariah.)

## Data availability

All potencies, descriptors and docking scores reported here are in `hidden_files/dock-HP-124-2026-11-27.json` (LeadForge pipeline run: target UniProt P30291; ChEMBL target CHEMBL5491, 60 bioactivities; 25 similarity leads; adavosertib PubChem-verified). The docking used PDB 8BJU at the QT9 ligand centre [−14.10, −11.12, 19.32], Vina 1.2.7, box 22.5 Å, exhaustiveness 8 — no re-dock was needed: the target, structure and centre all verified on the first run. Reference drug adavosertib (PubChem C27H32N8O2; duplicate ChEMBL record CHEMBL1976040); comparators CHEMBL6172478, CHEMBL5761564, CHEMBL6065998, with measured potencies retrieved live from ChEMBL on 2026-11-27. Structure: PDB 8BJU (1.53 Å, Wee1 + QT9). No additional data were generated.
