import re

passports = []

with open("../inputs/2020/day04.input", "r") as f:
    for desc in f.read().split("\n\n"):
        fields = re.split(r"\s+", desc.strip())
        passports.append(dict(f.split(":") for f in fields))


def byr(val):
    match = re.match("^[0-9]{4}$", val)
    return (match and 1920 <= int(val) <= 2002)


def iyr(val):
    match = re.match("^[0-9]{4}$", val)
    return (match and 2010 <= int(val) <= 2020)


def eyr(val):
    match = re.match("^[0-9]{4}$", val)
    return (match and 2020 <= int(val) <= 2030)


def hgt(val):
    match = re.match("^([0-9]+)(cm|in)$", val)
    return (match and ((match.group(2) == "cm"
                        and 150 <= int(match.group(1)) <= 193)
                       or (match.group(2) == "in"
                           and 59 <= int(match.group(1)) <= 76)))


def hcl(val):
    return re.match("^#[0-9a-f]{6}$", val) is not None


def ecl(val):
    return val in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def pid(val):
    return re.match("^[0-9]{9}$", val) is not None


required = {"byr": byr,
            "iyr": iyr,
            "eyr": eyr,
            "hgt": hgt,
            "hcl": hcl,
            "ecl": ecl,
            "pid": pid}

optional = {"cid"}


def part1(passports):
    req = set(required)

    def valid(p):
        return set(p).issuperset(req)

    return sum(map(valid, passports))


def part2(passports):
    def valid(p):
        return (set(p).issuperset(required)
                and all(v(p[k]) for k, v in required.items()))
    return sum(map(valid, passports))


print(f"Part 1: {part1(passports)}")
print(f"Part 2: {part2(passports)}")
