import re

import numpy

with open("../inputs/2018/day10.input", "r") as f:
    input = f.readlines()

data = numpy.asarray([[int(i) for i in re.findall(r'-?\d+', l)] for l in input]).astype(int)

positions = data[:, :2].copy()
velocities = data[:, 2:]


def bbox(positions):
    return numpy.linalg.norm(numpy.max(positions, axis=0) - numpy.min(positions, axis=0))


minbox = numpy.finfo(float).max
found = 0

for i in range(20000):
    cur = bbox(positions)
    if cur < minbox:
        found = i
        minbox = cur
    positions += velocities

best = data[:, :2] + found*velocities

xextent = best[:, 0].max() - best[:, 0].min()
yextent = best[:, 1].max() - best[:, 1].min()

shape = (xextent + 1, yextent + 1)

vals = numpy.zeros(shape, dtype=int)

vals[best[:, 0] - best[:, 0].min(), best[:, 1] - best[:, 1].min()] = 1

for row in vals.T:
    print("".join("#" if x == 1 else " " for x in row))
