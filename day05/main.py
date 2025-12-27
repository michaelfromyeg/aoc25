from shared import read_input

DEBUG = False


def parse_input(lines: list[str]) -> tuple[list[int], list[tuple[int, int]]]:
    """Parse input into values and ranges."""
    ranges = []
    idx = 0
    while idx < len(lines) and lines[idx].strip() != "":
        mn, mx = lines[idx].strip().split("-")
        ranges.append((int(mn), int(mx)))
        idx += 1

    vals = []
    for line in lines[idx + 1 :]:
        line = line.strip()
        if line == "":
            continue
        vals.append(int(line))

    return vals, ranges


def part1(vals: list[int], ranges: list[tuple[int, int]]) -> int:
    """Count how many values fall within the ranges."""
    count = 0
    for v in vals:
        for mn, mx in ranges:
            if mn <= v <= mx:
                count += 1
                break
    return count


def part2(ranges: list[tuple[int, int]]) -> int:
    """Merge overlapping ranges and count total coverage."""
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    new_ranges = []

    current_range = sorted_ranges[0]
    for next_range in sorted_ranges[1:]:
        if next_range[0] <= current_range[1]:
            # combine
            new_range = (current_range[0], max(current_range[1], next_range[1]))
            current_range = new_range
        else:
            new_ranges.append(current_range)
            current_range = next_range
    new_ranges.append(current_range)

    c = 0
    for r in new_ranges:
        c += r[1] - r[0] + 1

    return c


def main():
    lines = read_input(DEBUG)
    vals, ranges = parse_input(lines)
    print(part1(vals, ranges))
    print(part2(ranges))


if __name__ == "__main__":
    main()
