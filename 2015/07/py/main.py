import sys
from operator import and_, lshift, or_, rshift


OPERATORS = {
    "AND": and_,
    "OR": or_,
    "LSHIFT": lshift,
    "RSHIFT": rshift,
}


def resolve(instructions, wire):
    instruction = instructions.get(wire, wire)

    if isinstance(instruction, int):
        return instruction
    elif len(instruction) == 1:
        value = resolve(instructions, instruction[0])
    elif len(instruction) == 2:
        value = ~resolve(instructions, instruction[1])
    else:
        left = resolve(instructions, instruction[0])
        right = resolve(instructions, instruction[2])
        op = OPERATORS[instruction[1]]

        value = op(left, right)

    value &= 0xFFFF
    instructions[wire] = value

    return value


def main():
    instructions = {}

    for line in sys.stdin.read().splitlines():
        parts = tuple(
            part if not part.isdigit() else int(part) for part in line.split(" ")
        )
        instructions[parts[-1]] = parts[:-2]

    part1 = resolve(instructions.copy(), "a")
    instructions["b"] = part1
    part2 = resolve(instructions, "a")

    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
