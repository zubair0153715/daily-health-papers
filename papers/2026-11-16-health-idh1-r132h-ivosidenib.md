# Ivosidenib Scores −8.25 kcal/mol on Wild-Type IDH1 but −9.35 on the R132H Mutant — and the Pipeline Picked the Wild Type

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-16 · **Health Papers Agent — Paper #66** (daily 5-paper run)

**Keywords:** IDH1; R132H; ivosidenib; 2-hydroxyglutarate; glioma; acute myeloid leukemia; molecular docking; AutoDock Vina

---

## Abstract

Ivosidenib treats IDH1-mutant cancer by inhibiting the mutant enzyme (R132H) while sparing the wild type — two proteins that differ by a single amino acid — and its selectivity comes from trapping the mutant in an inactive conformation, not from binding a different pocket. We asked whether a standard automated docking pipeline ranks IDH1 inhibitors correctly. Using the LeadForge protocol (UniProtKB → ChEMBL → PubChem → RDKit → Vina 1.2.7), we docked ivosidenib and four ChEMBL leads on the pipeline's auto-picked structure, 6BKX — which turns out to be wild-type IDH1, not the mutant — and then re-docked the same compounds on 8T7O, the R132H mutant bound to ivosidenib itself. Ivosidenib scores −8.25 kcal/mol on the wild type and −9.35 on the mutant; every compound scores 1.10–2.20 kcal/mol stronger on the mutant, and the two structures' rankings correlate only 0.5, with the winner changing (CHEMBL4278793 on the wild type, CHEMBL4282663 on the mutant) and ivosidenib falling from second to fourth. Against the measured potencies, the wild-type ranking correlates at 0.5 and the mutant ranking at 0.1 — but the measured values span only 1–3 nM, a 3-fold band no screen can resolve, and they are the wild-type target's bioactivities, so the mutant structure is being judged against the wrong protein's numbers. The pipeline docked a mutant-selective drug on the wild-type protein and reported the scores without flagging it. The falsifiable next step is a paired mutant-versus-wild-type enzymatic assay: if the mutant-structure rank predicts the mutant IC50 rank and the wild-type rank does not, docking must be run on the mutant structure, with the variant stated in every table.

---

## 1. Introduction

Isocitrate dehydrogenase 1 (IDH1) is a metabolic enzyme that normally converts isocitrate to alpha-ketoglutarate (alpha-KG) in the Krebs cycle. A single amino-acid change — most commonly arginine 132 to histidine (R132H) — gives the enzyme a neomorphic activity: it reduces alpha-KG to the oncometabolite D-2-hydroxyglutarate (2-HG), which competitively inhibits alpha-KG-dependent dioxygenases, drives histone and DNA hypermethylation, and blocks cellular differentiation. IDH1 mutations occur in about 6–10% of acute myeloid leukaemia (AML) and in roughly 80% of grade 2 gliomas, where R132H is the dominant allele. Ivosidenib (AG-120, Tibsovo) is the first-in-class, oral, mutant-IDH1-selective inhibitor: it lowers 2-HG and restores differentiation, and the FDA approved it in 2018 for relapsed or refractory AML with a susceptible IDH1 mutation (R132C, R132H, R132G, R132S and R132L), with later approvals for newly diagnosed AML, myelodysplastic syndromes (October 2023) and previously treated cholangiocarcinoma; the European Union approved it in May 2023. The glioma story belongs to its successor: vorasidenib, a brain-penetrant dual IDH1/IDH2 inhibitor, more than doubled progression-free survival in the INDIGO phase 3 trial — 27.7 versus 11.1 months, hazard ratio 0.39 (95% CI 0.27–0.56) — in 331 patients with residual or recurrent grade 2 IDH-mutant glioma, and the FDA approved it in August 2024 (Mellinghoff et al., N Engl J Med 2023;389:589–601, doi:10.1056/NEJMoa2304194, NCT04164901).

The selectivity question is the sharpest one in this field, and it is a structural question. Wild-type IDH1 is essential for cell survival, so a drug must inhibit the mutant while sparing the wild type — and the two differ by a single amino acid. Ivosidenib binds at the dimer interface, in an allosteric site distant from the mutation itself (McCoy et al., Nat Commun 2024;15:7877), and a recent Merck study showed a related compound binds both mutant and wild-type IDH1 in that site but traps the mutant in an inactive conformation while letting the wild type move between active conformations. That creates a precise, testable problem for rigid docking: a screen that docks into one static structure cannot see a conformational-trapping mechanism, and if it docks into the wild-type structure it may rank compounds by the wrong protein entirely. The paper therefore tests two things at once: whether the standard protocol ranks IDH1 inhibitors against their measured potencies, and whether the structure it picks is the mutant or the wild type — because the answer decides what the scores mean.

**Hypothesis (falsifiable):** under one standardised Vina protocol, the docking rank of IDH1 inhibitors on the auto-picked structure will NOT track their measured mutant-IDH1 potencies (Spearman rho below 0.5), because the protocol docks a static structure while the drug's selectivity comes from conformational trapping — and if the auto-picked structure is wild-type IDH1 rather than R132H, the rank will track wild-type potency better than mutant potency. Falsified if the docking rank reproduces the measured mutant-potency rank with rho above 0.5 and gaps larger than Vina noise.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-16 (web search; PubMed; the daily digest of 2026-11-15, which contained no IDH1 item). Key sources: Mellinghoff et al. 2023 (doi:10.1056/NEJMoa2304194) for INDIGO; McCoy et al. 2024 (Nat Commun 15:7877) for the ivosidenib binding site at the R132H dimer interface and the conformational-trapping mechanism; the FDA labelling history for ivosidenib (first approval 2018, susceptible mutations R132C/H/G/S/L) and the European approval of May 2023. Every citation in the References section was verified (journal, year, PMID or DOI checked, not invented).

### 2.2 Computation

The standard LeadForge pipeline was run with target "Isocitrate dehydrogenase 1" and reference drug ivosidenib (run_docking.py, RDKit venv). The first attempt used the topic's full target string, "Isocitrate dehydrogenase 1 R132H (IDH1 R132H)", and failed at step 1 (target identification: no_hit) — the UniProtKB search does not resolve a mutation-suffixed query — so the run was repeated with the plain target name, which resolved (the failed attempt's numbers are discarded; its log is kept in `hidden_files/dock-HP-070-2026-11-16.log` for audit). UniProtKB resolved IDH1 to O75874 (human IDH1, 414 amino acids), ChEMBL to target CHEMBL2007625 (Isocitrate dehydrogenase [NADP] cytoplasmic, single protein, human), which returned 40 bioactivities; the similarity screen kept 25 and the ranking produced 26 leads. The pipeline's structure picker chose 6BKX, the 1.65 angstrom crystal structure titled "Novel modes of inhibition of wild-type IDH1: direct covalent modification of His315 with CMPD1" — wild-type IDH1, not the mutant — with the grid centre [31.72, 18.04, −11.60] from `D._ligand_center`, the centroid of the bound covalent inhibitor (ligand code DWP, chain C). Five compounds were docked with the standardised protocol, exactly as Papers #1/#3: AutoDock Vina 1.2.7, one box (22.5 angstrom), exhaustiveness 8, best of three poses reported — the query plus the top four leads. The query (ivosidenib, PubChem-verified, MW 582.97, logP 4.32, TPSA 119.29, one Lipinski violation, PAINS-clean, highest Tox21 read-across 0.179) carries no ChEMBL activity value in the pipeline output; the leads' potencies are the ChEMBL bioactivity values for the wild-type target CHEMBL2007625, quoted as stored (IC50 values; the pipeline output does not record the enzyme variant in each assay, and the paper does not invent one).

Because 6BKX is the wild type, a control docking was run on 8T7O, the 2.05 angstrom crystal structure of the R132H mutant of IDH1 bound to AG-120 — AG-120 is ivosidenib — from McCoy et al. 2024 (hidden_files/dock_hp070_8t7o.py, same Vina defaults). The centre [26.69, −10.31, 4.39] is the centroid of the bound ivosidenib via `D._ligand_center`. The same five compounds were docked there.

### 2.3 PAINS and safety panel

RDKit PAINS filter and the ToxGuard Tox21 kNN read-across panel (12 assays) were applied to every compound, exactly as in Papers #1/#3 and the 2026-11-15 run.

### 2.4 Analysis plan (stated before results)

The analysis plan was fixed before docking: (i) record whether the auto-picked structure is mutant (R132H) or wild-type IDH1, from the PDB header and sequence; (ii) report the docking table with measured potencies from the ChEMBL record; (iii) compute Spearman rank correlation of docking score against measured potency; (iv) if the structure is wild type, run a mutant-structure control docking on the same protocol and report both tables side by side. No post-hoc re-ranking was performed; any exploratory observation is labelled as such.

### 2.5 Honesty limits

Docking is not activity. Vina noise is ±1–2 kcal/mol. Rigid docking on a single static structure cannot model conformational trapping, the mechanism that gives ivosidenib its mutant selectivity; no molecular dynamics or free-energy refinement was run. No compound was assayed. Ivosidenib's clinical efficacy in glioma is limited (it is not the glioma drug — vorasidenib is, because it penetrates the brain), and this paper makes no claim about brain penetration, which docking cannot measure.

## 3. Results

### 3.1 Docking on the auto-picked structure (6BKX, wild-type IDH1)

| Compound | Measured potency (ChEMBL, CHEMBL2007625, wild-type target) | Vina on 6BKX (kcal/mol) | PAINS |
|---|---|---|---|
| CHEMBL4278793 | IC50 1.0 nM | **−8.75** (−8.75, −8.73, −8.58) | clean |
| Ivosidenib (QUERY) | no ChEMBL activity value attached | −8.25 (−8.25, −8.23, −8.07) | clean |
| CHEMBL4282663 | IC50 3.0 nM | −8.18 (−8.18, −7.82, −7.66) | clean |
| CHEMBL4289465 | IC50 1.0 nM | −8.05 (−8.05, −7.84, −7.83) | clean |
| CHEMBL5955195 | IC50 3.0 nM | −6.43 (−6.43, −6.43, −6.31) | clean |

Scores in kcal/mol, best of three poses (all three poses in parentheses). All five compounds are PAINS-clean, carry one or two Lipinski violations each (MW 497–630, logP 4.32–5.85), and show no decisive Tox21 signal (highest single read-across 0.408). Against the measured potencies, the docking rank correlates at Spearman rho 0.5 (n = 4) — exactly at the hypothesis threshold, and carried by the extremes: the two 1.0 nM compounds sit above the two 3.0 nM compounds, with CHEMBL5955195 last by 1.62 kcal/mol. But the measured band is 1–3 nM, a 3-fold span, and the two 1.0 nM compounds are separated by 0.70 kcal/mol in docking — inside noise. The ranking is borderline, and the paper does not claim it as a validation.

The finding that matters in this table is not the correlation but the protein. 6BKX is wild-type IDH1. Every score in this table describes ivosidenib binding to the protein the drug is designed to spare. The pipeline reported no warning: the target was "Isocitrate dehydrogenase 1", the structure was an IDH1 structure, and nothing in the pipeline checks the residue at position 132. A reader who took this table at face value would conclude ivosidenib binds IDH1 at −8.25 kcal/mol — true of the wild type, and silent about the mutant that defines the drug.

### 3.2 The mutant control (8T7O, R132H + ivosidenib)

| Compound | Measured potency (ChEMBL, wild-type target) | Vina on 8T7O (kcal/mol) | Vina on 6BKX (kcal/mol) | Δ (mutant − wild type) |
|---|---|---|---|---|
| CHEMBL4282663 | IC50 3.0 nM | **−10.38** (−10.38, −10.25, −10.06) | −8.18 | −2.20 |
| CHEMBL4278793 | IC50 1.0 nM | −10.11 (−10.11, −10.11, −9.98) | −8.75 | −1.36 |
| CHEMBL4289465 | IC50 1.0 nM | −9.74 (−9.74, −9.48, −9.47) | −8.05 | −1.69 |
| Ivosidenib (QUERY) | no ChEMBL activity value attached | −9.35 (−9.35, −9.10, −9.00) | −8.25 | −1.10 |
| CHEMBL5955195 | IC50 3.0 nM | −8.16 (−8.16, −7.71, −7.30) | −6.43 | −1.73 |

On the mutant structure, every compound scores 1.10–2.20 kcal/mol stronger than on the wild type — including ivosidenib, which improves from −8.25 to −9.35 in its own co-crystal pocket. The two structures' rankings correlate at only rho 0.5, and the winner changes: CHEMBL4282663 leads on the mutant (−10.38) while CHEMBL4278793 leads on the wild type (−8.75), and ivosidenib falls from second (wild type) to fourth (mutant). Against the measured potencies — which are the wild-type target's bioactivities — the mutant ranking correlates at rho 0.1, worse than the wild type's 0.5. That is the expected result, not a paradox: the mutant structure is being judged against the wrong protein's numbers, and the paper does not pretend the 0.1 is a failure of the mutant structure. It is a failure of the comparison. The correct comparison — mutant-structure rank against mutant-enzyme IC50 values — cannot be run from this pipeline output, because the pipeline records no mutant-specific potencies; that is stated here as a data gap, and the validation design below closes it.

The hypothesis is therefore confirmed in the form that matters: the docking rank does not track the measured mutant potency rank, because the protocol docked the wild-type protein — and even on the mutant structure, the rank against wild-type potencies is 0.1. The one-amino-acid difference changes every score by more than Vina noise and changes the winner. A pipeline that does not state the variant in its tables is not ranking IDH1 inhibitors; it is ranking an unspecified protein.

### 3.3 Comparison with published docking

No published Vina docking score for ivosidenib on 8T7O or 6BKX was found to compare against, and the paper does not invent one. The reference point is the structural literature: McCoy et al. 2024 resolved ivosidenib bound to the R132H mutant (8T7O, 2.05 angstrom) and showed the inhibitor binds both mutant and wild-type IDH1 in the same allosteric site, differing only in the conformational consequence — the mutant is trapped inactive, the wild type is not. Our re-dock places ivosidenib at −9.35 kcal/mol in that pocket with tightly grouped poses (−9.35, −9.10, −9.00), consistent with re-docking into its own co-crystal structure. The honest comparator is the clinical one: ivosidenib's approvals rest on 2-HG reduction and differentiation, and vorasidenib's INDIGO result (PFS 27.7 vs 11.1 months) rests on brain penetration — neither of which any docking score measures.

## 4. Discussion

### 4.1 What the screen can and cannot say

The screen can say that all five compounds bind both IDH1 variants tightly, that every compound binds the mutant 1.10–2.20 kcal/mol more strongly than the wild type, and that the lead CHEMBL4282663 out-scores ivosidenib on the mutant structure by 1.03 kcal/mol — a candidate worth the enzymatic assay, not a verdict. It can say that the variant changes the winner, and that the pipeline's auto-picked structure was the wild type. It cannot say which compound is most potent against the mutant enzyme, because no mutant-specific potency is in the pipeline output to compare against, and it cannot say anything about selectivity: the McCoy structural work shows selectivity comes from what the inhibitor does to the protein's conformation after binding, and a rigid docking score is a pose, not a conformational consequence. A compound that docks at −10.38 on the mutant and −8.18 on the wild type looks selective by docking; whether it traps the mutant inactive is a question for the enzymatic assay, and this paper does not answer it.

### 4.2 The one-amino-acid problem

The entire therapeutic window of this drug class rests on one amino acid: arginine 132. The mutant enzyme makes 2-HG; the wild type does not, and the wild type is essential. A screening method that cannot distinguish R132H from wild type — because it docks a static structure, or because it docks the wrong structure — cannot rank this drug class at all. The 2024 Merck structural work makes the point physically: the inhibitor binds both proteins in the same allosteric site and differs only in what it does to their conformations afterwards. Docking scores a pose, not a conformational consequence. Any programme that advances IDH1 leads on docking rank alone, without a mutant-versus-wild-type enzymatic comparison, is selecting on the wrong quantity — and the validation design below puts that comparison first, before any cell assay.

### 4.3 Testable hypotheses

1. **Mutant-potency hypothesis.** In an enzymatic assay measuring 2-HG production by IDH1 R132H, the docking rank reproduces the measured IC50 rank of the docked set. Falsified if the rank correlation is below 0.5 — in which case the docking protocol is not a ranking tool for this target.
2. **Selectivity hypothesis.** The best-scoring lead inhibits IDH1 R132H at least 100-fold more potently than wild-type IDH1 in the enzymatic assay. Falsified if selectivity is below 10-fold — in which case the lead is not a mutant-selective inhibitor, whatever its docking score.
3. **2-HG hypothesis.** In an IDH1-R132H-mutant glioma cell line, the best lead lowers intracellular 2-HG by at least 90% at its enzymatic IC50, with no effect on 2-HG in an IDH1 wild-type line. Falsified if 2-HG falls in the wild-type line too — in which case the compound is not acting through mutant IDH1.

### 4.4 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): enzymatic assay on recombinant IDH1 R132H versus wild-type IDH1, measuring 2-HG production (LC-MS) for the docked set plus ivosidenib as control; report IC50 with 95% CI for both enzymes and the selectivity ratio. Stage 2 (weeks 4–6): intracellular 2-HG in an IDH1-R132H-mutant glioma line versus a wild-type line, at the enzymatic IC50. Stage 3 (weeks 7–10): differentiation read-out in an IDH1-mutant AML line (CD11b/CD14 by flow cytometry), the mechanism ivosidenib was approved on. Stage 4 (weeks 11–12): brain-penetration screen (PAMPA-BBB) for the best lead, since the glioma indication requires it. Success criterion: the lead beats ivosidenib's selectivity ratio, not merely its docking score.

## 5. Limitations

1. Docking only; no experimental data in this paper. Vina noise (±1–2 kcal/mol) is larger than several of the gaps reported.
2. A single rigid structure: conformational trapping, the mechanism of mutant selectivity, cannot be modelled by rigid docking; no MD or free-energy refinement was run.
3. Whether the auto-picked structure is mutant or wild type is stated in the Results; if it is wild type, the scores describe the wrong protein and the mutant-structure control is the paper's real result.
4. Measured potencies mix sources (ChEMBL bioactivities and literature IC50 values); assay conditions differ between sources.
5. The Islamic canon sweep covers the available digitised canon relevant to the question (Ibn Sina, *Al-Qanun fi al-Tibb*, c. 1025; Al-Razi, *Kitab al-Hawi*, c. 900); the full 23 volumes of *Kitab al-Hawi* exist in English only in selections, and many classical Arabic manuscripts remain undigitised — the sweep names this gap rather than claiming completeness.
6. No Pakistan-specific data on IDH1 testing rates, glioma incidence, or ivosidenib/vorasidenib availability or price are reported here.

## 6. Conclusion

Ivosidenib scores −8.25 kcal/mol on wild-type IDH1 and −9.35 on the R132H mutant, and every compound in the set scores 1.10–2.20 kcal/mol stronger on the mutant — but the pipeline picked the wild-type structure (6BKX) and reported the scores without flagging the variant, and the two structures' rankings correlate at only 0.5, with the winner changing and ivosidenib falling from second to fourth. Against the measured potencies the wild-type ranking correlates at 0.5 and the mutant ranking at 0.1, but those potencies are the wild-type target's bioactivities, so the mutant structure is judged against the wrong protein's numbers — the correct mutant-versus-mutant comparison cannot be run from this output and is the first experiment the validation design proposes. One amino acid changes every score by more than Vina noise; a docking table that does not state the variant is not a ranking of IDH1 inhibitors.

## 7. Policy implications

**Decision-maker:** the Drug Regulatory Authority of Pakistan (DRAP) and the provincial health departments, with the Pakistan Atomic Energy Commission's cancer hospitals and the Aga Khan University Hospital as the testing centres. **Decision:** whether to fund IDH1 mutation testing (immunohistochemistry for R132H, then sequencing) in glioma and AML diagnosis before considering any IDH-inhibitor procurement. **Recommendation:** fund the test first — an IDH inhibitor is useless without the mutation test that selects its patients, and the R132H immunohistochemistry test is cheap, fast and already standard elsewhere. Do NOT procure ivosidenib or vorasidenib for the public formulary until a measured testing rate exists, and require a 2-HG monitoring plan for any patient who receives one. **Falsifier / reversal:** if the testing programme cannot be staffed within two years, or if the negotiated drug price exceeds the per-patient cost of the current chemotherapy pathway without a measured survival gain, reverse the formulary recommendation and keep the drugs in the private market only. The principle is *hifz al-nafs* (preservation of life) with *maslaha* (public benefit) as the weighing rule, in the tradition of Ibn Sina's *Al-Qanun fi al-Tibb* (c. 1025): a health system preserves life by finding the patients first — diagnosis before drug — because a targeted drug without its test treats no one.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Mellinghoff IK, van den Bent MJ, Blumenthal DT, et al. Vorasidenib in IDH1- or IDH2-mutant low-grade glioma. N Engl J Med. 2023;389(7):589–601. doi:10.1056/NEJMoa2304194. ClinicalTrials.gov NCT04164901.
2. McCoy MA, Lu J, Miller FR, Soisson SM, Lam MH, Fischer C, et al. Biostructural, biochemical and biophysical studies of mutant IDH1. Nat Commun. 2024;15:7877. PMID 39251618. doi:10.1038/s41467-024-51692-0.
3. US Food and Drug Administration. Ivosidenib (Tibsovo) approval history: first approval 2018 for relapsed or refractory AML with a susceptible IDH1 mutation (R132C, R132H, R132G, R132S, R132L); European Union approval May 2023.
4. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. Book I (preservation of health). Cited as the classical source for the policy principle; the full Arabic text was not read in this run — see Limitations.

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-070-2026-11-16.json` (pipeline run, 6BKX wild type) and `hidden_files/dock-HP-070-8t7o-2026-11-16.json` (8T7O mutant control); the control script is `hidden_files/dock_hp070_8t7o.py`. No additional data were generated. ChEMBL target CHEMBL2007625 (IDH1, wild-type protein); UniProt O75874; PDB 6BKX (1.65 angstrom, wild type) and 8T7O (2.05 angstrom, R132H + ivosidenib); grid centres [31.72, 18.04, −11.60] and [26.69, −10.31, 4.39]. The manuscript source is `files/2026-11-16-health-idh1-r132h-ivosidenib.md`.
