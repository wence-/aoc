import time
from typing import Iterable

Tidx = tuple[int, int]
Toct = dict[Tidx, int]

start = time.time()
with open("../inputs/2021/day11.input", "r") as f:
    data = f.read()
    data = data.strip().split("\n")
    inp: Toct = {}
    for i, line in enumerate(data):
        for j, c in enumerate(map(int, line.strip())):
            inp[i, j] = c
    N, M = map(max, zip(*inp))
    N += 1
    M += 1


def neighbours(i: int, j: int) -> Iterable[Tidx]:
    for di, dj in (
        (i - 1, j - 1),
        (i, j - 1),
        (i + 1, j - 1),
        (i - 1, j),
        (i + 1, j),
        (i - 1, j + 1),
        (i, j + 1),
        (i + 1, j + 1),
    ):
        if 0 <= di < N and 0 <= dj < M:
            yield di, dj


def step(octopuses: Toct) -> int:
    for k in octopuses:
        octopuses[k] += 1
    lifo = [k for k, v in octopuses.items() if v > 9]
    seen = set()
    while lifo:
        seed = lifo.pop()
        if seed not in seen:
            seen.add(seed)
            for i in neighbours(*seed):
                octopuses[i] += 1
                if i not in seen and octopuses[i] > 9:
                    lifo.append(i)
    for idx in seen:
        octopuses[idx] = 0
    return len(seen)


def part1(octopuses: Toct) -> int:
    octopuses = octopuses.copy()
    return sum(step(octopuses) for _ in range(100))


def part2(octopuses: Toct) -> int:
    octopuses = octopuses.copy()
    i = 0
    while any(v != 0 for v in octopuses.values()):
        step(octopuses)
        i += 1
    return i


print(
    f"Day 11     {part1(inp):<13} {part2(inp):<14} {(time.time() - start)*1e6:>11.0f}"
)
