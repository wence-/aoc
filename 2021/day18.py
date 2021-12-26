import time
from functools import reduce
from itertools import chain, combinations

start = time.time()


with open("../inputs/2021/day18.input", "r") as f:
    inp = []
    for line in f.read().strip().split("\n"):
        values = []
        depths = []
        depth = 0
        for c in line.strip():
            if c == "[":
                depth += 1
            elif c == "]":
                depth -= 1
            elif c == ",":
                pass
            else:
                values.append(int(c))
                depths.append(depth)
        inp.append((values, depths))


def magnitude(values, depths):
    while depths[0]:
        i = 0
        while depths[i] != depths[i + 1]:
            i += 1
        values.insert(i, values.pop(i) * 3 + values.pop(i) * 2)
        l = depths.pop(i) - 1
        depths[i] = l
    return values[0]


def explode(values, depths):
    i = 0
    while depths[i] < 5:
        i += 1
    l = depths[i] - 1

    if i - 1 >= 0:
        values[i - 1] += values.pop(i)
        depths.pop(i)
    else:
        values.pop(i)
        depths.pop(i)

    if i + 1 < len(values):
        x = values.pop(i)
        depths.pop(i)
        values[i] += x
    else:
        values.pop(i)
        depths.pop(i)

    values.insert(i, 0)
    depths.insert(i, l)
    return (values, depths)


def split(values, levels):
    i = 0
    while values[i] < 10:
        i += 1
    v = values[i]
    l = levels[i] + 1
    values.pop(i)
    levels.pop(i)
    low = v // 2
    high = (v + 1) // 2

    values.insert(i, high)
    values.insert(i, low)
    levels.insert(i, l)
    levels.insert(i, l)
    return (values, levels)


def add(left, right):
    lval, ldepth = left
    rval, rdepth = right
    values = lval + rval
    depths = [d + 1 for d in chain(ldepth, rdepth)]

    while True:
        if max(depths) >= 5:
            values, depths = explode(values, depths)
        elif max(values) >= 10:
            values, depths = split(values, depths)
        else:
            break

    return values, depths


def part1(inp):
    return magnitude(*reduce(add, inp))


def part2(inp):
    return max(
        max(magnitude(*add(a, b)), magnitude(*add(b, a)))
        for a, b in combinations(inp, 2)
    )


print(
    f"Day 18     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
