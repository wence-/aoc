from itertools import cycle, islice

import numpy

with open("../inputs/2019/day16.input", "r") as f:
    data = f.read().strip()


def part1(data):
    arr = list(map(int, data))
    for _ in range(100):
        for i in range(len(arr)):
            arr[i] = (
                abs(
                    sum(
                        sum(arr[off : off + i + 1]) * sign
                        for off, sign in zip(
                            range(i, len(arr), 2 * i + 2), cycle([1, -1])
                        )
                    )
                )
                % 10
            )
    return "".join(map(str, arr[:8]))


def part2(data):
    offset = int(data[:7])
    digits = cycle(reversed(list(map(int, data))))
    end = 10000 * len(data) - offset
    arr = numpy.asarray(list(islice(digits, end)), dtype=int)
    for _ in range(100):
        arr = numpy.cumsum(arr) % 10
    return "".join(map(str, arr[::-1][:8]))


print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
