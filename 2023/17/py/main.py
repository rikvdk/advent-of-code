import sys
from collections import defaultdict, namedtuple
from heapq import heappop, heappush


UP = 1
RIGHT = 10
DOWN = 100
LEFT = 1000

Item = namedtuple("Item", ["priority", "y", "x", "d"])


def neighbors(grid, y, x, d):
    h, w = len(grid), len(grid[-1])

    m = max(d)
    i = d.index(m)

    # print(y, x, "|",  m, i, "|", d)

    # up
    # if not d[2] y > 0: yield y - 1, x, (d[0] + 1, 0, 0, 0)
    if (m == 0 or m >= 4 or i == 0) and not d[2] and d[0] != 11 and y > 0: yield y - 1, x, (d[0] + 1, 0, 0, 0)

    # left
    # if not d[3] and x > 0: yield y, x - 1, (0, d[1] + 1, 0, 0)
    if (m == 0 or m >= 4 or i == 1) and not d[3] and d[1] != 11 and x > 0: yield y, x - 1, (0, d[1] + 1, 0, 0)

    # down
    # if not d[0] and y < h - 1: yield y + 1, x, (0, 0, d[2] + 1, 0)
    if (m == 0 or m >= 4 or i == 2) and not d[0] and d[2] != 11 and y < h - 1: yield y + 1, x, (0, 0, d[2] + 1, 0)

    # right
    if (m == 0 or m >= 4 or i == 3) and not d[1] and d[3] != 11 and x < w - 1: yield y, x + 1, (0, 0, 0, d[3] + 1)


def a_start(sy, sx, gy, gx, grid):
    open_set = [Item(0, 0, 0, (0, 0, 0, 0))]
    came_from = {(0, 0, (0, 0, 0, 0)): (0, 0, (0, 0, 0, 0))}
    cost_so_far = defaultdict(lambda: sys.maxsize)
    cost_so_far[(sy, sx, (0, 0, 0, 0))] = 0

    while open_set:
        item = heappop(open_set)

        if (item.y, item.x) == (gy, gx):
            if max(item.d) < 4: continue

            # print(open_set)
            # quit()
            grid[0][0] = "#"

            _, y, x, d = item
            dd = d
            while y != sy or x != sx and (y, x, d) in came_from:
                # print(y, x, d)
                grid[y][x] = "#"
                y, x, d = came_from[(y, x, d)]

            # print(cost_so_far)
            return cost_so_far[(gy, gx, dd)]

        # py, px = came_from[came_from[came_from[(item.y, item.x)]]]
        for ny, nx, d in neighbors(grid, item.y, item.x, item.d):
            # print(d)
            if 11 in d: continue
            # if abs(ny - py) == 4 or abs(nx - px) == 4:
                # continue

            new_cost = cost_so_far[(item.y, item.x, item.d)] + grid[ny][nx]
            if new_cost < cost_so_far[(ny, nx, d)]:
                cost_so_far[(ny, nx, d)] = new_cost
                priority = new_cost + abs(gy - ny) + abs(gx - nx)
                heappush(open_set, Item(priority, ny, nx, d))
                came_from[(ny, nx, d)] = (item.y, item.x, item.d)


def main():
    part1 = 0
    part2 = 0

    grid = [list(map(int, line.strip())) for line in sys.stdin]
    h, w = len(grid), len(grid[0])

    print(a_start(0, 0, h - 1, w - 1, grid))
    print()
    for row in grid:
        print("".join(str(c) for c in row))

    # print(part1)
    # print(part2)


if __name__ == "__main__":
    main()
