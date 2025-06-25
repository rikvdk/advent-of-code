import re
import sys


def solve(ingredients):
    part1 = 0
    part2 = 0

    for i in range(0, 101):
        for j in range(0, 101 - i):
            for k in range(0, 101 - i - j):
                m = 100 - i - j - k
                score, calories = calculate_score(ingredients, (i, j, k, m))
                part1 = max(part1, score)

                if calories == 500:
                    part2 = max(part2, score)

    return part1, part2


def calculate_score(ingredients_properties, teaspoons):
    sums = [0] * len(ingredients_properties[0])

    for properties, teaspoon in zip(ingredients_properties, teaspoons):
        for i, property in enumerate(properties):
            sums[i] += teaspoon * property

    score = 1
    for x in sums[:-1]:
        if x < 0:
            return 0, 0

        score *= x
    return score, sums[-1]


def main():
    ingredients = [list(map(int, re.findall(r"-?\d+", line))) for line in sys.stdin]

    print(*solve(ingredients), sep="\n")


if __name__ == "__main__":
    main()
