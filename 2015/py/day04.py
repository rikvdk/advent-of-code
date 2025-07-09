import sys
from itertools import count
from hashlib import md5


def solve(key, prefix_length, start=1):
    prefix = "0" * prefix_length

    for i in count(start):
        guess = f"{key}{i}".encode("utf-8")
        if md5(guess).hexdigest().startswith(prefix):
            return i


def main():
    key = next(sys.stdin).strip()

    part1 = solve(key, 5)
    part2 = solve(key, 6, part1)

    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
