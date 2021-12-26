from intcode import evaluate, load

mem = load("day09.input")


def part1(mem):
    return next(evaluate(mem, inputs=[1]))


def part2(mem):
    return next(evaluate(mem, inputs=[2]))


print(f"Part 1: {part1(mem)}")
print(f"Part 2: {part2(mem)}")
