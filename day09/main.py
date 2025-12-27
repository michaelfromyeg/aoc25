from itertools import combinations

# from pprint import pprint
from shared import read_input

DEBUG = False

type Point = tuple[int, int]


def parse_input(lines: list[str]) -> list[Point]:
    """Parse input into structured data."""
    coords: list[Point] = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        x, y = line.split(",")
        coords.append((int(x), int(y)))
    # pprint(coords)
    return coords


def area(p1: Point, p2: Point) -> int:
    x1, y1 = p1
    x2, y2 = p2
    return (abs(y2 - y1) + 1) * (abs(x2 - x1) + 1)


def part1(data: list[Point]) -> int:
    """Solve part 1 of the puzzle."""
    mx = area(data[0], data[1])
    for p1, p2 in combinations(data, 2):
        other1 = (p1[0], p2[1])
        other2 = (p1[1], p2[0])
        if other1 in data or other2 in data:
            continue
        mx = max(mx, area(p1, p2))
    return mx


def part2(data) -> int:
    """Solve part 2 of the puzzle."""
    # TODO: Implement part 2
    return 0


def main():
    lines = read_input(DEBUG)
    data = parse_input(lines)
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
