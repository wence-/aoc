import time

start = time.time()
with open("../inputs/2015/01.input", "r") as f:
    data = f.read().strip()

part1 = data.count("(") - data.count(")")

level = 0
for i, c in enumerate(data, start=1):
    level += {"(": 1, ")": -1}[c]
    if level == -1:
        part2 = i
        break


print(f"Day 01     {part1:<14} {part2:<14} {(time.time() - start)*1e3:>11.2f}")
