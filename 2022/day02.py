import time

start = time.time()
with open("../inputs/2022/day02.input") as f:
    inp = [tuple(ord(c) - ord(b) for c, b in zip(line.split(), "AX")) for line in f]


# Rock-paper-scissors
def part1(inp: list[tuple[int, int]]) -> int:
    # rock == 0, paper == 1, scissors == 2
    # score is 0 for loss, 3 for draw, 6 for win
    # "shape" score is shape + 1
    return sum(me + 1 + 3 * ((me - you + 1) % 3) for you, me in inp)


def part2(inp: list[tuple[int, int]]) -> int:
    # back out desired shape from result
    # scoring as for part 1
    return sum((you + result + 2) % 3 + 1 + 3 * result for you, result in inp)


print(
    f"Day 02     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
