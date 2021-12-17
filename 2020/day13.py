import math
from functools import reduce
from operator import add, itemgetter, mul

with open("../inputs/2020/day13.input", "r") as f:
    target, buses = f.readlines()
    target = int(target)
    buses = [(i, int(n)) for i, n in enumerate(buses.split(","))
             if n != "x"]


def part1(target, buses):
    best = 10**10
    which = -1
    for _, bus in buses:
        if (n := bus - target % bus) < best:
            which = bus
            best = n
    return best * which


def part2(buses):
    # Chinese remainder theorem
    N = reduce(mul, map(itemgetter(1), buses))
    return reduce(add, ((bus - i) * (N // bus)
                        * pow(N // bus, -1, bus)
                        for i, bus in buses)) % N


def part2_alternate(buses):
    # LCM
    time = 0
    lcm = 1
    for i, bus in buses:
        while (time + i) % bus:
            time += lcm
        # Since all buses are prime, could just be lcm *= bus
        lcm = math.lcm(lcm, bus)
    return time


print(f"Part 1: {part1(target, buses)}")
print(f"Part 2: {part2(buses)}")
# print(f"Part 2 (LCM): {part2_alternate(buses)}")

