# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an Advent of Code 2025 solutions repository written in Python 3.14, using `uv` for dependency management. The package is installed in development mode, allowing imports to work seamlessly across all solutions.

## Quick Start

Run the setup script to install dependencies:

```bash
make setup
# or: bash scripts/setup.sh
```

Create a new day from template:

```bash
make new-day DAY=04
# or: python scripts/new_day.py 4
```

Run a solution:

```bash
make run DAY=01
# or: uv run python day01/main.py
```

## Running Solutions

**Recommended:** Use the Makefile:

```bash
make run DAY=01
make run DAY=08
```

Alternatively, run directly with `uv run`:

```bash
uv run python day01/main.py
uv run python day08/main.py
```

Or as a module:

```bash
uv run python -m day01.main
uv run python -m day08.main
```

All solutions have a `DEBUG` flag at the top of the file. Set `DEBUG = True` to use `test.txt` instead of `input.txt`.

## Project Structure

```
dayNN/          # Each day is a top-level package (day01, day02, etc.)
  __init__.py   # Package marker
  main.py       # Solution script
  input.txt     # Puzzle input
  test.txt      # Test/example input
shared/         # Reusable utilities and data structures
  __init__.py
  union_find.py
scripts/        # Setup scripts
```

## Shared Library

The `shared/` directory contains reusable utilities:

- `shared/__init__.py`: Common helpers
  - `read_input(debug: bool = False)`: Read input file for the calling module (test.txt if debug=True, else input.txt)
- `shared/union_find.py`: Union-Find (disjoint set) data structure with path compression and union by rank

Solutions import from `shared/` using absolute imports:
```python
from shared import read_input
from shared.union_find import UnionFind
```

## Solution Patterns

All solutions follow this standardized structure:

```python
from shared import read_input

DEBUG = False


def parse_input(lines: list[str]):
    """Parse raw input lines into structured data."""
    # Parse input...
    return data


def part1(data) -> int:
    """Solve part 1 of the puzzle."""
    # Solution for part 1...
    return result


def part2(data) -> int:
    """Solve part 2 of the puzzle."""
    # Solution for part 2...
    return result


def main():
    lines = read_input(DEBUG)
    data = parse_input(lines)
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
```

Key patterns:
- Use `read_input(DEBUG)` from `shared` module to load input files
- Separate `parse_input()`, `part1()`, and `part2()` functions
- Each solution has dedicated functions for both parts (even if part 2 isn't implemented yet)
- Results are printed directly to stdout
- Solutions can be run from any directory

Some solutions use type aliases for clarity:
```python
type Point = tuple[int, int, int]
type Pair = tuple[Point, Point]
```

## Development Tools

This project uses Astral's suite of tools for development:

- **uv**: Fast Python package manager and runner
- **ruff**: Fast Python linter and formatter
- **ty**: Extremely fast Python type checker (10-100x faster than mypy/pyright)

### Makefile Commands

```bash
make help          # Show all available commands
make setup         # Install dependencies
make new-day DAY=04 # Create a new day from template

make run DAY=01    # Run a specific day
make lint          # Lint with ruff
make format        # Format with ruff
make typecheck     # Type check with ty
make check         # Run lint + typecheck
make all           # Format + check

make clean         # Remove Python cache files
```

### Manual Commands

If you prefer not to use the Makefile:

```bash
# Linting and formatting
uv run ruff check .
uv run ruff format .

# Type checking
uv run ty check .

# Create new day
python scripts/new_day.py 4
```

### Editor Setup (Zed)

This project includes `.zed/settings.json` with pre-configured settings for:
- **ty** as the primary language server (disables basedpyright)
- **ruff** for formatting with format-on-save enabled
- Python-specific settings (4-space tabs)

The configuration runs tools via `uv run` to ensure they use the project's virtual environment.

To customize these settings globally, you can also configure `~/.config/zed/settings.json`. See [ty's Zed documentation](https://docs.astral.sh/ty/editors/#zed) for more details.

## Development Setup

Initial setup (run once):

```bash
make setup
# or: bash scripts/setup.sh
```

This will:
- Verify uv is installed
- Install the package in editable mode
- Install development dependencies (ruff, ty)

If you add a new day or make structural changes, reinstall:

```bash
uv pip install -e .
```
