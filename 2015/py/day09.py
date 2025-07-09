import sys
from collections import defaultdict
from itertools import permutations


def main():
    part1 = sys.maxsize
    part2 = 0

    graph = defaultdict(dict)

    for line in sys.stdin:
        start, end, distance = line.split(" ")[::2]
        graph[start][end] = graph[end][start] = int(distance)

    for route in permutations(graph.keys()):
        distance = sum(graph[a][b] for a, b in zip(route, route[1:]))

        part1 = min(part1, distance)
        part2 = max(part2, distance)

    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
