import sys
from collections import deque


UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4


def solve(grid, y, x, d):
    h, w = len(grid), len(grid[0])

    q = deque([(y, x, d)])
    visited = {(y, x, d)}
    seen = {(y, x)}
    aa = [["." for _ in range(w)] for _ in range(h)]
    aa[y][x] = "#"

    while q:
        y, x, d = q.popleft()
        neighbors = []
        # for row in aa:
        #     print("".join(row))
        # print()

        match grid[y][x]:
            case ".":
                match d:
                    case 1: neighbors.append((y - 1, x, d))
                    case 2: neighbors.append((y, x + 1, d))
                    case 3: neighbors.append((y + 1, x, d))
                    case 4: neighbors.append((y, x - 1, d))
            case "|":
                match d:
                    case 1: neighbors.append((y - 1, x, UP))
                    case 2:
                        neighbors.append((y - 1, x, UP))
                        neighbors.append((y + 1, x, DOWN))
                    case 3: neighbors.append((y + 1, x, DOWN))
                    case 4:
                        neighbors.append((y - 1, x, UP))
                        neighbors.append((y + 1, x, DOWN))
            case "-":
                match d:
                    case 1: 
                        neighbors.append((y, x - 1, LEFT))
                        neighbors.append((y, x + 1, RIGHT))
                    case 2: neighbors.append((y, x + 1, d))
                    case 3:
                        neighbors.append((y, x - 1, LEFT))
                        neighbors.append((y, x + 1, RIGHT))
                    case 4: neighbors.append((y, x - 1, d))
            case "\\":
                match d:
                    case 1: neighbors.append((y, x - 1, LEFT))
                    case 2: neighbors.append((y + 1, x, DOWN))
                    case 3: neighbors.append((y, x + 1, RIGHT))
                    case 4: neighbors.append((y - 1, x, UP))
            case "/":
                match d:
                    case 1: neighbors.append((y, x + 1, RIGHT))
                    case 2: neighbors.append((y - 1, x, UP))
                    case 3: neighbors.append((y, x - 1, LEFT))
                    case 4: neighbors.append((y + 1, x, DOWN))

        for n in neighbors:
            yy, xx, dd = n
            if (yy, xx, dd) not in visited and 0 <= yy < h and 0 <= xx < w:
                seen.add((yy, xx))
                aa[yy][xx] = "#"
                visited.add(n)
                q.append(n)

    # for row in aa:
    #     print("".join(row))
    return len(seen)


def main():
    part1 = 0
    part2 = 0

    grid = [line.strip() for line in sys.stdin]
    h, w = len(grid), len(grid[0])

    print(solve(grid, 0, 0, RIGHT))
    # print(solve(grid, 0, 3, DOWN))

    for y in range(h):
        part2 = max(part2, solve(grid, y, 0, RIGHT), solve(grid, y, w - 1, LEFT))

    for x in range(w):
        part2 = max(part2, solve(grid, 0, x, DOWN), solve(grid, h - 1, x, UP))

    print(part2)


if __name__ == "__main__":
    main()
