# Contributing to U₂₄ Spectral Operator

Welcome to the `U₂₄ Spectral Operator` repository! This repository serves as a comprehensive companion to our two papers, "A Spectral Operator Approach to the Riemann Hypothesis" and "The Universality Constant of U₂₄", providing the computational infrastructure, data, and verification tools for the presented research. We welcome contributions that enhance the clarity, reproducibility, and verifiability of our work.

## Environment Setup

This project requires Python 3.10 or higher. We recommend setting up your environment using Conda for consistency.

**Conda (Recommended):**
1.  Navigate to the root directory of this repository.
2.  Create the Conda environment:
    ```bash
    conda env create -f notebooks/environment.yml
    ```
3.  Activate the environment:
    ```bash
    conda activate u24-spectral-operator
    ```

**Pip (Alternative):**
1.  Ensure you have Python 3.10+ installed.
2.  Install the required packages:
    ```bash
    pip install -r notebooks/requirements.txt
    ```

## Running Validation

To verify the integrity and consistency of the data and key computational steps, run the primary validation script:

```bash
python scripts/validate_data.py
```

This script executes 140 automated checks across four categories, covering data format, consistency, mathematical properties, and cross-referencing between data files. Successful execution indicates that the repository's core data aligns with expected properties.

## Reproducing Figures

All figures presented in the accompanying papers can be regenerated using the dedicated script:

```bash
python scripts/regenerate_figures.py
```

This script will output all generated figures into the `figures/` directory. The main hero SVG figure can be specifically generated via `python scripts/generate_hero_svg.py`.

## Reproducing Key Results

The `notebooks/` directory contains 8 Jupyter notebooks that walk through the computational steps and verify key claims made in the papers. Below are specific notebooks crucial for reproducing central results:

*   **Notebook 04**: Verifies the GUE pair correlation (R₂ convergence at α = 0.2833).
*   **Notebook 06**: Conducts Eigenvalue Kolmogorov-Smirnov (KS) tests.
*   **Notebook 07**: Explores the H₂ = 0 topology across 7 scales.
*   **Notebook 08**: Demonstrates the coupling matrix J reconstruction from the Reeds table.

To run these notebooks, ensure your environment is set up (see "Environment Setup") and launch Jupyter Lab or Jupyter Notebook.

## Adding Verification Checks

The existing suite of 140 automated checks is a cornerstone of this repository's reliability. We encourage contributions that extend this suite. To add new verification checks:

1.  Examine `scripts/validate_data.py` to understand the existing structure and check categories.
2.  Implement your new check as a function within `validate_data.py` or a new module it imports.
3.  Ensure your check clearly states what it verifies and provides informative output upon success or failure.
4.  Integrate your new check into the main validation routine, categorizing it appropriately.

## Data Integrity

The `data/` directory contains approximately 20 data files (JSON, NPY, CSV) that are foundational to this research. SHA-256 checksums for all data files are provided in `data/checksums.sha256` for integrity verification. **It is critical that files within the `data/` directory are NOT manually modified.**

If you need to regenerate specific data (e.g., the coupling matrix J), use the provided scripts like `scripts/reconstruct_J.py`. Any regenerated data should be verified against the original checksums or clearly documented if a deviation is intentional and justified.

## Transparency Policy

This research leverages a combination of independently verifiable mathematical and computational methods alongside results derived from the "Isomorphic Engine" (a proprietary computational framework).

*   **Independently Verifiable**: All data integrity checks, figure reproductions, and the core mathematical claims demonstrated in Notebooks 04, 06, 07, and 08 are designed to be independently verifiable using the provided code and data.
*   **Isomorphic Engine Dependent**: Certain initial data generation steps or complex numerical optimizations, while their outputs are verifiable, rely on the "Isomorphic Engine" for their original computation. The outputs of these steps are provided in the `data/` directory and are subject to the same rigorous validation.

## Reporting Issues

We encourage users to report any issues they encounter. Please use the GitHub Issues tracker for:

*   **Data Discrepancies**: If `validate_data.py` reports an unexpected failure or if you find inconsistencies in the `data/` files.
*   **Mathematical Corrections**: If you identify potential errors or ambiguities in the mathematical derivations or claims presented.
*   **Code Bugs**: Any errors in the Python scripts or notebooks.

When reporting an issue, please provide a clear description, steps to reproduce (if applicable), and any relevant error messages or output.

## Code of Conduct

As an academic research repository, we expect all contributors and users to adhere to principles of academic integrity, respectful discourse, and proper attribution. Please engage constructively and professionally.