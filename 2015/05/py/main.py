import sys


def main():
    part1 = 0
    part2 = 0

    rules1 = [
        lambda s: sum(s.count(c) for c in "aeiou") >= 3,
        lambda s: any(a == b for a, b in zip(s, s[1:])),
        lambda s: all(t not in s for t in ["ab", "cd", "pq", "xy"]),
    ]
    rules2 = [
        lambda s: any(s[i : i + 2] in s[i + 2 :] for i in range(len(s) - 2)),
        lambda s: any(s[i] == s[i + 2] for i in range(len(s) - 2)),
    ]

    for line in sys.stdin:
        part1 += all(rule(line) for rule in rules1)
        part2 += all(rule(line) for rule in rules2)

    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
