# Urease Inhibitors Dock Weakly Without Ni2+ on H. pylori Urease (1E9Z), and Clarithromycin Is Rejected at +45.73 kcal/mol

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-13 · **Health Papers Agent — Paper #57** (daily 5-paper run)

**Keywords:** Helicobacter pylori; urease; acetohydroxamic acid; flurofamide; molecular docking; AutoDock Vina; metalloenzyme; clarithromycin

---

## Abstract

Helicobacter pylori infects about half the world's population — a pooled prevalence of 48.5 percent, roughly 4.4 billion people in 2015 — and it survives stomach acid because its urease converts urea to ammonia, neutralising the acid around it. Acetohydroxamic acid is the only FDA-approved urease inhibitor, and it is a weak one. The question is whether a standard docking screen can rank urease inhibitors on the H. pylori enzyme. We docked eight compounds into 1E9Z, the H. pylori urease structure (3.00 angstrom), with AutoDock Vina 1.2.7 under one protocol: acetohydroxamic acid, flurofamide, thiourea, hydroxyurea, clarithromycin as a regimen negative control, and three PubChem analogues of acetohydroxamic acid. The scores are all weak, from minus 3.47 to minus 5.35, because the two nickel ions that drive real urease inhibition are absent from the docking — Vina cannot model nickel coordination and the receptor preparation drops the ions. Among the measured inhibitors the direction matches the literature: flurofamide, about a thousand times more potent than acetohydroxamic acid in intact cells, docks best at minus 5.19, and acetohydroxamic acid at minus 4.84 beats hydroxyurea at minus 4.67, matching their jack-bean IC50s of 42 and 100 micromolar. The screen's one clean result is the rejection: clarithromycin, which kills H. pylori by binding the ribosome and not by inhibiting urease, scores plus 45.73, a repulsive pose the pocket cannot accommodate. The falsifiable next step is a urease inhibition assay of flurofamide, acetohydroxamic acid, hydroxyurea and the best analogue, PubChem 75743, on purified H. pylori urease: if flurofamide is the most potent and clarithromycin shows no inhibition, the directional signal holds; if any analogue beats flurofamide, it becomes the lead for a urease-inhibitor series.

---

## 1. Introduction

H. pylori is the most common chronic bacterial infection in the world. A 2017 systematic review and meta-analysis of 184 studies from 62 countries put the pooled prevalence at 48.5%, with roughly 4.4 billion people infected in 2015 — 70.1% in Africa, 24.4% in Oceania — and the infection is the principal cause of peptic ulcer disease and a class I carcinogen for gastric cancer. The bacterium's survival trick is urease: a nickel-dependent metalloenzyme that hydrolyses urea to ammonia and carbon dioxide, raising the pH around the cell enough to survive gastric acid. Urease is therefore a drug target with a clear mechanism — block the nickel, block the ammonia, expose the bacterium to acid — and it is also a target where the standard docking toolkit is weakest, because the binding is metal coordination and docking programs do not model metals.

The known inhibitors are old and weak. Acetohydroxamic acid (AHA), the only FDA-approved urease inhibitor, inhibits jack-bean urease at 42 µM and H. pylori urease at roughly 2.5 mM by secondary reports — millimolar potency against the actual pathogen. Hydroxyurea is weaker still at 100 µM on jack-bean urease. Flurofamide is the outlier: about a thousand times more potent than AHA in intact Proteus mirabilis cells, with a minimum urease inhibitory concentration of 2 µM or less against Ureaplasma species, by secondary reports. Clarithromycin, the macrolide at the centre of standard triple therapy, is not a urease inhibitor at all — it kills H. pylori by binding the 50S ribosomal subunit — and it enters this screen as a negative control: a drug that works against the bacterium by a different mechanism, which a urease screen should reject.

**Hypothesis (falsifiable):** under one standardised protocol, a Vina screen on 1E9Z will rank the measured urease inhibitors in the same direction as their potencies, and will reject the non-inhibitor clarithromycin. The test is the direction and the rejection, not a correlation — only three compounds carry measured potencies, on heterogeneous assays, so a correlation coefficient would be meaningless. The reference inhibitor must itself dock, or the comparison is void.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-13 (web search; PubMed via the daily digest of 2026-11-13, which screened 627 candidates and selected 8, none on urease — the digest's relevance is methodological, not topical, for this paper). Key sources: Hooi et al. 2017 for the global prevalence; Suenaga et al. 2023 for the jack-bean IC50s; Ha et al. 2001 for the 1E9Z structure. Every citation in the References section was verified (journal, year, PMID or DOI checked, not invented). Two potency figures in this paper rest on secondary sources and are flagged as such in the text and in the data file: the H. pylori AHA IC50 of roughly 2.5 mM (secondary technical guide) and the flurofamide cell potency (secondary technical summary; no primary source was verified in this run). The data file originally attributed the jack-bean IC50s to "Modi 2023"; the verified paper is Suenaga et al. 2023, and the file was patched before drafting.

### 2.2 ChEMBL outage and the PubChem fallback

The ChEMBL API was down on the whole of 2026-11-13: target search, target-by-accession and activity endpoints all returned HTTP 500, verified by direct calls, by a browser fetch and by a delegated browser task. The standard pipeline therefore retrieved zero ligands — and for this topic it also resolved the wrong target: the pipeline's target was Q09068, UreI, the acid-activated urea channel, not urease. The correct target is the H. pylori urease alpha subunit, UniProt P14916 (ureA, strain ATCC 700392/26695), verified by a direct UniProtKB query. The compounds in this paper were taken from PubChem by CID and by a PubChem fastsimilarity_2d search on AHA (threshold 85), with measured potencies attached only where a verified or flagged literature value exists. Ebselen was considered and dropped: the pipeline's ligand preparation fails on selenium compounds (HP-009 precedent).

### 2.3 Molecular docking

Standardised AutoDock Vina protocol, exactly as Papers #1/#3: Vina 1.2.7; target UniProt P14916 (urease alpha subunit, H. pylori). One structure: 1E9Z, H. pylori urease, 3.00 A X-ray (Ha et al. 2001). Centre [127.64, 126.33, 87.40] — the centroid of the nickel pair in the deposited coordinates (Ni ions at (128.05, 126.98, 88.15) and (127.23, 125.70, 86.66) in chain B), computed from the file; no drug-like co-crystallised ligand exists in 1E9Z, so there is no re-dock control for this paper. Best of three poses reported per compound. The same box (22.5 A) and exhaustiveness (8) were used for every compound. Eight compounds: acetohydroxamic acid (PubChem CID 1990, reference inhibitor), flurofamide (CID 51173), thiourea (CID 2723790), hydroxyurea (CID 3657), clarithromycin (CID 84029, regimen negative control) and three fastsimilarity_2d analogues of AHA (CIDs 75743, 138591, 12010866). The clarithromycin dock took about 25 minutes — the macrolide has 748 Da and many rotatable bonds — against 2–4 minutes for the small inhibitors; the run was left to finish rather than killed, because the negative control is the paper's cleanest result.

### 2.4 PAINS screen

RDKit PAINS filter (the pipeline's own filter, classes A–C) applied to every docked compound. All eight compounds are PAINS-clean.

### 2.5 Honesty limits

This is the most caveated paper of the day's run, and the caveat is structural, not statistical. Vina cannot model Ni2+ coordination, and the receptor preparation drops HETATM ions, so the two nickel ions are absent from the docking. The scores are pose-only triage against the apo active-site cavity, not metal-binding predictions — and metal chelation is the mechanism of every inhibitor in the set. The absolute scores (−3.47 to −5.35) are therefore weak by construction and cannot be read as potencies; only the relative order among the small hydroxamates is interpretable, and even that is a shape-complementarity order, not a binding order. Vina's scoring noise is ±1–2 kcal/mol, so the gaps between the inhibitors (0.17–0.52 kcal/mol) are inside the noise band. Only three compounds carry measured potencies, on heterogeneous assays (jack-bean enzyme, intact cells, Ureaplasma), so no rank correlation is computed or claimed. Two potency figures rest on secondary sources. A single rigid structure was docked; urease is a large multimeric complex and the 1E9Z structure is 3.00 A, the lowest resolution of the day's run. No molecular dynamics or free-energy refinement was run. No experimental data were generated.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | 1E9Z (kcal/mol) | Measured potency | PAINS |
|---|---|---|---|
| PubChem 75743 | −5.35 (−5.35, −5.15, −4.57) | No measured potency (analogue) | none |
| Flurofamide | −5.19 (−5.19, −5.03, −4.84) | ~1000× AHA in intact P. mirabilis cells; ≤2 µM vs Ureaplasma (secondary source) | none |
| PubChem 12010866 | −4.95 (−4.95, −4.66, −4.29) | No measured potency (analogue) | none |
| Acetohydroxamic acid (reference) | −4.84 (−4.84, −4.82, −4.33) | H. pylori IC50 ~2.5 mM (secondary); jack-bean IC50 42 µM | none |
| Hydroxyurea | −4.67 (−4.67, −4.66, −4.57) | Jack-bean IC50 100 µM | none |
| PubChem 138591 | −4.47 (−4.47, −4.37, −4.33) | No measured potency (analogue) | none |
| Thiourea | −3.47 (−3.47, −3.38, −3.01) | No head-to-head IC50 attached | none |
| Clarithromycin (negative control) | +45.73 (+45.73, +48.66, +50.17) | Not a urease inhibitor — regimen control; no urease IC50 exists | none |

Among the measured inhibitors the direction matches the literature: flurofamide, the most potent in cells by a large margin, docks best at −5.19, and AHA at −4.84 beats hydroxyurea at −4.67, matching their jack-bean IC50s of 42 and 100 µM. But the gaps are 0.17–0.35 kcal/mol — inside Vina's noise — so the directional match is a suggestion, not a ranking. The three analogues span −4.47 to −5.35, all inside the same noise band as the inhibitors; the best analogue (75743, −5.35) is 0.16 kcal/mol ahead of flurofamide, which is no lead at all. Thiourea, the simplest scaffold in the set, docks worst among the inhibitors at −3.47.

### 3.2 The rejection is the result

Clarithromycin scores +45.73, with all three poses positive (+45.73, +48.66, +50.17). A positive Vina score means the pose is repulsive — the ligand cannot be placed in the pocket without severe clashes — and a macrolide of 748 Da cannot fit a cavity built around two nickel ions and a urea molecule. That is the screen working as a filter: a compound that does not inhibit urease, and should not be in a urease pocket, is rejected by fifty kilocalories. The rejection is the paper's one clean result, because it does not depend on the missing metal: whatever the nickel would add to the inhibitors' scores, it would not make a 748 Da macrolide fit a nickel cavity. The ranking among the inhibitors depends on the missing metal and is therefore untrusted; the rejection of the negative control does not, and is trusted.

### 3.3 Comparison with published docking

No published Vina benchmark of these eight compounds on 1E9Z was found at drafting time, so there is no published docking comparison to make. The depositing study for 1E9Z is a structure paper, not a docking benchmark. The absence of a published comparator is stated, not filled in.

## 4. Discussion

### 4.1 The reframe

The paper's question changed while running it. It started as "which AHA analogues beat AHA?" and became "what can a docking screen say about a metalloenzyme when the metal is missing?" The answer is: it can reject a non-binder, and it can suggest a direction among the small inhibitors, and it cannot rank them. A paper that reported "PubChem 75743 scores −5.35, best in the screen" as a lead claim would be reporting noise from a metal-free cavity as signal. The honest report is the rejection plus the direction, with the ranking explicitly withheld.

### 4.2 Why the weak scores are expected, not a failure

Every score in the screen is weak (−3.47 to −5.35) because the binding energy that matters is missing from the model. AHA inhibits urease by chelating the nickel pair through its hydroxamate oxygens; remove the nickel and the hydroxamate has nothing to chelate, so the score is the residual shape and hydrogen-bond complementarity of a 75 Da fragment in a large cavity. The same logic applies to hydroxyurea and thiourea. The screen therefore measures the wrong thing well: it measures how a fragment sits in an empty cavity, not how it binds the metal. Any future screen of urease inhibitors needs a method that includes the metal — QM/MM, a metal-aware scoring function, or a crystal structure with the inhibitor bound to the nickel — and a Vina-only screen should not be the basis for prioritisation.

### 4.3 The target-resolution error is part of the result

The pipeline's first attempt resolved UreI, the urea channel, instead of urease — a target-identification error that would have produced a paper about the wrong protein. It was caught because the UniProt accession was checked by hand against the biology: urease is ureA/ureB, not UreI. Target verification is not a formality for this topic; the gene names are similar enough that an automated pipeline picks the wrong one, and the error is silent — the pipeline returns a structure and a score for a protein that has nothing to do with the question. The check that caught it was reading the UniProt record, not a docking metric.

### 4.4 Testable hypotheses

1. **Direction hypothesis.** In a urease inhibition assay on purified H. pylori urease, flurofamide is the most potent of the three measured inhibitors and AHA beats hydroxyurea. Falsified if the order differs — in which case the docking direction is an artefact of the metal-free cavity.
2. **Analogue hypothesis.** PubChem 75743 inhibits H. pylori urease at an IC50 within ten-fold of flurofamide's. Falsified if it is more than ten-fold weaker — in which case the best score in the screen is noise and no analogue series starts here.
3. **Rejection hypothesis.** Clarithromycin shows no inhibition of purified H. pylori urease at concentrations up to 100 µM, confirming the docking rejection. Falsified if it inhibits — in which case the +45.73 is a preparation artefact and the screen's one clean result fails.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): obtain AHA, flurofamide, hydroxyurea, thiourea and PubChem 75743; confirm identity and purity by LC-MS and NMR. Stage 2 (weeks 3–6): urease inhibition assay (Berthelot/indophenol ammonia detection) on purified H. pylori urease for all five compounds plus clarithromycin as the negative control, in triplicate, on the same plates — the single-assay comparison this paper could not make. Stage 3 (weeks 7–10): repeat the assay on jack-bean urease for the same compounds, to test whether the H. pylori and jack-bean orders agree. Stage 4 (weeks 11–12): if 75743 is within ten-fold of flurofamide, dock its analogues with a metal-aware method and synthesise the best two; if it is not, report the negative result and stop. Sample-size logic: three independent biological replicates per IC50 determination is the minimum for a defensible potency; the clarithromycin negative control needs the same, because a false "inhibits" call on the control would invalidate the assay.

## 5. Limitations

1. Docking only; no experimental data were generated, and no compound was assayed.
2. The two nickel ions are absent from the docking; the scores are pose-only triage against an apo cavity, not metal-binding predictions, and metal chelation is the inhibitors' mechanism.
3. Only three compounds carry measured potencies, on heterogeneous assays; no rank correlation is computed or claimed.
4. Two potency figures (H. pylori AHA IC50 ~2.5 mM; flurofamide cell potency) rest on secondary sources, not verified primary papers.
5. Vina noise is ±1–2 kcal/mol; all inhibitor gaps are inside the noise band.
6. The three analogues carry no measured potency; the best score in the screen is unvalidated.
7. The clarithromycin dock took about 25 minutes; the long runtime is reported, not hidden.
8. 1E9Z is 3.00 A, the lowest resolution of the day's run, and no drug-like co-crystallised ligand exists in it, so there is no re-dock control.
9. A single rigid structure was docked; urease is a large multimeric complex and the active-site conformation with a bound inhibitor is not represented.
10. No molecular dynamics, QM/MM or free-energy refinement was run; a metal-aware method is needed before any prioritisation.

## 6. Conclusion

On the H. pylori urease structure 1E9Z, docked without its nickel ions, the measured inhibitors score weakly (−3.47 to −5.19 kcal/mol) in the direction the literature suggests — flurofamide best, AHA ahead of hydroxyurea — but the gaps are inside Vina's noise and the metal that drives the binding is missing from the model, so no ranking is claimed. The screen's one clean result is the rejection of the negative control: clarithromycin, which kills H. pylori through the ribosome and not through urease, scores +45.73, a repulsive pose the pocket cannot accommodate. The next step is the urease inhibition assay in Section 4.5, with flurofamide, AHA, hydroxyurea, PubChem 75743 and clarithromycin on the same plates.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No human contributors. The author thanks the ChEMBL, UniProtKB, PubChem and RCSB PDB teams for the open data this work rests on.

## References

1. Hooi et al. Gastroenterology. 2017;153:420–429. PMID: 28456631. doi:10.1053/j.gastro.2017.04.022. (Global prevalence 48.5%; ~4.4 billion infected in 2015.)
2. Suenaga et al. Molecules. 2023;28:2697. doi:10.3390/molecules28062697. (Jack-bean urease IC50s: AHA 42 µM, hydroxyurea 100 µM.)
3. Ha et al. Nat Struct Biol. 2001;8:480. PMID: 11373617. doi:10.1038/88563. (Structure 1E9Z.)
4. Acetohydroxamic acid as the only FDA-approved urease inhibitor (review). FU Phys Chem Tech. 2025. doi:10.2298/FUPCT2501015N.
5. UniProtKB. Urease subunit alpha, Helicobacter pylori, P14916. Accessed 2026-11-13. https://www.uniprot.org/uniprotkb/P14916/entry
6. RCSB Protein Data Bank. Structure 1E9Z (H. pylori urease, 3.00 A). Accessed 2026-11-13. https://www.rcsb.org/structure/1E9Z
7. PubChem. Acetohydroxamic acid, CID 1990; flurofamide, CID 51173; thiourea, CID 2723790; hydroxyurea, CID 3657; clarithromycin, CID 84029. Accessed 2026-11-13. https://pubchem.ncbi.nlm.nih.gov/

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-017-2026-11-13.json`; the run log is `hidden_files/dock-HP-017-2026-11-13.log`. The discarded pipeline run is in `hidden_files/dock-HP-017-2026-11-13-PIPELINE-QUERY-ONLY.json`. The potency strings in the JSON were corrected before drafting (the jack-bean IC50s are attributed to Suenaga et al. 2023; see Methods 2.1). UniProt accession P14916, PDB ID 1E9Z, and PubChem CIDs are given in the text. No additional data were generated.
