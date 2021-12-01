import numpy
import scipy.signal

../input/2018 = 8199

cells = numpy.zeros((300, 300), dtype=int)

for x, y in numpy.ndindex(*cells.shape):
    val = x + 10
    val *= y
    val += input
    val *= (x + 10)
    val = (val % 1000) // 100
    val -= 5
    cells[x, y] = val


sums = scipy.signal.convolve(cells, numpy.full((3, 3), 1), mode="valid")
val = sums.max()
pos = numpy.where(sums == val)

print(f"Part 1: {','.join(map(lambda x: str(x[0]), pos))}")

best = 0
for s in range(1, 300):
    sums = scipy.signal.convolve(cells, numpy.full((s, s), 1), mode="valid")
    val = sums.max()
    if val > best:
        best = val
        pos = numpy.where(sums == val)
        extent = s

print(f"Part 2: {','.join(map(lambda x: str(x[0]), pos))},{extent}")
