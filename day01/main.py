"""
Turning a dial.

Tried doing divmod stuff but it didn't work.
"""

from shared import read_input

DEBUG = False


def part1(lines: list[str]) -> int:
    """Count times dial lands on 0 after each full instruction."""
    dial = 50
    count = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue

        dir, amt = line[0], int(line[1:])
        for _ in range(amt):
            dial += 1 * (-1 if dir == "L" else 1)
            dial %= 100

        if dial == 0:
            count += 1

    return count


def part2(lines: list[str]) -> int:
    """Count times dial lands on 0 during any step."""
    dial = 50
    count = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue

        dir, amt = line[0], int(line[1:])
        for _ in range(amt):
            dial += 1 * (-1 if dir == "L" else 1)
            dial %= 100

            if dial == 0:
                count += 1

    return count


def main():
    lines = read_input(DEBUG)
    print(part1(lines))
    print(part2(lines))


if __name__ == "__main__":
    main()
