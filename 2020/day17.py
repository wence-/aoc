import numpy
import scipy.ndimage

with open("../inputs/2020/day17.input", "r") as f:
    data = f.readlines()
    zlice = numpy.asarray(
        [[0 if c == "." else 1 for c in line.strip()] for line in data]
    )


def step(grid, kernel):
    grid = numpy.pad(grid, 1, "constant", constant_values=0)
    neighbours = scipy.ndimage.convolve(grid, kernel, mode="constant", cval=0)
    born = numpy.logical_and(grid == 0, neighbours == 3)
    stay = numpy.logical_and(
        grid == 1, numpy.logical_or(neighbours == 3, neighbours == 2)
    )
    grid[:] = 0
    grid[born | stay] = 1
    return grid


def part1(zlice):
    grid = numpy.zeros(zlice.shape + (3,))
    grid[..., 1] = zlice
    kernel = numpy.full((3, 3, 3), 1)
    kernel[1, 1, 1] = 0
    for _ in range(6):
        grid = step(grid, kernel)
    return int(grid.sum())


def part2(zlice):
    grid = numpy.zeros(zlice.shape + (3, 3))
    grid[..., 1, 1] = zlice
    kernel = numpy.full((3, 3, 3, 3), 1)
    kernel[1, 1, 1, 1] = 0
    for _ in range(6):
        grid = step(grid, kernel)
    return int(grid.sum())


print(f"Part 1: {part1(zlice)}")
print(f"Part 2: {part2(zlice)}")
