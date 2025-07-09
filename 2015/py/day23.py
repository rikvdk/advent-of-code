import sys


def solve(program, a):
    registers = [a, 0]
    i = 0

    while i >= 0 and i < len(program):
        line = program[i]
        instruction, rest = line.split(" ", 1)
        register_index = rest[0] == "b"

        match instruction:
            case "hlf":
                registers[register_index] //= 2
                i += 1
            case "tpl":
                registers[register_index] *= 3
                i += 1
            case "inc":
                registers[register_index] += 1
                i += 1
            case "jmp":
                i += int(rest)
            case "jie":
                offset = int(rest[3:])
                i += offset if registers[register_index] % 2 == 0 else 1
            case "jio":
                offset = int(rest[3:])
                i += offset if registers[register_index] == 1 else 1

    return registers[1]


def main():
    program = list(sys.stdin)

    print(solve(program, 0))
    print(solve(program, 1))


if __name__ == "__main__":
    main()
