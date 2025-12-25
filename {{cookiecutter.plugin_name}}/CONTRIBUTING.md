# Contributing to {{cookiecutter.plugin_display_name}}

Thank you for considering contributing to {{cookiecutter.plugin_display_name}}!

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/PEAT-AI/{{cookiecutter.plugin_name}}.git
   cd {{cookiecutter.plugin_name}}
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -e ".[dev]"
   ```

3. Run tests to verify setup:
   ```bash
   pytest
   ```

## Code Style

We use [Ruff](https://github.com/astral-sh/ruff) for linting. Run before committing:

```bash
ruff check .
ruff format .
```

## Testing

Write tests for new functionality:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov

# Run specific test file
pytest tests/test_cli.py
```

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Make your changes
4. Run tests and linting
5. Commit with a clear message
6. Push to your fork
7. Open a Pull Request

## Commit Messages

Use clear, descriptive commit messages:

```
Add feature X for handling Y

- Implemented X using pattern Z
- Added tests for edge cases
- Updated documentation
```

## Hooks Development

When modifying hooks:

1. Test hooks locally by running them with sample JSON input:
   ```bash
   echo '{"session_id": "test", "cwd": "/tmp"}' | python hooks/session_start.py
   ```

2. Check logs in the configured log directory
3. Ensure hooks don't block Claude Code on errors

## Questions?

Open an issue or reach out to the maintainers.
