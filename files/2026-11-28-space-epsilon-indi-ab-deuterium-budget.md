# Thirty Earth Masses of Interstellar Ice: The Deuterium Budget of ε Indi Ab and a Decisive Test of Cold Accretion

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent verification.**

**Author:** Zubair Ali, Pharm-D student, SMBBMU Larkana, Pakistan (ORCID: 0009-0001-5921-7509)
**Drafting assistant:** Lapis (AI)
**Date:** 28 November 2026 | **Field:** Space (astronomy / exoplanets) | **Series:** Daily Research Papers, Space #7

---

## Abstract

The James Webb Space Telescope has measured the deuterium-to-hydrogen ratio (D/H) of a mature giant exoplanet for the first time: ε Indi Ab, the nearest directly imaged exoplanet (3.6 pc), shows D/H = (4.4 ± 0.7) × 10⁻⁵ from a 48σ detection of deuterated methane (CH₃D) — twice the protosolar value and identical, within errors, to Uranus. We compute the deuterium budget this measurement implies. The excess over the protosolar baseline is Δ(D/H) = (2.3 ± 0.9) × 10⁻⁵, corresponding to 0.067 ± 0.025 Earth masses of excess deuterium in the planet. If ε Indi Ab is fully mixed and its solids carried the minimum D/H of ≳1% required by Xuan et al. (2026), the planet must have accreted **30.4 ± 11.4 Earth masses of pristine interstellar water ice** (60.7 Earth masses of 50%-ice solids) — a solid-accretion budget comparable to the entire heavy-element inventory of Jupiter. If the accreted solids were as deuterium-rich as the interstellar comet 3I/ATLAS (CH₄ D/H = 3.18%), the requirement falls to 9.5 ± 3.6 Earth masses of ice; if the enrichment is confined to the outer envelope, it falls to ~3 Earth masses. **Falsifiable claim:** ε Indi Ab's enrichment is either a bulk property produced by massive cold accretion or a skin-deep atmospheric property produced by incomplete mixing — and the two are separable. **Falsifier:** a bulk D/H measurement of ε Indi Ab from HD at the protosolar value (≤2.5 × 10⁻⁵) falsifies the fully-mixed interpretation; a second cold directly imaged giant with protosolar D/H falsifies the claim that cold accretion always enriches. **Causal identification: association only** — this is a comparative synthesis of published observations plus a new mass-budget computation, not an experiment. **The memorable number: 30 Earth masses of ice** — the minimum interstellar ice a fully mixed ε Indi Ab must have swallowed.

**Keywords:** exoplanets; ε Indi Ab; deuterium; D/H ratio; JWST; planet formation; interstellar comets; 3I/ATLAS; cold accretion

---

## 1. Introduction

Deuterium is the only element whose abundance was fixed entirely in the first minutes of the Universe and then only destroyed, never created, by stars. Its ratio to hydrogen (D/H) is therefore a fossil: gas that has never been inside a star carries the primordial value, while material processed at temperatures below ~30 K in prestellar cores is enriched by orders of magnitude through H₂D⁺ ion–molecule chemistry. In the Solar System this fossil has already told a two-part story. The gas giants Jupiter and Saturn carry near-protosolar D/H — Jupiter (2.25 ± 0.35) × 10⁻⁵ (Lellouch et al. 2001) against a protosolar (2.1 ± 0.5) × 10⁻⁵ (Geiss & Gloeckler 1998) — because they are mostly nebular gas. The ice giants Uranus and Neptune carry (4.4 ± 0.4) × 10⁻⁵ and (4.1 ± 0.4) × 10⁻⁵ (Feuchtgruber et al. 2013): twice the protosolar value, because a large fraction of their mass is ice accreted as solids. Until November 2026, no D/H value existed for any planet outside the Solar System.

That changed on 6 November 2026, when Xuan et al. (arXiv:2611.10129) reported a 48σ detection of deuterated methane (CH₃D) in ε Indi Ab with JWST, measuring D/H = (4.4 ± 0.7) × 10⁻⁵ — the same number as Uranus, in a planet ~100 times more massive. ε Indi Ab is the nearest directly imaged exoplanet (3.6 pc, ~11.9 light-years) and the coolest (~275 K), a 6.5-Jupiter-mass super-Jupiter on a wide, eccentric orbit (Sanghi et al. 2026; Matthews et al. 2024). Xuan et al. concluded the planet "accreted solids with D/H ≳ 1%, at least 30 times more deuterium-rich than typical Solar System comets", and noted that such values are found in the interstellar comet 3I/ATLAS and in organic molecules in star-forming regions.

This paper asks the quantitative question Xuan et al. left open: **how much** D-rich solid must ε Indi Ab have accreted? The answer turns a striking measurement into a testable fork in planet-formation theory. The same deuterium ladder this series built for interstellar comets (Ali 2026, 19 November: 3I/ATLAS water D/H = 0.98%, methane D/H = 3.18% — the highest ever measured) now extends to a planet: the comet's ices and the planet's atmosphere may be two ends of one cold-accretion process, or the planet's enrichment may be only skin deep.

### 1.1 The Islamic canon on this question

The method of this paper — measure precisely, then reason from the measurement — is the method of Ibn al-Haytham's *Kitab al-Manazir* (Book of Optics, c. 1011–1021), which founded the experimental method on controlled observation of light. The measurement tradition it belongs to runs through Al-Battani's *Kitab al-Zij* (c. 900), which fixed the solar year to within ~2 minutes, and Al-Biruni's *Al-Qanun al-Mas'udi* (c. 1030s), which measured the Earth's circumference to within ~1% and treated planetary motion quantitatively; Al-Tusi's *Tadhkira fi 'Ilm al-Hay'a* (13th century) supplied the Tusi couple later used by Copernicus. The Qur'an frames this observation as a duty of attention to "signs in the horizons" (Qur'an 41:53, Surah Fussilat; Sahih International translation: "We will show them Our signs in the horizons and within themselves until it becomes clear to them that it is the truth"), and describes the stars as the adornment of the nearest heaven (Qur'an 67:5, Surah Al-Mulk). Guessoum (2011, *Islam's Quantum Question*) treats such measurement as continuous with, not separate from, the Islamic intellectual tradition. These works were consulted through the programme's verified literature map, not read in full Arabic (see Limitations).

---

## 2. Methods

**Analysis plan (stated before results).** Before computing anything, the plan was: (1) tabulate every published D/H value for ε Indi Ab, the Solar System giants, the protosolar nebula, VSMOW, and 3I/ATLAS, with uncertainties, from peer-reviewed or arXiv sources only; (2) compute the excess D/H of ε Indi Ab over the protosolar baseline with propagated uncertainty; (3) convert the excess to an excess deuterium mass assuming a hydrogen mass fraction f_H = 0.71 (solar composition) and the dynamical mass M_p = 6.5 M_Jup (Sanghi et al. 2026); (4) convert that mass to a required mass of accreted water ice under three stated solids-D/H scenarios (1% — the Xuan et al. lower bound; 3.18% — the 3I/ATLAS methane value; 0.98% — the 3I/ATLAS water value) and one mixing scenario (envelope-only, outer 10% of mass); (5) compare against the strongest incumbent interpretations and state the falsifier. No post-hoc redefinition of scenarios was performed after seeing the numbers.

**Literature sweep.** (a) Modern literature: targeted searches of arXiv (astro-ph.EP) and journal/news sources for ε Indi Ab and D/H results published October–November 2026; the daily research digest (last available 14 November 2026) is bio/health-focused and contained no space items, so the space literature was swept directly. (b) Islamic canon: Al-Biruni, *Al-Qanun al-Mas'udi* and *Kitab al-Hind*; Al-Battani, *Kitab al-Zij*; Ibn al-Haytham, *Kitab al-Manazir*; Al-Tusi, *Tadhkira*; Guessoum (2011); Nasr, *Man and Nature* (1968). (c) Method standard: the policy-shaping professors' checklist (Banerjee & Duflo; Acemoglu, Johnson & Robinson; Chetty; Thaler & Sunstein; Heckman; Hanushek; Rodrik; Deaton; Haynes & Gawande; Pacala & Socolow; Allen) — one falsifiable claim, named falsifier, mechanism, effect size with uncertainty, comparison against the strongest incumbent, one memorable number.

**Computation.** All arithmetic was performed in Python 3 from the published values; the equations are:

- Excess D/H: Δ = (D/H)_obs − (D/H)_proto, σ_Δ = √(σ_obs² + σ_proto²).
- Hydrogen atoms: N_H = f_H · M_p / m_H.
- Excess deuterium mass: M_D = Δ · N_H · m_D.
- Ice mass required: M_ice = M_D / [ (D/H)_solids · (2/18) · (m_D/m_H) ], where 2/18 is the hydrogen mass fraction of water and m_D/m_H ≈ 2.
- Constants: M_Jup = 1.8982 × 10²⁷ kg; M_Earth = 5.9722 × 10²⁴ kg; m_H = 1.6735 × 10⁻²⁷ kg; m_D = 3.3436 × 10⁻²⁷ kg.

The result is insensitive to f_H within its plausible range (0.68–0.75 changes M_ice by <6%); the dominant uncertainty is the D/H measurement error (±37% on Δ).

---

## 3. Results

### 3.1 The deuterium ladder, extended to a planet

| Reservoir | D/H | Source |
|---|---|---|
| Protosolar nebula | (2.1 ± 0.5) × 10⁻⁵ | Geiss & Gloeckler 1998 |
| Jupiter | (2.25 ± 0.35) × 10⁻⁵ | Lellouch et al. 2001 |
| Saturn | ~1.7 × 10⁻⁵ | Lellouch et al. 2001 |
| Uranus | (4.4 ± 0.4) × 10⁻⁵ | Feuchtgruber et al. 2013 |
| Neptune | (4.1 ± 0.4) × 10⁻⁵ | Feuchtgruber et al. 2013 |
| **ε Indi Ab (this work's subject)** | **(4.4 ± 0.7) × 10⁻⁵** | **Xuan et al. 2026** |
| 3I/ATLAS, water | (0.98 ± 0.06)% | Cordiner et al. 2026 |
| 3I/ATLAS, methane | (3.18 ± 0.30)% | Roth et al. 2026 |
| VSMOW (Earth ocean water) | 1.5576 × 10⁻⁴ | Standard |
| Typical Solar System comet, water | ~3 × 10⁻⁴ | Bockelée-Morvan et al. |

ε Indi Ab's D/H is **2.10× the protosolar value**, **1.96× Jupiter's**, and **1.00× Uranus's** — identical to an ice giant, in a planet 6.5 times Jupiter's mass. The protosolar null hypothesis (no enrichment) is excluded at 2.7σ: (4.4 − 2.1) / √(0.7² + 0.5²) = 2.7. The CH₃D detection itself is 48σ; the limiting uncertainty is the retrieval, not the detection.

### 3.2 The deuterium budget

For M_p = 6.5 M_Jup (2,066 M_Earth) and f_H = 0.71, the planet holds 5.24 × 10⁵⁴ hydrogen atoms. The excess over protosolar is Δ(D/H) = (2.3 ± 0.9) × 10⁻⁵, i.e. **0.067 ± 0.025 Earth masses of excess deuterium**.

| Scenario | Solids D/H | Ice required (M_Earth) | 50%-ice solids (M_Earth) |
|---|---|---|---|
| A. Fully mixed, Xuan lower bound | ≥1% | **30.4 ± 11.4** | 60.7 ± 22.8 |
| B. Fully mixed, 3I/ATLAS-methane solids | 3.18% | 9.5 ± 3.6 | 19.1 ± 7.2 |
| C. Fully mixed, 3I/ATLAS-water solids | 0.98% | 31.0 ± 11.6 | 62.0 ± 23.2 |
| D. Envelope-only (outer 10% of mass), 1% solids | 1% | ~3.0 | ~6.1 |

Scenario A is the headline: a fully mixed ε Indi Ab needs **~30 Earth masses of pristine interstellar ice** — and ~61 Earth masses of realistic 50%-ice planetesimals — to carry its deuterium excess. That is comparable to, or larger than, the entire heavy-element inventory of Jupiter. Scenario B shows the escape hatch: if the accreted solids were as extreme as 3I/ATLAS methane, the bill falls to ~10 Earth masses of ice. Scenario D shows the other escape hatch: if the deuterium never mixed into the deep interior, ~3 Earth masses of ice in the envelope suffices.

### 3.3 Comparison against the strongest incumbent

The strongest incumbent interpretation is the Feuchtgruber et al. (2013) ice-giant picture: Uranus and Neptune are fully mixed, their atmospheric D/H reflects their bulk, and their ice mass fraction is 14–32% — which forced the conclusion that they are rock-dominated, not ice-dominated. Applied to ε Indi Ab, the same fully-mixed logic demands an ice budget (Scenario A) that is ~1.5% of the planet's total mass — a modest fraction of the planet, but an absolute mass of solids that strains core-accretion budgets for a planet that formed around a K-dwarf with a presumably modest disk. The incumbent's own logic therefore generates the tension this paper quantifies: either ε Indi Ab's disk was extraordinarily rich in cold solids, or the fully-mixed assumption that worked for Uranus and Neptune fails for a super-Jupiter. The second-strongest incumbent — the "Jupiter-like" picture, in which a giant planet's D/H stays near protosolar because it is mostly nebular gas — is already excluded at 2.7σ by the measurement itself.

---

## 4. Discussion

### 4.1 Mechanism

The mechanism is the same H₂D⁺ ion–molecule chemistry that deuterated 3I/ATLAS: below ~30 K, the reaction H₃⁺ + HD → H₂D⁺ + H₂ runs forward, and H₂D⁺ passes its deuterium into water and methane ices. The ices that fed ε Indi Ab must have formed, or been stored, in such a cold environment — a prestellar core or the far outer disk — and survived incorporation into the planet without being thermally reset. Two links in this chain are directly testable: (i) the CH₄/H₂O deuteration ratio should be preserved from the source ices (as it was in 3I/ATLAS, where CH₄/H₂O D/H ≈ 3.24, matching comet 67P's ratio within a factor of 1.4); (ii) the planet's heavy elements (C, O, N, S) are uniformly enriched to about Jupiter's level (Xuan et al. 2026), consistent with solid accretion rather than pure gas capture. A measurement of ε Indi Ab's water D/H would test link (i) immediately: if its CH₄/H₂O D/H ratio matches 3I/ATLAS's 3.24, the shared-mechanism case strengthens; if it is near 1, the methane and water took different paths.

### 4.2 What the budget means

The 30-Earth-mass number is a lower bound in one sense and an upper bound in another. It is a lower bound because Xuan et al.'s ≳1% is itself a lower bound on the solids' D/H — the true solids could have been less enriched, which would raise the required ice mass further. It is an upper bound because it assumes the enrichment is spread through the whole 6.5-Jupiter-mass interior; giant planets are not necessarily fully mixed, and if ε Indi Ab's interior is layered, the same atmospheric D/H can be produced by a few Earth masses of ice (Scenario D). This is not a weakness of the analysis — it is the point. The budget converts one atmospheric number into a fork with two branches, and each branch has a distinct observable consequence: bulk HD spectroscopy separates them.

### 4.3 The population test

ε Indi Ab is one object. The claim "cold accretion enriches giant planets" becomes a population claim only with a second and third D/H measurement. The natural next targets are the other directly imaged cold giants already in the JWST archive — 51 Eridani b (recovered in November 2026 from two-year-old JWST data by the FLIP glare-removal method, Ferrer-Chavez et al. 2026, *Nature*, doi:10.1038/s41586-026-11213-z, which improved sensitivity 2–15×) and the HR 8799 planets. The prediction, stated before those measurements: a cold (T < 300 K) giant that formed beyond the CO snowline and accreted ≥20 Earth masses of cold solids will show D/H ≥ 3.5 × 10⁻⁵; a warm giant formed inside the water snowline will show protosolar D/H (~2 × 10⁻⁵). A single cold giant at protosolar D/H falsifies the universal version of the claim.

---

## 5. Limitations

1. **One object.** Every population inference rests on a single D/H measurement. The 2.7σ exclusion of the protosolar null is suggestive, not decisive; a 1σ downward shift in the retrieval would halve the ice budget.
2. **Retrieval systematics.** The D/H value comes from a CH₃D retrieval against a modelled atmosphere; unmodelled clouds (Matthews et al. 2026 report thick water-ice clouds on this planet) or an incorrect temperature profile can bias the abundance. The 48σ figure is detection significance, not accuracy.
3. **Mixing assumed, not measured.** Scenarios A–C assume complete mixing; Scenario D assumes none. The truth is between them and currently unmeasurable — HD spectroscopy is the missing observation, and no HD measurement of ε Indi Ab exists yet.
4. **Mass and composition assumptions.** The budget uses M_p = 6.5 M_Jup (Sanghi et al. 2026); Matthews et al. (2026) prefer 7.6 ± 0.7 M_Jup, which would raise the ice budget by ~17%. The hydrogen fraction f_H = 0.71 is a solar-composition assumption; the planet's measured metal enrichment would lower it slightly. Both effects are smaller than the D/H uncertainty.
5. **Age uncertainty.** The host star's age (3.5 ± 1.0 Gyr) affects evolutionary-model radii but not the budget, which depends on mass, not radius.
6. **Islamic canon gap (stated honestly).** Al-Biruni's *Al-Qanun al-Mas'udi*, Al-Battani's *Kitab al-Zij* and Al-Tusi's *Tadhkira* were consulted through the programme's verified literature map and secondary literature, not read in full in the original Arabic: no complete modern English translation of *Al-Qanun al-Mas'udi* or *Kitab al-Zij* is freely available, and many classical Arabic astronomical manuscripts remain undigitised in libraries (Süleymaniye, Istanbul; Dar al-Kutub, Cairo; the British Library). The method ancestry claimed here is therefore a documented lineage, not a first-hand textual reading.
7. **Digest gap.** The daily research digest (last available 14 November 2026) is bio/health-focused and contained no space items; the literature sweep for this paper was direct (arXiv + journals), not digest-based.

---

## 6. Policy implications

**Decision-maker:** the Chairman of SUPARCO (Pakistan Space and Upper Atmosphere Research Commission) and the Chairman of the Higher Education Commission (HEC), jointly.

**Exact change:** establish a **JWST Archival D/H Programme** inside Pakistan's national space science effort, with two funded deliverables in 2027: (1) reprocess the public JWST/MIRI + NIRSpec archive for ε Indi Ab (CH₃D at additional bands and a first HD bulk-D/H attempt) using the FLIP-class glare-removal methods now published; (2) submit one JWST Cycle 5 archival proposal to measure D/H in a second cold giant (51 Eridani b or HR 8799 c). The cost is analyst time, not telescope time: JWST archival data are public in MAST, and the FLIP result proves that new science can be extracted from data already taken. A programme of 3–5 analysts is a rounding error in SUPARCO's budget and produces citable, first-author science for Pakistani institutions.

**Islamic principle.** The programme is an act of *'ilm* (seeking knowledge): the Qur'an directs attention to "signs in the horizons" (41:53) and presents the stars as the adornment of the nearest heaven (67:5). It is also *maslaha* (public interest, Al-Shatibi, *Al-Muwafaqat*): public money is spent on analysis of a shared human trust — open telescope data — rather than on duplicating hardware, and the benefit accrues to students and researchers who could never afford telescope time. The stewardship frame (*khilafah*, Qur'an 2:30; Nasr, *Man and Nature*, 1968) applies here to data as much as to nature: a public archive is a trust, and leaving it unmined is the waste of a trust.

**Falsifier for the policy itself:** if, after two funded years, the programme produces no peer-reviewed D/H result and no accepted archival proposal, the funding should be redirected to instrument-adjacent work (e.g. detector or data-pipeline training) rather than continued. If the evidence is thin, the recommendation is "run the analysis", not "build the telescope".

---

## 7. Conclusion

ε Indi Ab carries twice the deuterium of the Sun — the first D/H measurement of any exoplanet, and a number identical to Uranus in a planet a hundred times more massive. We have turned that number into a mass budget: **30.4 ± 11.4 Earth masses of pristine interstellar ice** if the planet is fully mixed and its solids were at the minimum enrichment the data require; ~10 Earth masses if its solids were as extreme as 3I/ATLAS; ~3 Earth masses if the enrichment never left the envelope. The measurement excludes a purely nebular origin at 2.7σ and strains the fully-mixed ice-giant picture that worked for Uranus and Neptune. The fork is decidable: bulk HD spectroscopy of ε Indi Ab, and D/H in the next cold giant, will say whether giant planets are enriched through and through or only skin deep. Until then, the cheapest decisive science Pakistan can buy in astronomy is not a telescope — it is the reprocessing of data humanity has already taken.

---

## References

1. Xuan, J. W., et al. 2026, "The deuterium-rich atmosphere of a mature super-Jupiter", arXiv:2611.10129 (submitted 6 Nov 2026, under review).
2. Sanghi, A., et al. 2026, "Worlds Next Door. IV. Mapping the Late Stages of Giant Planet Evolution with a Precise Dynamical Mass and Luminosity for ε Ind Ab", arXiv:2603.08787.
3. Matthews, E. C., et al. 2024, "A temperate super-Jupiter imaged with JWST in the mid-infrared", *Nature* 633, 789–792. doi:10.1038/s41586-024-07837-8.
4. Matthews, E. C., et al. 2026, "A second visit to ε Ind Ab with JWST: new photometry confirms ammonia and suggests thick clouds in the exoplanet atmosphere of the closest super-Jupiter", *Astrophysical Journal Letters*.
5. Feuchtgruber, H., et al. 2013, "The D/H ratio in the atmospheres of Uranus and Neptune from Herschel-PACS observations", *Astronomy & Astrophysics* 551, A126.
6. Lellouch, E., et al. 2001, *Astronomy & Astrophysics* — D/H in Jupiter (2.25 ± 0.35) × 10⁻⁵ and Saturn, from ISO-SWS observations (values as compiled in Feuchtgruber et al. 2013).
7. Geiss, J., & Gloeckler, G. 1998, "Abundances of deuterium and helium-3 in the protosolar cloud", *Space Science Reviews* 84 — protosolar D/H (2.1 ± 0.5) × 10⁻⁵.
8. Cordiner, M. A., et al. 2026, "Interstellar comet 3I/ATLAS water D/H", *Nature* 655, 870–874.
9. Roth, N. X., et al. 2026, "Methane D/H in interstellar comet 3I/ATLAS", *Nature Astronomy*.
10. Ali, Z. 2026, "One Hydrogen Atom in Thirty-One: The Deuterium Ladder of Interstellar Comets and a Two-Population Test for the Rubin Era", Daily Research Papers series, 19 November 2026 (internal series manuscript).
11. Ferrer-Chavez, R., et al. 2026, "Imaging exoplanets below the telescope stability limit", *Nature*. doi:10.1038/s41586-026-11213-z.
12. Al-Biruni, *Al-Qanun al-Mas'udi* (c. 1030s); *Kitab al-Hind* (c. 1030).
13. Al-Battani, *Kitab al-Zij* (c. 900).
14. Ibn al-Haytham, *Kitab al-Manazir* (Book of Optics, c. 1011–1021).
15. Al-Tusi, Nasir al-Din, *Tadhkira fi 'Ilm al-Hay'a* (13th century).
16. Guessoum, N. 2011, *Islam's Quantum Question: Reconciling Muslim Tradition and Modern Science*.
17. Nasr, S. H. 1968, *Man and Nature: The Spiritual Crisis of Modern Man*. London: George Allen & Unwin.
18. The Qur'an 41:53 (Surah Fussilat) and 67:5 (Surah Al-Mulk), Sahih International translation.
19. Al-Shatibi, *Al-Muwafaqat* (maslaha / maqasid al-shariah).

---

## Data availability

All input values are published: Xuan et al. 2026 (arXiv:2611.10129); Sanghi et al. 2026 (arXiv:2603.08787); Matthews et al. 2024 (*Nature* 633, 789–792); Feuchtgruber et al. 2013 (A&A 551, A126); Cordiner et al. 2026 and Roth et al. 2026 (3I/ATLAS isotope values, via the series manuscript of 19 November 2026). No new observations are presented. The deuterium-budget computation is fully specified by the equations in §2 and the constants listed there; it can be reproduced in any scripting language from the table in §3.1. JWST data for ε Indi Ab are public in the Mikulski Archive for Space Telescopes (MAST).

---

*AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent verification. Never submit or publish anywhere without the author's full read-through and approval. The Harvard/MIT/Oxford scholars named in the method brief are the standard for this work, not co-authors; no endorsement is claimed.*
