from itertools import chain, combinations

with open("inputs/17.input", "r") as f:
    data = list(map(int, f.read().strip().split("\n")))


nc = sum(1 for x in chain(*(combinations(data, i) for i in range(1, len(data) + 1)))
         if sum(x) == 150)

print("Part 1:", nc)

for minc in range(1, len(data) + 1):
    nc = sum(1 for x in combinations(data, minc) if sum(x) == 150)
    if nc > 0:
        break

print("Part 2:", nc)
