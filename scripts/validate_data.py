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
  - reeds/           (reeds_endomorphism_z23.json, coupling_matrix_J.json)
  - pair-correlation/ (r2_convergence_9scales.json, perturbation_sweep.json, ...)
  - quantum-graph/   (gamma0_23_graph.json)

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
    check(all(z500[i] < z500[i+1] for i in range(len(z500)-1)), "500 zeros in ascending order")

    # NPY: 2000 zeros
    path2k = os.path.join(DATA_DIR, "riemann-zeros", "riemann_zeros_2000.npy")
    check(os.path.exists(path2k), "riemann_zeros_2000.npy exists")
    z2k = np.load(path2k)
    check(z2k.shape[0] >= 2000, f"At least 2000 zeros (got {z2k.shape[0]})")
    check(all(z2k[i] < z2k[i+1] for i in range(len(z2k)-1)), "2000 zeros in ascending order")
    check(abs(z2k[0] - 14.134725) < 0.01, f"2000-set first zero ~ 14.1347 (got {z2k[0]:.4f})")

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

    check(len(data["table"]) == 35, f"Table has 35 representative rows (got {len(data['table'])})")
    check("ad_statistic" in stats, "Anderson-Darling statistic present")
    check(stats.get("matches_2sigma") == 31, f"31 matches within 2-sigma (got {stats.get('matches_2sigma')})")
    check(data["table"][0].get("k") == 1, "First table entry k = 1")


# ── rh-bridge/ ──────────────────────────────────────────────────────

def validate_rh_bridge():
    print("\n=== rh-bridge/ ===")
    path = os.path.join(DATA_DIR, "rh-bridge", "rh_verification_certificate.json")
    check(os.path.exists(path), "rh_verification_certificate.json exists")

    with open(path) as f:
        cert = json.load(f)

    check(isinstance(cert, dict), "Certificate is a JSON object")
    check(os.path.getsize(path) > 1000, f"File size > 1KB ({os.path.getsize(path)} bytes)")

    check(cert.get("bridge_established") is True, "Bridge established = true")
    check("engine_version" in cert.get("engine", "") or "engine_version" in cert,
          "Engine version present")
    check("convergence" in cert, "Has 'convergence' key")
    check(len(cert.get("convergence", {}).get("scales", [])) == 3,
          "Convergence fitted to 3 scales")
    check("scale_results" in cert, "Has 'scale_results' key")
    check(len(cert.get("scale_results", [])) == 3, "3 scale results")
    check(all(sr.get("u24_consistent") is True for sr in cert.get("scale_results", [])),
          "All scale results U24-consistent")
    check("perturbation" in cert, "Has 'perturbation' key")


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
    check(all(r.get("h0_final") == 1 for r in extended["results"]),
          "H0 converges to 1 (connected) at all VR scales")
    check(all(r["h1"] > 0 for r in extended["results"]), "H1 > 0 at all VR scales (nontrivial 1-cycles)")
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


# ── reeds/ ────────────────────────────────────────────────────────

def validate_reeds():
    print("\n=== reeds/ ===")

    # Endomorphism
    path = os.path.join(DATA_DIR, "reeds", "reeds_endomorphism_z23.json")
    check(os.path.exists(path), "reeds_endomorphism_z23.json exists")
    with open(path) as f:
        data = json.load(f)

    table = data["reeds_table"]["numeric_table"]
    check(len(table) == 23, f"Table has 23 entries (got {len(table)})")
    check(all(0 <= v < 23 for v in table), "All values in [0, 22]")
    check(data["properties"]["cycle_type"] == [3, 3, 2, 1], "Cycle type = [3,3,2,1]")
    check(data["properties"]["order_on_eventual_image"] == 6, "ord(f|_E) = 6")

    basins = data["basins"]
    check(len(basins) == 4, "4 basins")
    sizes = [b["basin_size"] for b in basins]
    check(sizes == [9, 7, 1, 6], f"Basin sizes = [9,7,1,6] (got {sizes})")
    check(sum(sizes) == 23, "Basin sizes sum to 23")

    check(data["constants"]["alpha_D"] == -0.008193, "alpha_D = -0.008193")
    check(data["constants"]["omega"] == 24, "Omega = 24")
    check(data["properties"]["image_size"] == 11, "|Im(f)| = 11")
    check(data["properties"]["is_surjective"] is False, "f is not surjective")

    # Verify f^6 = f^12 computationally
    table = data["reeds_table"]["numeric_table"]
    def apply_f(x): return table[x % 23]
    def iterate_f(x, n):
        for _ in range(n): x = apply_f(x)
        return x
    check(all(iterate_f(x, 6) == iterate_f(x, 12) for x in range(23)),
          "f^6 = f^12 for all x (ord(f|_E) = 6 verified computationally)")
    check(data["constants"]["omega"] // data["properties"]["order_on_eventual_image"] == 4,
          "Omega / ord(f|_E) = 24/6 = 4 = |V4|")

    # Coupling matrix
    path_J = os.path.join(DATA_DIR, "reeds", "coupling_matrix_J.json")
    check(os.path.exists(path_J), "coupling_matrix_J.json exists")
    with open(path_J) as f:
        J_data = json.load(f)

    J = J_data["coupling_matrix_J"]
    check(len(J) == 23, f"J has 23 rows (got {len(J)})")
    check(len(J[0]) == 23, f"J has 23 cols (got {len(J[0])})")
    check(J_data["properties"]["symmetric"], "J is symmetric")
    check(abs(J_data["properties"]["trace"]) < 1e-10, "Trace(J) = 0")
    check(len(J_data["eigenvalues_J"]) == 23, "23 eigenvalues")


# ── pair-correlation/ ────────────────────────────────────────────

def validate_pair_correlation():
    print("\n=== pair-correlation/ ===")

    # 9-scale convergence
    path = os.path.join(DATA_DIR, "pair-correlation", "r2_convergence_9scales.json")
    check(os.path.exists(path), "r2_convergence_9scales.json exists")
    with open(path) as f:
        data = json.load(f)

    scales = data["scales"]
    check(len(scales) == 9, f"9 scales (got {len(scales)})")
    check(scales[0]["n_zeros"] == 200, "First scale = 200")
    check(scales[-1]["n_zeros"] == 5000000, "Last scale = 5,000,000")

    r2_vals = [s["r2_l2"] for s in scales]
    check(all(r2_vals[i] >= r2_vals[i+1] for i in range(len(r2_vals)-1)),
          "R2 monotonically decreasing")
    check(abs(data["convergence_fit"]["alpha"] - 0.2833) < 0.001,
          f"alpha = 0.2833 (got {data['convergence_fit']['alpha']})")
    check(abs(r2_vals[0] - 0.465) < 0.01,
          f"R2 at N=200 ~ 0.465 (got {r2_vals[0]:.3f})")
    check(abs(r2_vals[-1] - 0.026) < 0.01,
          f"R2 at N=5M ~ 0.026 (got {r2_vals[-1]:.3f})")
    check(data["convergence_fit"].get("significant") is True, "Convergence fit significant")

    ks_vals = [s["ks_distance"] for s in scales]
    check(all(k > 0 for k in ks_vals), "All KS distances positive")

    # Perturbation sweep
    path_p = os.path.join(DATA_DIR, "pair-correlation", "perturbation_sweep.json")
    check(os.path.exists(path_p), "perturbation_sweep.json exists")
    with open(path_p) as f:
        pert = json.load(f)
    check(len(pert["sweeps"]) == 9, f"9 perturbation points (got {len(pert['sweeps'])})")
    check(pert["sweeps"][0]["epsilon"] == 0.0, "First perturbation epsilon = 0")

    # Higher correlations
    path_h = os.path.join(DATA_DIR, "pair-correlation", "higher_correlations.json")
    check(os.path.exists(path_h), "higher_correlations.json exists")
    with open(path_h) as f:
        hc = json.load(f)
    check(hc["r3"]["match"] == "GUE", "R3 matches GUE")
    check(hc["r4"]["match"] == "GUE", "R4 matches GUE")
    check(hc["cluster_t3"]["nonzero"] is True, "Cluster T3 nonzero (confirms GUE, not Poisson)")

    # Form factor
    path_f = os.path.join(DATA_DIR, "pair-correlation", "form_factor_k2.json")
    check(os.path.exists(path_f), "form_factor_k2.json exists")
    with open(path_f) as f:
        ff = json.load(f)
    check(ff["spectral_rigidity"]["best_match"] == "GUE", "Spectral rigidity matches GUE")
    check(ff["spectral_rigidity"]["l2_from_poisson"] > ff["spectral_rigidity"]["l2_from_gue"],
          "Spectral rigidity: Poisson L2 > GUE L2")
    check(len(ff["number_variance"]["data"]) == 20, "20 number variance entries")
    check(all(d["status"] == "GUE" for d in ff["number_variance"]["data"]),
          "All number variance entries classified as GUE")


# ── quantum-graph/ ───────────────────────────────────────────────

def validate_quantum_graph():
    print("\n=== quantum-graph/ ===")
    path = os.path.join(DATA_DIR, "quantum-graph", "gamma0_23_graph.json")
    check(os.path.exists(path), "gamma0_23_graph.json exists")
    with open(path) as f:
        data = json.load(f)

    check(data["graph"]["vertices"] == 2, "2 vertices (cusps)")
    check(data["graph"]["bonds"] == 15, "15 bonds")
    check(len(data["bonds"]) == 15, f"15 bond entries (got {len(data['bonds'])})")

    primes = [b["prime"] for b in data["bonds"]]
    check(primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],
          "Primes 2..47")

    # Bond lengths should be log(prime)
    import math
    bond_lengths_ok = all(
        abs(b["length"] - math.log(b["prime"])) < 0.001
        for b in data["bonds"]
    )
    check(bond_lengths_ok, "All bond lengths = log(prime)")

    check(data["zeta_zero_comparison"]["n_zeta_zeros_compared"] == 50, "50 zeta zeros compared")

    bw = data["berkolaiko_winn_conditions"]
    check(bw["score"] == "2/4", "BW score = 2/4")
    check(bw["conditions"][0]["status"] == "PASS", "BW unitarity condition PASS")
    check(data["secular_eigenvalues"]["n_found"] == 160, "160 secular eigenvalues")


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
    validate_reeds()
    validate_pair_correlation()
    validate_quantum_graph()

    print("\n" + "=" * 60)
    print(f"RESULTS: {PASS} passed, {FAIL} failed")
    print("=" * 60)

    if FAIL > 0:
        sys.exit(1)
    else:
        print("\nAll validations passed!")


if __name__ == "__main__":
    main()
