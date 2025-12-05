import re
import sys


def main():
    part1 = 0
    part2 = 0
    enabled = True

    pattern = re.compile(r"(don't\(\)|do\(\)|mul\((\d+),(\d+)\))")
    for line in sys.stdin:
        matches = pattern.findall(line)
        for match in matches:
            if match[0] == "do()":
                enabled = True
            elif match[0] == "don't()":
                enabled = False
            elif enabled:
                part2 += int(match[1]) * int(match[2])

    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
