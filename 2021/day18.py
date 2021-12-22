import time
from functools import cache
from itertools import combinations

start = time.time()


def tuplify(data):
    if isinstance(data, int):
        return data
    else:
        return tuple(map(tuplify, data))


with open("../inputs/2021/day18.input", "r") as f:
    data = f.read()
    inp = []
    inp2 = []
    for line in data.strip().split("\n"):
        num = []
        d = 0
        for c in line:
            if c == "[":
                d += 1
            elif c == "]":
                d -= 1
            elif c == ",":
                pass
            else:
                num.append([d, int(c)])
        inp2.append(num)
        inp.append(tuplify(eval(line)))
    inp = tuple(inp)


@cache
def add(l, n, toleft):
    if isinstance(l, int):
        return l + n
    l_, r_ = l
    if toleft:
        return (add(l_, n, True), r_)
    else:
        return (l_, add(r_, n, False))


@cache
def explode(n, depth=0):
    if isinstance(n, int):
        return False, n, (None, None)
    if depth == 4:
        l, r = n
        return True, 0, (l, r)
    left, right = n
    changed, lo, (l, r) = explode(left, depth=depth + 1)
    if changed:
        if r is not None:
            return True, (lo, add(right, r, True)), (l, None)
        else:
            return True, (lo, right), (l, r)
    changed, ro, (l, r) = explode(right, depth=depth + 1)
    if changed:
        if l is not None:
            return True, (add(left, l, False), ro), (None, r)
        else:
            return True, (left, ro), (l, r)
    return False, (lo, ro), (None, None)


@cache
def split(n):
    if isinstance(n, int):
        if n >= 10:
            return True, (n // 2, (n + 1) // 2)
        else:
            return False, n
    else:
        l, r = n
        changed, l_ = split(l)
        if changed:
            return True, (l_, r)
        changed, r_ = split(r)
        if changed:
            return True, (l, r_)
        return False, n


def reduce(n):
    while True:
        changed, n, _ = explode(n)
        if changed:
            continue
        changed, n = split(n)
        if changed:
            continue
        break
    return n


def magnitude(n) -> int:
    if isinstance(n, int):
        return n
    l, r = n
    return 3 * magnitude(l) + 2 * magnitude(r)


def part1(inp):
    left, *rest = inp
    while rest:
        right, *rest = rest
        left = reduce((left, right))
    return magnitude(left)


def part2(inp):
    return max(
        max(magnitude(reduce((a, b))), magnitude(reduce((b, a))))
        for a, b in combinations(inp, 2)
    )


print(
    f"Day 18     {part1(inp):<13} {part2(inp):<14} {(time.time() - start)*1e6:>11.0f}"
)
