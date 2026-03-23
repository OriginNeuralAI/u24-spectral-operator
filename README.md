<div align="center">

<img src="assets/hero-24cell.svg" alt="U24 Spectral Operator — 24-cell polytope projection" width="720"/>

# U&#x2082;&#x2084; Spectral Operator

**Bryan Daugherty &middot; Gregory Ward &middot; Shawn Ryan**

*March 2026*

---

[![arXiv](https://img.shields.io/badge/arXiv-2603.XXXXX-b31b1b.svg)](https://arxiv.org/abs/2603.XXXXX)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.XXXXXXX-blue.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![Data: Open](https://img.shields.io/badge/Data-Open-brightgreen.svg)](#data)
[![Verification](https://img.shields.io/badge/Verification-133%2F133_checks-D4AF37.svg)](#verification)
[![Reproducible](https://img.shields.io/badge/Reproducible-with_public_tools-blue.svg)](#notebooks)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)

</div>

---

## Papers

| Paper | Description | PDF | LaTeX |
|-------|-------------|-----|-------|
| **A Spectral Operator for the Riemann Hypothesis** (v12.0) | Self-adjoint H&#x2083; on C&#xB2;&#xB3; &#x2297; L&#xB2;([0,2&#x3C0;]), 5M zeta zeros verified | [PDF](papers/spectral-operator/main.pdf) | [TeX](papers/spectral-operator/main.tex) |
| **The Universality Constant: Eleven Paths to &#x3A9; = 24** (v1.3) | Derives &#x3B1;&#x2091;&#x2098; &#x2248; 1/137.03 from Monster group, zero free parameters | [PDF](papers/universality-constant/main.pdf) | [TeX](papers/universality-constant/main.tex) |

## Key Result

We construct a self-adjoint operator **H&#x2083;** acting on **C&#xB2;&#xB3; &#x2297; L&#xB2;([0,2&#x3C0;])** whose spectral statistics reproduce Riemann zeta zero correlations to within &#x2016;R&#x2082; &#x2212; R&#x2082;&#x1D33;&#x1D41;&#x1D38;&#x2016;&#x2082; = **0.026**. The 23-dimensional internal space is fixed uniquely by requiring H&#x2082; = 0 for the spacing manifold (verified from N = 10&#xB3; to height ~10&#xB2;&#xB2;), recovering the Leech lattice &#x39B;&#x2082;&#x2084; and linking the operator's spectrum to Monster group moonshine. As a corollary, the universality constant **&#x3A9; = 24** determines the fine-structure constant &#x3B1;&#x2091;&#x2098; = 1/137.035999... with zero free parameters.

## Transparency Statement

> **What the Isomorphic Engine computed.** The proprietary Engine (Rust, v0.12.0) performed: (1) Riemann-Siegel zero-finding up to N = 5,000,000, (2) 9-scale pair correlation R&#x2082;(r) convergence table, (3) Gamma&#x2080;(23) quantum graph secular eigenvalues, (4) Li coefficient, Weil explicit formula, and Beurling-Nyman distance computations, (5) perturbation sweeps and form factor analysis. The Engine itself is not released.
>
> **What we release.** All numerical outputs from those computations are in `data/`. The 9-scale R&#x2082; convergence table (`data/pair-correlation/`), the Reeds endomorphism and coupling matrix J (`data/reeds/`), the quantum graph structure (`data/quantum-graph/`), and all zero datasets are provided as structured JSON. The script `scripts/reconstruct_J.py` rebuilds the 23&#xD7;23 coupling matrix from the Reeds table alone&#x2014;no Engine needed.
>
> **What you can verify independently.** Every claim about GUE statistics at N &#x2264; 2000 is reproducible using the provided `.npy` zero files and standard Python (NumPy, SciPy). The power-law convergence &#x3B1; = 0.2833 can be verified by fitting the 9-scale table. The coupling matrix eigenspectrum, basin structure, and &#x3A9; = 24 relationships are fully derivable from the Reeds table.
>
> **What requires trust.** The zero-finding at N > 2000 and the Odlyzko-height blocks rely on the Engine's Riemann-Siegel implementation. We provide the numerical outputs but cannot release the source code.

## Verification

**133 / 133** automated checks pass across four categories:

| Category | Checks | Description |
|----------|--------|-------------|
| Structural | 46 | Operator self-adjointness, domain density, spectral resolution |
| RH Bridge | 26 | Isomorphic Engine certificate validation, zero matching |
| GUE Form Factor | 46 | Pair correlation R&#x2082;(r), level spacing, KS tests |
| Spectral Inclusion | 15 | Monster prime peaks detected in spectral data (14/15) |

## Repository Structure

```
u24-spectral-operator/
├── papers/
│   ├── spectral-operator/       # RH paper (v12.0) — .tex + .pdf
│   └── universality-constant/   # Omega paper (v1.3) — .tex + .pdf
├── data/
│   ├── riemann-zeros/           # 50, 500, 2000 zeros + 1000 GPU (RTX 5070 Ti)
│   ├── eigenvalue-verification/ # 200-zero KS test vs GUE
│   ├── rh-bridge/               # Isomorphic Engine verification certificate
│   ├── h2-topology/             # H2=0 persistent homology (7 scales)
│   ├── odlyzko/                 # Odlyzko zeros near 10^21 and 10^22
│   ├── spectral-unity/          # DSC-1 dataset, Lehmer predictions, moonshine
│   ├── reeds/                   # Reeds endomorphism + coupling matrix J
│   ├── pair-correlation/        # 9-scale R₂ convergence, perturbation, form factor
│   └── quantum-graph/           # Gamma_0(23) quantum graph structure
├── notebooks/                   # 8 Jupyter notebooks (guided analysis)
├── scripts/                     # Validation, reconstruction, figure generation
├── figures/                     # Generated output
└── assets/                      # Hero SVG
```

## Data

All data files are included in this repository. No external downloads required.

| File | Location | Records | Description |
|------|----------|---------|-------------|
| `riemann_zeros_50.json` | `data/riemann-zeros/` | 50 | First 50 non-trivial zeros (LMFDB/Odlyzko) |
| `riemann_zeros_500.npy` | `data/riemann-zeros/` | 500 | 30-digit precision |
| `riemann_zeros_2000.npy` | `data/riemann-zeros/` | 2,000 | 30-digit precision |
| `riemann_gpu_tf32_1000.json` | `data/riemann-zeros/` | 1,000 | RTX 5070 Ti, 100-digit precision |
| `eigenvalue_verification_200.json` | `data/eigenvalue-verification/` | 200 | KS test, 2-sigma bands, Spearman &#x3C1; |
| `rh_verification_certificate.json` | `data/rh-bridge/` | 1 | Isomorphic Engine bridge certificate |
| `h2_scaling_verification.json` | `data/h2-topology/` | 7 scales | H&#x2082;=0 from N=10&#xB3; to height ~10&#xB2;&#xB2; |
| `h2_extended_results.json` | `data/h2-topology/` | 7 scales | Vietoris-Rips persistent homology |
| `odlyzko_1e21.npy` | `data/odlyzko/` | ~1,000 | Zeros near height 10&#xB2;&#xB9; |
| `odlyzko_1e22.npy` | `data/odlyzko/` | ~1,000 | Zeros near height 10&#xB2;&#xB2; |
| `experiment_results.json` | `data/spectral-unity/` | &mdash; | Full DSC-1 spectral unity dataset |
| `lehmer_predictions.csv` | `data/spectral-unity/` | 28,160 | Monster resonance Lehmer pair predictions |
| `moonshine_peaks.csv` | `data/spectral-unity/` | 15 | Monster primes + spectral peak data |
| `reeds_endomorphism_z23.json` | `data/reeds/` | 23 | Reeds lookup table, basin structure, cycle data |
| `coupling_matrix_J.json` | `data/reeds/` | 23&#xD7;23 | Reconstructed coupling matrix + eigenvalues |
| `r2_convergence_9scales.json` | `data/pair-correlation/` | 9 scales | R&#x2082; L&#x2082; from N=200 to 5M, &#x3B1;=0.2833 |
| `perturbation_sweep.json` | `data/pair-correlation/` | 9 | R&#x2082; and D&#x2095;&#x2096; vs perturbation &#x3B5; |
| `higher_correlations.json` | `data/pair-correlation/` | &mdash; | R&#x2083;, R&#x2084;, cluster T&#x2083; vs GUE |
| `form_factor_k2.json` | `data/pair-correlation/` | 20 | K&#x2082;(&#x3C4;), &#x3A3;&#xB2;(L), spectral rigidity |
| `gamma0_23_graph.json` | `data/quantum-graph/` | 15 bonds | &#x393;&#x2080;(23) quantum graph structure |

See [`data/README.md`](data/README.md) for the full data dictionary.

## Notebooks

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [Explore Data](notebooks/01_explore_data.ipynb) | Guided tour of the spectral unity dataset |
| 02 | [Lehmer Pair Resonance](notebooks/02_lehmer_pair_resonance.ipynb) | Monster resonance formula verification |
| 03 | [Moonshine Peaks](notebooks/03_moonshine_peaks.ipynb) | 14/15 Monster primes detected in spectrum |
| 04 | [GUE Universality](notebooks/04_gue_universality.ipynb) | Pair correlation + level spacing analysis |
| 05 | [Generate Predictions](notebooks/05_generate_predictions.ipynb) | Generate Lehmer pair predictions from formula |
| 06 | [Eigenvalue Verification](notebooks/06_eigenvalue_verification.ipynb) | 200+1000 zero GUE comparison, KS tests |
| 07 | [H&#x2082; Topology](notebooks/07_h2_topology.ipynb) | Persistent homology H&#x2082;=0 verification |
| 08 | [Coupling Matrix](notebooks/08_coupling_matrix_and_alpha.ipynb) | Reconstruct J from Reeds table, eigenspectrum, &#x3B1;&#x2083; |

### Setup

```bash
# Option A: Conda (recommended)
conda env create -f notebooks/environment.yml
conda activate u24-spectral-operator
jupyter notebook notebooks/

# Option B: pip
python -m venv .venv && source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r notebooks/requirements.txt
jupyter notebook notebooks/
```

### Reproduce figures

```bash
python scripts/regenerate_figures.py   # Regenerate all figures from data
python scripts/validate_data.py        # Run data integrity checks
python scripts/reconstruct_J.py       # Rebuild coupling matrix from Reeds table
```

## Citation

If you use this data or analysis, please cite:

```bibtex
@article{daugherty2026spectral,
  title   = {A Spectral Operator for the {Riemann} Hypothesis},
  author  = {Daugherty, Bryan and Ward, Gregory and Ryan, Shawn},
  year    = {2026},
  month   = {March},
  note    = {v12.0, 133/133 automated verification checks}
}

@article{daugherty2026universality,
  title   = {The Universality Constant: Eleven Paths to $\Omega = 24$},
  author  = {Daugherty, Bryan and Ward, Gregory and Ryan, Shawn},
  year    = {2026},
  month   = {March},
  note    = {v1.3, zero free parameters}
}
```

See also [`CITATION.cff`](CITATION.cff) for machine-readable citation metadata.

## License

This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Papers, data, notebooks, and scripts are all freely available for reuse with attribution.

> The **Isomorphic Engine** itself remains proprietary and is not included in this repository.

---

<div align="center">

**&#x3A9; = 24** &nbsp;|&nbsp; **H&#x2083; = J&#x2297;I + I&#x2297;T + V&#x2095;&#x2096; + V&#x2098;** &nbsp;|&nbsp; **&#x3B1;&#x2091;&#x2098; = 1/137.03**

*OriginNeuralAI &middot; 2026*

</div>
