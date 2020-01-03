from collections import defaultdict
from functools import partial
from itertools import permutations

with open("inputs/13.input", "r") as f:
    data = f.readlines()


happiness = defaultdict(partial(defaultdict, int))
for line in data:
    who, _, what, val, *_, nextto = line.strip()[:-1].split(" ")
    if what == "lose":
        val = -int(val)
    else:
        val = int(val)
    happiness[who][nextto] = val


def happy(mapping):
    people = set(mapping)
    n = len(people)
    return max(sum(mapping[person][order[(i-1) % n]] + mapping[person][order[(i+1) % n]]
                   for i, person in enumerate(order))
               for order in permutations(people))


print("Part 1:", happy(happiness))
happiness["Me"] = defaultdict(int)
print("Part 2:", happy(happiness))
