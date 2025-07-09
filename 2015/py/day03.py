import sys
from collections import defaultdict


def main():
    part1 = {(0, 0)}
    part2 = {(0, 0)}

    x = 0
    y = 0
    positions = [[0, 0], [0, 0]]

    for i, move in enumerate(next(sys.stdin).strip()):
        position = positions[i % 2]

        match move:
            case "^":
                y += 1
                position[1] += 1
            case ">":
                x += 1
                position[0] += 1
            case "v":
                y -= 1
                position[1] -= 1
            case "<":
                x -= 1
                position[0] -= 1

        part1.add((x, y))
        part2.add(tuple(position))

    print(len(part1))
    print(len(part2))


if __name__ == "__main__":
    main()
