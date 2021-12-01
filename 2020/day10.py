from collections import defaultdict
from operator import mul

from more_itertools import windowed

with open("../inputs/2020/day10.input", "r") as f:
    adapters = [0]
    adapters.extend(sorted(map(int, f.readlines())))
    adapters.append(adapters[-1]+3)


def part1(adapters):
    acc = {1: (1, 0), 3: (0, 1)}
    return mul(*map(sum, zip(*(acc.get(b-a, (0, 0))
                               for a, b in windowed(adapters, 2)))))


def part2(adapters):
    table = defaultdict(int, [(adapters.pop(), 1)])
    # Work backwards from end, adding in all the paths we've already
    # seen.
    for rating in adapters[::-1]:
        table[rating] += sum(table[rating + i] for i in range(1, 4))
    return table[0]


print(f"Part 1: {part1(adapters)}")
print(f"Part 2: {part2(adapters)}")
