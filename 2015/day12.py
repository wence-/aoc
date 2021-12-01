import itertools
import json
import numbers
from functools import partial

with open("../inputs/2015/12.input", "r") as f:
    data = json.loads(f.read())


def traverse(data, part2=False):
    if isinstance(data, dict):
        if part2 and "red" in data.values():
            return
        else:
            for k, v in data.items():
                yield from traverse(k, part2=part2)
                yield from traverse(v, part2=part2)
    elif isinstance(data, str):
        return
    elif isinstance(data, list):
        yield from itertools.chain(*(map(partial(traverse, part2=part2), data)))
    elif isinstance(data, numbers.Integral):
        yield data


print("Part 1:", sum(traverse(data)))
print("Part 2:", sum(traverse(data, part2=True)))
