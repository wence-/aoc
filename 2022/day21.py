import time
from dataclasses import dataclass
from operator import add, floordiv, mul, sub
from typing import Any, Callable, ClassVar, cast

start = time.time()
with open("../inputs/2022/day21.input") as f:
    inp = dict(line.split(": ") for line in f.read().split("\n"))


mapping = {"+": add, "-": sub, "*": mul, "/": floordiv}


def as_expr(o):
    if isinstance(o, Expr):
        return o
    return Literal(o)


@dataclass
class Expr:
    operands: tuple["Expr", ...] | int | str
    inverse: ClassVar[Callable[[Any, Any], Any]]

    def __mul__(self, o: "Expr"):
        return Mul((self, as_expr(o)))

    def __sub__(self, o: "Expr"):
        return Sub((self, as_expr(o)))

    def __floordiv__(self, o: "Expr"):
        return Div((self, as_expr(o)))

    def __add__(self, o: "Expr"):
        return Add((self, as_expr(o)))

    def __rmul__(self, o):
        return Mul((self, as_expr(o)))

    def __rsub__(self, o):
        return Sub((as_expr(o), self))

    def __radd__(self, o):
        return Add((self, as_expr(o)))


class Literal(Expr):
    operands: int


class Var(Expr):
    operands: str


class Mul(Expr):
    inverse = floordiv


class Add(Expr):
    inverse = sub


class Div(Expr):
    inverse = mul


class Sub(Expr):
    inverse = add


def evaluate(who: str, inp: dict[str, Any], bindings: dict) -> int | Expr:
    val = inp[who]
    if who in bindings:
        return bindings[who]
    try:
        return bindings.setdefault(who, int(val))
    except ValueError:
        pass
    x, op, y = val.split(" ")
    return bindings.setdefault(
        who, mapping[op](evaluate(x, inp, bindings), evaluate(y, inp, bindings))
    )


def part1(inp: dict) -> int:
    return cast(int, evaluate("root", inp, {}))


def part2(inp: dict) -> int:
    left, _, right = inp["root"].split(" ")
    inp = inp | {"humn": (x := Var("x"))}
    left = evaluate(left, inp, {"humn": x})
    right = evaluate(right, inp, {"humn": x})
    assert isinstance(right, int)
    while left != x:
        match left:
            case Sub((Literal(l), r)):
                right = l - right
                left = r
            case Expr((l, Literal(r))):
                right = left.inverse(right, r)
                left = l
            case _:
                assert False
    return right


print(
    f"Day 21     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
