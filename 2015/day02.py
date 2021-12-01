from functools import partial, reduce
from itertools import combinations
from operator import add, mul

with open("../inputs/2015/02.input", "r") as f:
    lines = f.read().strip().splitlines()


data = [list(map(int, line.split("x"))) for line in lines]


def area(line):
    l, w, h = line
    areas = list(map(partial(reduce, mul), combinations(line, 2)))
    return 2*reduce(add, areas) + min(areas)


def part1(data):
    return sum(map(area, data))


def ribbon(line):
    l, w, h = line
    return reduce(mul, line) + 2*min(map(partial(reduce, add), combinations(line, 2)))


def part2(data):
    return sum(map(ribbon, data))


print("Part 1:", part1(data))
print("Part 2:", part2(data))
