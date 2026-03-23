# Data Dictionary

All data files needed to reproduce the analysis in both papers.

## riemann-zeros/

| File | Format | Size | Description |
|------|--------|------|-------------|
| `riemann_zeros_50.json` | JSON | 1.5 KB | First 50 non-trivial Riemann zeta zeros (LMFDB/Odlyzko verified) |
| `riemann_zeros_500.npy` | NumPy | 4 KB | First 500 zeros, 30-digit precision |
| `riemann_zeros_2000.npy` | NumPy | 16 KB | First 2000 zeros, 30-digit precision |
| `riemann_gpu_tf32_1000.json` | JSON | 1.6 KB | 1000 zeros computed on RTX 5070 Ti (TF32), 100-digit precision. Includes spacing statistics, GUE comparison (KS/AD tests), pair correlation MSE, and timing data. |

## eigenvalue-verification/

| File | Format | Size | Description |
|------|--------|------|-------------|
| `eigenvalue_verification_200.json` | JSON | 5 KB | Comparison of first 200 Riemann zero spacings against GUE predictions. Contains KS statistic (0.0512), 2-sigma match rate (91.2%), Spearman rho (1.0), and a 35-row detail table. |

## rh-bridge/

| File | Format | Size | Description |
|------|--------|------|-------------|
| `rh_verification_certificate.json` | JSON | 2.9 KB | Isomorphic Engine verification certificate for the RH bridge computation. Documents the bridge between operator eigenvalues and zeta zeros. |

## h2-topology/

| File | Format | Size | Description |
|------|--------|------|-------------|
| `h2_scaling_verification.json` | JSON | 1.2 KB | Betti numbers (H0, H1, H2) computed across 7 scales from N=10^3 to height ~10^22. Confirms H2=0 at all scales. |
| `h2_extended_results.json` | JSON | 1.5 KB | Vietoris-Rips persistent homology (ripser/gudhi) on R^3 sliding-window embedding. 7 scales (n=100 to 1000). H2=0 everywhere, max H2 lifetime < 0.1. |

## odlyzko/

| File | Format | Size | Description |
|------|--------|------|-------------|
| `odlyzko_1e21.npy` | NumPy | 80 KB | ~1000 Riemann zeros near height 10^21 (Odlyzko's tables) |
| `odlyzko_1e22.npy` | NumPy | 80 KB | ~1000 Riemann zeros near height 10^22 (Odlyzko's tables) |

## spectral-unity/

| File | Format | Size | Description |
|------|--------|------|-------------|
| `experiment_results.json` | JSON | 7 KB | Full DSC-1 spectral unity dataset. Contains 50 Riemann zeros with phi mapping, four-wall and thirteen-wall frequency spectra, moonshine data (15 Monster primes, j-function coefficients, peak locations), 4 Lehmer pairs, GUE statistics, horizon entropy rankings, K3-zeta duality, Busy Beaver values, and 7 verification entries. |
| `lehmer_predictions.csv` | CSV | 920 KB | 28,160 predicted Lehmer pair locations from the Monster resonance formula. Columns: `gamma_predicted`, `k`, `prime_i`, `prime_j`, `formula`. Sorted by gamma. All primes are Monster primes. |
| `moonshine_peaks.csv` | CSV | 0.5 KB | 15 Monster primes with spectral peak data. Columns: `prime`, `exponent_in_monster`, `r_p`, `weight`, `status`. 14/15 peaks detected in the spectral data. |

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
```
