import time

start = time.time()
with open("../inputs/2021/day01.input") as f:
    inp = list(map(int, f.readlines()))


def part1(inp):
    return sum(a < b for a, b in zip(inp, inp[1:]))


def part2(inp):
    return sum(a < b for a, b in zip(inp, inp[3:]))


print(
    f"Day 01     {part1(inp):<13} {part2(inp):<14} {(time.time() - start)*1e6:>13.0f}"
)
