import math
from itertools import islice

with open("../inputs/2019/day10.input", "r") as f:
    data = f.read().strip().split("\n")


def setup(data):
    field = set()
    for y, row in enumerate(data):
        for x, col in enumerate(row):
            if col == "#":
                field.add((x, y))
    return field


def move(a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    g = math.gcd(dx, dy)
    return (dx, dy), (dx // g, dy // g)


def prune(pos, field):
    maxx, maxy = map(max, zip(*field))
    pruned = field - {pos}
    for p in field - {pos}:
        (dx, dy), (ix, iy) = move(pos, p)
        (nx, ny) = (pos[0] + dx, pos[1] + dy)
        while True:
            nx += ix
            ny += iy
            if 0 <= nx <= maxx and 0 <= ny <= maxy:
                pruned -= {(nx, ny)}
            else:
                break
    return pruned, len(pruned), pos


def part1(data):
    field = setup(data)
    return max(prune(p, field)[1] for p in field)


def destruction_order(data):

    field = setup(data)
    *_, pos = max((prune(p, field) for p in field), key=lambda x: x[1])

    def direction(a):
        x, y = pos
        X, Y = a
        return (X - x < 0, math.atan2(X - x, y - Y))

    left = field.copy() - {pos}
    while left:
        toremove = sorted(prune(pos, left)[0], key=direction)
        yield from toremove
        left.difference_update(toremove)


def part2(data):
    (x, y), = islice(destruction_order(data), 199, 200)
    return x*100 + y


print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
