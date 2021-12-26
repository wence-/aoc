import time

import numpy

start = time.time()
target = 36000000

bound = target // 10

A = numpy.zeros(bound, dtype=int)
B = numpy.zeros(bound, dtype=int)

for i in range(1, bound):
    A[i::i] += 10 * i
    B[i : (i + 1) * 50 : i] += 11 * i

((part1, *_),) = numpy.where(A >= target)
((part2, *_),) = numpy.where(B >= target)

print(f"Day 20     {part1:<14} {part2:<14} {(time.time() - start)*1e3:>11.2f}")
