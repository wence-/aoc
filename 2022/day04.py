import time

start = time.time()
with open("../inputs/2022/day04.input") as f:
    inp = [
        tuple(tuple(map(int, part.split("-"))) for part in line.split(","))
        for line in f.read().split("\n")
    ]


def contains(sections):
    (s1, e1), (s2, e2) = sections
    return (s2 <= s1 and e1 <= e2) or (s1 <= s2 and e2 <= e1)


def overlaps(sections):
    (s1, e1), (s2, e2) = sections
    return s1 <= e2 and s2 <= e1


def part1(inp: list[tuple[tuple[int], tuple[int]]]) -> int:
    return sum(map(contains, inp))


def part2(inp: list[tuple[tuple[int], tuple[int]]]) -> int:
    return sum(map(overlaps, inp))


print(
    f"Day 04     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
