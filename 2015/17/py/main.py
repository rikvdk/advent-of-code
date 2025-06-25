import sys


def solve(containers, remaining, ways, n):
    if remaining == 0:
        ways[n] += 1
        return

    if remaining < 0 or not containers:
        return

    solve(containers[1:], remaining - containers[0], ways, n + 1)
    solve(containers[1:], remaining, ways, n)


def main():
    containers = tuple(map(int, sys.stdin))
    ways = [0] * (len(containers) + 1)

    solve(containers, 150, ways, 0)
    print(sum(ways))
    print(next(way for way in ways if way != 0))


if __name__ == "__main__":
    main()
