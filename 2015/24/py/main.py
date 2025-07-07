import sys
from itertools import combinations
from math import prod


def solve(numbers, group_count):
    answer = float("inf")
    target = sum(numbers) // group_count

    for i in range(1, len(numbers)):
        for c in combinations(numbers, i):
            if sum(c) == target and prod(c) < answer:
                answer = prod(c)

        if answer != float("inf"):
            return answer


def main():
    numbers = sorted(int(line) for line in sys.stdin)

    print(solve(numbers, 3))
    print(solve(numbers, 4))


if __name__ == "__main__":
    main()
