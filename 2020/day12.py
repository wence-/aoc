def parse(line):
    line = line.strip()
    c = line[:1]
    n = int(line[1:])
    if c in {"L", "R"}:
        assert n % 90 == 0
        n //= 90
    return c, n


with open("../inputs/2020/day12.input", "r") as f:
    instructions = list(map(parse, f.readlines()))


class Ferry:
    def __init__(self):
        self.pos = (0, 0)
        self.facing = 1
        self.waypoint = (10, 1)

    move = {"E": lambda we, ns, n: (we+n, ns),
            "W": lambda we, ns, n: (we-n, ns),
            "N": lambda we, ns, n: (we, ns+n),
            "S": lambda we, ns, n: (we, ns-n)}
    rotate = {"R": lambda f, n: [0, 1, 2, 3][(f + n) % 4],
              "L": lambda f, n: [0, 1, 2, 3][(f - n) % 4]}
    FACING = {0: "N", 1: "E", 2: "S", 3: "W"}

    def move1(self, c, n):
        if c == "F":
            self.pos = self.move[self.FACING[self.facing]](*self.pos, n)
        elif c in self.move:
            self.pos = self.move[c](*self.pos, n)
        elif c in self.rotate:
            self.facing = self.rotate[c](self.facing, n)
        else:
            raise ValueError(f"Unhandled instruction {c}")

    def move2(self, c, n):
        way_we, way_ns = self.waypoint
        if c in self.move:
            self.waypoint = self.move[c](*self.waypoint, n)
        elif c == "F":
            WE, NS = self.pos
            self.pos = WE + n*way_we, NS + n*way_ns
        elif c == "L":
            for _ in range(n):
                way_we, way_ns = self.waypoint
                self.waypoint = -way_ns, way_we
        elif c == "R":
            for _ in range(n):
                way_we, way_ns = self.waypoint
                self.waypoint = way_ns, -way_we
        else:
            raise ValueError(f"Unhandled unstruction {c}")


def part1(instructions):
    ferry = Ferry()
    for c, n in instructions:
        ferry.move1(c, n)
    return sum(map(abs, ferry.pos))


def part2(instructions):
    ferry = Ferry()
    for c, n in instructions:
        ferry.move2(c, n)
    return sum(map(abs, ferry.pos))


print(f"Part 1: {part1(instructions)}")
print(f"Part 2: {part2(instructions)}")
