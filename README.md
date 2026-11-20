# Every phase mixture recurs

**The planar Ising model with random boundary spins**

Seth Douglas and Nidhal Mghirbi. Preprint, version 2.0.0, November 2026. [Archive DOI](https://doi.org/10.5281/zenodo.24385704) (all versions); version 2.0.0: [10.5281/zenodo.24401253](https://doi.org/10.5281/zenodo.24401253); version 1.0.0: [10.5281/zenodo.24385705](https://doi.org/10.5281/zenodo.24385705)

For the two-dimensional nearest-neighbour Ising model on centred squares with independent fair exterior spins and boundary bonds of the bulk strength, every convex mixture of the plus and minus phases is almost surely a subsequential limit along the full sequence of sizes. The result holds at every fixed finite inverse temperature K > K_c = (1/2) log(1 + sqrt 2), that is, throughout the ordered phase.

## Results

- **Theorem A:** the almost-sure cluster set is the whole Gibbs mixture segment, at every K > K_c. This proves the two-dimensional conjecture of van Enter, Netocny and Schaap (2005, Remark 3.2), stated there for sufficiently low temperature; an earlier form of the conjecture, for weak boundary couplings, is in van Enter, Medved' and Netocny (2002).
- **Theorem B:** every fixed interior window of mixture weights has probability at least c/sqrt(n), with a positive constant depending on the temperature and the window.
- **Theorem C:** every fixed nonzero boundary bias selects the favoured pure phase along all sizes almost surely (strong biases, with plus-density below 3/8 or above 5/8, were already covered at low temperature by Higuchi 1978, Theorem 1). For fair spins the empirical metastate has equal masses at the pure endpoints and the ordinary mean of the origin plus-probability is 1/2.

The empirical metastate conclusion recovers van Enter, Netocny and Schaap's Theorem 3.4, proved there at sufficiently low temperature, throughout the ordered phase. Their Proposition 3.5 supplies a complementary upper bound in its own published temperature regime. The paper distinguishes those prior results from the full-sequence recurrence and local-window lower bound.

## Changes in 2.0.0

Version 2.0.0 proves Theorems A, B and C at every K > K_c = 0.44068679..., the whole ordered phase; version 1.0.0 proved them for K > K_P = 0.9791163662... . The Peierls-type contour comparisons, the threshold K_P and the appendix of numerical margins are replaced by a new argument. The random-line representation of the subcritical dual model gives long open arcs an exponentially small weight, typical boundaries make macroscopic arcs rare, and the sign of the spin sum in a central square, in place of a pinned line, labels the phase. The fair anti-concentration lemma now holds at every scale o(sqrt n). The paper adds the references used by the new argument, among them Pfister and Velenik (1997, 1999), Ioffe (1995), Schonmann (1987), the Griffiths inequalities and Yang (1952), credits the constructions of every mixture from tuned deterministic boundaries (Gallavotti; Messager and Miracle-Solé; Abraham and Reed), and cites Fröhlich and Pfister as the primary source for the wall input. The open questions are now the exact order n^(-1/2), the weak-coupling model of van Enter, Medved' and Netocny (2002), and three dimensions.

## Contents and build

`paper/` contains the PDF, LaTeX source, plain-text abstract and build instructions. From that directory run `python -I build.py`. The strict driver disables automatic package installation and shell escape and requires stable references and zero final warnings or box defects. It uses an existing MiKTeX pdfLaTeX installation; no package installation is performed by the driver.

The root contains citation metadata, licensing information and `SHA256SUMS`, the SHA-256 digest of every distributed file except the checksum list itself. Verify it from the archive root with `sha256sum -c SHA256SUMS`.

## How it was checked

The first page of the paper names the models that assisted with this work. The argument of version 2.0.0 was checked by three non-author audits during its development and then by two independent refutation-first checks, by models from more than one developer in all, with the imported statements compared against their sources. Enumerations on small boxes served as evidence; no proof depends on them. Not formalized in Lean.

## Citation and license

Douglas, Seth, and Nidhal Mghirbi (2026). *Every phase mixture recurs: The planar Ising model with random boundary spins*. Version 2.0.0. [Archive DOI](https://doi.org/10.5281/zenodo.24385704) · [Citation metadata](CITATION.cff)

Paper and documentation are licensed under CC BY 4.0; the build script under MIT or Apache 2.0, at your option. See `RIGHTS.md` and the license files.
