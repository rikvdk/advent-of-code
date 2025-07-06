import sys


def count_neighbours(board, w, h, x, y):
    left = x > 0
    right = x < w - 1
    top = y > 0
    bottom = y < h - 1

    return (
        (top and left and board[y - 1][x - 1])
        + (top and board[y - 1][x])
        + (top and right and board[y - 1][x + 1])
        + (left and board[y][x - 1])
        + (right and board[y][x + 1])
        + (bottom and left and board[y + 1][x - 1])
        + (bottom and board[y + 1][x])
        + (bottom and right and board[y + 1][x + 1])
    )


def solve(board, stuck_lights):
    h = len(board)
    w = len(board[0])

    if stuck_lights:
        board[0][0] = True
        board[0][w - 1] = True
        board[h - 1][0] = True
        board[h - 1][w - 1] = True

    for i in range(100):
        next_board = [[False] * w for _ in range(h)]

        for y, row in enumerate(board):
            for x, cell in enumerate(row):
                count = count_neighbours(board, w, h, x, y)
                next_board[y][x] = count == 3 or board[y][x] and count == 2

        if stuck_lights:
            next_board[0][0] = True
            next_board[0][w - 1] = True
            next_board[h - 1][0] = True
            next_board[h - 1][w - 1] = True

        board, next_board = next_board, board

    return sum(cell for row in board for cell in row)


def main():
    board = [list(c == "#" for c in line.strip()) for line in sys.stdin]
    print(solve(board, False))
    print(solve(board, True))


if __name__ == "__main__":
    main()
