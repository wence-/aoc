import time
from typing import Any

start = time.time()


def rle(digits):
    prev = None
    c = 1
    for d in digits:
        if d != prev:
            if prev is not None:
                yield c, prev
            c = 1
            prev = d
        else:
            c += 1
    else:
        yield c, prev


def say(digits):
    return "".join(str(n) + d for n, d in rle(digits))


s = "1113222113"
for _ in range(40):
    s = say(s)

part1 = len(s)

for _ in range(10):
    s = say(s)
part2 = len(s)

print(f"Day 10     {part1:<14} {part2:<14} {(time.time() - start)*1e3:>11.2f}")
