.PHONY: install test lint clean help register unregister

PYTHON := python3
VENV := .venv
BIN := $(VENV)/bin

help:
	@echo "{{cookiecutter.plugin_display_name}} - Claude Code Plugin"
	@echo ""
	@echo "Usage:"
	@echo "  make install    Create venv, install deps, register with Claude Code"
	@echo "  make test       Run test suite"
	@echo "  make lint       Run linter (ruff)"
	@echo "  make clean      Remove venv and caches"
	@echo "  make register   Register hooks with Claude Code"
	@echo "  make unregister Remove hooks from Claude Code"

install: $(VENV)/bin/activate register
	@echo ""
	@echo "Installation complete!"
	@echo "Run 'source $(VENV)/bin/activate' to activate the virtual environment."

$(VENV)/bin/activate:
	@echo "Creating virtual environment..."
	$(PYTHON) -m venv $(VENV)
	@echo "Installing dependencies..."
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install -e ".[dev]"

test: $(VENV)/bin/activate
	$(BIN)/pytest

lint: $(VENV)/bin/activate
	$(BIN)/ruff check .

register: $(VENV)/bin/activate
	@echo "Registering with Claude Code..."
	$(BIN)/python scripts/register.py

unregister: $(VENV)/bin/activate
	@echo "Unregistering from Claude Code..."
	$(BIN)/python scripts/register.py --unregister

clean:
	rm -rf $(VENV)
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf *.egg-info
	rm -rf dist build
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
