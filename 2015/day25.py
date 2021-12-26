import time

start = time.time()
row = 2978
col = 3083
idx = (row + col - 2) * (row + col - 1) // 2 + col - 1
part1 = 20151125 * pow(252533, idx, 33554393) % 33554393
part2 = 0

print(f"Day 25     {part1:<14} {part2:<14} {(time.time() - start)*1e3:>11.2f}")
