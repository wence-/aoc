import time

start = time.time()
with open("../inputs/2015/05.input", "r") as f:
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


part1 = sum(map(nice, lines))
part2 = sum(map(nice2, lines))

print(f"Day 05     {part1:<14} {part2:<14} {(time.time() - start)*1e3:>11.2f}")
