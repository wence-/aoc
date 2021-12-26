from operator import add, mul

import pyparsing as pp

with open("../inputs/2020/day18.input", "r") as f:
    lines = f.readlines()


digits = pp.Word(pp.nums).setParseAction(lambda tok: int(tok[0]))
mulop = pp.Literal("*").setParseAction(lambda tok: mul)
addop = pp.Literal("+").setParseAction(lambda tok: add)


def evaluate(result):
    try:
        (r,) = result
        return evaluate(r)
    except ValueError:
        *a, op, b = result
        return op(evaluate(a), evaluate(b))
    except TypeError:
        return result


def run(oplist):
    parser = pp.infixNotation(digits, oplist)
    parser.enablePackrat()
    return sum(evaluate(parser.parseString(line).asList()) for line in lines)


def part1(lines):
    return run([(mulop ^ addop, 2, pp.opAssoc.LEFT)])


def part2(lines):
    return run([(addop, 2, pp.opAssoc.LEFT), (mulop, 2, pp.opAssoc.LEFT)])


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
