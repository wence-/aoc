import ast
import json

with open("../inputs/2015/08.input", "r") as f:
    data = f.readlines()
    data = [line[:-1] for line in data]

ondisk = sum(map(len, data))
inmem = sum(map(len, map(ast.literal_eval, data)))
encoded = sum(map(len, map(json.dumps, data)))

print("Part 1:", ondisk - inmem)
print("Part 1:", encoded - ondisk)
