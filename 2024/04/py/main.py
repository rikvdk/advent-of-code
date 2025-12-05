import sys


def count_xmas(board):
    count = 0
    h, w = len(board), len(board[0])

    for y in range(h):
        for x in range(w):
            count += x >= 3 and "XMAS" == board[y][x] + board[y][x-1] + board[y][x-2] + board[y][x-3]
            count += y >= 3 and x >= 3 and "XMAS" == board[y][x] + board[y-1][x-1] + board[y-2][x-2] + board[y-3][x-3]
            count += y >= 3 and "XMAS" == board[y][x] + board[y-1][x] + board[y-2][x] + board[y-3][x]

            count += y >= 3 and x <= w-4 and "XMAS" == board[y][x] + board[y-1][x+1] + board[y-2][x+2] + board[y-3][x+3]
            count += x <= w-4 and "XMAS" == board[y][x] + board[y][x+1] + board[y][x+2] + board[y][x+3]

            count += y <= h-4 and "XMAS" == board[y][x] + board[y+1][x] + board[y+2][x] + board[y+3][x]
            count += y <= h-4 and x <= w-4 and "XMAS" == board[y][x] + board[y+1][x+1] + board[y+2][x+2] + board[y+3][x+3]
            count += y <= h-4 and x >= 3 and "XMAS" == board[y][x] + board[y+1][x-1] + board[y+2][x-2] + board[y+3][x-3]

    return count


def count_x_mas(board):
    count = 0
    h, w = len(board), len(board[0])

    for y in range(1, h - 1):
        for x in range(1, w - 1):
            if board[y][x] != "A":
                continue

            if {"M", "S"} != {board[y-1][x-1], board[y+1][x+1]}:
                continue

            if {"M", "S"} != {board[y-1][x+1], board[y+1][x-1]}:
                continue

            count += 1

    return count


def main():

    board = [line.strip() for line in sys.stdin]
    print(count_xmas(board))
    print(count_x_mas(board))


if __name__ == "__main__":
    main()
