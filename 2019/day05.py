from intcode import evaluate, load

mem = load("day05.input")


def part1(mem):
    *_, out = evaluate(mem, inputs=[1])
    return out


print(f"Part 1: {part1(mem)}")


def part2(mem):
    *_, out = evaluate(mem, inputs=[5])
    return out


print(f"Part 2: {part2(mem)}")
