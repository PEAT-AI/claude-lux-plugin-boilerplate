# {{cookiecutter.plugin_display_name}}

{{cookiecutter.plugin_description}}

## Installation

```bash
# Clone the repository
git clone https://github.com/PEAT-AI/{{cookiecutter.plugin_name}}.git
cd {{cookiecutter.plugin_name}}

# Install and register with Claude Code
make install
```

This will:
1. Create a virtual environment
2. Install dependencies
3. Backup existing settings and register hooks with Claude Code

## Usage

### CLI Commands

```bash
# Show plugin status
{{cookiecutter.plugin_name}} status
```

### Hooks

This plugin provides the following Claude Code hooks:

| Hook | Trigger | Purpose |
|------|---------|---------|
| `SessionStart` | Session begins | Inject context, initialize state |
| `PostToolUse` | After each tool | Capture tool executions |
| `Stop` | Session ends | Save state, generate summaries |

## Configuration

### Environment Variables

Copy `.env.example` to `.env` and configure:

```bash
cp .env.example .env
```

Available settings:

| Variable | Description | Default |
|----------|-------------|---------|
| `{{cookiecutter.plugin_name | upper}}_VERBOSE` | Enable verbose logging | `false` |
| `{{cookiecutter.plugin_name | upper}}_DATA_DIR` | Override data directory | `~/.local/share/{{cookiecutter.plugin_name}}` |
| `{{cookiecutter.plugin_name | upper}}_LOG_DIR` | Override log directory | `~/.local/state/{{cookiecutter.plugin_name}}/logs` |

## Development

```bash
# Run tests
make test

# Run linter
make lint

# Clean up
make clean
```

## Uninstalling

```bash
# Remove hooks from Claude Code
make unregister

# Clean up files
make clean
```

## File Structure

```
{{cookiecutter.plugin_name}}/
├── {{cookiecutter.plugin_name}}/    # Python package
│   ├── cli.py                       # CLI commands
│   ├── config.py                    # Configuration loading
│   ├── paths.py                     # XDG path utilities
│   └── hooks.py                     # Hook utilities
├── hooks/                           # Claude Code hooks
│   ├── session_start.py
│   ├── post_tool_use.py
│   └── stop.py
├── tests/                           # Test suite
└── scripts/                         # Utility scripts
```

## License

Apache 2.0 - See [LICENSE](LICENSE) for details.
