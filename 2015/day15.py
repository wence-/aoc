from itertools import product, repeat

import numpy

with open("../inputs/2015/15.input", "r") as f:
    data = f.readlines()

mapping = {}
for line in data:
    name, *stuff = line.split()
    stuff[-1] += ","
    mapping[name[:-1]] = tuple(int(c[:-1]) for c in (stuff[1::2]))


a = numpy.asarray(list(mapping.values()))

A = a[:, :-1].T
C = a[:, -1]


def score(assignment):
    x = (A @ assignment)
    x[x < 0] = 0
    return x.prod()


def cals(assignment):
    return C @ assignment


print("Part 1:", max(score(a_) for a_ in product(*repeat(range(100), len(mapping)))
                     if sum(a_) == 100))

print("Part 2:", max(score(a_) for a_ in product(*repeat(range(100), len(mapping)))
                     if sum(a_) == 100 and cals(a_) == 500))
