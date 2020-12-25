from functools import partial, reduce
from operator import mul

with open("inputs/day16.input", "r") as f:
    constraints, me, nearby = f.read().strip().split("\n\n")


def check(n, alo, ahi, blo, bhi):
    return alo <= n <= ahi or blo <= n <= bhi


checkers = {}
for constraint in constraints.strip().split("\n"):
    loc, ranges = constraint.split(": ")
    a, b = ranges.split(" or ")
    a1, a2 = map(int, a.split("-"))
    b1, b2 = map(int, b.split("-"))
    checkers[loc] = partial(check, alo=a1, ahi=a2, blo=b1, bhi=b2)


me = list(map(int, me.split("\n")[1].split(",")))
nearby = list(list(map(int, line.split(",")))
              for line in nearby.split("\n")[1:])


def part1(checkers, nearby):
    return sum(sum(filter(lambda x: not any(v(x) for v in checkers.values()),
                          ticket))
               for ticket in nearby)


def part2(checkers, nearby, me):
    possible = [set(checkers.keys()) for _ in range(len(nearby[0]))]
    for line in filter(lambda ticket: all(any(v(x) for v in checkers.values())
                                          for x in ticket), nearby):
        for i, n in enumerate(line):
            possible[i] &= set(k for k, v in checkers.items()
                               if v(n))

    toremove = list(filter(lambda p: len(p) == 1, possible))
    while toremove:
        found = toremove.pop()
        for p in possible:
            if len(p) == 1 or p == found:
                continue
            p -= found
            if len(p) == 1:
                toremove.append(p)
    return reduce(mul, (me[i] for i, p in enumerate(possible)
                        if p.pop().startswith("departure")))


print(f"Part 1: {part1(checkers, nearby)}")
print(f"Part 2: {part2(checkers, nearby, me)}")
