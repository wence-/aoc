with open("../inputs/2015/23.input", "r") as f:
    data = f.readlines()


def evaluate(program, regs=None):
    if regs is None:
        regs = {"a": 0,
                "b": 0}
    ops = {"inc": lambda x: x+1,
           "tpl": lambda x: x*3,
           "hlf": lambda x: x//2}
    jumps = {"jie": lambda x: x % 2 == 0,
             "jio": lambda x: x == 1}
    pc = 0
    while pc < len(program):
        op, reg, *args = program[pc].strip().split(" ")
        if op in ops:
            regs[reg] = ops[op](regs[reg])
            pc += 1
        elif op == "jmp":
            pc += int(reg)
        elif op in jumps:
            reg = reg[:-1]
            jmp, = args
            if jumps[op](regs[reg]):
                pc += int(jmp)
            else:
                pc += 1
        else:
            raise ValueError(f"Unknown op '{op}'")
    return regs


print("Part 1:", evaluate(data)["b"])
print("Part 2:", evaluate(data, regs={"a": 1, "b": 0})["b"])
