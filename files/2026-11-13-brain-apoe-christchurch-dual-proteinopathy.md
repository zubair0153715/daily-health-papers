# One variant, two proteinopathies: APOE Christchurch (R136S) as a heparan-sulfate-gated brake on tau and α-synuclein seeding — a structural hypothesis and a testable therapeutic programme

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent verification.**

**Author:** Zubair Ali, Pharm-D student, SMBBMU Larkana, Pakistan · ORCID: 0009-0001-5921-7509
**Drafting assistant:** Lapis (AI)
**Date:** 13 November 2026 · **Field:** Brain (neuroscience) · **Paper:** Brain #5

---

## Abstract

**Background.** APOE is the strongest genetic risk factor for late-onset Alzheimer's disease, and a rare variant — APOE3 Christchurch (APOE3ch, R136S) — protected a PSEN1 E280A carrier from dementia for roughly 28 years despite extensive amyloid deposition. Until November 2026 the protection was understood as a tau story: R136S weakens apolipoprotein E (ApoE) binding to heparan sulfate proteoglycans (HSPGs), limiting tau spread. **New evidence.** Soto-Faguás and colleagues (Cell Reports, 11 November 2026) now report that the Christchurch mutation engineered into mouse ApoE also prevents the accumulation of α-synuclein — the protein of Parkinson's disease and Lewy body dementia — in predisposed mice, with the senior author describing it as acting "like a super-APOE-2". **Hypothesis.** We propose a single shared mechanism: tau and α-synuclein seeds both enter neurons through the same HSPG gateway, and R136S closes that gateway for both. We test the structural premise on the real human sequence (UniProt P02649): residues 136–150 form a cationic cluster (Arg136, Arg142, Lys143, Arg145, Lys146, Arg147, Arg150) carrying a net charge of +7; R136S removes one positive charge (+7 → +6) and shifts the N-terminal domain net charge to −4 — the same value as protective APOE2, versus −2 for risk-conferring APOE4. **Falsifiable claim.** If the shared-gateway model is correct, recombinant ApoE3ch will reduce α-synuclein preformed-fibril uptake into primary neurons by a comparable fraction to its reduction of tau uptake, and any Christchurch-mimetic that occupies the ApoE HSPG-binding pocket will inhibit α-synuclein seeding as well as tau seeding. We specify the experiments, effect-size expectations, and the observations that would falsify the model. **Conclusion.** One rare variant may define one druggable gateway for two diseases — and, because women with Parkinson's disease dementia carry a substantially higher amyloid co-pathology burden, the benefit of closing that gateway should be tested with sex-stratified analysis.

## Keywords

APOE Christchurch; R136S; heparan sulfate proteoglycan; tau propagation; alpha-synuclein; Parkinson's disease; Alzheimer's disease; prion-like seeding

---

## 1. Introduction

Alzheimer's disease and Parkinson's disease are clinically distinct and pathologically overlapping. Alzheimer's is defined by amyloid-β (Aβ) plaques and tau tangles; Parkinson's by α-synuclein Lewy pathology. Yet mixed pathology is the rule, not the exception: most brains with Lewy pathology also carry amyloid, and most Alzheimer's brains carry some Lewy pathology. Treatments aimed at one protein have repeatedly left the other untouched. A therapy that acted on a mechanism shared by both seeds would therefore be worth far more than a therapy aimed at either protein alone.

APOE is the natural place to look for such a mechanism. The APOE ε4 allele is the strongest genetic risk factor for late-onset Alzheimer's disease, and ApoE is increasingly implicated in Parkinson's disease and Lewy body dementia as well. The decisive clue came from a single patient: a Colombian woman carrying the fully penetrant PSEN1 E280A mutation for early-onset Alzheimer's disease, who remained cognitively intact into her seventies because she was homozygous for a rare APOE variant, APOE3 Christchurch (R136S) (Arboleda-Velasquez et al., 2019). Her brain carried extremely high Aβ pathology but minimal tau burden, minimal hippocampal atrophy and minimal neuroinflammation (Nelson et al., 2023). A single amino-acid change — arginine to serine at position 136 — had apparently uncoupled amyloid from tau.

Two mechanistic studies then pinned down the tau arm. Nelson et al. (2023) engineered R136S into the APOE4 background in knock-in mice and in human induced pluripotent stem cells from an APOE4-homozygous Alzheimer's patient, and showed protection against APOE4-driven tau pathology, neurodegeneration and neuroinflammation; a major functional effect of R136S is disruption of ApoE binding to anionic HSPGs on the cell surface. Chen et al. (2025) showed that ApoE3 R136S binds tau more strongly than wild-type ApoE3, reduces tau uptake into neurons and microglia, suppresses asparagine endopeptidase (AEP) activation and tau N368 fragmentation, and attenuates tau preformed-fibril (PFF) spreading in both 5xFAD and Tau P301S mice, with improved cognition. The tau story was, by 2025, mechanistically coherent: R136S weakens the ApoE–HSPG interaction, and HSPGs are essential co-factors for cellular uptake of tau seeds (Holmes et al., 2013).

What was missing was the second proteinopathy. On 11 November 2026, Soto-Faguás and colleagues reported in Cell Reports that the Christchurch mutation, engineered into mouse ApoE, protects against Aβ-induced tau aggregation — and, for the first time, against α-synuclein aggregation in mice predisposed to accumulate it (Soto-Faguás et al., 2026). Senior author Vivek Unni (Oregon Health & Science University) described the variant as acting "like a super-APOE-2", and raised gene therapy based on the Christchurch mutation as a route to forestall cognitive and motor impairment in Parkinson's disease and related conditions. The result is striking, but the mechanism for the α-synuclein arm is untested: reduced accumulation in vivo does not by itself show reduced seed uptake.

This paper makes the missing connection explicit and testable. We synthesise the tau and α-synuclein uptake literatures, add an original sequence-level analysis of the human ApoE HSPG-binding cluster, and derive a falsifiable shared-gateway model with a concrete experimental programme — including a prediction about who should benefit most, grounded in a second November 2026 finding: women with Parkinson's disease dementia carry a substantially higher burden of Alzheimer's amyloid co-pathology than men (Dunckley et al., 2026).

## 2. Methods

### 2.1 Literature sweep

We swept the daily research digest for 13 November 2026 (PubMed E-utilities entry-date window, arXiv q-bio, bioRxiv, 627 candidates screened) and ran targeted PubMed searches for APOE Christchurch, HSPG-mediated seed uptake, and α-synuclein internalisation. Every citation in this paper was verified against PubMed (PMID) or the publisher's DOI on 13 November 2026; no citation is invented. One cited item is a preprint (Research Square) and is labelled as such. Quantitative figures attributed to Dunckley et al. (2026) are taken from the Mayo Clinic news release of 6 November 2026 reporting that study, as the underlying article's full text was not yet accessible at the time of writing.

### 2.2 Sequence and charge analysis (original computation)

The human ApoE sequence was retrieved live from UniProt (accession P02649, 317-amino-acid precursor) on 13 November 2026. The mature protein (residues 19–317 of the precursor, 299 amino acids) was used, with literature numbering throughout (mature-protein numbering, so that R136S, C112R and R158C refer to the positions used in the cited papers). Net charge was computed with the rule: lysine and arginine +1, aspartate and glutamate −1, histidine 0 at neutral pH. We computed, for APOE2, APOE3, APOE4 and APOE3ch (R136S): (i) the sequence and net charge of the receptor-binding / HSPG-binding region, residues 136–150; (ii) the net charge of the wider 130–150 window; (iii) the net charge of the N-terminal domain (residues 1–191); and (iv) the net charge of the full mature protein. The script and its output are archived with this paper's working files. No structural modelling was performed: this is a sequence-level analysis, and its limits are stated in Section 6.

### 2.3 Hypothesis construction

The hypothesis was built by requiring that each of its three legs be independently established in the peer-reviewed literature before the synthesis was drawn: (a) R136S weakens ApoE–HSPG binding; (b) tau seed uptake is HSPG-dependent; (c) α-synuclein fibril uptake is HSPG-dependent. The synthesis — that R136S therefore gates both seeds — is the new claim, and Section 5 states how to test it and what would falsify it.

## 3. Results

### 3.1 The three legs are each established

**Leg A — R136S weakens ApoE–HSPG binding.** The receptor-binding region of ApoE (residues 136–150) is enriched in positively charged amino acids and binds negatively charged cell-surface receptors including HSPGs (Nelson et al., 2023). The R136S substitution disrupts that binding, and ApoE also recognises the Alzheimer's-associated 3-O-sulfation of heparan sulfate; knocking out the 3-O-sulfotransferase HS3ST1 reduces ApoE cell-surface binding and uptake (Mah et al., 2023).

**Leg B — tau seed uptake is HSPG-dependent.** Holmes et al. (2013) showed that HSPGs mediate the internalisation and propagation of specific proteopathic seeds, including tau. Chen et al. (2025) showed the functional consequence for the Christchurch variant: ApoE3 R136S binds tau more strongly than wild-type, reduces its uptake into neurons and microglia via the receptor LRP1, and attenuates tau PFF spreading in vivo.

**Leg C — α-synuclein fibril uptake is HSPG-dependent.** Ihse et al. (2017) showed that internalisation of α-synuclein amyloid fibrils in neuroblastoma cells depends on heparan sulfate, as does uptake in an oligodendrocyte-like line, while soluble non-amyloid oligomers do not depend on it and astrocyte- and microglia-like lines use other routes; soluble heparin (20 µg/ml) competitively reduced uptake. Zhang et al. (2020) identified the pathway genetically: a CRISPR screen found SLC35B2, a regulator of HSPG biosynthesis, and myosin-7B (MYO7B) to be critical for α-synuclein PFF entry, with fibrils binding HSPGs through clustered K-T-K motifs and entering by clathrin-mediated endocytosis. Vanderperre et al. (2025) confirmed the axis with new regulators: deletion of SLC39A9 or C3orf58 impaired α-synuclein PFF binding and uptake, and C3orf58-knockout human iPSC-derived dopaminergic neurons and microglia showed a strong reduction in PFF internalisation.

**The new result.** Soto-Faguás et al. (2026) close the loop in vivo: mice predisposed to accumulate tau or α-synuclein did not accumulate either protein when the Christchurch mutation was present in ApoE. The α-synuclein arm had no established mechanism; legs A–C supply one.

### 3.2 Original analysis: R136S removes exactly one positive charge from the HSPG-binding cluster

Table 1 gives the sequence-level result. The 136–150 cluster of APOE3 reads RLASHLRKLRKRLLR: seven basic residues (Arg136, Arg142, Lys143, Arg145, Lys146, Arg147, Arg150) and a net charge of +7 — the cationic surface that grips anionic heparan sulfate. R136S changes the first residue to serine (SLASHLRKLRKRLLR), leaving six basic residues and a net charge of +6. The wider 130–150 window falls from +6 to +5. Notably, APOE4 and APOE2 carry a 136–150 window identical to APOE3 (+7): their isoform-defining substitutions sit elsewhere (C112R for APOE4, R158C for APOE2), so the Christchurch change is the only one of the four that alters the HSPG-binding cluster itself.

| Variant | Residues 136–150 | Basic residues | Net charge 136–150 | Net charge 130–150 | N-terminal domain (1–191) | Full mature protein |
|---|---|---|---|---|---|---|
| APOE3 | RLASHLRKLRKRLLR | 7 | +7 | +6 | −3 | −5 |
| APOE3ch (R136S) | SLASHLRKLRKRLLR | 6 | +6 | +5 | −4 | −6 |
| APOE4 | RLASHLRKLRKRLLR | 7 | +7 | +6 | −2 | −4 |
| APOE2 | RLASHLRKLRKRLLR | 7 | +7 | +6 | −4 | −6 |

A second pattern emerges from the same computation and is reported here as an observation, not a proof: the two protective variants converge on the same N-terminal-domain net charge (−4 for both APOE3ch and APOE2), while neutral APOE3 is −3 and risk-conferring APOE4 is −2. Charge alone cannot explain protection — APOE2 reaches −4 through R158C, outside the HSPG-binding motif, while APOE3ch reaches it through R136S, inside the motif — so position, not just charge, matters. But the convergence is consistent with a model in which reduced electrostatic engagement with anionic surfaces is part of the protective phenotype, and it yields a quantitative prediction: a Christchurch-mimetic need only remove or mask roughly one positive charge-equivalent from the 136–150 cluster to reproduce the variant's electrostatic profile.

### 3.3 Who carries the most mixed pathology: the sex difference

Dunckley et al. (2026) examined brain tissue from 230 people with Parkinson's disease (74 women, 156 men) in the Arizona Study of Aging and Neurodegenerative Disorders and Brain and Body Donation Program. Women had a higher mean amyloid plaque score than men (6.5 versus 4.9 out of 15); 56.8% of women versus 39.7% of men had an elevated amyloid plaque burden; and after accounting for age at death, APOE ε4 status and Lewy body levels, women had more than twice the odds of elevated amyloid burden. There was no significant sex difference in tau buildup, and the sexes had similar rates of clinically diagnosed dementia. The implication for a dual-proteinopathy therapy is direct: the population with the heaviest mixed amyloid-plus-Lewy burden — women with Parkinson's disease dementia — is the population in which a therapy that gates both seeds should show the largest absolute benefit, and in which it should therefore be tested first and analysed separately.

### 3.4 A Christchurch-mimetic already exists on paper

A structure-guided docking study (Research Square preprint) targeted the ApoE HSPG-binding pocket with benzene-1,3-disulfonic acid, a small anionic molecule resembling sulfated glycosaminoglycans, reporting a top docking score of −5.93 kcal/mol and an estimated inhibition constant (Ki) of 44.6 µM. The authors propose it as a candidate Christchurch mimetic. It is a preprint, not peer-reviewed, and its pharmacokinetics preclude systemic use as reported — but it demonstrates that the pocket is druggable in silico, and it gives the shared-gateway model an immediate, concrete test compound.

## 4. Discussion

**The shared-gateway model.** The three legs and the new in-vivo result fit one mechanism. Tau and α-synuclein are different proteins with different sequences, but as amyloid fibrils they present the same kind of surface to the cell: clustered positive charges (K-T-K motifs in α-synuclein PFFs) that bind the negatively charged sulfate groups of HSPGs. ApoE sits at that gateway twice over: it binds HSPGs through its 136–150 cationic cluster, and (for tau at least) it binds the seed itself. R136S weakens the ApoE–HSPG interaction and, per Chen et al. (2025), strengthens ApoE–tau binding while reducing seed uptake — ApoE3ch appears to sequester tau away from the uptake machinery rather than escorting it in. If the same holds for α-synuclein, one substitution gates two seeds. That is the falsifiable claim of this paper.

**Why the α-synuclein arm is not yet proven.** Soto-Faguás et al. (2026) show reduced α-synuclein accumulation in vivo. Accumulation is the net result of production, uptake, templating and clearance; the experiment does not isolate uptake. It is possible that the α-synuclein protection works through a different route — for example, altered microglial handling, since ApoE3ch also reduces microglial activation (Chen et al., 2025), or reduced AEP activation, which cleaves both APP and tau. The shared-gateway model predicts a specific, separable effect — reduced neuronal uptake of α-synuclein PFFs — that can be tested without any new mouse line.

**Cell-type limits.** Ihse et al. (2017) found that astrocyte- and microglia-like cells internalise α-synuclein fibrils by means other than heparan sulfate. The model therefore predicts neuronal and oligodendroglial protection primarily, not a blanket block of all fibril uptake. That is a feature, not a flaw: microglial clearance of seeds is desirable, and a therapy that spares it while blocking neuronal uptake would be preferable to one that blocks both. Any mimetic should be screened for this selectivity.

**Therapeutic routes.** Three routes follow from the model, in order of tractability: (i) small-molecule Christchurch mimetics that occupy the ApoE HSPG-binding pocket, exemplified by the benzene-1,3-disulfonic acid scaffold (−5.93 kcal/mol; Ki 44.6 µM, preprint) — intranasal delivery or ligand optimisation would be needed for brain exposure; (ii) ApoE-derived peptides spanning residues 130–150 carrying the R136S substitution, as competitive inhibitors of seed uptake; (iii) APOE Christchurch gene therapy, already envisaged by the OHSU group and conceptually supported by APOE2 gene-therapy programmes in development — the longest and most expensive route, and the one requiring the most caution given that APOE is a lipid-transport protein with systemic roles. The charge analysis in Table 1 gives medicinal chemistry a quantitative target: reproduce the +7 → +6 shift in the 136–150 cluster, or the equivalent masking of one positive charge.

**Sex-stratified testing.** The Dunckley et al. (2026) finding reframes trial design. If a therapy gates both amyloid-driven tau seeding and α-synuclein seeding, its measurable benefit should scale with the burden of mixed pathology. Women with Parkinson's disease dementia carry more amyloid co-pathology (plaque score 6.5 vs 4.9; 56.8% vs 39.7% elevated burden; odds ratio > 2) at similar dementia rates — so a sex-stratified analysis is not a subgroup fishing expedition here; it is a pre-specified prediction of the model. The same logic applies to APOE ε4 carriers, in whom amyloid and tau co-pathology is heavier.

**What would change our mind.** The model stands or falls on the uptake experiments in Section 5. A negative result on prediction P1 would not invalidate the 2026 in-vivo finding, but it would force the mechanism elsewhere (clearance, AEP, or microglial handling) and would remove the rationale for HSPG-pocket mimetics against synucleinopathy specifically.

## 5. Falsifiable claim and how to test it

**Claim.** APOE Christchurch (R136S) protects against both tau and α-synuclein aggregation by one shared mechanism: weakening ApoE binding to HSPGs at the 136–150 cationic cluster, thereby reducing HSPG-dependent neuronal uptake of both proteopathic seeds. Consequently, any Christchurch-mimetic that disrupts the ApoE–HSPG interface will inhibit α-synuclein seeding as well as tau seeding.

**Prediction P1 (uptake).** In primary mouse or human iPSC-derived neurons, recombinant ApoE3ch will reduce uptake of fluorescently labelled α-synuclein PFFs by a comparable fraction to its reduction of tau PFF uptake, measured in matched assays (same cells, same fibril dose, same readout, e.g. pHrodo labelling with flow cytometry after 8–24 h, as in Ihse et al., 2017). Expected direction: reduction of at least 30% relative to wild-type ApoE3, mirroring the tau effect reported by Chen et al. (2025). **Falsifier:** ApoE3ch reduces tau PFF uptake but leaves α-synuclein PFF uptake unchanged (±10%) in the matched assay.

**Prediction P2 (mimetic).** Benzene-1,3-disulfonic acid, or an optimised analogue, will inhibit α-synuclein PFF uptake into neurons dose-dependently, with an inhibitory potency in the same order of magnitude as its inhibition of tau seeding (reported Ki 44.6 µM for the ApoE pocket; preprint). **Falsifier:** the compound blocks tau seeding but has no effect on α-synuclein PFF uptake at concentrations up to 10× its tau-seeding IC50.

**Prediction P3 (in vivo, sex-stratified).** In a mouse model of mixed pathology (e.g. 5xFAD crossed with an α-synuclein transgenic line) carrying the Christchurch-equivalent Apoe mutation, the reduction in α-synuclein pathology will be larger in females, tracking their higher amyloid burden; and in any future human study of an ApoE–HSPG disruptor, the absolute benefit on mixed-pathology endpoints will be larger in women with Parkinson's disease dementia than in men. **Falsifier:** no sex difference in the mouse cross, or a benefit confined to males.

**Controls required.** (i) Wild-type ApoE3 and ApoE4 arms in every uptake assay; (ii) an HSPG-deficient control (heparinase treatment or SLC35B2 knockdown) to confirm the uptake being measured is HSPG-dependent; (iii) a non-fibrillar α-synuclein oligomer arm, which Ihse et al. (2017) showed is not HSPG-dependent — the model predicts no ApoE3ch effect there, a useful negative control; (iv) microglial uptake measured in parallel, where the model predicts little or no effect.

## 6. Limitations

1. **The α-synuclein mechanism is inferred, not shown.** The 2026 Cell Reports result is in mice, with the mutation engineered into mouse Apoe; human translation is unproven, and the in-vivo experiment does not isolate uptake from clearance or production.
2. **Sequence charge is a proxy.** The +7 → +6 computation describes electrostatics, not binding free energy. Real ApoE–HSPG affinity depends on conformation, lipidation, 3-O-sulfation patterns (Mah et al., 2023), and the oligomeric state of ApoE. No docking or molecular dynamics was performed here.
3. **One preprint is cited.** The benzene-1,3-disulfonic acid result (Research Square) is not peer-reviewed; its −5.93 kcal/mol score and 44.6 µM Ki are the authors' figures and have not been independently reproduced.
4. **Sex-difference figures come from a news release.** The Dunckley et al. (2026) numbers (plaque scores, percentages, odds ratio) are taken from the Mayo Clinic release of 6 November 2026; the underlying article's full text was not accessible when this draft was written.
5. **Cell-type scope.** The shared-gateway model applies to neuronal and oligodendroglial uptake; astrocytes and microglia use additional routes (Ihse et al., 2017), so the model does not predict a universal block of fibril uptake.
6. **APOE biology is pleiotropic.** ApoE is a lipid-transport protein; disrupting its receptor interactions systemically could have off-target metabolic effects. Any mimetic or gene therapy must demonstrate that it spares ApoE's lipid-transport function.
7. **This is an AI-assisted draft.** No experiment in Section 5 has been performed by the author; the paper is a hypothesis and a programme, not a report of results.

## 7. Conclusion

A single amino-acid change, R136S, protected one woman from a deterministic Alzheimer's mutation for roughly 28 years. Two years of mechanistic work explained the tau arm. The November 2026 extension to α-synuclein suggests the protection was never tau-specific: it was gateway-specific. Tau and α-synuclein seeds enter neurons through the same heparan sulfate gateway, and the Christchurch variant closes it for both — removing one positive charge from a seven-charge cluster, shifting the N-terminal domain to the same net charge as protective APOE2. That makes the ApoE–HSPG interface a single druggable target for two diseases, with a concrete test compound already docked in silico and a concrete experiment — matched tau versus α-synuclein uptake assays — that can falsify the idea within months. The first patients to test it in should include the people who carry the heaviest mixed pathology: women with Parkinson's disease dementia.

---

## References

1. Soto-Faguás CM, et al. Mouse APOE Christchurch protects against Aβ-induced tau and α-synuclein aggregation. *Cell Reports*. 2026. doi:10.1016/j.celrep.2026.118301
2. Arboleda-Velasquez JF, Lopera F, O'Hare M, Delgado-Tirado S, et al. Resistance to autosomal dominant Alzheimer's disease in an APOE3 Christchurch homozygote: a case report. *Nature Medicine*. 2019 Nov. doi:10.1038/s41591-019-0611-3. PMID: 31686034
3. Nelson MR, Liu P, Agrawal A, et al. The APOE-R136S mutation protects against APOE4-driven tau pathology, neurodegeneration and neuroinflammation. *Nature Neuroscience*. 2023 Dec. doi:10.1038/s41593-023-01480-8. PMID: 37957317
4. Chen G, Wang M, Zhang Z, et al. ApoE3 R136S binds to tau and blocks its propagation, suppressing neurodegeneration in mice with Alzheimer's disease. *Neuron*. 2025;113(5):719–736.e5. doi:10.1016/j.neuron.2024.12.015. PMID: 39814008
5. Holmes BB, DeVos SL, Kfoury N, et al. Heparan sulfate proteoglycans mediate internalization and propagation of specific proteopathic seeds. *Proceedings of the National Academy of Sciences of the USA*. 2013;110(33):E3138–E3147. doi:10.1073/pnas.1301440110. PMID: 23898162
6. Ihse E, et al. Cellular internalization of alpha-synuclein aggregates by cell surface heparan sulfate depends on aggregate conformation and cell type. *Scientific Reports*. 2017;7:9008. doi:10.1038/s41598-017-08720-5. PMID: 28827536
7. Zhang Q, Xu Y, Lee J, et al. A myosin-7B–dependent endocytosis pathway mediates cellular entry of α-synuclein fibrils and polycation-bearing cargos. *Proceedings of the National Academy of Sciences of the USA*. 2020;117(20):10865–10875. doi:10.1073/pnas.1918617117. PMID: 32366666
8. Vanderperre B, et al. Novel regulators of heparan sulfate proteoglycans modulate cellular uptake of α-synuclein fibrils. *Communications Biology*. 2025;8:1426. doi:10.1038/s42003-025-08786-2. PMID: 41053297
9. Mah D, Zhu Y, Su G, et al. Apolipoprotein E recognizes Alzheimer's disease associated 3-O sulfation of heparan sulfate. *Angewandte Chemie International Edition*. 2023;62(23):e202212636. doi:10.1002/anie.202212636. PMID: 37014788
10. Dunckley N, Driver-Dunckley ED, Zhang N, Serrano GE, et al. Greater burden of Alzheimer's co-pathology in women with Parkinson's disease dementia. *Journal of Parkinson's Disease*. 2026. doi:10.1177/1877718X261470295. PMID: 42496210
11. Structure-guided docking of benzene-1,3-disulfonic acid to the ApoE-HSPG binding site as a Christchurch-mimetic therapeutic strategy for Alzheimer's disease. *Research Square* preprint. rs-6515132. (Preprint — not peer-reviewed.)
12. Mayo Clinic News Network. Parkinson's disease: more Alzheimer's amyloid in women. News release, 6 November 2026. (Source of the plaque-score, percentage and odds-ratio figures for reference 10.)

## Data availability

All quantitative results in this paper derive from (a) the cited peer-reviewed literature and the Mayo Clinic news release listed above, and (b) an original sequence-charge computation on the human apolipoprotein E sequence retrieved live from UniProt (accession P02649) on 13 November 2026. The computation script and its output are archived in the goal workspace hidden files (`apoe-christchurch-charge-2026-11-13.py`). No new experimental data were generated. No patient data were used.

## AI-assistance disclosure

This manuscript was drafted with AI assistance (Lapis) from a structured literature sweep and an original sequence computation performed on 13 November 2026. All citations were verified against PubMed or publisher DOIs on that date. The author takes responsibility for the content and for the requirement of independent verification before any submission.
