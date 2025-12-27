#!/usr/bin/env python3
"""
Script to create a new Advent of Code day directory.

Usage:
    python scripts/new_day.py <day_number>
    python scripts/new_day.py 04
"""

import sys
from pathlib import Path

TEMPLATE = '''from shared import read_input

DEBUG = False


def parse_input(lines: list[str]):
    """Parse input into structured data."""
    # TODO: Implement parsing
    return lines


def part1(data) -> int:
    """Solve part 1 of the puzzle."""
    # TODO: Implement part 1
    return 0


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
'''


def create_day(day_num: int) -> None:
    """Create a new day directory with template files."""
    # Get project root (parent of scripts directory)
    project_root = Path(__file__).parent.parent
    day_dir = project_root / f"day{day_num:02d}"

    # Check if directory already exists
    if day_dir.exists():
        print(f"Error: Day {day_num:02d} already exists at {day_dir}", file=sys.stderr)
        sys.exit(1)

    # Create directory and files
    day_dir.mkdir()

    # Create __init__.py
    (day_dir / "__init__.py").touch()

    # Create main.py with template
    (day_dir / "main.py").write_text(TEMPLATE)

    # Create empty input files
    (day_dir / "input.txt").touch()
    (day_dir / "test.txt").touch()

    print(f"✓ Created day{day_num:02d}/ with template files")
    print(f"  - {day_dir / 'main.py'}")
    print(f"  - {day_dir / 'input.txt'}")
    print(f"  - {day_dir / 'test.txt'}")
    print("\nNext steps:")
    print(f"  1. Add your input to day{day_num:02d}/input.txt")
    print(f"  2. Add test input to day{day_num:02d}/test.txt")
    print(f"  3. Implement the solution in day{day_num:02d}/main.py")
    print(f"  4. Run with: make run DAY={day_num:02d}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/new_day.py <day_number>", file=sys.stderr)
        print("Example: python scripts/new_day.py 04", file=sys.stderr)
        sys.exit(1)

    try:
        day_num = int(sys.argv[1])
        if day_num < 1 or day_num > 25:
            raise ValueError("Day must be between 1 and 25")
    except ValueError as e:
        print(f"Error: Invalid day number - {e}", file=sys.stderr)
        sys.exit(1)

    create_day(day_num)


if __name__ == "__main__":
    main()
