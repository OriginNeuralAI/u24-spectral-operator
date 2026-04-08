# Changelog

All notable changes to the U₂₄ Spectral Operator papers and data.

## [v14.1 / v1.1] — 2026-04-08

### Spectral Operator Paper (v14.0 → v14.1)
- **Fixed:** All instances of K₂^off(τ) = 0 corrected to K₂^off(τ) = o(1) with explicit rate O(N⁻¹(log N)¹⁵)
- **Added:** Gap verification computational campaign (Isomorphic Engine v0.15.0, RTX 6000 Ada)

### Complete Proofs Paper (v1.0 → v1.1)
- **Fixed:** Proposition 9.4 (Off-Diagonal Vanishing → Off-Diagonal Suppression): statement corrected from exact 0 to o(1)
- **Added:** Remark (computational verification of off-diagonal suppression) after Proposition 9.4 proof
- **Resolved:** Issue B6 (Time-Reversal Symmetry) in Structural Notes appendix — bond transfer matrix ‖T−T⊤‖ = 4.006, rank(G) = 14 = n_transient, GUE confirmed over GOE
- **Added:** Version changelog at top of paper

### Repository
- **Added:** `data/gap-verification/` directory with 3 JSON result files (TRS, Weyl bound, cross-prime)
- **Added:** Gap Verification section in README with B1-B6 status table
- **Added:** Secular equation results: 169/169 zeta zeros matched at 0.23% mean error
- **Added:** `FAQ.md` addressing skeptic, researcher, and press questions
- **Added:** `CHANGELOG.md` (this file)
- **Updated:** On-Chain Anchoring section with v14.1/v1.1 BSV transaction IDs
- **Updated:** `.zenodo.json` metadata to version 1.1.0
- **Updated:** All version references from v14.0 → v14.1, v1.0 → v1.1
- **Updated:** `assets/proof-chain.svg` Step 4 label corrected

### Zenodo
- Paper 07 v14.1: [10.5281/zenodo.19469480](https://doi.org/10.5281/zenodo.19469480)
- Paper 08 v1.1: [10.5281/zenodo.19469502](https://doi.org/10.5281/zenodo.19469502)

### BSV Blockchain
- Paper 07 v14.1: [`aa4b5dd4...`](https://whatsonchain.com/tx/aa4b5dd4f67017fe6aace3ab4cac28b132e5d1ec7afe6f3b3522f51677855a70)
- Paper 08 v1.1: [`148b6c38...`](https://whatsonchain.com/tx/148b6c38410043afe3ec84fb64d63223c424ebb84db9f3da56a652808b872883)
- Campaign results: [`bb48ed5c...`](https://whatsonchain.com/tx/bb48ed5cf1ecb3ae366b7d67da027c5fd253846e1141bf8bb195644848231dfa)

## [v14.0 / v1.0] — 2026-03-27

### Initial Release
- Spectral Operator paper v14.0 (50 pages)
- Complete Proofs paper v1.0 (35 pages)
- Universality Constant paper v1.3
- Two Ramsey R(5,5) papers v1.0
- 140/140 automated verification checks
- 8 Jupyter notebooks
- 20 data files across 8 subdirectories
- BSV blockchain anchoring (4 transactions)
- Zenodo DOIs: 10.5281/zenodo.19414409 (Paper 07), 10.5281/zenodo.19414413 (Paper 08)
