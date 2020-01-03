import numpy
from scipy.signal import convolve

with open("inputs/18.input", "r") as f:
    data = f.readlines()


grid = numpy.asarray([[1 if c == "#" else 0 for c in line.strip()]
                      for line in data], dtype=int)

ic = grid.copy()
stencil = numpy.asarray([[1, 1, 1],
                         [1, 0, 1],
                         [1, 1, 1]], dtype=int)


for _ in range(100):
    up = convolve(grid, stencil, mode="same")
    grid = (grid & ((up == 2) | (up == 3))) + (~grid & (up == 3))

print("Part 1:", grid.sum())

ix = numpy.ix_([0, -1], [0, -1])
grid = ic.copy()
grid[ix] = 1
for _ in range(100):
    up = convolve(grid, stencil, mode="same")
    grid = (grid & ((up == 2) | (up == 3))) + (~grid & (up == 3))
    grid[ix] = 1

print("Part 2:", grid.sum())
