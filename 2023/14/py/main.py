import sys
from itertools import islice


def tilt_north(grid, h, w):
    for i, row in islice(enumerate(grid), 1, None):
        for j, c in enumerate(row):
            if c != "O":
                continue

            for k in reversed(range(i)):
                if grid[k][j] != ".":
                    break

                grid[k][j] = "O"
                grid[k + 1][j] = "."


def tilt_west(grid, h, w):
    for i, row in enumerate(grid):
        for j in range(1, w):
            c = row[j]
            if c != "O":
                continue

            for k in reversed(range(j)):
                if row[k] != ".":
                    break

                row[k] = "O"
                row[k + 1] = "."


def tilt_south(grid, h, w):
    for i in range(h - 2, -1, -1):
        for j, c in enumerate(grid[i]):
            if c != "O":
                continue

            for k in range(i + 1, h):
                if grid[k][j] != ".":
                    break

                grid[k - 1][j] = "."
                grid[k][j] = "O"


def tilt_east(grid, h, w):
    for i, row in enumerate(grid):
        for j in reversed(range(w - 1)):
            c = row[j]

            if c != "O":
                continue

            print(f"{row=} {c=} {i=} {j=}")
            # print(range(j, w - 1))
            for k in reversed(range(j, w - 1)):
                print(k, row[k + 1])
                if row[k + 1] != ".":
                    break

                row[k] = "."
                row[k + 1] = "O"


def cycle(grid, n, h, w):
    tilt_north(grid, h, w)
    tilt_west(grid, h, w)
    tilt_south(grid, h, w)
    tilt_east(grid, h, w)


def print_grid(grid):
    print(*("".join(row) for row in grid), sep="\n")
    print()


def total_load_north(grid):
    return sum(i * row.count("O") for i, row in enumerate(reversed(grid), 1))


def main():
    part2 = 0

    grid = [list(line.rstrip()) for line in sys.stdin]
    h, w = len(grid[0]), len(grid)

    print("Start")
    print_grid(grid)

    print("East")
    tilt_east(grid, h, w)
    print_grid(grid)


if __name__ == "__main__":
    main()
