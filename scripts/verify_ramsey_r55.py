#!/usr/bin/env python3
"""
Independent Verification: R(5,5) >= 43

Proves that the coloring below has ZERO monochromatic K5 subgraphs
in K42, by exhaustive brute-force over all C(42,5) = 850,668
five-cliques.

Zero dependencies. Python 3.8+. Runs in ~2 seconds.

Usage:
    python verify_ramsey_r55.py

Paper: "A Computational Lower Bound for R(5,5)"
       Daugherty, Ward, Ryan (March 2026)
       https://github.com/OriginNeuralAI/u24-spectral-operator
"""

# Certificate: 861 edge colors (+1/-1) for K42
# Source: isomorphic-engine, cpu-ils-gf43-b2-c11
# Seed: f(x) = x^2 + 2x + 11 over GF(43), basin 1
COLORING = [
    1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,1,-1,1,-1,1,1,1,1,-1,1,-1,1,-1,
    1,1,1,-1,1,-1,-1,1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,
    1,-1,1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1,-1,-1,
    -1,-1,1,-1,-1,1,-1,1,1,1,-1,1,-1,1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,1,-1,1,
    -1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,1,-1,1,-1,1,1,1,
    1,-1,1,-1,1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,
    1,1,1,-1,1,-1,1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,
    -1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,1,-1,1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,1,-1,
    1,-1,-1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,1,-1,1,-1,1,1,1,1,-1,
    1,-1,1,-1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,1,-1,
    1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,1,-1,1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,
    1,1,-1,1,-1,1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,1,-1,
    -1,1,-1,1,1,1,-1,1,-1,1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,1,-1,1,1,-1,-1,-1,
    -1,1,-1,-1,1,-1,1,1,1,-1,1,-1,1,-1,1,-1,1,1,-1,1,-1,1,-1,1,1,1,1,1,-1,
    -1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,1,-1,1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,1,1,
    -1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,1,-1,1,-1,1,1,1,1,-1,1,-1,1,-1,1,-1,
    1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,1,-1,1,-1,1,1,1,1,-1,1,-1,1,-1,-1,
    1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,1,-1,1,-1,1,1,1,1,-1,1,-1,1,-1,1,
    -1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,1,-1,1,-1,1,1,1,1,-1,1,-1,-1,1,-1,-1,
    -1,-1,1,-1,-1,1,-1,1,1,1,-1,1,-1,1,-1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,1,
    -1,-1,1,-1,1,1,1,-1,1,-1,1,-1,1,1,1,1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,
    1,1,1,-1,1,-1,1,-1,1,1,1,1,1,1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,1,-1,1,
    -1,1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,1,-1,1,-1,1,1,1,1,-1,-1,
    -1,-1,1,-1,-1,1,-1,1,1,1,-1,1,-1,1,-1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,
    1,1,-1,1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,1,-1,1,-1,1,-1,
    -1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,
    -1,1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,
    1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,
    -1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1,-1,-1,
    -1,1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,1,1,
    -1,-1,-1,1,1,-1,-1,1,1,-1,-1,1,-1,
]

def edge_index(u, v, n):
    """Index of edge (u,v) in lexicographic order, u < v."""
    return u * n - u * (u + 1) // 2 + v - u - 1

def main():
    n = 42
    k = 5
    ne = n * (n - 1) // 2  # 861
    edges_per_clique = k * (k - 1) // 2  # 10

    print("=" * 60)
    print("  R(5,5) >= 43  Independent Verification")
    print("=" * 60)
    print()

    assert len(COLORING) == ne, f"Expected {ne} edges, got {len(COLORING)}"
    assert all(s in (1, -1) for s in COLORING), "Invalid spin values"

    n_red = sum(1 for s in COLORING if s == 1)
    n_blue = ne - n_red
    print(f"  Graph:       K_{n} (complete graph on {n} vertices)")
    print(f"  Edges:       {ne}")
    print(f"  Color balance: {n_red} red / {n_blue} blue "
          f"({100*n_red/ne:.1f}% / {100*n_blue/ne:.1f}%)")
    print(f"  Five-cliques:  C({n},{k}) = ", end="")

    # Count C(42,5)
    from math import comb
    total_cliques = comb(n, k)
    print(f"{total_cliques:,}")
    print()
    print("  Checking all five-cliques...")

    mono_count = 0
    checked = 0

    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                for d in range(c + 1, n):
                    for e in range(d + 1, n):
                        checked += 1
                        s = (COLORING[edge_index(a, b, n)]
                           + COLORING[edge_index(a, c, n)]
                           + COLORING[edge_index(a, d, n)]
                           + COLORING[edge_index(a, e, n)]
                           + COLORING[edge_index(b, c, n)]
                           + COLORING[edge_index(b, d, n)]
                           + COLORING[edge_index(b, e, n)]
                           + COLORING[edge_index(c, d, n)]
                           + COLORING[edge_index(c, e, n)]
                           + COLORING[edge_index(d, e, n)])
                        if abs(s) == edges_per_clique:
                            mono_count += 1
                            print(f"  VIOLATION: ({a},{b},{c},{d},{e})"
                                  f" sum={s}")

    print()
    print(f"  Total five-cliques checked: {checked:,}")
    print(f"  Monochromatic K5 found:     {mono_count}")
    print()

    if mono_count == 0:
        print("  " + "=" * 46)
        print("  |  VERIFIED: R(5,5) >= 43 is PROVEN          |")
        print("  |  Zero monochromatic K5 in this coloring.   |")
        print("  " + "=" * 46)
    else:
        print(f"  FAILED: {mono_count} monochromatic K5 found.")

    print()
    print("  Certificate: GF(43), f(x) = x^2 + 2x + 11, basin 1")
    print("  Paper: Daugherty, Ward, Ryan (March 2026)")
    print("  Repo:  github.com/OriginNeuralAI/u24-spectral-operator")

if __name__ == "__main__":
    main()
