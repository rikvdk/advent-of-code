import sys


def main():
    part1 = 0
    part2 = 0

    for line in sys.stdin:
        l, w, h = sorted(map(int, line.split("x")))

        part1 += 3 * l * w + 2 * w * h + 2 * l * h
        part2 += 2 * l + 2 * w + l * w * h

    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
