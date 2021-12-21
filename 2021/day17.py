import math
import time
from itertools import product

start = time.time()
with open("../inputs/2021/day17.input", "r") as f:
    data = f.read()
    # data = "target area: x=20..30, y=-10..-5"
    data = data[len("target area:") :]
    x, y = data.split(",")
    xmin, xmax = map(int, x[3:].split(".."))
    ymin, ymax = map(int, y[3:].split(".."))
    inp = (xmin, xmax, ymin, ymax)


def loc(v, t):
    return (1 / 2 + v) * t - t ** 2 / 2


def t_loc(v, loc):
    # Solve loc(v, t) = loc for t
    b = 1 / 2 + v
    disc = b ** 2 - 2 * loc
    # Only want real roots
    if disc < 0:
        return None
    else:
        l = b + math.sqrt(disc)
        r = b - math.sqrt(disc)
        return min(filter(lambda t: t >= 0, (l, r)))


def trange(v, enter, exit):
    lo = t_loc(v, enter)
    if lo is None:
        return None
    lo = math.ceil(lo)

    hi = t_loc(v, exit)
    hi = math.inf if hi is None else math.floor(hi)
    if lo <= hi:
        return lo, hi
    else:
        return None


def max_y(v):
    return round(loc(v, max(0, v)))


def intersects(a, b):
    return (a[0] <= b[1] and a[1] >= b[0]) or (b[0] <= a[1] and b[1] >= a[0])


def count(xmin, xmax, ymin, ymax):
    ys = []
    for y in range(ymin, -ymin):
        if (t := trange(y, ymax, ymin)) is not None:
            ys.append(t)
    xs = []
    for x in range(int(math.ceil(math.sqrt(1 + 8 * xmin) - 1) / 2), xmax + 1):
        if (t := trange(x, xmin, xmax)) is not None:
            xs.append(t)
    count = 0
    for x in xs:
        for y in ys:
            if intersects(x, y):
                count += 1
    return count


def part1(inp):
    _, _, ymin, _ = inp
    return (ymin * (ymin + 1)) // 2


def part2(inp):
    return count(*inp)


print(
    f"Day 17     {part1(inp):<13} {part2(inp):<14} {(time.time() - start)*1e6:>11.0f}"
)
