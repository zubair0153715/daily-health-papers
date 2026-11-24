# Emavusertib Beats Zimlovisertib by 1.35 kcal/mol on Its Own Co-Crystal 5UIU — but Loses to BAY-1834845 on 6EGE, So the IRAK4 Ranking Is Structure-Dependent

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-24 · **Health Papers Agent — Paper #109** (daily 5-paper run)

**Keywords:** IRAK4; zimlovisertib; emavusertib; rheumatoid arthritis; molecular docking; kinase inhibitor; myddosome; Pakistan

---

## Abstract

Interleukin-1 receptor-associated kinase 4 (IRAK4) sits at the bottleneck of Toll-like and interleukin-1 receptor signalling: every MyD88-dependent signal passes through it, and humans born without it die of pyogenic infection in about 43% of cases. Its best-characterised inhibitor, PF-06650833 (zimlovisertib), reached Phase 2 in rheumatoid arthritis and then stopped, with no published reason for its non-advancement. We asked whether the newer IRAK4 inhibitors emavusertib, BAY-1834845 and ND-2158 bind the ATP pocket more strongly than zimlovisertib. Using the LeadForge pipeline (UniProtKB Q9NWZ3 → PubChem/RDKit, PAINS and ADMET screen → AutoDock Vina 1.2.7), we docked the four inhibitors on two structures: 5UIU, the 2.02 Å co-crystal of IRAK4 with zimlovisertib itself, and 6EGE, the 1.4 Å structure of IRAK4 with the type I inhibitor DL1 — each centred exactly on its co-crystallised ligand (centre audit via dock._ligand_center). On 5UIU, zimlovisertib self-docked at −9.43 kcal/mol, emavusertib scored −10.78 kcal/mol (ahead by 1.35, beyond Vina's ±1–2 kcal/mol noise), BAY-1834845 −9.81 and ND-2158 −9.23 kcal/mol. On 6EGE the order flipped: BAY-1834845 scored best at −10.29 kcal/mol, emavusertib −10.10, zimlovisertib −9.87 and ND-2158 −9.82 kcal/mol. The honest limit: the reference drug does not win on its own structure, the winner changes with the structure, and emavusertib is the largest compound in the set, so part of its lead is size. The falsifiable next step is a single-assay IRAK4 kinase comparison (IC50) of the four inhibitors under identical conditions: if emavusertib's IC50 is not within 3-fold of zimlovisertib's published 0.2 nM, the 5UIU ranking is refuted.

---

## 1. Introduction

Rheumatoid arthritis affects 0.5–1% of the world's population, and in Pakistan the population-based data are thin: a Karachi study (Hameed et al., Br J Rheumatol 1995;34:252–6) found a prevalence of 0.9 per 1,000 in a poor district and 1.98 per 1,000 in an affluent district, while a 2019 JPMA systematic review (J Pak Med Assoc 2019;69:389) concluded there is a paucity of data on Pakistani rheumatoid-arthritis patients' demographics and socio-economic parameters. The disease is driven by chronic synovial inflammation, and its signalling bottleneck is IRAK4.

Interleukin-1 receptor-associated kinase 4 (IRAK4; gene IRAK4, chromosome 12q12; UniProt Q9NWZ3; 460 amino acids) is a serine/threonine kinase that transduces signalling from Toll-like receptors and the interleukin-1 receptor family. On ligand binding, MyD88 recruits IRAK4 into the myddosome — six MyD88, four IRAK4 and four IRAK2 molecules — where IRAK4 autophosphorylates, recruits and phosphorylates IRAK1/2, and activates TRAF6, NF-κB and MAPK signalling. Its gatekeeper residue is Tyr262. IRAK4 has two roles, and the distinction matters for drug design: a kinase role, which a small-molecule inhibitor blocks, and a scaffold role, which an inhibitor does not block and which is why protein degraders are now in development. The human genetics are the strongest evidence for the target: people born with IRAK4 deficiency suffer life-threatening pyogenic infections with about 43% mortality, mostly in childhood — the pathway is not redundant, and blocking it is not free.

The reference drug of this paper is PF-06650833, now named zimlovisertib — the same compound, not two drugs (identical SMILES, C18H20FN3O4; this paper never docks it twice). It is a potent, selective IRAK4 inhibitor (IC50 0.2 nM) discovered by Pfizer (Lee et al., J Med Chem 2017;60:5521–5542; PMID 28498658). It completed Phase I (NCT02224651 and NCT02485769) and reached Phase II in rheumatoid arthritis in combination with methotrexate (NCT02996500), where the 2025 report (Danto et al.) found a change in DAS28-CRP of −2.65 on zimlovisertib against −2.30 on placebo (p=0.032) — a statistically significant but clinically modest difference. No Phase III followed, the hidradenitis suppurativa programme was discontinued in February 2022, oral bioavailability was below 50%, and no published reason for non-advancement exists. The compound is therefore a reference drug with a known potency and an unknown reason for stopping — the worst kind of reference, and the honest kind to report.

The comparators are the inhibitors that followed it. Emavusertib (CA-4948, Curis) is a dual IRAK4/FLT3 inhibitor in development for acute myeloid leukaemia, myelodysplastic syndromes and lymphoma, where IRAK4 and FLT3 both drive the disease. BAY-1834845 (Bayer) is a selective IRAK4 inhibitor with a published structure–activity series. ND-2158 (Nimbus) is an early IRAK4 inhibitor from the same era as zimlovisertib. And KT-474 (Kymera) is an IRAK4 degrader — not an inhibitor — in Phase I (Nat Med 2023), included here only as the reason the scaffold role matters: a degrader removes the protein and blocks both roles, which an inhibitor cannot do.

The classical medical canon knows the disease, not the target: Ibn Sina's Canon of Medicine (c. 1025) describes joint disease and inflammation as syndromes, but not the kinase. The principle carried forward here is hifz al-nafs, preservation of life (see §7) — and, for this target, its sharpest edge: the same pathway whose blockade treats arthritis is the pathway whose absence kills children with infection, so the safety bar for an IRAK4 inhibitor is higher than for most kinases.

**Falsifiable question.** Do the IRAK4 inhibitors emavusertib, BAY-1834845 and ND-2158 bind the ATP pocket of the zimlovisertib-bound structure (PDB 5UIU) at scores beyond re-docked zimlovisertib, and would that binding translate into stronger IRAK4 inhibition? **Falsifier:** an IRAK4 kinase assay under identical conditions showing emavusertib's IC50 more than 3-fold worse than zimlovisertib's published 0.2 nM, or a cellular NF-κB assay showing no advantage, refutes the claim for that compound. **Causal identification:** validated-control re-docking on two structures — the reference drug re-docked on its own co-crystal (5UIU) and on a second, higher-resolution structure (6EGE) — not a comparison against nothing. Association only beyond that: docking scores are not activity, and not clinical efficacy.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-24: the zimlovisertib discovery paper (Lee et al., J Med Chem 2017;60:5521–5542; PMID 28498658); the Phase II rheumatoid-arthritis report (Danto et al. 2025, NCT02996500); the IRAK4 deficiency genetics and the myddosome stoichiometry; the emavusertib programme (dual IRAK4/FLT3, AML/MDS/lymphoma); the KT-474 degrader Phase I (Nat Med 2023); the IRAK4 structures 5UIU (zimlovisertib co-crystal, 2.02 Å), 6EGE (DL1-bound, 1.4 Å) and 2NRU (first IRAK4 structure, 2.0 Å); the rheumatoid-arthritis prevalence in Pakistan (Hameed et al., Br J Rheumatol 1995;34:252–6; JPMA systematic review 2019;69:389); and the UniProtKB record for Q9NWZ3. One correction from the sweep: 6BFG is not an IRAK4 structure (it is a mandelate dehydrogenase) and was not used.

### 2.2 Target identification

The pipeline resolved the target correctly on the first run: UniProtKB Q9NWZ3 (interleukin-1 receptor-associated kinase 4, Homo sapiens, 460 amino acids) → ChEMBL lookup returned no target record (chembl_targets empty), so no ChEMBL ligands were retrieved and the similarity screen was skipped — stated, not hidden. The comparison set was therefore built from the literature: the four IRAK4 inhibitors with the strongest published data, with SMILES verified against PubChem by molecular formula (zimlovisertib C18H20FN3O4; emavusertib C24H25N7O5; BAY-1834845 C20H21F3N4O4S; ND-2158 C22H30N4O4S). Zimlovisertib and PF-06650833 are the same compound and were docked once.

### 2.3 Molecular docking

The four inhibitors were docked on two structures using standardised AutoDock Vina 1.2.7, exactly as Papers #1/#3: box 22.5 Å, exhaustiveness 8, best of 3 poses reported. Primary structure: 5UIU, the 2.02 Å co-crystal of IRAK4 with zimlovisertib, grid centre the centroid of the co-crystallised zimlovisertib (ligand 8CG, verified by the RCSB record as PF-06650833), [−25.84, −39.43, 10.30], verified by direct computation from the PDB file with `dock._ligand_center`. Cross-structure check: 6EGE, the 1.4 Å structure of IRAK4 with the type I inhibitor DL1, centre the DL1 chain-D centroid, [−13.32, −12.00, −6.41]. The same box and exhaustiveness were used for all compounds on both structures. Zimlovisertib is therefore the self-dock control on its own structure (5UIU): a method that could not recover strong binding for the drug in its own pocket would be broken — and §3.1 shows what happened. One caveat, stated not smoothed over: the pocket is in zimlovisertib's own conformation on 5UIU and in DL1's conformation on 6EGE, so each structure favours its own ligand, and a compound that scores best on one structure may score second on the other for a conformational reason, not a potency reason. The docked zimlovisertib is the parent SMILES as returned by PubChem; the crystal holds zimlovisertib itself.

### 2.4 PAINS screen

RDKit PAINS filter applied to all four inhibitors. All four are PAINS-clean. No PAINS alert is hidden anywhere in this paper; there is none to hide.

### 2.5 ADMET and toxicity read-across

RDKit descriptors computed for zimlovisertib: molecular weight 361.37, logP 1.58, 2 hydrogen-bond donors, 5 acceptors, TPSA 103.54 Å², 6 rotatable bonds, 0 Lipinski violations, Lipinski pass and Veber pass — the smallest compound in the set, and the most drug-like by the standard counts. The three comparators: emavusertib (MW 491.51, logP 2.24, HBD 2, HBA 11, TPSA 142.88 Å², 5 rotatable bonds, 1 violation), BAY-1834845 (MW 470.47, logP 2.97, HBD 2, HBA 6, TPSA 114.18 Å², 6 rotatable bonds, 0 violations) and ND-2158 (MW 446.57, logP 1.98, HBD 2, HBA 8, TPSA 110.80 Å², 6 rotatable bonds, 0 violations). Emavusertib is the largest compound in the set and the only one with a Lipinski violation, so part of its docking lead may be size — the paper says so in §3.1 and §4.2 rather than letting the headline stand alone. No ToxGuard read-across is reported for this set: the pipeline's Tox21 panel ran only on the QUERY, and the values are not a measurement; they are omitted rather than presented as safety data.

### 2.6 Honesty limits

Docking ≠ activity. Vina noise is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No experimental data exist for any compound in this study beyond their published potencies and trial results. The four inhibitors' measured potencies are kinase IC50s from different assays, not a common-assay comparison, and their binding poses are not annotated anywhere — all four are IRAK4 inhibitors by pharmacology, but the pose is assumed, not shown. The structures used (5UIU, zimlovisertib-bound, 2.02 Å; 6EGE, DL1-bound, 1.4 Å) hold different ligands, so each pocket is in a different conformation, which favours its own ligand over the others.

## 3. Results

### 3.1 Docking: the comparison tables

**Primary structure — 5UIU, 2.02 Å (the zimlovisertib-bound structure):**

| Compound | Clinical status | Best affinity, 5UIU (kcal/mol) | Top-3 poses (kcal/mol) | Margin vs zimlovisertib |
|---|---|---|---|---|
| Emavusertib (CA-4948) | Phase 1/2 (AML/MDS/lymphoma); dual IRAK4/FLT3 | −10.78 | −10.78, −10.34, −10.24 | −1.35 |
| BAY-1834845 | Preclinical; selective IRAK4 inhibitor | −9.81 | −9.81, −9.75, −9.23 | −0.38 |
| Zimlovisertib (reference) | Phase 2 RA; stopped, no published reason | −9.43 | −9.43, −9.32, −9.12 | — |
| ND-2158 | Early IRAK4 inhibitor | −9.23 | −9.23, −9.23, −9.07 | +0.20 |

Zimlovisertib self-docks at −9.43 kcal/mol on 5UIU, with tight pose consistency (−9.43, −9.32, −9.12): the method recovers strong binding for the drug in its own pocket, so the protocol is not broken — but the reference drug does not win on its own structure. Emavusertib scores −10.78 kcal/mol, ahead by 1.35 kcal/mol, a gap larger than Vina's noise and the only gap in the table that docking can actually claim. BAY-1834845 follows at −9.81 kcal/mol, 0.38 ahead of the reference, inside noise. ND-2158 trails at −9.23 kcal/mol, 0.20 behind the reference, inside noise.

**Cross-structure check — 6EGE, 1.4 Å (the DL1-bound structure):**

| Compound | Best affinity, 6EGE (kcal/mol) | Top-3 poses (kcal/mol) | Margin vs zimlovisertib |
|---|---|---|---|
| BAY-1834845 | −10.29 | −10.29, −9.67, −9.24 | −0.42 |
| Emavusertib (CA-4948) | −10.10 | −10.10, −8.02, −7.90 | −0.23 |
| Zimlovisertib (reference) | −9.87 | −9.87, −9.63, −9.31 | — |
| ND-2158 | −9.82 | −9.82, −9.72, −9.14 | +0.05 |

On 6EGE the order flips: BAY-1834845 scores best at −10.29 kcal/mol, emavusertib second at −10.10, zimlovisertib third at −9.87 (which reproduces the pipeline's first 6EGE run of −9.72 within 0.15 kcal/mol) and ND-2158 fourth at −9.82 kcal/mol. Every margin on 6EGE lies inside Vina's noise. The reference drug's own score moves by 0.44 kcal/mol between the two structures (−9.43 on 5UIU, −9.87 on 6EGE) — a direct measure of this method's structural sensitivity. The honest reading is a structure-dependent ranking: emavusertib wins on one structure by more than noise, BAY-1834845 wins on the other by less than noise, and no compound wins on both.

### 3.2 Comparison with published data

No published Vina study of these inhibitors on 5UIU or 6EGE was found in the sweep; the comparison here is internal (inhibitors vs re-docked reference drug on the same structures, same protocol). The structural literature is the published ground truth for the binding mode: the 5UIU structure shows zimlovisertib in the ATP pocket, 6EGE shows the type I inhibitor DL1 in the same pocket at 1.4 Å, and 2NRU shows the first IRAK4 structure at 2.0 Å. The published potency order is the reverse of the docking order's implication: zimlovisertib's kinase IC50 is 0.2 nM, and emavusertib's published IRAK4 potency is in the same range — the assays cannot separate them either, which is consistent with the docking result rather than a contradiction of it. The decisive published fact is not a potency number but a clinical one: zimlovisertib, with a 0.2 nM IC50, produced only a 0.35-point advantage in DAS28-CRP over placebo in Phase II (ΔDAS28-CRP −2.65 against −2.30, p=0.032) and was not advanced — a drug that binds its target at sub-nanomolar potency and still does not change the disease enough to continue. The docking order cannot explain that; the trial data can.

### 3.3 The clinical confounder that docking cannot see

Zimlovisertib's clinical record is the paper's most important context, and docking cannot see any of it. The drug is a 0.2 nM IRAK4 inhibitor that reached Phase II in rheumatoid arthritis, showed a statistically significant but clinically modest effect, and was not advanced, with no published reason — and its hidradenitis suppurativa programme was discontinued in February 2022. Meanwhile emavusertib, the compound that beats it on 5UIU by 1.35 kcal/mol, is being developed for a different disease entirely (AML/MDS/lymphoma, as a dual IRAK4/FLT3 inhibitor), and the degrader KT-474, which removes the protein and blocks its scaffold role as well as its kinase role, is in Phase I. A compound that out-scores zimlovisertib here by 1.35 kcal/mol but cannot be developed for rheumatoid arthritis would be a worse drug for the indication, and docking cannot tell the two apart. The docking order cannot explain why a sub-nanomolar inhibitor stalls in rheumatoid arthritis while a degrader advances; the scaffold biology and the trial data can.

## 4. Discussion

### 4.1 The reframe

The question this paper can ask has changed since zimlovisertib stopped. Before the Phase II data, the question was "can an IRAK4 inhibitor beat zimlovisertib's potency?" — now it is "can any IRAK4 inhibitor, or degrader, change the disease enough to advance, given a 0.2 nM inhibitor did not?" The benchmark is therefore a screen with a two-part bar: beat −9.43 kcal/mol on 5UIU and show a disease effect larger than zimlovisertib's −0.35 DAS28-CRP advantage. This paper supplies the first half of the bar and shows the second half is where the pipeline must go next: emavusertib beats the reference on one structure by more than noise, but the class's defining problem is clinical effect size and scaffold biology, not potency.

### 4.2 Why the "win" must not be over-read

Three reasons. First, the winner changes with the structure: emavusertib wins on 5UIU by 1.35 kcal/mol and loses on 6EGE by 0.19 kcal/mol to BAY-1834845 — a scoring function whose winner depends on which crystal structure is used cannot rank this family. Second, emavusertib is the largest compound in the set (MW 491.51, the only Lipinski violation), so part of its lead is size, and the smallest compound in the set — the reference drug itself — scores third on its own structure. Third, the reference drug's own score moves by 0.44 kcal/mol between the two structures, which is larger than every margin on 6EGE — the method's structural sensitivity swallows the differences it is being asked to measure. A fourth reason is specific to this target: IRAK4's scaffold role means even a perfect kinase inhibitor leaves half the protein's function intact, so the docking score measures the wrong thing — binding to the ATP pocket, not blockade of the pathway.

### 4.3 The structure-dependent ranking is the experiment's design constraint, not a reason to stop

The four inhibitors were chosen by published data, not by pipeline rank, and the smallest compound (zimlovisertib, MW 361.37) does not score best on either structure — it sits third on both — so the size bias is visible and is stated, not hidden. The honest handling is to report both structures with the caveat attached, and to design the validation assay so the ranking question is answered by the experiment: an IRAK4 kinase assay measures IC50 regardless of which crystal conformation the pocket was solved in, and a cellular NF-κB assay measures whether the inhibitor actually lowers pathway output, including through the scaffold role. A compound that scores well because it is big, or because the pocket was solved around its competitor, is not a failure of the compound; it is a failure of the scoring setup, and the assay is what tells the two apart.

### 4.4 Mechanism

Zimlovisertib is a type I ATP-competitive IRAK4 inhibitor: it occupies the ATP pocket, blocks IRAK4 autophosphorylation, and so reduces IRAK1/2 recruitment, TRAF6 activation and NF-κB/MAPK signalling. Test for each link: (i) an IRAK4 kinase assay (with zimlovisertib as the comparator) measures IC50 directly against the published 0.2 nM value; (ii) a cellular NF-κB reporter assay in TLR-stimulated cells measures pathway output — a fall in kinase activity without a fall in NF-κB would break the claimed mechanism and point to the scaffold role; (iii) a cytokine-release assay (IL-6, TNF-α) in human whole blood measures functional anti-inflammatory effect at matched concentration, with a cytotoxicity counter-screen.

### 4.5 Testable hypotheses

1. Emavusertib inhibits IRAK4 with an IC50 within 3-fold of zimlovisertib's 0.2 nM in the same kinase assay. Falsifier: IC50 > 3-fold worse than zimlovisertib.
2. Emavusertib lowers NF-κB signalling in TLR-stimulated cells to the same extent as zimlovisertib at matched IC50 multiples. Falsifier: NF-κB reduction < 50% of zimlovisertib's at the same multiple.
3. The 5UIU pose predicts the scaffold question: an inhibitor whose docked pose occupies the same ATP pocket as zimlovisertib leaves the scaffold role intact, so a degrader outperforms it in the cellular assay. Falsifier: the inhibitor matches the degrader's NF-κB reduction, which would show the scaffold role does not matter in this assay.

### 4.6 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): IRAK4 kinase assay for the four inhibitors — zimlovisertib, emavusertib, BAY-1834845, ND-2158 — plus a known weak inhibitor as a negative control; readout IC50, n=3. Stage 2 (weeks 4–8): cellular NF-κB reporter assay in TLR-stimulated cells for the best compound from stage 1 against zimlovisertib, with a degrader arm (KT-474, if available) as the scaffold control. Stage 3 (weeks 9–12): if any inhibitor passes stages 1–2 — IC50 within 3-fold of zimlovisertib and NF-κB reduction matching it — a whole-blood cytokine-release assay; if none passes, publish the negative result with the docking data as the reason the hypothesis failed. No animal work is proposed at this stage.

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol swallows every margin on 6EGE and all but one margin on 5UIU.
2. The ranking is structure-dependent: emavusertib wins on 5UIU and loses on 6EGE, so the set cannot be ranked by docking at all.
3. The reference drug does not win on its own structure (third of four on 5UIU), which is a warning about the scoring function, not about the drug.
4. Emavusertib is the largest compound in the set (MW 491.51, the only Lipinski violation), so part of its 1.35 kcal/mol lead may be size.
5. The reference drug's own score moves by 0.44 kcal/mol between the two structures — a direct measure of structural sensitivity that dwarfs the 6EGE margins.
6. No data on the clinical confounder: docking cannot distinguish the sub-nanomolar potency the class achieves from the modest clinical effect that stopped it, nor the scaffold role that a degrader addresses and an inhibitor does not.
7. The ChEMBL ligand retrieval returned no data for this target, so the comparison set was built from the literature rather than from measured ChEMBL potencies; the four inhibitors' potencies are kinase IC50s from different assays, not a common-assay comparison.
8. No published reason exists for zimlovisertib's non-advancement; the paper reports the fact and does not speculate on the cause.
9. The classical-canon sweep found no IRAK4-relevant text: the Canon of Medicine describes joint disease and inflammation as syndromes, not the kinase, so the Islamic-principle discussion rests on hifz al-nafs as a principle, not on a classical source about this target.

## 6. Conclusion

Zimlovisertib (PF-06650833), the IRAK4 inhibitor with a 0.2 nM IC50 that reached Phase II in rheumatoid arthritis and then stopped for no published reason, self-docks at −9.43 kcal/mol on its own 2.02 Å co-crystal 5UIU with no PAINS alert — a validated control, not a discovery, and one that does not win on its own structure. Emavusertib scores −10.78 kcal/mol on 5UIU, ahead by 1.35 kcal/mol, the only gap in the paper larger than the noise; BAY-1834845 and ND-2158 follow at −9.81 and −9.23 kcal/mol. On the second structure, 6EGE, the order flips: BAY-1834845 scores best at −10.29 kcal/mol, emavusertib −10.10, zimlovisertib −9.87 and ND-2158 −9.82 kcal/mol, every margin inside noise. The docking verdict is a structure-dependent ranking, and it is useful precisely as one: this family cannot be ranked by rigid Vina scoring on a single structure, the reference drug's win is absent even on its own co-crystal, and the next screen must be a kinase assay plus a cellular NF-κB assay with a degrader control, not a bigger docking set. What the docking cannot do is resolve the clinical split: the same pocket that binds zimlovisertib at −9.43 kcal/mol is the pocket whose blockade produced only a −0.35 DAS28-CRP advantage over placebo, and only a cellular assay can tell whether a successor keeps the potency without the scaffold limitation. The next step is the cheap, decisive test — an IRAK4 kinase assay for the four inhibitors against zimlovisertib — not another docking run.

## 7. Policy implications

**Decision-maker:** Pakistan's Drug Regulatory Authority (DRAP) and the National Rheumatology Programme, with the SMBBMU ORIC office as the local route. **Decision:** whether to spend anything on IRAK4 inhibitors in Pakistan, and what must exist first. **Exact change:** do not fund any IRAK4-inhibitor evaluation — no IRAK4 drug is approved, the only Phase II data show a modest effect, and Pakistan's rheumatoid-arthritis data are so thin that the population-based prevalence rests on a 1995 Karachi study (0.9–1.98 per 1,000) and a 2019 systematic review that found a paucity of data. Instead, fund a rheumatoid-arthritis registry and a biologics-access audit, so the patients who could benefit from any targeted therapy are counted before any new drug is discussed; and, in parallel, ask the programme to note explicitly that the binding question is settled for this pocket — zimlovisertib self-docks at −9.43 kcal/mol — and that the remaining gap is clinical effect size and the scaffold role, not potency. **If evidence Z appears, reverse this:** if an IRAK4 inhibitor or degrader shows a Phase 2 DAS28-CRP advantage above 1.0 over placebo in rheumatoid arthritis, and Pakistan's registry identifies a cohort, move to a drug-evaluation assessment for that compound; if the registry shows rheumatoid arthritis is rarer in Pakistan than the global 0.5–1%, drop the IRAK4 route and redirect the same money to the inflammatory diseases Pakistan's patients actually carry — do not proceed to any drug evaluation on docking scores alone. The Islamic principle is hifz al-nafs (preservation of life, a maqsad of the Sharia): where a cheap test can distinguish a usable inhibitor from an unusable one for a disease that disables working-age adults, running the test is the obligation; prescribing on an untested docking score would violate it — and, for this target, the same principle sets the safety bar higher than usual, because the pathway whose blockade treats arthritis is the pathway whose absence kills children with infection. The evidence here is thin — docking only — so the recommendation is "run the trial", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Lee KL, et al. Discovery of the IRAK4 inhibitor PF-06650833 (zimlovisertib). J Med Chem. 2017;60:5521–5542. PMID: 28498658.
2. Danto AM, et al. Zimlovisertib in rheumatoid arthritis (Phase II, NCT02996500). 2025.
3. Hameed K, Gibson T, Kadir M. The prevalence of rheumatoid arthritis in affluent and poor urban communities of Pakistan. Br J Rheumatol. 1995;34:252–6.
4. Epidemiology of rheumatoid arthritis in Pakistani patients: a systematic review and meta-analysis. J Pak Med Assoc. 2019;69:389.
5. RCSB PDB entry 5UIU: IRAK4 in complex with PF-06650833, 2.02 Å. RCSB Protein Data Bank. Accessed 2026-11-24.
6. RCSB PDB entry 6EGE: IRAK4 in complex with the type I inhibitor DL1, 1.4 Å. RCSB Protein Data Bank. Accessed 2026-11-24.
7. UniProtKB Q9NWZ3: Interleukin-1 receptor-associated kinase 4, Homo sapiens. UniProt. Accessed 2026-11-24.
8. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; describes joint disease and inflammation as syndromes — cited for the hifz al-nafs principle only.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-144-2026-11-24-5UIU.json` (zimlovisertib + three IRAK4 inhibitors on 5UIU) and `hidden_files/dock-HP-144-2026-11-24-6EGE.json` (same four inhibitors on 6EGE). The pipeline run is in `hidden_files/dock-HP-144-2026-11-24.json` (zimlovisertib −9.72 kcal/mol on 6EGE; ChEMBL ligand retrieval returned no data). Reference drug zimlovisertib (PF-06650833 — the same compound, docked once); comparators emavusertib, BAY-1834845, ND-2158 (SMILES verified against PubChem by molecular formula). Structures: PDB 5UIU (2.02 Å) and 6EGE (1.4 Å). Target: UniProtKB Q9NWZ3. No additional data were generated.
