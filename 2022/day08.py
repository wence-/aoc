import time
from itertools import count

start = time.time()
with open("../inputs/2022/day08.input") as f:
    data = f.read()
    inp = [list(map(int, line)) for line in data.split("\n")]


def part1(inp: list) -> int:
    visible = set()
    for i, line in enumerate(inp):
        maxseen = -1
        for j, c in enumerate(line):
            if c > maxseen:
                visible.add((i, j))
                maxseen = c
        maxseen = -1
        for j, c in enumerate(line[::-1]):
            if c > maxseen:
                visible.add((i, (len(line) - j - 1)))
                maxseen = c
    transposed = list(zip(*inp))
    for j, c in enumerate(transposed):
        rowmax = -1
        for i, line in enumerate(c):
            if line > rowmax:
                visible.add((i, j))
                rowmax = line
        rowmax = -1
        for i, line in enumerate(c[::-1]):
            if line > rowmax:
                visible.add((len(c) - i - 1, j))
                rowmax = line
    return len(visible)


def ray_length(line, pos, direction, n):
    val = line[pos]
    for i in count():
        pos += direction
        if pos == -1 or pos == n:
            return i
        if line[pos] >= val:
            return i + 1
    raise ValueError


def score(i, j, row, col, n):
    return (
        ray_length(row, j, -1, n)
        * ray_length(row, j, 1, n)
        * ray_length(col, i, -1, n)
        * ray_length(col, i, 1, n)
    )


def part2(inp: list) -> int:
    n = len(inp)
    k = len(inp[0])
    transposed = list(zip(*inp))
    return max(
        score(i, j, inp[i], transposed[j], n) for i in range(n) for j in range(k)
    )


print(
    f"Day 08     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
