with open("../inputs/2018/day05.input", "r") as f:
    polymer = f.read().strip()


def merge(polymer, remove=None):
    if remove is not None:
        polymer = [x for x in polymer if x.lower() != remove]
    out = []
    for c in polymer:
        if out and out[-1] == c.swapcase():
            out.pop()
        else:
            out.append(c)
    return len(out)


print(f"Part 1: {merge(polymer)}")

candidates = set(polymer.lower())
min_ = min(merge(polymer, remove=c) for c in candidates)
print(f"Part 2: {min_}")
