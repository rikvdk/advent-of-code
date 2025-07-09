import sys
from collections import defaultdict
from itertools import count


def solve1(medicine, forward_map):
    new_molecules = set()

    for origin, targets in forward_map.items():
        start = 0
        while (index := medicine.find(origin, start)) != -1:
            for target in targets:
                new_medicine = (
                    medicine[:index] + target + medicine[index + len(origin) :]
                )
                new_molecules.add(new_medicine)
            start = start + 1

    return len(new_molecules)


def solve2(medicine, reverse_list, count=0):
    if medicine == "e":
        return count

    for before, after in reverse_list:
        if (index := medicine.find(after)) != -1:
            new_medicine = medicine[:index] + before + medicine[index + len(after) :]

            if answer := solve2(new_medicine, reverse_list, count + 1):
                return answer


def main():
    forward_map = defaultdict(list)
    reverse_list = []

    while line := sys.stdin.readline().strip():
        before, after = line.split(" => ")
        forward_map[before].append(after)
        reverse_list.append((before, after))

    reverse_list.sort(key=lambda t: len(t[0]) - len(t[1]))
    medicine = next(sys.stdin).strip()

    print(solve1(medicine, forward_map))
    print(solve2(medicine, reverse_list))


if __name__ == "__main__":
    main()
