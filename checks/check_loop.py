"""Enumerate inner colors and loop pairings independently on a two-by-two patch."""

import itertools
import json
from collections import Counter

# Each tuple lists N,E,S,W edge indices; 0..7 are external, 8..11 internal.
CELLS = ((0, 8, 9, 7), (1, 2, 10, 8), (9, 11, 5, 6), (10, 3, 4, 11))


def loops_and_endpoint_pairs(turns):
    neighbors = [[] for _ in range(12)]
    for cell, turn in zip(CELLS, turns, strict=True):
        n, e, s, w = cell
        for a, b in (((n, e), (s, w)) if turn == 0 else ((n, w), (s, e))):
            neighbors[a].append(b)
            neighbors[b].append(a)
    seen = set()
    pairs = []
    loops = 0
    for start in range(12):
        if start in seen:
            continue
        stack = [start]
        ends = []
        while stack:
            v = stack.pop()
            if v in seen:
                continue
            seen.add(v)
            if v < 8:
                ends.append(v)
            stack.extend(neighbors[v])
        if ends:
            a, b = ends
            pairs.append((a, b))
        else:
            loops += 1
    return loops, pairs


def check(q):
    configurations = [loops_and_endpoint_pairs(t) for t in itertools.product(range(2), repeat=4)]
    counts = Counter(loops for loops, _ in configurations)
    assert counts[1] > 0
    for boundary in itertools.product(range(q), repeat=8):
        weight = 0
        for internal in itertools.product(range(q), repeat=4):
            colors = boundary + internal
            local_product = 1
            for cell in CELLS:
                n, e, s, w = (colors[i] for i in cell)
                local_product *= int(n == e and s == w) + int(n == w and s == e)
            weight += local_product
        assert weight == sum(q**loops for loops, pairs in configurations
                             if all(boundary[a] == boundary[b] for a, b in pairs))
    return {"q": q, "boundary_assignments": q**8, "internal_assignments_each": q**4,
            "loop_count_histogram": dict(counts), "all_entries_match": True}


if __name__ == "__main__":
    print(json.dumps(check(2), indent=2))
