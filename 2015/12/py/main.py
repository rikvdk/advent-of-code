import re
import json
import sys


def sum_non_red_numbers(obj):
    if isinstance(obj, int):
        return obj
    elif isinstance(obj, str):
        return 0
    elif isinstance(obj, list):
        return sum(sum_non_red_numbers(item) for item in obj)
    elif "red" not in obj.values():
        return sum(sum_non_red_numbers(item) for item in obj.values())

    return 0


def main():
    pattern = re.compile(r"[-+]?\d+")
    line = next(sys.stdin)

    print(sum(map(int, re.findall(pattern, line))))
    print(sum_non_red_numbers(json.loads(line)))


if __name__ == "__main__":
    main()
