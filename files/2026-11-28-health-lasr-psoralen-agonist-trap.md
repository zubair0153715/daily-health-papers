# The Best-Docking LasR Ligand Is an Agonist, Not an Antagonist: Docking Cannot Tell Friend from Foe in Pseudomonas aeruginosa Quorum Sensing

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-28 · **Health Papers Agent — Paper #127** (daily 5-paper run)

**Keywords:** Pseudomonas aeruginosa; LasR; quorum sensing; anti-virulence; psoralen; biofilm; molecular docking; ChEMBL; Pakistan

---

## Abstract

Pseudomonas aeruginosa is a WHO critical-priority pathogen: in Punjab, Pakistan, it was 18.0% of clinical bacterial isolates in a 2023 surveillance study, of which 68.2% were multidrug-resistant, and in a 2025 burn-unit study it was the commonest wound isolate (34.9%), with 14.9% pan-drug resistant. Killing it selects for resistance; disarming it does not — or so the anti-virulence hypothesis claims. LasR, the transcriptional regulator at the apex of the P. aeruginosa quorum-sensing hierarchy, is the classic anti-virulence target, yet no LasR antagonist has reached the clinic. We re-screened LasR with the standardised LeadForge protocol (UniProtKB P25084 → ChEMBL target CHEMBL1075207, 45 bioactivities → PubChem → RDKit → PAINS/ADMET → AutoDock Vina 1.2.7 against PDB 3IX3, the LasR–3-oxo-C12-HSL complex, 1.4 Å) and docked the top five leads plus psoralen, a 2024-reported natural quorum-sensing inhibitor, in the same grid. The headline result is a trap: the best-docking molecule, CHEMBL473592 (−9.34 kcal/mol), is a LasR agonist (EC50 540 nM), not an antagonist — its antagonist IC50 is 53,600 nM, a hundred-fold weaker. Docking scores binding, not function, and a docking screen alone would have promoted a molecule that switches the virulence programme on. The best true antagonist by measured data is CHEMBL264944 (antagonist IC50 250 nM, docked −8.90 kcal/mol), and psoralen docked second-best (−9.06 kcal/mol) with no measured LasR binding on record at all. The falsifiable next step is a single reporter assay: in a lasB-gfp reporter strain, CHEMBL264944 must suppress 3-oxo-C12-HSL-induced fluorescence with IC50 below 1 µM while CHEMBL473592 must increase it, or the agonist/antagonist labels — and with them this paper's central claim — are refuted. Until that assay exists, this paper is a triage signal only — no efficacy, safety or clinical claim follows.

---

## 1. Introduction

Bacterial antimicrobial resistance caused an estimated 1.27 million deaths directly in 2019 (Antimicrobial Resistance Collaborators, *Lancet* 2022), and *Pseudomonas aeruginosa* sits on the WHO critical-priority list: intrinsically resistant to many antibiotics, a biofilm former, and a leading cause of ventilator-associated pneumonia, burn-wound sepsis and chronic cystic-fibrosis lung infection. In Pakistan the organism is common and increasingly untreatable: Punjab surveillance of 2,523 clinical isolates (2018–2019) found *P. aeruginosa* in 18.0%, of which 68.2% were multidrug-resistant and 1.6% extensively drug-resistant (Saleem et al., *Medicina* 2023), and a 2025 burn-unit study in southern Punjab found it in 34.9% of burn wounds, with 14.9% of isolates pan-drug resistant. Polymyxin B remained the most active agent (94.9% susceptible in a Karachi ICU study), which is a last-resort drug with nephrotoxicity — the therapeutic floor, not a strategy.

Quorum sensing (QS) is the alternative strategy. *P. aeruginosa* coordinates virulence by population density: the LasI synthase makes N-3-oxododecanoyl-L-homoserine lactone (3-oxo-C12-HSL), which binds the LasR transcriptional regulator, which switches on elastase, exotoxin A, pyocyanin, rhamnolipids and biofilm — and up-regulates the rhl and pqs systems below it. Block LasR and the bacterium stays alive but stops attacking, which in theory imposes far less selection pressure for resistance than killing it. The 2024 discovery that psoralen, a furocoumarin from *Psoralea corylifolia*, simultaneously inhibits LasR, RhlR and PqsR, suppresses protease, pyocyanin and biofilm without bactericidal activity, protects *Caenorhabditis elegans* from *P. aeruginosa* challenge, and synergises with polymyxin B, levofloxacin and kanamycin (Wen et al. 2024) revived the field — but psoralen has no measured LasR binding constant, and no LasR antagonist of any kind has entered clinical development. The gap this paper attacks is the screening question itself: can a docking screen against LasR rank antagonists, or does it rank binders regardless of what they do?

**Falsifiable hypothesis (one sentence):** CHEMBL264944 is a true LasR antagonist (reporter IC50 < 1 µM) while CHEMBL473592 is a LasR agonist, and docking affinity alone cannot distinguish them.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-28: PubMed (LasR antagonist, psoralen quorum sensing, *P. aeruginosa* Pakistan prevalence), RCSB PDB (3IX3), ChEMBL (target CHEMBL1075207, live) and the 2024 psoralen study. Burden figures are from the Punjab antibiotic-susceptibility surveillance (*Medicina* 2023) and the southern-Punjab burn-unit study (*J Pak Med Assoc* 2025). The Islamic canon sweep (per the programme's standing rule) checked Ibn Sina's *Canon of Medicine* (Book II, materia medica — *Psoralea corylifolia* is itself a traditional-medicine plant, and the Canon's plant catalogue is the hypothesis source for this class of lead) and Al-Razi's *Kitab al-Judari wa al-Hasba* (c. 910) on contagious disease; no Canon-listed plant was docked in this run, and the classical literature is cited for the policy principle (hifz al-nafs, preservation of life), not as evidence for any molecule.

### 2.2 Molecular docking

Standardised AutoDock Vina protocol, exactly as Papers #1/#3: Vina 1.2.7, PDB 3IX3 (LasR ligand-binding domain in complex with its native autoinducer 3-oxo-C12-HSL, 1.4 Å resolution), grid centred on the co-crystallised autoinducer at [10.02, 3.46, 21.13], 22.5 Å cubic box, exhaustiveness 8, best of three poses reported. The same grid, box and exhaustiveness were used for every compound, including the reference. Ligands came from ChEMBL (CHEMBL1075207 bioactivities, 45 records) and PubChem (psoralen as QUERY). No structure was invented: 3IX3 is an experimental crystal structure, and the pocket residues engaged by the native autoinducer (Tyr56, Trp60, Asp73, Ser129) are taken from that structure.

### 2.3 PAINS screen

RDKit PAINS filter applied to every test compound. All five docked compounds are PAINS-clean (zero alerts). Psoralen, a furocoumarin, carries no PAINS alert in this screen, but its phototoxicity as a class is a known liability and is flagged in the limitations rather than hidden.

### 2.4 Honesty limits

Docking is not activity, and for a transcription factor it is not even direction: a ligand can bind the same pocket and switch the receptor on or off. Vina's scoring error is ±1–2 kcal/mol. No molecular dynamics, no reporter assay, no biofilm assay and no animal data were generated in this paper. The agonist/antagonist labels below are ChEMBL records from *E. coli* reporter assays, not new measurements. Human off-target binding was not assessed.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Best affinity (kcal/mol) | Top-3 poses (kcal/mol) | Measured LasR activity (ChEMBL) | MW | logP | PAINS |
|---|---|---|---|---|---|---|
| CHEMBL473592 | **−9.34** | −9.34, −9.01, −8.73 | Agonist EC50 540 nM; antagonist IC50 53,600 nM | 261.28 | 0.62 | none |
| Psoralen (QUERY, PubChem) | −9.06 | −9.06, −8.98, −8.88 | No LasR binding record; phenotypic anti-QS (Wen et al. 2024) | 186.17 | 2.54 | none |
| CHEMBL264944 | −8.90 | −8.90, −8.41, −8.38 | Antagonist IC50 250 nM (*E. coli* reporter) | 312.16 | 1.81 | none |
| CHEMBL258912 | −8.79 | −8.79, −8.74, −8.36 | Antagonist IC50 1,720 nM | 345.14 | 1.27 | none |
| CHEMBL468790 | −8.56 | −8.56, −8.37, −8.37 | Antagonist IC50 1,720 nM (pipeline record) | 345.14 | 1.27 | none |

All five compounds pass Lipinski's rule with zero violations. Psoralen's Tox21 kNN read-across shows the highest predicted signal in the set (0.469 maximum across 12 assays) — consistent with a furocoumarin that needs a phototoxicity check before any development step. CHEMBL264944's Tox21 maximum is 0.074, the lowest of the antagonists.

### 3.2 Comparison with published docking

Recent computational LasR studies report docking affinities in the same range and the same pocket residues (Tyr56, Trp60, Asp73, Ser129), and a 2026 thiolactone-triazole series showed 79–35% quorum-sensing inhibition at 250 µM in a *P. aeruginosa* reporter strain with LasR docking support — but those studies, like this one, report binding, not function. No published study was found that docks CHEMBL473592 or CHEMBL264944 against LasR with an accompanying functional label; the agonist/antagonist distinction in the table above comes from ChEMBL assay records, and it is the distinction that matters.

### 3.3 The standardisation problem: LasR mutants already exist

Anti-LasR therapy faces a confounder that no docking run can see: lasR loss-of-function mutants are repeatedly recovered from chronic cystic-fibrosis lung infections, where the QS hierarchy rewires and RhlR takes over. A drug that only blocks LasR may therefore fail exactly in the chronic infections where *P. aeruginosa* is hardest to treat. This is why psoralen's triple inhibition (LasR + RhlR + PqsR) matters more than its LasR docking score, and why any validation must test the leads against a lasR-mutant strain as well as wild-type PAO1 — a LasR-only antagonist that fails the mutant test is a narrow-spectrum tool, not a therapy.

## 4. Discussion

### 4.1 The reframe: a docking screen that cannot see direction will promote the wrong molecule

The table's top row is the paper. CHEMBL473592 out-docks every antagonist in the set, and a naive screen — rank by affinity, take the top hit — would nominate an agonist as the lead anti-virulence candidate. An agonist does the opposite of the therapy: it switches on elastase, pyocyanin and biofilm at 540 nM. The error is structural, not numerical: Vina scores the fit of a molecule in a pocket, and the LasR pocket accepts both the native autoinducer and its antagonists. Function lives in what the bound ligand does to the receptor's conformation, which a rigid docking score does not measure. The honest conclusion is that docking is a triage filter for LasR binders, and the functional assay — not a better docking score — is the decision point.

### 4.2 Why the "win" must not be over-read

Three reasons. First, the 0.28 kcal/mol gap between the agonist (−9.34) and psoralen (−9.06), and the 0.44 kcal/mol gap to the best antagonist (−8.90), are far inside Vina's ±1–2 kcal/mol noise — the ranking itself is not significant. Second, psoralen's strong docking (−9.06) comes with no measured LasR binding at all: its 2024 phenotypic effect could run through RhlR or PqsR, or through LasR binding that nobody has measured. Docking psoralen into LasR and calling it a LasR inhibitor would be circular. Third, CHEMBL258912 and CHEMBL468790 share identical descriptors (MW 345.14, logP 1.27) and the same recorded IC50 — they are near-duplicate records, not two independent confirmations.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

All five compounds are PAINS-clean, so no aggregation or redox artefact is expected. The design constraint that does apply is functional: the validation assay must read direction (agonist vs antagonist) in the same experiment, in the same strain, against the same autoinducer concentration — otherwise the table's labels are never tested. Psoralen additionally needs a phototoxicity control (furocoumarins are photoactivated), run in the dark alongside the light condition.

### 4.4 Testable hypotheses

1. In a lasB-gfp reporter strain, CHEMBL264944 suppresses 3-oxo-C12-HSL-induced fluorescence with IC50 < 1 µM (falsifier: IC50 > 5 µM).
2. In the same assay, CHEMBL473592 increases fluorescence (agonism) at ≤ 1 µM (falsifier: no activation, or antagonism — which would refute the ChEMBL label).
3. Psoralen suppresses reporter fluorescence without binding LasR in a purified-protein assay (falsifier: psoralen binds LasR with Kd < 1 µM, which would make it a direct LasR inhibitor after all).
4. CHEMBL264944 reduces pyocyanin and biofilm in wild-type PAO1 at its reporter IC50 (falsifier: no phenotypic effect at 10× IC50).
5. CHEMBL264944 retains activity against a lasR-mutant strain via RhlR/PqsR, or fails honestly (falsifier: the paper's scope is LasR-only; a fail here narrows the claim, it does not kill the molecule).

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): lasB-gfp reporter assay in *E. coli* and in *P. aeruginosa* PAO1 — dose-response for CHEMBL473592, CHEMBL264944, CHEMBL258912 and psoralen, with and without 3-oxo-C12-HSL, reading both activation and inhibition in the same plate. Stage 2 (weeks 4–6): pyocyanin quantification, elastase assay and crystal-violet biofilm assay in PAO1 at reporter-IC50 multiples; lasR-mutant control strain in parallel. Stage 3 (weeks 7–9): checkerboard synergy with polymyxin B and levofloxacin (psoralen's reported synergy is the benchmark), plus HepG2 cytotoxicity and a dark/light phototoxicity control for psoralen. Stage 4 (weeks 10–12): *C. elegans* slow-killing assay for the best antagonist, if stages 1–3 pass. No animal work before the reporter assay settles direction — that is the whole point of this paper.

## 5. Limitations

1. Docking only: no reporter, biofilm or animal data were generated; the 0.44 kcal/mol gap between the agonist and the best antagonist is far inside Vina's ±1–2 kcal/mol noise.
2. Function is inferred, not measured: the agonist/antagonist labels are ChEMBL records from *E. coli* reporter assays, in different laboratories, at different autoinducer concentrations.
3. Single structure: docking used one LasR structure (3IX3); no MD, no induced-fit, no free-energy refinement.
4. Psoralen's mechanism is unresolved: strong docking with no binding record means its phenotypic effect may not be LasR-mediated at all.
5. LasR-mutant escape (§3.3) may limit any LasR-only antagonist to acute, not chronic, infection — untested here.
6. The Pakistan burden figures are single-province surveillance (Punjab, 2018–2019) and a single burn unit (southern Punjab, 2020–2022); they are not national rates.
7. Islamic-canon sweep: the full 23 volumes of Al-Razi's *Kitab al-Hawi* exist in English only in selections, and Ibn al-Nafis's commentary survives as an Arabic manuscript with only partial English translation; those texts were not read in full. No classical work was used as evidence for any molecule.
8. No local-market data: availability and price of the test compounds in Pakistan were not checked.

## 6. Conclusion

The best-docking LasR ligand in this screen is an agonist, and the best antagonist docks third — a docking rank for LasR is a list of binders, not a list of drugs. The paper's usable result is a short, cheap, falsifiable experiment: one reporter assay that reads direction, on four molecules, before any development step. Until that assay runs, nothing here is a treatment claim, and no molecule here should be called a LasR inhibitor on docking evidence alone.

## 7. Policy implications

**Decision-maker:** the National Institute of Health (NIH) Pakistan AMR surveillance programme and the Drug Regulatory Authority of Pakistan (DRAP), with the provincial health departments that run burn units and ICUs. **Decision:** whether to fund anti-virulence screening — a reporter-gene assay for LasR antagonism — as a complement to the existing kill-based antibiotic pipeline. **Exact change:** NIH should add a LasR reporter assay to its AMR reference work and screen the four molecules in this paper (CHEMBL264944, CHEMBL258912, CHEMBL473592 as the agonist control, and psoralen) against local MDR *P. aeruginosa* isolates, publishing the direction (agonist vs antagonist) for each — instead of funding another docking-only study or another broad-spectrum antibiotic that repeats the resistance cycle. **If the evidence reverses this:** if CHEMBL264944 fails the reporter assay (IC50 > 5 µM) and psoralen's effect proves LasR-independent, the LasR programme should stop and the funds should move to RhlR/PqsR targets or to stewardship, not to more LasR docking. **Islamic principle:** hifz al-nafs (preservation of life), defined by Al-Ghazali in *Al-Mustasfa min 'Ilm al-Usul* (c. 1109) and systematised by Al-Shatibi in *Al-Muwafaqat* — and maslaha (public interest): an anti-virulence drug that disarms without killing imposes less selection pressure, so it preserves the antibiotic commons for future patients, which is precisely what maslaha requires of a steward. Ibn Sina's *Canon* (Book II) catalogued *Psoralea* relatives as materia medica; the classical precedent is to test the plant claim, not to repeat it — which is what the reporter assay does.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author thanks the open-data providers — UniProtKB, ChEMBL, PubChem and the RCSB Protein Data Bank — without which this work would not exist.

## References

1. Antimicrobial Resistance Collaborators. Global burden of bacterial antimicrobial resistance in 2019: a systematic analysis. Lancet. 2022;399(10325):629–655. doi:10.1016/S0140-6736(21)02724-0. PMID: 35065702.
2. Saleem, et al. Antibiotic susceptibility surveillance in the Punjab Province of Pakistan: findings and implications. Medicina. 2023;59(7):1215. doi:10.3390/medicina59071215. (P. aeruginosa 18.0% of 2,523 isolates; 68.2% MDR.)
3. Prevalence of microorganisms and antibiotic susceptibility at burn unit of tertiary care hospital in southern Punjab — a retrospective study. J Pak Med Assoc. 2025;75(10):1575. doi:10.47391/JPMA.11604. (P. aeruginosa 34.9% of burn-wound isolates; 14.9% pan-drug resistant.)
4. Wen F, et al. Discovery of psoralen as a quorum sensing inhibitor suppresses Pseudomonas aeruginosa virulence. Appl Microbiol Biotechnol. 2024;108(1):222. doi:10.1007/s00253-024-13067-9. PMID: 38372782.
5. RCSB PDB entry 3IX3: LasR–3-oxo-C12-HSL complex, 1.4 Å. RCSB Protein Data Bank. Accessed 2026-11-28.
6. UniProtKB P25084: transcriptional activator protein LasR, Pseudomonas aeruginosa PAO1. UniProt. Accessed 2026-11-28.
7. ChEMBL target CHEMBL1075207: transcriptional activator protein LasR, Pseudomonas aeruginosa (SINGLE PROTEIN); 45 bioactivities retrieved live 2026-11-28, including antagonist IC50 values for CHEMBL264944 (250 nM) and CHEMBL258912 (1,720 nM) and agonist EC50 540 nM / antagonist IC50 53,600 nM for CHEMBL473592. ChEMBL, EMBL-EBI.
8. Al-Ghazali. Al-Mustasfa min 'Ilm al-Usul. c. 1109. (Defines the five necessities of the law, including hifz al-nafs.)
9. Al-Shatibi. Al-Muwafaqat fi Usul al-Shari'a. 14th c. (Systematises maqasid al-shariah.)
10. Al-Razi. Kitab al-Judari wa al-Hasba (On Smallpox and Measles). c. 910. (First clinical distinction of two contagious diseases; cited for method precedent only.)
11. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Book II, materia medica, checked as a hypothesis source; no lead taken from it.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-111-2026-11-28.json` (LeadForge pipeline raw output: UniProtKB P25084, ChEMBL target CHEMBL1075207, 26 ranked leads, Vina 1.2.7 docking vs PDB 3IX3). Compound identifiers: psoralen (QUERY), CHEMBL473592, CHEMBL264944, CHEMBL258912, CHEMBL468790. No additional data were generated.
