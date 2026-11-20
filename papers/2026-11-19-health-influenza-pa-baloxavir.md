# Baloxavir Acid Re-Docks at −6.62 kcal/mol on the Influenza PA Endonuclease Fragment Structure — but the ChEMBL Ligand Set Is Undockable and the Older Inhibitor L-742,001 Scores Better

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-19 · **Health Papers Agent — Paper #81** (daily 5-paper run)

**Keywords:** influenza; PA endonuclease; baloxavir; cap-snatching; antiviral resistance; molecular docking; ChEMBL; I38T

---

## Abstract

Influenza causes about a billion infections a year, and baloxavir marboxil — the only approved cap-dependent endonuclease inhibitor — is losing ground to treatment-emergent PA I38T substitutions, which appear in roughly 10% of treated adults and up to about 23% of treated children. We asked whether ChEMBL-recorded inhibitors of the influenza A polymerase acidic (PA) endonuclease bind the true active site more strongly than baloxavir acid itself. Using the LeadForge pipeline (UniProtKB P15659 → ChEMBL target CHEMBL3885620, 7 bioactivities → PubChem/RDKit similarity, PAINS and ADMET screen → AutoDock Vina 1.2.7), we found the ChEMBL ligand set unusable: all seven recorded ligands are giant molecules (MW 1,686–2,722 Da, 52–80 rotatable bonds) that failed conformer generation, so none could be docked. Instead we re-docked baloxavir acid on the 2.2 Å PA endonuclease fragment structure 5IEQ, centred on the co-crystallised fragment (verified centroid), and compared it with two literature compounds docked on the same centre: the diketo-acid inhibitor L-742,001 scored −7.17 kcal/mol and the co-crystallised fragment EBSI-747 scored −5.55 kcal/mol, against −6.62 kcal/mol for baloxavir acid, all with tight pose consistency and no PAINS alerts. The honest limit: the 0.55 kcal/mol gap between L-742,001 and baloxavir acid lies inside Vina's ±1–2 kcal/mol noise, baloxavir acid is roughly 100-fold more potent than L-742,001 by measured enzyme IC50 (low-nanomolar versus 0.5 µM), and the 5IEQ structure contains no catalytic metal ions — yet both inhibitors bind by chelating the two active-site metals, so the scoring omits the interaction that matters most. The claim that L-742,001 is the better PA inhibitor would be refuted if a metal-containing endonuclease assay shows baloxavir acid retaining its ~100-fold potency advantage. The falsifiable next step is a 8–12-week metal-containing enzyme-plus-cellular test of baloxavir acid against L-742,001 and its analogues on wild-type and I38T PA.

---

## 1. Introduction

Seasonal influenza causes an estimated one billion infections annually, including 3–5 million severe cases and 290,000–650,000 deaths, and pandemic risk never leaves the agenda: H5N1 continues to circulate in birds and mammals. The virus transcribes its mRNA by "cap-snatching" — the PB2 subunit binds host capped pre-mRNAs and the polymerase acidic (PA) subunit's cap-dependent endonuclease cleaves them 10–13 nucleotides downstream, generating the primers for viral mRNA synthesis. Block the endonuclease and viral transcription stops. Baloxavir marboxil, approved in Japan and the United States in 2018, is a prodrug rapidly hydrolysed to baloxavir acid, a first-in-class inhibitor of this enzyme; it works against strains resistant to neuraminidase inhibitors, and the two drug classes show no cross-resistance. But the genetic barrier is low: a single amino-acid substitution, I38T in PA, raises the inhibitor constant ~18-fold and the IC50/EC50 by 44- to 211-fold, and treatment-emergent I38X substitutions appear in roughly 10% of treated adults and up to about 23% of treated children, with transient viral rebound. A second endonuclease inhibitor that tolerates I38T would be clinically valuable — and the obvious place to look is the older diketo-acid inhibitor L-742,001, which inhibits the same enzyme (IC50 0.5 µM) and whose resistance profile is different: up to 20-fold resistance for H41A, I120T and G81F/V/T mutants, with some mutants (R124Q, Y130A) three-fold more sensitive.

The classical medical canon has no concept of a viral endonuclease, and this paper does not pretend otherwise: Ibn Sina's Canon of Medicine (c. 1025) discusses epidemic respiratory illness (waba) as a clinical syndrome, and Al-Razi's Kitab al-Hawi records epidemic fevers. These texts are hypothesis sources, not evidence — they knew the syndrome, not the target — but they establish that the disease burden this paper addresses is centuries old in the region, and the Islamic principle behind acting on it is hifz al-nafs, preservation of life (see §7).

**Falsifiable question.** Do ChEMBL-recorded PA endonuclease inhibitors bind the true active site (PDB 5IEQ) more strongly than baloxavir acid, and does the older inhibitor L-742,001 offer a better starting point for I38T-tolerant design? **Falsifier:** a metal-containing endonuclease assay showing baloxavir acid retaining a ≥10-fold potency advantage over L-742,001, or a >10-fold IC50 loss for any proposed analogue against I38T PA, refutes the claim for that compound. **Causal identification:** validated-control re-docking — the reference drug re-docked on a co-crystal structure of its own target class — not a comparison against nothing. Association only beyond that: docking scores are not activity.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-19: baloxavir mechanism and I38T resistance, the L-742,001 mutational analysis (Stevaert et al., J Virol 2013), the WHO influenza burden figures, and the RCSB record for PDB 5IEQ. The Islamic-canon sweep covered the available digitised canon relevant to the question: Ibn Sina, Al-Qanun fi al-Tibb (c. 1025); Al-Razi, Kitab al-Hawi (c. 900) — consulted in the literature-map summaries, not in full Arabic text (see Limitations).

### 2.2 Molecular docking

Standardised AutoDock Vina 1.2.7 protocol, exactly as Papers #1/#3. Target: influenza A virus polymerase acidic protein, UniProtKB P15659 (strain A/Wilson-Smith/1933 H1N1, gene PA); ChEMBL target CHEMBL3885620 (7 bioactivities retrieved live 2026-11-19). Structure: PDB 5IEQ, the PA endonuclease domain (Wilson-Smith/1933 H1N1) bound to fragment hit EBSI-747 (1-(4-chlorophenyl)-1H-imidazole), 2.2 Å. Grid centre: centroid of the co-crystallised fragment 1CI in chain A, [−29.61, −45.19, 62.49], verified by direct computation from the PDB file; box 22.5 Å, exhaustiveness 8, best of 3 poses reported. The same centre, box and exhaustiveness were used for baloxavir acid, L-742,001 and the fragment.

**A data-quality failure, stated plainly.** The pipeline's ChEMBL ligand set for this target is unusable for docking: all seven recorded ligands have molecular weights of 1,686–2,722 Da with 52–80 rotatable bonds, and all four docked leads failed conformer generation (`conformer_failed`) — RDKit cannot build 3D conformers for molecules of this size. These are not small-molecule endonuclease inhibitors; they are giant peptide-like records in the ChEMBL target file, and reporting a docking score for them would be fabrication. The paper therefore reports the failure, and compares baloxavir acid instead with two literature compounds docked on the same centre: L-742,001 (SMILES fetched live from PubChem by CAS 174605-64-2, desalted to the free base) and EBSI-747 (the co-crystallised fragment, SMILES fetched live from PubChem). All docking scores in §3 are from `hidden_files/dock-HP-087-2026-11-19.json` (pipeline run) and `hidden_files/dock-HP-087b-2026-11-19.json` (salvage run, `hidden_files/redock_hp087.py`).

### 2.3 PAINS screen

RDKit PAINS filter applied to the pipeline leads and to the two salvage compounds. None carries a PAINS alert: baloxavir acid, L-742,001 and EBSI-747 are all PAINS-clean.

### 2.4 ADMET and toxicity read-across

RDKit descriptors (Lipinski/Veber) computed for every lead; ToxGuard Tox21 kNN read-across (12 assays) run for baloxavir acid. Baloxavir acid (PubChem CID 124081876, C24H19F2N3O4S, MW 483.50) passes Lipinski with 0 violations (logP 2.98, TPSA 75.01) and scores at most 0.33 on any Tox21 assay (SR-ARE).

### 2.5 Honesty limits

Docking ≠ activity. Vina noise is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No experimental data were generated in this study. The 5IEQ structure contains no catalytic metal ions (verified: no Mn/Mg/Zn HETATM records in the file), so the metal-chelation interaction that both inhibitors rely on is absent from scoring — the single largest physical omission in this paper.

## 3. Results

### 3.1 The ChEMBL ligand set is undockable

| Compound | ChEMBL IC50 vs PA* | MW / rotatable bonds | Docking result |
|---|---|---|---|
| CHEMBL3981816 | 6.3 nM (pChEMBL 8.20) | 1,796 / 54 | conformer_failed |
| CHEMBL3954115 | 21.64 nM (pChEMBL 7.67) | 1,748 / 53 | conformer_failed |
| CHEMBL3955138 | 13.9 nM (pChEMBL 7.86) | 1,751 / 52 | conformer_failed |
| CHEMBL3915821 | 1.8 nM (pChEMBL 8.74) | 2,722 / 80 | conformer_failed |
| CHEMBL3964090 | 16.6 nM (pChEMBL 7.78) | 1,763 / 58 | not docked |
| CHEMBL3110332 | 43.32 nM (pChEMBL 7.36) | 1,686 / 52 | not docked |
| CHEMBL3973799 | 21.7 nM (pChEMBL 7.66) | 1,774 / 55 | not docked |

\* ChEMBL-recorded IC50 against PA (target CHEMBL3885620), retrieved live 2026-11-19. All seven are peptide-scale molecules; their nanomolar "IC50" values cannot be validated as small-molecule endonuclease inhibition from the records available, and no docking score is reported for any of them. This is a data-quality finding, not a result about the compounds: the ChEMBL PA target record contains no dockable small-molecule inhibitor set.

### 3.2 Docking: the comparison table

| Compound | Published enzyme potency | Best affinity, 5IEQ (kcal/mol) | Top-3 poses (kcal/mol) | PAINS | MW / logP / TPSA |
|---|---|---|---|---|---|
| L-742,001 | IC50 0.5 µM† | **−7.17** | −7.17, −6.88, −6.73 | none | 413.90 / — / — |
| Baloxavir acid (reference, re-docked) | low-nanomolar‡ | −6.62 | −6.62, −6.58, −6.53 | none | 483.50 / 2.98 / 75.01 |
| EBSI-747 (co-crystallised fragment) | fragment hit§ | −5.55 | −5.55, −5.54, −5.54 | none | 178.62 / — / — |

† L-742,001 PA endonuclease IC50 0.5 µM (Stevaert et al., Mol Pharmacol 2015). ‡ Baloxavir acid inhibits the PA endonuclease at low-nanomolar concentrations (published in-vitro summaries). § EBSI-747 is the fragment hit co-crystallised in 5IEQ; no enzyme IC50 was reported for it in the structure record.

L-742,001 out-scores baloxavir acid by 0.55 kcal/mol with tight pose consistency (top-3 spread 0.44 kcal/mol). The fragment re-docks at −5.55 kcal/mol with near-identical poses — the expected behaviour for a small fragment in a large pocket, and a useful sanity check that the grid is on the real site.

### 3.3 The docking–activity discordance that must not be hidden

The measured potencies do not track the docking order. Baloxavir acid is roughly 100-fold more potent than L-742,001 by enzyme IC50 (low-nanomolar versus 0.5 µM), yet it docks 0.55 kcal/mol worse. The reason is visible in the structure: both inhibitors bind by chelating the two catalytic metal ions of the endonuclease active site, and 5IEQ contains no metal ions at all — Vina is scoring only the non-metal contacts (hydrophobic packing, hydrogen bonds), which favour the larger, more hydrophobic L-742,001. Rigid Vina scoring on a metal-free structure cannot rank metal-chelating inhibitors. This is the paper's most important negative result: **the docking ranking is not a potency ranking**, and any claim built on the −7.17 vs −6.62 gap alone would be over-reading noise on top of a missing physical interaction.

### 3.4 Comparison with published docking

No published Vina study of baloxavir acid or L-742,001 on 5IEQ was found in the sweep; the comparison here is internal (compounds vs re-docked reference on the same structure, same protocol). The re-docked baloxavir acid score of −6.62 kcal/mol and the fragment's −5.55 kcal/mol are the validated controls that anchor the comparison. Stevaert et al. (2013) previously docked L-742,001 into an inhibitor-free PA N-terminal structure and found a binding orientation distinct from the later crystal structure — a reminder that this pocket's docking poses are method-sensitive.

## 4. Discussion

### 4.1 The reframe

The question this paper can actually answer is narrower than the one it started with. It cannot say "L-742,001 beats baloxavir" — the margin is inside noise, the potency order is reversed, and the scoring omits the metal chelation that defines both inhibitors. What it can say is: (a) baloxavir acid re-docks cleanly on the fragment structure with tight poses, so the protocol is sound; (b) the ChEMBL PA record has no usable small-molecule ligand set, a data-quality gap that any future screen must work around by curating inhibitors from the literature instead; (c) the decisive experiment is now sharply defined — a metal-containing endonuclease assay comparing baloxavir acid, L-742,001 and analogues on wild-type and I38T PA — and it is cheap and feasible in a university lab.

### 4.2 Why the "win" must not be over-read

Three reasons. First, the 0.55 kcal/mol margin is inside Vina's ±1–2 kcal/mol noise. Second, the docking order contradicts the measured potency order by ~100-fold. Third, the two catalytic metal ions are absent from the structure, and resistance mutations act precisely around that metal centre — I38T sits adjacent to the active site and perturbs inhibitor binding without destroying catalysis. A compound that scores well here may still fail against I38T, and the only way to know is the enzyme assay.

### 4.3 Mechanism

The PA endonuclease cleaves host capped pre-mRNAs using two divalent metal ions coordinated by the catalytic residues (including His41 and Glu80); inhibitors chelate those metals while their hydrophobic groups occupy the surrounding pockets. I38T changes the shape of the pocket without touching the metals, which is why it costs baloxavir ~18-fold in binding while leaving the enzyme functional. Test for each link: (i) a metal-containing endonuclease cleavage assay measures whether the compound still inhibits wild-type and I38T enzyme; (ii) a cellular vRNP reporter assay measures whether inhibition survives in cells; (iii) a metal-containing co-crystal structure, if one becomes available, would let docking test the mechanism directly.

### 4.4 Testable hypotheses

1. In a metal-containing PA endonuclease assay, baloxavir acid retains a ≥10-fold IC50 advantage over L-742,001 on wild-type PA. Falsifier: L-742,001 within 3-fold of baloxavir acid.
2. At least one L-742,001 analogue (from the Stevaert et al. series) shows ≤3-fold IC50 loss against I38T PA where baloxavir acid loses ≥18-fold. Falsifier: all analogues lose ≥10-fold against I38T.
3. Re-docking on a metal-containing PA structure reverses the L-742,001 advantage over baloxavir acid. Falsifier: the advantage persists with metals present.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): recombinant wild-type and I38T PA endonuclease cleavage assay (fluorescence-based, with Mg²⁺/Mn²⁺ present) for baloxavir acid, L-742,001 and two analogues; readout IC50, n=3. Stage 2 (weeks 4–8): cellular mini-genome (vRNP) reporter assay in HEK293T cells for the same compounds, wild-type versus I38T. Stage 3 (weeks 9–12): if any analogue passes stages 1–2, cytotoxicity (HepG2) and a first resistance-passage experiment; if none passes, publish the negative result with the docking data as the reason the hypothesis failed.

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol swallows the reported margin.
2. The 5IEQ structure contains no catalytic metal ions, removing the chelation interaction that defines both inhibitors; scores may not reflect true binding energetics.
3. The ChEMBL PA ligand set is undockable (all seven ligands >1,686 Da); no ChEMBL-derived lead is proposed.
4. Docking order contradicts measured IC50 order (~100-fold discordance); rigid docking cannot rank these compounds.
5. A single structure (5IEQ, a fragment-bound H1N1 PA) was used; the pocket differs across subtypes and the I38T question is untested in this work.
6. Published baloxavir enzyme IC50 values are taken from in-vitro summaries; the primary assay data were not re-verified compound by compound.
7. The Islamic-canon sweep used the literature-map summaries of Ibn Sina's Canon and Al-Razi's Kitab al-Hawi; the full Arabic texts were not read, and the canon has no concept of a viral enzyme — the sweep is historical context only.

## 6. Conclusion

Baloxavir acid re-docks at −6.62 kcal/mol on the influenza PA endonuclease fragment structure 5IEQ, against −7.17 kcal/mol for the older diketo-acid inhibitor L-742,001 and −5.55 kcal/mol for the co-crystallised fragment, with tight pose consistency and no PAINS alerts. The ChEMBL PA ligand set proved undockable — seven giant molecules, none of which could generate a conformer — and the 0.55 kcal/mol L-742,001 advantage is inside Vina noise, reverses the ~100-fold measured potency order, and was scored on a metal-free structure that omits the chelation both inhibitors rely on. This is not evidence that L-742,001 beats baloxavir — it is evidence that the two are worth the cheap, decisive test: a metal-containing enzyme assay on wild-type versus I38T PA. That test, not another docking run, is the next step.

## 7. Policy implications

**Decision-maker:** Pakistan's National Institute of Health (NIH Islamabad) influenza surveillance programme and the provincial health departments, with DRAP as regulator. **Decision:** whether to fund a small, targeted validation of alternative PA endonuclease inhibitors against locally circulating influenza strains. **Exact change:** commission the 8–12-week metal-containing enzyme-plus-cellular screen proposed in §4.5 for baloxavir acid versus L-742,001 analogues on wild-type and I38T PA, instead of relying on imported susceptibility assumptions for baloxavir. **If evidence Z appears, reverse this:** if all analogues lose ≥10-fold activity against I38T PA, drop this chemotype set and redirect the same screen to the next PA inhibitor series — do not proceed to any animal or clinical work on docking scores alone. The Islamic principle is hifz al-nafs (preservation of life, a maqsad of the Sharia): where a cheap test can distinguish a usable antiviral from a useless one for a virus that kills hundreds of thousands a year, running the test is the obligation; prescribing on an untested docking score would violate it. The evidence here is thin — docking only — so the recommendation is "run the trial", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Hayden FG, Sugaya N, Hirotsu N, et al. Baloxavir marboxil for uncomplicated influenza in adults and adolescents. N Engl J Med. 2018;379(10):913-923. doi:10.1056/NEJMoa1716197.
2. Stevaert A, Nurra S, Pala N, et al. An integrated biological approach to guide the development of metal-chelating inhibitors of influenza virus PA endonuclease. Mol Pharmacol. 2015;87(2):323-337.
3. Stevaert A, et al. Mutational analysis of the binding pockets of the diketo acid inhibitor L-742,001 in the influenza virus PA endonuclease. J Virol. 2013;87(19):10524-10538. doi:10.1128/JVI.00832-13. PMID: 23824822.
4. DuBois RM, et al. Structural and biochemical basis for development of influenza virus inhibitors targeting the PA endonuclease. PLoS Pathog. 2012;8(8):e1002830. doi:10.1371/journal.ppat.1002830.
5. RCSB PDB entry 5IEQ: Crystal structure of polymerase acid protein (PA) from Influenza A virus, Wilson-Smith/1933 (H1N1) bound to fragment hit EBSI-747. RCSB Protein Data Bank. Accessed 2026-11-19.
6. ChEMBL target CHEMBL3885620: Polymerase acidic protein, Influenza A virus. ChEMBL database, European Bioinformatics Institute. Accessed 2026-11-19.
7. World Health Organization. Influenza (seasonal) — fact sheet. Geneva: WHO. (Burden: ~1 billion cases, 3–5 million severe cases, 290,000–650,000 deaths annually.)
8. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; epidemic respiratory illness, waba.)
9. Al-Razi. Kitab al-Hawi fi al-Tibb (Comprehensive Book of Medicine). c. 900. (Classical source; epidemic fevers.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-087-2026-11-19.json` (pipeline run; baloxavir acid re-dock and the failed ChEMBL leads) and `hidden_files/dock-HP-087b-2026-11-19.json` (salvage run, `hidden_files/redock_hp087.py`: L-742,001 and EBSI-747). Ligand identities are ChEMBL IDs CHEMBL3981816, CHEMBL3954115, CHEMBL3955138, CHEMBL3915821, CHEMBL3964090, CHEMBL3110332, CHEMBL3973799; reference drug baloxavir acid, PubChem CID 124081876; L-742,001, PubChem CID 71779114 (CAS 174605-64-2); EBSI-747, 1-(4-chlorophenyl)-1H-imidazole. Structure: PDB 5IEQ (2.2 Å). Target: UniProtKB P15659; ChEMBL target CHEMBL3885620. No additional data were generated.
