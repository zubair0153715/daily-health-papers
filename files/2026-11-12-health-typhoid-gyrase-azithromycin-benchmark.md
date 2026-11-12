# Four Whole-Cell-Active Compounds Dock Into S. Typhi GyrB at −8.39 to −9.41 kcal/mol, But Azithromycin Cannot Be Docked and the Potencies Are Phenotypic, Not Gyrase Binding

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-12 · **Health Papers Agent — Paper #49** (daily 5-paper run)

**Keywords:** Salmonella Typhi; DNA gyrase; azithromycin; extensively drug-resistant typhoid; molecular docking; AutoDock Vina; phenotypic screening; XDR typhoid

---

## Abstract

Extensively drug-resistant (XDR) typhoid — resistant to ampicillin, chloramphenicol, co-trimoxazole, fluoroquinolones and ceftriaxone — emerged in Hyderabad, Sindh in late 2016 and now accounts for roughly 70% of Salmonella Typhi in Pakistan, leaving azithromycin as the last oral option, with resistance already appearing. The gap this paper attacks is whether a standardised docking screen can find a DNA gyrase binder better than azithromycin for XDR typhoid. We ran the LeadForge pipeline (UniProtKB P0A2I4 → ChEMBL target CHEMBL614448, 5 bioactivities → PubChem → RDKit ADMET/PAINS → AutoDock Vina 1.2.7) and docked four whole-cell-active compounds into the 2.2 Å S. Typhi GyrB structure 6J90, with the grid centre audited to the co-crystallised ATP centroid. All four leads docked strongly — CHEMBL3585716 −9.41, CHEMBL5171589 −9.28, CHEMBL3585709 −9.27, CHEMBL3585717 −8.39 kcal/mol — but azithromycin itself could not be docked at all (the Vina run timed out at the pipeline's 900-second limit on the 749 Da macrolide), so no "beats azithromycin" claim can be made, and the docking order does not track whole-cell potency (Spearman ρ = −0.20, n = 4, p = 0.80). Critically, no S. Typhi DNA gyrase target exists in ChEMBL at all — the potencies used here are phenotypic whole-cell data, not gyrase binding data — so this screen tests a hypothesis (does whole-cell potency track GyrB binding?) rather than validating one. The falsifiable next step is a GyrB ATPase inhibition assay of the four leads against azithromycin with whole-cell MICs: if a lead inhibits GyrB at concentrations matching its MIC, it is a genuine GyrB-targeting candidate; if it does not, its whole-cell activity works through another target.

---

## 1. Introduction

Typhoid fever still sickens millions, and Pakistan carries one of the highest burdens: roughly 493.5 cases per 100,000 people, with incidence doubling from 7 to 15 per 100,000 as XDR strains spread. Extensively drug-resistant Salmonella Typhi — resistant to ampicillin, chloramphenicol, trimethoprim-sulfamethoxazole, fluoroquinolones and the third-generation cephalosporin ceftriaxone — was first detected in Hyderabad, Sindh in late 2016, and has since caused more than 17,000 XDR cases nationally, including 14,360 in Karachi between January 2017 and June 2021. By 2019–2021 XDR strains made up about 70% of S. Typhi isolates, and in a 2017–2019 population-based study XDR accounted for 57% of culture-confirmed cases. Azithromycin is now the last reliable oral option: 96.9% of isolates were susceptible in a 2024–25 paediatric cohort (n = 65, POF Hospital), but a Gilgit study already found 2.9% azithromycin resistance and 1% meropenem resistance, with 40.3% of 208 isolates XDR. DNA gyrase subunit B (GyrB) is a validated antibacterial target — its ATP-binding site is druggable and distinct from the fluoroquinolone site on GyrA — so a GyrB binder would sidestep existing XDR resistance. The falsifiable hypothesis of this paper is: **a standardised Vina screen on the S. Typhi GyrB structure 6J90 ranks whole-cell-active compounds in the same order as their measured anti-Typhi potencies, with azithromycin as the reference.**

## 2. Methods

### 2.1 Literature basis

The XDR definition, Hyderabad emergence, case counts and resistance proportions are from Klemm et al., mBio 2018 (PMID 29463654) and Qamar et al., Open Forum Infectious Diseases 2025 (PMID 40212028), with the Gilgit resistance figures from Life and Science 2026 (doi:10.37185/LnS.1.1.1148) and the plasmid epidemiology from Scientific Reports (doi:10.1038/s41598-026-37560-5). Today's literature digest (research-team digest 2026-11-12, 840 candidates screened, 8 selected) contained no paper topical to this benchmark and is cited only as a methodological source. All database identifiers were verified live on 2026-11-12.

### 2.2 Molecular docking

Standardised AutoDock Vina 1.2.7 protocol, exactly as Papers #1 and #3: UniProtKB P0A2I4 (S. Typhi DNA gyrase subunit B, gyrB, 804 aa) → ChEMBL target CHEMBL614448 ("Salmonella typhi", ORGANISM) → 5 bioactivities → PubChem verification of azithromycin (CID 447043) → RDKit similarity/ADMET/PAINS → Vina docking of the top 5 leads (the reference query plus four ChEMBL leads) into PDB 6J90 (S. Typhi GyrB N-terminal domain in complex with ATP, chain A, 2.2 Å). Grid centre [−12.65, 51.02, 28.42] is the co-crystallised ATP centroid exactly (audited against the ATP atoms in the PDB file); ATP is the ATP-site ligand, so the grid sits on the correct drug site. Box 22.5 Å, exhaustiveness 8, best of three poses reported for every molecule, same protocol for reference and leads. The per-ligand Vina limit in this pipeline is 900 seconds.

**Correction history (disclosed, not hidden).** The first docking run for this topic was invalid and is discarded: UniProt P0A2I4 was correct, but the ChEMBL target resolved to CHEMBL2074 maltase-glucoamylase — the by-accession endpoint failed and the fallback picked the first entry of the text-search list — so the run docked N-substituted deoxynojirimycin iminosugars (alpha-glucosidase inhibitors) into the GyrB pocket. Those numbers are kept in `dock-HP-051-2026-11-12.json` for audit and are not used anywhere in this paper. A live search of the ChEMBL website on 2026-11-12 (verified twice) established that **no ChEMBL target for Salmonella Typhi DNA gyrase (subunit A or B) exists**: the only S. Typhi targets are organism targets. The corrected run therefore uses the closest verified target, CHEMBL614448 "Salmonella typhi" (ORGANISM, 3,065 associated compounds, 4,418 bioactivities, 387 assays), monkey-patched in because the ChEMBL target-by-accession API endpoint returned HTTP 500 pages and timeouts throughout 2026-11-12. The bioactivities are the verbatim ChEMBL API response for CHEMBL614448 saved to `hidden_files/chembl-activities-CHEMBL614448-2026-11-12.json` (the complete set: 5 activities with pChEMBL ≥ 5, page_meta total_count 5), because the live activity endpoint timed out on limit=50 queries and intermittently returned HTML error pages all day; only the record transport differs, not the data. The structure picker was not wrong in either run: 6J90 is the correct S. Typhi GyrB structure in both.

**The phenotypic caveat — read before the Results.** CHEMBL614448 is an organism target, so its bioactivities are whole-cell potencies (MIC/EC50 against S. Typhi), not gyrase binding measurements. The docking-versus-potency comparison in this paper is therefore a hypothesis test — does whole-cell anti-Typhi potency track with GyrB ATP-site binding? — and not a target-validated benchmark. No claim that any lead "inhibits gyrase" follows from this screen.

### 2.3 PAINS screen

RDKit PAINS filter applied to every docked molecule. All four docked leads and azithromycin are PAINS-clean. The fifth ChEMBL compound (CHEMBL3585711, IC50 2.72 µM) was not docked (only the top 5 are docked) and is also PAINS-clean.

### 2.4 Honesty limits

Docking is not activity: Vina scores carry ±1–2 kcal/mol noise, a single rigid structure (6J90) cannot capture induced fit, and no experimental data, molecular dynamics, or free-energy refinement were run. The potencies are phenotypic, so even a perfect rank correlation would not prove GyrB is the target. No clinical recommendation follows from this paper.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Measured whole-cell potency (ChEMBL) | Best affinity (kcal/mol) | Poses (kcal/mol) | PAINS |
|---|---|---|---|---|
| CHEMBL3585716 | IC50 3.66 µM (pChEMBL 5.44) | **−9.41** | −9.41, −8.72, −8.63 | clean |
| CHEMBL5171589 | EC50 280 nM (pChEMBL 6.55) | −9.28 | −9.28, −8.90, −8.66 | clean |
| CHEMBL3585709 | IC50 3.06 µM (pChEMBL 5.51) | −9.27 | −9.27, −8.77, −8.73 | clean |
| CHEMBL3585717 | IC50 3.19 µM (pChEMBL 5.50) | −8.39 | −8.39, −8.39, −7.80 | clean |
| **Azithromycin (query)** | reference drug | **could not be docked** | — | clean |

All four leads docked strongly into the GyrB ATP pocket (−8.39 to −9.41 kcal/mol), with consistent poses. The spread among the four (1.02 kcal/mol) sits inside Vina's ±1–2 kcal/mol noise, so the four cannot be ordered by these scores. Azithromycin — the reference drug and the last oral option for XDR typhoid — could not be docked: the Vina run timed out at the pipeline's 900-second per-ligand limit (the process ran for over 16 CPU-minutes without returning), and an earlier independent attempt also failed with a Vina command error. The failure is a property of the molecule in this protocol (749 Da macrolide, 14 hydrogen-bond acceptors, 2 Lipinski violations), not of the structure: the same protocol docked all four smaller leads on the same grid. There is therefore no reference score, and no lead can be said to beat — or lose to — azithromycin in this screen.

### 3.2 Comparison with published docking

No published Vina benchmark of these four ChEMBL compounds on 6J90 was found in the literature sweep, so there is no published docking comparison to make. The four scores reported here are new reference points for this structure under this protocol.

### 3.3 The ranking does not track whole-cell potency

The docking order shows no agreement with measured whole-cell potency: Spearman ρ = −0.20 (n = 4, p = 0.80). The most potent compound by far — CHEMBL5171589 (EC50 280 nM, pChEMBL 6.55, the only lead under 1 µM) — ranks second by Vina, while the weakest measured lead, CHEMBL3585716 (IC50 3.66 µM, pChEMBL 5.44), ranks first. The other three leads cluster at 2.72–3.66 µM, a potency range too narrow to rank. This is the expected outcome if whole-cell potency is driven by factors docking cannot see (permeation through the Gram-negative outer membrane, efflux, or a different target): GyrB binding is only one contributor to a whole-cell MIC, and for these compounds it may not be the dominant one.

Drug-likeness is a second problem. Only CHEMBL5171589 is drug-like (MW 356.86, logP 3.02, zero Lipinski violations). The other three docked leads are large, lipophilic brominated analogues from a single chemical series (assays CHEMBL3588323): MW 532–637, logP 5.45–6.33, two Lipinski violations each. The undocked fifth compound (CHEMBL3585711) is worse still (MW 715.97, logP 7.09). Whatever their GyrB scores, the brominated series is a poor starting point for an oral drug. ToxGuard Tox21 read-across flags appear on every molecule; these are similarity-screen flags, not toxicity findings, and are reported as such.

## 4. Discussion

### 4.1 The reframe

This paper set out to benchmark GyrB binders against azithromycin and instead established three facts that change the question. First, there is no S. Typhi DNA gyrase target in ChEMBL, so a target-specific benchmark for this organism cannot be built from ChEMBL at all — only a phenotypic one. Second, the reference drug cannot be docked under this protocol, so the screen has no baseline. Third, the four leads that do dock are strong binders in absolute terms but their order does not track whole-cell potency, which is exactly what a phenotypic dataset should produce if GyrB is not the potency-driving target for these molecules. The honest reframe is that this screen is a pocket-fit test, not a potency ranking: it shows four whole-cell-active compounds fit the GyrB ATP site, and it cannot show whether GyrB is why they kill S. Typhi.

### 4.2 Why the "win" must not be over-read

No lead "wins" here. There is no reference score to beat, the 1.02 kcal/mol spread among the leads is inside Vina noise, and the strongest docking score belongs to the weakest whole-cell compound. A reader who takes −9.41 kcal/mol as evidence that CHEMBL3585716 is a GyrB inhibitor would be making three errors at once: mistaking a docking score for a binding measurement, mistaking a phenotypic potency for a target potency, and ignoring that the molecule violates two Lipinski rules.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

No molecule in this paper carries a PAINS alert, so no redox-control redesign is needed. The design constraint here is different: the validation assay must separate GyrB inhibition from whole-cell killing (see 4.5), because the two need not coincide.

### 4.4 Testable hypotheses

1. **CHEMBL5171589 kills S. Typhi through GyrB.** A GyrB ATPase inhibition assay will show inhibition at concentrations near its whole-cell EC50 (280 nM); if it inhibits GyrB only at micromolar concentrations, its whole-cell activity works through another target.
2. **The brominated series does not act through GyrB.** The three CHEMBL35857xx leads will show no GyrB inhibition at their whole-cell IC50s (3–3.7 µM), and their MICs will be unchanged in a GyrB-overexpressing strain — if their MICs shift, GyrB is involved after all.
3. **Azithromycin's failure is a protocol limit, not a biology result.** Docking azithromycin at reduced exhaustiveness, or with a flexible-receptor protocol, will return a score; if it still fails, the macrolide needs a different method (e.g. induced-fit docking) before any GyrB comparison can be made.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): GyrB ATPase inhibition assay (purified S. Typhi GyrB, malachite-green phosphate readout) for the four leads, 10-point dose–response in triplicate, with novobiocin (a known GyrB ATP-site inhibitor) as the positive control. Stage 2 (weeks 4–6): whole-cell MICs against S. Typhi (including an XDR clinical isolate if available under appropriate biosafety approval) for the four leads, compared with their GyrB IC50s — the ratio is the test of hypothesis 1. Stage 3 (weeks 7–12): for any lead whose GyrB IC50 matches its MIC, a GyrB-overexpression shift assay and a time-kill curve; for CHEMBL5171589 specifically, a medicinal-chemistry assessment of its drug-like scaffold as the starting point for optimisation.

## 5. Limitations

1. Docking only: no experimental data, no molecular dynamics, no free-energy refinement.
2. The potencies are phenotypic whole-cell data, not gyrase binding data; the rank correlation (ρ = −0.20, n = 4) tests a hypothesis, not a validation.
3. No S. Typhi DNA gyrase target exists in ChEMBL — the target-specific benchmark this topic posed cannot be built from ChEMBL.
4. Azithromycin could not be docked (Vina 900-second timeout, twice), so there is no reference score.
5. Vina noise (±1–2 kcal/mol) exceeds the 1.02 kcal/mol spread among the four leads; they cannot be ordered.
6. Single rigid structure (6J90, 2.2 Å); induced fit and the DNA-bound holoenzyme are not modelled.
7. Three of the four leads violate two Lipinski rules and come from one brominated series; only CHEMBL5171589 is drug-like.
8. The ChEMBL bioactivities were fetched via a saved verbatim API response because the live endpoint was unstable all day (see Methods 2.2); the data are real ChEMBL records, but the fetch was not the pipeline's live call.

## 6. Conclusion

Four whole-cell-active compounds dock strongly into the S. Typhi GyrB ATP pocket (−8.39 to −9.41 kcal/mol), but the reference drug azithromycin cannot be docked under this protocol, the docking order does not track whole-cell potency (Spearman ρ = −0.20, n = 4), and no S. Typhi DNA gyrase target exists in ChEMBL — the potencies are phenotypic, not target binding. The screen establishes pocket fit, not GyrB inhibition. The next step is a GyrB ATPase assay paired with whole-cell MICs, which will settle whether any of these compounds acts through GyrB at all.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content.

## References

1. Klemm EJ, Shakoor S, Page AJ, et al. Emergence of an extensively drug-resistant Salmonella enterica serovar Typhi clone harboring a promiscuous plasmid encoding resistance to fluoroquinolones and third-generation cephalosporins. mBio. 2018;9(1):e00105-18. doi:10.1128/mBio.00105-18. PMID 29463654
2. Qamar FN, Yousafzai MT, Qazi I, et al. Trends of enteric fever and emergence of extensively drug-resistant typhoid in Pakistan: population-based surveillance. Open Forum Infect Dis. 2025. doi:10.1093/ofid/ofaf106. PMID 40212028
3. Life and Science. Azithromycin and meropenem resistance among Salmonella Typhi isolates, Gilgit, Pakistan. Life and Science. 2026. doi:10.37185/LnS.1.1.1148
4. Scientific Reports. Plasmid epidemiology of extensively drug-resistant Salmonella Typhi, Lahore, Pakistan. Sci Rep. doi:10.1038/s41598-026-37560-5
5. ChEMBL. Target CHEMBL614448, Salmonella typhi (organism). https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL614448
6. UniProtKB. P0A2I4, DNA gyrase subunit B, Salmonella Typhi, 804 aa. https://rest.uniprot.org/uniprotkb/P0A2I4
7. RCSB Protein Data Bank. 6J90, crystal structure of GyraseB N-terminal domain complex with ATP from Salmonella Typhi, 2.2 Å. https://www.rcsb.org/structure/6J90
8. PubChem. Azithromycin, CID 447043. https://pubchem.ncbi.nlm.nih.gov/compound/447043

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-051c-2026-11-12.json`; the discarded maltase-glucoamylase run is in `hidden_files/dock-HP-051-2026-11-12.json`. Bioactivities are the verbatim ChEMBL API response in `hidden_files/chembl-activities-CHEMBL614448-2026-11-12.json`. ChEMBL target CHEMBL614448, UniProt P0A2I4, PDB 6J90, PubChem CID 447043. No additional data were generated.
