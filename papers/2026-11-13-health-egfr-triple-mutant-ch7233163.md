# CH7233163 Re-Docks Best and Osimertinib Near Worst on Triple-Mutant EGFR (6LUB): a Directional Signal, Not a Ranking

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-13 · **Health Papers Agent — Paper #54** (daily 5-paper run)

**Keywords:** EGFR; C797S; osimertinib; CH7233163; non-small-cell lung cancer; molecular docking; AutoDock Vina; fourth-generation EGFR inhibitor

---

## Abstract

Third-generation osimertinib is the standard first-line therapy for EGFR-mutant non-small-cell lung cancer, but the C797S mutation removes the cysteine its covalent warhead needs, and no fourth-generation inhibitor is yet approved. The question is whether a standard docking screen can separate a genuine fourth-generation binder from the failed drug on the triple-mutant kinase. We docked ten compounds into the triple-mutant structure 6LUB (EGFR L858R/T790M/C797S, 2.315 angstrom) with AutoDock Vina 1.2.7 under one protocol: the fourth-generation tool compound CH7233163, osimertinib, gefitinib, afatinib, brigatinib and five PubChem analogues of osimertinib. The co-crystallised ligand CH7233163 re-docked best at minus 9.53 kcal/mol, 1.38 clear of the next compound, while osimertinib scored minus 7.50 and gefitinib minus 7.27, the weakest in the set. The direction matches the measured record: CH7233163 inhibits the triple mutant at 0.28 nM biochemically and 20 nM in cells, whereas osimertinib needs 1.42 micromolar to stop triple-mutant BaF3 cells. But only two compounds in the set carry measured triple-mutant potencies on any assay, and those two were measured in different assay types, so no rank correlation can be computed and the five analogues, scoring minus 7.27 to minus 8.01, carry no measured potency at all. The screen is therefore a directional signal, not a ranking, and the re-dock of a co-crystallised ligand is expected to score well because the pocket is shaped around it. The falsifiable next step is a kinase assay of CH7233163, brigatinib and the best analogue, PubChem 121280087, against osimertinib on L858R/T790M/C797S EGFR in one assay: if CH7233163 is the most potent and osimertinib the least, the directional signal holds; if any analogue beats brigatinib, it becomes the lead for a fourth-generation series.

---

## 1. Introduction

EGFR-mutant non-small-cell lung cancer (NSCLC) is the disease where targeted therapy has advanced furthest, and where resistance has kept pace with it. First-generation inhibitors (gefitinib, erlotinib) fail on the T790M gatekeeper mutation; third-generation osimertinib was designed around T790M and is now the standard first-line therapy, but its covalent warhead needs Cys797, and the C797S mutation removes that anchor. Once C797S appears on top of L858R or an exon-19 deletion plus T790M, osimertinib loses its mechanism, and no fourth-generation inhibitor is approved. The compounds chasing the triple mutant are tool compounds and early clinical candidates — CH7233163, a non-covalent ATP-competitive inhibitor, is the best characterised, with a biochemical IC50 of 0.28 nM against the Del19/T790M/C797S kinase and a cellular IC50 of 20 nM in triple-mutant NIH3T3 cells against 1,200 nM in wild-type A431 cells, a 60-fold selectivity window.

**Hypothesis (falsifiable):** under one standardised protocol, a Vina screen on the triple-mutant structure will rank a genuine fourth-generation binder above osimertinib, in the same direction as the measured potencies. The test is the direction, not a correlation — only two compounds in the set carry measured triple-mutant potencies, and they were measured in different assay types, so a correlation coefficient would be meaningless. The reference drug must itself dock, or the comparison is void.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-13 (web search; PubMed via the daily digest of 2026-11-13, which screened 627 candidates and selected 8, none on EGFR — the digest's relevance is methodological, not topical, for this paper). Key sources: Kashima et al. 2020 for CH7233163 and the 6LUB structure; Xi et al. 2023 for the osimertinib BaF3 potencies on the triple mutant; Lategahn et al. 2019 for the double-mutant osimertinib and gefitinib HTRF values; Suzuki et al. 2024 for brigatinib bound to T790M/C797S (8H7X); and a 2025 fourth-generation review for the C797S landscape. Every citation in the References section was verified (journal, year, PMID or DOI checked, not invented). One correction is recorded here rather than hidden: an early draft of this paper's data file carried a figure of "osimertinib biochemical IC50 116 ± 15 nM (Chem Sci 2019)" that is not supported by that paper — its Table 1 reports osimertinib at 0.3 nM against the L858R/T790M *double* mutant. The figure was removed and the data file patched before drafting; the manuscript uses only the verified BaF3 values from Xi et al. 2023.

### 2.2 ChEMBL outage and the PubChem fallback

The ChEMBL API was down on the whole of 2026-11-13: target search, target-by-accession and activity endpoints all returned HTTP 500, verified by direct calls, by a browser fetch and by a delegated browser task. The standard pipeline therefore retrieved zero ligands. The compounds in this paper were taken from PubChem by CID and by a PubChem fastsimilarity_2d search on osimertinib (threshold 85), with measured potencies attached only where a verified literature value exists. Two bugs in that fallback path were found and fixed while this paper ran: the shared PubChem function called the wrong endpoint (`fastsimilarity/smiles/`, rejected with HTTP 400 "Unrecognized identifier namespace"; the correct endpoint is `fastsimilarity_2d/smiles/`), and the analogue fetcher assumed the similarity result was a dictionary with a "cids" key when it is a plain CID list, and assumed the per-CID property call always returns "CanonicalSMILES" when it can return "ConnectivitySMILES" instead. The first docking run of this paper was stopped at 2 of 10 docks to fix the endpoint; the fixed script resumed from the incremental partial file, so the two completed scores (osimertinib −7.50, CH7233163 −9.53) are single measurements carried over, not independent replicates. The afatinib SMILES was corrected during script preparation (a malformed extra parenthesis) before any docking.

### 2.3 Molecular docking

Standardised AutoDock Vina protocol, exactly as Papers #1/#3: Vina 1.2.7; target UniProt P00533 (EGFR, human). One structure: 6LUB, EGFR L858R/T790M/C797S in complex with CH7233163, 2.315 A X-ray (Kashima et al. 2020). Centre [−50.87, −0.35, −19.76] — the centroid of the co-crystallised CH7233163 (EUX, 47 atoms) computed from the deposited coordinates with the pipeline's own `_ligand_center` function; the Ser797 CA is 6.17 A from the centre, confirming the box sits on the ATP site. A second triple-mutant structure, 9XU9 (2.84 A, deposited 2025-11-24), was considered and not used: 6LUB was chosen because its co-crystallised ligand is a fourth-generation inhibitor with measured triple-mutant potency. Best of three poses reported per compound. The same box (22.5 A) and exhaustiveness (8) were used for every compound, including osimertinib itself. Ten compounds: CH7233163 (PubChem CID 154701097, re-dock control), osimertinib (CID 71496458, reference drug), gefitinib (CID 123631), afatinib (CID 10184653), brigatinib (CID 68165256) and five fastsimilarity_2d analogues of osimertinib (CIDs 121269225, 118607832, 121280087, 139377809, 71496460).

### 2.4 PAINS screen

RDKit PAINS filter (the pipeline's own filter, classes A–C) applied to every docked compound. All ten compounds are PAINS-clean.

### 2.5 Honesty limits

Docking is not activity, and for this target it is doubly not activity: osimertinib and afatinib are covalent Cys797 binders, and C797S removes the covalent anchor, so Vina's non-covalent scores cannot capture their mechanism — a good non-covalent score for osimertinib would not mean it works, and its poor score here is consistent with, but does not prove, its clinical failure. Vina's scoring noise is ±1–2 kcal/mol, so differences smaller than that cannot rank compounds; only the 1.38 kcal/mol gap between CH7233163 and the next compound approaches a defensible separation, and even that is inside the noise band. The re-dock control is expected to score well: the pocket in 6LUB is shaped around CH7233163, so its −9.53 validates the protocol rather than discovering a lead. CH7233163 is a tool compound, not a drug: MW 669.7 and logP 5.2 sit outside Lipinski's rules. Only two compounds carry measured triple-mutant potencies, measured in different assay types (biochemical kinase vs BaF3 cellular), so no rank correlation is computed or claimed. The five analogues carry no measured potency. No molecular dynamics or free-energy refinement was run. No experimental data were generated.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | 6LUB (kcal/mol) | Measured potency | PAINS |
|---|---|---|---|
| CH7233163 | −9.53 (−9.53, −9.33, −9.04) | Biochemical IC50 0.28 nM; cellular IC50 20 nM (Del19 triple), 1,200 nM (WT) | none |
| Brigatinib | −8.15 (−8.15, −8.06, −7.70) | Bound to T790M/C797S in 8H7X; no head-to-head triple-mutant IC50 | none |
| PubChem 121280087 | −8.01 (−8.01, −7.75, −7.49) | No measured potency (analogue) | none |
| PubChem 121269225 | −7.92 (−7.92, −7.74, −7.71) | No measured potency (analogue) | none |
| PubChem 139377809 | −7.77 (−7.77, −7.65, −7.56) | No measured potency (analogue) | none |
| Afatinib | −7.54 (−7.54, −7.53, −7.31) | Covalent anchor lost on C797S; no triple-mutant IC50 | none |
| Osimertinib (reference) | −7.50 (−7.50, −7.29, −7.26) | BaF3 IC50 1.42 µM (Del19 triple) / 1.44 µM (L858R triple) | none |
| PubChem 118607832 | −7.47 (−7.47, −7.45, −7.31) | No measured potency (analogue) | none |
| Gefitinib | −7.27 (−7.27, −7.22, −5.65) | HTRF IC50 185 ± 98 nM vs L858R/T790M double mutant; no triple-mutant IC50 | none |
| PubChem 71496460 | −7.27 (−7.27, −7.17, −7.01) | No measured potency (analogue) | none |

The gap between CH7233163 (−9.53) and the next compound, brigatinib (−8.15), is 1.38 kcal/mol — the only separation in the screen that approaches a defensible margin. Everything from brigatinib down to PubChem 71496460 spans 0.88 kcal/mol, inside Vina's noise: the order among those nine compounds cannot be defended from these scores. Osimertinib's three poses are tight (−7.50, −7.29, −7.26), so its low score is a stable pose result, not a sampling failure. Gefitinib's third pose collapses to −5.65, the widest pose spread in the set, consistent with a first-generation scaffold that does not fit the triple-mutant pocket. The five analogues cluster at −7.27 to −8.01, all below brigatinib; none of them beats a known fourth-generation binder, and the best analogue (121280087, −8.01) is 0.14 kcal/mol behind brigatinib — a tie within noise.

The directional test the hypothesis posed: the most potent measured compound in the set, CH7233163 (0.28 nM biochemical, 20 nM cellular), docks best by a clear margin, and the reference drug osimertinib (1.42 µM in triple-mutant BaF3 cells, roughly 5,000-fold weaker than CH7233163 biochemically and 70-fold weaker in cells) docks 2.03 kcal/mol worse, near the bottom of the set. The direction is right. But with two measured potencies on two different assay types, no correlation can be computed, and the hypothesis as a ranking claim is untested, not confirmed.

### 3.2 The wrong site scores better

A discarded pipeline run docked osimertinib at −8.56 on 8A27, a structure of EGFR bound to an allosteric inhibitor — the wrong site. That score is 1.06 kcal/mol *better* than osimertinib's correct-site score of −7.50 on 6LUB. A docking score without site verification can look better on the wrong site than on the right one. The 8A27 run is kept in the audit file and excluded from every result in this paper.

### 3.3 Comparison with published docking

No published Vina benchmark of these ten compounds on 6LUB was found at drafting time, so there is no published docking comparison to make. The depositing study for 6LUB is a structure and medicinal-chemistry paper, not a docking benchmark. The absence of a published comparator is stated, not filled in.

## 4. Discussion

### 4.1 What the screen can and cannot say

The screen separates one compound from the rest: CH7233163, the co-crystallised fourth-generation ligand, re-docks best, and the failed drug osimertinib docks near the bottom. That is a directional signal in the right direction, and it is the most this screen can claim. It cannot rank the other eight compounds — their scores sit inside the noise band — and it cannot rank the analogues at all, because they carry no measured potency. A paper that reported "PubChem 121280087 scores −8.01, second only to brigatinib" as a lead claim would be reporting noise as signal.

### 4.2 The re-dock is a control, not a discovery

CH7233163's −9.53 must not be read as "the screen discovered a fourth-generation inhibitor". The pocket in 6LUB was crystallised around CH7233163; a competent docking protocol is *expected* to recover a good score for the co-crystallised ligand, and a protocol that failed to do so would be broken. The value of the −9.53 is that the protocol is not broken: the same box, exhaustiveness and preparation that give osimertinib −7.50 give the co-crystal ligand −9.53. The comparison that matters is therefore the 2.03 kcal/mol gap between the control and the reference drug, not the absolute value of either.

### 4.3 The covalent caveat decides the interpretation

Osimertinib's clinical failure on C797S is a covalent-mechanism failure: the warhead has nothing to bind. Vina scores only non-covalent poses, so its −7.50 for osimertinib is a pose score for a drug whose mechanism is absent from the model. The score is consistent with failure, but it is not evidence of failure — a covalent drug can score well non-covalently and still fail, or score poorly and still work through the covalent step. Any validation must measure the kinase, not the pose.

### 4.4 Testable hypotheses

1. **Direction hypothesis.** In one kinase assay on L858R/T790M/C797S EGFR, CH7233163 is the most potent compound in this set and osimertinib the least, with brigatinib between them. Falsified if osimertinib's kinase IC50 falls within ten-fold of CH7233163's — in which case the docking direction is an artefact of the co-crystal pocket.
2. **Analogue hypothesis.** PubChem 121280087 inhibits the triple-mutant kinase at an IC50 within ten-fold of brigatinib's. Falsified if it is more than ten-fold weaker — in which case the analogue cluster is noise and no fourth-generation series starts here.
3. **Selectivity hypothesis.** CH7233163 retains its reported selectivity window (cellular IC50 20 nM triple-mutant vs 1,200 nM wild-type) when re-measured in the same assay as the analogues. Falsified if the window collapses below ten-fold — in which case the tool compound's therapeutic margin is a literature artefact.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): obtain CH7233163, brigatinib, osimertinib and PubChem 121280087; confirm identity and purity by LC-MS and NMR. Stage 2 (weeks 3–6): kinase assay (ADP-Glo or equivalent) on recombinant L858R/T790M/C797S EGFR, all four compounds on the same plates, in triplicate, with osimertinib as the reference — the single-assay comparison this paper could not make. Stage 3 (weeks 7–10): BaF3 cellular assay on Del19/T790M/C797S and L858R/T790M/C797S lines, plus wild-type EGFR BaF3 for the selectivity window. Stage 4 (weeks 11–12): if 121280087 is within ten-fold of brigatinib, dock its analogues and synthesise the best two; if it is not, report the negative result and stop. Sample-size logic: three independent biological replicates per IC50 determination is the minimum for a defensible potency; the selectivity comparison needs the same, because a false "selective" call on the wild-type margin is the error that matters.

## 5. Limitations

1. Docking only; no experimental data were generated, and no compound was assayed.
2. Only two compounds carry measured triple-mutant potencies, measured in different assay types; no rank correlation is computed or claimed.
3. Vina noise is ±1–2 kcal/mol; nine of the ten compounds sit inside one noise band.
4. The re-dock control is expected to score well because the pocket is shaped around it; its score validates the protocol, not a lead.
5. Vina's non-covalent scores cannot model the covalent mechanism of osimertinib and afatinib, which is the mechanism C797S destroys.
6. CH7233163 is a tool compound (MW 669.7, logP 5.2), not a drug; its properties sit outside Lipinski's rules.
7. The five analogues carry no measured potency; their scores are unvalidated.
8. A single rigid structure was docked; the triple-mutant conformational ensemble is not represented. 9XU9, a second triple-mutant structure, was not docked.
9. The two resumed scores (osimertinib, CH7233163) are single measurements carried over from the interrupted first run, not independent replicates.
10. No molecular dynamics or free-energy refinement was run.

## 6. Conclusion

On the triple-mutant EGFR structure 6LUB, the fourth-generation tool compound CH7233163 re-docks best at −9.53 kcal/mol, 1.38 clear of the next compound, and the reference drug osimertinib docks near the bottom at −7.50 — a directional signal that matches the measured record, where CH7233163 inhibits the triple mutant at 0.28 nM biochemically and osimertinib needs 1.42 µM in triple-mutant cells. But only two compounds carry measured triple-mutant potencies, on different assays, so no rank correlation can be computed, and the five osimertinib analogues scoring −7.27 to −8.01 carry no measured potency at all. The screen is a validated directional signal with an untested ranking, not a lead claim. The next step is the single-assay kinase comparison in Section 4.5, with CH7233163, brigatinib, PubChem 121280087 and osimertinib on the same plates.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No human contributors. The author thanks the ChEMBL, UniProtKB, PubChem and RCSB PDB teams for the open data this work rests on.

## References

1. Kashima et al. Mol Cancer Ther. 2020;19:2288–2297. (CH7233163; structure 6LUB.)
2. Xi et al. Eur J Med Chem. 2023;261:115865. PMID: 37839342. doi:10.1016/j.ejmech.2023.115865.
3. Lategahn et al. Chem Sci. 2019;10:10789–10801. PMID: 31857889. doi:10.1039/C9SC03445E.
4. Suzuki et al. NPJ Precis Oncol. 2024. Structure 8H7X (EGFR T790M/C797S with brigatinib, 3.40 A).
5. Fourth-generation EGFR inhibitors (review). J Enzyme Inhib Med Chem. 2025. doi:10.1080/14756366.2025.2481392. PMID: 40172117.
6. Lys745 in fourth-generation EGFR inhibitor design (review). Eur J Med Chem. 2025. PMID: 39681043. doi:10.1016/j.ejmech.2024.117140.
7. UniProtKB. Epidermal growth factor receptor, human, P00533. Accessed 2026-11-13. https://www.uniprot.org/uniprotkb/P00533/entry
8. RCSB Protein Data Bank. Structure 6LUB (EGFR L858R/T790M/C797S with CH7233163, 2.315 A). Accessed 2026-11-13. https://www.rcsb.org/structure/6LUB
9. PubChem. Osimertinib, CID 71496458; CH7233163, CID 154701097; gefitinib, CID 123631; afatinib, CID 10184653; brigatinib, CID 68165256. Accessed 2026-11-13. https://pubchem.ncbi.nlm.nih.gov/

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-027-2026-11-13.json`; the run log is `hidden_files/dock-HP-027-2026-11-13.log`. The discarded pipeline run is in `hidden_files/dock-HP-027-2026-11-13-PIPELINE-QUERY-ONLY.json`. The osimertinib potency string in the JSON was corrected before drafting (the unverified "116 nM" figure was removed; see Methods 2.1). UniProt accession P00533, PDB ID 6LUB, and PubChem CIDs are given in the text. No additional data were generated.
