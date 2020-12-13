import math
from functools import reduce
from operator import add, mul

with open("inputs/day13.input", "r") as f:
    target, busses = f.readlines()
    target = int(target)
    busses = [int(n) if n != "x" else None for n in busses.split(",")]


keep = lambda x: x is not None


def part1(target, busses):
    best = 10**10
    which = -1
    for bus in filter(keep, busses):
        n = int(math.ceil(target / bus))
        if bus * n - target < best:
            which = bus
            best = bus * n - target
    return best * which


def part2(busses):
    modulus = reduce(mul, filter(keep, busses))
    # Chinese remainder theorem
    ts = reduce(add, (-i * (modulus // bus) * pow(modulus // bus, -1, bus)
                      for i, bus in enumerate(busses)
                      if keep(bus)))
    return ts % modulus


print(f"Part 1: {part1(target, busses)}")
print(f"Part 2: {part2(busses)}")
