import time

start = time.time()
with open("../inputs/2015/03.input", "r") as f:
    data = f.read().strip()

directions = {"v": -1j, "^": 1j, "<": -1, ">": 1}

begin = 0
seen = {start}

for c in data:
    begin += directions[c]
    seen.add(begin)

part1 = len(seen)

begin = 0
rstart = 0
seen = {start}
rseen = {rstart}

moves = iter(data)
for s, r in zip(moves, moves):
    begin += directions[s]
    rstart += directions[r]
    seen.add(begin)
    rseen.add(rstart)

part2 = len(seen | rseen)

print(f"Day 03     {part1:<14} {part2:<14} {(time.time() - start)*1e3:>11.2f}")
