import time
from functools import reduce
from operator import and_

from more_itertools import grouper

start = time.time()
with open("../inputs/2022/day03.input") as f:
    inp = [
        (set(line[: (mid := len(line) // 2)]), set(line[mid:]))
        for line in f.read().split("\n")
    ]


def score(char):
    return 1 + ord(char) - (ord("A") - 26 if char <= "Z" else ord("a"))


def part1(inp: list[tuple[set, set]]) -> int:
    return sum(map(score, ((a & b).pop() for a, b in inp)))


def part2(inp: list[tuple[set, set]]) -> int:
    return sum(
        map(
            score,
            (
                reduce(and_, ((a | b) for a, b in group)).pop()
                for group in grouper(inp, 3, incomplete="strict")
            ),
        )
    )


print(
    f"Day 03     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
