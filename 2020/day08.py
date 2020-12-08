from enum import IntEnum


class Op(IntEnum):
    NOP = 1
    ACC = 2
    JMP = 3


class HaltError(Exception):
    pass


class CPU:
    def __init__(self, program):
        self.load(program)
        self.reset()

    def load(self, program):
        self.instructions = []
        with open(program, "r") as f:
            for ins in f.readlines():
                if ins[:3] == "nop":
                    self.instructions.append((Op.NOP, int(ins[4:])))
                elif ins[:3] == "acc":
                    self.instructions.append((Op.ACC, int(ins[4:])))
                elif ins[:3] == "jmp":
                    self.instructions.append((Op.JMP, int(ins[4:])))
                else:
                    raise RuntimeError(f"Unsupported instruction {ins}")

    def reset(self):
        self.ip = 0
        self.accumulator = 0

    def isinf(self):
        seen = set()
        while self.ip not in seen:
            seen.add(self.ip)
            try:
                self.step()
            except HaltError:
                return False
        return True

    def step(self):
        try:
            op, v = self.instructions[self.ip]
        except IndexError:
            raise HaltError()
        if op == Op.JMP:
            self.ip += v
            return
        elif op == Op.ACC:
            self.accumulator += v
            self.ip += 1
            return
        elif op == Op.NOP:
            self.ip += 1
            return
        else:
            raise RuntimeError(f"Unhandled instruction {op}")


cpu = CPU("inputs/day08.input")


def part1(cpu):
    cpu.reset()
    assert cpu.isinf()
    return cpu.accumulator


def part2(cpu):
    opmap = {Op.NOP: Op.JMP, Op.JMP: Op.NOP, Op.ACC: Op.ACC}
    for i in range(len(cpu.instructions)):
        cpu.reset()
        op, v = cpu.instructions[i]
        cpu.instructions[i] = (opmap[op], v)
        if cpu.isinf():
            cpu.instructions[i] = (op, v)
        else:
            cpu.instructions[i] = (op, v)
            return cpu.accumulator


print(f"Part 1: {part1(cpu)}")
print(f"Part 2: {part2(cpu)}")
