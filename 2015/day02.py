import time
from functools import partial, reduce
from itertools import combinations
from operator import add, mul

start = time.time()
with open("../inputs/2015/02.input", "r") as f:
    lines = f.read().strip().splitlines()


inp = [list(map(int, line.split("x"))) for line in lines]


def area(line):
    l, w, h = line
    areas = list(map(partial(reduce, mul), combinations(line, 2)))
    return 2 * reduce(add, areas) + min(areas)


def part1(data):
    return sum(map(area, data))


def ribbon(line):
    l, w, h = line
    return reduce(mul, line) + 2 * min(map(partial(reduce, add), combinations(line, 2)))


def part2(data):
    return sum(map(ribbon, data))


print(
    f"Day 02     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
