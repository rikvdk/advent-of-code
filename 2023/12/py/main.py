import sys
from functools import cache
from itertools import groupby, islice, product


def is_correct(damaged_record, record, nums):
    if record.count("#") != sum(nums):
        return False

    if not all(a == b for a, b in zip(damaged_record, record) if a != "?"):
        return False

    record_nums = []
    for k, g in groupby(record):
        if k == "#":
            record_nums.append(sum(1 for _ in g))

    if record_nums != nums:
        return False

    return True


@cache
def recursive(record, r, nums, n):
    if n >= len(nums):
        return "#" not in islice(record, r, len(record))

    if r >= len(record) or record[r] == "#":
        return 0

    r += 1
    num = nums[n]
    s = sum(x + i == 0 for i, x in enumerate(range(n + 1, len(nums))))
    answer = 0
    for i in range(r, len(record) - num - s + 1):
        if "#" not in islice(record, r, i) and "." not in islice(record, i,  i + num):
            answer += recursive(record, i + num, nums, n + 1)

    return answer

def main():
    part1 = 0
    part2 = 0

    for i, line in enumerate(sys.stdin):
        damaged_record, nums = line.split()
        nums = tuple(map(int, nums.split(",")))

        part1 += (recursive(tuple("?" + damaged_record), 0, nums, 0))
        part2 += recursive("?" + "?".join(damaged_record for i in range(5)), 0, nums * 5, 0)

        # damaged = nums.count("#")

        # for record in product(".#", repeat=len(damaged_record)):
        #     part1 += is_correct(damaged_record, record, nums)


    print(part1)
    print(part2)


if __name__ == "__main__":
    # import cProfile
    # cProfile.run("main()")

    main()
