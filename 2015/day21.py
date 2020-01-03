import math
from collections import Counter
from itertools import chain, combinations, product

boss = {"hp": 104,
        "damage": 8,
        "armor": 1}

me = Counter({"hp": 100,
              "damage": 0,
              "armor": 0})

weapons = {
    "Dagger": {"cost": 8, "damage": 4, "armor": 0},
    "Shortsword": {"cost": 10, "damage": 5, "armor": 0},
    "Warhammer": {"cost": 25, "damage": 6, "armor": 0},
    "Longsword": {"cost": 40, "damage": 7, "armor": 0},
    "Greataxe": {"cost": 74, "damage": 8, "armor": 0},
}

armor = {
    "Leather": {"cost": 13, "damage": 0, "armor": 1},
    "Chainmail": {"cost": 31, "damage": 0, "armor": 2},
    "Splintmail": {"cost": 53, "damage": 0, "armor": 3},
    "Bandedmail": {"cost": 75, "damage": 0, "armor": 4},
    "Platemail": {"cost": 102, "damage": 0, "armor": 5},
}

rings = {
    "Damage +1": {"cost": 25, "damage": 1, "armor": 0},
    "Damage +2": {"cost": 50, "damage": 2, "armor": 0},
    "Damage +3": {"cost": 100, "damage": 3, "armor": 0},
    "Defense +1": {"cost": 20, "damage": 0, "armor": 1},
    "Defense +2": {"cost": 40, "damage": 0, "armor": 2},
    "Defense +3": {"cost": 80, "damage": 0, "armor": 3},
}


def combine(items):
    c = Counter()
    for item in items:
        c.update(item)
    return c


def viable(choice):
    me_ = combine([me, choice])
    memoves = math.ceil(boss["hp"] / max(me_["damage"] - boss["armor"], 1))
    bossmoves = math.ceil(me["hp"] / max(boss["damage"] - me_["armor"], 1))
    return memoves <= bossmoves


choices = map(combine, product(weapons.values(), chain([Counter()], armor.values()),
                               chain([Counter()], rings.values(),
                                     map(combine, combinations(rings.values(), 2)))))

print("Part 1:", min(choice["cost"] for choice in choices if viable(choice)))
choices = map(combine, product(weapons.values(), chain([Counter()], armor.values()),
                               chain([Counter()], rings.values(),
                                     map(combine, combinations(rings.values(), 2)))))

print("Part 2:", max(choice["cost"] for choice in choices if not viable(choice)))
