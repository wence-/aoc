import operator


def evaluate(instruction, regs):
    return instruction.update(regs)


class Instruction(object):
    def __init__(self, *operands):
        self.operands = tuple(operands)

    def update(self, regs):
        *_, c = self.operands
        a, b = self.../inputs/2018(regs)
        out = regs.copy()
        out[c] = self.op(a, b)
        return out


class RI(Instruction):
    def inputs(self, regs):
        a, b, _ = self.operands
        return (regs[a], b)


class IR(Instruction):
    def inputs(self, regs):
        a, b, _ = self.operands
        return (a, regs[b])


class RR(Instruction):
    def inputs(self, regs):
        a, b, _ = self.operands
        return (regs[a], regs[b])


class Addr(RR):
    op = operator.add


class Mulr(RR):
    op = operator.mul


class BAndr(RR):
    op = operator.and_


class BOrr(RR):
    op = operator.or_


class Addi(RI):
    op = operator.add


class Muli(RI):
    op = operator.mul


class BAndi(RI):
    op = operator.and_


class BOri(RI):
    op = operator.or_


class Setr(RR):
    op = lambda self, a, b: a


class Seti(IR):
    op = lambda self, a, b: a


class Gtir(IR):
    op = lambda self, a, b: int(a > b)


class Gtri(RI):
    op = lambda self, a, b: int(a > b)


class Gtrr(RR):
    op = lambda self, a, b: int(a > b)


class Eqir(IR):
    op = lambda self, a, b: int(a == b)


class Eqri(RI):
    op = lambda self, a, b: int(a == b)


class Eqrr(RR):
    op = lambda self, a, b: int(a == b)


with open("inputs/day16.input", "r") as f:
    lines = f.read().split("\n\n")

samples = []

i = 0
for line in lines:
    if not line.startswith("Before"):
        break
    i += 1
    ls = line.split("\n")
    sample = eval(ls[0][8:]), list(map(int, ls[1].split(" "))), eval(ls[2][8:])
    samples.append(sample)


count = 0

instructions = [Addr, Addi, Mulr, Muli, BAndr, BAndi, BOrr, BOri,
                Setr, Seti, Gtir, Gtri, Gtrr, Eqir, Eqri, Eqrr]
code2ins = dict((i, set(instructions)) for i in range(16))
for before, ins, after in samples:
    n = 0
    seen = set()
    for possible in instructions:
        out = possible(*ins[1:]).update(before)
        if out == after:
            seen.add(possible)
            n += 1
    if n >= 3:
        count += 1
    code2ins[ins[0]].intersection_update(seen)

print("Part 1:", count)

while True:
    unique_ops = dict((i, v) for i, v in code2ins.items() if len(v) == 1)
    for ui, uv in unique_ops.items():
        for i, v in code2ins.items():
            if i != ui:
                v.difference_update(uv)
    if len(unique_ops) == len(code2ins):
        break


ops = dict((i, v.pop()) for i, v in unique_ops.items())

regs = [0, 0, 0, 0]

for line in lines[-1].strip().split("\n"):
    op, *operands = map(int, line.split(" "))
    regs = ops[op](*operands).update(regs)

print("Part 2:", regs[0])
