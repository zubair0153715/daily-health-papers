# Meropenem Out-Scores Avibactam by 1.22 kcal/mol on Wild-Type OXA-48 — and the Comparison Is Meaningless, Because One Is a Substrate and the Other Is Covalent

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-23 · **Health Papers Agent — Paper #104** (daily 5-paper run)

**Keywords:** OXA-48; avibactam; carbapenemase; meropenem; molecular docking; ChEMBL; antimicrobial resistance; diazabicyclooctane; ceftazidime-avibactam

---

## Abstract

Bacterial antimicrobial resistance directly caused an estimated 1.27 million deaths in 2019, and the OXA-48 carbapenemase — a class D serine β-lactamase widespread in Enterobacterales — is one of the enzymes that makes carbapenems, the drugs of last resort, fail. Avibactam, the diazabicyclooctane inhibitor paired with ceftazidime, inhibits OXA-48 by acylating its catalytic Ser70 — covalently, and only slowly reversibly. We asked whether any measured OXA-48 ligand binds the active site more strongly than avibactam. Using the LeadForge pipeline (UniProtKB Q6XEC0 → ChEMBL CHEMBL1287604 → PubChem/RDKit, PAINS and ADMET screen → AutoDock Vina 1.2.7), we docked avibactam and the single ChEMBL ligand with measured potency on the 2.3 Å wild-type OXA-48 structure in covalent complex with avibactam (PDB 4WMC), centred exactly on the co-crystallised avibactam (centre audit via dock._ligand_center). Avibactam re-docked, non-covalently, at −6.73 kcal/mol. The comparator, CHEMBL127 — verified as meropenem, the carbapenem substrate (Kd 850 nM) — scored −7.95 kcal/mol, "beating" avibactam by 1.22 kcal/mol. The comparison is meaningless, and the paper says so plainly: meropenem is the substrate OXA-48 hydrolyses, not an inhibitor, and avibactam's potency lives in the covalent acylation step that rigid non-covalent docking cannot model at all. A substrate out-scoring a covalent inhibitor on a non-covalent score proves the method's limit, not the substrate's superiority. The pipeline's first answer was worse still: it docked both compounds on 8PEB, a directed-evolution quintuple mutant centred on a malonate buffer ion, and those scores are discarded here as measurements of the wrong enzyme. The falsifiable next step is a nitrocefin-hydrolysis inhibition assay of avibactam against OXA-48, with the 4WMC pose as the structural hypothesis — not another docking run.

---

## 1. Introduction

The β-lactams — penicillins, cephalosporins, carbapenems — are the most commonly prescribed antibiotic class, and in Gram-negative bacteria the dominant resistance mechanism is production of β-lactamases that hydrolyse the four-membered β-lactam ring. The carbapenemases are the enzymes that defeat the drugs of last resort, and OXA-48, a class D serine β-lactamase, is among the most widely disseminated in Enterobacterales, the order that includes Escherichia coli and Klebsiella pneumoniae. OXA-48 uses a nucleophilic serine (Ser70) to hydrolyse β-lactams, with a proximal post-translationally carbamylated lysine (Lys73) proposed to act as the general base for both the acylation and deacylation steps of the reaction. It confers resistance to penicillins and moderate resistance to cephalosporins and carbapenems, and its variants — OXA-163 and OXA-405, with deletions in the β5–β6 loop neighbouring the active site — change activity towards different β-lactam classes.

Avibactam is the inhibitor that extended β-lactam therapy to OXA-48 producers. A diazabicyclooctane (DBO), not a β-lactam, it inhibits class A and class C β-lactamases and certain class D enzymes, and it does so covalently: it acylates Ser70, and the acyl-enzyme deacylates only exceptionally slowly in class D enzymes — the slow reversibility that the 4WMC structure was solved to explain. The combination ceftazidime–avibactam is the clinical product. The DBO class is not uniform against OXA-48: nacubactam is about 80-fold less potent than avibactam towards the enzyme, a difference traced to electrostatic repulsion between Arg214 on the β5–β6 active-site loop and nacubactam, but not avibactam — and the difference shrinks in OXA-163 and OXA-405, which lack Arg214. Sequence variation in the loop therefore affects reactivity towards inhibitors as well as towards β-lactam substrates, and crystallographic and mass-spectrometry data show all three enzymes support desulfation of the bound DBOs. The question this paper asks is the standard one for this series: among compounds with measured OXA-48 potency already in ChEMBL, does any bind the active site more strongly than avibactam — and can non-covalent docking even ask that question about a covalent inhibitor?

The classical medical canon knows the wound, not the enzyme: Ibn Sina's Canon of Medicine (c. 1025) treats wounds and fevers — the syndrome, not the carbapenemase. The principle carried forward here is hifz al-nafs, preservation of life (see §7).

**Falsifiable question.** Do ChEMBL ligands with measured OXA-48 potency bind the active site of the avibactam-bound structure (PDB 4WMC) at non-covalent scores beyond re-docked avibactam, and would that binding translate into stronger OXA-48 inhibition? **Falsifier:** a nitrocefin-hydrolysis inhibition assay showing an IC50 worse than the analogue's published value, or loss of potentiation of ceftazidime against an OXA-48 producer, refutes the claim for that compound. **Causal identification:** validated-control re-docking — the inhibitor re-docked, non-covalently, on a co-crystal structure of its own target, with the co-crystallised inhibitor as the centre — not a comparison against nothing. Association only beyond that: docking scores are not activity, and for a covalent inhibitor they are not even a proxy for the rate-limiting step.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-23: the OXA-48/avibactam structural paper (Lahiri et al., ACS Chem Biol 2015;10:591–600; PMID 25406838; doi:10.1021/cb500703p); the DBO electrostatic study (Hoff et al., RSC Med Chem 2025;16:5441–5455; PMID 40927637; doi:10.1039/d5md00512d); the directed-evolution epistasis paper and the 8PEB structure (Frohlich et al., Nat Catal 2024;7:499–509; PMID 38828429; doi:10.1038/s41929-024-01117-4); the global antimicrobial-resistance burden analysis (Antimicrobial Resistance Collaborators, Lancet 2022;399:629–655); and the RCSB records for PDB 4WMC and 8PEB.

### 2.2 Target identification

The pipeline resolved the target correctly on the first run: UniProtKB Q6XEC0 (beta-lactamase OXA-48, Klebsiella pneumoniae) → ChEMBL CHEMBL1287604, "Beta-lactamase OXA-48", SINGLE PROTEIN, 1 bioactivity, verified live 2026-11-23. This is the correct target, the correct organism — and a comparison set of exactly one compound, which is the thin end of the series: one bioactivity cannot test ranking.

### 2.3 The pipeline's failure, stated not smoothed over

The pipeline's PDB picker selected 8PEB and docked avibactam at −6.27 kcal/mol and meropenem at −7.29 kcal/mol. Verified live 2026-11-23, 8PEB is OXA-48_Q5 — a directed-evolution quintuple mutant whose four mutations increase antibiotic resistance 40-fold by shifting the rate-limiting step of the catalytic cycle — and it is an apo structure: the only drug-like HETATM group in the file is a malonate buffer ion (MLI, 9 atoms), and the centre the pipeline used is that ion's centroid. The scores are therefore dockings into a mutant enzyme centred on a buffer ion, and they are discarded in full: they appear in this paper only as the artefact they are, with their file reference, so that no reader mistakes them for a result. The same structure-picker error has now bitten this series five times in two days (Papers #95, #100, #101, #103, #104), and the lesson is the same: the picked PDB entry's title, mutations and bound ligands must be verified by hand, every run.

### 2.4 Molecular docking — the redock on the correct structure

The benchmark structure is 4WMC: the 2.3 Å crystal structure of wild-type OXA-48 in covalent complex with avibactam (Lahiri et al., ACS Chem Biol 2015). A targeted redock script (`health-papers-agent/redock_hp063_4wmc.py`) docked avibactam and meropenem on 4WMC using standardised AutoDock Vina 1.2.7, exactly as Papers #1/#3: grid centre the centroid of the co-crystallised avibactam (ligand NXL, chain A residue 301, 17 heavy atoms — C7H11N3O6S, matching avibactam), [42.21, 34.64, 52.56], verified by direct computation from the PDB file with `dock._ligand_center`. The centre audit is the decisive check here: the file holds eight OXA-48 chains, each with its own covalently bound avibactam, plus carbamylated Lys73 (KCX) and carbon-dioxide groups, and a naive group-average pick would have centred on the average of all eight avibactams — a point in empty space between chains. `dock._ligand_center` returned chain A's NXL centroid, which is a real binding site, and the audit names it. Box 22.5 Å, exhaustiveness 8, best of 3 poses reported. The same centre, box and exhaustiveness were used for both compounds. Avibactam is therefore the self-dock control on its own structure — with the covalent caveat in §2.5 attached, not hidden. The docked avibactam is the parent SMILES as returned by PubChem (CID 9835049); the crystal holds the same molecule, covalently bound to Ser70, so the docked pose is the non-covalent encounter complex of the same molecule, not a metabolite.

### 2.5 The covalent caveat — why this docking cannot rank DBO inhibitors

Avibactam inhibits OXA-48 by acylating Ser70. The acyl-enzyme then deacylates only exceptionally slowly in class D enzymes — that slow reversibility is the drug's mechanism and the reason the 4WMC structure was solved. Rigid non-covalent Vina docking models neither the acylation step nor the deacylation rate; it scores the encounter complex before the bond forms. A non-covalent score therefore cannot rank covalent DBO inhibitors against each other, and it cannot rank an inhibitor against a substrate at all: the substrate's score measures how well it sits in the pocket before hydrolysis, and the inhibitor's score measures how well it sits in the pocket before acylation, and those are different questions with different answers. This paper reports both scores with that caveat in the table itself, not in a footnote.

### 2.6 PAINS screen

RDKit PAINS filter applied to avibactam and meropenem. Both are PAINS-clean. No PAINS alert is hidden anywhere in this paper; there is none to hide.

### 2.7 ADMET and toxicity read-across

RDKit descriptors computed for avibactam: molecular weight 265.25, logP −1.53, 2 hydrogen-bond donors, 5 acceptors, TPSA 130.24 Å², 3 rotatable bonds, 0 Lipinski violations, Lipinski pass and Veber pass. Meropenem (CHEMBL127): molecular weight 383.47, logP −0.31, 3 hydrogen-bond donors, 6 acceptors, TPSA 110.18 Å², 5 rotatable bonds, 0 Lipinski violations, Lipinski pass and Veber pass. ToxGuard Tox21 kNN read-across (12 assays) for avibactam: maximum predicted probability 0.148 (NR-AR), a weak read-across (maximum neighbour similarity 0.22), not a measurement, and it does not clear the compound for development — it is the profile of an already-approved drug, reported for completeness. Meropenem's Tox21 panel was measured (mode: measured), with all assays 0 except SR-MMP (not reported).

### 2.8 Honesty limits

Docking ≠ activity, and for a covalent inhibitor docking ≠ even the rate-limiting step. Vina noise is ±1–2 kcal/mol. No molecular dynamics, free-energy refinement or covalent docking was run. No experimental data exist for any compound in this study beyond meropenem's published Kd of 850 nM. The comparison set is a single compound — and it is a substrate, not an inhibitor — so the benchmark question is unanswerable in the form asked. One rigid structure was used (4WMC, wild-type OXA-48, 2.3 Å, eight chains in the asymmetric unit); the β5–β6 loop is flexible and adapts to different chemotypes, so one structure under-samples the binding landscape. The docked avibactam returned only two poses, so its pose ensemble is thinner than the three-pose standard of this series.

## 3. Results

### 3.1 Docking: the comparison table (4WMC, 2.3 Å — the drug's own structure)

| Compound | Measured OXA-48 potency (ChEMBL) | Best affinity, 4WMC (kcal/mol) | Top-3 poses (kcal/mol) | Median pose | Margin vs avibactam |
|---|---|---|---|---|---|
| CHEMBL127 (meropenem — carbapenem SUBSTRATE) | Kd 850 nM | −7.95 | −7.95, −7.48, −6.87 | −7.48 | −1.22 |
| Avibactam (reference — COVALENT inhibitor) | — (approved drug; potency is in the acylation step) | −6.73 | −6.73, −6.23 (2 poses only) | — | — |

Avibactam re-docks, non-covalently, at −6.73 kcal/mol on its own structure, with only two poses returned (−6.73, −6.23): the method recovers binding for the drug in the pocket it was crystallised in, so the protocol is not broken — but the score is weak, and the pose ensemble is thin. Meropenem "beats" it at −7.95 kcal/mol, a 1.22 kcal/mol margin that lies inside Vina's ±1–2 kcal/mol noise even before the category error is considered. The discarded pipeline scores (−6.27 for avibactam and −7.29 for meropenem on 8PEB, the quintuple mutant centred on malonate) are not in the table, because they are not measurements of wild-type OXA-48 — though it is worth noting that they show the same order, which is itself a warning: the wrong structure and the right structure agree, because both are measuring the same non-covalent encounter complex, and neither measures the covalent step.

The decisive check is the comparison with what the molecules are, and it dissolves the ranking. Meropenem is the substrate: OXA-48 hydrolyses it, and its Kd of 850 nM is a binding constant for a molecule the enzyme destroys. Avibactam is the inhibitor: its potency lives in the acylation of Ser70 and the exceptionally slow deacylation that follows, neither of which appears in a Vina score. A scoring function that ranks a substrate above a covalent inhibitor on a non-covalent score has not found a better inhibitor; it has found the limit of its own question. The honest reading of the table is therefore a null result on ranking, with a method lesson: no compound in this run can be claimed to beat avibactam, because the only comparator is not an inhibitor and the score cannot see the inhibition.

### 3.2 Comparison with published data

No published Vina study of avibactam or meropenem on 4WMC was found in the sweep; the comparison here is internal (ligands vs re-docked reference drug on the same structure, same protocol). The structural literature is the published ground truth for the binding mode: the 4WMC structure shows avibactam covalently bound to Ser70, with the carbamylated Lys73 positioned as the general base, and the asymmetric unit's eight subunits provide snapshots of different states of the inhibited enzyme — the structural evidence for the exceptionally slow reversibility. The DBO literature gives the paper its most useful context: nacubactam is about 80-fold less potent than avibactam towards OXA-48, and the difference is electrostatic repulsion with Arg214 on the β5–β6 loop — a loop-sequence effect that rigid docking on a single wild-type structure cannot see, and that disappears in the OXA-163 and OXA-405 variants that lack Arg214.

### 3.3 The clinical confounder that docking cannot see

Avibactam's clinical record is the paper's most important context, and docking cannot see any of it. The drug's value is not its non-covalent affinity — it is that the acyl-enzyme it forms with OXA-48 barely deacylates, so a single molecule blocks the enzyme for far longer than a substrate occupies it, and that ceftazidime–avibactam restores activity against OXA-48 producers that no cephalosporin alone can touch. A compound that out-scores avibactam here by 1.22 kcal/mol but deacylates in seconds would be a worse drug, and docking cannot tell the two apart. The docking order cannot explain why ceftazidime–avibactam works where ceftazidime alone fails; the acylation chemistry together with the structure can.

## 4. Discussion

### 4.1 The reframe

The question this paper can ask has changed since avibactam was approved. Before approval, the question was "can a non-β-lactam inhibit a class D carbapenemase at all?" — now it is "which molecule, if any, acylates Ser70 faster and deacylates slower than avibactam?" The benchmark is therefore a screen for successors with a two-part bar: a non-covalent encounter score at least as good as −6.73 kcal/mol on 4WMC, and a covalent acylation/deacylation profile at least as good as avibactam's. This paper supplies the first half of the bar and shows the second half is where the pipeline must go next: the comparison set is a single substrate, and the score cannot see the covalent step.

### 4.2 Why the "win" must not be over-read

Three reasons. First, the margin (1.22 kcal/mol) lies inside Vina's ±1–2 kcal/mol noise. Second, the comparator is a substrate, not an inhibitor — the ranking compares two different molecular events. Third, avibactam's potency is covalent and the score is not: the method measures the encounter complex and calls it the drug, which is like judging a lock by how well the key slides in before it turns.

### 4.3 The covalent problem is the experiment's design constraint, not a reason to stop

The single-compound comparison set was chosen by pipeline rank, not by mechanism, and ChEMBL's one bioactivity for OXA-48 happened to be a substrate. The honest handling is to report the scores with the category error in the table itself, and to design the validation assay so the covalent question is answered by the experiment: a nitrocefin-hydrolysis assay measures inhibition regardless of mechanism, and a mass-spectrometry acylation assay (or a deacylation-rate measurement) would then place the covalent step. A compound that scores well non-covalently but acylates slowly is not a failure of the compound; it is a failure of the scoring function, and the assay is what tells the two apart.

### 4.4 Mechanism

Avibactam binds the OXA-48 active site, acylates Ser70, and deacylates only exceptionally slowly, with the carbamylated Lys73 acting as the general base; desulfation of the bound DBO is also observed. Test for each link: (i) a nitrocefin-hydrolysis inhibition assay (with avibactam as the comparator) measures IC50 directly against the published mechanism; (ii) a mass-spectrometry acylation assay measures the acyl-enzyme formation rate and the deacylation rate — the numbers that actually decide whether a DBO beats avibactam; (iii) a checkerboard MIC assay of ceftazidime plus the candidate against an OXA-48-producing Klebsiella pneumoniae measures potentiation at matched concentration, with a cytotoxicity counter-screen; (iv) the same assay on OXA-163 and OXA-405 producers measures whether the candidate kept activity where the β5–β6 loop differs.

### 4.5 Testable hypotheses

1. Avibactam inhibits OXA-48 nitrocefin hydrolysis with an IC50 within 3-fold of its published value. Falsifier: IC50 > 3-fold worse than published.
2. A candidate DBO that out-scores avibactam on 4WMC acylates Ser70 at least as fast as avibactam and deacylates no faster. Falsifier: deacylation >10-fold faster than avibactam's.
3. The 4WMC pose predicts the loop effect: a candidate whose docked pose clashes with Arg214 loses activity against wild-type OXA-48 but keeps it against OXA-163. Falsifier: a candidate with an Arg214 clash keeps wild-type potency.

### 4.6 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): fix the pipeline query (hand-verify PDB title, mutations and bound ligands with a centre audit; exclude mutant structures from the benchmark) and re-run the ligand retrieval for OXA-48 to build the comparison set this paper could not — five ChEMBL DBO ligands with measured potency, docked on 4WMC at the audited centre, plus nacubactam docked on 4WMC as the known 80-fold-weaker control. Stage 2 (weeks 4–8): nitrocefin-hydrolysis inhibition assay for avibactam against its published mechanism, plus the best-scoring candidate from stage 1, on wild-type OXA-48. Stage 3 (weeks 9–12): if any candidate passes stages 1–2, mass-spectrometry acylation/deacylation assay plus a ceftazidime-potentiation MIC assay against an OXA-48 producer; if none passes, publish the negative result with the docking data as the reason the hypothesis failed. No animal work is proposed at this stage.

## 5. Limitations

1. Docking only, and non-covalent docking of a covalent inhibitor; no experimental data in this study. Vina noise ±1–2 kcal/mol swallows the reported margin.
2. The comparison set is a single compound — and it is a substrate, not an inhibitor — so the benchmark question is unanswerable in the form asked.
3. The pipeline's first structure (8PEB) was a quintuple mutant centred on a malonate ion; the scores on it are discarded — the centre audit is what separates the two.
4. One rigid structure was used (4WMC, wild-type OXA-48, 2.3 Å, eight chains); the β5–β6 loop is flexible, and the Arg214 loop effect was not docked.
5. Docking was on the wild-type structure only; the OXA-163/OXA-405 variant question — the one that changes DBO potency 80-fold — was not docked, because no variant structure with a candidate ligand was in the comparison set.
6. No data on the clinical confounder: docking cannot distinguish the ceftazidime–avibactam combination that works from the ceftazidime that fails, because the difference is the covalent step.
7. The classical-canon sweep found no OXA-48-relevant text: the Canon of Medicine treats wounds and fevers, not enzymes, so the Islamic-principle discussion rests on hifz al-nafs as a principle, not on a classical source about this target.

## 6. Conclusion

Avibactam, the diazabicyclooctane that acylates OXA-48's Ser70 and barely lets go, re-docks non-covalently at −6.73 kcal/mol on its own 2.3 Å structure 4WMC with a thin two-pose ensemble and no PAINS alert — a validated control, and a weak one by the only number this method can produce. Meropenem, the carbapenem substrate, "beats" it at −7.95 kcal/mol — but the margin lies inside Vina noise, the comparator is a molecule the enzyme destroys rather than one that blocks it, and avibactam's potency lives in the covalent step the score cannot see. The paper's useful result is therefore the control plus the named failure: the method works on the right structure, the question was the wrong one, and the fix — covalent docking or an acylation assay, a real inhibitor comparison set, and a hand-verified wild-type structure — is specified so the next run can ask the question this one could not. What the docking cannot do is resolve the covalent question that defines this drug: the same active site that binds avibactam at −6.73 kcal/mol is the site where Ser70 acylation and slow deacylation decide whether a DBO works, and only an acylation assay can tell whether a successor keeps avibactam's barrier. The next step is the cheap, decisive test — fix the query, build the inhibitor comparison set, and run a nitrocefin assay plus an acylation-rate measurement — not another non-covalent docking run on an unverified structure.

## 7. Policy implications

**Decision-maker:** Pakistan's Drug Regulatory Authority (DRAP) and the National Institute of Health's antimicrobial-resistance programme, with the SMBBMU ORIC office as the local route. **Decision:** whether to fund a small, targeted validation of DBO inhibition as an academic drug-discovery exercise, and whether to prioritise ceftazidime–avibactam in procurement for carbapenem-resistant Enterobacterales. **Exact change:** commission the 8–12-week pipeline-fix plus nitrocefin screen proposed in §4.6 for the five best ChEMBL DBO ligands against avibactam, with nacubactam as the known weaker control, instead of funding another purely computational screen of the same target on unverified structures; and, in parallel, ask the AMR programme to note explicitly that the binding question is settled for the wild-type active site — avibactam re-docks at −6.73 kcal/mol — and that the remaining gap is the covalent step and the variant loop, not the drug's non-covalent affinity: every rupee spent re-docking avibactam into a mutant enzyme is a rupee not spent measuring acylation rates. **If evidence Z appears, reverse this:** if a candidate beats avibactam's acylation rate and deacylates no faster in the mass-spectrometry assay, drop the access-only framing and fund the candidate's development; if the fixed query returns no DBO within noise of avibactam, drop this ligand set and redirect the same screen to the next DBO chemotypes — do not proceed to any animal or clinical work on docking scores alone. The Islamic principle is hifz al-nafs (preservation of life, a maqsad of the Sharia): where a cheap test can distinguish a usable OXA-48 inhibitor from a useless one for a resistance mechanism that defeats the drugs of last resort, running the test is the obligation; prescribing on an untested docking score would violate it. The evidence here is thin — docking only, and a single-substrate comparison at that — so the recommendation is "run the trial", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Antimicrobial Resistance Collaborators. Global burden of bacterial antimicrobial resistance in 2019: a systematic analysis. Lancet. 2022;399:629-655.
2. Lahiri SD, et al. Molecular basis of selective inhibition and slow reversibility of avibactam against class D carbapenemases: a structure-guided study of OXA-24 and OXA-48. ACS Chem Biol. 2015;10:591-600. doi:10.1021/cb500703p. PMID: 25406838.
3. Hoff JF, et al. Electrostatic interactions influence diazabicyclooctane inhibitor potency against OXA-48-like β-lactamases. RSC Med Chem. 2025;16:5441-5455. doi:10.1039/d5md00512d. PMID: 40927637.
4. Frohlich C, et al. Epistasis arises from shifting the rate-limiting step during enzyme evolution of a beta-lactamase. Nat Catal. 2024;7:499-509. doi:10.1038/s41929-024-01117-4. PMID: 38828429.
5. RCSB PDB entry 4WMC: OXA-48 covalent complex with avibactam inhibitor, 2.3 Å. RCSB Protein Data Bank. Accessed 2026-11-23.
6. RCSB PDB entry 8PEB: OXA-48_Q5 (directed-evolution quintuple mutant). RCSB Protein Data Bank. Accessed 2026-11-23.
7. ChEMBL target CHEMBL1287604: Beta-lactamase OXA-48, Klebsiella pneumoniae. ChEMBL database, European Bioinformatics Institute. Accessed 2026-11-23.
8. UniProtKB Q6XEC0: Beta-lactamase OXA-48, Klebsiella pneumoniae. UniProt. Accessed 2026-11-23.
9. PubChem CID 9835049: avibactam. National Library of Medicine. Accessed 2026-11-23.
10. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; treats wounds and fevers — cited for the hifz al-nafs principle only.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-063-4wmc-2026-11-23.json` (avibactam + meropenem on 4WMC) and `hidden_files/dock-HP-063-2026-11-23.json` (Q6XEC0 pipeline run, including the discarded 8PEB docking step). Reference inhibitor avibactam (PubChem CID 9835049); comparator meropenem (CHEMBL127, Kd 850 nM). Structure: PDB 4WMC (2.3 Å); discarded structure PDB 8PEB (OXA-48_Q5 quintuple mutant). Target: UniProtKB Q6XEC0; ChEMBL target CHEMBL1287604. No additional data were generated.
