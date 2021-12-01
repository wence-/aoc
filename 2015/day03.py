with open("../inputs/2015/03.input", "r") as f:
    data = f.read().strip()

directions = {"v": -1j, "^": 1j, "<": -1, ">": 1}

start = 0
seen = {start}

for c in data:
    start += directions[c]
    seen.add(start)

print("Part 1:", len(seen))

start = 0
rstart = 0
seen = {start}
rseen = {rstart}

moves = iter(data)
for s, r in zip(moves, moves):
    start += directions[s]
    rstart += directions[r]
    seen.add(start)
    rseen.add(rstart)

print("Part 2:", len(seen | rseen))
