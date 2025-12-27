from collections import Counter
from itertools import combinations
from math import dist

from shared import read_input
from shared.union_find import UnionFind

type Point = tuple[int, int, int]
type Pair = tuple[Point, Point]

DEBUG = False


def parse_input(lines: list[str]) -> list[Point]:
    """Parse input into list of 3D points."""
    points: list[Point] = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        x, y, z = line.split(",")
        point: Point = (int(x), int(y), int(z))
        points.append(point)
    return points


def part1(points: list[Point]) -> int:
    """Find product of sizes of three largest connected components."""
    # list of tuple[distance, pair of points]
    pairwise_dists: list[tuple[float, Pair]] = []
    for p1, p2 in combinations(points, 2):
        d = dist(p1, p2)
        pairwise_dists.append((d, (p1, p2)))
    pairwise_dists.sort()

    uf = UnionFind()
    conns = 0
    for d, (p0, p1) in pairwise_dists:
        if uf.union(p0, p1):
            conns += 1
        if conns >= 20 if DEBUG else 1000:
            break

    roots = [uf.find(p) for p in points]
    group_counts = Counter(roots)
    top_three = [count for _, count in group_counts.most_common(3)]
    return top_three[0] * top_three[1] * top_three[2]


def part2() -> None:
    """Part 2 not yet implemented."""
    return None


def main():
    lines = read_input(DEBUG)
    points = parse_input(lines)
    print(part1(points))
    # print(part2())  # Not implemented yet


if __name__ == "__main__":
    main()
