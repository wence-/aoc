import numpy

with open("../inputs/2018/day04.input", "r") as f:
    lines = f.readlines()


class Guard(object):
    def __init__(self, id_):
        self.id_ = id_
        self.asleep = []
        self.awake = []

    def summary(self):
        asleep = numpy.zeros(60, dtype=int)
        for (s, e) in self.asleep:
            asleep[s:e] += 1
        return asleep


def parse(lines):
    state = None
    guard = None
    guards = {}
    estart = 0
    for line in lines:
        time = line[12:17]
        x = line.find("#")
        hr, mins = map(int, time.split(":"))
        if x > -1:
            if guard is not None:
                if state == "asleep":
                    guard.asleep.append((estart, 60))
                elif state == "awake":
                    guard.awake.append((estart, 60))
            e = line[x:].find(" ")
            id_ = int(line[x + 1 : x + e])
            guard = guards.get(id_)
            if guard is None:
                guard = guards.setdefault(id_, Guard(id_))
            if hr == 23:
                estart = 0
            else:
                estart = mins
            state = "awake"
        if line.find("wakes up") > 0:
            assert state == "asleep"
            guard.asleep.append((estart, mins))
            state = "awake"
        elif line.find("falls asleep") > 0:
            assert state == "awake"
            guard.awake.append((estart, mins))
            state = "asleep"
        estart = mins
    return guards


guards = parse(lines)

max_ = -1
id__ = -1

for id_, guard in guards.items():
    lmax = numpy.sum(guard.summary())
    if lmax > max_:
        max_ = lmax
        id__ = id_

print(f"Part 1: {id__*numpy.argmax(guards[id__].summary())}")


max_ = -1
id__ = -1
for id_, guard in guards.items():
    lmax = numpy.max(guard.summary())
    if lmax > max_:
        max_ = lmax
        id__ = id_

print(f"Part 2: {id__*numpy.argmax(guards[id__].summary())}")
