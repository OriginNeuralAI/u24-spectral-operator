#!/usr/bin/env python3
"""
Validate data integrity for U24 Spectral Operator repository.

Checks all data subdirectories:
  - spectral-unity/  (experiment_results.json, lehmer_predictions.csv, moonshine_peaks.csv)
  - riemann-zeros/   (riemann_zeros_50.json, .npy files, GPU results)
  - eigenvalue-verification/  (eigenvalue_verification_200.json)
  - rh-bridge/       (rh_verification_certificate.json)
  - h2-topology/     (h2_scaling_verification.json, h2_extended_results.json)
  - odlyzko/         (.npy files)

Usage:
    python scripts/validate_data.py
"""

import json
import csv
import os
import sys

import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(REPO_DIR, "data")

PASS = 0
FAIL = 0


def check(condition, message):
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"  [PASS] {message}")
    else:
        FAIL += 1
        print(f"  [FAIL] {message}")


# ── spectral-unity/ ─────────────────────────────────────────────────

def validate_experiment_results():
    print("\n=== spectral-unity/experiment_results.json ===")
    path = os.path.join(DATA_DIR, "spectral-unity", "experiment_results.json")
    check(os.path.exists(path), "File exists")

    with open(path, "r") as f:
        data = json.load(f)

    required_keys = [
        "riemann_zeros", "four_walls", "thirteen_walls", "moonshine",
        "lehmer_pairs", "gue", "horizon_entropy", "k3_zeta",
        "busy_beaver", "verification",
    ]
    for key in required_keys:
        check(key in data, f"Key '{key}' present")

    zeros = data["riemann_zeros"]["zeros"]
    check(len(zeros) == 50, f"50 Riemann zeros (got {len(zeros)})")
    check(abs(zeros[0] - 14.134725) < 0.001, f"First zero ~ 14.134725 (got {zeros[0]})")
    check(all(zeros[i] < zeros[i+1] for i in range(len(zeros)-1)), "Zeros in ascending order")

    check(len(data["moonshine"]["monster_primes"]) == 15, "15 Monster primes")
    check(data["moonshine"]["monster_primes"][0] == 2, "First Monster prime = 2")
    check(data["moonshine"]["monster_primes"][-1] == 71, "Last Monster prime = 71")

    check(len(data["lehmer_pairs"]) == 4, "4 Lehmer pairs")
    check(data["gue"]["level_repulsion_beta"] == 2, "GUE beta = 2")
    check(data["k3_zeta"]["euler_char"] == 24, "K3 Euler characteristic = 24")
    check(data["busy_beaver"]["5"] == 47176870, "BB(5) = 47,176,870")
    check(len(data["verification"]) == 7, "7 verification entries")


def validate_lehmer_csv():
    print("\n=== spectral-unity/lehmer_predictions.csv ===")
    path = os.path.join(DATA_DIR, "spectral-unity", "lehmer_predictions.csv")
    check(os.path.exists(path), "File exists")

    with open(path, "r") as f:
        rows = list(csv.DictReader(f))

    check(len(rows) > 25000, f"At least 25,000 predictions (got {len(rows)})")

    expected_cols = {"gamma_predicted", "k", "prime_i", "prime_j", "formula"}
    check(set(rows[0].keys()) == expected_cols, f"Correct columns")

    gammas = [float(r["gamma_predicted"]) for r in rows]
    check(all(g > 0 for g in gammas), "All gamma values positive")
    check(gammas == sorted(gammas), "Predictions sorted by gamma")

    monster_primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 47, 59, 71}
    primes_used = {int(r["prime_i"]) for r in rows} | {int(r["prime_j"]) for r in rows}
    check(primes_used.issubset(monster_primes), "All primes are Monster primes")


def validate_moonshine_csv():
    print("\n=== spectral-unity/moonshine_peaks.csv ===")
    path = os.path.join(DATA_DIR, "spectral-unity", "moonshine_peaks.csv")
    check(os.path.exists(path), "File exists")

    with open(path, "r") as f:
        rows = list(csv.DictReader(f))

    check(len(rows) == 15, f"15 peaks (got {len(rows)})")

    expected_cols = {"prime", "exponent_in_monster", "r_p", "weight", "status"}
    check(set(rows[0].keys()) == expected_cols, "Correct columns")

    primes = [int(r["prime"]) for r in rows]
    check(primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 47, 59, 71],
          "Primes in correct order")


# ── riemann-zeros/ ──────────────────────────────────────────────────

def validate_riemann_zeros():
    print("\n=== riemann-zeros/ ===")

    # JSON: 50 zeros
    path50 = os.path.join(DATA_DIR, "riemann-zeros", "riemann_zeros_50.json")
    check(os.path.exists(path50), "riemann_zeros_50.json exists")
    with open(path50) as f:
        z50 = json.load(f)
    n50 = len(z50) if isinstance(z50, list) else len(z50.get("zeros", z50.get("imaginary_parts", [])))
    check(n50 >= 50, f"At least 50 zeros (got {n50})")

    # NPY: 500 zeros
    path500 = os.path.join(DATA_DIR, "riemann-zeros", "riemann_zeros_500.npy")
    check(os.path.exists(path500), "riemann_zeros_500.npy exists")
    z500 = np.load(path500)
    check(z500.shape[0] >= 500, f"At least 500 zeros (got {z500.shape[0]})")
    check(abs(z500[0] - 14.134725) < 0.01, f"First zero ~ 14.1347 (got {z500[0]:.4f})")

    # NPY: 2000 zeros
    path2k = os.path.join(DATA_DIR, "riemann-zeros", "riemann_zeros_2000.npy")
    check(os.path.exists(path2k), "riemann_zeros_2000.npy exists")
    z2k = np.load(path2k)
    check(z2k.shape[0] >= 2000, f"At least 2000 zeros (got {z2k.shape[0]})")

    # GPU TF32: 1000 zeros
    path_gpu = os.path.join(DATA_DIR, "riemann-zeros", "riemann_gpu_tf32_1000.json")
    check(os.path.exists(path_gpu), "riemann_gpu_tf32_1000.json exists")
    with open(path_gpu) as f:
        gpu = json.load(f)
    check("computation" in gpu, "Has 'computation' key")
    check("zeros" in gpu, "Has 'zeros' key")
    check("spacings" in gpu, "Has 'spacings' key")
    check("pair_correlation" in gpu, "Has 'pair_correlation' key")
    check(gpu["computation"]["precision_digits"] >= 100, "100+ digit precision")


# ── eigenvalue-verification/ ────────────────────────────────────────

def validate_eigenvalue_verification():
    print("\n=== eigenvalue-verification/ ===")
    path = os.path.join(DATA_DIR, "eigenvalue-verification", "eigenvalue_verification_200.json")
    check(os.path.exists(path), "eigenvalue_verification_200.json exists")

    with open(path) as f:
        data = json.load(f)

    check(data["n_zeros"] == 200, f"n_zeros = 200 (got {data['n_zeros']})")
    check("statistics" in data, "Has 'statistics' key")
    check("table" in data, "Has 'table' key")

    stats = data["statistics"]
    check("ks_statistic" in stats, "KS statistic present")
    check("ks_p_value" in stats, "KS p-value present")
    check(stats["match_percent"] > 85, f"Match percent > 85% (got {stats['match_percent']})")
    check(len(data["table"]) > 0, f"Table has entries (got {len(data['table'])})")


# ── rh-bridge/ ──────────────────────────────────────────────────────

def validate_rh_bridge():
    print("\n=== rh-bridge/ ===")
    path = os.path.join(DATA_DIR, "rh-bridge", "rh_verification_certificate.json")
    check(os.path.exists(path), "rh_verification_certificate.json exists")

    with open(path) as f:
        cert = json.load(f)

    check(isinstance(cert, dict), "Certificate is a JSON object")
    check(os.path.getsize(path) > 1000, f"File size > 1KB ({os.path.getsize(path)} bytes)")


# ── h2-topology/ ────────────────────────────────────────────────────

def validate_h2_topology():
    print("\n=== h2-topology/ ===")

    # Scaling verification
    path_scale = os.path.join(DATA_DIR, "h2-topology", "h2_scaling_verification.json")
    check(os.path.exists(path_scale), "h2_scaling_verification.json exists")
    with open(path_scale) as f:
        scaling = json.load(f)

    check(scaling["verified"] is True, "H2=0 verified")
    check(scaling["scales_tested"] == 7, f"7 scales tested (got {scaling['scales_tested']})")
    check(all(r["h2"] == 0 for r in scaling["results"]), "H2=0 at all scales")

    # Extended results
    path_ext = os.path.join(DATA_DIR, "h2-topology", "h2_extended_results.json")
    check(os.path.exists(path_ext), "h2_extended_results.json exists")
    with open(path_ext) as f:
        extended = json.load(f)

    check(extended["method"] == "Vietoris-Rips persistent homology", "Correct method")
    check(len(extended["results"]) == 7, f"7 scales (got {len(extended['results'])})")
    check(all(r["h2"] == 0 for r in extended["results"]), "H2=0 at all VR scales")
    max_life = max(r["h2_max_life"] for r in extended["results"])
    check(max_life < 0.2, f"Max H2 lifetime < 0.2 (got {max_life})")


# ── odlyzko/ ────────────────────────────────────────────────────────

def validate_odlyzko():
    print("\n=== odlyzko/ ===")

    for name in ["odlyzko_1e21.npy", "odlyzko_1e22.npy"]:
        path = os.path.join(DATA_DIR, "odlyzko", name)
        check(os.path.exists(path), f"{name} exists")
        data = np.load(path)
        check(data.shape[0] >= 100, f"{name}: at least 100 entries (got {data.shape[0]})")
        check(os.path.getsize(path) > 10000, f"{name}: file size > 10KB ({os.path.getsize(path)} bytes)")


# ── Main ────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("U24 SPECTRAL OPERATOR — DATA VALIDATION")
    print("=" * 60)

    validate_experiment_results()
    validate_lehmer_csv()
    validate_moonshine_csv()
    validate_riemann_zeros()
    validate_eigenvalue_verification()
    validate_rh_bridge()
    validate_h2_topology()
    validate_odlyzko()

    print("\n" + "=" * 60)
    print(f"RESULTS: {PASS} passed, {FAIL} failed")
    print("=" * 60)

    if FAIL > 0:
        sys.exit(1)
    else:
        print("\nAll validations passed!")


if __name__ == "__main__":
    main()
