with open("../inputs/2021/day01.input") as f:
    inp = list(map(int, f.readlines()))


def part1(inp):
    return sum(a < b for a, b in zip(inp, inp[1:]))


def part2(inp):
    return sum(a < b for a, b in zip(inp, inp[3:]))


print(f"Part 1: {part1(inp)}")
print(f"Part 2: {part2(inp)}")
