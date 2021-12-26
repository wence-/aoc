with open("../inputs/2020/day05.input", "r") as f:
    data = f.readlines()

mapping = {"F": "0", "B": "1", "R": "1", "L": "0"}
ids = set(int("".join(map(mapping.get, d.strip())), 2) for d in data)


def part1(ids):
    return max(ids)


def part2(ids):
    (x,) = (
        seat
        for seat in range(max(ids) + 1)
        if (seat not in ids and (seat + 1) in ids and (seat - 1) in ids)
    )
    return x


print(f"Part 1: {part1(ids)}")
print(f"Part 2: {part2(ids)}")
