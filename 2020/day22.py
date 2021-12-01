from collections import deque

with open("../inputs/2020/day22.input", "r") as f:
    zero, one = f.read().strip().split("\n\n")

zero = deque(map(int, zero.strip().splitlines()[1:]))
one = deque(map(int, one.strip().splitlines()[1:]))


def part1(zero, one):
    zero = deque(list(zero))
    one = deque(list(one))
    while zero and one:
        a = zero.popleft()
        b = one.popleft()
        assert a != b
        if a > b:
            zero.extend([a, b])
        else:
            one.extend([b, a])
    return sum(i*x for i, x in enumerate(reversed(zero or one), start=1))


def part2(zero, one):
    zero = deque(list(zero))
    one = deque(list(one))

    def recurse(zero, one):
        seen = set()
        while zero and one:
            key = tuple(zero), tuple(one)
            if key in seen:
                return 0
            seen.add(key)
            a = zero.popleft()
            b = one.popleft()
            if len(zero) >= a and len(one) >= b:
                # we'll recurse
                winner = (zero, one)[recurse(deque(list(zero)[:a]),
                                             deque(list(one)[:b]))]
            else:
                assert a != b
                winner = (zero, one)[int(a < b)]
            if winner is zero:
                winner.extend([a, b])
            else:
                winner.extend([b, a])
        return int(winner is one)

    winner = (zero, one)[recurse(zero, one)]
    return sum(i*x for i, x in enumerate(reversed(winner), start=1))


print(part1(zero, one))
print(part2(zero, one))
