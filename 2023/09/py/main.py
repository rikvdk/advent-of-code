import sys


def main():
    part1 = 0
    part2 = 0

    for line in sys.stdin:
        nums = [list(map(int, line.split()))]

        while any(num != 0 for num in nums[-1]):
            # nums.append([nums[-1][i - 1] - nums[-1][i] for i in range(1, len(nums[-1]))])
            nums.append([nums[-1][i] - nums[-1][i - 1] for i in range(1, len(nums[-1]))])
        # print(*nums, sep="\n")
        # print(nums[0][0])
        last = 0
        for x in reversed(nums):
            last = x[0] - last
        part2 += last




    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
