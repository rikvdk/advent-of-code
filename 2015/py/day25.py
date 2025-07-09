import re
import sys


STARTING_CODE = 20151125
FACTOR = 252533
QUOTIENT = 33554393


def solve(row, column):
    n = row + column - 2
    index = (n * (n + 1)) // 2 + column

    code = STARTING_CODE
    for i in range(index - 1):
        code = (code * FACTOR) % QUOTIENT
    return code


def main():
    line = sys.stdin.readline()
    row = int(re.search(r"row (\d+)", line).group(1))
    column = int(re.search(r"column (\d+)", line).group(1))

    print(solve(row, column))


if __name__ == "__main__":
    main()
