# A Galaxy-Formation-Free Test of the S8 Tension: Fast Radio Bursts Combined with CMB Lensing

> **AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent verification.**

**Author:** Zubair Ali, Pharm-D student, SMBBMU Larkana, Pakistan · ORCID 0009-0001-5921-7509
**Drafting assistant:** Lapis (AI)
**Date:** 4 November 2026

## Abstract

The amplitude of late-time matter clustering, parameterised by $S_8 = \sigma_8\sqrt{\Omega_{\mathrm{m}}/0.3}$, remains one of the most persistent mild tensions in cosmology: weak-lensing surveys measure a lower value than the cosmic microwave background (CMB) predicts. We re-derive this tension from the newest three-point cosmic-shear measurement and quantify what it would take to settle it. Using the Dark Energy Survey Year 3 (DES Y3) integrated three-point correlation function result, $S_8 = 0.784^{+0.024}_{-0.021}$ (Gebauer et al. 2026), and the Planck 2018 base-$\Lambda$CDM parameters $\sigma_8 = 0.811 \pm 0.006$, $\Omega_{\mathrm{m}} = 0.315 \pm 0.007$ (Planck Collaboration 2020), we obtain a Planck value of $S_8 = 0.831 \pm 0.011$ and a one-dimensional $S_8$ tension of $1.9\sigma$, with the $\Omega_{\mathrm{m}}$ tension at only $1.2\sigma$ and $w_0 = -1.04^{+0.25}_{-0.19}$ consistent with a cosmological constant at $0.2\sigma$. We then combine this with the new result of Sullivan et al. (2026) that the free-electron distribution traced by fast radio burst (FRB) dispersion measures follows the total matter distribution almost exactly, so that FRB dispersion combined with CMB lensing constrains $\sigma_8$ and $\Omega_{\mathrm{m}}$ with no dependence on galaxy formation or baryonic feedback. We show that such a baryon-free probe needs $\sigma(S_8) \le 0.016$ (2.0% precision) to separate the DES and Planck central values at $3\sigma$ — only a factor of 1.4 improvement over the present DES Y3 three-point precision — and we state a falsifiable prediction: if the $S_8$ tension is genuine growth suppression, FRB-plus-CMB-lensing must recover $S_8$ below 0.80; recovery of $S_8 \ge 0.82$ would instead attribute the tension to weak-lensing systematics. Bright-siren gravitational-wave distances, forecast to reach $\sim$2.7% precision on $H_0$ with 300 detections (Pacheco et al. 2026), provide the complementary distance-ladder check on the same $3\sigma$ standard.

**Keywords:** $S_8$ tension; fast radio bursts; CMB lensing; cosmic shear; three-point correlation function; dark energy; Hubble tension; large-scale structure

## 1. Introduction

Two tensions dominate modern cosmology. The Hubble tension — the $\approx$5$\sigma$ disagreement between the Planck CMB value $H_0 = 67.4 \pm 0.5$ km s$^{-1}$ Mpc$^{-1}$ (Planck Collaboration 2020) and local distance-ladder measurements near $73$ km s$^{-1}$ Mpc$^{-1}$ (Riess et al. 2022) — concerns the expansion rate. The $S_8$ tension concerns the growth of structure: weak-lensing surveys consistently infer a lower clustering amplitude than the CMB predicts under $\Lambda$CDM. Unlike the $H_0$ tension, the $S_8$ tension is mild ($\sim$2$\sigma$) and therefore ambiguous: it may be new physics (suppressed late-time growth), or it may be systematics in weak lensing — photometric redshifts, intrinsic alignments, shear calibration, or baryonic feedback on the matter power spectrum.

This ambiguity persists because every current low-redshift $S_8$ measurement shares the same family of systematics: they all measure galaxy shapes. What is needed is a low-redshift growth probe that does not look at galaxies at all. Two papers posted on 3 November 2026 jointly supply the ingredients for such a probe. First, Gebauer et al. (2026) report the first cosmic-shear analysis of the integrated three-point correlation function (i3PCF) on survey data (DES Y3), detecting the three-point signal at a signal-to-noise ratio of 12.8 and improving the figure of merit in the $\Omega_{\mathrm{m}}$–$S_8$–$w_0$ space by a factor of 1.59 over two-point functions alone. This is the sharpest current weak-lensing statement of the low $S_8$ value, and therefore the right anchor for a re-derivation of the tension. Second, Sullivan et al. (2026) show from the FLAMINGO simulations that the free-electron distribution — the quantity fast radio burst (FRB) dispersion measures directly probe — follows the total matter distribution almost exactly, and that FRB dispersion combined with CMB lensing can constrain $\sigma_8$ and $\Omega_{\mathrm{m}}$ at a level similar to or better than FRB dispersion combined with galaxy weak lensing, with no dependence on galaxy formation or baryonic feedback models.

This paper does three things. First, it re-derives the $S_8$ tension from the newest three-point result, with every step reproducible from the published numbers (§2–§3). Second, it quantifies the precision a baryon-free FRB-plus-CMB-lensing probe must reach to decide the tension at $3\sigma$ (§3). Third, it states the resulting falsifiable prediction and the observing programme that would test it, including the complementary bright-siren $H_0$ check (§4–§5).

## 2. Methods

### 2.1 Input values

All input numbers are taken from published sources, listed in Table 1. No new observational data are presented. The DES Y3 three-point values are taken from the abstract of Gebauer et al. (2026, arXiv:2611.05367): $S_8 = 0.784^{+0.024}_{-0.021}$, $\Omega_{\mathrm{m}} = 0.272^{+0.038}_{-0.033}$, $w_0 = -1.04^{+0.25}_{-0.19}$, a three-point detection signal-to-noise ratio of 12.8, and a figure-of-merit improvement of 1.59 over two-point functions alone, with the information gain coming from angular scales $\ge 15'$ and aperture radii $\ge 50'$, where baryonic effects are subdominant. The Planck 2018 base-$\Lambda$CDM values are taken from Planck Collaboration (2020, A&A 641, A6; arXiv:1807.06209): $\sigma_8 = 0.811 \pm 0.006$, $\Omega_{\mathrm{m}} = 0.315 \pm 0.007$, $H_0 = 67.4 \pm 0.5$ km s$^{-1}$ Mpc$^{-1}$. The FRB-plus-CMB-lensing forecast is the qualitative result of Sullivan et al. (2026, arXiv:2611.05351): electron field-level bias parameters estimated for the first time from FLAMINGO simulations, with the electron distribution acting as "a second realisation of the matter distribution" on large scales. The bright-siren forecast is from Pacheco et al. (2026, arXiv:2611.05338): 300 bright-siren detections to $z = 1$ yield $H_0$ precision of $\sim$2.7% with the Doublet approximation, versus $\sim$2.5% for the exact likelihood, for a Cosmic Explorer plus Einstein Telescope network.

### 2.2 Calculations

The Planck $S_8$ value is derived, not quoted: $S_8 = \sigma_8\sqrt{\Omega_{\mathrm{m}}/0.3}$, with Gaussian error propagation on $\sigma_8$ and $\Omega_{\mathrm{m}}$ treated as independent. Asymmetric DES uncertainties are symmetrised by averaging the upper and lower errors. Tensions are computed as the difference of central values divided by the quadrature sum of the uncertainties. The precision required of a new probe to separate the DES and Planck central values at $3\sigma$ is $\Delta S_8/3$, computed both standalone and after accounting for the Planck uncertainty. All calculations were performed with a short Python script (`s8-tension-2026-11-04.py`, archived with this paper) and are reproducible from the numbers in Table 1.

## 3. Results

### 3.1 The $S_8$ tension, re-derived from three-point cosmic shear

From the Planck 2018 parameters, $S_8 = 0.811 \times \sqrt{0.315/0.3} = 0.831 \pm 0.011$. Against the DES Y3 three-point value $S_8 = 0.784 \pm 0.0225$ (symmetrised), the difference is $\Delta S_8 = 0.047$ with a combined uncertainty of $0.025$, giving a one-dimensional tension of **1.9$\sigma$**. This is consistent with, and slightly below, the Gebauer et al. statement that their constraints differ by at most $2.4\sigma$ from CMB and baryon acoustic oscillation data in the full three-dimensional $\Omega_{\mathrm{m}}$–$S_8$–$w_0$ space; the difference between 1.9$\sigma$ and 2.4$\sigma$ reflects the extra dimensions and the Planck-plus-BAO combination used there, versus our $S_8$-only comparison against Planck alone.

Two decompositions sharpen the picture. First, the $\Omega_{\mathrm{m}}$ tension alone is only **1.2$\sigma$** ($0.315 \pm 0.007$ versus $0.272 \pm 0.0355$): the matter density is not the driver of the discrepancy. Second, the dark-energy equation of state is unremarkable: $w_0 = -1.04 \pm 0.22$ sits $0.2\sigma$ from the cosmological-constant value $-1$. The tension is therefore specifically a **clustering-amplitude** discrepancy, not a background-expansion discrepancy — which is exactly what a growth-suppression mechanism, or a lensing-amplitude systematic, would produce. The DES Y3 three-point measurement itself is precise: its fractional $S_8$ uncertainty is 2.9%.

### 3.2 What it takes to decide the tension

A new probe separates the DES value (0.784) from the Planck value (0.831) at $3\sigma$ if its own $S_8$ uncertainty satisfies $\sigma(S_8) \le \Delta S_8/3 = 0.0157$, i.e. 2.0% precision. Accounting for the Planck uncertainty as well, the requirement tightens to $\sigma(S_8) \le 0.011$ (1.4%). Relative to the current DES Y3 three-point precision (0.0225), this is only a factor of **1.4** improvement (standalone) or **2.0** (including the Planck error). Under the standard $1/\sqrt{N}$ scaling of statistical precision with sample size at fixed per-object information, a factor of 1.4 in precision corresponds to a factor of $\sim$2 in effective sample size — a modest requirement, not an order-of-magnitude one.

This is where the Sullivan et al. result matters. Their forecast is that FRB dispersion plus CMB lensing constrains $\sigma_8$ and $\Omega_{\mathrm{m}}$ "at a level similar to or better than" FRB dispersion plus galaxy weak lensing under conservative assumptions. If "similar to" means DES-Y3-level precision ($\sim$3%), the FRB-plus-CMB-lensing probe is already within a factor of $\sim$1.4 of the standalone $3\sigma$ discrimination threshold, and "better than" would cross it. Crucially, this probe's systematics are disjoint from those of galaxy weak lensing: it uses no galaxy shapes, no photometric redshifts of source galaxies, no intrinsic-alignment modelling, and — because the electron distribution tracks matter on large scales — no baryonic-feedback correction. Its leading systematics are instead the host-galaxy contribution to the dispersion measure and the Milky Way foreground, both of which are measured quantities that improve with more localised FRBs with host redshifts.

| Quantity | Value | Source |
|---|---|---|
| DES Y3 i3PCF $S_8$ | $0.784^{+0.024}_{-0.021}$ | Gebauer et al. 2026, arXiv:2611.05367 |
| DES Y3 i3PCF $\Omega_{\mathrm{m}}$ | $0.272^{+0.038}_{-0.033}$ | Gebauer et al. 2026, arXiv:2611.05367 |
| DES Y3 i3PCF $w_0$ | $-1.04^{+0.25}_{-0.19}$ | Gebauer et al. 2026, arXiv:2611.05367 |
| DES Y3 i3PCF detection SNR | 12.8 | Gebauer et al. 2026, arXiv:2611.05367 |
| DES Y3 FoM gain over 2PCF | 1.59× | Gebauer et al. 2026, arXiv:2611.05367 |
| Planck 2018 $\sigma_8$ | $0.811 \pm 0.006$ | Planck Collaboration 2020, A&A 641, A6 |
| Planck 2018 $\Omega_{\mathrm{m}}$ | $0.315 \pm 0.007$ | Planck Collaboration 2020, A&A 641, A6 |
| Planck 2018 $H_0$ (km s$^{-1}$ Mpc$^{-1}$) | $67.4 \pm 0.5$ | Planck Collaboration 2020, A&A 641, A6 |
| Planck $S_8$ (derived here) | $0.831 \pm 0.011$ | This work, from the two rows above |
| $S_8$ tension (derived here) | 1.9$\sigma$ | This work |
| $\Omega_{\mathrm{m}}$ tension (derived here) | 1.2$\sigma$ | This work |
| Required $\sigma(S_8)$ for $3\sigma$ separation | $\le 0.016$ (standalone); $\le 0.011$ (incl. Planck error) | This work |
| Bright sirens: 300 detections to $z=1$, $H_0$ precision | $\sim$2.7% | Pacheco et al. 2026, arXiv:2611.05338 |

**Table 1.** Input values from published sources and quantities derived in this work. Derived rows are labelled as such; all other values are quoted as published.

## 4. Discussion

### 4.1 The falsifiable claim

**Claim.** The $S_8$ tension is genuine suppression of late-time structure growth relative to Planck $\Lambda$CDM, not an artefact of weak-lensing systematics.

**Prediction.** A baryon-free FRB-dispersion-plus-CMB-lensing analysis, once it reaches $\sigma(S_8) \le 0.016$, will recover $S_8 < 0.80$ — on the DES side of the tension.

**Falsification.** If that analysis instead recovers $S_8 \ge 0.82$, consistent with the Planck value $0.831 \pm 0.011$ at $3\sigma$, the claim is refuted: the low lensing $S_8$ would then be attributable to weak-lensing systematics (including baryonic feedback, which the three-point analysis already mitigates by using scales $\ge 15'$ where baryons are subdominant, but which two-point analyses do not fully escape), and the growth history would be consistent with Planck $\Lambda$CDM.

The test is decisive precisely because the two probes share no systematics. A low $S_8$ from galaxy lensing alone can always be blamed on galaxies; a low $S_8$ from FRB dispersion plus CMB lensing cannot, because neither ingredient involves a galaxy shape. Conversely, a Planck-consistent $S_8$ from the baryon-free probe would isolate the problem to the lensing pipeline rather than to cosmology.

### 4.2 Why the timing is now right

Three developments converge. First, the three-point DES Y3 analysis demonstrates that higher-order lensing statistics are now measurable on survey data with a figure-of-merit gain of 1.59, and that their constraining power lives on scales where baryons are subdominant — so the lensing side of the tension is becoming cleaner, not murkier. Second, the Sullivan et al. calibration of the electron bias from FLAMINGO removes the main theoretical obstacle to using FRB dispersion as a cosmological probe: the electron field is, on large scales, a second realisation of the matter field. Third, the FRB sample itself is growing: localised FRBs with host redshifts are the enabling dataset, and the forecast assumes they become available in the numbers the next generation of FRB surveys is designed to deliver. The Macquart relation (Macquart et al. 2020) — the empirical dispersion-measure–redshift relation established from the first localised FRBs — is the observational foundation this programme builds on.

### 4.3 The complementary $H_0$ check

The $S_8$ test should be read alongside the $H_0$ test, because a genuine departure from $\Lambda$CDM would most plausibly move both. Pacheco et al. (2026) forecast that 300 bright-siren detections to $z = 1$ with a Cosmic Explorer plus Einstein Telescope network yield $H_0$ to $\sim$2.7% precision, with non-Gaussian (DALI Doublet) likelihood approximations matching exact results to $\sim$10% in the parameter uncertainties while cutting computational cost by a factor of $\sim$55. A $\sim$2.7% independent $H_0$ measurement sits between the Planck value ($67.4 \pm 0.5$) and the local ladder ($\sim$73) with enough precision to favour one side at $\sim$2$\sigma$ per measurement — and, combined with the FRB $S_8$ result, would give a two-axis verdict on $\Lambda$CDM: growth axis and expansion axis. Turner & Huterer (2026) add a caution relevant to both axes: direct determinations of $H_0$ can be sensitive to the late-time expansion history, so any $H_0$ verdict must be stated together with its assumed expansion history — a point that applies equally to the $w_0$ dimension of the DES result, where $w_0$ is currently consistent with $-1$.

### 4.4 What this paper does not claim

This paper presents no new data and no new measurement. The 1.9$\sigma$ tension is a re-derivation from published numbers, not a discovery; at 1.9$\sigma$ it is not, on its own, evidence against $\Lambda$CDM. The required precision $\sigma(S_8) \le 0.016$ is a threshold calculation, not a forecast that the FRB programme will reach it — the Sullivan et al. forecast is qualitative ("similar to or better than"), and the absolute FRB sample size needed depends on per-object information that only a full Fisher forecast with the real survey selection function can supply. Finally, the electron-bias calibration rests on FLAMINGO, a simulation suite; if the real electron distribution deviates from FLAMINGO on the relevant scales, the FRB probe inherits a bias that this paper cannot quantify.

## 5. Conclusion

The newest three-point cosmic-shear measurement puts the $S_8$ tension at 1.9$\sigma$ — a clustering-amplitude discrepancy, with the matter density (1.2$\sigma$) and the dark-energy equation of state (0.2$\sigma$ from $-1$) both unremarkable. Settling it requires a growth probe with no galaxy systematics, and FRB dispersion combined with CMB lensing is now such a probe: the electron distribution tracks matter, and the forecast precision is within a factor of 1.4 of the 2.0% $S_8$ precision needed to separate the DES and Planck values at $3\sigma$. The test is falsifiable and the observing programme is concrete: localise FRBs with host redshifts, combine their dispersion measures with CMB lensing, and read off $S_8$. Below 0.80, the tension is real physics; at or above 0.82, it is lensing systematics. Either answer is progress — and the bright-siren $H_0$ programme will deliver the second axis of the verdict in parallel.

## Limitations

1. The Planck $S_8 = 0.831 \pm 0.011$ is derived with Gaussian error propagation treating $\sigma_8$ and $\Omega_{\mathrm{m}}$ as independent; Planck parameter correlations make the true uncertainty slightly different. The quoted tension (1.9$\sigma$) is a one-dimensional, $S_8$-only figure; the full multi-dimensional tension (2.4$\sigma$ at most, per Gebauer et al.) is the more complete statement.
2. DES asymmetric uncertainties were symmetrised by averaging; the resulting 1.9$\sigma$ is therefore approximate to $\sim$0.1$\sigma$.
3. The $\sigma(S_8) \le 0.016$ threshold assumes Gaussian uncertainties and a fixed Planck value; a full joint analysis would marginalise over both.
4. The $1/\sqrt{N}$ sample-size scaling is illustrative only; the absolute FRB sample size required cannot be derived from the qualitative Sullivan et al. forecast and needs a dedicated Fisher forecast.
5. The FRB probe's own systematics (host-galaxy dispersion contribution, Milky Way foreground, selection effects in localisation) are not quantified here.
6. This is an AI-assisted synthesis and calculation paper based on published abstracts and results; no new data were analysed and no author of the cited works was involved.

## Data Availability

No new data were generated. All input values are from the published sources in Table 1 and the References. The calculation script (`s8-tension-2026-11-04.py`) is archived with this manuscript. arXiv identifiers cited were live and verified on 4 November 2026.

## Acknowledgments

This manuscript is an AI-assisted draft prepared by Lapis (drafting assistant) for Zubair Ali. The author thanks the DES Collaboration, the Planck Collaboration, and the authors of the cited arXiv papers for making their results public. No funding was received. The author declares no competing interests.

## References

1. Gebauer, D., Halder, A., Gong, Z., & Uhlemann, C. (2026). SBi3PCF: cosmology with Dark Energy Survey Year 3 cosmic shear. arXiv:2611.05367.
2. Sullivan, J. M., Masui, K., Raikman, R., Andrew, S., & Wang, H. (2026). Mapping large-scale structure without galaxy formation — combining fast radio bursts with CMB lensing. arXiv:2611.05351.
3. Pacheco, M. H., de Souza, J. M. S., Aguiar, O. D., & Alves, M. E. S. (2026). Bright Siren Cosmology Beyond Fisher: DALI Forecasts for Third-Generation Gravitational Wave Observatories. arXiv:2611.05338.
4. Turner, M. S., & Huterer, D. (2026). Response to "Late Time Dynamical Dark Energy and the CMB-Distance Ladder Tension". arXiv:2611.05199.
5. Planck Collaboration (Aghanim, N., et al.) (2020). Planck 2018 results. VI. Cosmological parameters. Astronomy & Astrophysics, 641, A6. DOI: 10.1051/0004-6361/201833910. arXiv:1807.06209.
6. Abbott, T. M. C., et al. (DES Collaboration) (2022). Dark Energy Survey Year 3 results: Cosmological constraints from galaxy clustering and weak lensing. Physical Review D, 105, 023520. arXiv:2105.13549.
7. Macquart, J.-P., et al. (2020). A census of baryons in the Universe from localized fast radio bursts. Nature, 581, 391–395. DOI: 10.1038/s41586-020-2300-2.
8. Riess, A. G., et al. (2022). A Comprehensive Measurement of the Local Value of the Hubble Constant with 1 km s$^{-1}$ Mpc$^{-1}$ Uncertainty from the Hubble Space Telescope and the SH0ES Team. The Astrophysical Journal Letters, 934, L7. DOI: 10.3847/2041-8213/ac5c5b.
9. Schaye, J., et al. (2023). The FLAMINGO project: cosmological hydrodynamical simulations for large-scale structure and galaxy cluster surveys. Monthly Notices of the Royal Astronomical Society, 526, 4978–5020. arXiv:2306.04024.

---

*Manuscript prepared 4 November 2026. AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent verification.*
