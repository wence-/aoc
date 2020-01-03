with open("inputs/01.input", "r") as f:
    data = f.read().strip()

print("Part 1:", data.count("(") - data.count(")"))

level = 0
for i, c in enumerate(data, start=1):
    level += {"(": 1, ")": -1}[c]
    if level == -1:
        print("Part 2:", i)
        break
