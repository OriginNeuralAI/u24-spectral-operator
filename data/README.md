# Data Dictionary

All data files needed to reproduce the analysis in both papers.

## riemann-zeros/

| File | Format | Size | Description |
|------|--------|------|-------------|
| `riemann_zeros_50.json` | JSON | 1.5 KB | First 50 non-trivial Riemann zeta zeros (LMFDB/Odlyzko verified) |
| `riemann_zeros_500.npy` | NumPy | 4 KB | First 500 zeros, 30-digit precision |
| `riemann_zeros_2000.npy` | NumPy | 16 KB | First 2000 zeros, 30-digit precision |
| `riemann_gpu_tf32_1000.json` | JSON | 1.6 KB | 1000 zeros computed on RTX 5070 Ti (TF32), 100-digit precision. Includes spacing statistics, GUE comparison (KS/AD tests), pair correlation MSE, and timing data. **Note:** The `conclusion` field reads `"GUE_DEVIATION"` because the GPU run compared 999 spacings against 19,800 GUE samples using a strict KS test (p < 0.05). At N=1000 the finite-size deviation is expected; see `pair-correlation/r2_convergence_9scales.json` for the full 9-scale convergence showing R₂ L₂ = 0.194 at N=1000, well within the monotonic convergence trend to 0.026 at N=5M. |

## eigenvalue-verification/

| File | Format | Size | Description |
|------|--------|------|-------------|
| `eigenvalue_verification_200.json` | JSON | 5 KB | Comparison of first 200 Riemann zero spacings against GUE predictions. Contains KS statistic (0.0512), 2-sigma match rate (91.2%), Spearman rho (1.0), and a 35-row detail table. |

## rh-bridge/

| File | Format | Size | Description |
|------|--------|------|-------------|
| `rh_verification_certificate.json` | JSON | 2.9 KB | Isomorphic Engine verification certificate for the RH bridge computation. **Note:** This certificate was generated from 3 scales (N=200, 500, 1000) and reports alpha=0.5396. The full 9-scale computation (N=200 to 5M) gives alpha=0.2833; see `pair-correlation/r2_convergence_9scales.json`. |

## h2-topology/

| File | Format | Size | Description |
|------|--------|------|-------------|
| `h2_scaling_verification.json` | JSON | 1.2 KB | Betti numbers (H0, H1, H2) computed across 7 scales from N=10^3 to height ~10^22. Confirms H2=0 at all scales. Scales 6-7 (heights ~10^21, ~10^22) use the Odlyzko zeros from `odlyzko/`. |
| `h2_extended_results.json` | JSON | 1.5 KB | Vietoris-Rips persistent homology (ripser/gudhi) on R^3 sliding-window embedding. 7 scales (n=100 to 1000). H2=0 everywhere, max H2 lifetime < 0.1. |

## odlyzko/

| File | Format | Size | Description |
|------|--------|------|-------------|
| `odlyzko_1e21.npy` | NumPy | 80 KB | 10,000 unfolded zero positions near height 10^21 (derived from Odlyzko's tables). Consecutive differences give normalized spacings. |
| `odlyzko_1e22.npy` | NumPy | 80 KB | 10,000 unfolded zero positions near height 10^22 (derived from Odlyzko's tables). Consecutive differences give normalized spacings. |

## spectral-unity/

| File | Format | Size | Description |
|------|--------|------|-------------|
| `experiment_results.json` | JSON | 7 KB | Full DSC-1 spectral unity dataset. Contains 50 Riemann zeros with phi mapping, four-wall and thirteen-wall frequency spectra, moonshine data (15 Monster primes, j-function coefficients, peak locations), 4 Lehmer pairs, GUE statistics, horizon entropy rankings, K3-zeta duality, Busy Beaver values, and 7 verification entries. |
| `lehmer_predictions.csv` | CSV | 920 KB | 28,160 predicted Lehmer pair locations from the Monster resonance formula. Columns: `gamma_predicted`, `k`, `prime_i`, `prime_j`, `formula`. Sorted by gamma. All primes are Monster primes. |
| `moonshine_peaks.csv` | CSV | 0.5 KB | 15 Monster primes with spectral peak data. Columns: `prime`, `exponent_in_monster`, `r_p`, `weight`, `status`. 14/15 peaks detected in the spectral data. |

## reeds/

| File | Format | Size | Description |
|------|--------|------|-------------|
| `reeds_endomorphism_z23.json` | JSON | 4 KB | Complete Reeds lookup table f: Z₂₃ → Z₂₃ (reverse-engineered by Jim Reeds from Bodley MS 908). Includes the numeric table, 4 attractor basins (Creation/Perception/Stability/Exchange), cycle structure (3,3,2,1), basin sizes 9+7+1+6=23, coupling construction formula, and all constants (α_D, Ω, Kramers barriers). |
| `coupling_matrix_J.json` | JSON | 15 KB | The 23×23 Daugherty coupling matrix J, reconstructed from the Reeds table by `scripts/reconstruct_J.py`. Includes the full matrix, eigenvalues, basin classification, and adjacency matrix eigenvalues. |

## pair-correlation/

| File | Format | Size | Description |
|------|--------|------|-------------|
| `r2_convergence_9scales.json` | JSON | 2 KB | **Key dataset.** Pair correlation R₂(r) L₂ distance from GUE at 9 scales: N=200, 500, 1K, 5K, 10K, 100K, 500K, 1M, 5M. Shows monotonic convergence with power-law exponent α=0.2833 (1000-resample bootstrap, 95% CI). R₂ drops from 0.465 at N=200 to 0.026 at N=5M. |
| `perturbation_sweep.json` | JSON | 1 KB | R₂ and Hausdorff-Prokhorov distance D_HP as a function of perturbation strength ε (0 to 5). R₂ consistency breaks at ε ≈ 0.49; D_HP grows monotonically. |
| `higher_correlations.json` | JSON | 0.5 KB | R₃ and R₄ correlation functions + cluster function T₃ at N=500. All match GUE predictions (not Poisson). |
| `form_factor_k2.json` | JSON | 3 KB | GUE form factor K₂(τ): ramp slope 1.897 (GUE=1.0), plateau 1.010 (GUE=1.0). Spectral rigidity Δ₃(L): best match GUE. Number variance Σ²(L) for L=1..20: all GUE. |

## quantum-graph/

| File | Format | Size | Description |
|------|--------|------|-------------|
| `gamma0_23_graph.json` | JSON | 3 KB | Γ₀(23) quantum graph: 2 cusps, 15 bonds (primes ≤ 47), bond lengths c·log(p). Includes Berkolaiko-Winn conditions (2/4 satisfied), secular eigenvalue count (160), and KS comparison with zeta zeros. |

## Loading data

```python
import json
import numpy as np
import pandas as pd

# JSON
with open('data/spectral-unity/experiment_results.json') as f:
    data = json.load(f)

# NumPy
zeros_500 = np.load('data/riemann-zeros/riemann_zeros_500.npy')

# CSV
lehmer = pd.read_csv('data/spectral-unity/lehmer_predictions.csv')

# Reeds endomorphism
with open('data/reeds/reeds_endomorphism_z23.json') as f:
    reeds = json.load(f)
table = reeds['reeds_table']['numeric_table']  # [2, 2, 3, 5, 14, ...]

# 9-scale convergence
with open('data/pair-correlation/r2_convergence_9scales.json') as f:
    r2 = json.load(f)
for scale in r2['scales']:
    print(f"N={scale['n_zeros']:>8d}  R2={scale['r2_l2']:.6f}")
```
