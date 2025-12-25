def ppprint(grid, m, n, beams):
    for y in range(m):
        for x in range(n):
            char = grid.get((x, y))
            if (x, y) in beams:
                print("|", end="")
            elif char is not None:
                print(char, end="")
        print()


def main():
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

        grid: dict[tuple[int, int], str] = {}
        beams: list[tuple[int, int]] = []

        # n = len(lines)
        # m = len(lines[0].strip())

        for y, line in enumerate(lines):
            for x, char in enumerate(line.strip()):
                grid[(x, y)] = char
                if char == "S":
                    beams.append((x, y))

        splits = 0
        moved = True
        while moved:
            # ppprint(grid, m, n, beams)
            # input()
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

        print(splits)


main()
