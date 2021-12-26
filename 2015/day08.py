import ast
import json
import time

start = time.time()
with open("../inputs/2015/08.input", "r") as f:
    data = f.readlines()
    data = [line[:-1] for line in data]

ondisk = sum(map(len, data))
inmem = sum(map(len, map(ast.literal_eval, data)))
encoded = sum(map(len, map(json.dumps, data)))

part1 = ondisk - inmem
part2 = encoded - ondisk

print(f"Day 08     {part1:<14} {part2:<14} {(time.time() - start)*1e3:>11.2f}")
