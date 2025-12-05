import sys


def dfs(x, y, w, h, topo_map, visited):
    curr = topo_map[y][x]
    if curr == 9:
        visited.add((x, y))
        return 1

    val = 0
    if x > 0 and topo_map[y][x-1] == curr + 1:
        val += dfs(x-1, y, w, h, topo_map, visited)
    if x < w-1 and topo_map[y][x+1] == curr + 1:
        val += dfs(x+1, y, w, h, topo_map, visited)
    if y > 0 and topo_map[y-1][x] == curr + 1:
        val += dfs(x, y-1, w, h, topo_map, visited)
    if y < h-1 and topo_map[y+1][x] == curr + 1:
        val += dfs(x, y+1, w, h, topo_map, visited)
    return val


def main():
    part1 = 0
    part2 = 0

    topo_map = [list(map(int, line.strip())) for line in sys.stdin]
    h = len(topo_map)
    w = len(topo_map[0])

    for y, row in enumerate(topo_map):
        for x, cell in enumerate(row):
            if cell == 0:
                visited = set()
                part2 += dfs(x, y, w, h, topo_map, visited)
                part1 += len(visited)

    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
