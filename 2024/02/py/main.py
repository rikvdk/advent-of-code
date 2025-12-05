import sys


def is_safe(numbers):
    increasing = True
    decreasing = True
    difference = True

    for a, b in zip(numbers, numbers[1:]):
        increasing &= a > b
        decreasing &= a < b
        difference &= 1 <= abs(a-b) <= 3

    return (increasing or decreasing) and difference


def main():
    part1 = 0
    part2 = 0

    for line in sys.stdin:
        numbers = list(map(int, line.split()))

        if is_safe(numbers):
            part1 += 1

        for i in range(0, len(numbers)):
            numbs = numbers[:]
            del numbs[i]
            if is_safe(numbs):
                part2 += 1
                break

    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
