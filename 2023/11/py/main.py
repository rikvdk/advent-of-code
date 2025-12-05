import sys
from bisect import bisect_left
from itertools import combinations
from operator import sub


def find_nodes(grid):
    return [
        [y, x]
        for x in range(len(grid[0]))
        for y in range(len(grid))
        if grid[y][x] == "#"
    ]


def expand(grid, n):
    nodes = find_nodes(grid)
    row_inserts = [i for i, row in enumerate(grid) if "#" not in row]
    column_inserts = [
        i for i in range(len(grid[0])) if all(row[i] != "#" for row in grid)
    ]

    for node in nodes:
        node[0] += n * bisect_left(row_inserts, node[0])
        node[1] += n * bisect_left(column_inserts, node[1])

    return list(map(tuple, nodes))


def main():
    grid = [list(line.rstrip()) for line in sys.stdin]

    print(sum(sum(map(abs, map(sub, a, b))) for a, b in combinations(expand(grid, 1), 2)))
    print(sum(sum(map(abs, map(sub, a, b))) for a, b in combinations(expand(grid, 999_999), 2)))


if __name__ == "__main__":
    main()
