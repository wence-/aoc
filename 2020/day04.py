import re

passports = []

with open("inputs/day04.input", "r") as f:
    for desc in f.read().split("\n\n"):
        fields = re.split(r"\s+", desc.strip())
        passports.append(dict(f.split(":") for f in fields))


required = {"byr", "iyr", "eyr",
            "hgt", "hcl", "ecl",
            "pid"}

optional = {"cid"}


def part1(passports):
    nvalid = 0
    for passport in passports:
        if not required.difference(passport.keys()):
            nvalid += 1
    return nvalid


def part2(passports):
    nvalid = 0
    for passport in passports:
        if required.difference(passport.keys()):
            # Doesn't pass minimal check
            continue
        valid = True
        for req in required:
            val = passport[req]
            if req == "byr":
                match = re.match("^[0-9]{4}$", val)
                if not (match and 1920 <= int(val) <= 2002):
                    valid = False
                    break
            elif req == "iyr":
                match = re.match("^[0-9]{4}$", val)
                if not (match and 2010 <= int(val) <= 2020):
                    valid = False
                    break
            elif req == "eyr":
                match = re.match("^[0-9]{4}$", val)
                if not (match and 2020 <= int(val) <= 2030):
                    valid = False
                    break
            elif req == "hgt":
                match = re.match("^([0-9]+)(cm|in)$", val)
                if not (match and ((match.group(2) == "cm"
                                    and 150 <= int(match.group(1)) <= 193)
                                   or (match.group(2) == "in"
                                       and 59 <= int(match.group(1)) <= 76))):
                    valid = False
                    break
            elif req == "hcl":
                if not re.fullmatch("^#([0-9a-f]{6})$", val):
                    valid = False
                    break
            elif req == "ecl":
                if val not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
                    valid = False
                    break
            elif req == "pid":
                if not re.fullmatch("^[0-9]{9}$", val):
                    valid = False
                    break
        if valid:
            nvalid += 1
    return nvalid


print(f"Part 1: {part1(passports)}")
print(f"Part 2: {part2(passports)}")
