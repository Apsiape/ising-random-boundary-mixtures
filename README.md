# Every phase mixture recurs

**The planar Ising model with random boundary spins**

Seth Douglas and Nidhal Mghirbi. Preprint, version 1.0.0, November 2026. [Archive DOI](https://doi.org/10.5281/zenodo.24385704) (all versions); version 1.0.0: [10.5281/zenodo.24385705](https://doi.org/10.5281/zenodo.24385705)

For the two-dimensional nearest-neighbour Ising model on centred squares with independent fair exterior spins and boundary bonds of the bulk strength, every convex mixture of the plus and minus phases is almost surely a subsequential limit along the full sequence of sizes. The result holds for every fixed finite inverse temperature K > K_P = 0.9791163662..., with K_P defined by an explicit Peierls sum in the paper.

## Results

- **Theorem A:** the almost-sure cluster set is the whole Gibbs mixture segment. This proves, in the stated range, the two-dimensional conjecture of van Enter, Netocny and Schaap (2005, Remark 3.2); an earlier form for weak boundary couplings is in van Enter, Medved' and Netocny (2002).
- **Theorem B:** every fixed interior window of mixture weights has probability at least c/sqrt(n), with a positive window-dependent constant.
- **Theorem C:** every fixed nonzero boundary bias selects the favoured pure phase along all sizes almost surely (strong biases, with plus-density below 3/8 or above 5/8, were already covered at low temperature by Higuchi 1978, Theorem 1). For fair spins the empirical metastate has equal masses at the pure endpoints and the ordinary mean of the origin plus-probability is 1/2.

The empirical metastate conclusion recovers van Enter, Netocny and Schaap's Theorem 3.4 in an explicit temperature range. Their Proposition 3.5 supplies a complementary upper bound in its own published temperature regime. The paper distinguishes those prior results from the full-sequence recurrence and local-window lower bound.

## Contents and build

`paper/` contains the PDF, LaTeX source, plain-text abstract and build instructions. From that directory run `python -I build.py`. The strict driver disables automatic package installation and shell escape and requires stable references and zero final warnings or box defects. It uses an existing MiKTeX pdfLaTeX installation; no package installation is performed by the driver.

The root contains citation metadata, licensing information and `SHA256SUMS`, the SHA-256 digest of every distributed file except the checksum list itself. Verify it from the archive root with `sha256sum -c SHA256SUMS`.

## How it was checked

The first page of the paper names the models that assisted with this work. The proofs were checked refutation-first by models from two developers, with every imported statement compared against its source. Not formalized in Lean.

## Citation and license

Douglas, Seth, and Nidhal Mghirbi (2026). *Every phase mixture recurs: The planar Ising model with random boundary spins*. Version 1.0.0. [Archive DOI](https://doi.org/10.5281/zenodo.24385704) · [Citation metadata](CITATION.cff)

Paper and documentation are licensed under CC BY 4.0; the build script under MIT or Apache 2.0, at your option. See `RIGHTS.md` and the license files.
