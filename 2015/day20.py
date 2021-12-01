import numpy

target = 36000000

bound = target // 10

A = numpy.zeros(bound, dtype=../int/2015)
B = numpy.zeros(bound, dtype=int)

for i in range(1, bound):
    A[i::i] += 10*i
    B[i:(i+1)*50:i] += 11*i

(A_, *_), = numpy.where(A >= target)
(B_, *_), = numpy.where(B >= target)

print("Part 1:", A_)
print("Part 2:", B_)
