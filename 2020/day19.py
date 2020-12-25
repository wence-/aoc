import regex

with open("inputs/day19.input", "r") as f:
    rules, strings = f.read().strip().split("\n\n")

messages = list(s.strip() for s in strings.strip().split("\n"))
rules = dict(rule.replace('"', '').split(": ", 1)
             for rule in rules.splitlines())


def compile(rule, rules):
    def expand(rule):
        if not rule.isdigit():
            return rule
        return f"(?:{''.join(map(expand, rules[rule].split()))})"

    return regex.compile(f"^{expand(rule)}$")


def part1(messages, rules):
    r = compile("0", rules)
    return sum(r.match(m) is not None for m in messages)


def part2(messages, rules):
    rules = rules.copy()
    # one or more of rule 42
    rules["8"] = "42 +"
    # match 42 and bind recursive pattern, finish with 31. Need this
    # rather than one or more because pattern needs equal numbers of
    # 42 and 31 subrules.
    rules["11"] = "(?P<R> 42 (?&R)? 31 )"

    r = compile("0", rules)
    return sum(r.match(m) is not None for m in messages)


print(f"Part 1: {part1(messages, rules)}")
print(f"Part 2: {part2(messages, rules)}")
