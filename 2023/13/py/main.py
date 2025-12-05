import sys


def solve1(x, grid, val):
    rows = [sum((c == "#") << i for i, c in enumerate(row)) for row in grid]
    cols = [sum((row[i] == "#") << j for j, row in enumerate(grid)) for i in range(len(grid[0]))]

    for i in range(1, len(rows)):
        l = min(i, len(rows) - i)
        if sum((a ^ b).bit_count() for a, b in zip(rows[i - l : i], reversed(rows[i : i + l]))) == val:
            return i * 100

    for i in range(1, len(cols)):
        l = min(i, len(cols) - i)
        if sum((a ^ b).bit_count() for a, b in zip(cols[i - l : i], reversed(cols[i : i + l]))) == val:
            return i

    return 0


def main():
    part1 = 0
    part2 = 0

    grid = []
    for i, line in enumerate(sys.stdin.read().splitlines()):
        if not line:
            part1 += solve1(i, grid, 0)
            part2 += solve1(i, grid, 1)
            grid = []
        else:
            grid.append(line)
    part1 += solve1(-1, grid, 0)
    part2 += solve1(-1, grid, 1)

    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
