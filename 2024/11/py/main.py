import sys
from functools import lru_cache

@lru_cache(maxsize=None)
def blink(number, n):
    if n == 0:
        return 1

    if number == 0:
        return blink(1, n - 1)

    s = str(number)
    l = len(s)
    if l % 2 == 0:
        return blink(int(s[:l//2]), n - 1) + blink(int(s[l//2:]), n - 1)
    else:
        return blink(number * 2024, n - 1)


def main():
    part1 = 0
    part2 = 0

    for number in map(int, next(sys.stdin).split()):
        x = blink(number, 75)
        part1 += x

    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
