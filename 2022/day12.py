import time
from collections import defaultdict, deque
from functools import partial
from operator import eq

start = time.time()
with open("../inputs/2022/day12.input") as f:
    inp = defaultdict(lambda: -1)
    source = None
    target = None
    for i, line in enumerate(f.read().split("\n")):
        for j, c in enumerate(line):
            if c == "S":
                source = (i, j)
                c = "a"
            elif c == "E":
                target = (i, j)
                c = "z"
            inp[i, j] = ord(c) - ord("a")
    inp = inp, (source, target)


def keep(grid, node, neighbour):
    return grid[node] - 1 <= grid[neighbour]


def solve(grid, source, done):
    q: deque[tuple[tuple, int]] = deque([(source, 0)])
    seen = {source}
    while q:
        node, distance = q.popleft()
        if done(node):
            return distance
        for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbour = (node[0] + dx, node[1] + dy)
            if neighbour not in seen and keep(grid, node, neighbour):
                seen.add(neighbour)
                q.append((neighbour, distance + 1))
    raise ValueError


def part1(inp: tuple[dict, tuple]) -> int:
    grid, (source, target) = inp
    return solve(grid, target, partial(eq, source))


def part2(inp: tuple[dict, tuple]) -> int:
    grid, (_, target) = inp
    return solve(grid, target, lambda node: grid[node] == 0)


print(
    f"Day 12     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
