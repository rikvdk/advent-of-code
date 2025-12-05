import sys


def main():
    part1 = 0
    part2 = 0

    m = ["R", "D", "L", "U"]

    py, px = 0, 0
    ppy, ppx = 0, 0
    for i, line in enumerate(sys.stdin):
        d, c, _ = line.split()
        c = int(c)

        cy, cx = py, px
        match d:
            case "U": cy -= c
            case "R": cx += c
            case "D": cy += c
            case "L": cx -= c

        part1 += (px * cy - cx * py) / 2
        part1 += (abs(cy - py) + abs(cx - px)) / 2
        py, px = cy, cx

        cc = int(_[2:7], 16)
        dd = m[int(_[7], 16)]
        ccy, ccx = ppy, ppx
        match dd:
            case "U": ccy -= cc
            case "R": ccx += cc
            case "D": ccy += cc
            case "L": ccx -= cc

        part2 += (ppx * ccy - ccx * ppy) / 2
        part2 += (abs(ccy - ppy) + abs(ccx - ppx)) / 2
        ppy, ppx = ccy, ccx

    print(int(part1) + 1)
    print(int(part2) + 1)


if __name__ == "__main__":
    main()
