import hashlib
import time
from itertools import count

start = time.time()

salt = "iwrupvqb"
part1 = None
for i in count():
    hsh = hashlib.md5(f"{salt}{i}".encode())
    if hsh.hexdigest()[:5] == "00000" and part1 is None:
        part1 = i
    if hsh.hexdigest()[:6] == "000000":
        part2 = i
        break


print(f"Day 04     {part1:<14} {part2:<14} {(time.time() - start)*1e3:>11.2f}")
