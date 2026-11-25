# Crossing rates for coherent Bell pairings and packed loops

**zhangjinba** · Research manuscript, November 25, 2026

[Read the paper (PDF)](main.pdf) · [LaTeX source](main.tex)

Four parties share the coherent sum of the two adjacent Bell pairings on a square. Each party may act jointly on its copies. How many independent pairs can they extract along both diagonals? At local dimension eight the paper bounds the exact asymptotic conversion rate between 1/3 and 4/(3√2). All bipartite flattening ranks and singleton quantum functionals permit unit rate. The upper bound uses the [Euclidean prices theorem](https://github.com/openai/math/blob/main/preprints/Euclidean-geometry-in-the-asymptotic-spectrum-of-tensors-November-24-2026/paper.pdf).

The second theorem applies the same price to the vertex weights of a completely packed loop model. It bounds boundary color transmission for whole patches as a function of the fraction of vertices with arbitrary weights.

## Reproduce the calculations

From the repository root, build the PDF with Tectonic and run the finite checks with Python 3.10 or later. The checks use the standard library.

```sh
tectonic main.tex
python3 checks/check_pairings.py
python3 checks/check_loop.py
```

The first check constructs the coefficient arrays at dimensions 2, 3, 6 and 8 and computes their flattening ranks and one-site marginals in exact arithmetic. The second compares every binary boundary assignment on a two-by-two patch against separate enumerations of internal colors and loop pairings. The general bounds are proved in the manuscript.
