import sys


def dfs(x, y, w, h, plots, visited):
    area = 1
    perim = 0
    val = plots[y][x]

    visited.add((x, y))

    if x > 0 and plots[y][x-1] == val:
        if (x-1, y) not in visited:
            area2, perim2 = dfs(x-1, y, w, h, plots, visited)
            area += area2
            perim += perim2
    else:
        perim += 1

    if x < w-1 and plots[y][x+1] == val:
        if (x+1, y) not in visited:
            area2, perim2 = dfs(x+1, y, w, h, plots, visited)
            area += area2
            perim += perim2
    else:
        perim += 1

    if y > 0 and plots[y-1][x] == val:
        if (x, y-1) not in visited:
            area2, perim2 = dfs(x, y-1, w, h, plots, visited)
            area += area2
            perim += perim2
    else:
        perim += 1

    if y < h-1 and plots[y+1][x] == val:
        if (x, y+1) not in visited:
            area2, perim2 = dfs(x, y+1, w, h, plots, visited)
            area += area2
            perim += perim2
    else:
        perim += 1

    return (area, perim)


def main():
    part1 = 0
    part2 = 0

    visited = set()
    plots = [line.rstrip() for line in sys.stdin]
    h, w = len(plots), len(plots[0])
    for y, row in enumerate(plots):
        for x, cell in enumerate(row):
            if (x, y) not in visited:
                a, p = dfs(x, y, w, h, plots, visited)
                # print(plots[y][x], a, p, a*p)
                part1 += a*p

    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
