from functools import reduce
from operator import itemgetter


def traverse(string):
    x = 0
    directions = {"R": 1, "L": -1, "U": 1j, "D": -1j}
    for ins in string.strip().split(","):
        d = directions[ins[0]]
        n = int(ins[1:])
        yield from (x + i*d for i in range(n))
        x += n*d
    yield x


with open("inputs/day03.input", "r") as f:
    data = f.readlines()


def setup(data):
    distances = tuple(dict((x, i) for i, x in enumerate(traverse(line)))
                      for line in data)
    return distances, reduce(set.intersection, map(set, distances))


def part1():
    _, candidates = setup(data)

    def norm(x):
        return int(abs(x.real) + abs(x.imag))

    return min(map(norm, candidates - {0}))


def part2():
    distances, candidates = setup(data)

    def norm(x):
        return sum(map(itemgetter(x), distances))

    return min(map(norm, candidates - {0}))


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
