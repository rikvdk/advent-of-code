import sys
from collections import defaultdict


def main():
    part1 = 0
    part2 = 0
    positions = defaultdict(list)
    board = []

    for y, line in enumerate(sys.stdin):
        for x, cell in enumerate(line.strip()):
            if cell != ".":
                positions[cell].append((x, y))
        board.append(list(line.strip()))

    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell != ".":
                part2 += 1
                board[y][x] = "#"

    w = len(board[0])
    h = len(board)

    # print(*(''.join(row) for row in board), sep="\n")

    for key, locs in positions.items():
        for i, (x1, y1) in enumerate(locs):
            for (x2, y2) in locs[i+1:]:
                dx = x1 - x2
                dy = y1 - y2

                x3 = x2 - dx
                y3 = y2 - dy

                if 0 <= x3 < w and 0 <= y3 < h and board[y3][x3] != "#":
                    # board[y3][x3] = "#"
                    part1 += 1
                while True:
                    if not (0 <= x3 < w and 0 <= y3 < h):
                        break
                    if board[y3][x3] != "#":
                        board[y3][x3] = "#"
                        part2 += 1
                    x3 = x3 - dx
                    y3 = y3 - dy

                x4 = x1 + dx
                y4 = y1 + dy
                if 0 <= x4 < w and 0 <= y4 < h and board[y4][x4] != "#":
                    # board[y4][x4] = "#"
                    part1 += 1
                while True:
                    if not (0 <= x4 < w and 0 <= y4 < h):
                        break
                    if board[y4][x4] != "#":
                        board[y4][x4] = "#"
                        part2 += 1
                    x4 = x4 + dx
                    y4 = y4 + dy

    print(part1)
    print(part2)

    # print(*(''.join(row) for row in board), sep="\n")


if __name__ == "__main__":
    main()
