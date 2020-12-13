from itertools import chain

EMPTY = 0
OCC = 1
FLOOR = 2

gridmap = {"#": OCC,
           'L': EMPTY,
           '.': FLOOR}

invmap = dict((v, k) for k, v in gridmap.items())

with open("inputs/day11.input", "r") as f:
    data = f.readlines()
    grid = [list(map(gridmap.get, line.strip()))
            for line in data]


def print_grid(grid):
    for line in grid:
        print("".join(map(invmap.get, line)))
    print("\n")


def next_state_part1(grid, new_grid):
    a, b = len(grid), len(grid[0])
    for i in range(a):
        for j in range(b):
            if grid[i][j] == FLOOR:
                new_grid[i][j] = FLOOR
            else:
                nocc = -int(grid[i][j] == OCC)
                for k in range(max(0, i-1), min(a, i+2)):
                    for l in range(max(0, j-1), min(b, j+2)):
                        nocc += grid[k][l] == OCC
                if grid[i][j] == EMPTY and nocc == 0:
                    new_grid[i][j] = OCC
                elif nocc >= 4:
                    new_grid[i][j] = EMPTY
                else:
                    new_grid[i][j] = grid[i][j]
    return new_grid, grid


def part1(grid):
    grid = [list(g) for g in grid]
    next_grid = [[0 for _ in g] for g in grid]
    while next_grid != grid:
        grid, next_grid = next_state_part1(grid, next_grid)
    return sum(chain(*((g == OCC for g in gridline)
                       for gridline in grid)))


print(f"Part 1: {part1(grid)}")


def next_state_part2(grid, new_grid):
    a, b = len(grid), len(grid[0])
    for i in range(a):
        for j in range(b):
            if grid[i][j] == FLOOR:
                new_grid[i][j] = FLOOR
            else:
                nocc = 0
                for k in (-1, 0, 1):
                    for l in (-1, 0, 1):
                        if k == l == 0:
                            continue
                        m = 1
                        while 0 <= i + k*m < a and 0 <= j + l*m < b:
                            if grid[i + k*m][j+l*m] != FLOOR:
                                nocc += grid[i+k*m][j+l*m] == OCC
                                break
                            m += 1
                if grid[i][j] == EMPTY and nocc == 0:
                    new_grid[i][j] = OCC
                elif nocc >= 5:
                    new_grid[i][j] = EMPTY
                else:
                    new_grid[i][j] = grid[i][j]
    return new_grid, grid


def part2(grid):
    grid = [list(g) for g in grid]
    next_grid = [[0 for _ in g] for g in grid]
    while next_grid != grid:
        grid, next_grid = next_state_part2(grid, next_grid)
    return sum(chain(*((g == OCC for g in gridline)
                       for gridline in grid)))


print(f"Part 2: {part2(grid)}")
