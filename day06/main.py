from functools import reduce

from shared import read_input

DEBUG = False


def parse_input(lines: list[str]) -> tuple[list[list[int]], list[str]]:
    """Parse input into parts grid and operations."""
    parts = []
    for line in lines[:-1]:
        line = line.strip()
        ps = line.split()
        parts.append([int(part) for part in ps])

    ops = lines[-1].strip().split()
    return parts, ops


def part1(parts: list[list[int]], ops: list[str]) -> int:
    """Calculate result based on operations applied to transposed parts."""
    # Transpose the parts
    parts = [list(row) for row in zip(*parts)]

    total = 0
    for i, part in enumerate(parts):
        if ops[i] == "+":
            total += sum(part)
        else:
            total += reduce(lambda x, y: x * y, part)
    return total


def part2() -> None:
    """Part 2 not yet implemented."""
    return None


def main():
    lines = read_input(DEBUG)
    parts, ops = parse_input(lines)
    print(part1(parts, ops))
    # print(part2())  # Not implemented yet


if __name__ == "__main__":
    main()
