# Daily Paper — Submission Pack (2026-11-05, Health)

Status: PDF ready. NOT submitted — submit click is his per standing rule.

## PDF (ready to upload)
- `2026-11-05-health-lpxh-metal-aware-reranking.pdf` (30 KB, 8 pages)

## Recommended route: ChemRxiv (Medicinal Chemistry / Chemical Biology)
Preprint first — free, citable, does not block a journal later. He already has a ChemRxiv account via ORCID sign-in (used for Papers #1/#3). **Results-first framing applied throughout** (the lesson from the ChemRxiv rejections of Papers #1 and #3: no proposed-framework framing; the paper leads with its own docking + geometry numbers and a falsifiable prediction). arXiv is not the route for this medicinal-chemistry manuscript (and would need a first-time-author endorser).

| Paper | Platform | Subject area |
|---|---|---|
| LpxH metal-aware re-ranking | ChemRxiv | Medicinal Chemistry / Chemical Biology |

## Submission details
- **Title:** Metal-aware re-ranking of sulfonyl piperazine LpxH inhibitors: docking scores alone cannot distinguish di-manganese chelators from non-chelators in *Klebsiella pneumoniae* LpxH
- **Abstract:** 1,795 characters / 248 words — fits the 2,500-char ChemRxiv limit.
- **Keywords (9):** LpxH; *Klebsiella pneumoniae*; lipid A; sulfonyl piperazine; di-manganese cluster; molecular docking; AutoDock Vina; metal chelation; antimicrobial resistance
- **Author:** Zubair Ali, Pharm-D student, SMBBMU Larkana, Pakistan · ORCID 0009-0001-5921-7509
- **Affiliation:** "SMBBMU, Larkana, Pakistan"
- **Licence:** CC BY 4.0
- **AI disclosure:** in the manuscript text (header + Acknowledgments).
- **Core claim (falsifiable):** CID 156252442 will inhibit *Kp*LpxH within 3-fold of JH-LPH-50 (7.7 nM), while CID 156252448 and CID 156252462 will be ≥10-fold weaker despite Vina scores within 1.9 kcal/mol — testable in one malachite-green enzyme assay.

## What's new in this paper (own computation)
- Full LeadForge run on *K. pneumoniae* LpxH (UniProt A6T5R0): PubChem 2D-similar analogues of JH-LPH-50 (25 CIDs, threshold 0.85), 24 scored (Lipinski/Veber/PAINS/Tox21 kNN), 8 compounds docked with Vina 1.2.7 into PDB 7SS7.
- Grid-centre audit: docking centre = co-crystallised BN8 centroid exactly (deviation 0.0 Å) — the failure mode that invalidated earlier papers.
- Re-dock validation: JH-LPH-50 RMSD 2.22 / 2.28 Å (two independent runs). An earlier 8.23 Å value was a confirmed atom-order artifact in the first analysis script and is NOT reported.
- Metal geometry (order-independent graph method, validated against the crystal: 2.49 / 2.11 Å): known nanomolar inhibitors place a hydroxamate O 1.93–2.21 Å from Mn; non-chelating analogues place no O closer than 6.5 Å. Vina alone misranks the references (JH-LPH-45 −11.37 outscores JH-LPH-50 −11.04 despite 2.3-fold lower potency).
- Two pipeline faults found and fixed during the run (disclosed in the manuscript Methods): ChEMBL fallback mis-assigned human maltase-glucoamylase (CHEMBL2074) to this bacterial target — its 55 ligands were discarded; and ChEMBL has no LpxH target at all, so the lead set comes from PubChem similarity, not ChEMBL.
- Novelty check via PubChem synonyms: top "analogue" CID 146680856 is the published JH-LPH-41 and CID 167713202 is JH-LPH-45 — both treated as references, not leads. The four prediction compounds are patent-disclosed (US20240279174) with no published enzyme data.

## His steps (only his — I cannot do these)
1. Read-through and approval of the manuscript.
2. Final submit click on ChemRxiv — he logs in, I fill the form, he presses submit (standing rule).

## Standing order
Every daily paper → PDF → submission pack → submit on the chosen route, same day, under his name.

## Direct InhA Inhibitors Dock 3.5–4.4 kcal/mol Better Than Free Isoniazid on Mycobacterium tuberculosis InhA: A Standardised Vina Benchmark at the INH–NAD Adduct Site

- **File:** `2026-11-05-health-inha-isoniazid-direct-inhibitors.md`
- **Abstract:** 1892 characters (limit 2,500)
- **Keywords (8):** InhA; isoniazid; KatG; molecular docking; AutoDock Vina; tuberculosis; drug resistance; ChEMBL
- **Subject area:** Medicinal Chemistry / Chemical Biology
- **Licence:** CC BY 4.0 · **Author:** Zubair Ali, ORCID 0009-0001-5921-7509 · **Affiliation:** SMBBMU, Larkana, Pakistan

## Five Triazolium Trypanothione Reductase Inhibitors Dock at −6.3 to −7.8 kcal/mol on Leishmania infantum TR: A Vina Benchmark, a Species Surrogate, and Two Pipeline Faults Caught

- **File:** `2026-11-05-health-trypanothione-reductase-leishmania.md`
- **Abstract:** 1952 characters (limit 2,500)
- **Keywords (8):** trypanothione reductase; cutaneous leishmaniasis; molecular docking; AutoDock Vina; Leishmania infantum; antimonials; triazolium; ChEMBL
- **Subject area:** Medicinal Chemistry / Chemical Biology
- **Licence:** CC BY 4.0 · **Author:** Zubair Ali, ORCID 0009-0001-5921-7509 · **Affiliation:** SMBBMU, Larkana, Pakistan

## Trametinib Beats Itself by 1.75 kcal/mol: A Vina Benchmark of MEK1 Inhibitors on 7B7R and the Conformer-Sampling Error Hiding Inside Every Docking Score

- **File:** `2026-11-05-health-mek1-trametinib-benchmark.md`
- **Abstract:** 1756 characters (limit 2,500)
- **Keywords (8):** MEK1; trametinib; molecular docking; AutoDock Vina; melanoma; BRAF; allosteric inhibitor; ChEMBL
- **Subject area:** Medicinal Chemistry / Chemical Biology
- **Licence:** CC BY 4.0 · **Author:** Zubair Ali, ORCID 0009-0001-5921-7509 · **Affiliation:** SMBBMU, Larkana, Pakistan

## Four Known Neprilysin Inhibitors Dock at −7.1 to −9.9 kcal/mol on the Omapatrilat Site: A Vina Benchmark, a 37.9 Å Grid Error, and the Zinc That Vina Cannot See

- **File:** `2026-11-05-health-neprilysin-sacubitrilat-benchmark.md`
- **Abstract:** 1851 characters (limit 2,500)
- **Keywords (8):** neprilysin; sacubitril; sacubitrilat; molecular docking; AutoDock Vina; heart failure; zinc metallopeptidase; ChEMBL
- **Subject area:** Medicinal Chemistry / Chemical Biology
- **Licence:** CC BY 4.0 · **Author:** Zubair Ali, ORCID 0009-0001-5921-7509 · **Affiliation:** SMBBMU, Larkana, Pakistan

## Five Sub-Nanomolar PCSK9 Expression Modulators Dock Only Weakly at the LDLR-Interface Site: A Vina Benchmark on 7S5H, Two Target-Resolution Faults, and the Binder-versus-Modulator Distinction

- **File:** `2026-11-05-health-pcsk9-evolocumab-expression-modulators.md`
- **Abstract:** 1889 characters (limit 2,500)
- **Keywords (8):** PCSK9; evolocumab; LDL cholesterol; molecular docking; AutoDock Vina; cyclic peptide; expression modulator; protein–protein interaction
- **Subject area:** Medicinal Chemistry / Chemical Biology
- **Licence:** CC BY 4.0 · **Author:** Zubair Ali, ORCID 0009-0001-5921-7509 · **Affiliation:** SMBBMU, Larkana, Pakistan
