# ChemRxiv Submission Package — LeadForge manuscript v1
Status: MANUSCRIPT APPROVED by author (2026-10-07). Awaiting lab validation before submission (author's strategy).

## How to submit (author does this — account + upload are yours)
1. Go to https://chemrxiv.org → Sign up / Log in (use za0153715@gmail.com)
2. "Submit a preprint" → upload `leadforge-manuscript-v1.pdf`
3. Fill the fields below (copy-paste ready)
4. Choose license: CC-BY (recommended for max visibility)
5. Submit. You'll get a DOI within ~1-2 days after their check.

## Copy-paste fields
- **Title:** LeadForge: An AI-Driven Computational Pipeline for Accelerated Hit Discovery and Novel Analog Design
- **Authors:** Zubair Ahmed
- **Affiliation:** Faculty of Pharmacy, SMBBMU, Larkana, Pakistan
- **Corresponding author email:** za0153715@gmail.com
- **Abstract:** (see below)
- **Keywords:** computer-aided drug design; virtual screening; molecular docking; ADMET prediction; SGLT2 inhibitors; hit-to-lead; cheminformatics
- **Subject area:** Chemical Biology / Medicinal Chemistry

## Abstract (paste into the abstract box)
Early-stage drug discovery remains slow and expensive, with the hit-to-lead transition representing a major bottleneck. We describe LeadForge, an open, automated computational pipeline that triages candidate compounds against a protein target in seven stages: (1) target identification from UniProtKB and ChEMBL, (2) bioactivity mining, (3) query verification via PubChem, (4) RDKit Morgan-fingerprint similarity screening, (5) ADMET and safety filtering (Lipinski/Veber, PAINS, and a Tox21 kNN read-across model), (6) composite lead ranking, and (7) AutoDock Vina molecular docking against experimentally determined protein structures from the RCSB Protein Data Bank. We validate the pipeline on four targets — EGFR, DPP4, SGLT2, and Escherichia coli dihydrofolate reductase (DHFR) — and in each case the pipeline independently rediscovers the reference drug from the ChEMBL bioactivity set (similarity 1.0), confirming that the workflow recovers known chemistry before proposing anything new. As a design case study, we enumerated 240 analogs of the SGLT2 lead CHEMBL5288495, filtered them through novelty (<0.85 Tanimoto vs 23 known SGLT2 actives), ADMET, and docking screens to five finalists; the best candidate docks at −8.19 kcal/mol versus an in-run dapagliflozin control at −7.23 kcal/mol. All findings are computational hypotheses: no compounds have been synthesized or tested, docking scores carry run-to-run variability, and novelty is assessed computationally only. The five SGLT2 analogs are proposed for university-laboratory synthesis and assay as the next step.

## Files
- Manuscript PDF: `leadforge-manuscript-v1.pdf` (this folder)
- Manuscript source: `leadforge-manuscript-v1.md` (this folder)

## Before submitting — final checklist
- [ ] Lab validation results are in (author's decision: submit after university-lab testing for max impact)
- [ ] If validation changes any numbers, regenerate manuscript v2 first
- [ ] Confirm affiliation wording once more at submission time
