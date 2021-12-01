import hashlib
from itertools import count

salt = "iwrupvqb"
for i ../in/2015 count():
    hsh = hashlib.md5(f"{salt}{i}".encode())
    if hsh.hexdigest()[:5] == "00000":
        print("Part 1:", i)
    if hsh.hexdigest()[:6] == "000000":
        print("Part 2:", i)
        break
