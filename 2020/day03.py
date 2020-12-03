from functools import partial, reduce
from operator import mul

with open("inputs/day03.input", "r") as f:
    grid = list(line.strip() for line in f.readlines())


def trees(grid, r, d):
    return sum(row[(i*r) % len(row)] == "#"
               for i, row in enumerate(grid[::d]))


part1 = partial(trees, r=3, d=1)


def part2(grid):
    skips = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return reduce(mul, (trees(grid, *skip) for skip in skips))


print(f"Part 1: {part1(grid)}")
print(f"Part 2: {part2(grid)}")
