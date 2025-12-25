# Claude Lux Plugin Boilerplate

A [Cookiecutter](https://cookiecutter.readthedocs.io/) template for creating Claude Code plugins.

## Features

- **Python-first**: Clean, typed Python codebase
- **Claude Code hooks**: SessionStart, PostToolUse, Stop hooks out of the box
- **CLI framework**: Click-based command-line interface
- **XDG-compliant paths**: Data stored in standard locations
- **Auto-registration**: One-command setup with Claude Code (with backup)
- **Testing**: pytest + ruff ready
- **CI/CD**: GitHub Actions workflow included

## Quick Start

```bash
# Install cookiecutter if you haven't
pip install cookiecutter

# Or use uvx (no install needed)
uvx cookiecutter gh:PEAT-AI/claude-lux-plugin-boilerplate

# Generate a new plugin
cookiecutter gh:PEAT-AI/claude-lux-plugin-boilerplate
```

You'll be prompted for:

| Variable | Description | Default |
|----------|-------------|---------|
| `plugin_name` | Python package name (snake_case) | `my_plugin` |
| `plugin_display_name` | Human-readable name | `My Plugin` |
| `plugin_description` | Short description | `A Claude Code plugin...` |
| `author` | Author name | `PEAT-AI` |
| `author_email` | Author email | `dev@peat.ai` |
| `python_version` | Minimum Python version | `3.10` |

## After Generation

```bash
cd my_plugin

# Install and register with Claude Code
make install

# Activate the virtual environment
source .venv/bin/activate

# Test it
my_plugin status
```

## Project Structure

Generated plugins follow this structure:

```
my_plugin/
├── my_plugin/           # Python package
│   ├── __init__.py
│   ├── cli.py           # Click CLI
│   ├── config.py        # Configuration
│   ├── paths.py         # XDG paths
│   └── hooks.py         # Hook utilities
├── hooks/               # Claude Code hooks
│   ├── session_start.py
│   ├── post_tool_use.py
│   └── stop.py
├── tests/               # Test suite
├── scripts/
│   └── register.py      # Claude Code registration
├── pyproject.toml
├── plugin.json          # Plugin manifest
├── Makefile
└── README.md
```

## Lux Plugin Family

This boilerplate is used for:

- **[lux-knowledge](https://github.com/PEAT-AI/lux-knowledge)**: Persistent memory for Claude Code
- **[lux-coworker](https://github.com/PEAT-AI/lux-coworker)**: AI co-workers for second opinions

## Requirements

- Python 3.10+
- [Cookiecutter](https://cookiecutter.readthedocs.io/)
- Claude Code

## License

Apache 2.0 - See [LICENSE](LICENSE) for details.
