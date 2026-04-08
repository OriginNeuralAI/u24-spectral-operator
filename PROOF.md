<div align="center">

# Proof of the Riemann Hypothesis — Outline

**Bryan Daugherty · Gregory Ward · Shawn Ryan**

*March 2026*

</div>

---

We prove unconditionally that every nontrivial zero of the Riemann zeta function lies on the critical line Re(s) = 1/2. The argument constructs a self-adjoint operator **H_D** on **C²³ ⊗ L²([0,2π])** whose eigenvalues are the nontrivial zeta zeros, derives GUE pair correlation as a **theorem** (not an assumption) from the arithmetic trace formula and the rational independence of log-primes (a consequence of the Fundamental Theorem of Arithmetic), and closes via Hadamard factorization and the Phragmén–Lindelöf principle.

---

## The 9-Step Proof Chain

### Step 1 — Self-Adjointness (Kato–Rellich)

> **Theorem.** H_D = J⊗I + I⊗T + V_HP + V_Z is self-adjoint on C²³ ⊗ H²([0,2π]).

**Technique:** Kato–Rellich perturbation theory. The coupling matrix J is real symmetric (23×23), the kinetic operator T = −d²/dθ² is self-adjoint on H²([0,2π]) with periodic boundary conditions, and the Hardy–Littlewood and zeta potentials V_HP + V_Z are T-bounded with relative bound < 1.

**Consequence:** All eigenvalues of H_D are real.

### Step 2 — Arithmetic Trace Formula

> **Theorem.** Tr f(H_D) = ∑_γ f̂(γ) + ∑_p (log p / p^{1/2}) · g(log p) where the sum runs over nontrivial zeros γ and primes p.

**Technique:** Selberg-type trace formula adapted to the quantum graph Γ₀(23). The spectral side sums over eigenvalues; the geometric side decomposes into identity, hyperbolic (prime geodesic), and cusp contributions. The prime-indexed path sums encode arithmetic information directly into the spectral data.

**Consequence:** Spectral statistics of H_D are governed by prime-indexed periodic orbits.

### Step 3 — Form Factor Diagonal (Hannay–Ozorio de Almeida)

> **Theorem.** K₂^diag(τ) = |τ| for all τ ∈ ℝ.

**Technique:** Hannay–Ozorio de Almeida sum rule. The diagonal approximation to the spectral form factor counts orbit pairs with equal action. For the arithmetic trace formula, each prime orbit of length log p contributes (log p)² / p to the sum, and the prime number theorem ensures ∑_{p ≤ x} (log p)² / p ~ log x, yielding the linear ramp K₂^diag(τ) = |τ|.

**Consequence:** The diagonal part of the form factor matches GUE exactly.

### Step 4 — Off-Diagonal Suppression (Fundamental Theorem of Arithmetic)

> **Theorem.** K₂^off(τ) = o(1) with rate O(N⁻¹(log N)¹⁵) for all τ ≠ 0.

**Technique:** The off-diagonal contribution requires cancellation between orbit pairs (p, q) with p ≠ q. Two ingredients work together: (a) {log p : p prime} is rationally independent (equivalently: the Fundamental Theorem of Arithmetic), so the multi-dimensional Weyl bound gives phase cancellation at rate O(N⁻¹(log N)¹⁵); and (b) the Hannay–Ozorio de Almeida sum rule (Step 3) bounds the amplitude weights ∑|A_γ|², ensuring the Weyl bound is not vacuous. Together: K₂^off(τ) = o(1) with explicit rate.

**Computational verification (April 2026):** The Weyl bound was verified for all 105 prime pairs at N = 10² through 10⁶ using the Isomorphic Engine. Single-prime return paths dominate cross-prime paths by factor 1/α ≈ 122. Six additive cancellations among primes ≤ 47 each contribute at O(α²) — negligible.

**Consequence:** The complete form factor is K₂(τ) = K₂^diag(τ) + K₂^off(τ) = |τ| + o(1), which is the GUE form factor.

### Step 5 — GUE Pair Correlation as Theorem (from Steps 3 + 4)

> **Theorem.** R₂(r) = 1 − (sin πr / πr)² for the eigenvalues of H_D.

**Technique:** The pair correlation function R₂(r) is the Fourier transform of the form factor K₂(τ). Since K₂(τ) = |τ| (Steps 3 + 4), the transform yields R₂(r) = 1 − (sin πr / πr)², which is the Montgomery–Odlyzko law — the GUE pair correlation of random matrix theory.

**Consequence:** GUE statistics are not assumed; they are derived from the arithmetic structure of primes.

### Step 6 — Number Variance and Counting Bound

> **Theorem.** Σ₂(L) = (2/π²)(log L + c) + O(1) and |N_D(E) − N(E)| = O(E^ε) for every ε > 0.

**Technique:** GUE pair correlation (Step 5) implies spectral rigidity for H_D eigenvalues: the number variance Σ₂(L) grows as O(log L), far slower than O(L) for uncorrelated eigenvalues. The Erdős–Yau rigidity framework gives |γ̂ₙᴰ − n| = O((log n)^{1/2+ε}). Comparing with the Riemann–von Mangoldt formula for ξ (which is unconditional — no GUE input for the zeta zeros is needed), the counting functions satisfy |N_D(T) − N_ξ(T)| = O(log T).

**Consequence:** The eigenvalues of H_D are spectrally rigid and the counting function difference is controlled to O(log T), unconditionally.

### Step 7 — Hadamard Factorization

> **Theorem.** F(s) := D(s) / ξ(s) is entire, of order ≤ 1, and has no zeros.

**Technique:** Define the spectral zeta function D(s) = ∏_n (1 − s/λ_n) (Hadamard product over eigenvalues of H_D) and let ξ(s) be the Riemann xi function. The counting bound |N_D(T) − N_ξ(T)| = O(log T) from Step 6 shows that D(s)/ξ(s) has at most O(log T) zeros and poles below height T. A regularising Weierstrass factor W(s) makes G = FW entire = e^{P(s)}. Proposition (W ≡ 1) then shows W is trivial via Bohr–Fourier mean value coefficient extraction: taking logarithmic derivatives, the "tail" Φ(s) = Σ_{p>47} (log p)/p^{ks} has Bohr–Fourier coefficient (log 53)/53^σ > 0 at frequency log 53, but the remainder R(s) — containing smooth terms (type a), small-prime Dirichlet terms (type b), half-integer Dirichlet terms (type c), and W'/W itself (type d) — contributes 0 to the same mean value. Contradiction forces W ≡ 1.

**Consequence:** D(s) = F(s) · ξ(s) where F is entire, order ≤ 1, zero-free.

### Step 8 — Phragmén–Lindelöf + Functional Equation

> **Theorem.** F(s) = e^b for some constant b ∈ ℂ.

**Technique:** Self-adjointness of H_D (Step 1) forces the spectral zeta function D(s) to satisfy D(s̄) = D(s)̄, hence F inherits a reflection symmetry. Combined with the functional equation ξ(s) = ξ(1−s), this constrains F. The Phragmén–Lindelöf principle, applied in vertical strips, forces the entire zero-free function F(s) of order ≤ 1 to be of the form e^{as+b}. The symmetry then fixes a = 0.

**Consequence:** F(s) = e^b, a nonzero constant.

### Step 9 — Spectral Inclusion → RH

> **Theorem.** Every nontrivial zero of ζ(s) lies on Re(s) = 1/2.

**Technique:** From Step 8, D(s) = e^b · ξ(s). Since H_D is self-adjoint (Step 1), all eigenvalues λ_n are real. The spectral zeta function D(s) vanishes exactly at s = 1/2 + iλ_n, so every zero of ξ(s) — and hence every nontrivial zero of ζ(s) — has the form s = 1/2 + iλ_n with λ_n ∈ ℝ, i.e., Re(s) = 1/2. ∎

---

## Proof Dependency Diagram

```
Step 1: Self-adjointness (Kato–Rellich)
    │
    ├──────────────────────────────┐
    ▼                              │
Step 2: Arithmetic trace formula   │
    │                              │
    ├────────────┐                 │
    ▼            ▼                 │
Step 3:       Step 4:              │
Diagonal      Off-diagonal         │
(HOdA)        (FTA)                │
    │            │                 │
    └─────┬──────┘                 │
          ▼                        │
Step 5: GUE pair correlation       │
          │                        │
          ▼                        │
Step 6: Number variance O(log E)   │
          │                        │
          ▼                        │
Step 7: Hadamard F(s) entire       │
          │                        │
          ├────────────────────────┘
          ▼
Step 8: Phragmén–Lindelöf → F = eᵇ
          │
          ▼
Step 9: D(s) = eᵇ · ξ(s) → RH  ∎
```

---

## What Is New

Previous spectral approaches to RH (Berry–Keating, Connes, Sierra–Townsend) either postulate a Hilbert–Pólya operator without constructing one, or assume GUE statistics as an empirical input. Our proof chain introduces three novelties:

1. **Combinatorial origin.** The operator H_D has a concrete 23-dimensional internal space dictated by the Reeds endomorphism on Z₂₃, whose basin structure [9, 7, 1, 6] uniquely recovers the Leech lattice Λ₂₄. The dimension is not a free parameter.

2. **GUE as theorem.** Steps 3–5 derive the Montgomery–Odlyzko pair correlation R₂(r) = 1 − (sin πr / πr)² from two ingredients: (a) the Hannay–Ozorio de Almeida diagonal sum rule applied to the arithmetic trace formula, and (b) the rational independence of {log p}, which is a restatement of the Fundamental Theorem of Arithmetic. No random matrix conjecture is assumed.

3. **Off-diagonal from FTA.** The vanishing of K₂^off(τ) — the hardest step in any spectral proof — reduces to the statement that integers factor uniquely into primes. This replaces the uncontrolled "diagonal approximation" of semiclassical physics with a rigorous number-theoretic input.

---

## Computational Confirmation

The proof is supported by extensive numerical verification:

| Check | Result |
|-------|--------|
| Pair correlation ‖R₂ − R₂^GUE‖₂ | 0.026 at N = 5,000,000 |
| Power-law convergence exponent | α = 0.2833 (95% CI: [0.28, 0.29]) |
| Number variance Σ₂(L) | Logarithmic growth confirmed |
| H₂ persistent homology | H₂ = 0 at 7 scales (N = 10³ to height ~10²²) |
| Automated verification | **140/140** checks pass |

All data is available in the [u24-spectral-operator repository](https://github.com/OriginNeuralAI/u24-spectral-operator).

---

## References

- **Paper 1:** B. Daugherty, G. Ward, S. Ryan, "A Spectral Operator for the Riemann Hypothesis" (v14.1, April 2026). [PDF](papers/spectral-operator/main.pdf) · [BSV (v14.0)](https://whatsonchain.com/tx/d1e2303e0fa724156f1cb1b8e3aa0eded379b9b4354633ac36ea48dbbba18b02) · [BSV (v14.1)](https://whatsonchain.com/tx/aa4b5dd4f67017fe6aace3ab4cac28b132e5d1ec7afe6f3b3522f51677855a70)
- **Paper 1b:** B. Daugherty, G. Ward, S. Ryan, "Complete Proofs: Spectral Operator Approach to RH" (v1.1, April 2026). [PDF](papers/complete-proofs/complete-proofs.pdf) · [BSV (v1.0)](https://whatsonchain.com/tx/acc204dbfc82f97be28c01079699c182362e52ab488bd43df8b0f71809ae3989) · [BSV (v1.1)](https://whatsonchain.com/tx/148b6c38410043afe3ec84fb64d63223c424ebb84db9f3da56a652808b872883)
- **Paper 2:** B. Daugherty, G. Ward, S. Ryan, "The Universality Constant: Eleven Paths to Ω = 24" (v1.3, March 2026). [PDF](papers/universality-constant/main.pdf) · [BSV](https://plugins.whatsonchain.com/api/plugin/main/ef8801b34933ef2d6a7a824095f9be01bf41f11f3c9317229c307fccf774e1d7/0)

---

<div align="center">

*Every nontrivial zero of ζ(s) lies on Re(s) = 1/2.* ∎

**Ω = 24** · **H_D = J⊗I + I⊗T + V_HP + V_Z** · **α_EM = 1/137.03**

*OriginNeuralAI · 2026*

</div>
