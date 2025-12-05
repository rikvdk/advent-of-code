import sys


def has_correct_order(numbers, mapping):
    for i, number in enumerate(numbers):
        for j in range(i + 1, len(numbers)):
            if number in mapping[numbers[j]]:
                return False
    return True


def fix_order(numbers, mapping):
    done = False
    while not done:
        for i, number in enumerate(numbers):
            for j in range(i + 1, len(numbers)):
                if number in mapping[numbers[j]]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
                    break
            else:
                continue
            break
        else:
            done = True


def main():
    part1 = 0
    part2 = 0

    mapping = [set() for _ in range(100)]
    while line := next(sys.stdin).strip():
        left, right = map(int, line.split("|"))
        mapping[left].add(right)

    for line in sys.stdin:
        numbers = list(map(int, line.split(",")))

        if has_correct_order(numbers, mapping):
            part1 += numbers[len(numbers) // 2]
        else:
            fix_order(numbers, mapping)
            part2 += numbers[len(numbers) // 2]


    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
