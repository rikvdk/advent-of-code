import sys


def main():
    part1 = 0
    part2 = 0

    for i, c in enumerate(next(sys.stdin), 1):
        if c == "(":
            part1 += 1
        else:
            part1 -= 1

        if part2 == 0 and part1 == -1:
            part2 = i

    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
