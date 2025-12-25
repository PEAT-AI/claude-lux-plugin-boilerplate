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
3. Register hooks with Claude Code

## Usage

### CLI Commands

```bash
# Show plugin status
{{cookiecutter.plugin_name}} status

# Echo a message (example command)
{{cookiecutter.plugin_name}} echo "Hello, Claude!"

# Test API connection (if configured)
{{cookiecutter.plugin_name}} test-connection
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
| `{{cookiecutter.plugin_name | upper}}_API_KEY` | API key (if needed) | - |
| `{{cookiecutter.plugin_name | upper}}_VERBOSE` | Enable verbose logging | `false` |
| `{{cookiecutter.plugin_name | upper}}_DATA_DIR` | Override data directory | `~/.local/share/{{cookiecutter.plugin_name}}` |
| `{{cookiecutter.plugin_name | upper}}_LOG_DIR` | Override log directory | `~/.local/state/{{cookiecutter.plugin_name}}/logs` |

### Secrets File (Alternative)

You can also store API keys in `~/.claude/secrets/KEYS_TOKENS_CLAUDE.md`:

```markdown
## {{cookiecutter.plugin_display_name}}
API Key: your-key-here
```

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
│   └── client.py                    # API client (optional)
├── hooks/                           # Claude Code hooks
│   ├── session_start.py
│   ├── post_tool_use.py
│   └── stop.py
├── tests/                           # Test suite
├── scripts/                         # Utility scripts
└── bin/                             # Entry point wrapper
```

## License

Apache 2.0 - See [LICENSE](LICENSE) for details.
