import time

start = time.time()


def encode(line):
    direction, distance = line.split(" ")
    return {"U": 1j, "D": -1j, "L": -1, "R": 1}[direction] * int(distance)


with open("../inputs/2022/day09.input") as f:
    inp = list(map(encode, f.read().split("\n")))


def part1(inp: list[complex]) -> int:
    head = 0 + 0j
    tail = 0 + 0j
    locations = {tail}
    for move in inp:
        head = head + move
        while abs(diff := head - tail) > 1.4142135623730951:
            re = diff.real
            im = diff.imag
            tail = (
                tail + (re // abs(re) if re else 0) + (im // abs(im) if im else 0) * 1j
            )
            locations.add(tail)
    return len(locations)


def part2(inp: list) -> int:
    rope = [0 + 0j for _ in range(10)]
    locations = {rope[-1]}
    for move in inp:
        for _ in range((size := int(abs(move)))):
            rope[0] = rope[0] + (move.real // size + 1j * (move.imag // size))
            for i in range(1, len(rope)):
                h = rope[i - 1]
                t = rope[i]
                diff = h - t
                if abs(diff) > 1.4142135623730951:
                    re = diff.real
                    im = diff.imag
                    t = (
                        t
                        + (re // abs(re) if re else 0)
                        + (im // abs(im) if im else 0) * 1j
                    )
                rope[i] = t
            locations.add(rope[-1])
    return len(locations)


print(
    f"Day 09     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
