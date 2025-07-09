import operator
import re
import sys
from collections import defaultdict


def main():
    part1 = 0
    part2 = 0

    properties = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }
    ops = defaultdict(
        lambda: operator.eq,
        {
            "cats": operator.gt,
            "trees": operator.gt,
            "pomeranians": operator.lt,
            "goldfish": operator.lt,
        },
    )
    pattern = re.compile(r"(\w+): (\d+)")

    for i, line in enumerate(sys.stdin, 1):
        matches = pattern.findall(line)

        if all(properties[key] == int(value) for key, value in matches):
            part1 = i

        if all(ops[key](int(value), properties[key]) for key, value in matches):
            part2 = i

    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
