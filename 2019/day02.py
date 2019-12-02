from itertools import product

from intcode import CPU, load

mem = load("day02.input")


def part1(mem):
    cpu = CPU(mem)
    cpu.mem[1:3] = 12, 2
    cpu.run()
    return cpu.mem[0]


def part2(mem):
    for a, b in product(range(100, -1, -1), range(100, -1, -1)):
        cpu = CPU(mem)
        cpu.mem[1:3] = a, b
        cpu.run()
        if cpu.mem[0] == 19690720:
            return 100*a + b


print(f"Part 1: {part1(mem)}")
print(f"Part 2: {part2(mem)}")
