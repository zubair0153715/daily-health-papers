# Black-Hole Spectroscopy at Both Ends of the Mass Ladder: GW250114's Ringdown and the First Pulsar-Timing Limits on Supermassive Binaries at Cosmic Dawn

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent verification.**

**Author:** Zubair Ali, Pharm-D student, SMBBMU Larkana, Pakistan — ORCID: 0009-0001-5921-7509
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-11
**Field:** Space (astronomy / gravitational-wave astrophysics)

---

## Abstract

Two results published within days of each other in November 2026 bracket the black-hole mass spectrum from opposite ends. At the stellar-mass end, the LIGO-Virgo-KAGRA Collaboration's black-hole spectroscopy of GW250114 — the loudest gravitational-wave signal recorded to date, network signal-to-noise ratio 76 — requires at least two quasi-normal modes in the ringdown, constrains the dominant quadrupolar mode and its first overtone to match the Kerr prediction to tens of percent, and bounds the quadrupolar frequency to within a few percent of general relativity, delivering the most stringent single-event test of general relativity to date. At the supermassive end, the Parkes Pulsar Timing Array Collaboration reports the first direct nanohertz gravitational-wave limits on supermassive black-hole binaries at cosmic dawn (Phys. Rev. Lett. 137, 191401, 2 November 2026), with a best all-sky chirp-mass upper limit of 8.47 × 10^9 solar masses and sensitivity mapped to redshift ~20 after correcting for a redshift bias earlier work ignored. We combine the two results into a single quantitative test. Treating the 1.2 × 10^10 solar-mass black hole in the quasar J0100+2802 (z = 6.327) as a hypothetical equal-mass binary gives a chirp mass of 5.22 × 10^9 solar masses — a factor of 1.62 below the current best pulsar-timing limit and a factor of 1.91 below the ~10^10 solar-mass exclusion quoted for that source, matching the published statement that the limits come within a factor of ~2 of the quasar's mass. A chirp-mass sensitivity improvement of a factor of ~1.6, equivalent to a factor of ~2.2 in strain, would therefore cross the threshold for this source. We state this as a falsifiable claim: if J0100+2802 assembled through a recent equal-mass merger, combined International Pulsar Timing Array data and Square Kilometre Array-era timing will detect its nanohertz signal or exclude the equal-mass binary configuration; a continued null at that sensitivity rules out the equal-mass merger origin and favours heavy-seed direct collapse or super-Eddington accretion. (Abstract: 2,110 characters.)

**Keywords:** gravitational waves; black-hole spectroscopy; quasi-normal modes; pulsar timing arrays; supermassive black holes; cosmic dawn; GW250114; J0100+2802

---

## 1. Introduction

Black holes are now empirical objects, studied with telescopes and gravitational-wave detectors alike, but one question remains open: how did the supermassive black holes — millions to billions of solar masses — assemble? The debate reduces to three options: black holes started massive (heavy seeds, e.g. direct collapse of a massive gas cloud), grew massive (sustained rapid accretion, possibly super-Eddington), or built up through mergers. The James Webb Space Telescope has sharpened the problem by finding luminous quasars powered by billion-solar-mass black holes less than a billion years after the Big Bang, and an unexpected abundance of luminous "little red dots" at redshifts around z = 10, corresponding to a cosmic age of about 500 million years, some of which may be active black holes as massive as 10^8 solar masses.

Two observational windows now constrain this problem from opposite ends of the mass scale, and both produced landmark results in the same week. At the stellar-mass end, gravitational-wave ringdown spectroscopy tests whether a merger remnant is a Kerr black hole of general relativity, mode by mode. At the supermassive end, pulsar timing arrays (PTAs) search for the nanohertz gravitational waves emitted by slowly orbiting supermassive binaries. Until November 2026, PTA limits applied only to the local Universe (z < 0.4); the new work extends them to cosmic dawn. This paper synthesises the two results and derives, from published numbers alone, the exact sensitivity gap that separates a null result from a decisive test of how the earliest quasars were built.

## 2. Methods

### 2.1 Literature sweep

The daily research digest for 2026-11-11 (health-focused; no space entries) was read, and targeted searches were run on arXiv (gr-qc, astro-ph) and in the press for gravitational-wave results dated 1–11 November 2026. Every cited result was verified against its publisher or arXiv record: the GW250114 spectroscopy paper (arXiv:2509.08099; Phys. Rev. Lett. 136, 041403, 2026) and its companion area-law paper (Phys. Rev. Lett. 135, 111403, 2025); the Parkes Pulsar Timing Array cosmic-dawn paper (arXiv:2609.00613; Phys. Rev. Lett. 137, 191401, published 2 November 2026) and the accompanying Physics viewpoint (Physics 19, 146, 2026). No citation, number, or identifier in this manuscript is invented; where a number is our own derivation, the formula and inputs are shown in full.

### 2.2 Analytic methods (own calculations)

**Chirp mass of a hypothetical equal-mass binary.** For component masses m1 and m2, the chirp mass is M_c = (m1·m2)^(3/5) / (m1 + m2)^(1/5). For an equal-mass binary with each component m, this reduces to M_c = m / 2^(1/5) = m / 1.1487. Applied to J0100+2802, whose black-hole mass is estimated at 1.2 × 10^10 solar masses: splitting that mass into an equal-mass pair (m = 6.0 × 10^9 solar masses each) gives M_c = 5.22 × 10^9 solar masses.

**Gap factors.** The best published all-sky chirp-mass upper limit is 8.47 × 10^9 solar masses, and the exclusion quoted for the two cosmic-dawn targets is ~10^10 solar masses. The ratios 8.47 × 10^9 / 5.22 × 10^9 = 1.62 and 10^10 / 5.22 × 10^9 = 1.91 quantify how far current sensitivity is from testing the equal-mass binary hypothesis for J0100+2802.

**Strain-sensitivity equivalent.** For a binary at fixed distance and frequency, gravitational-wave strain scales as h ∝ M_c^(5/3). A chirp-mass reach improvement of a factor 1.62 therefore requires a strain-sensitivity improvement of 1.62^(5/3) ≈ 2.2.

**Frequency scale.** A binary orbiting about once per year emits gravitational waves at f_GW = 2 / P_orb ≈ 63 nHz in the observer frame. At the redshift of J0100+2802 (z = 6.327), the source-frame frequency is higher by (1 + z): ≈ 63 × 7.327 ≈ 464 nHz — the redshift brightening that makes distant sources counterintuitively easier for PTAs to see, because the observed signal comes from a later, tighter, more luminous stage of the inspiral.

All arithmetic was computed in Python 3 and is reproducible from the formulae above.

## 3. Results

### 3.1 GW250114: the loudest signal becomes the sharpest test of general relativity

GW250114 was recorded by the LIGO detectors on 14 January 2025 (Virgo and KAGRA were offline), with a network signal-to-noise ratio of 76 — the loudest gravitational-wave signal to date. Independent analyses agree on the source: two nearly equal-mass, low-spin, first-generation black holes of roughly 34 and 32 solar masses (mass ratio ≈ 0.94), with eccentricity e ≤ 0.03 at 13.33 Hz, forming a remnant inside the pair-instability mass gap. The LIGO-Virgo-KAGRA spectroscopy analysis finds:

- At least **two quasi-normal modes are required** to explain the post-merger signal: the dominant quadrupolar (ℓ = m = 2, n = 0) mode and its first overtone (n = 1), the most damped of which remains statistically significant for about one cycle. The overtone is supported at 3.6σ in the standard analysis, rising to 99.9% significance with orthonormalised modes.
- The spectroscopic pattern of the dominant mode and its first overtone matches the **Kerr prediction to tens of percent** at multiple post-peak times; the fundamental (ℓ = m = 4) mode is constrained to tens of percent, and the quadrupolar frequency is bounded to **within a few percent** of the general-relativistic prediction.
- A suite of inspiral, merger, and ringdown tests gives constraints comparable to — and in some cases **2–3 times more stringent than** — those obtained by combining dozens of events in the fourth Gravitational-Wave Transient Catalog: the most stringent single-event verification of general relativity and the Kerr nature of black holes to date.
- The companion analysis strongly favours a final horizon area larger than the sum of the initial areas, a direct test of **Hawking's area law**.
- Independent follow-up analyses confirm subdominant (4, ±4) multipoles with higher evidence than the Collaboration first reported, find the quadratic (2,2,0)×(2,2,0) mode coupling consistent with numerical relativity to within 1.3σ, and recover the general-relativistic expectation for the remnant mass and spin within the 50% credible region.

### 3.2 The Parkes Pulsar Timing Array reaches cosmic dawn

Chen et al. (2026) reformulate pulsar-timing searches with a cosmological correction — the redshift bias — that earlier work ignored. Because a distant binary's observed frequency is redshifted, the signal seen in the nanohertz PTA band originates from a higher source-frame frequency, i.e. a later, tighter, more luminous stage of inspiral; this intrinsic brightening can outpace cosmological dimming, making PTAs counterintuitively more sensitive to faraway sources. Using Parkes Pulsar Timing Array data with this correction, they:

- Map PTA sensitivity to binary mass and redshift from the local Universe out to **z ~ 20** for the first time (previous work stopped at z < 0.4).
- Set a best all-sky chirp-mass upper limit of **8.47 × 10^9 solar masses**.
- Anchor the limits on two electromagnetically detected cosmic-dawn sources: the quasar **J0100+2802** (z = 6.327; black-hole mass ≈ 1.2 × 10^10 solar masses; its light left when the Universe was barely 900 million years old) and the galaxy **JADES-GS-z14-0** (z = 14.32; only ~290 million years after the Big Bang). For both, binaries with chirp masses at or above **~10^10 solar masses are excluded** across the nanohertz band — the tightest constraints to date on supermassive binaries at z > 6, and the first constraints of any kind at the redshift of JADES-GS-z14-0.
- Show the Parkes observations are **not yet sensitive enough** to test whether either system is a binary, but the limits come close — **within a factor of ~2** of the quasar's estimated mass.

### 3.3 Our calculation: the gap is a factor of 1.6 in chirp mass

Applying the method of §2.2 to J0100+2802 (Table 1), a hypothetical equal-mass binary totalling the quasar's estimated 1.2 × 10^10 solar masses has a chirp mass of 5.22 × 10^9 solar masses. This sits a factor of 1.62 below the best published all-sky limit (8.47 × 10^9 solar masses) and a factor of 1.91 below the ~10^10 solar-mass exclusion quoted for the source — quantitatively reproducing the published "within a factor of ~2" statement from first principles, and showing that the two published numbers (best limit vs target exclusion) are mutually consistent. Reaching this binary requires a strain-sensitivity improvement of only a factor of ~2.2, the scale of improvement expected from combining International Pulsar Timing Array data and from Square Kilometre Array-era timing precision.

**Table 1. The sensitivity gap for J0100+2802 as a hypothetical equal-mass binary (own calculation from published inputs).**

| Quantity | Value | Source |
|---|---|---|
| Black-hole mass, J0100+2802 | 1.2 × 10^10 M☉ | Wu et al. 2015; Chen et al. 2026 |
| Redshift | 6.327 | Chen et al. 2026 |
| Hypothetical equal-mass components | 6.0 × 10^9 M☉ each | This work (§2.2) |
| Chirp mass M_c | 5.22 × 10^9 M☉ | This work (§2.2) |
| Best all-sky chirp-mass upper limit | 8.47 × 10^9 M☉ | Chen et al. 2026 |
| Gap factor (limit / M_c) | 1.62 | This work |
| Exclusion for the target | ~10^10 M☉ | Chen et al. 2026 |
| Gap factor (exclusion / M_c) | 1.91 | This work |
| Required strain improvement | ~2.2× | This work (h ∝ M_c^5/3) |
| Observed f_GW (1-yr orbit) / source-frame | ~63 nHz / ~464 nHz | This work (§2.2) |

### 3.4 The falsifiable claim

**Claim.** If the 1.2 × 10^10 solar-mass black hole in J0100+2802 assembled through a recent equal-mass merger, then a pulsar-timing chirp-mass sensitivity improvement of a factor of ~1.6 (≈ 2.2× in strain) will detect its nanohertz gravitational-wave signal or exclude the equal-mass binary configuration.

**How to test it.** (i) Apply the redshift-corrected analysis of Chen et al. to the next International Pulsar Timing Array data release and to Square Kilometre Array-era timing; a detection at ~63 nHz from the direction of J0100+2802 confirms the binary. (ii) A continued null at the improved sensitivity excludes an equal-mass binary totalling 1.2 × 10^10 solar masses at z = 6.327, and thereby rules out the equal-mass merger origin for this quasar, leaving heavy-seed direct collapse or super-Eddington accretion as the remaining explanations. (iii) Corollary at the stellar-mass end: if the Kerr hypothesis holds, the (2,2,1) overtone amplitude measured in the next signal-to-noise-ratio ≳ 50 binary black-hole event will match the numerical-relativity prediction within the same tens-of-percent band established by GW250114; a systematic deviation across events would falsify Kerr.

## 4. Discussion

The two results are complementary in a precise sense. GW250114 shows that general relativity and the Kerr metric survive their most stringent single-event examination: the remnant's ringing matches Kerr mode by mode, the area law holds, and no discrepancy appears in any of inspiral, merger, or ringdown. That licenses the use of general-relativistic waveforms to interpret the nanohertz sky. The Parkes result then uses that same physics at the opposite end of the spectrum: a galaxy-sized detector made of pulsars, sensitive to binaries orbiting about once a year, now reaches the epoch in which the first quasars turned on.

The scientific payoff is a dated, quantitative fork in the road for seed models. Heavy seeds (direct collapse of ~10^5 solar-mass clouds) predict that a quasar like J0100+2802 need never have been an equal-mass binary of two ~6 × 10^9 solar-mass holes; light seeds grown by mergers predict binary phases. Our calculation puts the fork within reach: a factor of ~2 in strain, not an order of magnitude. The redshift-bias correction is what makes this possible — without it, the sensitivity at z > 6 would be underestimated and the test would look decades away. Two further points strengthen the case: first, the same redshift brightening applies to JADES-GS-z14-0, so the method's first constraints at z = 14.32 are a floor, not a ceiling; second, the nanohertz gravitational-wave background detected by PTA collaborations in 2023 guarantees a population of supermassive binaries exists in the local Universe, so the question is now where in mass and redshift that population extends.

At the stellar-mass end, GW250114 also changes the economics of testing gravity: one event at signal-to-noise ratio 76 now constrains general relativity 2–3 times more tightly than dozens of earlier events combined. The implication for the next observing runs is that ringdown spectroscopy should be treated as a primary science goal, not a follow-up, and that the (4,4) mode and quadratic mode couplings are now measurable quantities with which to stress-test numerical relativity.

## 5. Limitations

1. **No new data.** This is a synthesis and analytic re-derivation from published results; the chirp-mass and strain figures are calculations, not measurements.
2. **The binary hypothesis for J0100+2802 is hypothetical.** There is no evidence that J0100+2802 is a binary; the calculation tests what PTAs could say if it were. The quasar's mass estimate (≈ 1.2 × 10^10 solar masses) carries systematic uncertainty from the virial estimator, so the gap factors 1.62 and 1.91 are approximate to that uncertainty.
3. **Upper limits, not detections.** The Parkes limits are non-detections; the "factor of ~2" is a statement about sensitivity, not a measurement of a signal.
4. **Sensitivity projections are extrapolations.** The expected factor ~2.2 strain improvement from combined International Pulsar Timing Array data and Square Kilometre Array-era timing is a projection from published statements, not a guaranteed schedule.
5. **Single-event gravity tests.** GW250114 is one event; the Kerr constraints, however stringent, are a single realisation, and the corollary test in §3.4 requires future loud events.
6. **Research agents.** The installed research agents (Co-Scientist, Denario, EvoScientist) remain blocked on authentication — they need a real API key in the Authorization header, which this run does not hold — and Mimosa's literature-synthesis run is blocked on an unresolved MCP-discovery stall; the literature sweep and analysis here were therefore done directly from the daily digest and targeted arXiv/publisher checks.

## 6. Conclusion

In a single week, gravitational-wave astronomy bracketed the black-hole mass spectrum: GW250114's ringdown verified Kerr and general relativity more stringently than dozens of earlier events combined, and the Parkes Pulsar Timing Array placed the first gravitational-wave limits on supermassive binaries at cosmic dawn. Our re-derivation shows the two results meet in a concrete number: the equal-mass binary hypothesis for the 1.2 × 10^10 solar-mass quasar J0100+2802 sits only a factor of ~1.6 in chirp mass — ~2.2× in strain — beyond current pulsar-timing sensitivity. The next generation of pulsar-timing data will therefore either detect the nanohertz signal of the earliest quasars' binary past or rule it out. Either outcome decides between the seed models that explain how billion-solar-mass black holes existed less than a billion years after the Big Bang.

---

## References

1. Abac, A. G., et al. (LIGO Scientific Collaboration, Virgo Collaboration, KAGRA Collaboration). GW250114: Testing Hawking's Area Law and the Kerr Nature of Black Holes. *Phys. Rev. Lett.* **135**, 111403 (2025).
2. Abac, A. G., et al. (LIGO Scientific Collaboration, Virgo Collaboration, KAGRA Collaboration). Black Hole Spectroscopy and Tests of General Relativity with GW250114. *Phys. Rev. Lett.* **136**, 041403 (2026). arXiv:2509.08099.
3. Chen, Y., Zhao, S.-Y., Zhu, X., et al. (PPTA Collaboration). Nanohertz Gravitational-Wave Constraints on Supermassive Binary Black Holes at Cosmic Dawn. *Phys. Rev. Lett.* **137**, 191401 (2026). arXiv:2609.00613.
4. Burke-Spolaor, S. Using Pulsars to Probe Early Growth of Black Holes. *Physics* **19**, 146 (2026).
5. Abbott, B. P., et al. (LIGO Scientific Collaboration, Virgo Collaboration). Observation of Gravitational Waves from a Binary Black Hole Merger. *Phys. Rev. Lett.* **116**, 061102 (2016).
6. Agazie, G., et al. (NANOGrav Collaboration). The NANOGrav 15 yr Data Set: Evidence for a Gravitational-wave Background. *Astrophys. J. Lett.* **951**, L8 (2023).
7. Wu, X.-B., et al. An ultraluminous quasar with a twelve-billion-solar-mass black hole at redshift 6.30. *Nature* **518**, 512–515 (2015).
8. From Source Properties to Strong-Field Tests: a multipronged analysis of GW250114 with an effective one-body model for generic orbits. arXiv:2512.04593.
9. Suzuki, M., Kubota, K., Morisaki, S., Motohashi, H., Watarai, D. Ringdown Analysis of GW250114 with Orthonormal Modes. arXiv:2605.03576.
10. Yang, Y., et al. Constraining the Quadratic-mode Amplitude Coupling in GW250114. arXiv:2609.28953.

## Data availability

No new data were generated. All observational numbers are taken from the cited published sources (Refs. 1–4, 7), verified against the arXiv record and the *Physics* viewpoint on 2026-11-11. All derived numbers (chirp mass 5.22 × 10^9 M☉, gap factors 1.62 and 1.91, strain factor ~2.2, frequencies ~63 nHz / ~464 nHz) are computed in this manuscript from the formulae in §2.2 and are reproducible with a pocket calculator. The literature sweep used the daily research digest for 2026-11-11 (~/workspace/research-team/digests/2026-11-11.md) and targeted arXiv searches on 2026-11-11.
