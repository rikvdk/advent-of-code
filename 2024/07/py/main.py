import sys
from itertools import product
from operator import add, mul


def main():
    part1 = 0
    part2 = 0
    operators = [add, mul]
    operators2 = [add, mul, lambda a, b: int(str(a) + str(b))]

    for line in sys.stdin:
        left, right = line.split(":")
        value = int(left)
        numbers = list(map(int, right.split()))

        for i in range(2 ** (len(numbers) - 1)):
            expr = numbers[0]
            for number in numbers[1:]:
                expr = operators[i & 1](expr, number)
                i = i >> 1
            if expr == value:
                part1 += value
                break

        for t in product([0, 1, 2], repeat=len(numbers) - 1):
            expr = numbers[0]
            for i, number in zip(t, numbers[1:]):
                expr = operators2[i](expr, number)
            if expr == value:
                part2 += value
                break

    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
