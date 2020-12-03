from itertools import product

with open("inputs/day01.input", "r") as f:
    data = set(map(lambda x: int(x.strip()), f.readlines()))


def part1(data):
    return next(n*(2020-n) for n in data
                if 2020 - n in data)


def part2(data):
    return next(n*p*(2020-n-p) for n, p in product(data, data)
                if 2020 - n - p in data)


print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
