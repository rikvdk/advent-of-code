import sys
from functools import reduce
from operator import mul


def read_workflows():
    workflows = {}

    for line in sys.stdin:
        line = line.strip()[:-1]
        if not line:
            break

        name, rest = line.split("{")
        workflows[name] = []
        for rule in rest.split(","):
            if ":" not in rule:
                workflows[name].append(rule)
            else:
                val, result = rule[2:].split(":")
                workflows[name].append((rule[0], rule[1], int(val), result))
    return workflows


def is_accepted(workflows, part, name="in"):
    # print(f"{name} -> ", end="")
    if name == "A": return True
    if name == "R": return False

    for rule in workflows[name]:
        if isinstance(rule, str):
            return is_accepted(workflows, part, rule)

        if rule[1] == "<" and part[rule[0]] < rule[2]:
            return is_accepted(workflows, part, rule[3])

        if rule[1] == ">" and part[rule[0]] > rule[2]:
            return is_accepted(workflows, part, rule[3])

    return True


def total_combinations(workflows, xmas, name="in"):
    if name == "A": return reduce(mul, map(len, xmas))
    if name == "R": return 0

    result = 0
    for rule in workflows[name]:
        if isinstance(rule, str):
            result += total_combinations(workflows, xmas, rule)
        else:
            i = "xmas".index(rule[0])
            temp = xmas[i]
            if rule[1] == "<":
                # a < rule[2]
                xmas[i] = range(temp.start, rule[2])
                result += total_combinations(workflows, xmas[:], rule[3])
                xmas[i] = range(rule[2], temp.stop)

            elif rule[1] == ">":
                # a > rule[2]
                xmas[i] = range(rule[2] + 1, temp.stop)
                result += total_combinations(workflows, xmas[:], rule[3])
                xmas[i] = range(temp.start, rule[2] + 1)

    return result


def main():
    part1 = 0
    part2 = 0

    workflows = read_workflows()
    for line in sys.stdin.read().splitlines():
        part = eval(f"dict({line[1:-1]})")
        if is_accepted(workflows, part):
            part1 += sum(part.values())

    xmas = [range(1, 4001)] * 4
    part2 += total_combinations(workflows, xmas)
        

    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
