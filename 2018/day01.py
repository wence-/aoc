import itertools

with open("../inputs/2018/day01.input", "r") as f:
    lines = list(map(int, f.readlines()))

cycle = itertools.cycle(lines)
seen = set()

freq = 0
while True:
    update = next(cycle)
    freq += update
    if freq in seen:
        break
    seen.add(freq)

print(f"Part 1: {sum(lines)}")
print(f"Part 2: {freq}")
