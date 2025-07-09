import re
import sys


def solve1(reindeers, time_limit):
    return max(
        calculate_distance(time_limit, *attributes)
        for reindeer, attributes in enumerate(reindeers)
    )


def solve2(reindeers, time_limit):
    points = [0] * len(reindeers)

    for current_time in range(1, time_limit + 1):
        distances = [
            calculate_distance(current_time, *attributes)
            for reindeer, attributes in enumerate(reindeers)
        ]
        max_distance = max(distances)

        for i, distance in enumerate(distances):
            if distance == max_distance:
                points[i] += 1

    return max(points)


def calculate_distance(time_limit, speed, flying_time, rest_time):
    q, r = divmod(time_limit, flying_time + rest_time)
    return speed * (flying_time * q + min(flying_time, r))


def main():
    pattern = re.compile(r"\d+")
    reindeers = [list(map(int, re.findall(pattern, line))) for line in sys.stdin]

    print(solve1(reindeers, 2503))
    print(solve2(reindeers, 2503))


if __name__ == "__main__":
    main()
