import sys


def is_valid(pw):
    return all([
        any(ord(b) - ord(a) == 1 and ord(c) - ord(b) == 1 for a, b, c in zip(pw, pw[1:], pw[2:])),
        all(c not in pw for c in "iol"),
        len(set(a + b for a, b in zip(pw, pw[1:]) if a == b)) >= 2,
    ])


def increment(pw):
    for i, c in reversed(list(enumerate(pw))):
        if c != "z":
            pw[i] = chr(ord(c) + 1)
            break

        pw[i] = "a"
    return pw


def next_password(pw):
    pw = increment(list(pw))

    while not is_valid(pw):
        pw = increment(pw)

    return "".join(pw)


def main():
    password = next(sys.stdin).rstrip()
    part1 = next_password(password)
    part2 = next_password(part1)

    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
