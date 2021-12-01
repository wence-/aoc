from intcode import evaluate, load

mem = load("day21.input")


def part1(mem):
    # !(A & C) & D
    spring = ["OR A J",
              "AND C J",
              "NOT J J",
              "AND D J",
              "WALK",
              ""]
    *_, out = evaluate(mem, ../inputs/2019=map(ord, "\n".join(spring)))
    return out


def part2(mem):
    # !(A & B & (!H | C)) & D
    spring = ["OR A J",
              "AND B J",
              "NOT H T",
              "OR C T",
              "AND T J",
              "NOT J J",
              "AND D J",
              "RUN",
              ""]
    *_, out = evaluate(mem, inputs=map(ord, "\n".join(spring)))
    return out


print("Part 1", part1(mem))
print("Part 2", part2(mem))
