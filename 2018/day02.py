from collections import Counter

with open("../inputs/2018/day02.input", "r") as f:
    lines = f.readlines()

chksum = list(map(Counter, lines))
twos = sum((2 in c.values()) for c in chksum)
threes = sum((3 in c.values()) for c in chksum)

print(f"Part 1: {twos * threes}")


class Node(object):
    def __init__(self, char):
        self.char = char
        self.count = 1
        self.children = []
        self.word = None


root = Node('')


def add(root, word):
    node = root
    for char in word:
        for child in node.children:
            if child.char == char:
                node = child
                node.count += 1
                break
        else:
            new = Node(char)
            node.children.append(new)
            node = new
    node.word = word


for word in lines:
    add(root, word)


def print_trie(trie, off=0, newline=False):
    if trie.children == []:
        print("")
    else:
        for c in trie.children:
            if newline:
                print("")
                for _ in range(off):
                    print(" ", end="")
            print(c.char, end="")
            print_trie(c, off=(off+1), newline=(c.count != 1))


def search(trie, word):
    row = list(range(len(word) + 1))
    results = []
    for node in trie.children:
        search_(node, word, row, results)
    return results


def search_(node, word, prow, results):
    cols = len(word) + 1
    row = [prow[0] + 1]
    for col in range(1, cols):
        rcost = prow[col-1] + (word[col-1] != node.char)
        row.append(rcost)

    if row[-1] <= 1 and node.children == []:
        results.append((node, row[-1]))
    if min(row) <= 1:
        for n in node.children:
            search_(n, word, row, results)


for word in lines:
    matches = search(root, word)
    if any(x == 1 for (_, x) in matches):
        a, b = matches
        assert a[1] + b[1] == 1
        aset = set(a[0].word.strip())
        bset = set(b[0].word.strip())
        print("Part 2: ", end="")
        for a, b in zip(a[0].word, b[0].word):
            if a == b:
                print(a, end="")
        break
else:
    raise ValueError("Didn't satisfy problem")
