import sys


def neighbors(grid, y, x):
    h, w = len(grid), len(grid[0])

    # y %= h
    # x %= w

    if grid[(y - 1) % h][x % w] == ".": yield y - 1, x
    if grid[y % h][(x - 1) % w] == ".": yield y, x - 1
    if grid[(y + 1) % h][x % w] == ".": yield y + 1, x
    if grid[y % h][(x + 1) % w] == ".": yield y, x + 1

    # if y > 0 and grid[y - 1][x] == ".": yield y - 1, x
    # if x > 0 and grid[y][x - 1] == ".": yield y, x - 1
    # if y < h - 1 and grid[y + 1][x] == ".": yield y + 1, x
    # if x < w - 1 and grid[y][x + 1] == ".": yield y, x + 1


def solve1(grid, sy, sx, n):
    prev = {(sy, sx)}
    for i in range(n):
        curr = set()

        for y, x in prev:
            for ny, nx in neighbors(grid, y, x):
                curr.add((ny, nx))

        prev = curr

    return len(prev)


def solve2(grid, sy, sx, n):
    h, w = len(grid), len(grid[0])
    prev = {(sy, sx)}

    for i in range(n):
        # if i in [6, 10, 50, 100, 500, 1000, 5000]:
        print(len(prev))

        min_y = min(p[0] for p in prev)
        min_x = min(p[1] for p in prev)
        max_y = max(p[0] for p in prev)
        max_x = max(p[1] for p in prev)

        for y in range(min_y - 1, max_y + 2):
            for x in range(min_x - 1, max_x + 2):
                if (y, x) in prev:
                    c = "O"
                else:
                    c = grid[y % h][x % w]
                print(c, end="")
            print()
        print()


        curr = set()

        for y, x in prev:
            for ny, nx in neighbors(grid, y, x):
                curr.add((ny, nx))

        prev = curr

    return len(prev)


def main():
    part1 = 0
    part2 = 0

    grid = sys.stdin.read().splitlines()
    sy, sx = next((y, row.index("S")) for y, row in enumerate(grid) if "S" in row)
    grid[sy] = grid[sy].replace("S", ".")

    # print(solve1(grid, sy, sx, 64))
    # print(solve2(grid, sy, sx,  100))

    grid2 = [
        list("###"),
        list("..."),
        list("..."),
    ]
    solve2(grid2, 1, 1, 10)


if __name__ == "__main__":
    main()
