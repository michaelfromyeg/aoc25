"""
Joltage.

Turns out: actually faster to remove digits?
"""

from shared import read_input

DEBUG = False


def next_digit(line: str, imin: int, imax: int) -> tuple[int, int]:
    """Find the index and value of the largest digit in range [imin, imax)."""
    idx, digit = imin, int(line[imin])
    for i, c in enumerate(line[0:imax]):
        if i <= imin:
            continue
        if int(c) > digit:
            idx, digit = i, int(c)
    return idx, digit


def part1(lines: list[str]) -> int:
    """Find two largest digits and form a two-digit number."""
    total = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue

        n = len(line)
        tens_index, tens_digit = next_digit(line, 0, n - 1)
        ones_index, ones_digit = next_digit(line, tens_index + 1, n)

        if ones_index < tens_index:
            raise Exception("Invalid indices")
        total += tens_digit * 10 + ones_digit

    return total


def part2(lines: list[str]) -> int:
    """Find 12 largest digits in order and form a 12-digit number."""
    total = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue

        n = len(line)
        digits = []
        k = 12

        if n < k:
            raise Exception("Line too short")

        imin, imax = 0, n - (k - 1)

        for i in range(k):
            ni, nd = next_digit(line, imin, imax)
            digits.append(nd)
            imin = ni + 1
            imax += 1

        for i, digit in enumerate(digits):
            total += digit * (10 ** (k - i - 1))

    return total


def main():
    lines = read_input(DEBUG)
    print(part1(lines))
    print(part2(lines))


if __name__ == "__main__":
    main()
