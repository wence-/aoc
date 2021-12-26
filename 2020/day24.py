from collections import Counter
from operator import add

from more_itertools import iterate, nth

with open("../inputs/2020/day24.input", "r") as f:
    lines = [line.strip() for line in f.readlines()]


neighbours = {
    "e": (+1, 0),
    "w": (-1, 0),
    "nw": (0, 1),
    "ne": (1, 1),
    "sw": (-1, -1),
    "se": (0, -1),
}


def advance(line):
    ((m, v),) = ((m, v) for m, v in neighbours.items() if line.startswith(m))
    return v, line[len(m) :]


def load_grid(lines):
    grid = set()
    for line in lines:
        pos = (0, 0)
        while line:
            v, line = advance(line)
            pos = tuple(map(add, pos, v))
        if pos in grid:
            grid.remove(pos)
        else:
            grid.add(pos)
    return grid


def part1(lines):
    return len(load_grid(lines))


def step(grid):
    adj = Counter(
        (tuple(map(add, loc, n)) for n in neighbours.values() for loc in grid)
    )
    return {loc for loc, n in adj.items() if n == 2 or (n == 1 and loc in grid)}


def part2(lines):
    return len(nth(iterate(step, load_grid(lines)), 100))


print(f"Part 1: {part1(lines)}")
print(f"Part 2: {part2(lines)}")
