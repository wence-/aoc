from itertools import product
from typing import Iterable

T = tuple[int, int]
OCTS = dict[tuple[int, int], int]

with open("../inputs/2021/day11.input", "r") as f:
    data = f.read()
    data = data.strip().split("\n")
    octs: OCTS = {}
    for i, line in enumerate(data):
        for j, c in enumerate(map(int, line.strip())):
            octs[i, j] = c
    N, M = map(max, zip(*octs))
    N += 1
    M += 1


def neighbours(i: int, j: int) -> Iterable[T]:
    for di, dj in product((-1, 0, 1), (-1, 0, 1)):
        if 0 <= i + di < N and 0 <= j + dj < M and not (di == 0 and dj == 0):
            yield (i + di, j + dj)


def step(octs: OCTS) -> int:
    for k in octs:
        octs[k] += 1
    seeds = set(k for k, v in octs.items() if v > 9)
    flashed = set()
    while seeds:
        seed = seeds.pop()
        flashed.add(seed)
        for idx in neighbours(*seed):
            octs[idx] += 1
            if idx not in flashed and octs[idx] > 9:
                seeds.add(idx)
    for idx in flashed:
        octs[idx] = 0
    return len(flashed)


def part1(octs: OCTS) -> int:
    octs = octs.copy()
    return sum(step(octs) for _ in range(100))


def part2(octs: OCTS) -> int:
    octs = octs.copy()
    i = 0
    while any(v != 0 for v in octs.values()):
        step(octs)
        i += 1
    return i


print(part1(octs))
print(part2(octs))
