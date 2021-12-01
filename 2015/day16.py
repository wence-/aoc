
with open("../inputs/2015/16.input", "r") as f:
    data = f.readlines()

sues = {}
for i, line in enumerate(data, start=1):
    _, _, *stuff = line.split(" ")
    sue = set()
    for k, v in zip(stuff[::2], stuff[1::2]):
        sue.add((k[:-1], int(v[:-1])))
    sues[i] = sue


target = set([("children", 3),
              ("cats", 7),
              ("samoyeds", 2),
              ("pomeranians", 3),
              ("akitas", 0),
              ("vizslas", 0),
              ("goldfish", 5),
              ("trees", 3),
              ("cars", 2),
              ("perfumes", 1)])

possibles = set()
for i, sue in sues.items():
    if sue & target == sue:
        possibles.add(i)


sue, = possibles
print("Part 1:", sue)


possibles = set()
target_ = dict(target)
for i, sue in sues.items():
    add = True
    for k, v in sue:
        if k in {"cats", "trees"} and v <= target_[k]:
            add = False
            break
        elif k in {"pomeranians", "goldfish"} and v >= target_[k]:
            add = False
            break
        elif k not in {"cats", "trees", "pomeranians", "goldfish"} and v != target_[k]:
            add = False
            break
    if add:
        possibles.add(i)

sue, = possibles
print("Part 2:", sue)
