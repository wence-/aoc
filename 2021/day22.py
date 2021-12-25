import time
from functools import cache

import numpy

start = time.time()

with open("../inputs/2021/day22.input", "r") as f:
    data = f.read()
    inp = []
    for line in data.strip().split("\n"):
        switch, cube = line.split(" ")
        on = switch[1] == "n"
        bounds = []
        for bound in cube.split(","):
            lo, hi = bound[2:].split("..")
            bounds.append(int(lo))
            bounds.append(int(hi))
        inp.append((on, tuple(bounds)))
    inp = tuple(inp)


def part1(inp):
    space = numpy.zeros((101, 101, 101), dtype=bool)
    for on, bounds in inp:
        if not all(-50 <= b <= 50 for b in bounds):
            continue
        xlo, xhi, ylo, yhi, zlo, zhi = bounds
        space[xlo + 50 : xhi + 51, ylo + 50 : yhi + 51, zlo + 50 : zhi + 51] = on
    return space.sum()


def volume(cube):
    x1, x2, y1, y2, z1, z2 = cube
    return (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)


def clip(a, b):
    x1, x2, y1, y2, z1, z2 = a
    a1, b2, c1, d2, e1, f2 = b

    x1 = max(x1, a1)
    x2 = min(x2, b2)
    if x1 >= x2:
        return None

    y1 = max(y1, c1)
    y2 = min(y2, d2)
    if y1 >= y2:
        return None
    z1 = max(z1, e1)
    z2 = min(z2, f2)
    if z1 >= z2:
        return None
    return x1, x2, y1, y2, z1, z2


def clipped(clipper, clipees):
    return tuple(
        sorted(
            cube
            for cube in (clip(clipee, clipper) for clipee in clipees)
            if cube is not None
        )
    )


@cache
def sum_volume(cubes):
    if len(cubes) == 0:
        return 0
    cube = cubes[0]
    cubes = cubes[1:]
    overlap = sum_volume(clipped(cube, cubes))
    return volume(cube) + sum_volume(cubes) - overlap


def solve(inp):
    if len(inp) == 0:
        return 0
    on, cube = inp[0]
    rest = inp[1:]
    if not on:
        return solve(rest)
    overlap = sum_volume(clipped(cube, (cube for _, cube in rest)))
    return volume(cube) + solve(rest) - overlap


def part2(inp):
    return solve(inp)


print(f"Day 22     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>9.2f}")
