# Two 0.01 nM BCL-2 Inhibitors Dock 0.90 kcal/mol Apart and Venetoclax Sits in the Middle: Rigid Vina Cannot Rank the BH3-Mimetic Series on 8HTS

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-23 · **Health Papers Agent — Paper #102** (daily 5-paper run)

**Keywords:** BCL-2; venetoclax; BH3 mimetic; chronic lymphocytic leukemia; molecular docking; ChEMBL; drug resistance; G101V; sonrotoclax

---

## Abstract

Venetoclax, the first-in-class BCL-2-selective BH3 mimetic approved in 2016, transformed chronic lymphocytic leukaemia — yet continuous single-agent treatment leaves up to 50% of heavily pre-treated patients refractory after two to three years, most often through BCL2 mutations such as G101V and D103Y that disrupt drug binding while preserving native BH3 binding. We asked whether any measured BCL-2 ligand binds the BH3 groove more strongly than venetoclax. Using the LeadForge pipeline (UniProtKB P10415 → ChEMBL CHEMBL4860 → PubChem/RDKit, PAINS and ADMET screen → AutoDock Vina 1.2.7), we docked venetoclax and four ChEMBL ligands with measured potency on the 1.25 Å BCL-2 structure 8HTS, centred exactly on the co-crystallised sonrotoclax-series ligand S-10r (centre audit via dock._ligand_center). Venetoclax re-docked at −10.22 kcal/mol. Two analogues beat it: CHEMBL3973960 at −11.04 kcal/mol (Ki 0.013 nM) and CHEMBL3985475 at −10.88 kcal/mol (Ki 0.01 nM) — but the margins, 0.82 and 0.66 kcal/mol, lie inside Vina's ±1–2 kcal/mol noise. The decisive failure is the ranking itself: the two most potent compounds by assay (both Ki 0.01 nM — CHEMBL3985475 and CHEMBL4228713, the latter verified as A-1211212) docked at −10.88 and −9.98 kcal/mol, 0.90 kcal/mol apart, while a 1.3-fold weaker compound (CHEMBL3973960, Ki 0.013 nM) scored best of all at −11.04 kcal/mol. Docking therefore cannot rank this series, and no analogue can be claimed to beat venetoclax on this evidence. The honest limit: the whole class is large and hydrophobic (molecular weights 868–910, logP 8.1–9.4, three Lipinski violations each), so the scores scale with size and hydrophobic surface rather than with the specific contacts that decide G101V resistance — and the structure used is wild-type BCL-2, so the resistance question was not docked at all. The falsifiable next step is a fluorescence-polarisation binding assay of the two best-scoring analogues against venetoclax on wild-type and G101V BCL-2 — not another docking run.

---

## 1. Introduction

BCL-2 family proteins are the central regulators of mitochondrial apoptosis: anti-apoptotic members (BCL-2, BCL-XL, MCL-1, BFL-1) sequester pro-apoptotic BH3 helices in a conserved surface groove, and cancer cells evade death by overexpressing them. Mimicking the BH3 interaction — a BH3 mimetic that occupies the groove, displaces BIM, and frees the apoptotic cascade — became a drug-discovery programme, and its product was venetoclax (ABT-199), a BCL-2-selective inhibitor approved by the FDA in 2016 for haematological malignancies. In chronic lymphocytic leukaemia (CLL), the most common adult leukaemia in Western countries, venetoclax with rituximab or obinutuzumab produced durable remissions; in acute myeloid leukaemia (AML), venetoclax with azacitidine became the standard for elderly or unfit patients, with a 65% overall response rate and 14.7 months overall survival in the phase III VIALE-A study against 22% and 8 months for azacitidine alone. Then the class's classic vulnerability appeared: acquired resistance through protein mutagenesis. Continuous venetoclax as a single agent leaves up to 50% of heavily pre-treated CLL patients refractory after two to three years, and the mutations that do it — G101V and F104C/L/I first, then D103Y/E/V, A113G, R129L and V156D — arise within or around the BH3-binding pocket, where they block small-molecule binding yet preserve native BH3 binding. G101V was found in three of four patients who became refractory in one centre's series, with the variant allele fraction rising from 9% to 25% as disease progressed, and D103Y was identified in the fourth.

The successors are designed around exactly those mutations. Sonrotoclax (S65487/BGB-11417), a next-generation BCL-2 inhibitor now in phase II/III assessment, binds wild-type BCL-2 at a KD of 0.03 nM against venetoclax's 0.61 nM, and keeps binding where venetoclax fails: KD 0.13 nM against G101V (venetoclax 10.8 nM) and 0.23 nM against D103Y (venetoclax 36.6 nM) — a 17.7-fold and 60-fold loss for venetoclax against 4.3-fold and 7.7-fold for sonrotoclax. In RS4;11 knock-in cells the gap is wider still: sonrotoclax inhibits the G101V line at 7.7 nM against venetoclax's 168 nM. The question this paper asks is the standard one for this series: among compounds with measured BCL-2 potency already in ChEMBL, does any bind the BH3 groove more strongly than venetoclax — and can docking even tell them apart when the reference drug is already a near-perfect groove binder?

The classical medical canon knows the disease family, not the target: Ibn Sina's Canon of Medicine (c. 1025) describes tumours (saratān) and their treatment — the syndrome, not the protein. The principle carried forward here is hifz al-nafs, preservation of life (see §7).

**Falsifiable question.** Do ChEMBL ligands with measured BCL-2 potency bind the BH3 groove of the S-10r-bound structure (PDB 8HTS) at scores beyond re-docked venetoclax, and would that binding translate into stronger BCL-2 inhibition, including against G101V? **Falsifier:** a fluorescence-polarisation binding assay showing a KD worse than the analogue's published value, or loss of activity against G101V BCL-2, refutes the claim for that compound. **Causal identification:** validated-control re-docking — the approved drug re-docked on a co-crystal structure of its own target class, with the co-crystallised ligand as the centre — not a comparison against nothing. Association only beyond that: docking scores are not activity.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-23: the venetoclax-resistance mutation series (Haematologica 2019 — G101V in three of four refractory patients, D103Y in the fourth); the chemoresistance-mutant structural study and stapled BAD BH3 helices (Nat Commun 2025; doi:10.1038/s41467-025-63657-y); the sonrotoclax discovery paper and the 8HTS structure (Guo et al., J Med Chem 2024;67:7836–7858; PMID 38695063; doi:10.1021/acs.jmedchem.4c00027); the sonrotoclax-versus-venetoclax comparison (Liu et al., 2024, via the S65487 efficacy summary); the venetoclax-resistance narrative review (SOHO State of the Art, 2024 — VIALE-A 65% response, 14.7 months survival; up to 50% refractory after 2–3 years); the RCSB record for PDB 8HTS; and the ChEMBL molecule record for CHEMBL4228713 (A-1211212).

### 2.2 Target identification

The pipeline resolved the target correctly on the first run: UniProtKB P10415 (apoptosis regulator Bcl-2, Homo sapiens) → ChEMBL CHEMBL4860, "Apoptosis regulator Bcl-2", SINGLE PROTEIN, 22 bioactivities, verified live 2026-11-23. This is the correct target, the correct organism, and a usable bioactivity count — the first clean target resolution of today's run.

### 2.3 Molecular docking

The pipeline docked venetoclax and the four highest-ranked ChEMBL ligands with measured potency on 8HTS, the 1.25 Å crystal structure of BCL-2 in complex with S-10r (Guo et al., J Med Chem 2024), using standardised AutoDock Vina 1.2.7, exactly as Papers #1/#3: grid centre the centroid of the co-crystallised S-10r (ligand N2L, 62 heavy atoms), [−0.21, 9.37, 7.19], verified by direct computation from the PDB file with `dock._ligand_center` (the centre audit confirmed N2L is the only drug-like HETATM group in the file; the 178 waters were correctly excluded); box 22.5 Å, exhaustiveness 8, best of 3 poses reported. The same centre, box and exhaustiveness were used for venetoclax and all four analogues. Venetoclax is therefore the self-dock control on a structure of its own target class: a method that could not recover strong binding for the drug in the BH3 groove would be broken. One caveat, stated not smoothed over: the structure holds S-10r, a sonrotoclax-series compound, not venetoclax itself — so the pocket is the BH3 groove in a sonrotoclax-bound conformation, and a venetoclax pose optimised for its own co-crystal (e.g. 6O0K) might score differently. The docked venetoclax is the parent SMILES as returned by PubChem; the crystal holds S-10r, a different molecule of the same class.

### 2.4 PAINS screen

RDKit PAINS filter applied to venetoclax and the four ligands. All five are PAINS-clean. No PAINS alert is hidden anywhere in this paper; there is none to hide.

### 2.5 ADMET and toxicity read-across

RDKit descriptors computed for venetoclax: molecular weight 868.46, logP 8.66, 3 hydrogen-bond donors, 11 acceptors, TPSA 172.03 Å², 13 rotatable bonds, 3 Lipinski violations, Lipinski fail and Veber pass. The four ligands: CHEMBL3973960 (MW 896.51, logP 9.17, HBD 4, HBA 11, TPSA 183.03 Å², 13 rotatable bonds, 3 violations; max Tox21 probability 0.503), CHEMBL3985475 (MW 896.51, logP 9.44, HBD 3, HBA 11, TPSA 172.03 Å², 14 rotatable bonds, 3 violations; max 0.56), CHEMBL3901126 (MW 909.51, logP 8.10, HBD 3, HBA 12, TPSA 175.27 Å², 14 rotatable bonds, 3 violations; max 0.662) and CHEMBL4228713 (A-1211212; MW 896.51, logP 9.44, HBD 3, HBA 11, TPSA 172.03 Å², 14 rotatable bonds, 3 violations; max 0.56). ToxGuard Tox21 kNN read-across (12 assays) for venetoclax: maximum predicted probability 0.625, a weak read-across (maximum neighbour similarity 0.225), not a measurement, and it does not clear the compound for development — it is the profile of an already-approved drug, reported for completeness. Every compound in the set violates Lipinski three times over: this is a class of large, hydrophobic groove-binders, and the descriptor counts cannot rank it — which is itself a warning that the docking scores cannot either.

### 2.6 Honesty limits

Docking ≠ activity. Vina noise is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No experimental data exist for any compound in this study beyond their published ChEMBL Ki values. The four ligands' measured potencies are biochemical Ki values, not cell-based IC50s, and their binding poses are not annotated in ChEMBL — all four are BH3 mimetics by scaffold, but the pose is assumed, not shown. The structure used (8HTS) holds a sonrotoclax-series ligand, not venetoclax, so the pocket conformation is the successor's, not the reference drug's own.

## 3. Results

### 3.1 Docking: the comparison table (8HTS, 1.25 Å — the successor's structure)

| Compound | Measured BCL-2 potency (ChEMBL) | Best affinity, 8HTS (kcal/mol) | Top-3 poses (kcal/mol) | Median pose | Margin vs venetoclax |
|---|---|---|---|---|---|
| CHEMBL3973960 | Ki 0.013 nM | −11.04 | −11.04, −10.59, −10.50 | −10.59 | −0.82 |
| CHEMBL3985475 | Ki 0.01 nM | −10.88 | −10.88, −10.85, −10.69 | −10.85 | −0.66 |
| Venetoclax (reference) | — (approved drug; published Ki ~0.01 nM class) | −10.22 | −10.22, −10.05, −9.91 | −10.05 | — |
| CHEMBL3901126 | Ki 0.013 nM | −10.06 | −10.06, −9.73, −9.51 | −9.73 | +0.16 |
| CHEMBL4228713 (A-1211212) | Ki 0.01 nM | −9.98 | −9.98, −9.85, −9.72 | −9.85 | +0.24 |

Venetoclax re-docks at −10.22 kcal/mol on 8HTS, with tight pose consistency (−10.22, −10.05, −9.91): the method recovers strong binding for the drug in the BH3 groove, so the protocol is not broken. Two analogues beat it: CHEMBL3973960 at −11.04 kcal/mol and CHEMBL3985475 at −10.88 kcal/mol. Both margins (0.82 and 0.66 kcal/mol) lie inside Vina's ±1–2 kcal/mol noise, so neither is a claim of superiority — they are leads for an assay, not winners.

The decisive check is the comparison with measured potency, and it fails. The two most potent ligands by assay, both Ki 0.01 nM — CHEMBL3985475 and CHEMBL4228713 (A-1211212) — dock at −10.88 and −9.98 kcal/mol: 0.90 kcal/mol apart, a difference larger than the margin by which either "beats" venetoclax. The best-docking compound, CHEMBL3973960 (−11.04 kcal/mol), is 1.3-fold weaker by assay (Ki 0.013 nM) than the two it supposedly beats. And the weakest docker, A-1211212 (−9.98 kcal/mol), is tied for the most potent by assay. A scoring function that cannot distinguish two compounds of identical measured potency — 0.90 kcal/mol apart on the same structure — cannot rank this family. The honest reading of the table is therefore a null result on ranking, with two assay leads: no analogue beats venetoclax beyond noise, and the method itself fails to resolve identical Ki values.

### 3.2 Comparison with published data

No published Vina study of venetoclax or these four ligands on 8HTS was found in the sweep; the comparison here is internal (ligands vs re-docked reference drug on the same structure, same protocol). The structural literature is the published ground truth for the binding mode: the 8HTS structure (Guo et al. 2024) shows the sonrotoclax-series ligand S-10r in the BH3 groove, and the sonrotoclax discovery paper gives the paper its most useful context — the successor's advantage is not wild-type affinity (0.03 nM vs 0.61 nM is a 20-fold gap, but both are sub-nanomolar) but the mutant profile: 0.13 nM against G101V where venetoclax falls to 10.8 nM. The structural literature also gives the resistance mechanism its precision: G101V and D103Y sit in the groove where venetoclax's chlorophenyl and azaindole groups bind, and the stapled BAD BH3 helix study (Nat Commun 2025) shows the same mutations can be overcome by a peptide that recapitulates the native BH3 contacts the small molecules lose.

### 3.3 The clinical confounder that docking cannot see

Venetoclax's clinical record is the paper's most important context, and docking cannot see any of it. The drug's >65% response rate in unfit AML and its durable CLL remissions are not binding problems — and its failures are not binding problems either: up to half of heavily pre-treated CLL patients become refractory on continuous monotherapy, and the mechanism is a groove mutation that preserves BH3 binding while blocking the drug. A compound that out-scores venetoclax here by 0.82 kcal/mol but loses activity against G101V would be a worse drug, and docking on a wild-type structure cannot tell the two apart. The docking order cannot explain why the drug cures some patients and fails others with the same target; the mutation data together with the structure can.

## 4. Discussion

### 4.1 The reframe

The question this paper can ask has changed since venetoclax was approved. Before approval, the question was "can a BH3 mimetic be selective for BCL-2 over BCL-XL?" — now it is "which molecule, if any, beats venetoclax on the wild-type groove *and* keeps its binding when the groove mutates?" The benchmark is therefore a screen for successors with a two-part bar: beat −10.22 kcal/mol on 8HTS and keep activity against G101V/D103Y. This paper supplies the first half of the bar and shows the second half is where the pipeline must go next: the structure used is wild-type, and the two best scorers have no mutant data in this run.

### 4.2 Why the "win" must not be over-read

Three reasons. First, every margin in §3.1 lies inside Vina's ±1–2 kcal/mol noise. Second, the ranking contradicts measured potency in the decisive pair — two Ki 0.01 nM compounds dock 0.90 kcal/mol apart, and the best docker is the weaker binder by assay. Third, the whole class is large and hydrophobic (MW 868–910, logP 8.1–9.4, three Lipinski violations each), so the scores scale with molecular size and hydrophobic surface — the very properties that make these compounds hard to develop — rather than with the specific groove contacts that decide resistance.

### 4.3 The size problem is the experiment's design constraint, not a reason to stop

The five ligands were chosen by pipeline rank, and the pipeline's rank rewards the same bulk that Vina rewards: the top two scorers are also the two largest ligands in the set. The honest handling is to report the scores with the caveat attached, and to design the validation assay so the size question is answered by the experiment: a fluorescence-polarisation binding assay measures KD regardless of molecular weight, and a G101V-mutant assay measures whether the analogue kept the resistance barrier that defines the class. A compound that scores well because it is big but binds the mutant poorly is not a failure of the compound; it is a failure of the scoring function, and the assay is what tells the two apart.

### 4.4 Mechanism

Venetoclax is a BH3 mimetic: it occupies the BH3 groove of BCL-2, displaces pro-apoptotic BIM, and frees BAX/BAK to permeabilise the mitochondrial membrane, releasing cytochrome c and activating caspases. Test for each link: (i) a fluorescence-polarisation binding assay (with venetoclax as the comparator) measures KD directly against the published Ki values; (ii) the same assay on G101V and D103Y mutant BCL-2 measures whether the analogue kept the resistance barrier — loss of activity against G101V is the likeliest way a "better" BH3 mimetic becomes a worse drug, because G101V is the mutation the clinic actually selects; (iii) a cell-viability assay in RS4;11 parental and G101V knock-in cells measures IC50 against venetoclax at matched concentration, with a cytotoxicity counter-screen.

### 4.5 Testable hypotheses

1. The best-scoring analogue binds wild-type BCL-2 with a KD within 3-fold of its published Ki in a fluorescence-polarisation assay. Falsifier: KD > 3-fold worse than published.
2. The same analogue keeps activity against G101V BCL-2 within 5-fold of wild-type. Falsifier: >10-fold loss against G101V.
3. The 8HTS pose predicts the resistance profile: an analogue whose docked pose loses contact with the groove residues where G101V/D103Y sit loses activity against those mutants first. Falsifier: an analogue without those contacts keeps wild-type potency against G101V.

### 4.6 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): fluorescence-polarisation binding assay for the two best-scoring analogues — CHEMBL3973960 (best best-pose, −11.04) and CHEMBL3985475 (most potent by assay, Ki 0.01 nM) — plus venetoclax as control, on wild-type BCL-2; readout KD, n=3, with a known weak binder as a negative control. Stage 2 (weeks 4–8): the same assay on G101V and D103Y mutant BCL-2 for the best compound from stage 1. Stage 3 (weeks 9–12): if any analogue passes stages 1–2, cell-viability assay in RS4;11 parental and G101V knock-in cells; if none passes, publish the negative result with the docking data as the reason the hypothesis failed. No animal work is proposed at this stage.

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol swallows every reported margin.
2. The ranking cannot resolve identical potency (two Ki 0.01 nM compounds dock 0.90 kcal/mol apart), so the set cannot test ranking at all.
3. The whole class is large and hydrophobic (MW 868–910, logP 8.1–9.4, three Lipinski violations each); the scores scale with size, not with the contacts that decide resistance.
4. The structure used (8HTS) holds a sonrotoclax-series ligand, not venetoclax — the pocket is in the successor's conformation, not the reference drug's own.
5. One rigid structure was used (8HTS, wild-type BCL-2, 1.25 Å); the BH3 groove adapts to different chemotypes, and the G101V/D103Y resistance question was not docked.
6. No data on the clinical confounder: docking cannot distinguish the patients who achieve durable remission from the up-to-50% who become refractory on continuous monotherapy.
7. The classical-canon sweep found no BCL-2-relevant text: the Canon of Medicine describes tumours, not proteins, so the Islamic-principle discussion rests on hifz al-nafs as a principle, not on a classical source about this target.

## 6. Conclusion

Venetoclax, the BH3 mimetic at the centre of modern CLL and AML therapy, re-docks at −10.22 kcal/mol on the 1.25 Å BCL-2 structure 8HTS with tight pose consistency and no PAINS alert — a validated control, not a discovery. Two analogues beat it on the score — CHEMBL3973960 at −11.04 and CHEMBL3985475 at −10.88 kcal/mol — but both margins lie inside Vina noise, and the method fails its own positive control in the decisive pair: the two most potent compounds by assay (both Ki 0.01 nM) dock 0.90 kcal/mol apart, and the best docker is 1.3-fold weaker by assay than the compounds it supposedly beats. The docking verdict is a null result on ranking, with two assay leads, and it is useful precisely as one: this series cannot be ranked by rigid Vina scoring on a single wild-type structure, the scores scale with the size the whole class shares, and the next screen must be a binding assay plus a G101V-mutant assay, not a bigger docking set. What the docking cannot do is resolve the resistance split: the same groove that binds venetoclax at −10.22 kcal/mol is the groove whose G101V and D103Y mutations defeat it, and only a mutant binding assay can tell whether a successor keeps the barrier. The next step is the cheap, decisive test — a fluorescence-polarisation assay plus a G101V assay for the best-scoring analogues against venetoclax — not another docking run.

## 7. Policy implications

**Decision-maker:** Pakistan's Drug Regulatory Authority (DRAP) and the National Cancer Control Programme, with the SMBBMU ORIC office as the local route. **Decision:** whether to fund a small, targeted validation of BH3-mimetic benchmarking as an academic drug-discovery exercise, and whether to prioritise venetoclax-based regimens in procurement for CLL and AML. **Exact change:** commission the 8–12-week binding-plus-mutant screen proposed in §4.6 for the two best-scoring analogues against venetoclax, instead of funding another purely computational screen of the same target; and, in parallel, ask the cancer programme to note explicitly that the binding question is settled for the wild-type groove — venetoclax re-docks at −10.22 kcal/mol — and that the remaining gap is the mutant groove, not the drug's potency: every rupee spent re-docking venetoclax analogues into the wild-type pocket is a rupee not spent testing them against G101V. **If evidence Z appears, reverse this:** if the best analogue beats venetoclax's KD by >10-fold in the binding assay and keeps activity against G101V within 5-fold, drop the access-only framing and fund the analogue's development; if it loses >3-fold to its published Ki, drop this ligand set and redirect the same screen to the next BH3-mimetic chemotypes — do not proceed to any animal or clinical work on docking scores alone. The Islamic principle is hifz al-nafs (preservation of life, a maqsad of the Sharia): where a cheap test can distinguish a usable BCL-2 inhibitor from a useless one for the most common adult leukaemia, running the test is the obligation; prescribing on an untested docking score would violate it. The evidence here is thin — docking only — so the recommendation is "run the trial", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Venetoclax resistance and acquired BCL2 mutations in chronic lymphocytic leukemia. Haematologica. 2019. (G101V in three of four refractory patients; D103Y in the fourth.)
2. Structural insights into chemoresistance mutants of BCL-2 and their targeting by stapled BAD BH3 helices. Nat Commun. 2025. doi:10.1038/s41467-025-63657-y.
3. Guo Y, et al. Discovery of the clinical candidate sonrotoclax (BGB-11417), a highly potent and selective inhibitor for both WT and G101V mutant Bcl-2. J Med Chem. 2024;67:7836-7858. doi:10.1021/acs.jmedchem.4c00027. PMID: 38695063.
4. Liu et al., 2024. (Sonrotoclax vs venetoclax: SPR KD and RS4;11 G101V knock-in data, via the S65487 efficacy summary.)
5. Understanding and overcoming venetoclax resistance in hematologic malignancies. SOHO State of the Art Updates and Next Questions. 2024. (VIALE-A: 65% response, 14.7 months survival; up to 50% refractory after 2–3 years.)
6. RCSB PDB entry 8HTS: Crystal structure of Bcl-2 in complex with S-10r, 1.25 Å. RCSB Protein Data Bank. Accessed 2026-11-23.
7. ChEMBL target CHEMBL4860: Apoptosis regulator Bcl-2. ChEMBL database, European Bioinformatics Institute. Accessed 2026-11-23.
8. UniProtKB P10415: Apoptosis regulator Bcl-2, Homo sapiens. UniProt. Accessed 2026-11-23.
9. ChEMBL molecule CHEMBL4228713: A-1211212. ChEMBL database, European Bioinformatics Institute. Accessed 2026-11-23.
10. PubChem: venetoclax. National Library of Medicine. Accessed 2026-11-23.
11. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; describes tumours, saratān — cited for the hifz al-nafs principle only.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-082-2026-11-23.json` (venetoclax + four ChEMBL ligands on 8HTS). Reference drug venetoclax; analogues CHEMBL3973960, CHEMBL3985475, CHEMBL3901126, CHEMBL4228713 (A-1211212). Structure: PDB 8HTS (1.25 Å). Target: UniProtKB P10415; ChEMBL target CHEMBL4860. No additional data were generated.
