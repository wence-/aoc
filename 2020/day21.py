from collections import defaultdict

recipes = []
possible = defaultdict(list)
all_ingredients = set()
with open("inputs/day21.input", "r") as f:
    for line in f.readlines():
        recipe, allergens = line.strip()[:-1].split(" (contains ")
        ingredients = set(recipe.split(" "))
        recipes.append(ingredients)
        all_ingredients.update(ingredients)
        for allergen in allergens.split(", "):
            possible[allergen].append(set(ingredients))


def known_allergens(possible):
    known = dict((k, set.intersection(*v))
                 for k, v in possible.items())
    toremove = list(filter(lambda p: len(p) == 1, known.values()))
    while toremove:
        found = toremove.pop()
        for k, v in known.items():
            if len(v) == 1:
                continue
            v -= found
            if len(v) == 1:
                toremove.append(v)
    return known


known = known_allergens(possible)


def part1(known, recipes):
    noallergens = all_ingredients - set.union(*known.values())
    return sum(len(recipe & noallergens) for recipe in recipes)


def part2(known):
    return ",".join(f"{next(iter(known[k]))}" for k in sorted(known))


print("Part 1:", part1(known, recipes))
print("Part 2:", part2(known))
