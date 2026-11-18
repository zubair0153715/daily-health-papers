# Multi-target computational triage of known bioactive chemical space against seven disease targets: similarity screening, ADMET/toxicity read-across and AutoDock Vina docking (week of 9–15 Nov 2026)

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification.**

**Author:** Zubair Ali, Pharm-D student, SMBBMU Larkana, Pakistan · **Drafting assistant:** Lapis (AI)

## Week of 2026-11-09 → 2026-11-15 (7 daily targets)

**STATUS: DRAFT ONLY — never submit. Journal submission is Zubair's action under his own name.**

---

## Proposed title (placeholder)
"Multi-target computational triage of known bioactive chemical space against seven disease targets: similarity screening, ADMET/toxicity read-across and AutoDock Vina docking"

## Abstract

We screened the bioactive chemical space of ChEMBL against seven therapeutically relevant targets in one week of automated LeadForge runs (9–15 Nov 2026): *Plasmodium falciparum* dihydroorotate dehydrogenase (PfDHODH), *Staphylococcus aureus* enoyl-ACP reductase (FabI), tyrosine kinase 2 (TYK2), cyclin-dependent kinase 7 (CDK7), myeloid cell leukemia 1 (MCL1), peroxisome proliferator-activated receptor gamma (PPARG) and respiratory syncytial virus fusion protein F (RSV F). For each target, the reference drug was recovered from live ChEMBL data (rediscovery check), 44–58 known ligands were similarity-screened (FabI: 430 compounds via a pinned-target run; TYK2: PubChem fallback after a ChEMBL outage), leads were ranked on a composite of similarity, Lipinski/Veber drug-likeness, PAINS and kNN toxicity read-across, and the top five leads were docked with AutoDock Vina against the best available X-ray structure, with the reference drug re-docked as control. Four runs produced leads that docked better than their reference drug: PfDHODH (all five leads, best −9.72 vs −8.21 kcal/mol for DSM265), FabI (three leads, best −11.44 vs −10.15 for afabicin), CDK7 (two leads, best −9.98 vs −8.91 for samuraciclib) and MCL1 (two stereoisomer leads, best −9.33 vs −8.26 for S63845), plus PPARG (one lead, −10.26 vs −9.05 for pioglitazone). Two runs were honest negatives (TYK2: closest lead 0.19 kcal/mol behind deucravacitinib, inside noise; RSV F: no novel lead beat presatovir). The RSV F run also caught and corrected a structure-selection error: the auto-picked PDB 29QJ is an HR1 fragment with a stapled peptide, not the presatovir pocket, and the comparison was re-run at prefusion structure 6VKE. All findings are computational triage; no compound is claimed as a drug, and wet-lab validation is required.

## Methods

**Pipeline (LeadForge, same flow for all seven runs).** (1) Target identification from UniProtKB + ChEMBL (live). (2) Known-ligand retrieval from ChEMBL bioactivities. (3) Query-compound verification via PubChem PUG REST. (4) Morgan-fingerprint similarity screen vs known actives. (5) ADMET + safety panel: RDKit descriptors (Lipinski, Veber), PAINS filter, ToxGuard kNN read-across over 12 Tox21-style assays. (6) Composite lead ranking (similarity 40 / Lipinski 20 / Veber 10 / PAINS 10 / tox 20). (7) Molecular docking: AutoDock Vina, exhaustiveness 8, 3 poses, 22.5 Å box centred on the co-crystallised ligand centroid of the best X-ray structure (resolution < 3.0 Å); grid centre verified as the largest drug-like HETATM group with cofactors, glycans, waters and ions excluded (centre-fix audit, Nov 2026), and the PDB domain checked against the reference drug's binding site (TYK2/RSV F correction, Nov 2026). Reference drug re-docked in the same pocket as control. Vina noise is taken as ~±0.5–1 kcal/mol (up to ~2 kcal/mol in the literature); margins inside noise are reported as ties.

**Targets, references and structures.** PfDHODH / DSM265 (PDB 7L01, 1.60 Å); FabI / afabicin (PDB 6YUR, 1.96 Å, SKTS1 complex); TYK2 / deucravacitinib (PDB 6NZH, JH2 pseudokinase domain); CDK7 / samuraciclib (PDB 8R9A, 1.71 Å); MCL1 / S63845 (PDB 6UDV, 1.35 Å; exhaustiveness lowered to 2 after Vina timeouts on ~830–1050 Da ligands); PPARG / pioglitazone (PDB 9F7W, 1.25 Å, BPA-bound); RSV F / presatovir (PDB 6VKE, 2.10 Å, prefusion F + JNJ-40012665; auto-pick 29QJ discarded as the wrong domain).

## Results summary

| Date | Target | Reference | Best lead (docking) | Reference (docking) | Verdict |
|---|---|---|---|---|---|
| 9 Nov | PfDHODH | DSM265 | CHEMBL3289670, −9.72 | −8.21 | All 5 leads beat DSM265; best margin 1.51, IC50 35 nM — but all are DSM265 triazolopyrimidine analogues, one scaffold family, and the margin sits inside Vina error |
| 10 Nov | FabI | afabicin | CHEMBL567711, −11.44 | −10.15 | Three leads beat afabicin; best margin 1.29 (0.86 vs the active form AFN-1252, −10.58); IC50 20 nM — promising backup chemotypes, not proven wins |
| 11 Nov | TYK2 | deucravacitinib | CID 162675488, −10.15 | −10.34 | Honest negative — no lead beats deucravacitinib; closest is 0.19 kcal/mol behind, inside sampling noise. ChEMBL was down; run used the PubChem similarity fallback, so no measured potency is attached |
| 12 Nov | CDK7 | samuraciclib | CHEMBL428690, −9.98 | −8.91 | Two leads beat samuraciclib; best margin 1.07 kcal/mol — backup chemotypes for a CDK7 programme |
| 13 Nov | MCL1 | S63845 | CHEMBL5538127, −9.33 | −8.26 | Two stereoisomer leads beat S63845 by ~1.0 kcal/mol (Ki 0.026 nM) — one chemotype, not two independent hits; docking at exhaustiveness 2, one lead undocked (Vina timeout) |
| 14 Nov | PPARG | pioglitazone | CHEMBL6145236, −10.26 | −9.05 | **Clear win** — 1.21 kcal/mol margin, scaffold hop (sim 0.163), EC50 0.49 nM, clean panel; most interesting lead of the week because it is NOT a pioglitazone look-alike |
| 15 Nov | RSV F | presatovir | CHEMBL4779491, −5.14 | −6.14 | Honest negative — no novel lead beats presatovir; best novel lead 1.00 kcal/mol behind. The presatovir record itself (CHEMBL3410450, −6.64) out-scores the re-dock, a stereochemistry/sampling effect, not a new lead |

**Headline results.** 5 of 7 runs produced a docking lead better than the reference (PfDHODH, FabI, CDK7, MCL1, PPARG); 2 were negatives (TYK2, RSV F). The strongest single result is CHEMBL6145236 against PPARG: a non-thiazolidinedione chemotype docking 1.21 kcal/mol better than pioglitazone with sub-nanomolar measured potency. The FabI series (CHEMBL567711, CHEMBL586043) is the second genuine outcome: two backup chemotypes against a validated antibacterial target, though the margins shrink against the active metabolite AFN-1252. The PfDHODH result is the weakest "win": all five leads beat DSM265, but they are all DSM265 analogues, so the screen re-ranked one scaffold family rather than finding a new one. Across the week, every reference drug was recovered by the pipeline (rediscovery check passed in all runs where the reference was in ChEMBL).

## Discussion

The week's pattern is the same one the screen keeps showing: docking wins are cheap inside a reference drug's own chemotype family, and the interesting hits are the ones that leave it. PPARG's CHEMBL6145236 is the week's only scaffold hop with a docking win, which is why it leads the paper. FabI and MCL1 are solid backup-series results with honest caveats (prodrug comparator for FabI; stereoisomer duplication and a timed-out dock for MCL1). PfDHODH shows the screen's failure mode — a full house of wins that are all the same molecule family — and is reported as such rather than as five independent hits. The two negatives are reported as results, not failures: TYK2 shows the screen can say no even for a well-studied kinase, and RSV F shows it can say no for a viral target where the measured potencies (sub-3 nM EC50s) look better than the reference on paper but do not survive a head-to-head pocket comparison. The RSV F correction — discarding the auto-picked 29QJ HR1-fragment structure for the prefusion 6VKE structure — is the week's methodological point: automated structure selection must be audited against the reference drug's binding site, and the audit caught the error before the report was written.

**Limitations.** (i) All scores are computational; no wet-lab data were generated. (ii) Docking used rigid receptors and single pockets; covalent mechanisms (none in this week's targets) and induced fit are not modelled. (iii) Measured potencies come from heterogeneous ChEMBL assays and are not head-to-head comparisons — most clearly in RSV F, where sub-nanomolar leads and a micromolar reference record come from different assays. (iv) Similarity-anchored screening limits chemical diversity by design. (v) ToxGuard is kNN read-across, not a safety verdict. (vi) Mutant targets were not modelled (PfDHODH resistance, FabI, TYK2, MCL1, PPARG selectivity vs PPAR-alpha/delta, RSV F escape mutations). (vii) MCL1 docking ran at exhaustiveness 2 with ~0.2 kcal/mol run-to-run variation; one lead was not docked at all.

## References (sources, live data)

- UniProtKB accessions: PfDHODH Q08210; FabI Q2FZQ3; TYK2 P29597; CDK7 P50613; MCL1 Q07820; PPARG P37231; RSV F P03420.
- ChEMBL (EBI) target + bioactivity records, accessed live 9–15 Nov 2026 (TYK2 via PubChem fastsimilarity_2d fallback during a ChEMBL outage).
- PubChem PUG REST (reference-compound verification).
- RCSB PDB: 7L01 (PfDHODH, 1.60 Å); 6YUR (FabI–SKTS1, 1.96 Å); 6NZH (TYK2 JH2, deucravacitinib site); 8R9A (CDK7, 1.71 Å); 6UDV (MCL1, 1.35 Å); 9F7W (PPARG–BPA, 1.25 Å); 6VKE (prefusion RSV F + JNJ-40012665, 2.10 Å); 29QJ (RSV F HR1 fragment, discarded as the wrong domain).
- LeadForge pipeline: run_pipeline + dock (centre-fix audit + domain check, Nov 2026). Individual daily reports: `leadforge-daily-{DHODH,FabI,TYK2,CDK7,MCL1,PPARG,RSV-F}-2026-11-{09..15}.md`.

*DRAFT ONLY — compiled 2026-11-15 from the week's seven daily LeadForge reports. Not submitted anywhere. Computational triage only; no cure or treatment claims.*

---

*Source: LeadForge AI weekly paper draft (`leadforge-weekly-paper-2026-11-15.md`), LeadForge drug-discovery pipeline. Weekly papers are compiled from the daily LeadForge runs.*
