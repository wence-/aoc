import time
from functools import reduce
from itertools import chain
from operator import mul

import numpy

start = time.time()

with open("../inputs/2021/day22.input", "r") as f:
    data = f.read()
    #     data = """on x=-20..26,y=-36..17,z=-47..7
    # on x=-20..33,y=-21..23,z=-26..28
    # on x=-22..28,y=-29..23,z=-38..16
    # on x=-46..7,y=-6..46,z=-50..-1
    # on x=-49..1,y=-3..46,z=-24..28
    # on x=2..47,y=-22..22,z=-23..27
    # on x=-27..23,y=-28..26,z=-21..29
    # on x=-39..5,y=-6..47,z=-3..44
    # on x=-30..21,y=-8..43,z=-13..34
    # on x=-22..26,y=-27..20,z=-29..19
    # off x=-48..-32,y=26..41,z=-47..-37
    # on x=-12..35,y=6..50,z=-50..-2
    # off x=-48..-32,y=-32..-16,z=-15..-5
    # on x=-18..26,y=-33..15,z=-7..46
    # off x=-40..-22,y=-38..-28,z=23..41
    # on x=-16..35,y=-41..10,z=-47..6
    # off x=-32..-23,y=11..30,z=-14..3
    # on x=-49..-5,y=-3..45,z=-29..18
    # off x=18..30,y=-20..-8,z=-3..13
    # on x=-41..9,y=-7..43,z=-33..15
    # on x=-54112..-39298,y=-85059..-49293,z=-27449..7877
    # on x=967..23432,y=45373..81175,z=27513..53682"""
    inp = []
    for line in data.strip().split("\n"):
        switch, cube = line.split(" ")
        on = switch[1] == "n"
        bounds = []
        for bound in cube.split(","):
            lo, hi = bound[2:].split("..")
            lo = int(lo)
            hi = int(hi)
            bounds.append([lo, hi])
        inp.append((on, bounds))


def part1(inp):
    space = numpy.zeros((101, 101, 101), dtype=bool)
    for on, bounds in inp:
        if not all(-50 <= b <= 50 for b in chain(*bounds)):
            continue
        ((xlo, xhi), (ylo, yhi), (zlo, zhi)) = bounds
        space[xlo + 50 : xhi + 51, ylo + 50 : yhi + 51, zlo + 50 : zhi + 51] = on
    return space.sum()


def volume(cube):
    return reduce(mul, (hi - lo + 1 for lo, hi in cube))


def intersect(me, other):
    on, me = me
    _, other = other
    bounds = []
    for (a1, a2), (b1, b2) in zip(me, other):
        c1 = max(a1, b1)
        c2 = min(a2, b2)
        if c1 <= c2:
            bounds.append((c1, c2))
        else:
            return None, []
    return not on, bounds


def solve(inp, limitp=False):
    c = []
    for cube in inp:
        if limitp and not all(-50 <= b <= 50 for b in chain(*cube[1])):
            continue
        newcubes = []
        for other in c:
            lit, area = intersect(other, cube)
            if area:
                newcubes.append((lit, area))
        on, _ = cube
        c.extend(newcubes)
        if on:
            c.append(cube)
    print(len(c))
    flip = [-1, 1]
    return sum(flip[on] * volume(cube) for on, cube in c)


def part2(inp):
    return solve(inp)


print(
    f"Day 22     {part1(inp):<13} {part2(inp):<14} {(time.time() - start)*1e6:>11.0f}"
)
