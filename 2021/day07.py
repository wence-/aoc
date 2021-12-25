import time

start = time.time()
with open("../inputs/2021/day07.input", "r") as f:
    inp = sorted(map(int, f.read().strip().split(",")))


def part1(inp):
    # Probably doesn't work for all inputs
    median = inp[len(inp) // 2]
    return sum(abs(k - median) for k in inp)


def part2(inp):
    # Probably doesn't work for all inputs
    mean = sum(inp) // len(inp)
    return sum((abs(k - mean) * (abs(k - mean) + 1)) // 2 for k in inp)


print(
    f"Day 07     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
