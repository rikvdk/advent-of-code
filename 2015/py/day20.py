import sys


def solve1(value):
    max_value = 1_000_000
    arr = [0] * max_value

    for i in range(1, max_value):
        for j in range(i, max_value, i):
            arr[j] += 10 * i

        if arr[i] >= value:
            return i


def solve2(value):
    max_value = 5_000_000
    arr = [0] * (10 * max_value)

    for i in range(1, max_value):
        for j in range(i, i * 51, i):
            arr[j] += 11 * i

        if arr[i] >= value:
            return i


def main():
    value = int(next(sys.stdin))

    print(solve1(value))
    print(solve2(value))


if __name__ == "__main__":
    main()
