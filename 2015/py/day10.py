import sys
from itertools import groupby


def main():
    prev = next(sys.stdin).strip()

    for i in range(50):
        if i == 40:
            print(len(prev))

        curr = "".join(f"{sum(1 for _ in g)}{k}" for k, g in groupby(prev))
        prev = curr

    print(len(curr))


if __name__ == "__main__":
    main()
