import numpy
from intcode import evaluate, load
from scipy.signal import convolve

mem = load("day17.input")


def part1(mem):
    stencil = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    grid = numpy.fromiter(evaluate(mem), dtype=int)
    ((y, *_),) = numpy.where(grid == ord("\n"))
    grid = grid[grid != ord("\n")].reshape(-1, y)
    x, y = numpy.where(convolve(grid, stencil, mode="valid") == 5 * ord("#"))
    return ((x + 1) * (y + 1)).sum()


def part2(mem):
    # Determined by hand
    path = (
        "L,10,R,10,L,10,L,10,"
        "R,10,R,12,L,12,"
        "L,10,R,10,L,10,L,10,"
        "R,10,R,12,L,12,"
        "R,12,L,12,R,6,"
        "R,12,L,12,R,6,"
        "R,10,R,12,L,12,"
        "L,10,R,10,L,10,L,10,"
        "R,10,R,12,L,12,"
        "R,12,L,12,R,6"
    )

    steps = path.split(",")
    # Shorten it
    vars = {}
    for var in ["A", "B", "C"]:
        best = None
        start = 0
        while steps[start] in {"A", "B", "C"}:
            start += 1
        for x in range(2, len(steps)):
            temp = ",".join(steps[start : start + x])
            if len(temp) > 20 or "A" in temp or "B" in temp or "C" in temp:
                break
            if ",".join(steps).count(temp) > 1 and temp[-1] in "0123456789":
                best = temp
        steps = ",".join(steps)
        steps = steps.replace(best, var)
        vars[var] = best
        steps = steps.split(",")

    commands = [",".join(steps)]
    commands.extend(vars[n] for n in "ABC")
    commands.append("n\n")

    mem = mem.copy()
    mem[0] = 2
    *_, retval = evaluate(mem, inputs=map(ord, "\n".join(commands)))
    return retval


print("Part 1:", part1(mem))
print("Part 2:", part2(mem))
