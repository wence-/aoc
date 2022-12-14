import re
import time

start = time.time()
with open("../inputs/2015/19.input", "r") as f:
    data = f.readlines()

replacements = []
for line in data[:-2]:
    (m,) = re.findall(r"(\S+) => (\S+)", line)
    replacements.append(m)

molecule = data[-1].strip()

seen = set()
for i, j in replacements:
    for k in range(len(molecule)):
        if molecule[k : k + len(i)] == i:
            y = molecule[:k] + j + molecule[k + len(i) :]
            seen.add(y)
part1 = len(seen)


reps = dict((v[::-1], k[::-1]) for (k, v) in replacements)
patt = re.compile("|".join(reps.keys()))


def rep(x):
    return reps[x.group()]


count = 0
X = molecule[::-1]
while X != "e":
    X = re.sub(patt, rep, X, 1)
    count += 1

part2 = count

print(f"Day 19     {part1:<14} {part2:<14} {(time.time() - start)*1e3:>11.2f}")
