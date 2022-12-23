import time

start = time.time()
with open("../inputs/2022/day15.input") as f:
    inp = []
    for line in f.read().split("\n"):
        sensor, beacon = line.split(": ")
        a, b = sensor[10:].split(", ")
        a, b = int(a[2:]), int(b[2:])
        c, d = beacon[21:].split(", ")
        c, d = int(c[2:]), int(d[2:])
        inp.append((a, b, abs(a - c) + abs(b - d)))


def part1(inp: list) -> int:
    return 0


def part2(inp: list) -> int:
    return 0


print(
    f"Day 15     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
