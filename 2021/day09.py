import time
from collections import defaultdict
from functools import reduce
from itertools import product
from operator import mul
from typing import Iterable, Mapping

T = tuple[int, int]
M = Mapping[T, int]

start = time.time()
with open("../inputs/2021/day09.input", "r") as f:
    data = f.read()
    data = data.strip().split("\n")
    shape = (len(data) + 2, len(data[0].strip()) + 2)
    inp: M = defaultdict(lambda: 9)
    for i, line in enumerate(data):
        for j, c in enumerate(map(int, line.strip())):
            inp[i, j] = c


def neighbours(i: int, j: int) -> Iterable[T]:
    yield from ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))


def minima(heights: M) -> Iterable[T]:
    n, m = map(max, zip(*heights))
    yield from (
        i
        for i in product(range(n + 1), range(m + 1))
        if all(heights[i] < heights[n] for n in neighbours(*i))
    )


def part1(heights: M) -> int:
    return sum(heights[m] + 1 for m in minima(heights))


def size(seed: T, heights: M) -> int:
    found: set[T] = set()
    queue = {seed}
    while queue:
        seed = queue.pop()
        if seed not in found:
            found.add(seed)
            # Restriction that each point is either 9 or belonging to
            # exactly one basin means the termination criterion is
            # heights[c] == 9, and we don't need the additional check
            # that seed < heights[c]
            queue |= set((c for c in neighbours(*seed) if heights[c] < 9))
    return len(found)


def part2(heights: M) -> int:
    return reduce(mul, sorted(size(s, heights) for s in minima(heights))[-3:])


print(
    f"Day 09     {part1(inp):<13} {part2(inp):<14} {(time.time() - start)*1e6:>13.0f}"
)
