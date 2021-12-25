import time

import numpy

start = time.time()

with open("../inputs/2021/day25.input", "r") as f:
    data = f.read()

    lines = data.strip().split("\n")
    width = len(lines[0])
    height = len(lines)
    inp = numpy.zeros((width, height), dtype=int)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            inp[j, i] = {".": 0, ">": 1, "v": 2}[c]


def step(inp):
    width, height = inp.shape
    moved = False
    for (dx, dy, kind) in [(1, 0, 1), (0, 1, 2)]:
        new = inp.copy()
        x, y = numpy.where(inp == kind)
        next_x = (x + dx) % width
        next_y = (y + dy) % height
        freeslots = numpy.argwhere(inp[next_x, next_y] == 0)
        move_from = numpy.ravel_multi_index((x, y), inp.shape)[freeslots]
        move_to = numpy.ravel_multi_index((next_x, next_y), inp.shape)[freeslots]
        moved |= len(freeslots) > 0

        new.flat[move_to] = kind
        new.flat[move_from] = 0
        inp = new
    return moved, inp


def part1(inp):
    n = 0
    while True:
        moved, inp = step(inp)
        if not moved:
            return n + 1
        n += 1


print(f"Day 25     {part1(inp):<14} {(time.time() - start)*1e3:>26.2f}")
