.PHONY: help setup run lint format typecheck check all clean

# Default target - show help
help:
	@echo "🎄 Advent of Code 2025 - Available Commands"
	@echo ""
	@echo "Setup:"
	@echo "  make setup              Install dependencies and set up the project"
	@echo ""
	@echo "Development:"
	@echo "  make run DAY=XX         Run a specific day (e.g., make run DAY=01)"
	@echo "  make lint               Lint code with ruff"
	@echo "  make format             Format code with ruff"
	@echo "  make typecheck          Type check with ty"
	@echo "  make check              Run lint + typecheck"
	@echo "  make all                Run format + check"
	@echo ""
	@echo "Utilities:"
	@echo "  make clean              Remove Python cache files"
	@echo "  make new-day DAY=XX     Create a new day directory"
	@echo ""
	@echo "Examples:"
	@echo "  make run DAY=08         Run day 8"
	@echo "  make new-day DAY=04     Create day 4 from template"

# Setup the project
setup:
	@bash scripts/setup.sh

# Run a specific day (requires DAY argument)
run:
ifndef DAY
	@echo "Error: DAY argument required"
	@echo "Usage: make run DAY=XX (e.g., make run DAY=01)"
	@exit 1
endif
	@uv run python day$(DAY)/main.py

# Lint with ruff
lint:
	@echo "🔍 Linting with ruff..."
	@uv run ruff check .

# Format with ruff
format:
	@echo "✨ Formatting with ruff..."
	@uv run ruff format .

# Type check with ty
typecheck:
	@echo "🔬 Type checking with ty..."
	@uv run ty check .

# Run lint + typecheck
check: lint typecheck
	@echo "✅ All checks passed!"

# Run format + check
all: format check
	@echo "✅ Format and checks complete!"

# Clean Python cache files
clean:
	@echo "🧹 Cleaning cache files..."
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name "*.pyo" -delete
	@echo "✅ Cache cleaned!"

# Create a new day (requires DAY argument)
new-day:
ifndef DAY
	@echo "Error: DAY argument required"
	@echo "Usage: make new-day DAY=XX (e.g., make new-day DAY=04)"
	@exit 1
endif
	@uv run python scripts/new_day.py $(DAY)
