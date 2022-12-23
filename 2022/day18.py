import time

start = time.time()
with open("../inputs/2022/day18.input") as f:
    data = f.read()
    inp = {tuple(map(int, line.split(","))) for line in data.split("\n")}


moves = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
]


def part1(inp: set) -> int:
    return sum(
        (x + dx, y + dy, z + dz) not in inp
        for (dx, dy, dz) in moves
        for (x, y, z) in inp
    )


def part2(inp: set) -> int:
    minx, miny, minz = map(lambda x: x - 1, map(min, zip(*inp)))
    maxx, maxy, maxz = map(lambda x: x + 1, map(max, zip(*inp)))

    q = [(minx, miny, minz)]
    seen = {(minx, miny, minz)}
    count = 0
    while q:
        x, y, z = q.pop()
        for dx, dy, dz in moves:
            new = (x + dx, y + dy, z + dz)
            if new in inp:
                count += 1
            elif (
                minx <= new[0] <= maxx
                and miny <= new[1] <= maxy
                and minz <= new[2] <= maxz
                and new not in seen
            ):
                seen.add(new)
                q.append(new)
    return count


print(
    f"Day 18     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
