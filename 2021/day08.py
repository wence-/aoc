from collections import defaultdict
from functools import reduce
from itertools import chain
from operator import and_, xor

with open("../inputs/2021/day08.input", "r") as f:
    inputs = []
    outputs = []
    data = f.read().strip()
    for line in data.split("\n"):
        i, o = line.strip().split(" | ")
        inputs.append(i.split(" "))
        outputs.append(o.split(" "))


def part1(_, outputs):
    return sum(len(o) in {2, 3, 4, 7} for o in chain(*outputs))


# 0: a b c e f g
# 1: c f
# 2: a c d e g           a
# 3: a c d f g         b   c
# 4: b c d f             d
# 5: a b d f g         e   f
# 6: a b d e f g         g
# 7: a c f
# 8: a b c d e f g
# 9: a b c d f g
def decode(inputs, outputs):
    data = defaultdict(set)
    for digit in inputs:
        data[len(digit)].add(frozenset(digit))
    # Convention:
    # numbers => set of characters for that digit
    # letters => encoding of given letter
    (one,) = data[2]
    (four,) = data[4]
    (seven,) = data[3]
    eg = set(i - (four | seven) for i in data[5])
    cf = set(i & one for i in data[6])
    (a,) = seven - one
    (c,) = xor(*cf)
    (e,) = xor(*eg)
    (f,) = and_(*cf)
    (g,) = and_(*eg)
    bde = set(i - (seven | {g}) for i in data[5])
    (d,) = reduce(and_, bde)
    (b,) = four - (seven | {d})
    digits = {}
    digits[frozenset([a, b, c, e, f, g])] = 0
    digits[frozenset([c, f])] = 1
    digits[frozenset([a, c, d, e, g])] = 2
    digits[frozenset([a, c, d, f, g])] = 3
    digits[frozenset([b, c, d, f])] = 4
    digits[frozenset([a, b, d, f, g])] = 5
    digits[frozenset([a, b, d, e, f, g])] = 6
    digits[frozenset([a, c, f])] = 7
    digits[frozenset([a, b, c, d, e, f, g])] = 8
    digits[frozenset([a, b, c, d, f, g])] = 9
    return sum(10 ** i * digits[frozenset(d)] for i, d in enumerate(reversed(outputs)))


def part2(inputs, outputs):
    return sum(decode(*io) for io in zip(inputs, outputs))


print(part1(inputs, outputs))
print(part2(inputs, outputs))
