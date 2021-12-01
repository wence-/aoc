import numpy
from scipy.signal import convolve

with open("../inputs/2019/day24.input", "r") as f:
    data = [line.strip() for line in f.readlines()]


def hash_state(grid):
    return sum(x*2**i for i, x in enumerate(numpy.nditer(grid)))


def part1(data):
    W, H = len(data[0]), len(data)
    grid = numpy.zeros((H, W), dtype=numpy.int8)
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[y, x] = 1 if c == "#" else 0

    seen = set()
    seen.add(hash_state(grid))

    while True:
        update = convolve(grid, [[0, 1, 0], [1, 0, 1], [0, 1, 0]], mode="same")
        grid[...] = (grid & (update == 1)) + (~grid & ((update == 1) | (update == 2)))
        state = hash_state(grid)
        if state in seen:
            break
        seen.add(state)
    return state


def part2(data, maxits=200):
    W, H = len(data[0]), len(data)
    grid = numpy.zeros((H, W), dtype=numpy.int8)
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[y, x] = 1 if c == "#" else 0

    levels = [numpy.zeros_like(grid) for _ in range(maxits*2 + 3)]
    levels[maxits+1] = grid
    new_levels = [g.copy() for g in levels]

    def neighbour_sum(x, y, level):
        if x == 2 and y == 2:
            return 0
        val = 0
        for (a, b) in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if a == 2 and b == 2:  # centre
                index = {(1, 2): (slice(None), 0),
                         (3, 2): (slice(None), 4),
                         (2, 1): (0, slice(None)),
                         (2, 3): (4, slice(None))}[(x, y)]
                val += levels[level+1][index].sum()
            if a == -1:
                val += levels[level-1][2, 1]
            elif b == -1:
                val += levels[level-1][1, 2]
            elif a == 5:
                val += levels[level-1][2, 3]
            elif b == 5:
                val += levels[level-1][3, 2]
            else:
                val += levels[level][b, a]
        return val

    for n in range(0, maxits):
        for i in range(-n-1, n+2):
            ngrid = new_levels[maxits+i+1]
            ogrid = levels[maxits+i + 1]
            for y, x in numpy.ndindex(ogrid.shape):
                n = neighbour_sum(x, y, maxits+i + 1)
                ngrid[y, x] = (ogrid[y, x] & (n == 1)) + (~ogrid[y, x] & (1 <= n <= 2))
        levels, new_levels = new_levels, levels

    return sum(x.sum() for x in levels)


print("Part 1:", part1(data))
print("Part 2:", part2(data, maxits=200))
