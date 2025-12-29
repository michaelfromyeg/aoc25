from pprint import pprint

from shared import read_input

DEBUG = False

# a 2D Cartesian point: (x, y)
type Point = tuple[int, int]
# a present: the index, and a sparse representation of the gift
type Shape = set[Point]
type ShapeVariants = list[Shape]
type Present = tuple[int, ShapeVariants]
# a region to fill in: m, n, a list where len(list) == P where P is # of presents
type Region = tuple[int, int, list[int]]


def print_shape(shape: Shape, m: int | None, n: int | None) -> None:
    m = m if m is not None else max(p[0] for p in shape) + 1
    n = n if n is not None else max(p[1] for p in shape) + 1
    for y in range(n):
        for x in range(m):
            if (x, y) in shape:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


def normalize(shape: Shape) -> Shape:
    """
    First, we imagine taking the shape in arbitrary coordinate space
    and "sliding it" (translating it) into the first quadrant, such that

    - the bottom of the shape is flush against the x-axis (y=0)
    - the left   of the shape is flush against the y-axis (x=0)
    """
    cells = list(shape)

    min_x = min(p[0] for p in cells)
    min_y = min(p[1] for p in cells)

    for i in range(len(cells)):
        x, y = cells[i]
        cells[i] = (x - min_x, y - min_y)

    return set(cells)


def rotate(shape: Shape) -> Shape:
    return normalize({(y, -x) for x, y in shape})


def flip(shape: Shape) -> Shape:
    return normalize({(-x, y) for x, y in shape})


def get_orientations(shape: Shape) -> ShapeVariants:
    """
    Get all possible orientations of a shape.

    - rotate: (x, y) -> (y, -x)
    - flip: (x, y) -> (-x, y)
    """
    s000 = normalize(shape)
    s090 = rotate(s000)
    s180 = rotate(s090)
    s270 = rotate(s180)

    s000p = flip(s000)
    s090p = rotate(s000p)
    s180p = rotate(s090p)
    s270p = rotate(s180p)

    all_orientations = [s000, s090, s180, s270, s000p, s090p, s180p, s270p]
    # if we made the above a `set`, we can't dedupe them
    # but `frozenset` works for this
    # TODO(michaelfromyeg): use `frozenset` the whole time, where possible (this is a bit inefficient)
    unique = set(frozenset(s) for s in all_orientations)
    return [set(fs) for fs in unique]


def parse_input(lines: list[str]) -> tuple[list[Present], list[Region]]:
    """Parse input into structured data."""
    input = "".join(lines)
    chunks = input.split("\n\n")

    presents: list[Present] = []
    for chunk in chunks[:-1]:
        # pprint(chunk)
        lines = chunk.split("\n")

        index = int(lines[0].split(":")[0].strip())

        shape: Shape = set()
        for y, line in enumerate(lines[1:]):
            line = line.strip()
            for x, c in enumerate(line):
                if c == "#":
                    shape.add((x, y))

        presents.append((index, get_orientations(shape)))
    pprint(presents)

    regions: list[Region] = []
    for region_str in chunks[-1].split("\n"):
        region_str = region_str.strip()
        if not region_str:
            continue
        dims, amts_str = region_str.split(":")

        m_str, n_str = dims.split("x")
        m = int(m_str)
        n = int(n_str)

        amt_strs = amts_str.strip().split(" ")
        amts = [int(amt.strip()) for amt in amt_strs]

        regions.append((m, n, amts))
    pprint(regions)

    return (presents, regions)


def find_first_empty(grid: set[Point], m: int, n: int) -> Point:
    for y in range(n):
        for x in range(m):
            if (x, y) not in grid:
                return (x, y)
    return (-1, -1)


def choose_piece(pieces_remaining: list[int]) -> int:
    for i in range(len(pieces_remaining)):
        if pieces_remaining[i] > 0:
            return i
    return -1


def fits(grid: set[Point], m: int, n: int, shape: Shape, posx: int, posy: int) -> set[Point] | None:
    new_grid = grid.copy()
    # print("[fits]", new_grid)
    for cell in shape:
        x, y = cell
        x += posx
        y += posy
        # print("\tTrying", x, y)

        if x < 0 or x >= m:
            return None
        if y < 0 or y >= n:
            return None

        if (x, y) in new_grid:
            return None

        new_grid.add((x, y))
    return new_grid


def no_space_remaining(
    grid: set[Point], m: int, n: int, pieces_remaining: list[int], presents: list[Present]
) -> bool:
    cells_to_place = 0
    for i, piece_remaining in enumerate(pieces_remaining):
        present = presents[i][1][0]
        cells_to_place += piece_remaining * len(present)

    space_remaining = m * n - len(grid)

    return cells_to_place > space_remaining


attempts = 0


def can_place_all(
    grid: set[Point], m: int, n: int, pieces_remaining: list[int], presents: list[Present]
) -> bool:
    global attempts
    attempts += 1
    if attempts % 10000 == 0:
        print(f"Attempts: {attempts}, pieces left: {sum(pieces_remaining)}")

    if sum(pieces_remaining) == 0:
        return True

    if no_space_remaining(grid, m, n, pieces_remaining, presents):
        return False

    piece = choose_piece(pieces_remaining)
    if piece == -1:
        raise ValueError("No piece left")
    present = presents[piece][1]

    x, y = find_first_empty(grid, m, n)
    if x == -1 or y == -1:
        return False

    # print(f">> Trying {x}, {y} <<")
    for orientation in present:
        # print(f"Found piece {piece}, trying")
        # print_shape(orientation, None, None)
        for sx, sy in orientation:
            # print(f"Sliding {sx}, {sy}")
            if new_grid := fits(grid, m, n, orientation, x - sx, y - sy):
                # print("[[ NEW GRID ]]")
                # print_shape(new_grid, m, n)
                new_places_remaining = list(pieces_remaining)
                new_places_remaining[piece] -= 1
                if can_place_all(new_grid, m, n, new_places_remaining, presents):
                    # print("Found solution!")
                    # print_shape(new_grid, m, n)
                    return True
    new_grid = grid.copy()
    new_grid.add((x, y))
    return can_place_all(new_grid, m, n, pieces_remaining, presents)


def part1(data: tuple[list[Present], list[Region]]) -> int:
    """Solve part 1 of the puzzle."""
    global attempts

    presents, regions = data

    for present in presents:
        index, orientations = present
        print(f"=== Shape {index} ===")
        for jndex, orientation in enumerate(orientations):
            print(f"= Orientation {jndex}")
            print_shape(orientation, None, None)

    count = 0
    for region in regions:
        pprint(f"Trying {region}")
        m, n, pieces_remaining = region
        grid = set()
        if can_place_all(grid, m, n, pieces_remaining, presents):
            print("Found solution!")
            print_shape(grid, m, n)
            attempts = 0
            count += 1

    return count


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
