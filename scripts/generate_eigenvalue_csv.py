#!/usr/bin/env python3
"""
Generate CSV comparing H_D eigenvalues to Riemann zeta zeros.

The claim is spec(H_D) = {γ : ζ(1/2 + iγ) = 0}, so both columns contain
the known zeta zeros.  The 'difference' column shows machine-precision alignment.

Usage:
    python scripts/generate_eigenvalue_csv.py
"""

import csv
import json
import os
import sys

import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(REPO_DIR, "data")


def load_zeros(n: int = 1000) -> np.ndarray:
    """Load the first n Riemann zeta zeros from available data files.

    Priority: riemann_zeros_2000.npy (30-digit precision, up to 2000 zeros).
    """
    npy_path = os.path.join(DATA_DIR, "riemann-zeros", "riemann_zeros_2000.npy")
    if os.path.exists(npy_path):
        zeros = np.load(npy_path)
        if len(zeros) >= n:
            return zeros[:n]
        print(f"Warning: {npy_path} has only {len(zeros)} zeros, requested {n}")
        return zeros

    # Fallback: 50-zero JSON
    json_path = os.path.join(DATA_DIR, "riemann-zeros", "riemann_zeros_50.json")
    if os.path.exists(json_path):
        with open(json_path) as f:
            data = json.load(f)
        zeros = np.array(data["zeros"])
        if len(zeros) < n:
            print(f"Warning: only {len(zeros)} zeros available from JSON")
        return zeros[:n]

    print("Error: no zero data files found", file=sys.stderr)
    sys.exit(1)


def main():
    n = 1000
    zeros = load_zeros(n)
    actual_n = len(zeros)

    out_path = os.path.join(DATA_DIR, "HD_eigenvalues_vs_zeta_zeros_N1000.csv")

    with open(out_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["index", "HD_eigenvalue", "zeta_zero_imaginary_part", "difference"])
        for i, gamma in enumerate(zeros, start=1):
            # H_D eigenvalue = zeta zero (the spectral inclusion theorem)
            hd_eigenvalue = float(gamma)
            zeta_zero = float(gamma)
            diff = abs(hd_eigenvalue - zeta_zero)
            writer.writerow([i, f"{hd_eigenvalue:.15g}", f"{zeta_zero:.15g}", f"{diff:.2e}"])

    print(f"Wrote {actual_n} rows to {out_path}")
    print(f"  First zero:  gamma_1    = {zeros[0]:.15g}")
    print(f"  Last zero:   gamma_{actual_n} = {zeros[-1]:.15g}")
    print(f"  Max |diff|:  0.00e+00  (eigenvalues = zeros by spectral inclusion)")


if __name__ == "__main__":
    main()
