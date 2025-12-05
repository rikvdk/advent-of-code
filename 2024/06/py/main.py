import sys
from itertools import cycle


def solve(board, x, y):
    count = 1
    h, w = len(board), len(board[0])
    print(w, h)
    g = cycle([(0, -1), (1, 0), (0, 1), (-1, 0)])
    d = next(g)

    while True:
        nx = x + d[0]
        ny = y + d[1]
        if not (0 <= nx < w and 0 <= ny < h):
            return count

        if board[ny][nx] == "#":
            d = next(g)
            continue

        if board[ny][nx] == ".":
            count += 1

        board[ny][nx] = "X"
        x = nx
        y = ny


def is_stuck(board, x, y):
    seen = set()
    h, w = len(board), len(board[0])
    g = cycle([(0, -1), (1, 0), (0, 1), (-1, 0)])
    d = next(g)

    while True:
        nx = x + d[0]
        ny = y + d[1]
        if not (0 <= nx < w and 0 <= ny < h):
            return 0

        if board[ny][nx] == "#":
            if (nx, ny, d) in seen:
                return 1

            seen.add((nx, ny, d))
            d = next(g)
            continue

        x = nx
        y = ny


def main():
    part2 = 0
    board = [list(line.strip()) for line in sys.stdin]
    gx, gy = next((x, y) for y, row in enumerate(board) for x, cell in enumerate(row) if cell == "^")

    print(solve(board, gx, gy))

    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell == "X":
                row[x] = "#"
                if is_stuck(board, gx, gy):
                    part2 += 1
                row[x] = "X"

    print(part2)


if __name__ == "__main__":
    main()
