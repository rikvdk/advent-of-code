import sys
from collections import deque
from itertools import count


def print_grid(grid):
    for row in grid:
        for val in row:
            match val:
                case "|": print("│", end="")
                case "-": print("─", end="")
                case "L": print("└", end="")
                case "J": print("┘", end="")
                case "7": print("┐", end="")
                case "F": print("┌", end="")
                case ".": print(".", end="")
                case "I": print("I", end="")
                case "O": print("O", end="")
                case _: print(" ", end="")
        print()


def find_S(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "S":
                break
        else:
            continue
        break

    if (y, x) in con(grid, y - 1, x) and (y, x) in con(grid, y + 1, x):
        grid[y][x] = "|"
    elif (y, x) in con(grid, y, x - 1) and (y, x) in con(grid, y, x - 1):
        grid[y][x] = "-"
    elif (y, x) in con(grid, y - 1, x) and (y, x) in con(grid, y, x + 1):
        grid[y][x] = "L"
    elif (y, x) in con(grid, y, x - 1) and (y, x) in con(grid, y - 1, x):
        grid[y][x] = "J"
    elif (y, x) in con(grid, y, x - 1) and (y, x) in con(grid, y + 1, x):
        grid[y][x] = "7"
    elif (y, x) in con(grid, y, x + 1) and (y, x) in con(grid, y + 1, x):
        grid[y][x] = "F"
    else:
        print("foo")

    return y, x


def con(grid, y, x):
    if not (0 <= y < len(grid) and 0 <= x < len(grid[0])):
        return ()

    match grid[y][x]:
        case "|": return (y - 1, x), (y + 1, x)
        case "-": return (y, x - 1), (y, x + 1)
        case "L": return (y - 1, x), (y, x + 1)
        case "J": return (y - 1, x), (y, x - 1)
        case "7": return (y, x - 1), (y + 1, x)
        case "F": return (y, x + 1), (y + 1, x)

    return ()


def walk(grid, sy, sx):
    py, px = sy, sx
    y, x = con(grid, sy, sx)[0]

    for i in count(1):
        if (y, x) == (sy, sx):
            return i

        moves = con(grid, y, x)
        if moves[0] != (py, px):
            move = moves[0]
        else:
            move = moves[1]

        py, px = y, x
        y, x = move


def neighbors(grid, y, x):
    if y > 0 and grid[y - 1][x] == ".": yield y - 1, x
    if x > 0 and grid[y][x - 1] == ".": yield y, x - 1
    if y + 1 < len(grid) and grid[y + 1][x] == ".": yield y + 1, x
    if x + 1 < len(grid[0]) and grid[y][x + 1] == ".": yield y, x + 1


def flood(grid):
    visited = set([0, 0])
    q = deque([(0, 0)])
    while q:
        y, x = q.popleft()
        grid[y][x] = "O"

        for ny, nx in neighbors(grid, y, x):
            if (ny, nx) not in visited:
                visited.add((ny, nx))
                q.append((ny, nx))

def main():
    grid = [["."] + list(line.rstrip()) + ["."] for line in sys.stdin]
    grid.insert(0, ["."] * len(grid[0]))
    grid.append(["."] * len(grid[0]))

    sy, sx = find_S(grid)
    print(walk(grid, sy, sx) // 2)

    # print_grid(grid)
    print()
    flood(grid)
    print_grid(grid)

    

    # print(*("".join(row) for row in grid), sep="\n")


if __name__ == "__main__":
    main()
