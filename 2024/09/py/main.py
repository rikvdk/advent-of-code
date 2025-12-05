import sys


def main():
    part1 = 0
    part2 = 0

    disk_map = next(sys.stdin).strip()

    arr = []
    for i, c in enumerate(disk_map):
        v = int(c)

        if i % 2 == 0:
            arr += [i // 2] * v
        else:
            arr += [-1] * v

    # i = 0
    # j = len(arr) - 1
    # while i <= j:
    #     if arr[i] != -1:
    #         print(i, i * arr[i])
    #         part1 += i * arr[i]
    #         i += 1
    #     elif arr[j] != -1:
    #         arr[i] = arr[j]
    #         arr[j] = -2
    #         print(i, i * arr[i])
    #         part1 += i * arr[i]
    #         j -= 1
    #         i += 1
    #     else:
    #         j -= 1

    i = len(arr) - 1
    while i >= 0:
        # print(arr)
        # find next thing from the right
        while arr[i] == -1:
            i -= 1

        length = 1
        while arr[i] == arr[i-1]:
            length += 1
            i -= 1

        # print(arr[i], length)
        j = 0
        while j < len(arr):
            if arr[j] != -1:
                j += 1
                continue

            l2 = 1
            while arr[j] == -1 and j < len(arr) - 1:
                l2 += 1
                j += 1
                # print(j)

            if j - length > i:
                break
            # print(j, l2, length)
            if l2 > length:
                for k in range(length):
                    # print(j, l2, k, i)
                    arr[j - l2 + k + 1] = arr[i + k]
                    arr[i + k] = -1
                break
            elif j == len(arr) - 1:
                break

        # for n in arr:
        #     if n == -1:
        #         print(".", end="")
        #     else:
        #         print(n, end="")
        # print()
        i -= 1

    for i in range(len(arr)):
        if arr[i] != -1:
            part2 += i * arr[i]
    # print(part1)
    print(part2)


if __name__ == "__main__":
    main()
