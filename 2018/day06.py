import itertools

import numpy


class Patch(object):
    c = itertools.count()

    def __init__(self, string):
        coords = string.split(",")
        self.coords = numpy.asarray(tuple(map(lambda x: int(x.strip()), coords)))
        self.id_ = next(Patch.c)


with open("inputs/day06.input", "r") as f:
    patches = list(map(Patch, f.readlines()))

X = max(patch.coords[0] for patch in patches) + 1
Y = max(patch.coords[1] for patch in patches) + 1
shape = (X*Y, 2)
nearest = numpy.full(shape, 100000, dtype=int)
coords = numpy.asarray(list(numpy.ndindex(X, Y)))
for patch in patches:
    dist = numpy.linalg.norm(patch.coords - coords, 1, axis=1)
    equal = numpy.where(dist == nearest[..., 0])
    better = numpy.where(dist < nearest[..., 0])
    nearest[equal, 1] = -1
    nearest[better, 0] = dist[better]
    nearest[better, 1] = patch.id_

inf = set()

nearest = nearest.reshape(X, Y, 2)
candidates = set(numpy.unique(nearest[..., 1]))
inf.update(numpy.unique(nearest[[0, -1], :, 1]))
inf.update(numpy.unique(nearest[:, [0, -1], 1]))
candidates = candidates - (inf | {-1})

print(f"Part 1: {max(numpy.sum(nearest[..., 1] == c) for c in candidates)}")

total = numpy.zeros(X*Y, dtype=int)
for patch in patches:
    dist = numpy.linalg.norm(patch.coords - coords, 1, axis=1).astype(int)
    total += dist

print(f"Part 2: {numpy.sum(total < 10000)}")
