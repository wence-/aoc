from intcode import evaluate, load

mem = load("day13.input")


def part1(mem):
    outputs = evaluate(mem)
    return sum(t == 2 for _, _, t in zip(outputs, outputs, outputs))


def part2(mem):
    mem = mem.copy()
    mem[0] = 2

    def moves():
        directions = (-1, 1)
        while True:
            yield directions[ball > paddle] * (ball != paddle)

    outputs = evaluate(mem, inputs=moves())
    for x, _, id_ in zip(outputs, outputs, outputs):
        if x == -1:
            score = id_
        elif id_ == 3:
            paddle = x
        elif id_ == 4:
            ball = x
    return score


print("Part 1:", part1(mem))
print("Part 2:", part2(mem))
