# The Archive Is the Telescope: What Physics-Based PSF Subtraction Predicts for Hidden Worlds in the JWST Archive — and the Cold Census It Unlocks

> **AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent verification.**

**Author:** Zubair Ali, Pharm-D student, SMBBMU Larkana, Pakistan · ORCID 0009-0001-5921-7509
**Drafting assistant:** Lapis (AI)
**Date:** 7 November 2026

## Abstract

Two results published in the first week of November 2026 change what existing
telescope data can still deliver. First, Ferrer-Chavez et al. (2026) demonstrate
Physics-based Learning for Imaging Planets (FLIP), a differentiable
model-based point-spread-function subtraction that improves JWST/NIRCam
coronagraphic sensitivity by a factor of 2–15 over the standard KLIP pipeline
and recovers 51 Eridani b at 4.3 μm, where KLIP returned a non-detection.
Second, Liu et al. (2026) show that "Capotauro", a candidate galaxy at
redshift $z \simeq 32$, moved by $132 \pm 20$ milliarcseconds over 3.5 years
and is instead a Y1 dwarf at $\sim$350 K and $730 \pm 110$ pc — one of the
most distant Y dwarfs known. We combine these results with the JADES census
of 41 T- and Y-dwarf candidates in 309.5 arcmin$^2$ and the two Bullet Cluster
dropouts confirmed as Y dwarfs, and we derive three quantitative, falsifiable
consequences. (1) FLIP-class reprocessing of the JWST coronagraphic archive:
from the single published KLIP non-detection that FLIP turned into a
$6.3\sigma$ detection, the one-sided 95% lower bound on the per-dataset
recovery rate is 5%; reprocessing 20 such datasets therefore has a $\ge$64%
probability of at least one new companion, and 59 datasets give $>$95%.
(2) The Habitable Worlds Observatory stability requirement — 100–1000 times
the stability of JWST — is reduced by the measured FLIP gain to a residual
gap of 6.7–500 times, i.e. from 2–3 orders of magnitude to 0.8–2.7. (3)
Capotauro's proper motion, $37.6$ mas yr$^{-1}$, implies a transverse
velocity of $\approx 130 \pm 20$ km s$^{-1}$ at 730 pc, consistent with
thick-disc/halo kinematics and with the JADES finding that most ultra-distant
candidates are metal-poor subdwarfs. We state the observing programmes that
would test each claim, including a 59-dataset falsification threshold for the
archive yield and a proper-motion screen for the next ultra-high-redshift
dropout candidates.

**Keywords:** exoplanets; direct imaging; JWST; PSF subtraction; brown dwarfs; Y dwarfs; high-redshift galaxies; Habitable Worlds Observatory

## 1. Introduction

Direct imaging of exoplanets is a fight against starlight. Even the
brightest young giant planets are about $10^5$ times fainter than their host
stars in the near-infrared, so the stellar point spread function (PSF) must
be modelled and subtracted to the required precision (Ferrer-Chavez et al.
2026). Until now the most successful approaches built the PSF model
empirically, from reference observations of other stars or the same star at
other times — and those approaches are fundamentally limited by telescope
instability: pointing errors and thermal drifts change the aberrations
between the reference and the science image, so the reference PSF never
quite matches the science PSF. The limit this sets is called the stability
limit, and it has bounded what direct imaging can do even from space.

On 4 November 2026, Ferrer-Chavez et al. published in *Nature* the first
successful application of differentiable model-based PSF subtraction to real,
on-sky coronagraphic data. Their framework, Physics-based Learning for
Imaging Planets (FLIP), builds a physical model of the JWST Near-Infrared
Camera (NIRCam), pre-calibrates it on a reference observation, and then
solves — by gradient descent, with $\sim 10^6$ free parameters — for the
small changes in telescope aberrations that explain the science image. The
result is a sensitivity gain of 2–15 times over the standard KLIP pipeline,
largest at the smallest separations, and the recovery of a planet KLIP could
not see at all. The data were already in the archive: the planet had been
photographed two years earlier and missed.

In the same week, a second lesson arrived from the opposite end of
astronomy. "Capotauro", a compact red source in the CEERS field proposed as
a galaxy at redshift $z \simeq 32$ — light from $\sim$100 million years
after the Big Bang — turned out to have moved. Liu et al. (2026) measured a
shift of $132 \pm 20$ milliarcseconds over 3.5 years, ruling out any
extragalactic source at $>6\sigma$, and identified the object as a Y-type
brown dwarf of $\sim$350 K at $730 \pm 110$ pc. Two further
F277W/F356W dropout candidates in the Bullet Cluster field, selected as
possible $z \sim 20$–30 galaxies, were likewise shown by spectroscopy and
proper motion to be Y dwarfs of 272–351 K and 445–525 K at $\sim$150–650 pc.
And the JADES survey had already found 41 T- and Y-dwarf candidates in
309.5 arcmin$^2$ of deep extragalactic imaging, with Y dwarfs reaching
1–2 kpc (Hainline et al. 2026).

This paper does three things. First, it turns the single published FLIP
recovery into a quantitative forecast for a systematic reprocessing of the
JWST coronagraphic archive, with an explicit falsification threshold (§3.1).
Second, it quantifies how much of the Habitable Worlds Observatory (HWO)
stability problem FLIP-class processing removes (§3.2). Third, it derives
the kinematics of Capotauro from its published proper motion and distance,
and states what a proper-motion screen of the next ultra-high-redshift
candidates should find (§3.3–§4).

## 2. Methods

### 2.1 Input values

All input numbers are taken from published sources, listed in Table 1. No
new observational data are presented. The FLIP values are taken from
Ferrer-Chavez et al. (2026, *Nature* 659, 58–62; DOI
10.1038/s41586-026-11213-z): sensitivity improvements of 2–15 times over
KLIP; $\sim$15 times at 0.5 arcsec and $\sim$5 times at 1 arcsec for TYC
5899; $\sim$5 times at 0.5 arcsec and $\sim$2.5 times at 1 arcsec for
51 Eridani in F430M; $\sim$4 times at the planet's location in F430M;
$1.6\times$ better signal-to-noise ratio (SNR) on HIP 65426 b; $2.1\times$
better SNR on 51 Eridani b in F410M; a SNR $= 6.3$ detection of 51 Eridani b
in F430M where the original publication reported a non-detection; the first
image of 51 Eridani b at 4.3 μm; $\sim 10^6$ free model parameters;
$\sim$35 minutes per optimisation on a normal NVIDIA A30 GPU; and the HWO
requirement of $10^{10}$ brightness contrast with picometre-level stability
100–1000 times that of JWST. The Capotauro values are taken from Liu et al.
(2026, arXiv:2608.07461): a shift of $132 \pm 20$ mas over 3.5 years,
proper motion $(\mu_\xi, \mu_\eta) = (+9.4, -35.6)$ mas yr$^{-1}$ (total
$37.6$ mas yr$^{-1}$), spectral type Y1.0 $\pm$ 0.5, temperature
$\approx$350 K, and distance $730 \pm 110$ pc. The Bullet Cluster dropout
values are taken from the July 2026 preprint (arXiv:2604.23668): two
candidates with Y-dwarf template temperatures of 272–351 K and 445–525 K,
distances $\sim$150–650 pc, and proper motions of $49 \pm 8$ and
$24 \pm 3$ mas yr$^{-1}$. The JADES values are taken from Hainline et al.
(2026, arXiv:2510.00111): 41 brown-dwarf candidates (31 T, 10 Y) across
309.5 arcmin$^2$; T dwarfs out to 5–6 kpc, Y dwarfs out to 1–2 kpc; proper
motions for nine candidates. The 51 Eridani system facts — planet discovered
in December 2014 with the Gemini Planet Imager, announced August 2015;
star $\sim$96 light-years away — are as reported in the discovery and
press coverage of the FLIP result.

### 2.2 Calculations

All derived quantities in §3 were computed with a short Python script
(`flip-archive-forecast-2026-11-07.py`, archived with this manuscript) and
are reproducible from the numbers in Table 1. The recovery-rate bound uses
the exact one-sided Clopper–Pearson interval: with $k = 1$ success in
$n = 1$ trial (the single KLIP non-detection dataset FLIP reprocessed that
contained a planet), the 95% lower bound $p_{\rm low}$ satisfies
$P(X \ge 1 \mid p_{\rm low}) = 0.05$, giving $p_{\rm low} = 0.05$.
Detection probabilities for $n$ reprocessed datasets assume independent
trials at that rate: $P(\ge 1) = 1 - (1 - p)^n$. The falsification
threshold uses the rule of three: zero successes in $n$ trials bounds the
rate at $p < 3/n$ at $\approx$95% confidence, so $n = 59$ is the smallest
sample whose null result excludes $p \ge 0.05$ ($3/59 = 0.051$). The
transverse velocity uses $v_t = 4.74\,\mu\,d$ km s$^{-1}$ with $\mu$ in
arcsec yr$^{-1}$ and $d$ in parsecs. The parallax at distance $d$ is
$1/d$ arcsec. Surface densities are candidate counts divided by the
survey area. The HWO residual stability gap is the published 100–1000
requirement divided by the measured FLIP gain of 2–15.

## 3. Results

### 3.1 The archive yield: what reprocessing 20 datasets should find

FLIP was tested on three on-sky datasets. In the two known-planet systems
it improved the SNR (HIP 65426 b by $1.6\times$, 51 Eridani b in F410M by
$2.1\times$), and in F430M it turned a published KLIP non-detection into a
$6.3\sigma$ detection of 51 Eridani b — the first image of the planet at
4.3 μm, in the carbon-dioxide absorption band that is inaccessible from the
ground. On the third system, TYC 5899, which has no known companion, FLIP
recovered injected fake planets that KLIP could not detect, with no false
positive: the gain is real signal, not overfitting.

The single decisive event for forecasting is the F430M recovery: among
KLIP non-detection datasets reprocessed so far, one out of one contained a
missed planet. One event is a weak foundation, and this paper does not
pretend otherwise — so we use the weakest reading the event supports. The
one-sided 95% lower bound on the per-dataset recovery rate is $p \ge 0.05$.
At that rate, reprocessing 20 KLIP non-detection NIRCam coronagraphic
datasets gives $P(\ge 1\ {\rm recovery}) = 1 - 0.95^{20} = 0.64$, and 59
datasets give $0.95$. In other words, even if the 51 Eridani recovery was
near the bottom of what the evidence allows, a 20-dataset programme is
better than even money to find a hidden companion, and a 59-dataset
programme is a $>$95% bet. The compute cost is trivial: at $\sim$35 minutes
per dataset on a single NVIDIA A30 GPU, 20 datasets cost $\sim$12
GPU-hours. The archive is the telescope, and the observing time is already
paid for.

### 3.2 The HWO stability gap, reduced

Imaging an Earth analogue around a Sun-like star requires $10^{10}$
contrast, and the HWO concept therefore demands picometre-level stability
100–1000 times that of JWST — stability that, as Ferrer-Chavez et al.
note, has not been achieved even in a laboratory. FLIP attacks exactly this
requirement: by solving for the aberration changes instead of trusting a
reference PSF, it circumvents the stability limit rather than engineering
around it. Dividing the published requirement by the measured gain, the
residual stability gap is $100/15 \approx 6.7$ in the best case
(100$\times$ requirement, 15$\times$ gain) and $1000/2 = 500$ in the worst
case — i.e. the gap shrinks from 2–3 orders of magnitude to 0.8–2.7 orders
of magnitude. The gain is also largest exactly where it matters most: for
TYC 5899 it is $\sim$15$\times$ at 0.5 arcsec versus $\sim$5$\times$ at
1 arcsec, and for 51 Eridani F430M $\sim$5$\times$ at 0.5 arcsec versus
$\sim$2.5$\times$ at 1 arcsec — a factor of $\sim$2–3 improvement in the
gain itself as the separation halves, towards the inner working angle where
Earth-like planets orbit. This does not remove the stability problem: even
the best case leaves a $\sim$7$\times$ gap, and FLIP's gains were measured
on giant planets at $10^5$ contrast, five orders of magnitude short of
$10^{10}$. But it changes the engineering target from "100–1000 times more
stable than anything built" to "roughly one order of magnitude, with
software doing the rest" — and it does so with a method already proven on
real data, not a simulation.

### 3.3 Capotauro's kinematics, and the cold census

Capotauro's measured shift, $132 \pm 20$ mas over 3.5 years, is a proper
motion of $37.7$ mas yr$^{-1}$ (consistent with the published total of
$37.6$ mas yr$^{-1}$). At the template distance of $730 \pm 110$ pc this
implies a transverse velocity $v_t = 4.74 \times 0.0376 \times 730
\approx 130 \pm 20$ km s$^{-1}$, where the uncertainty is dominated by the
$\pm$15% distance error. That velocity is far above the $\sim$20–40 km
s$^{-1}$ typical of thin-disc stars and is consistent with thick-disc or
halo kinematics — the same population the JADES analysis infers for most
of its ultra-distant candidates, which are best fit by sub-solar
metallicity models. Capotauro's geometric parallax at 730 pc would be
only $1.37$ mas, well below the $\sim$20 mas astrometric uncertainty of
the current measurement, which is why its distance remains photometric;
a dedicated third epoch designed for parallax, as Liu et al. propose,
is the way to turn the estimate into a measurement.

The census numbers put Capotauro in context. JADES found 41 candidates in
309.5 arcmin$^2$ — a surface density of $0.13$ arcmin$^{-2}$, with Y dwarfs
at $0.032$ arcmin$^{-2}$ — and 10 of them are Y dwarfs reaching 1–2 kpc.
The Bullet Cluster field yielded two further Y dwarfs from two dropout
candidates, with proper motions of $49 \pm 8$ and $24 \pm 3$ mas yr$^{-1}$
detected on only a $\sim$1-year baseline. The coldest known brown dwarf,
WISE J085510.83$-$071442.5 at $\sim$250 K, sits just 2 pc away; the
instruments that found it could not have seen it at 730 pc. JWST deep
fields are therefore, incidentally, the largest survey ever conducted of
the coldest substellar population — and every ultra-high-redshift candidate
list drawn from them carries a foreground of cold, moving dwarfs.

| Quantity | Value | Source |
|---|---|---|
| FLIP sensitivity gain over KLIP | 2–15× | Ferrer-Chavez et al. 2026, *Nature* 659, 58–62 |
| FLIP gain, TYC 5899, 0.5″ / 1″ | ~15× / ~5× | Ferrer-Chavez et al. 2026 |
| FLIP gain, 51 Eri F430M, 0.5″ / 1″ | ~5× / ~2.5× | Ferrer-Chavez et al. 2026 |
| FLIP gain at 51 Eri b location, F430M | ~4× | Ferrer-Chavez et al. 2026 |
| 51 Eri b, F430M (was KLIP non-detection) | SNR 6.3, first image at 4.3 μm | Ferrer-Chavez et al. 2026 |
| FLIP SNR gain, HIP 65426 b / 51 Eri b F410M | 1.6× / 2.1× | Ferrer-Chavez et al. 2026 |
| FLIP optimisation cost | ~10⁶ parameters, ~35 min, 1× NVIDIA A30 | Ferrer-Chavez et al. 2026 |
| HWO contrast / stability requirement | 10¹⁰ / 100–1000× JWST | Ferrer-Chavez et al. 2026 |
| Capotauro shift, 3.5-yr baseline | 132 ± 20 mas | Liu et al. 2026, arXiv:2608.07461 |
| Capotauro proper motion (total) | 37.6 mas yr⁻¹ | Liu et al. 2026 |
| Capotauro type / temperature / distance | Y1.0 ± 0.5 / ~350 K / 730 ± 110 pc | Liu et al. 2026 |
| Bullet Cluster dropouts: Teff / distance / μ | 272–351 K, 445–525 K / ~150–650 pc / 49 ± 8, 24 ± 3 mas yr⁻¹ | arXiv:2604.23668 |
| JADES candidates / area | 41 (31 T, 10 Y) / 309.5 arcmin² | Hainline et al. 2026, arXiv:2510.00111 |
| JADES Y-dwarf reach | 1–2 kpc | Hainline et al. 2026 |
| Recovery rate, per KLIP non-detection (derived) | ≥ 0.05 (95% lower bound) | This work, from the 1/1 event |
| P(≥1 recovery) in 20 / 59 datasets (derived) | 0.64 / 0.95 | This work |
| HWO residual stability gap (derived) | 6.7–500× (0.8–2.7 orders) | This work |
| Capotauro v_t (derived) | ≈ 130 ± 20 km s⁻¹ | This work, from μ and d above |
| Capotauro parallax at 730 pc (derived) | 1.37 mas | This work |

**Table 1.** Input values from published sources and quantities derived in this work. Derived rows are labelled as such; all other values are quoted as published.

## 4. Discussion

### 4.1 The falsifiable claims

**Claim 1 (archive yield).** FLIP-class reprocessing of KLIP
non-detection JWST/NIRCam coronagraphic datasets recovers missed
companions at a per-dataset rate of at least 5%.

**Prediction.** Reprocessing the first 20 such datasets will yield at
least one companion at SNR $\ge 5$; the probability is $\ge$64% under the
weakest reading of the published evidence.

**Falsification.** Zero recoveries in the first 59 reprocessed datasets
would bound the rate at $p < 3/59 \approx 0.051$ at $\approx$95%
confidence (rule of three), refuting the claim and showing the 51 Eridani
recovery was exceptional rather than representative. A single recovery
anywhere in the first 59 confirms the rate is at least of that order and
justifies reprocessing the full archive.

**Claim 2 (HWO stability).** Physics-based PSF subtraction reduces the
wavefront-stability requirement for Earth-analogue imaging by the measured
sensitivity gain at the relevant separations, leaving a residual gap of
one order of magnitude or less in the best case.

**Prediction.** Applying FLIP-class processing to simulated HWO-like
coronagraphic data at $10^{10}$-contrast-relevant separations will
recover injected Earth-analogue signals at a stability budget relaxed by
a factor of $\sim$2–15 relative to empirical reference subtraction.

**Falsification.** If the gain collapses below a factor of 2 at the
separations and contrasts where HWO must operate — because model mismatch
grows as the wavefront error shrinks, or because the $\sim 10^6$-parameter
optimisation overfits at low SNR — then the stability requirement stands
unreduced and the HWO engineering problem is unchanged.

**Claim 3 (cold census).** A substantial fraction of ultra-high-redshift
($z_{\rm phot} \gtrsim 20$) dropout candidates in JWST deep fields are
foreground Y dwarfs, identifiable by proper motion alone on a
$\sim$1–3.5-year baseline without spectroscopy.

**Prediction.** Among the next 10 dropout candidates at
$z_{\rm phot} \gtrsim 20$ selected for second-epoch imaging, at least 2
will show proper motion $>20$ mas yr$^{-1}$ — the scale already observed
for Capotauro ($37.6$ mas yr$^{-1}$) and the Bullet Cluster dwarfs
($49 \pm 8$ and $24 \pm 3$ mas yr$^{-1}$).

**Falsification.** If none of the next 10 candidates moves at
$>20$ mas yr$^{-1}$ on a $\ge$1-year baseline, the three moving dwarfs so
far were a follow-up-selected fluke, and proper motion is not a useful
screen for this population.

### 4.2 Why the two stories belong in one paper

FLIP and Capotauro are the same lesson from opposite directions. In both
cases the data were already taken, and the discovery was in the processing:
a planet photographed and missed because the PSF model trusted a reference
image, and a "galaxy" believed for a year because nobody had measured
whether it moved. The archive is full of both kinds of oversight — planets
hidden under residual starlight, and nearby cold objects hiding among
distant-galaxy candidates — and the tools that expose them are cheap:
gradient descent on a physical instrument model, and a second epoch of
imaging. Neither requires a new telescope. Both change what the next
telescope must be: HWO's stability budget is smaller than assumed, and the
next ultra-high-redshift claim must survive a proper-motion test before it
survives peer review.

There is a direct operational link, too. The 4.3 μm detection of
51 Eridani b matters because that wavelength holds the carbon-dioxide
absorption band, and CO$_2$ is a tracer of atmospheric metallicity — the
quantity that distinguishes formation pathways. Every companion FLIP
recovers in the archive is therefore not only a detection but a potential
atmospheric characterisation target at a wavelength ground-based telescopes
cannot reach. The same logic extends to the cold census: Y dwarfs at
272–525 K are the temperature analogues of the coldest directly imaged
planets, and a parallax-calibrated sample of them — the programme the
JADES parallax result of 5 November 2026 begins — calibrates the
atmospheric models that will be applied to planets FLIP finds.

### 4.3 What this paper does not claim

This paper presents no new data and no new measurement. The 5% recovery
rate is a lower bound derived from a single event, not a measured rate;
the true rate could be far higher (the only observed value is 1/1) or, if
51 Eridani was a favourable case, lower — which is exactly why the
59-dataset falsification threshold is stated. The HWO gap reduction divides
a measured sensitivity gain by an engineering requirement; it assumes the
gain transfers across five orders of magnitude of contrast, which is
unproven and is itself the falsifiable part of Claim 2. The transverse
velocity of Capotauro inherits the $\pm$15% photometric distance error and
the assumption that the template match (Y1.0 $\pm$ 0.5, $\sim$350 K) is
correct; the authors note the templates stop at Y1, so Capotauro could be
colder, fainter and closer. The dropout-screen prediction (Claim 3) is
based on a follow-up-selected sample of three objects, so its rate is an
expectation for candidates selected for second-epoch imaging, not a
population rate for all dropouts.

## 5. Conclusion

Two November 2026 results show that the most productive telescope of the
next year may be the archive. FLIP improves JWST coronagraphic sensitivity
by 2–15 times and has already recovered a planet from two-year-old data
that standard processing missed; even the weakest reading of that single
event implies a $\ge$64% chance of another recovery in the next 20
reprocessed datasets, at a cost of $\sim$12 GPU-hours, and zero recoveries
in 59 datasets would refute the forecast outright. The same method cuts
the Habitable Worlds Observatory stability gap from 2–3 orders of
magnitude to 0.8–2.7. And the coldest objects in the sky keep turning up
where galaxies were expected: Capotauro moved $132 \pm 20$ mas in 3.5
years, implying $\approx 130 \pm 20$ km s$^{-1}$ of transverse motion at
730 pc, and the JADES census shows such objects are common in exactly the
fields where the earliest galaxies are sought. Reprocess the archive, and
re-image the candidates: both tests are cheap, both are decisive, and both
can be run now.

## Limitations

1. The 5% recovery-rate bound rests on a single event (1 success in 1
   trial); the Clopper–Pearson lower bound is exact but wide, and the true
   rate is essentially unconstrained above 0.05.
2. The 20- and 59-dataset probabilities assume independent trials at a
   constant rate; real archive datasets share instruments, filters and
   target selections, so the effective rate may vary with separation,
   filter and stellar type.
3. The HWO gap reduction assumes the FLIP gain measured at $10^5$ contrast
   on giant planets transfers to $10^{10}$ contrast on Earth analogues; no
   evidence at that contrast exists yet.
4. Capotauro's transverse velocity uses a photometric distance
   ($730 \pm 110$ pc) with no geometric parallax; a 1.37 mas parallax is
   below the current astrometric precision, so the distance — and hence
   the velocity — could shift with a dedicated parallax epoch.
5. The dropout-screen prediction is calibrated on three follow-up-selected
   objects; it is an expectation for candidates chosen for second-epoch
   imaging, not a population rate.
6. This is an AI-assisted synthesis and calculation paper based on
   published results; no new data were analysed and no author of the cited
   works was involved.

## Data Availability

No new data were generated. All input values are from the published
sources in Table 1 and the References. The calculation script
(`flip-archive-forecast-2026-11-07.py`) is archived with this manuscript.
arXiv identifiers and the Nature DOI cited were live and verified on
7 November 2026.

## Acknowledgments

This manuscript is an AI-assisted draft prepared by Lapis (drafting
assistant) for Zubair Ali. The author thanks the authors of the cited
works for making their results public, and the JWST, JADES, CEERS and
NIRCam teams for the open archive that makes reprocessing possible. No
funding was received. The author declares no competing interests.

## References

1. Ferrer-Chavez, R., Wang, J. J., Bouman, K. L., et al. (2026). Imaging exoplanets below the telescope stability limit. *Nature*, 659, 58–62. DOI: 10.1038/s41586-026-11213-z.
2. Liu, F.-Y. F., McLeod, D. J., et al. (2026). A clear detection of proper motion confirms that the claimed $z \simeq 32$ galaxy candidate, "Capotauro", is a Y-type brown dwarf. *Monthly Notices of the Royal Astronomical Society*. arXiv:2608.07461.
3. Hainline, K. N., et al. (2026). JADES: An Abundance of Ultra-Distant T- and Y-Dwarfs in Deep Extragalactic Data. arXiv:2510.00111.
4. Bradač, M., Willott, C., Asada, Y., et al. (2026). Two Exciting High-redshift Galaxy Candidates Turn Out to Be Two Exciting Ultra-cool Brown Dwarfs. arXiv:2604.23668.
5. Balmer, W. O., et al. (2025). JWST-TST high contrast: living on the wedge, or, NIRCam bar coronagraphy reveals CO$_2$ in the HR 8799 and 51 Eri exoplanets' atmospheres. *The Astronomical Journal*, 169, 209.
6. Macintosh, B., et al. (2015). Discovery and spectroscopy of the young Jovian planet 51 Eri b with the Gemini Planet Imager. *Science*, 350, 64–67. DOI: 10.1126/science.aac5891.
7. Luhman, K. L. (2014). Discovery of a $\sim$250 K brown dwarf at 2 pc from the Sun. *The Astrophysical Journal Letters*, 786, L18. DOI: 10.1088/2041-8205/786/2/L18.
8. Boucher, S., et al. (2026). A Highly Reflective Atmosphere on the Lava World TOI-561b Revealed by JWST/NIRSpec Phase Curves. *The Astronomical Journal*. DOI: 10.3847/1538-3881/ae9763.
9. Kirkpatrick, J. D., et al. (2021). The field substellar mass function based on the full-sky 20 pc census of 525 L, T, and Y dwarfs. *The Astrophysical Journal Supplement Series*, 253, 7. DOI: 10.3847/1538-4365/abd107.

---

*Manuscript prepared 7 November 2026. AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent verification.*
