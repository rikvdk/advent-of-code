import re
import sys


def main():
    part1 = 0
    part2 = 0

    for line in sys.stdin.read().splitlines():
        part1 += len(line) - len(eval(line))
        part2 += len(re.escape(line)) + line.count('"') + 2 - len(line)

    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
