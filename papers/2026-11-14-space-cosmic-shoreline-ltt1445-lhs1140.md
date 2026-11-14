# Pinning the Cosmic Shoreline with JWST: LTT 1445 A b and c Are Airless Above the Line, LHS 1140 b Keeps Its Helium Below It

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent verification.**

**Author:** Zubair Ali, Pharm-D student, SMBBMU Larkana, Pakistan — ORCID: 0009-0001-5921-7509
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-14
**Field:** Space (astronomy / exoplanet atmospheres)

---

## Abstract

Two results published in November 2026 test the cosmic shoreline — the I ∝ v_esc^4 boundary that separates rocky planets with atmospheres from airless worlds — from opposite sides. The JWST Rocky Worlds programme reports MIRI/F1500W secondary eclipses of LTT 1445 A b and c (Ih et al., arXiv:2611.17300): eclipse depths of 157(+18/−17) and 154(+54/−37) ppm give 15-µm brightness temperatures of 528(+39/−29) K and 625(+109/−79) K, both consistent with dark bare rock; for b, CO2 partial pressure is <0.6 mbar and surface pressure ≲0.1 bar. LTT 1445 A b is the closest planet to the shoreline yet observed in eclipse. In the same week, ground-based spectroscopy reported metastable helium escaping from the habitable-zone super-Earth LHS 1140 b in 2024 but not in 2025 (Cherubim et al., Science 2026), while four JWST NIRISS transits rule out helium at the reported level (Radica 2026; Bennett et al. 2026). We place all three planets on the classical Mars-anchored XUV shoreline, I_XUV = (a⊕/a)^2 (L*/L⊙)^0.4, and find LTT 1445 A b 2.3× above the line, LTT 1445 A c 11.9× above it, and LHS 1140 b 8.5× below it — every planet on its predicted side. The two results bracket the shoreline zero point to log10 I_XUV = 4 log10 v_esc + D with D in [−4.10, −2.81], against the canonical −3.17. We state this as a falsifiable claim: any substantial atmosphere found on a rocky planet more than 0.36 dex above the classical line, or any bare rock more than 0.93 dex below it, falsifies the classical zero point; simultaneous ground- and space-based helium transits of LHS 1140 b will decide whether its lower bound stands.

**Keywords:** exoplanet atmospheres; cosmic shoreline; atmospheric escape; JWST; M dwarfs; LTT 1445; LHS 1140 b; helium

---

## 1. Introduction

Which rocky planets keep their atmospheres? The question decides where habitable worlds can exist, and for a decade the organising idea has been the "cosmic shoreline" of Zahnle & Catling (2017): when Solar System bodies are arranged by escape velocity (v_esc) against the radiation they receive, a single straight line of slope four on logarithmic axes, I ∝ v_esc^4, separates the bodies with atmospheres from those without. The line is now the target-selection metric for the largest rocky-atmosphere survey ever attempted — the JWST Rocky Worlds Director's Discretionary Time (DDT) programme, 500 hours of JWST time plus 240 Hubble orbits, which uses secondary-eclipse photometry to test, planet by planet, whether rocky worlds around M dwarfs retain atmospheres (Ji et al. 2025).

Two results published within days of each other in November 2026 test the shoreline from opposite sides, and both concern the nearest rocky systems known. First, the Rocky Worlds programme reports MIRI/F1500W (15 µm) secondary eclipses of LTT 1445 A b and c, the transiting rocky siblings in the nearest M-dwarf system (6.9 pc): both planets are consistent with dark bare rock, and planet b — the closest planet to the canonical XUV-driven shoreline yet observed in eclipse — has no substantial atmosphere (Ih et al. 2026). Second, ground-based high-resolution spectroscopy reports metastable helium escaping from LHS 1140 b, a temperate super-Earth in the habitable zone of its M dwarf, detected in 2024 but not in 2025 (Cherubim et al. 2026), while four archival JWST NIRISS transits spanning December 2023 to July 2026 find no helium absorption at the reported level (Radica 2026; Bennett et al. 2026) — a dispute covered the same week in *Nature Astronomy* (Maltagliati 2026).

This paper does the quantitative step neither result takes on its own: it places all three planets on the same classical shoreline, using the published cumulative-XUV scaling, and derives the numerical bracket the two results jointly impose on the shoreline's zero point. The shoreline's slope is fixed by energy-limited escape physics; its height — the zero point — was set in 2017 by a single Solar System anchor, Mars, and has never been tested by exoplanets on both sides at once. These three planets now test it from both sides.

## 2. Methods

### 2.1 Literature sweep

The daily research digest for 2026-11-14 (health-focused; no space entries) was read, and targeted searches were run on arXiv (astro-ph.EP) and in the press for exoplanet-atmosphere results dated 10–14 November 2026. Every cited result was verified against its arXiv record or publisher page: the LTT 1445 paper (arXiv:2611.17300, submitted 12 November 2026), the LHS 1140 b helium detection (arXiv:2607.14326) and its two JWST follow-ups (arXiv:2608.13470; arXiv:2608.13473), and the *Nature Astronomy* News & Views piece (DOI 10.1038/s41550-026-03029-8, published 13 November 2026). No citation, number, or identifier in this manuscript is invented; where a number is our own derivation, the formula and inputs are shown in full.

### 2.2 The shoreline calculation (own analysis)

**Escape velocity.** v_esc = √(2GM_p/R_p), computed from published masses and radii relative to Earth (v_esc,⊕ = 11.186 km/s).

**Cumulative XUV instellation.** Following Zahnle & Catling (2017, Eq. 27), as restated by Meni-Gallardo & Pallé (2026):

I_XUV = (a⊕ / a)^2 × (L* / L⊙)^0.4

in Earth units, where a is the planet's semi-major axis and L* the stellar luminosity. This is the total stellar XUV flux integrated over the planet's lifetime, not the present-day bolometric insolation — the distinction matters for M dwarfs, whose long pre-main-sequence and flare activity make their cumulative XUV far larger than their present-day brightness suggests.

**Shoreline and zero point.** The classical shoreline is log10 I_XUV = 4 log10 v_esc + D. The zero point D was fixed by Zahnle & Catling by assuming Mars marks the boundary between worlds with and without atmospheres. We adopt that convention exactly: the shoreline passes through Mars's (v_esc, I_XUV) point, giving D = −3.17 (Mars: v_esc = 5.03 km/s, a = 1.524 AU, L* = L⊙, I_XUV = 0.43). A planet's shoreline distance is Δ = log10(I_XUV / I_XUV,shore), positive above the line (airless side), negative below it (retaining side).

**Dayside temperature scale.** For reference, the maximum dayside temperature for instant reradiation with zero albedo is T_day,max = T_eq × 4^(1/4), where T_eq is the zero-albedo equilibrium temperature. The observed 15-µm brightness temperature is a band temperature, not a bolometric dayside temperature, so ratios against T_day,max are reported as a scale comparison only; the papers' own conclusion ("consistent with the dark, bare rock limit") is what we rely on.

**Inputs.** LTT 1445 A b/c masses, radii, semi-major axes, instellations and equilibrium temperatures are from Pass et al. (2023, HST/WFC3 joint fit): b, M = 2.73 M⊕, R = 1.34 R⊕, a = 0.03813 AU, S = 5.7 S⊕, T_eq = 431 K; c, M = 1.37 ± 0.19 M⊕, R = 1.07 R⊕, a = 0.02659 AU, S = 11.7 S⊕, T_eq = 516 K; stellar luminosity L* = 0.00805 L⊙. LHS 1140 b uses the most precise values to date (Cherubim et al. 2026): M = 5.60 ± 0.19 M⊕, R = 1.730 ± 0.025 R⊕; with system parameters from Ment et al. (2019): a = 0.0936 AU, L* = 0.00441 L⊙, S = 0.503 S⊕, T_eq = 230 K. All arithmetic was computed in Python 3 and is reproducible from the formulae above.

**Robustness checks.** (i) Using the earlier Winters et al. (2022) masses and radii for LTT 1445 A b/c (M = 2.87/1.54 M⊕, R = 1.305/1.147 R⊕) changes the shoreline ratios from 2.29 to 1.96 (b) and 11.91 to 10.83 (c) — no conclusion changes. (ii) Pass et al. (2025), as summarised by Ji et al. (2025), revised cumulative XUV fluxes for mid-to-late M dwarfs upward by roughly a factor of 3 (pre-main-sequence plus flares); we repeat the calculation with I_XUV × 3 as a sensitivity test.

## 3. Results

### 3.1 LTT 1445 A b and c: bare rock at the shoreline

Ih et al. (2026) present Rocky Worlds DDT MIRI/F1500W observations of LTT 1445 A b and c — two eclipses of each planet across three visits — with three independent reductions and a joint fit including all existing JWST data and 220 radial velocities, improving the precision on planetary radii, masses, and orbital parameters by factors of 1.6–2.3. They measure eclipse depths of 157(+18/−17) ppm (b) and 154(+54/−37) ppm (c), corresponding to 15-µm brightness temperatures of 528(+39/−29) K and 625(+109/−79) K, both consistent with the dark, bare-rock limit. For planet b, combining these data with the archival MIRI/LRS spectrum in a Bayesian retrieval limits the CO2 partial pressure to <0.6 mbar and the surface pressure to ≲0.1 bar, while forward models exclude thick aerosol layers that could mimic a bare surface in transmission; the authors conclude planet b has no substantial atmosphere. For planet c, a potentially grazing eclipse and overlapping events leave the depth poorly constrained, and the data rule out only thick, CO2-bearing atmospheres (≳1 bar with ≥1% CO2). The paper states explicitly that LTT 1445 A b is the planet closest to the canonical XUV-driven Cosmic Shoreline observed in eclipse so far, and that its lack of a substantial atmosphere implies the shoreline cannot lie much farther toward the airless side than nominally predicted. This agrees with the earlier MIRI/LRS spectrum (Wachiraphan et al. 2025), which found a dayside brightness temperature of 525 ± 15 K and excluded >1 bar CO2 atmospheres at >4σ, and with the climate-constrained Bayesian analysis of Wogan et al. (2026), which found the bare-rock model moderately favoured over any atmospheric model (2σ upper limits ≲1 bar for O2/N2/CO, ≲0.1 bar for CO2).

### 3.2 LHS 1140 b: helium detected, then not — and JWST says no

Cherubim et al. (2026) observed LHS 1140 b with the WINERED high-resolution spectrograph on the Magellan Clay Telescope. In a transit on 23 September 2024 they detected excess absorption at the 1.083 µm metastable helium triplet: 1.24(+0.22/−0.23)% depth at the blended long-wavelength peaks, with FWHM 0.86 Å (23.9 km/s), interpreted as helium escaping from the upper atmosphere — the first evidence of an atmosphere, albeit a primordial one, around a rocky world in the classical habitable zone. A repeat transit in September 2025 showed no helium absorption, with an upper limit of 0.6% on the line depth, indicating time-variable escape; no helium was detected for the smaller, more irradiated sibling LHS 1140 c. The authors interpret the result as an upper atmosphere dominated by helium and depleted in hydrogen, consistent with atmospheric fractionation models.

Two independent JWST analyses challenge the persistence of that signal. Radica (2026) analyses four archival NIRISS/SOSS transits spanning December 2023 to July 2026: each visit disfavours helium absorption against a flat continuum with odds ratios of 3.9–11.6:1, and helium at the amplitude and width reported by Cherubim et al. is strongly ruled out, with odds ratios of 300–8.6×10^4:1 — though none of the JWST transits is contemporaneous with the ground-based detection — setting an abundance upper limit of 350–500 ppm. Bennett et al. (2026) likewise detect no helium in any of the four visits, reject the best-fit ground-based model at >3σ in each visit, and find no clear trend in mass loss with time; they conclude the reported detection may be spurious, although variability cannot be excluded if detectable helium absorption occurs in ≲50% of transits. Maltagliati (2026), in *Nature Astronomy*, frames the episode as "helium peekaboo": the first helium-escape claim for a habitable-zone rocky planet, contradicted in every JWST epoch so far.

### 3.3 Our calculation: three planets, three shoreline distances, one bracket

Table 1 gives the shoreline positions computed by §2.2. All three planets fall exactly on their predicted sides: the two planets above the line are airless, and the planet below the line shows (at least in one epoch) an escaping atmosphere.

**Table 1. Shoreline positions of the three newly measured rocky planets (own calculation from published inputs).**

| Planet | v_esc (km/s) | I_XUV (Earth units) | I_XUV,shore | Ratio | Δ (dex) | JWST / ground verdict |
|---|---|---|---|---|---|---|
| LTT 1445 A b | 15.97 | 99.95 | 43.71 | 2.29 | +0.36 | Airless (CO2 < 0.6 mbar) |
| LTT 1445 A c | 12.66 | 205.53 | 17.26 | 11.91 | +1.08 | Thick CO2 ruled out |
| LHS 1140 b | 20.13 | 13.04 | 110.34 | 0.12 | −0.93 | He escape reported 2024; JWST rules it out in 4/4 transits |

The two results jointly bracket the shoreline zero point. Planet b's airlessness requires the shoreline at v_esc = 15.97 km/s to sit at or below I_XUV = 99.95, i.e. D ≤ −2.81: the zero point cannot be more than a factor 2.29 above its canonical Mars-anchored value (D = −3.17). LHS 1140 b's reported atmosphere requires the shoreline at v_esc = 20.13 km/s to sit at or above I_XUV = 13.04, i.e. D ≥ −4.10: the zero point cannot be more than a factor 8.46 below canonical. The allowed interval is therefore D ∈ [−4.10, −2.81], a factor-of-19.4 band that contains the canonical value with room on both sides — but with a hard, new upper edge set by the closest-to-the-line airless planet ever measured in eclipse.

The Pass et al. (2025) 3× XUV revision, applied as a sensitivity test, moves all three ratios up by a factor of 3 (b: 6.86, c: 35.72, LHS 1140 b: 0.35) and flips none of the three classifications: LHS 1140 b remains below the line even under the revised fluence. The dayside-temperature scale is consistent throughout: T_b/T_day,max = 0.866 (b) and 0.856 (c), with T_b/T_eq = 1.23 and 1.21 — hot daysides with no sign of the heat redistribution a substantial atmosphere would provide (with the §2.2 caveat that 15-µm brightness temperature is a band temperature).

### 3.4 The falsifiable claim

**Claim.** The classical Mars-anchored XUV cosmic shoreline (log10 I_XUV = 4 log10 v_esc − 3.17) correctly separates airless from atmosphere-bearing rocky planets, with zero point D ∈ [−4.10, −2.81]: LTT 1445 A b (Δ = +0.36 dex) and c (Δ = +1.08 dex) are airless, and LHS 1140 b (Δ = −0.93 dex) retains an atmosphere.

**How to test it.** (i) The Rocky Worlds programme will eclipse roughly a dozen more rocky planets. The shoreline predicts that every planet with Δ > +0.36 dex — further above the line than LTT 1445 A b — will be airless, and every planet with Δ < −0.93 dex will show an atmosphere signature. A single substantial atmosphere found above +0.36 dex, or a single bare rock found below −0.93 dex, falsifies the classical zero point (and, if the counterexample sits far from the line, the slope as well), forcing a move toward the steeper empirical shoreline of Meni-Gallardo & Pallé (2026) or the hydrodynamic shoreline of Ji et al. (2025). (ii) The lower bound stands or falls with the reality of LHS 1140 b's helium: a simultaneous WINERED + JWST NIRISS transit campaign will decide it. If helium at the 2024 level (1.24%) reappears in both instruments at once, variability is real and the lower bound D ≥ −4.10 stands; if JWST rules it out again while ground data show it, the discrepancy is systematic, the lower bound must be re-derived from transmission data alone, and the shoreline's retaining side loses its only habitable-zone anchor.

## 4. Discussion

The value of this result is not that the shoreline survives — it was designed to survive these three planets — but that the shoreline is now a measured, bracketed quantity rather than a single-anchor extrapolation. Before November 2026, the zero point rested on Mars alone: one planet, with a 6-mbar remnant atmosphere, sitting essentially on the line. Now the upper edge is set by an exoplanet: LTT 1445 A b is the first airless world measured in eclipse close enough to the line to matter, and its distance from the line (+0.36 dex) is the tightest exoplanet constraint on how far the shoreline can move toward the airless side. The lower edge is set by LHS 1140 b, the only temperate rocky planet with a claimed escaping atmosphere, 0.93 dex below the line.

Three features of the bracket deserve emphasis. First, it is asymmetric: the shoreline is pinned 2.3× from above but 8.5× from below, because the airless side now has a near-line calibrator while the retaining side has only one planet, far below the line, whose atmosphere is itself disputed. The most valuable next measurement is therefore not another far-above-the-line bare rock — the Rocky Worlds programme already has several (TRAPPIST-1 b and c, GJ 3929b, GJ 367b) — but a planet just below the line, which would tighten the lower edge the way LTT 1445 A b tightened the upper one. Second, the bracket is robust to the largest known systematic: tripling the cumulative XUV fluence for M dwarfs, as Pass et al. (2025) propose, changes no classification, because the three planets sit far enough from the line in ratio space (2.3×, 11.9×, 8.5×) that a factor-3 shift cannot cross them. Third, the bracket is compatible with, but does not require, the two 2025–2026 revisions of the shoreline: the steeper empirical shoreline of Meni-Gallardo & Pallé (2026), anchored to Mars plus four exoplanets with tentative atmospheric detections, and the hydrodynamic shoreline of Ji et al. (2025), which finds that varying the initial volatile inventory (0.01%–1% of planetary mass) blurs any single line. Both revisions predict that the classical line is an approximation; our bracket quantifies how good an approximation it is, and §3.4 gives the observations that would break it.

The LHS 1140 b dispute also carries a methodological lesson. The ground-based detection and the JWST non-detections are not yet in direct conflict, because no JWST transit was contemporaneous with the ground-based detection, and Bennett et al. show variability below a ~50% duty cycle is still allowed. But the episode shows that single-epoch helium claims for rocky planets are now in the regime where a claimed atmosphere can be challenged within months by archival data — the standard of evidence for "this rocky planet has an atmosphere" has risen, and the shoreline's lower bound should be treated as provisional until a simultaneous campaign settles it.

## 5. Limitations

1. **No new data.** This is a synthesis and analytic re-derivation from published results; the shoreline positions are calculations, not measurements.
2. **Mars anchoring.** The zero point D = −3.17 assumes Mars marks the boundary, following Zahnle & Catling (2017). Mars has a 6-mbar atmosphere, so whether it sits just above or just below the line is a judgement call in the original paper; shifting the anchor by Mars's own ambiguity moves D by ≲0.1 dex, small against the bracket width.
3. **The I_XUV scaling is a proxy.** The (L*/L⊙)^0.4 scaling compresses stellar XUV evolution, pre-main-sequence duration, and flare history into one exponent; the Pass et al. (2025) 3× revision is tested as a sensitivity case, but the true fluence for any individual M dwarf is uncertain by factors of a few.
4. **Slope fixed at 4.** We test the classical slope; the steeper empirical slope of Meni-Gallardo & Pallé (2026) would change the bracket, and is itself falsifiable by the same test in §3.4.
5. **Band temperatures.** The 15-µm brightness temperatures are not bolometric dayside temperatures; the T_b/T_day,max ratios are a scale comparison only.
6. **The lower bound is conditional.** D ≥ −4.10 assumes the Cherubim et al. (2026) helium detection is genuine. If it is spurious, the lower bound weakens to whatever JWST transmission data support for LHS 1140 b (a water-world or thin-atmosphere interpretation), and the bracket's lower edge must be re-derived.
7. **Small numbers.** Three planets bracket a line; the test in §3.4 is the point — the bracket will tighten or break as the Rocky Worlds programme reports its remaining targets.
8. **Research agents.** The installed research agents (Co-Scientist, Denario, EvoScientist) remain blocked on authentication — they need a real API key in the Authorization header, which this run does not hold — and Mimosa's literature-synthesis run is blocked on an unresolved MCP-discovery stall; the literature sweep and analysis here were therefore done directly from the daily digest and targeted arXiv checks.

## 6. Conclusion

In a single week, JWST and ground-based spectroscopy bracketed the cosmic shoreline from both sides. LTT 1445 A b — the closest planet to the line yet observed in eclipse — is airless, with CO2 below 0.6 mbar and surface pressure below 0.1 bar; its sibling c is airless too. LHS 1140 b, 0.93 dex below the line, shows escaping helium in one epoch and none in four JWST transits. Our re-derivation puts numbers on what those results mean together: the shoreline's zero point lies in D ∈ [−4.10, −2.81], no more than 2.3× above and 8.5× below its canonical Mars-anchored value. The next Rocky Worlds eclipses and a simultaneous helium transit campaign for LHS 1140 b will either tighten that bracket or break the classical line — and either outcome is progress, because the shoreline is now a falsifiable, measured quantity instead of a sketch anchored on Mars alone.

---

## References

1. Ih, J., Kanodia, S., Wogan, N., et al. JWST Rocky Worlds DDT Observations of LTT 1445 A b and c in Secondary Eclipse Using MIRI/F1500W. arXiv:2611.17300 (2026).
2. Cherubim, C., Vissapragada, S., Cunningham, T., et al. Helium escaping from the atmosphere of a nearby rocky exoplanet orbiting in a habitable zone. *Science* (2026). arXiv:2607.14326.
3. Radica, M. Strict Limits on Helium Absorption from LHS 1140 b from Four JWST NIRISS Transits. arXiv:2608.13470 (2026).
4. Bennett, K. A., Gascon, C., Lustig-Yaeger, J. No Helium Detected in LHS 1140 b from Four JWST NIRISS/SOSS Transits. arXiv:2608.13473 (2026).
5. Maltagliati, L. Helium peekaboo. *Nat. Astron.* (2026). https://doi.org/10.1038/s41550-026-03029-8
6. Zahnle, K. J., & Catling, D. C. The cosmic shoreline: the evidence that escape determines which planets have atmospheres, and what this may mean for Proxima Centauri b. *Astrophys. J.* **843**, 122 (2017). arXiv:1702.03386.
7. Meni-Gallardo, P., & Pallé, E. An empirical determination of the Cosmic Shoreline. *Mon. Not. R. Astron. Soc.* (2026). arXiv:2508.12865.
8. Ji, X., Chatterjee, R. D., Coy, B. P., & Kite, E. The Cosmic Shoreline Revisited: A Metric for Atmospheric Retention Informed by Hydrodynamic Escape. *Astrophys. J.* (accepted 20 Aug 2025). arXiv:2504.19872.
9. Wogan, N. F., Batalha, N. E., Ih, J., Lustig-Yaeger, J., & Stevenson, K. B. A Climate-constrained Bayesian Inverse Method for JWST Rocky Exoplanet Eclipse Spectra: Case Study of LTT 1445A b. *Astrophys. J. Lett.* **1007**, L46 (2026). https://doi.org/10.3847/2041-8213/ae9305
10. Wachiraphan, P., et al. The Thermal Emission Spectrum of the Nearby Rocky Exoplanet LTT 1445A b from JWST MIRI/LRS. *Astron. J.* (2025). https://doi.org/10.3847/1538-3881/adc990
11. Pass, E. K., et al. HST/WFC3 Light Curve Supports a Terrestrial Composition for the Closest Exoplanet to Transit an M Dwarf. arXiv:2307.02970 (2023).
12. Winters, J. G., et al. A Second Planet Transiting LTT 1445A and a Determination of the Masses of Both Worlds. *Astron. J.* (2022). https://doi.org/10.3847/1538-3881/ac50a9
13. Ment, K., et al. A Second Terrestrial Planet Orbiting the Nearby M Dwarf LHS 1140. *Astron. J.* **157**, 32 (2019). https://doi.org/10.3847/1538-3881/aaf1b1
14. Dittmann, J. A., et al. A temperate rocky super-Earth transiting a nearby cool star. arXiv:1704.05556 (2017).
15. The JWST Rocky Worlds DDT Program reveals GJ 3929b to likely be a bare rock. arXiv:2508.12516 (2025).

## Data availability

No new data were generated. All observational numbers are taken from the cited published sources (Refs. 1–5, 9–14), verified against the arXiv record and publisher pages on 2026-11-14. All derived numbers (escape velocities 15.97, 12.66, 20.13 km/s; cumulative XUV instellations 99.95, 205.53, 13.04 Earth units; shoreline ratios 2.29, 11.91, 0.12; shoreline distances +0.36, +1.08, −0.93 dex; zero-point bracket D ∈ [−4.10, −2.81]; Pass-3× ratios 6.86, 35.72, 0.35) are computed in this manuscript from the formulae in §2.2 and are reproducible with a pocket calculator. The literature sweep used the daily research digest for 2026-11-14 (~/workspace/research-team/digests/2026-11-14.md) and targeted arXiv searches on 2026-11-14.

## Submission pack (ChemRxiv-ready)

- **Abstract:** as above (within the ChemRxiv 2,500-character limit; verified by character count at submission time).
- **Keywords:** exoplanet atmospheres; cosmic shoreline; atmospheric escape; JWST; M dwarfs; LTT 1445; LHS 1140 b; helium (8 keywords).
- **Primary subject area:** Earth and Planetary Astrophysics (astro-ph.EP).
- **AI-assistance disclosure:** This manuscript was drafted with AI assistance (Lapis) from published sources; all claims require independent verification. Not peer-reviewed, not published.
- **Author line:** Zubair Ali, Pharm-D student, SMBBMU Larkana, Pakistan — ORCID: 0009-0001-5921-7509.
