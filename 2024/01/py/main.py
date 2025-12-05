import sys


def main():
    rows = list(tuple(map(int, line.split())) for line in sys.stdin)
    left = sorted(a for a, _ in rows)
    right = sorted(b for _, b in rows)

    print(sum(abs(a - b) for a, b in zip(left, right)))
    print(sum(a * right.count(a) for a in left))


if __name__ == "__main__":
    main()
