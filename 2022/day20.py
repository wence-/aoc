import time
from collections import deque

start = time.time()
with open("../inputs/2022/day20.input") as f:
    inp = list(enumerate(map(int, f.read().split("\n"))))


def part1(inp: list) -> int:
    stuff = list(inp)
    N = len(inp)

    def loc(idx):
        for j, (i, n) in enumerate(stuff):
            if i == idx:
                return (j, n)
        raise ValueError

    def pos(v):
        for j, (_, n) in enumerate(stuff):
            if n == v:
                return (j, n)
        raise ValueError

    for i in range(len(inp)):
        j, n = loc(i)
        stuff.remove((i, n))
        stuff.insert((j + n) % (N - 1), (i, n))

    j, n = pos(0)
    return sum(stuff[(j + n) % N][1] for n in [1000, 2000, 3000])


def part2(inp: list) -> int:
    stuff = list(((i, n * 811589153) for i, n in inp))
    N = len(inp)

    def loc(idx):
        for j, (i, n) in enumerate(stuff):
            if i == idx:
                return (j, n)
        raise ValueError

    def pos(v):
        for j, (_, n) in enumerate(stuff):
            if n == v:
                return (j, n)
        raise ValueError

    for _ in range(10):
        for i in range(len(inp)):
            j, n = loc(i)
            stuff.remove((i, n))
            stuff.insert((j + n) % (N - 1), (i, n))

    j, n = pos(0)
    return sum(stuff[(j + n) % N][1] for n in [1000, 2000, 3000])


print(
    f"Day 20     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
