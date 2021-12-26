from collections import defaultdict
from itertools import combinations

with open("../inputs/2020/day14.input", "r") as f:
    instructions = f.readlines()


class Mask:
    def __init__(self, s):
        s = s.strip()
        assert s.startswith("mask =")
        s = s[7:]
        self.mask = s
        assert len(s) == 36
        self.setbits = int(s.replace("X", "0"), 2)
        self.unsetbits = int(s.replace("X", "1"), 2)
        self.floatmask = int(s.replace("0", "1").replace("X", "0"), 2)
        self.floating = tuple((35 - i for i, c in enumerate(s) if c == "X"))

    def update1(self, b):
        return (b & self.unsetbits) | self.setbits

    def update2(self, b):
        return (b | self.setbits) & self.floatmask


class Write:
    def __init__(self, s):
        s = s.strip()
        self.mem = s
        assert s.startswith("mem[")
        self.idx = int(s[4 : s.find("]")])
        self.val = int(s[s.find("=") + 1 :])

    def write1(self, mem, mask):
        mem[self.idx] = mask.update1(self.val)

    def write2(self, mem, address, bits):
        mem[address | sum(2 ** b for b in bits)] = self.val


instructions = list(
    Mask(ins) if ins.startswith("mask = ") else Write(ins) for ins in instructions
)


def part1(instructions):
    mem = defaultdict(int)
    mask = None
    for ins in instructions:
        if isinstance(ins, Mask):
            mask = ins
        else:
            assert mask is not None
            ins.write1(mem, mask)

    return sum(mem.values())


def part2(instructions):
    mem = defaultdict(int)
    mask = None
    for ins in instructions:
        if isinstance(ins, Mask):
            mask = ins
        else:
            assert mask is not None
            address = mask.update2(ins.idx)
            for i in range(len(mask.floating) + 1):
                for bits in combinations(mask.floating, i):
                    ins.write2(mem, address, bits)
    return sum(mem.values())


print(f"Part 1: {part1(instructions)}")
print(f"Part 2: {part2(instructions)}")
