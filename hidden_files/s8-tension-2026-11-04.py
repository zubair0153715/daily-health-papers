"""Own analysis for Paper #5 (2026-11-04, Space): S8 tension recomputation.

Inputs (all published, verified 2026-11-04):
- DES Y3 integrated 3-point cosmic shear (Gebauer et al., arXiv:2611.05367):
  S8 = 0.784 (+0.024 / -0.021); Omega_m = 0.272 (+0.038 / -0.033);
  w0 = -1.04 (+0.25 / -0.19); zeta_pm detected at SNR 12.8;
  figure-of-merit gain 1.59x over 2-point alone.
- Planck 2018 base-LCDM (Planck Collaboration, A&A 641, A6, 2020;
  arXiv:1807.06209; DOI 10.1051/0004-6361/201833910):
  sigma8 = 0.811 +/- 0.006; Omega_m = 0.315 +/- 0.007; H0 = 67.4 +/- 0.5.
- Bright sirens (Pacheco et al., arXiv:2611.05338):
  300 bright-siren detections to z = 1 -> H0 ~2.7% (Doublet) vs ~2.5% (exact).

Derived here: Planck S8 from sigma8 and Omega_m (S8 = sigma8 * sqrt(Omega_m/0.3));
1-D S8 and Omega_m tensions (Gaussian error propagation, correlations ignored --
stated as a limitation); the S8 precision a new probe needs to separate the two
values at 3 sigma.
"""
import math

# --- Planck 2018 S8, derived ---
s8_planck = 0.811 * math.sqrt(0.315 / 0.3)
rel = math.sqrt((0.006 / 0.811) ** 2 + (0.5 * 0.007 / 0.315) ** 2)
sig_s8_planck = s8_planck * rel
print(f"Planck S8 (derived) = {s8_planck:.3f} +/- {sig_s8_planck:.3f}")

# --- DES Y3 i3PCF, symmetrised errors ---
s8_des, sig_s8_des = 0.784, (0.024 + 0.021) / 2
om_des, sig_om_des = 0.272, (0.038 + 0.033) / 2
w0_des, sig_w0_des = -1.04, (0.25 + 0.19) / 2
print(f"DES S8 fractional precision = {sig_s8_des / s8_des * 100:.2f}%")

# --- 1-D tensions ---
d_s8 = s8_planck - s8_des
sig_comb = math.sqrt(sig_s8_planck ** 2 + sig_s8_des ** 2)
print(f"S8 tension: delta = {d_s8:.3f}, sigma_comb = {sig_comb:.4f}, "
      f"tension = {d_s8 / sig_comb:.2f} sigma")

d_om = 0.315 - om_des
sig_om_comb = math.sqrt(0.007 ** 2 + sig_om_des ** 2)
print(f"Omega_m tension: delta = {d_om:.3f}, sigma_comb = {sig_om_comb:.4f}, "
      f"tension = {d_om / sig_om_comb:.2f} sigma")

d_w0 = w0_des - (-1.0)
print(f"w0 offset from -1: {d_w0:.2f} ({abs(d_w0) / sig_w0_des:.2f} sigma)")

# --- Discrimination power required of a new, baryon-free probe ---
# Standalone 3-sigma separation of the two central values:
req_standalone = d_s8 / 3
# Accounting for Planck's own error as well:
req_with_planck = math.sqrt(max((d_s8 / 3) ** 2 - sig_s8_planck ** 2, 0))
print(f"Required sigma(S8) for 3-sigma separation (standalone) = "
      f"{req_standalone:.4f} ({req_standalone / s8_des * 100:.2f}% of DES value)")
print(f"Required sigma(S8) incl. Planck error = {req_with_planck:.4f} "
      f"({req_with_planck / s8_des * 100:.2f}%)")
# How much better than DES Y3 i3PCF precision is that?
print(f"Improvement over DES Y3 i3PCF precision needed: "
      f"{sig_s8_des / req_standalone:.2f}x (standalone) / "
      f"{sig_s8_des / req_with_planck:.2f}x (incl. Planck)")
# If precision scales as 1/sqrt(N) at fixed per-object information, the
# sample-size factor to reach the standalone requirement from DES-level
# precision (illustrative scaling only, no absolute N claimed):
print(f"Sample-size factor (1/sqrt(N) scaling) vs DES-level precision: "
      f"{(sig_s8_des / req_standalone) ** 2:.2f}x")
