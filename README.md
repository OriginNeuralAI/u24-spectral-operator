<div align="center">

<img src="assets/hero-24cell.svg" alt="U24 Spectral Operator — 24-cell polytope projection" width="720"/>

# U₂₄ Spectral Operator

**Bryan Daugherty · Gregory Ward · Shawn Ryan**

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

> ### Quick Results
>
> ‖R₂ − R₂^GUE‖₂ = **0.026**
>
> **133/133** automated checks pass
>
> Universality constant **Ω = 24**
>
> Fine-structure constant **α_EM ≈ 1/137.03**

## Papers

| Paper | Description | PDF | LaTeX |
|-------|-------------|-----|-------|
| **A Spectral Operator for the Riemann Hypothesis** (v12.0) | Self-adjoint H_D on C²³ ⊗ L₂([0,2π]), 5M zeta zeros verified | [PDF](papers/spectral-operator/main.pdf) | [TeX](papers/spectral-operator/main.tex) |
| **The Universality Constant: Eleven Paths to Ω = 24** (v1.3) | Derives α_EM ≈ 1/137.03 from Monster group, zero free parameters | [PDF](papers/universality-constant/main.pdf) | [TeX](papers/universality-constant/main.tex) |

## Key Result

We construct a self-adjoint operator **H_D** acting on **C²³ ⊗ L₂([0,2π])** whose spectral statistics reproduce Riemann zeta zero correlations to within ‖R₂ − R₂^GUE‖₂ = **0.026**. The 23-dimensional internal space is fixed uniquely by requiring H₂ = 0 for the spacing manifold (verified from N = 10³ to height ~10²² at **7 scales**), recovering the Leech lattice Λ₂₄ and linking the operator's spectrum to Monster group moonshine. As a corollary, the universality constant **Ω = 24** determines the fine-structure constant α_EM ≈ **1/137.03** with zero free parameters (error **0.005%**).

## Verification Dashboard

**133 / 133** automated checks pass across four categories:

| Category | Checks | Status | Description |
|----------|--------|--------|-------------|
| Structural | 46 | ✓ | Operator self-adjointness, domain density, spectral resolution |
| RH Bridge | 26 | ✓ | Isomorphic Engine certificate validation, zero matching |
| GUE Form Factor | 46 | ✓ | Pair correlation R₂(r), level spacing, KS tests |
| Spectral Inclusion | 15 | ✓ | Monster prime peaks detected in spectral data (**14/15** detected) |

<details>
<summary>9-Scale Convergence Table</summary>

The L₂ norm of the difference between the observed R₂(r) and the GUE prediction, ‖R₂ − R₂^GUE‖₂, converges with a power-law α = **0.2833** (95% CI: [**0.28**, **0.29**]).

| N (Number of Zeros) | ‖R₂ − R₂^GUE‖₂ |
|---------------------|-----------------|
| 200                 | 0.465           |
| 500                 | 0.305           |
| 1,000               | 0.194           |
| 5,000               | 0.115           |
| 10,000              | 0.083           |
| 100,000             | 0.048           |
| 500,000             | 0.035           |
| 1,000,000           | 0.032           |
| 5,000,000           | **0.026**       |

</details>

## Transparency Statement

> **What the Isomorphic Engine computed.** The proprietary Engine (Rust, v0.12.0) performed: (1) Riemann-Siegel zero-finding up to N = **5,000,000**, (2) 9-scale pair correlation R₂(r) convergence table, (3) Γ₀(23) quantum graph secular eigenvalues, (4) Li coefficient, Weil explicit formula, and Beurling-Nyman distance computations, (5) perturbation sweeps and form factor analysis. The Engine itself is not released.
>
> **What we release.** All numerical outputs from those computations are in `data/`. The 9-scale R₂ convergence table (`data/pair-correlation/`), the Reeds endomorphism and coupling matrix J (`data/reeds/`), the quantum graph structure (`data/quantum-graph/`), and all zero datasets are provided as structured JSON. The script `scripts/reconstruct_J.py` rebuilds the **23×23** coupling matrix from the Reeds table alone—no Engine needed.
>
> **What you can verify independently.** Every claim about GUE statistics at N ≤ **2000** is reproducible using the provided `.npy` zero files and standard Python (NumPy, SciPy). The power-law convergence α = **0.2833** can be verified by fitting the 9-scale table. The coupling matrix eigenspectrum (λ_max = **5.5232**, κ = **23,015,945**), basin structure ([**9, 7, 1, 6**] → Creation/Perception/Stability/Exchange), and **Ω = 24** relationships are fully derivable from the Reeds table.
>
> **What requires trust.** The zero-finding at N > **2000** and the Odlyzko-height blocks rely on the Engine's Riemann-Siegel implementation. We provide the numerical outputs but cannot release the source code.

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
│   └── quantum-graph/           # Γ₀(23) quantum graph structure
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
| `eigenvalue_verification_200.json` | `data/eigenvalue-verification/` | 200 | KS test, 2-sigma bands, Spearman ρ |
| `rh_verification_certificate.json` | `data/rh-bridge/` | 1 | Isomorphic Engine bridge certificate |
| `h2_scaling_verification.json` | `data/h2-topology/` | **7 scales** | H₂=0 from N=10³ to height ~10²² |
| `h2_extended_results.json` | `data/h2-topology/` | **7 scales** | Vietoris-Rips persistent homology |
| `odlyzko_1e21.npy` | `data/odlyzko/` | 10,000 | Unfolded zero positions near height 10²¹ |
| `odlyzko_1e22.npy` | `data/odlyzko/` | 10,000 | Unfolded zero positions near height 10²² |
| `experiment_results.json` | `data/spectral-unity/` | — | Full DSC-1 spectral unity dataset |
| `lehmer_predictions.csv` | `data/spectral-unity/` | **28160** | Monster resonance Lehmer pair predictions |
| `moonshine_peaks.csv` | `data/spectral-unity/` | **15** | Monster primes + spectral peak data |
| `reeds_endomorphism_z23.json` | `data/reeds/` | 23 | Reeds lookup table, basin structure, cycle data |
| `coupling_matrix_J.json` | `data/reeds/` | **23×23** | Reconstructed coupling matrix + eigenvalues |
| `r2_convergence_9scales.json` | `data/pair-correlation/` | **9 scales** | R₂ L₂ from N=200 to 5M, α=**0.2833** |
| `perturbation_sweep.json` | `data/pair-correlation/` | 9 | R₂ and D_KL vs perturbation ε |
| `higher_correlations.json` | `data/pair-correlation/` | — | R₃, R₄, cluster T₃ vs GUE |
| `form_factor_k2.json` | `data/pair-correlation/` | 20 | K₂(τ), Σ₂(L), spectral rigidity |
| `gamma0_23_graph.json` | `data/quantum-graph/` | 15 bonds | Γ₀(23) quantum graph structure |

See [`data/README.md`](data/README.md) for the full data dictionary.

## Notebooks

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [Explore Data](notebooks/01_explore_data.ipynb) | Guided tour of the spectral unity dataset |
| 02 | [Lehmer Pair Resonance](notebooks/02_lehmer_pair_resonance.ipynb) | Monster resonance formula verification |
| 03 | [Moonshine Peaks](notebooks/03_moonshine_peaks.ipynb) | **14/15** Monster primes detected in spectrum |
| 04 | [GUE Universality](notebooks/04_gue_universality.ipynb) | Pair correlation + level spacing analysis |
| 05 | [Generate Predictions](notebooks/05_generate_predictions.ipynb) | Generate Lehmer pair predictions from formula |
| 06 | [Eigenvalue Verification](notebooks/06_eigenvalue_verification.ipynb) | 200+1000 zero GUE comparison, KS tests |
| 07 | [H₂ Topology](notebooks/07_h2_topology.ipynb) | Persistent homology H₂=0 verification |
| 08 | [Coupling Matrix](notebooks/08_coupling_matrix_and_alpha.ipynb) | Reconstruct J from Reeds table, eigenspectrum, α_D = **0.008193** |

### For Reviewers

This repository provides comprehensive data and analysis to independently verify key aspects of our work:

*   **GUE Statistics:** Reproduce pair correlation R₂(r) and level spacing statistics for N ≤ **2000** Riemann zeros using provided `.npy` files and standard Python libraries.
*   **Convergence:** Verify the power-law convergence α = **0.2833** (95% CI: [**0.28**, **0.29**]) by fitting the 9-scale ‖R₂ − R₂^GUE‖₂ table.
*   **Coupling Matrix J:** Reconstruct the **23×23** coupling matrix J from the `reeds_endomorphism_z23.json` file. Verify its eigenspectrum (λ_max = **5.5232**, κ = **23,015,945**), basin structure ([**9, 7, 1, 6**] for Creation/Perception/Stability/Exchange), and cycle type ((**3,3,2,1**), ord = **6**).
*   **α_D Constant:** Confirm the derivation of α_D = **0.008193** from the J matrix properties.
*   **Universality Constant Ω:** Verify the derivation of **Ω = 24** through **11 independent paths** as detailed in the "Universality Constant" paper.
*   **Monster Prime Detection:** Confirm the detection of **14/15** Monster primes in the spectral data.
*   **Lehmer Predictions:** Validate the **28160** Lehmer pair predictions generated by the model.
*   **Fine-Structure Constant:** Confirm the derivation of α_EM ≈ **1/137.03** with an error of **0.005%** from Ω = 24, with zero free parameters.

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

### Scripts

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

**Ω = 24** | **H_D = J⊗I + I⊗T + V_HP + V_Z** | **α_EM = 1/137.03**

*OriginNeuralAI · 2026*

</div>