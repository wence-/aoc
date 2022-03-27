import time

import numpy

start = time.time()

DIM = 502
INPUT_SMALL = 100
INPUT_BIG = 500

with open("../inputs/2021/day15.input", "r") as f:
    data = f.read().strip()
    inp = [0] * DIM * DIM
    for r, line in enumerate(data.split("\n")):
        for c, char in enumerate(line):
            inp[DIM * (r + 1) + 1 + c] = int(char)
delta = [-1, 1, -DIM, DIM]


def search(r, c, lookup):
    goal = DIM * r + c
    Q = [[] for _ in range(17)]
    Q[0].append(DIM + 1)
    qi = 0
    while True:
        Q[16].clear()
        Q[qi % 16], Q[16] = Q[16], Q[qi % 16]
        for p in Q[16]:
            if lookup[p] == 0:
                continue
            if p == goal:
                return qi
            lookup[p] = 0
            for di in delta:
                n = p + di
                if lookup[n] == 0:
                    continue
                Q[(qi + lookup[n]) % 16].append(n)
        qi += 1


def part1(graph):
    graph = list(graph)
    return search(INPUT_SMALL, INPUT_SMALL, graph)


def replicate(graph):
    N = INPUT_BIG // INPUT_SMALL
    small = numpy.asarray(graph, dtype=object).reshape(DIM, DIM)[
        1 : INPUT_SMALL + 1, 1 : INPUT_SMALL + 1
    ]

    big = numpy.hstack(
        [
            (numpy.vstack([(small + i - 1) % 9 + 1 for i in range(N)]) + j - 1) % 9 + 1
            for j in range(N)
        ]
    )

    out = numpy.zeros((DIM, DIM), dtype=object)
    out[1 : INPUT_BIG + 1, 1 : INPUT_BIG + 1] = big
    return list(out.flat)


def part2(graph):
    graph = replicate(graph)
    return search(INPUT_BIG, INPUT_BIG, graph)


print(
    f"Day 15     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
