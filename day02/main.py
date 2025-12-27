"""
Invalid IDs.

Better ideas for part 2: directly generate repeated pattern
numbers within range. Use math (ABCABC = ABC * 1001).
"""

from shared import read_input

DEBUG = False


def parse_input(lines: list[str]) -> list[tuple[int, int]]:
    """Parse input into list of (start, end) ranges."""
    line = lines[0].strip()
    ranges = []
    for id_range in line.split(","):
        s, e = id_range.split("-")
        ranges.append((int(s), int(e)))
    return ranges


def part1(ranges: list[tuple[int, int]]) -> int:
    """Count numbers where first half equals second half."""
    total = 0
    for s, e in ranges:
        for i in range(s, e + 1):
            i_str = str(i)
            n = len(i_str)
            if n % 2 == 1:
                continue
            if i_str[0 : n // 2] == i_str[n // 2 :]:
                total += i
    return total


def part2(ranges: list[tuple[int, int]]) -> int:
    """Count numbers that are repeated patterns."""
    total = 0
    for s, e in ranges:
        for i in range(s, e + 1):
            i_str = str(i)
            n = len(i_str)
            for pattern_len in range(1, n // 2 + 1):
                if n % pattern_len == 0 and i_str == i_str[0:pattern_len] * (n // pattern_len):
                    total += i
                    break
    return total


def main():
    lines = read_input(DEBUG)
    ranges = parse_input(lines)
    print(part1(ranges))
    print(part2(ranges))


if __name__ == "__main__":
    main()
