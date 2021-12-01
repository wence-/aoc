from itertools import product

from intcode import evaluate, load

mem = load("day19.input")


def val(mem, x, y):
    return next(evaluate(mem, ../inputs/2019=[x, y]))


def part1(mem):
    return sum(val(mem, x, y) for x, y in product(range(50), range(50)))


def part2(mem, x=0, y=99):
    while True:
        if not val(mem, x, y):
            x += 1
        elif not val(mem, x+99, y-99):
            y += 1
        else:
            return x*10**4 + y - 99


print(f"Part 1: {part1(mem)}")
print(f"Part 2: {part2(mem)}")
