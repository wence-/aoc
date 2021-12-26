from collections import deque
from itertools import cycle

inputa = 400, 71864
inputb = 400, 71864 * 100


def run(nplayer, maxval):
    players = dict((n, 0) for n in range(nplayer))
    circle = deque()
    circle.append(0)
    for i, p in enumerate(cycle(range(nplayer)), start=1):
        if i % 23 == 0:
            circle.rotate(-7)
            players[p] += i + circle.pop()
        else:
            circle.rotate(2)
            circle.append(i)
        if i == maxval:
            break
    return players


print(f"Part1: {max(run(*inputa).values())}")
print(f"Part2: {max(run(*inputb).values())}")
