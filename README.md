# Crossing rates for coherent Bell pairings and packed loops

**Can four parties turn entanglement along the sides of a square into entanglement across both diagonals, at one output copy per input copy?** At local dimension eight, we prove that at least **5.7% of the rate is lost**, even when each party can process arbitrarily many copies together. All seven ways of cutting the square into two groups are consistent with a rate of one. A Euclidean tensor invariant detects the loss.

**zhangjinba** · Research manuscript, November 25, 2026 · [Read the paper](main.pdf) · [LaTeX source](main.tex)

## The four-party experiment

Place one party at each corner of a square. In one pairing, the top and bottom edges each carry a Bell pair. In the other, the left and right edges each carry one. The input is a coherent sum of these two pairings, with no label telling a party which pairing it holds. One copy of the target contains two independent Bell pairs, one on each diagonal.

We count exact target copies per input copy. Each party can apply a linear map jointly to its own copies, and the protocol may select a successful outcome. For local dimension $q=8$, an explicit protocol achieves rate $1/3$, while the upper bound is $4/(3\sqrt{2})\approx 0.9428$. Thus even 1,000 inputs cannot yield 943 exact target copies. The optimal rate within this interval remains open.

## What if one diagonal takes priority?

Let $r_1$ and $r_2$ be the numbers of independent Bell pairs delivered to the two diagonals per input copy. Changing the two diagonal lengths in the geometric proof gives the outer bound

$$
r_1^2+r_2^2 \le \left(1+\frac{1}{\log_2 q}\right)^2 .
$$

At $q=8$, if the first diagonal operates at rate one, the seven cut-rank tests permit the second to reach one as well. Averaging a protocol with its rotated copy and applying the equal-rate theorem lowers that ceiling to **0.88562** (rounded). The disk bound lowers it further to **0.88192**. The rate pair $(1,0.884)$ passes the first two tests and violates the third. Which points on the boundary are achievable remains open.

## How Euclidean geometry detects the loss

On a unit square a side has length 1 and a diagonal has length $\sqrt{2}$. The Euclidean prices theorem assigns a Bell pair of dimension $q$ the length of its segment times $\log_2 q$. Independent pairs add their prices. Crucially, the same theorem bounds the price of the **coherent sum** of the two side pairings by $2\log_2 q+2$. The diagonal target costs $2\sqrt{2}\log_2 q$. Local maps can only decrease price, so dividing the input bound by the target price gives a rate strictly below one for every integer $q\ge 6$.

The geometric theorem is the input from earlier work. This paper applies it to this fixed four-party state and shows explicitly that all bipartite flattening ranks and all quantum functionals based on single-party entropies permit unit rate. The comparison with more general quantum functionals remains open. [Euclidean prices theorem](https://github.com/openai/math/blob/main/preprints/Euclidean-geometry-in-the-asymptotic-spectrum-of-tensors-November-24-2026/paper.pdf)

## Why the same bound applies to a loop model

The two Bell pairings are also the two ways colored paths can turn at a vertex of a completely packed loop model. Glue these vertices into a square grid and sum over the interior colors. The boundary task is to transmit an independent color across every row and every column at the same time. The local price bounds add when the vertices are glued, so the loss persists in the boundary partition tensor.

With **eight colors**, reaching **99%** of full boundary transmission requires **at least about 82.5% of vertices** to allow an arbitrary local weight beyond the ordinary two-turn rule. This necessary condition holds for every square grid size. It measures information available at the boundary after summing the interior colors.

The lattice theorem also allows different horizontal and vertical rates. Stretching each cell horizontally and vertically assigns a separate weight to each output direction. For defect-free patches the two rates obey the same disk bound as the four-party state, independently of the side length.

## Reproduce the calculations

From the repository root, build the PDF with Tectonic and run the finite checks with Python 3.10 or later. The checks use the standard library.

```sh
tectonic main.tex
python3 checks/check_pairings.py
python3 checks/check_loop.py
```

The first check constructs the coefficient arrays at dimensions 2, 3, 6 and 8 and computes their flattening ranks and one-site marginals in exact arithmetic. The second compares every binary boundary assignment on a two-by-two patch against separate enumerations of internal colors and loop pairings. The general bounds are proved in the manuscript.
