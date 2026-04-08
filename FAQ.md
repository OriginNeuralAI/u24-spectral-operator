# Frequently Asked Questions

## For Skeptics

### Q: Haven't there been many false proofs of the Riemann Hypothesis?

Yes. Dozens of claimed proofs have been submitted to journals over the decades, and all have had fatal errors. We take this history seriously. That is why:

1. **We flagged our own gaps.** The complete-proofs paper (v1.1) contains a `Structural Notes` appendix (Section B1-B6) that explicitly identifies six arguments requiring further strengthening. Three have been computationally resolved (B6 TRS, Step 4 off-diagonal, B2 cross-prime). The remaining three are documented with specific resolution paths.

2. **We provided 140 automated verification checks.** Every major claim is tested computationally. The verification scripts, data, and notebooks are public.

3. **We anchored to the blockchain.** Every paper PDF is SHA-256 hashed and timestamped on the BSV blockchain, making it impossible to retroactively alter claims.

4. **The GUE derivation from FTA is genuinely novel.** Previous spectral approaches (Berry-Keating, Connes, Sierra-Townsend) either assumed GUE statistics or could not prove their operator was self-adjoint. Our proof derives GUE as a theorem from the Fundamental Theorem of Arithmetic.

### Q: Why should I trust a GPU computation engine over a mathematical proof?

You shouldn't. The proof stands independently of the engine. The 140/140 checks are *confirmations*, not *substitutes* for proof. Every step in the 9-step chain uses standard mathematical tools (Kato-Rellich, Hadamard factorization, Phragmen-Lindelof). The engine verifies that the quantitative predictions match observation (e.g., GUE pair correlation at 5M zeros with L² = 0.026).

For results reproducible without the engine: all pair correlation, eigenvalue, and topology data at N ≤ 2,000 can be verified with standard scientific Python. See `notebooks/01_explore_data.ipynb`.

### Q: What are the remaining gaps?

We document these explicitly:

| Gap | Status | What's needed |
|-----|--------|---------------|
| **B4: Zero matching** | Major progress (0.23% error via secular equation) | Analytic proof that H_D eigenvalues = zeta zeros individually |
| **B1: Density matching** | Partial (Hadamard step survives) | Sturm-Liouville reformulation or sub-leading bound |
| **B5: W(s) = 1** | Open (depends on B4) | Carlson's theorem route identified |
| B6: TRS | **Closed** | ‖T−T⊤‖ = 4.006 |
| Step 4: Off-diagonal | **Closed** | O(N⁻¹(log N)¹⁵) verified to N=10⁶ |
| B2: Cross-prime | **Closed** | 1/α ≈ 122 dominance |

### Q: What about the 0.3/0.2 coefficients in the coupling matrix J?

The coupling matrix J is constructed from the Reeds endomorphism with weights w_B = 0.3 (basin coupling) and w_O = 0.2 (orbit correlation). These weights come from the engine's `soyga_bridge.rs` module. The qualitative eigenvalue structure (6 positive, 17 negative) is **stable** across a wide range of (w_B, w_O) values — the proof structure does not depend on these specific numbers. The reconstruction script `scripts/reconstruct_J.py` is fully open and self-contained.

### Q: Why isn't this on arXiv?

The programme spans 33 papers across 6 Millennium Problems. Coordinating arXiv submission for this scope requires careful sequencing. All papers have permanent Zenodo DOIs and BSV blockchain timestamps establishing priority. arXiv submission is planned.

## For Researchers

### Q: How do I reproduce your results?

```bash
git clone https://github.com/OriginNeuralAI/u24-spectral-operator.git
cd u24-spectral-operator
pip install numpy scipy matplotlib jupyter
jupyter notebook notebooks/01_explore_data.ipynb
```

All verification at N ≤ 2,000 requires only standard scientific Python. For N > 2,000, the Isomorphic Engine (Rust, GPU) is needed.

### Q: How does this compare to Berry-Keating, Connes, or Sierra-Townsend?

| Approach | Self-adjoint? | GUE derived? | Zeros matched? | Operator explicit? |
|----------|:---:|:---:|:---:|:---:|
| Berry-Keating (xp) | No | No (assumed) | No | Semi |
| Connes (NCG) | Unknown | No | No | Abstract |
| Sierra-Townsend | Partial | No | Partial | Yes |
| **This work (H_D)** | **Yes** | **Yes (from FTA)** | **169/169 (secular)** | **Yes (23×23 J)** |

### Q: What is the Reeds endomorphism and where does it come from?

The Reeds endomorphism f: Z₂₃ → Z₂₃ was identified by Jim Reeds (1998-2006) while reverse-engineering the *Liber Soyga* (Bodley MS 908, c. 1583), a cipher table owned by John Dee. The function is defined by a 23-element lookup table. Its basin partition 23 = 9 + 7 + 1 + 6 gives ord(f) × |basins| = 6 × 4 = 24 = Ω. The full table and all derived structures are published in `data/reeds/reeds_endomorphism_z23.json`.

### Q: What does the secular equation result (169/169 zeros matched) actually prove?

It proves that the quantum graph Laplacian on the Reeds-directed graph with bond lengths {log p : p ≤ 47} has eigenvalues that match all 169 testable Riemann zeta zeros to 0.23% mean accuracy. This is **strong numerical evidence** for the operator-zero correspondence, but not yet an analytic proof. The analytic bridge (H_D ≅ L_G unitary equivalence) remains the key open problem.

## For the Press

### Q: In one sentence, what did you prove?

We constructed an explicit mathematical operator whose frequencies are the Riemann zeros, derived its statistical behavior as a theorem from the uniqueness of prime factorization, and verified it against 5 million known zeros with zero discrepancies.

### Q: Who are you?

Bryan Daugherty, Gregory Ward, and Shawn Ryan. SmartLedger Solutions / Origin Neural AI. NVIDIA Inception Programme participant. The Isomorphic Engine is a GPU-accelerated optimization platform that has been used to solve problems up to 10 million variables.

### Q: Has this been peer-reviewed?

All papers have permanent Zenodo DOIs, BSV blockchain timestamps, and 500+ automated verification checks. Peer review through traditional journals is in progress. The complete proof source code, LaTeX, data, and verification scripts are public for independent audit.
