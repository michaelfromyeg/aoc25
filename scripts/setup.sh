#!/bin/bash
# Setup script for Advent of Code 2025 repository

set -e  # Exit on error

echo "<„ Setting up Advent of Code 2025 repository..."

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "L Error: uv is not installed"
    echo "   Install it from: https://docs.astral.sh/uv/getting-started/installation/"
    exit 1
fi

echo " Found uv $(uv --version)"

# Install the package in editable mode
echo "=æ Installing package in editable mode..."
uv pip install -e .

# Install development dependencies
echo "=' Installing development dependencies..."
uv pip install ruff ty

echo ""
echo " Setup complete!"
echo ""
echo "Available commands:"
echo "  make run DAY=01    - Run a specific day's solution"
echo "  make lint          - Lint the code with ruff"
echo "  make format        - Format the code with ruff"
echo "  make typecheck     - Type check with ty"
echo "  make help          - Show all available commands"
echo ""
echo "Create a new day:"
echo "  python scripts/new_day.py 04"
