"""Compute all seven exact flattening ranks and the four one-site marginals."""

from collections import Counter
from fractions import Fraction
from itertools import product


def amplitudes(q, pairings):
    terms = Counter()
    for (i, j), (k, l) in pairings:
        for a, b in product(range(q), repeat=2):
            indices = [0] * 4
            indices[i] = indices[j] = a
            indices[k] = indices[l] = b
            terms[tuple(indices)] += 1
    return terms


def flatten(q, terms, left):
    right = tuple(i for i in range(4) if i not in left)

    def index(t, sites):
        n = 0
        for i in sites:
            n = n * q + t[i]
        return n

    matrix = [[0] * q**len(right) for _ in range(q**len(left))]
    for t, weight in terms.items():
        matrix[index(t, left)][index(t, right)] = weight
    return matrix


def rank(matrix):
    pivots = {}
    for row in matrix:
        residual = {i: Fraction(v) for i, v in enumerate(row) if v}
        while residual:
            lead = min(residual)
            scale = residual[lead]
            if lead not in pivots:
                pivots[lead] = {i: v / scale for i, v in residual.items()}
                break
            for i, v in pivots[lead].items():
                value = residual.get(i, 0) - scale * v
                if value:
                    residual[i] = value
                else:
                    residual.pop(i, None)
    return len(pivots)


def check(q):
    u = amplitudes(q, [((0, 1), (2, 3)), ((0, 3), (1, 2))])
    d = amplitudes(q, [((0, 2), (1, 3))])
    for site in range(4):
        for terms in (u, d):
            rows = flatten(q, terms, (site,))
            assert rank(rows) == q
            norm = sum(v * v for v in terms.values())
            for i, a in enumerate(rows):
                for j, b in enumerate(rows):
                    entry = sum(x * y for x, y in zip(a, b))
                    assert q * entry == (norm if i == j else 0)
    for partner in range(1, 4):
        left = (0, partner)
        observed = (rank(flatten(q, u, left)), rank(flatten(q, d, left)))
        expected = (q * (q + 1) // 2, 1) if partner == 2 else (q*q, q*q)
        assert observed == expected, (q, left, observed)
    print(f"q={q}: all seven cut ranks and all singleton marginals verified")


if __name__ == "__main__":
    for dimension in (2, 3, 6, 8):
        check(dimension)
