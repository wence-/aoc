with open("inputs/05.input", "r") as f:
    lines = f.readlines()

vowels = frozenset("aeiou")
bad = frozenset(["ab", "cd", "pq", "xy"])


def nice(line):
    nvowel = len([c for c in line if c in vowels])
    if nvowel < 3:
        return False
    if not any(a == b for a, b in zip(line, line[1:])):
        return False
    pairs = set((a + b for a, b in zip(line, line[1:])))
    return len(pairs & bad) == 0


def nice2(line):
    if not any(a == b for a, b in zip(line, line[2:])):
        return False
    pairs = set((a + b for a, b in zip(line, line[1:])))
    n = len(line)
    return any(len(line.replace(p, "")) + 4 == n for p in pairs)


print("Part 1:", sum(map(nice, lines)))
print("Part 2:", sum(map(nice2, lines)))
