import sys
from collections import defaultdict
from itertools import permutations


def read_happines_mapping():
    happiness_map = defaultdict(dict)

    for line in sys.stdin:
        person1, _, lose_gain, happiness, *_, person2 = line.rstrip(".\n").split()
        happiness_map[person1][person2] = (-1) ** (lose_gain == "lose") * int(happiness)

    return happiness_map


def add_mapping_for_me(happiness_map):
    for key in list(happiness_map.keys()):
        happiness_map["me"][key] = 0
        happiness_map[key]["me"] = 0


def solve(m):
    return max(
        sum(m[p[i - 1]][p[i]] + m[p[i]][p[i - 1]] for i in range(len(p)))
        for p in permutations(m.keys())
    )


def main():
    happiness_map = read_happines_mapping()
    print(solve(happiness_map))
    add_mapping_for_me(happiness_map)
    print(solve(happiness_map))


if __name__ == "__main__":
    main()
