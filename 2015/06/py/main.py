import sys
import numpy as np


def main():
    grid1 = np.zeros([1000, 1000], dtype=bool)
    grid2 = np.zeros([1000, 1000], dtype=int)

    for line in sys.stdin:
        parts = line.split(" ")
        if len(parts) == 5:
            parts.pop(0)

        sx, sy, ex, ey = map(int, f"{parts[1]},{parts[3]}".split(","))

        match parts[0]:
            case "on":
                grid1[sy : ey + 1, sx : ex + 1] = True
                grid2[sy : ey + 1, sx : ex + 1] += 1
            case "off":
                grid1[sy : ey + 1, sx : ex + 1] = False
                grid2[sy : ey + 1, sx : ex + 1][
                    grid2[sy : ey + 1, sx : ex + 1] > 0
                ] -= 1
            case "toggle":
                grid1[sy : ey + 1, sx : ex + 1] = ~grid1[sy : ey + 1, sx : ex + 1]
                grid2[sy : ey + 1, sx : ex + 1] += 2

    print(grid1.sum())
    print(grid2.sum())


if __name__ == "__main__":
    main()
