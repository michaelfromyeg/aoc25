from pprint import pprint

from shared import read_input

DEBUG = False

type Graph = dict[str, list[str]]

START1 = "you"
START2 = "svr"
END = "out"


def parse_input(lines: list[str]) -> Graph:
    """Parse input into structured data."""
    graph: Graph = {}
    for line in lines:
        line = line.strip()
        key, vals = line.split(":")
        vals = vals.strip()
        if key in graph:
            raise ValueError(f"{key} already in graph")
        graph[key] = vals.split(" ")
    return graph


def dfs(data: Graph, node: str, path: list[str]) -> list[list[str]]:
    if node == END:
        pprint(f"Found path of length {len(path)}, {path}")
        return [path]

    neighbors = data.get(node)
    if not neighbors:
        return []

    new_paths = []
    for neighbor in neighbors:
        if neighbor in path:
            continue
        fpath = list(path)
        fpath.append(neighbor)
        new_paths.extend(dfs(data, neighbor, fpath))

    return new_paths


def part1(data: Graph) -> int:
    """Solve part 1 of the puzzle."""
    pprint(data)
    paths = dfs(data, START1, [START1])
    pprint(paths)
    return len(paths)


def part2(data) -> int:
    """Solve part 2 of the puzzle."""
    pprint(data)
    paths = dfs(data, START2, [START2])
    count = 0
    pprint(paths)
    print(len(paths))
    for path in paths:
        if "fft" not in path or "dac" not in path:
            continue
        count += 1
    return count


def main():
    lines = read_input(DEBUG)
    data = parse_input(lines)
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
