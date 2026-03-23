# Notebooks

Eight Jupyter notebooks providing a guided analysis of the verification data.

> *Large-N results were generated with the proprietary Isomorphic Engine; these notebooks reproduce the analysis and figures from the released data.*

## Setup

```bash
# Option A: Conda (recommended)
conda env create -f environment.yml
conda activate u24-spectral-operator

# Option B: pip
pip install -r requirements.txt
```

Then launch:

```bash
jupyter notebook
```

## Notebook Index

| # | Notebook | Description |
|---|----------|-------------|
| 01 | `01_explore_data.ipynb` | Guided tour of the spectral unity dataset (experiment_results.json) |
| 02 | `02_lehmer_pair_resonance.ipynb` | Monster resonance formula: predict Lehmer pairs from Monster primes |
| 03 | `03_moonshine_peaks.ipynb` | Detect 14/15 Monster primes in the spectral pair correlation |
| 04 | `04_gue_universality.ipynb` | GUE pair correlation R_2(r) and level spacing analysis |
| 05 | `05_generate_predictions.ipynb` | Generate the 28,160 Lehmer pair predictions |
| 06 | `06_eigenvalue_verification.ipynb` | 200-zero KS test + 1000-zero GPU comparison vs GUE |
| 07 | `07_h2_topology.ipynb` | Persistent homology: H_2 = 0 at all scales |
| 08 | `08_coupling_matrix_and_alpha.ipynb` | Reconstruct coupling matrix J from Reeds table, eigenspectrum analysis |

## Dependencies

- Python 3.10+
- NumPy >= 1.21
- Matplotlib >= 3.5
- SciPy >= 1.7
- Pandas >= 1.3
- Jupyter

All notebooks use the data files in `../data/`. No external downloads or API keys required.
