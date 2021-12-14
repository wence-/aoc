import time
from collections import Counter
from functools import partial
from itertools import chain, zip_longest

start = time.time()
with open("../inputs/2021/day05.input", "r") as f:
    inp = [
        list(chain(*(map(int, x.split(",")) for x in line.split(" -> "))))
        for line in f.readlines()
    ]


def solve(diagonal, wires):
    c = Counter()
    cmp = lambda x: (x > 0) - (x < 0)
    for x1, y1, x2, y2 in wires:
        dx = cmp(x2 - x1)
        dy = cmp(y2 - y1)
        if dx and dy and not diagonal:
            continue
        for x, y in zip_longest(
            range(x1, x2 + dx, dx or 1),
            range(y1, y2 + dy, dy or 1),
            fillvalue=y1 if dx else x1,
        ):
            c[x, y] += 1
    return sum(i > 1 for i in c.values())


part1 = partial(solve, False)
part2 = partial(solve, True)
print(
    f"Day 05     {part1(inp):<13} {part2(inp):<13} {(time.time() - start)*1e6:>13.0f}"
)
