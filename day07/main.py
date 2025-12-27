from shared import read_input

DEBUG = False


def parse_input(lines: list[str]) -> dict[tuple[int, int], str]:
    """Parse input into a grid dictionary."""
    grid: dict[tuple[int, int], str] = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            grid[(x, y)] = char
    return grid


def part1(grid: dict[tuple[int, int], str]) -> int:
    """Count beam splits as beams fall through grid."""
    # Find starting positions (marked with 'S')
    beams: list[tuple[int, int]] = []
    for (x, y), char in grid.items():
        if char == "S":
            beams.append((x, y))

    splits = 0
    moved = True
    while moved:
        new_beams = set()
        for beam in beams:
            x, y = beam
            char = grid.get((x, y + 1))
            if char == ".":
                new_beams.add((x, y + 1))
            if char == "^":
                splits += 1
                new_beams.add((x + 1, y + 1))
                new_beams.add((x - 1, y + 1))
        beams = list(new_beams)
        if len(new_beams) == 0:
            moved = False

    return splits


def part2() -> None:
    """Part 2 not yet implemented."""
    return None


def main():
    lines = read_input(DEBUG)
    grid = parse_input(lines)
    print(part1(grid))
    # print(part2())  # Not implemented yet


if __name__ == "__main__":
    main()
