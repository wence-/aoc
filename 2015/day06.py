import numpy

with open("inputs/06.input", "r") as f:
    lines = f.readlines()

lights = numpy.zeros((1000, 1000), dtype=int)

for line in lines:
    line = line.replace(" through ", ",")
    if line.startswith("turn on"):
        x, y, dx, dy = map(int, line[8:].split(","))
        lights[x:dx+1, y:dy+1] = 1
    elif line.startswith("turn off"):
        x, y, dx, dy = map(int, line[9:].split(","))
        lights[x:dx+1, y:dy+1] = 0
    elif line.startswith("toggle"):
        x, y, dx, dy = map(int, line[7:].split(","))
        lights[x:dx+1, y:dy+1] = (lights[x:dx+1, y:dy+1] + 1) % 2

print("Part 1:", lights.sum())

lights = numpy.zeros((1000, 1000), dtype=int)

for line in lines:
    line = line.replace(" through ", ",")
    if line.startswith("turn on"):
        x, y, dx, dy = map(int, line[8:].split(","))
        lights[x:dx+1, y:dy+1] += 1
    elif line.startswith("turn off"):
        x, y, dx, dy = map(int, line[9:].split(","))
        lights[x:dx+1, y:dy+1] -= 1
        s = lights[x:dx+1, y:dy+1]
        s[numpy.where(s < 0)] = 0
    elif line.startswith("toggle"):
        x, y, dx, dy = map(int, line[7:].split(","))
        lights[x:dx+1, y:dy+1] += 2

print("Part 2:", lights.sum())
