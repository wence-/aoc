import time
from heapq import heapreplace as replace

start = time.time()
with open("../inputs/2022/day01.input") as f:
    inp = [sum(map(int, block.strip().split())) for block in f.read().split("\n\n")]


def part1(inp: list[int]) -> int:
    return max(inp)


def part2(inp: list[int]) -> int:
    result = [0, 0, 0]
    best = 0
    for e in inp:
        if best < e:
            # Probably a depth-3 sorting network would be faster in a
            # compiled language?
            replace(result, (best := e))
    return sum(result)


print(
    f"Day 01     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
