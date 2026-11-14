# The Weakest Measured Binder Docks Best on CDK6: A Centre-Audited Benchmark of Four ChEMBL Leads Against Palbociclib on 6OQO

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-12 · **Health Papers Agent — Paper #48** (daily 5-paper run)

**Keywords:** cyclin-dependent kinase 6; palbociclib; molecular docking; AutoDock Vina; breast cancer; CDK4/6 inhibitor; ChEMBL; structure-based screening

---

## Abstract

Breast cancer was diagnosed in 2.43 million women and killed 693,660 in 2024, and palbociclib — a CDK4/6 inhibitor that extended median progression-free survival in the PALOMA-2 trial — is limited by neutropenia and by resistance, so a better CDK6 binder would matter. The gap this paper attacks is whether a standardised docking screen can rank CDK6 ligands at all when the reference drug itself is the benchmark. We ran the LeadForge pipeline (UniProtKB Q00534 → ChEMBL target CHEMBL2508, 25 bioactivities → PubChem → RDKit ADMET/PAINS → AutoDock Vina 1.2.7) and docked four ChEMBL CDK6 actives plus palbociclib into the 1.98 Å CDK6 structure 6OQO, with the grid centre audited to 0.005 Å from the co-crystallised inhibitor CPD24. One lead out-scored palbociclib — CHEMBL3237704 −11.18 versus palbociclib −10.19 kcal/mol — but the margin (0.99 kcal/mol) sits inside Vina's ±1–2 kcal/mol noise, and the ranking does not track measured potency: the most potent measured binder (CHEMBL5280928, Ki 0.2 nM) ranks third by Vina while the weakest (CHEMBL3237704, IC50 1.1 nM) ranks first, Spearman ρ = −0.32 (n = 4, p = 0.68). Palbociclib itself docked reproducibly across four independent runs (−10.20 to −10.09 kcal/mol, range 0.11). The falsifiable next step is a CDK6 kinase inhibition assay of the four leads against palbociclib with a CDK4 counter-screen: if the measured order matches the ChEMBL record rather than the Vina order, docking alone must not be used to prioritise CDK6 leads on this structure.

---

## 1. Introduction

Breast cancer is the most commonly diagnosed cancer in women worldwide: GLOBOCAN 2024 recorded 2,434,087 new cases and 693,660 deaths in 2024. In Pakistan, 30,700 new cases were recorded in 2022, and more recent estimates put the annual figure near 44,000. Hormone-receptor-positive, HER2-negative (HR+/HER2−) disease is the largest subtype, and CDK4/6 inhibitors transformed its treatment: in the PALOMA-2 trial (N = 666), palbociclib plus letrozole extended median progression-free survival versus letrozole alone (hazard ratio 0.58, 95% CI 0.46–0.72), but neutropenia affected 80% of patients (grade ≥3 in 66%, febrile neutropenia 1.8%), and resistance eventually emerges. A CDK6 binder that beats palbociclib — or matches it with a cleaner profile — would be clinically valuable, and a standardised docking screen is the cheapest way to look for one. The falsifiable hypothesis of this paper is: **a standardised Vina screen on the CDK6 structure 6OQO ranks ChEMBL CDK6 actives in the same order as their measured potencies, with palbociclib as the reference.**

## 2. Methods

### 2.1 Literature basis

The burden figures are from GLOBOCAN 2024 (WHO) and the Pakistan figures from Dawn (2022, 30,700 cases) and Shaukat Khanum Memorial Cancer Hospital citing WHO (October 2026, ~44,000 cases/year). The PALOMA-2 efficacy and toxicity figures are from Finn et al., New England Journal of Medicine 2016;375(20):1925–1936. Today's literature digest (research-team digest 2026-11-12, 840 candidates screened, 8 selected) contained no paper topical to this benchmark and is cited only as a methodological source. All database identifiers were verified live on 2026-11-12.

### 2.2 Molecular docking

Standardised AutoDock Vina 1.2.7 protocol, exactly as Papers #1 and #3: UniProtKB Q00534 (CDK6, 326 aa, Homo sapiens) → ChEMBL target CHEMBL2508 ("Cyclin-dependent kinase 6", SINGLE PROTEIN) → 25 bioactivities (top 25 by pChEMBL of 1,038) → PubChem verification of palbociclib (CID 5330286) → RDKit similarity/ADMET/PAINS → Vina docking of the top 5 leads (the reference query plus four ChEMBL leads) into PDB 6OQO (CDK6 kinase domain, chain A, 1.98 Å, co-crystallised inhibitor CPD24, PDB component N1J, 34 atoms). Grid centre [22.80, 37.61, −9.50] was audited against the N1J centroid computed independently from the PDB file (agreement 0.005 Å; waters excluded by the pipeline's ligand-centre routine). Box 22.5 Å, exhaustiveness 8, best of three poses reported for every molecule, same protocol for reference and leads.

**Correction history (disclosed, not hidden).** The first docking run for this topic was invalid and is discarded: the pipeline's UniProt text search for "Cyclin-dependent kinase 6" returned P24941, which is CDK2, not CDK6 (verified live against rest.uniprot.org: P24941 = cyclin-dependent kinase 2; Q00534 = cyclin-dependent kinase 6). That run resolved ChEMBL CHEMBL301 (CDK2) and docked on 6Q4G, a CDK2 structure; its numbers are kept in `dock-HP-034-2026-11-12.json` for audit and are not used anywhere in this paper. The corrected run targets UniProt accession Q00534 directly and monkey-patches the ChEMBL target to CHEMBL2508, verified live on the ChEMBL website (target report card, 2026-11-12), because the ChEMBL target-by-accession API endpoint returned HTTP 500 pages and timeouts throughout 2026-11-12. The bioactivities are the verbatim ChEMBL API response for CHEMBL2508 saved to `hidden_files/chembl-activities-CHEMBL2508-2026-11-12.json` (top 25 by pChEMBL of 1,038; same endpoint and query the pipeline uses), because the live activity endpoint timed out on limit=50 queries and intermittently returned HTML error pages on limit=10 queries all day; only the record transport differs, not the data. Of the 25 records, 21 distinct molecules remained after SMILES deduplication, giving 22 leads including the palbociclib query.

### 2.3 PAINS screen

RDKit PAINS filter applied to every docked molecule. All five docked molecules are PAINS-clean. The sixth-ranked lead, CHEMBL3698657 (IC50 0.41 nM), was not docked (only the top 5 are docked) and carries a PAINS alert; it is reported here so the alert is not hidden, and it would need redox controls in any assay.

### 2.4 Honesty limits

Docking is not activity: Vina scores carry ±1–2 kcal/mol noise, a single rigid structure (6OQO) cannot capture induced fit, and no experimental data, molecular dynamics, or free-energy refinement were run. A docking "win" smaller than ~1 kcal/mol is not a superiority claim. No clinical recommendation follows from this paper.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Measured potency (ChEMBL) | Best affinity (kcal/mol) | Poses (kcal/mol) | PAINS |
|---|---|---|---|---|
| CHEMBL3237704 | IC50 1.1 nM (pChEMBL 8.96) | **−11.18** | −11.18, −9.94, −9.51 | clean |
| CHEMBL5751717 | IC50 0.2 nM (pChEMBL 9.70) | −10.24 | −10.24, −10.17, −10.16 | clean |
| **Palbociclib (query)** | reference drug | −10.19 | −10.19, −10.07, −9.83 | clean |
| CHEMBL5280928 | Ki 0.2 nM (pChEMBL 9.70) | −9.98 | −9.98, −9.60, −9.46 | clean |
| CHEMBL5892046 | IC50 0.6 nM (pChEMBL 9.22) | −9.78 | −9.78, −9.61, −9.11 | clean |

All five molecules docked successfully on 6OQO. One lead out-scores palbociclib: CHEMBL3237704 at −11.18 kcal/mol, 0.99 kcal/mol better than palbociclib's −10.19. That margin sits inside Vina's ±1–2 kcal/mol noise and is not a superiority claim. The remaining three leads dock worse than palbociclib by 0.05–0.41 kcal/mol — also inside noise, so no lead can be called worse than palbociclib either.

Palbociclib's own docking is highly reproducible: four independent CDK6 runs on 6OQO returned −10.20, −10.13, −10.09 and −10.19 kcal/mol (range 0.11, mean −10.15). The reference is stable; the screen's noise is in the ranking, not the reference.

### 3.2 Comparison with published docking

No published Vina benchmark of these four ChEMBL leads on 6OQO was found in the literature sweep, so there is no published docking comparison to make. The palbociclib value (−10.19 kcal/mol) is a new reference point for this structure under this protocol.

### 3.3 The ranking does not track measured potency

The docking order is mildly inverted against measured potency. The most potent measured binders — CHEMBL5280928 (Ki 0.2 nM) and CHEMBL5751717 (IC50 0.2 nM), both pChEMBL 9.70 — rank third and second by Vina, while the weakest measured lead, CHEMBL3237704 (IC50 1.1 nM, pChEMBL 8.96), ranks first. Spearman ρ = −0.32 (n = 4, p = 0.68): no significant rank agreement. In plain terms, on this structure, Vina cannot tell a 0.2 nM CDK6 binder from a 1.1 nM one — the potency spread among the four leads is only 5.5-fold, far narrower than Vina's resolving power.

ADMET is unremarkable across the docked set: molecular weights 447–553, logP 2.25–4.67, zero Lipinski violations except CHEMBL5892046 (1 violation, MW 552.63). ToxGuard Tox21 read-across flags (NR-Aromatase, SR-ARE, SR-ATAD5 and others) appear on every molecule including palbociclib itself; these are similarity-screen flags, not toxicity findings, and are reported as such.

## 4. Discussion

### 4.1 The reframe

The question this paper set out to answer — can a standardised screen find a better CDK6 binder than palbociclib? — has a two-part answer. Technically yes, one lead out-scores the reference; scientifically no, because the margin is inside noise and the ranking contradicts the measured potencies. The honest reframe is that a single-structure Vina screen on 6OQO is a triage tool for CDK6, not a ranking tool: it can confirm that a molecule fits the ATP pocket (all five did, with consistent poses), but it cannot order sub-nanomolar binders by potency.

### 4.2 Why the "win" must not be over-read

Three reasons. First, 0.99 kcal/mol is inside Vina's ±1–2 kcal/mol noise — a re-dock could erase it. Second, CHEMBL3237704's pose spread (−11.18, −9.94, −9.51) is the widest in the set, so its best pose is less consistent than CHEMBL5751717's (−10.24, −10.17, −10.16). Third, CHEMBL3237704 is the weakest measured binder of the four: if Vina were ranking by true affinity, the 0.2 nM compounds should lead. The screen's top hit is its least potent measured lead.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

No docked molecule carries a PAINS alert, so no redox-control redesign is needed for these four. The undocked sixth lead (CHEMBL3698657, IC50 0.41 nM) does carry a PAINS alert; if it is ever assayed, it needs detergent and redox controls (e.g. DTT/catalase) to expose aggregation or redox-cycling artefacts.

### 4.4 Testable hypotheses

1. **CHEMBL3237704 is not a better CDK6 inhibitor than palbociclib.** A CDK6 kinase inhibition assay (ADP-Glo or equivalent) will measure its IC50 within 2-fold of palbociclib's, not better — refuting the docking "win".
2. **The Vina order is noise.** A CDK6 assay of all four leads will reproduce the ChEMBL potency order (0.2 nM compounds first), not the Vina order — if it reproduces the Vina order instead, the screen gains credibility it does not currently deserve.
3. **Selectivity is the real differentiator.** A CDK4 counter-screen will show whether any lead is CDK6-selective; a CDK6-selective lead with equal potency would matter more than a 1 kcal/mol docking margin, because CDK4 inhibition drives part of palbociclib's neutropenia.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): CDK6 kinase inhibition assay (commercial CDK6/cyclin D1, ADP-Glo readout) for the four leads plus palbociclib, 10-point dose–response in triplicate, with staurosporine as a control. Stage 2 (weeks 4–6): CDK4/cyclin D1 counter-screen for selectivity. Stage 3 (weeks 7–12): cellular anti-proliferation assay (MCF-7, ER+ breast cancer) for any lead that beats palbociclib in Stage 1, with a palbociclib comparator and a CDK6-knockdown control to confirm on-target effect.

## 5. Limitations

1. Docking only: no experimental data, no molecular dynamics, no free-energy refinement.
2. Vina noise (±1–2 kcal/mol) exceeds every margin reported here; the 0.99 kcal/mol "win" is not significant.
3. Single rigid structure (6OQO, 1.98 Å); induced fit and the cyclin-bound conformation are not modelled.
4. The four leads span only a 5.5-fold potency range (0.2–1.1 nM), too narrow for a rank-correlation test to be powerful (n = 4, p = 0.68).
5. The ChEMBL bioactivities were fetched via a saved verbatim API response because the live endpoint was unstable all day (see Methods 2.2); the data are real ChEMBL records, but the fetch was not the pipeline's live call.
6. No CDK4 selectivity data were computed; selectivity is the clinically relevant question and remains untested.
7. Literature limits: the Pakistan case figure (~44,000/year) is a hospital-cited estimate, not a registry count.

## 6. Conclusion

On the CDK6 structure 6OQO, one ChEMBL lead (CHEMBL3237704) out-scores palbociclib by 0.99 kcal/mol — inside Vina's noise — while the docking order fails to track measured potency (Spearman ρ = −0.32, n = 4), with the weakest measured binder docking best. Palbociclib's own score is highly reproducible (−10.20 to −10.09 kcal/mol across four runs). The screen confirms these molecules fit the CDK6 ATP pocket; it does not rank them. The next step is a CDK6 kinase assay with a CDK4 counter-screen, not more docking.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content.

## References

1. World Health Organization. Global Cancer Observatory (GLOBOCAN) 2024: breast cancer incidence 2,434,087 cases and 693,660 deaths, 2024. https://gco.iarc.who.int
2. Dawn. Breast cancer in Pakistan: 30,700 new cases in 2022. https://www.dawn.com (2022 figures, as cited in the literature sweep 2026-11-12).
3. Shaukat Khanum Memorial Cancer Hospital and Research Centre, citing WHO. Pakistan breast cancer burden, ~44,000 new cases per year, October 2026.
4. Finn RS, Martin M, Rugo HS, et al. Palbociclib and letrozole in advanced breast cancer. N Engl J Med. 2016;375(20):1925–1936. doi:10.1056/NEJMoa1607303. PMID 27959613
5. ChEMBL. Target CHEMBL2508, Cyclin-dependent kinase 6. https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2508
6. UniProtKB. Q00534, Cyclin-dependent kinase 6, Homo sapiens, 326 aa. https://rest.uniprot.org/uniprotkb/Q00534
7. RCSB Protein Data Bank. 6OQO, CDK6 in complex with CPD24, 1.98 Å. https://www.rcsb.org/structure/6OQO
8. PubChem. Palbociclib, CID 5330286. https://pubchem.ncbi.nlm.nih.gov/compound/5330286

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-034c-2026-11-12.json`; the discarded CDK2 run is in `hidden_files/dock-HP-034-2026-11-12.json`. Bioactivities are the verbatim ChEMBL API response in `hidden_files/chembl-activities-CHEMBL2508-2026-11-12.json`. ChEMBL target CHEMBL2508, UniProt Q00534, PDB 6OQO, PubChem CID 5330286. No additional data were generated.
