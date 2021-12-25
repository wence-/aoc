import time
from functools import partial, reduce
from operator import eq, gt, lt, mul

start = time.time()
with open("../inputs/2021/day16.input", "r") as f:
    inp = f.read()


def to_chunks(data):
    mapping = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }
    return "".join(mapping[c] for c in data)


def parse_version(chunks):
    version = int(chunks[:3], 2)
    return version, chunks[3:]


SUM = 0b000
MUL = 0b001
MIN = 0b010
MAX = 0b011
VAL = 0b100
GT = 0b101
LT = 0b110
EQ = 0b111

OPS = {
    SUM: sum,
    MUL: partial(reduce, mul),
    MIN: min,
    MAX: max,
    GT: lambda v: gt(*v),
    LT: lambda v: lt(*v),
    EQ: lambda v: eq(*v),
}


def parse_type(chunks):
    type = int(chunks[:3], 2)
    return type, chunks[3:]


def parse_literal(chunks):
    value = 0
    while True:
        block = int(chunks[:5], 2)
        chunks = chunks[5:]
        value <<= 4
        value |= block & 0b01111
        if not (block & 0b10000):
            break
    return value, chunks


def parse_operator(chunks):
    typ = int(chunks[:1], 2)
    chunks = chunks[1:]
    cut = {1: 11, 0: 15}[typ]
    n = int(chunks[:cut], 2)
    chunks = chunks[cut:]
    return (typ, n), chunks


def parse_packet(chunks):
    version, rest = parse_version(chunks)
    typ, rest = parse_type(rest)
    if typ == VAL:
        value, rest = parse_literal(rest)
        return rest, version, value
    else:
        (length_type, n), rest = parse_operator(rest)
        values = []
        if length_type == 1:
            # Parse a fixed number of packets
            for _ in range(n):
                rest, v, value = parse_packet(rest)
                values.append(value)
                version += v
        else:
            # Parse a fixed number of bits
            sub = rest[:n]
            while sub:
                sub, v, value = parse_packet(sub)
                values.append(value)
                version += v
            rest = rest[n:]
        # Evaluate the values
        value = OPS[typ](values)
    return rest, version, value


def part1(inp):
    return parse_packet(to_chunks(inp))[1]


def part2(inp):
    return parse_packet(to_chunks(inp))[2]


print(
    f"Day 16     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
