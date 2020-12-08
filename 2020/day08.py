from contextlib import contextmanager
from enum import IntEnum


class CPU:
    class Op(IntEnum):
        NOP = 1
        ACC = 2
        JMP = 3

    NOP = Op.NOP
    ACC = Op.ACC
    JMP = Op.JMP

    class HaltError(Exception):
        pass

    def __init__(self, program):
        self.load(program)
        self.reset()

    @staticmethod
    def decode(ins):
        op, n = ins.split(" ")
        opmap = {"nop": CPU.NOP,
                 "acc": CPU.ACC,
                 "jmp": CPU.JMP}
        try:
            return opmap[op], int(n)
        except KeyError:
            raise RuntimeError(f"Unsupported instruction {op}")

    def load(self, program):
        with open(program, "r") as f:
            self.instructions = list(map(self.decode, f.readlines()))

    def reset(self):
        self.ip = 0
        self.accumulator = 0

    def isinf(self):
        seen = set()
        try:
            while self.ip not in seen:
                seen.add(self.ip)
                self.step()
        except CPU.HaltError:
            return False
        else:
            return True

    @contextmanager
    def modified_instruction(self, i, opmap):
        op, v = self.instructions[i]
        newop = opmap[op]
        self.instructions[i] = (newop, v)
        yield
        self.instructions[i] = (op, v)

    def step(self):
        try:
            op, v = self.instructions[self.ip]
        except IndexError:
            raise CPU.HaltError()
        if op == self.JMP:
            self.ip += v
        elif op == self.ACC:
            self.accumulator += v
            self.ip += 1
        elif op == self.NOP:
            self.ip += 1
        else:
            raise RuntimeError(f"Unhandled instruction {op}")


cpu = CPU("inputs/day08.input")


def part1(cpu):
    cpu.reset()
    if not cpu.isinf():
        raise RuntimeError("Expecting infinite loop")
    return cpu.accumulator


def part2(cpu):
    opmap = {CPU.NOP: CPU.JMP,
             CPU.JMP: CPU.NOP,
             CPU.ACC: CPU.ACC}
    for i in range(len(cpu.instructions)):
        cpu.reset()
        with cpu.modified_instruction(i, opmap):
            if not cpu.isinf():
                return cpu.accumulator
    raise RuntimeError("Expected to terminate")


print(f"Part 1: {part1(cpu)}")
print(f"Part 2: {part2(cpu)}")
