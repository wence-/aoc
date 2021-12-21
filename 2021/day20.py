import time

import numpy
import scipy.signal

start = time.time()
with open("../inputs/2021/day20.input", "r") as f:
    data = f.read().strip()

    encoding, inp = data.split("\n\n")

    encoding = numpy.asarray(
        [0 if c == "." else 1 for c in encoding.strip()], dtype=int
    )

    inp = numpy.asarray(
        [
            [0 if c == "." else 1 for c in line.strip()]
            for line in inp.strip().split("\n")
        ],
        dtype=int,
    )


stencil = numpy.logspace(0, 8, num=9, base=2, dtype=int).reshape(3, 3)


def step(image, padvalue):
    return encoding[
        scipy.signal.convolve2d(image, stencil, mode="full", fillvalue=padvalue).astype(
            int
        )
    ]


def solve(image, n):
    pad = 0
    for _ in range(n):
        image = step(image, pad)
        pad = encoding[511 * pad]
    return image.sum()


def part1(image):
    return solve(image, 2)


def part2(image):
    return solve(image, 50)


print(
    f"Day 20     {part1(inp):<13} {part2(inp):<14} {(time.time() - start)*1e6:>11.0f}"
)
