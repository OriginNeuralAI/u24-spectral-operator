#!/usr/bin/env python3
"""
Regenerate all publication figures from released data.

This script reproduces every figure in the figures/ directory using only
the data stored in data/. No Isomorphic Engine required.

Usage:
    python scripts/regenerate_figures.py
"""

import json
import math
import os
import sys

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(REPO_DIR, "data")
FIGURES_DIR = os.path.join(REPO_DIR, "figures")

PHI = 1.618033988749895
MONSTER_ORDER = 808017424794512875886459904961710757005754368000000000
LOG_MONSTER = 124.13
MONSTER_WAVELENGTH = 19.76

# Navy / gold color scheme
NAVY = '#0A2540'
GOLD = '#D4AF37'

plt.rcParams.update({
    'figure.facecolor': NAVY,
    'axes.facecolor': NAVY,
    'axes.edgecolor': GOLD,
    'axes.labelcolor': 'white',
    'text.color': 'white',
    'xtick.color': 'white',
    'ytick.color': 'white',
    'font.size': 12,
})


def load_json(subdir, filename):
    path = os.path.join(DATA_DIR, subdir, filename)
    with open(path, "r") as f:
        return json.load(f)


# ── DSC-1 Spectral Unity figures (original 10) ─────────────────────

def fig1_riemann_zeros(data):
    zeros = data["riemann_zeros"]["zeros"]
    phi_values = data["riemann_zeros"]["phi_mapping"]
    monster_primes = data["moonshine"]["monster_primes"]

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    ax1 = axes[0, 0]
    ax1.scatter(range(1, len(zeros)+1), zeros, c=GOLD, s=30, alpha=0.7)
    ax1.plot(range(1, len(zeros)+1), zeros, color=GOLD, alpha=0.3)
    ax1.set_xlabel('Zero Index n')
    ax1.set_ylabel(r'$\gamma_n$')
    ax1.set_title('Riemann Zeta Zeros (First 50)', fontweight='bold')
    ax1.grid(True, alpha=0.2)

    ax2 = axes[0, 1]
    ax2.scatter(range(1, len(phi_values)+1), phi_values, c='#66B2FF', s=30, alpha=0.7)
    ax2.set_xlabel('Zero Index n')
    ax2.set_ylabel(r'$\Phi(n) = 2\pi\gamma_n / \ln|M|$')
    ax2.set_title('Monster-Zeta Mapping', fontweight='bold')
    ax2.grid(True, alpha=0.2)

    gaps = np.diff(zeros)
    ax3 = axes[1, 0]
    ax3.bar(range(1, len(gaps)+1), gaps, color=GOLD, alpha=0.7)
    ax3.axhline(y=np.mean(gaps), color='white', linestyle='--', label=f'Mean: {np.mean(gaps):.3f}')
    ax3.set_xlabel('Gap Index')
    ax3.set_ylabel('Gap Size')
    ax3.set_title('Riemann Zero Gaps', fontweight='bold')
    ax3.legend(facecolor=NAVY, edgecolor=GOLD)
    ax3.grid(True, alpha=0.2)

    r_values = np.linspace(0.01, 2, 200)
    R2_gue = [1 - (np.sin(np.pi * r) / (np.pi * r))**2 for r in r_values]
    ax4 = axes[1, 1]
    ax4.plot(r_values, R2_gue, color=GOLD, linewidth=2, label=r'GUE $R_2(r)$')
    ax4.axhline(y=1, color='gray', linestyle='--', alpha=0.5)
    for p in monster_primes[:7]:
        r_p = np.log(p) / (2 * np.pi)
        ax4.axvline(x=r_p, color='#FF6666', linestyle=':', alpha=0.5)
    ax4.set_xlabel('Separation r')
    ax4.set_ylabel(r'$R_2(r)$')
    ax4.set_title('GUE Pair Correlation with Monster Primes', fontweight='bold')
    ax4.set_xlim(0, 1)
    ax4.legend(facecolor=NAVY, edgecolor=GOLD)
    ax4.grid(True, alpha=0.2)

    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, 'riemann_zeros.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print("  riemann_zeros.png")


def fig2_moonshine(data):
    monster_primes = data["moonshine"]["monster_primes"]
    peak_locations = data["moonshine"]["peak_locations"]
    exponents = [46, 20, 9, 6, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    ax1 = axes[0]
    peaks = [peak_locations[str(p)] for p in monster_primes]
    ax1.bar(range(len(monster_primes)), peaks, color=GOLD, alpha=0.8, edgecolor='white', linewidth=0.5)
    ax1.set_xticks(range(len(monster_primes)))
    ax1.set_xticklabels([str(p) for p in monster_primes], fontsize=8)
    ax1.set_xlabel('Monster Prime p')
    ax1.set_ylabel(r'$r_p = \ln(p)/2\pi$')
    ax1.set_title('Moonshine Peak Locations', fontweight='bold')
    ax1.grid(True, alpha=0.2)

    ax2 = axes[1]
    ax2.bar(range(len(monster_primes)), exponents, color='#66B2FF', alpha=0.8, edgecolor='white', linewidth=0.5)
    ax2.set_xticks(range(len(monster_primes)))
    ax2.set_xticklabels([str(p) for p in monster_primes], fontsize=8)
    ax2.set_xlabel('Prime p')
    ax2.set_ylabel('Exponent in |M|')
    ax2.set_title('Monster Group Order Factorization', fontweight='bold')
    ax2.grid(True, alpha=0.2)

    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, 'moonshine.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print("  moonshine.png")


def fig3_gue(data):
    zeros = data["riemann_zeros"]["zeros"]

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    s = np.linspace(0, 4, 200)
    P_gue = (32 / np.pi**2) * s**2 * np.exp(-4 * s**2 / np.pi)
    P_poisson = np.exp(-s)

    ax1 = axes[0]
    ax1.plot(s, P_gue, color=GOLD, linewidth=2, label='GUE (beta=2)')
    ax1.plot(s, P_poisson, color='#FF6666', linewidth=2, linestyle='--', label='Poisson')
    ax1.fill_between(s, P_gue, alpha=0.2, color=GOLD)
    ax1.set_xlabel('Normalized Spacing s')
    ax1.set_ylabel('P(s)')
    ax1.set_title('Level Spacing Distribution', fontweight='bold')
    ax1.legend(facecolor=NAVY, edgecolor=GOLD)
    ax1.grid(True, alpha=0.2)

    ax2 = axes[1]
    normalized_gaps = np.diff(zeros) / np.mean(np.diff(zeros))
    ax2.hist(normalized_gaps, bins=15, density=True, alpha=0.7, color=GOLD, edgecolor='white')
    s_theory = np.linspace(0, 3, 100)
    wigner = (np.pi * s_theory / 2) * np.exp(-np.pi * s_theory**2 / 4)
    ax2.plot(s_theory, wigner, color='white', linewidth=2, label='Wigner Surmise')
    ax2.set_xlabel('Normalized Gap s')
    ax2.set_ylabel('Probability Density')
    ax2.set_title('Gap Distribution (Riemann vs GUE)', fontweight='bold')
    ax2.legend(facecolor=NAVY, edgecolor=GOLD)
    ax2.grid(True, alpha=0.2)

    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, 'gue_distribution.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print("  gue_distribution.png")


# ── New figures from Phase 2 data ──────────────────────────────────

def fig_eigenvalue_verification():
    ev = load_json("eigenvalue-verification", "eigenvalue_verification_200.json")
    table = ev["table"]

    s_zeta = [row["s_zeta"] for row in table]
    s_gue = [row["s_gue"] for row in table]
    within = [row["within_2sigma"] for row in table]

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    ax = axes[0]
    colors = [GOLD if w else '#FF4444' for w in within]
    ax.scatter(s_gue, s_zeta, c=colors, s=15, alpha=0.8, zorder=3)
    lims = [min(min(s_zeta), min(s_gue)) * 0.9, max(max(s_zeta), max(s_gue)) * 1.1]
    ax.plot(lims, lims, '--', color='white', alpha=0.5, lw=1)
    ax.set_xlabel('GUE predicted spacing')
    ax.set_ylabel('Riemann zero spacing')
    ax.set_title(f'200-Zero GUE Comparison ({ev["statistics"]["match_percent"]}% within 2$\\sigma$)')

    ax = axes[1]
    s_zeta_sorted = np.sort(s_zeta)
    s_gue_sorted = np.sort(s_gue)
    n = len(s_zeta_sorted)
    ax.step(s_zeta_sorted, np.arange(1, n+1)/n, color=GOLD, lw=2, label='Riemann zeros')
    ax.step(s_gue_sorted, np.arange(1, n+1)/n, color='#66B2FF', lw=2, label='GUE prediction', linestyle='--')
    ax.set_xlabel('Spacing')
    ax.set_ylabel('CDF')
    ks = ev["statistics"]["ks_statistic"]
    pv = ev["statistics"]["ks_p_value"]
    ax.set_title(f'KS Test: D = {ks:.4f}, p = {pv:.4f}')
    ax.legend(facecolor=NAVY, edgecolor=GOLD)

    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, 'eigenvalue_200_comparison.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print("  eigenvalue_200_comparison.png")


def fig_h2_topology():
    scaling = load_json("h2-topology", "h2_scaling_verification.json")
    extended = load_json("h2-topology", "h2_extended_results.json")

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Scaling H2=0
    results = scaling["results"]
    h2 = [r["h2"] for r in results]
    labels = [f"Scale {i+1}" for i in range(len(results))]

    ax = axes[0]
    ax.bar(range(len(results)), h2, color='#FF4444', width=0.5, alpha=0.8)
    ax.axhline(y=0, color=GOLD, linestyle='--', lw=2, alpha=0.8)
    ax.set_xticks(range(len(results)))
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylabel(r'$H_2$ (voids)')
    ax.set_title(r'$H_2 = 0$ Verified at 7 Scales ($10^3$ to $10^{22}$)', color=GOLD)
    ax.set_ylim(-0.5, 1)
    ax.text(3, 0.7, r'$H_2 \equiv 0$ $\checkmark$', fontsize=20, color=GOLD, ha='center', fontweight='bold')

    # VR lifetimes
    ext_results = extended["results"]
    n_zeros = [r.get("n_zeros", r.get("n")) for r in ext_results]
    h2_life = [r["h2_max_life"] for r in ext_results]

    ax = axes[1]
    ax.bar(range(len(n_zeros)), h2_life, color='#FF4444', alpha=0.8, width=0.5)
    ax.axhline(y=0.1, color=GOLD, linestyle='--', lw=1, alpha=0.6, label='noise threshold (0.1)')
    ax.set_xticks(range(len(n_zeros)))
    ax.set_xticklabels([str(n) for n in n_zeros], fontsize=8)
    ax.set_xlabel('Number of zeros')
    ax.set_ylabel(r'$H_2$ max lifetime')
    ax.set_title(r'$H_2$ Lifetimes: All Below Noise', fontweight='bold')
    ax.legend(facecolor=NAVY, edgecolor=GOLD)

    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, 'h2_topology.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print("  h2_topology.png")


def main():
    print("=" * 50)
    print("REGENERATING ALL FIGURES FROM DATA")
    print("=" * 50)

    os.makedirs(FIGURES_DIR, exist_ok=True)

    data = load_json("spectral-unity", "experiment_results.json")
    print(f"\nLoaded experiment_results.json")
    print(f"Generating figures in {FIGURES_DIR}/\n")

    fig1_riemann_zeros(data)
    fig2_moonshine(data)
    fig3_gue(data)
    fig_eigenvalue_verification()
    fig_h2_topology()

    print(f"\nAll figures regenerated successfully.")


if __name__ == "__main__":
    main()
