with open("inputs/day22.input", "r") as f:
    lines = f.readlines()


def affine(ncards, lines):
    a = 1
    b = 0
    for line in lines:
        if line.startswith("deal with"):
            n = int(line[len("deal with increment "):])
            a = (a * n) % ncards
            b = (b * n) % ncards
        elif line.startswith("cut "):
            n = int(line[4:])
            a = a
            b = (b - n) % ncards
        elif line.startswith("deal into new stack"):
            a = -a % ncards
            b = (ncards - 1 - b) % ncards
        else:
            raise ValueError("Unknown method")
    return a, b


def part1(lines):
    ncards = 10007
    nshuffles = 1
    card = 2019
    a, b = affine(ncards, lines)
    r = b * pow(1 - a, ncards - 2, ncards) % ncards
    return ((card - r) * pow(a, nshuffles, ncards) + r) % ncards


def part2(lines):
    ncards = 119315717514047
    nshuffles = 101741582076661
    pos = 2020
    a, b = affine(ncards, lines)
    r = b * pow(1 - a, ncards - 2, ncards) % ncards
    return ((pos - r) * pow(a, nshuffles*(ncards-2), ncards) + r) % ncards


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
