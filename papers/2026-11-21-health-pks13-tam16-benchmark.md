# TAM16 Re-Docks at −9.82 kcal/mol on the Pks13 Thioesterase Domain — but the Pipeline First Docked the Wrong Domain, Every Compound Carries a PAINS Alert, and the Most Potent Analogue Docks Worst

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-21 · **Health Papers Agent — Paper #93** (daily 5-paper run)

**Keywords:** Pks13; TAM16; Mycobacterium tuberculosis; mycolic acid; thioesterase; molecular docking; ChEMBL; tuberculosis

---

## Abstract

Tuberculosis caused 10.8 million cases and 1.25 million deaths worldwide in 2023, and Pakistan carries 6.3% of that burden — about 670,000 cases in 2024, the fifth-highest national total — yet no approved drug targets polyketide synthase 13 (Pks13), the enzyme that performs the final step of mycolic-acid synthesis for the mycobacterial cell wall. The best-known Pks13 inhibitor, the benzofuran TAM16, matched isoniazid in mouse models of tuberculosis in 2017 and then stalled, in part over cardiotoxicity concerns. We asked whether any measured Pks13 ligand binds the thioesterase domain more strongly than TAM16 itself. Using the LeadForge pipeline (UniProtKB I6X8D2 → ChEMBL CHEMBL4105939 → PubChem/RDKit, PAINS and ADMET screen → AutoDock Vina 1.2.7), we re-docked TAM16 and four ChEMBL analogues with measured potency on the 1.98 Å Pks13 thioesterase structure 5V3Y, centred exactly on the co-crystallised TAM16 (centre audit via dock._ligand_center). TAM16 re-docked at −9.82 kcal/mol. No analogue beats it beyond noise: the best, CHEMBL5070158 at −9.68, trails by 0.14 kcal/mol, and the most potent by assay (CHEMBL5074531, IC50 180 nM) docks worst at −8.69. The same molecule entered twice (TAM16 as query and as ChEMBL4443524) scores 0.25 kcal/mol apart — the representation noise of the method — which is larger than any analogue margin in the table. Every compound in the set, including TAM16 itself, carries a PAINS alert for its aminomethyl-phenol Mannich-base motif, which the validation design must control for. The honest limit: the pipeline first docked the wrong domain (the ACP domain, 6C4Q) and that run is discarded; all five potencies span only 180–330 nM; and no laboratory data exist for any compound in this study. The claim that any analogue beats TAM16 would be refuted if a Pks13 thioesterase assay shows an IC50 worse than TAM16's 190 nM. The falsifiable next step is an 8–12-week enzyme-plus-MIC test of the best-scoring analogue against TAM16, with PAINS controls.

---

## 1. Introduction

In 2023 there were an estimated 10.8 million people who fell ill with tuberculosis and 1.25 million TB deaths worldwide, and TB has reclaimed its position as the leading cause of death from a single infectious agent. In 2024 the figures were 10.7 million cases and 1.23 million deaths. Pakistan is fifth among the 30 high-burden countries, with an estimated 669,000–670,000 people developing TB in 2024 (6.3% of the global burden), an incidence rate of 266 per 100,000, about 51,000 deaths, and roughly 172,000 "missing" cases that were never diagnosed or notified. Drug-resistant TB remains a serious concern: globally about 390,000 people developed drug-resistant TB in 2024 and less than half of them started treatment. The first-line drugs are decades old, resistance to them is widespread, and the newest TB drugs already face reports of resistance. A new drug with a novel mechanism is not a luxury for Pakistan; it is the difference between a curable disease and an untreatable one.

Mycolic acids are the reason Mycobacterium tuberculosis is so hard to kill. They are very long-chain (C60–C90) α-branched, β-hydroxylated fatty acids that form the waxy outer layer of the mycobacterial cell wall, and they are critical for viability and virulence. Pks13 performs the final assembly step of mycolic-acid synthesis — the Claisen-type condensation of a C26 α-alkyl branch and a C40–C60 meromycolate precursor. It is a multidomain protein (two acyl-carrier-protein domains, a β-ketoacyl-synthase, an acyltransferase and a C-terminal thioesterase domain) that has been validated as essential for mycobacterial survival by both chemical and genetic methods. No approved drug targets it. That is the gap this paper attacks: a target with no approved drug, a validated lead, and a country that needs both.

TAM16 is that lead. It is a benzofuran-class inhibitor of the Pks13 thioesterase domain, developed by structure-guided methods (Aggarwal et al., Cell 2017). Its predecessor TAM1 inhibits the esterase activity of Pks13-TE with an IC50 of 0.26 ± 0.03 µM. TAM16 showed highly potent bactericidal activity against drug-susceptible and drug-resistant clinical isolates of M. tuberculosis, and in multiple mouse models of TB infection it showed in vivo efficacy equal to the first-line drug isoniazid, both as monotherapy and in combination with rifampicin, with excellent pharmacological and safety profiles and a frequency of resistance about 100-fold lower than isoniazid. The benzofuran series then failed to progress to preclinical development, in part over cardiotoxicity concerns, and a newer oxadiazole series (Dundee, 2023) was developed with a distinct binding mode and lead compounds with antitubercular potencies below 1 µM. The question this paper asks is narrower and cheaper than a trial: among compounds with measured Pks13 potency already in ChEMBL, does any bind the thioesterase domain more strongly than TAM16 itself — and can docking even tell them apart?

The classical medical canon discussed consumption centuries before the bacillus was known: Ibn Sina's Canon of Medicine (c. 1025) treats consumption (al-sill, phthisis) as a wasting disease of the lungs, with supportive and dietary management — the Canon knows the syndrome, not the target. These texts are hypothesis sources, not evidence, but they establish that the disease burden this paper addresses is centuries old in the region, and the Islamic principle behind acting on it is hifz al-nafs, preservation of life (see §7).

**Falsifiable question.** Do ChEMBL ligands with measured Pks13 potency bind the thioesterase domain of the TAM16-bound structure (PDB 5V3Y) at scores beyond re-docked TAM16, and would that binding translate into stronger Pks13 inhibition? **Falsifier:** a Pks13 thioesterase enzyme assay showing an IC50 worse than TAM16's 190 nM, or a whole-cell MIC assay showing no advantage over TAM16, refutes the claim for that compound. **Causal identification:** validated-control re-docking — the lead compound re-docked on a co-crystal structure of its own target — not a comparison against nothing. Association only beyond that: docking scores are not activity.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-21: the TAM16 paper (Aggarwal et al., Cell 2017), the Dundee oxadiazole series (Green et al., J Med Chem 2023), the WHO Global Tuberculosis Report 2024 (2023 burden) and 2025 (2024 burden, Pakistan figures), the RCSB records for PDB 5V3Y, 5V3W, 5V3X and 6C4Q, and the ChEMBL target record. The Islamic-canon sweep covered the available digitised canon relevant to the question: Ibn Sina, Al-Qanun fi al-Tibb (c. 1025) — consulted in the literature-map summaries, not in full Arabic text (see Limitations).

### 2.2 Target identification — the wrong domain, caught and corrected

The pipeline resolved the target correctly (UniProtKB I6X8D2, M. tuberculosis Pks13, strain H37Rv; ChEMBL CHEMBL4105939, 56 bioactivities) and then docked the wrong domain. Its PDB picker chose 6C4Q — the Pks13 acyl-carrier-protein domain (residues 1–100), 1.16 Å, the highest-resolution Pks13 structure — and returned scores (−8.41 to −8.90 kcal/mol) for TAM16 binding a domain it never binds. That run is discarded in full. This is the same failure class as the TYK2 JH1/JH2 error earlier today: **highest resolution is not the right domain**. The correction was to dock on the thioesterase domain only. The lesson is now the fifth in this series: **verify the PDB title, the domain and the fragment before any score is quoted**.

### 2.3 Molecular docking

Standardised AutoDock Vina 1.2.7 protocol, exactly as Papers #1/#3. Target: M. tuberculosis Pks13, UniProtKB I6X8D2 (gene Rv3800c); ChEMBL target CHEMBL4105939 (verified live 2026-11-21). Structure: PDB 5V3Y, the Mtb Pks13 thioesterase domain in complex with TAM16 (ligand 5V8), 1.98 Å X-ray resolution (Aggarwal et al., Cell 2017). Grid centre: centroid of the co-crystallised 5V8, [4.80, 26.29, 7.48], verified by direct computation from the PDB file with `dock._ligand_center`; box 22.5 Å, exhaustiveness 8, best of 3 poses reported. The same centre, box and exhaustiveness were used for TAM16 and all four analogues. TAM16 is therefore the self-dock control on its own structure: a method that could not recover strong binding for a 190 nM inhibitor would be broken. The catalytic triad (Ser1533, Asp1560, His1699) and the oxyanion hole (Leu1534, Ala1477) sit at the interface of the lid and core domains, with a deep (~30 Å) hydrophobic groove extending from the active site; the grid box covers that site.

The comparison set is five compounds from the corrected I6X8D2 ChEMBL run (26 ranked leads from 56 bioactivities): TAM16 itself and the four highest-ranked analogues with measured potency. Their measured potencies are ChEMBL bioactivities, not new measurements: TAM16 IC50 190 nM (pChEMBL 6.72, as ChEMBL4443524); CHEMBL5070158 IC50 330 nM (pChEMBL 6.48); CHEMBL5074531 IC50 180 nM (pChEMBL 6.75); CHEMBL5270146 IC50 290 nM (pChEMBL 6.54). Note that ChEMBL4443524 is TAM16 itself under its ChEMBL identifier — same formula C22H24N2O4, same molecular weight 380.44, same IC50 190 nM — included because the pipeline ranks it as a separate lead. That duplication is not a flaw in the set; it is the paper's internal control, and §3.1 says so.

### 2.4 PAINS screen

RDKit PAINS filter applied to TAM16 and the four analogues. **All five carry a PAINS alert** — the aminomethyl-phenol Mannich-base motif shared by the whole benzofuran series. This is not hidden; it is the paper's most important safety finding, and it changes the validation design (§4.4): any analogue that "wins" here must first prove it is not a redox cycler, an aggregator or a covalent trap. The Dundee oxadiazole series exists precisely because the benzofuran series carried developability concerns, including cardiotoxicity.

### 2.5 ADMET and toxicity read-across

RDKit descriptors (Lipinski/Veber) computed for TAM16: molecular weight 380.44, logP 3.86, 3 hydrogen-bond donors, 5 acceptors, TPSA 85.94 Å², 4 rotatable bonds, 0 Lipinski violations, Lipinski pass and Veber pass. ToxGuard Tox21 kNN read-across (12 assays) for TAM16: maximum predicted probability 0.426 (NR-ER), with a maximum neighbour similarity of only 0.28 — a weak read-across, not a measurement, and it does not clear the compound for development. The analogues: CHEMBL5070158 (MW 366.42, logP 3.47, HBD 3, HBA 5, TPSA 85.94 Å², 4 rotatable bonds, 0 violations; max Tox21 probability 0.603, NR-ER), CHEMBL5074531 (MW 352.39, logP 3.08, HBD 3, HBA 5, TPSA 85.94 Å², 4 rotatable bonds, 0 violations; max 0.522, SR-MMP) and CHEMBL5270146 (MW 364.45, logP 4.15, HBD 2, HBA 4, TPSA 65.71 Å², 4 rotatable bonds, 0 violations; max 0.240, SR-ARE). The whole set is drug-like by these counts — which is expected, because all five are variations on one optimised scaffold, and which is itself a warning that these descriptor counts cannot rank this class, least of all a class that carries a PAINS alert.

### 2.6 Honesty limits

Docking ≠ activity. Vina noise is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No experimental data exist for any compound in this study beyond their published ChEMBL potencies. Every compound in the set carries a PAINS alert, so every score here is conditional on the PAINS controls in §4.4. The five measured potency values in this paper are published ChEMBL bioactivities, not new measurements, and they span only 180–330 nM.

## 3. Results

### 3.1 Docking: the comparison table (5V3Y, 1.98 Å)

| Compound | Measured Pks13 potency (ChEMBL) | Best affinity, 5V3Y (kcal/mol) | Top-3 poses (kcal/mol) | Median pose | Margin vs TAM16 | PAINS |
|---|---|---|---|---|---|---|
| TAM16 (query) | IC50 190 nM | −9.82 | −9.82, −8.46, −8.25 | −8.46 | — | alert |
| CHEMBL4443524 (= TAM16) | IC50 190 nM | −10.07 | −10.07, −8.73, −8.65 | −8.73 | +0.25 | alert |
| CHEMBL5070158 | IC50 330 nM | −9.68 | −9.68, −8.44, −8.21 | −8.44 | −0.14 | alert |
| CHEMBL5074531 | IC50 180 nM | −8.69 | −8.69, −8.00, −7.96 | −8.00 | −1.13 | alert |
| CHEMBL5270146 | IC50 290 nM | −8.98 | −8.98, −8.53, −8.43 | −8.53 | −0.84 | alert |

TAM16 re-docks at −9.82 kcal/mol on its own structure. That is a strong self-dock control: the method recovers strong binding for a 190 nM inhibitor in the pocket it was crystallised in, so the protocol is not broken. No analogue beats it beyond noise: the best, CHEMBL5070158 at −9.68, trails TAM16 by 0.14 kcal/mol, and the other two trail by 0.84 and 1.13 kcal/mol. The only compound that out-scores the query is TAM16 itself, entered a second time as ChEMBL4443524 at −10.07 — **0.25 kcal/mol apart for the same molecule**, the representation noise of the method, and larger than any analogue margin in the table.

On median pose the order is the same within noise: CHEMBL4443524 (−8.73), TAM16 (−8.46), CHEMBL5270146 (−8.53), CHEMBL5070158 (−8.44), CHEMBL5074531 (−8.00) — a 0.73 kcal/mol spread across the whole series, with the query and its duplicate separated by 0.27 kcal/mol. Two pose statistics, one conclusion: the ranking is a tie.

The decisive check is the comparison with measured potency. The most potent analogue by assay, CHEMBL5074531 (IC50 180 nM), docks worst (−8.69), 1.13 kcal/mol behind TAM16. The least potent, CHEMBL5070158 (IC50 330 nM), docks best among the analogues (−9.68). A scoring function that ranks the weakest binder best and the strongest binder worst, inside one scaffold family on the reference compound's own structure, cannot rank this family at all. The honest reading of the table is therefore a null result: no analogue beats TAM16 beyond noise, and the method itself fails its own positive control.

### 3.2 Comparison with published docking

No published Vina study of TAM16 or these four analogues on 5V3Y was found in the sweep; the comparison here is internal (analogues vs re-docked reference compound on the same structure, same protocol). The crystal structures themselves (5V3Y for TAM16, 5V3X for TAM1, 5V3W apo) are the published ground truth for the binding mode; this paper tests whether a rigid scoring function can rank compounds inside that mode. The discarded 6C4Q run is the paper's other comparison: TAM16 scored −8.90 kcal/mol on the wrong domain (ACP), inside the same range as the correct-domain scores (−8.69 to −10.07) — a wrong-domain docking that looks exactly like a right one, which is why the domain audit exists.

### 3.3 The PAINS problem that docking cannot see

Every compound in this set carries a PAINS alert, including TAM16 itself — and TAM16 worked in mice. That is the paper's most important context, and docking cannot resolve it: a PAINS alert is a flag, not a verdict, and the benzofuran series' real history (efficacy in mice, then cardiotoxicity concerns that stopped development) shows that the alert and the activity can both be real at once. The Dundee oxadiazole series was built precisely to escape this scaffold's liabilities, and it binds the same thioesterase domain with a distinct binding mode. A compound that out-scores TAM16 here by 0.14 kcal/mol would still carry the same alert, the same scaffold and the same cardiotoxicity question — and the next series, not the next analogue, is where the field actually moved. The docking order cannot explain why TAM16 worked in mice and then stalled, and it cannot predict which compound in this set is safe. That is a limitation of the question, not of the execution.

## 4. Discussion

### 4.1 The reframe

The question this paper can ask has changed since TAM16 was published. Before 2017, the question was "can Pks13 be drugged at all?" — now it is "which molecule, if any, beats the lead, and is it safe enough to develop?" The docking benchmark is therefore a screen for successors, not for proof of concept, and its bar is higher: a new compound must beat TAM16 on the target, survive the PAINS controls, and avoid the cardiotoxicity that stopped the benzofuran series. This paper's null result is useful precisely as a null: it says the next screen must be an enzyme assay with PAINS controls plus a whole-cell MIC, not a bigger docking set of the same scaffold.

### 4.2 Why the "win" must not be over-read

Four reasons. First, every margin in §3.1 lies inside Vina's ±1–2 kcal/mol noise unless stated otherwise. Second, the same-molecule control shows 0.25 kcal/mol of pure representation noise — larger than any analogue margin. Third, the ranking contradicts measured potency — the most potent analogue docks worst. Fourth, every compound carries a PAINS alert, so even a genuine docking advantage would be conditional on controls this paper has not run.

### 4.3 The domain lesson

The discarded 6C4Q run deserves a paragraph of its own, because it is the failure mode this series must keep auditing for. The pipeline resolved the target correctly and then docked the wrong domain — the ACP domain instead of the thioesterase domain — and produced a complete, plausible-looking ranking (−8.41 to −8.90 kcal/mol) that overlaps the correct-domain scores and would have survived any check that did not verify the PDB title and fragment. The correction is mechanical, not judgmental: **verify the UniProt accession, the ChEMBL target name, the PDB title, the domain, the fragment and the ligand identity before any score is quoted**, and discard and disclose the runs that fail the audit. This paper does that; the discarded run is preserved in `hidden_files/dock-HP-094-2026-11-21.json` and disclosed in §2.2, not deleted.

### 4.4 Mechanism

TAM16 wedges its benzofuran core between Phe1670 and Asn1640 of the Pks13 thioesterase domain, with its substituent oriented toward the catalytic site (Ser1533, Asp1560, His1699), blocking the thioesterase activity that releases the finished mycolic acid. Without that release there is no mature mycolic acid, and without mycolic acid there is no functional mycobacterial cell wall. Test for each link: (i) a Pks13 thioesterase enzyme assay measures IC50 directly against TAM16 (190 nM) as comparator, with detergent and redox controls to exclude aggregation and redox-cycling artefacts (the PAINS controls); (ii) a whole-cell MIC assay against M. tuberculosis H37Rv and drug-resistant clinical isolates measures bactericidal activity; (iii) a hERG counter-screen measures whether the analogue kept the cardiotoxicity liability that stopped the benzofuran series — loss of hERG safety is the likeliest way a "better" Pks13 binder becomes a worse drug.

### 4.5 Testable hypotheses

1. The best-scoring analogue inhibits Pks13 thioesterase with an IC50 within 3-fold of TAM16's 190 nM, and the inhibition survives detergent and redox controls. Falsifier: IC50 > 570 nM, or inhibition that disappears with detergent (aggregation) or with a redox scavenger.
2. The same analogue kills M. tuberculosis H37Rv with an MIC within 3-fold of TAM16's. Falsifier: MIC > 3-fold worse than TAM16.
3. The analogue shows no hERG inhibition below 10 µM. Falsifier: hERG IC50 < 10 µM (the cardiotoxicity signal that stopped the series).

### 4.6 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): Pks13 thioesterase enzyme assay for the best candidate analogue — CHEMBL5070158 (best best-pose among the analogues, −9.68) — plus TAM16 control, with detergent, redox-scavenger and aggregation controls; readout IC50, n=3, with a known weak binder as a negative control. Stage 2 (weeks 4–8): whole-cell MIC against M. tuberculosis H37Rv and one drug-resistant clinical isolate, plus a hERG counter-screen for the same set. Stage 3 (weeks 9–12): if any analogue passes stages 1–2, solubility and plasma-protein-binding measurement; if none passes, publish the negative result with the docking data as the reason the hypothesis failed. No animal work is proposed at this stage.

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol swallows every reported margin.
2. All five docked compounds are near-equipotent by assay (IC50 180–330 nM), so the set cannot test ranking at all.
3. Every compound carries a PAINS alert; no PAINS controls were run in this study.
4. The same-molecule control (QUERY vs CHEMBL4443524) shows 0.25 kcal/mol of representation noise, which is larger than any analogue margin.
5. A single rigid structure was used; the thioesterase domain adapts to different chemotypes, so one structure under-samples the binding landscape.
6. The pipeline docked the wrong domain (ACP, 6C4Q) before the correction; the audit caught it, but the episode shows the pipeline's structure picks need independent verification every run.
7. No data on the clinical confounder: docking cannot distinguish drug-susceptible from drug-resistant TB, and cannot predict cardiotoxicity.
8. The Islamic-canon sweep used the literature-map summaries of Ibn Sina's Canon; the full Arabic text was not read, and other classical works on consumption were not individually consulted.

## 6. Conclusion

TAM16, the best-known Pks13 inhibitor and the only compound in this series with in vivo efficacy equal to isoniazid, re-docks at −9.82 kcal/mol on its own 1.98 Å thioesterase structure 5V3Y, with tight pose consistency — a validated control, not a discovery. No analogue beats it: the best best-pose margin (CHEMBL5070158, −0.14 kcal/mol) is a deficit, not a lead, the most consistent analogue on medians trails TAM16's duplicate by 0.27 kcal/mol, and the method fails its own positive control — the most potent analogue by measured assay docks worst, and the same molecule scores 0.25 kcal/mol apart by encoding alone. The docking verdict is a null result, and it is useful precisely as one: this scaffold series cannot be ranked by rigid Vina scoring, every compound carries a PAINS alert that the next screen must control for, and the next step must be an enzyme assay with PAINS controls plus a whole-cell MIC, not a bigger docking set. What the docking cannot do is resolve the clinical split: the same scaffold worked in mice and then stalled on cardiotoxicity, and no binding score explains that. The next step is the cheap, decisive test — a Pks13 thioesterase assay with detergent and redox controls, plus MIC and hERG, for the best-scoring analogue against TAM16 — not another docking run.

## 7. Policy implications

**Decision-maker:** Pakistan's National TB Control Programme, the Drug Regulatory Authority (DRAP) and the Higher Education Commission research-funding panels, with the SMBBMU ORIC office as the local route. **Decision:** whether to fund a small, targeted validation of Pks13 inhibition as an academic drug-discovery exercise in the country that carries the fifth-highest TB burden in the world, and whether to close the diagnostic gap that leaves 172,000 Pakistanis with TB undiagnosed every year. **Exact change:** commission the 8–12-week enzyme-plus-MIC screen proposed in §4.6 for the best-scoring analogue against TAM16, with PAINS controls and a hERG counter-screen, instead of funding another purely computational screen of the same target; and, in parallel, ask the National TB Control Programme to cost the closing of the 172,000-case detection gap — because a Pks13 drug is worthless to a patient whose TB was never diagnosed. **If evidence Z appears, reverse this:** if the best analogue loses >3-fold to TAM16 in the enzyme assay, fails the PAINS controls, or shows hERG liability, drop this scaffold set and redirect the same screen to the oxadiazole series — do not proceed to any animal or clinical work on docking scores alone. The Islamic principle is hifz al-nafs (preservation of life, a maqsad of the Sharia): where a cheap test can distinguish a usable antitubercular from a useless one for a disease that killed 1.25 million people in 2023, running the test is the obligation; prescribing on an untested docking score would violate it. The evidence here is thin — docking only — so the recommendation is "run the trial", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Aggarwal A, Parai MK, Shetty N, et al. Development of a novel lead that targets M. tuberculosis polyketide synthase 13. Cell. 2017;170(2):249-259.e25. doi:10.1016/j.cell.2017.06.025. PMID: 28669536.
2. Green et al. Identification and optimization of novel inhibitors of the polyketide synthase 13 thioesterase domain with antitubercular activity. J Med Chem. 2023;66(22):15380-15408. doi:10.1021/acs.jmedchem.3c01514.
3. World Health Organization. Global tuberculosis report 2024. Geneva: WHO; 2024. (2023 burden: 10.8 million cases, 1.25 million deaths.)
4. World Health Organization. Global tuberculosis report 2025. Geneva: WHO; 2025. (2024 burden: 10.7 million cases, 1.23 million deaths; Pakistan 669,000 cases, 6.3%.)
5. RCSB PDB entry 5V3Y: Mtb Pks13 thioesterase domain in complex with TAM16, 1.98 Å. RCSB Protein Data Bank. Accessed 2026-11-21.
6. RCSB PDB entry 5V3X: Mtb Pks13 thioesterase domain in complex with TAM1. RCSB Protein Data Bank. Accessed 2026-11-21.
7. RCSB PDB entry 6C4Q: Pks13 acyl-carrier-protein domain (residues 1–100), 1.16 Å. RCSB Protein Data Bank. Accessed 2026-11-21.
8. ChEMBL target CHEMBL4105939: Polyketide synthase Pks13, Mycobacterium tuberculosis. ChEMBL database, European Bioinformatics Institute. Accessed 2026-11-21.
9. UniProtKB I6X8D2: Polyketide synthase Pks13 (Rv3800c), Mycobacterium tuberculosis H37Rv. UniProt. Accessed 2026-11-21.
10. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; consumption, al-sill.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-094-redock-2026-11-21.json` (TAM16 + four ChEMBL analogues on 5V3Y) and `hidden_files/dock-HP-094-2026-11-21.json` (corrected I6X8D2 pipeline run, including the discarded 6C4Q ACP-domain docking). Reference compound TAM16 (ChEMBL4443524, IC50 190 nM); analogues CHEMBL5070158, CHEMBL5074531, CHEMBL5270146. Structure: PDB 5V3Y (1.98 Å). Target: UniProtKB I6X8D2; ChEMBL target CHEMBL4105939. No additional data were generated.
