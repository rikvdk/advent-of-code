import sys


def h(s):
    x = 0

    for c in s:
        x += ord(c)
        x *= 17
        x %= 256
    return x


def main():
    part1 = 0
    part2 = 0

    lenses = [[] for _ in range(256)]
    line = next(sys.stdin).strip()

    for part in line.split(","):
        part1 += h(part)
        
        if "=" in part:
            label, focal = part.split("=")
            i = h(label)
            focal = int(focal)

            for lens in lenses[i]:
                if lens[0] == label:
                    lens[1] = focal
                    break
            else:
                lenses[i].append([label, focal])
        else:
            label = part[:-1]
            i = h(label)

            lenses[i] = [lens for lens in lenses[i] if lens[0] != label]



#         print(f"After {part}:")
#         for i, lens in enumerate(lenses[:5]):
#             if lens:
#                 print(f"Box {i}: {lens}")
#         print()
    
    for i, box in enumerate(lenses, 1):
        for j, lens in enumerate(box, 1):
            part2 += i * j * lens[1]

    
    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
