import time
from collections import defaultdict

start = time.time()
with open("../inputs/2021/day12.input", "r") as f:
    inp = defaultdict(list)
    data = f.read()
    lines = data.strip().split("\n")
    for line in lines:
        a, b = line.split("-")
        if b != "start":
            inp[a].append(b)
        if a != "start":
            inp[b].append(a)


def recurse(head, seen, twice, nodes, cache):
    # Original implementation
    if head == "end":
        return 1
    try:
        return cache[(head, seen, twice)]
    except KeyError:
        pass

    s = sum(
        recurse(
            c,
            seen if c.isupper() else frozenset(seen | {c}),
            twice or c in seen,
            nodes,
            cache,
        )
        for c in nodes[head]
        if not (twice and c in seen)
    )
    return cache.setdefault((head, seen, twice), s)


def part1(nodes):
    return recurse("start", frozenset(), True, nodes, {})


def part2(nodes):
    return recurse("start", frozenset(), False, nodes, {})


print(
    f"Day 12     {part1(inp):<13} {part2(inp):<14} {(time.time() - start)*1e6:>13.0f}"
)
