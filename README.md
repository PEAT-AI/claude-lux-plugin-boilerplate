# Claude Lux Plugin Boilerplate

A [Cookiecutter](https://cookiecutter.readthedocs.io/) template for creating Claude Code plugins.

## Features

- **Python-first**: Clean, typed Python codebase
- **Claude Code hooks**: SessionStart, PostToolUse, Stop hooks out of the box
- **CLI framework**: Click-based command-line interface
- **XDG-compliant paths**: Data stored in standard locations
- **Secrets handling**: Environment variables + file fallback
- **Auto-registration**: One-command setup with Claude Code
- **Testing**: pytest + coverage ready
- **CI/CD**: GitHub Actions workflow included

## Quick Start

```bash
# Install cookiecutter if you haven't
pip install cookiecutter

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
| `include_hooks` | Include Claude Code hooks | `true` |
| `include_api_client` | Include HTTP client module | `true` |

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
│   └── client.py        # HTTP client
├── hooks/               # Claude Code hooks
│   ├── session_start.py
│   ├── post_tool_use.py
│   └── stop.py
├── tests/               # Test suite
├── scripts/             # Utilities
│   └── register.py      # Claude Code registration
├── bin/
│   └── run              # Entry point wrapper
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
