"""Configuration loading for {{cookiecutter.plugin_display_name}}.

Secrets are loaded in this order:
1. Environment variables (preferred for CI/CD)
2. .env file in plugin directory
3. ~/.claude/secrets/KEYS_TOKENS_CLAUDE.md (Rob's pattern)
"""

import os
import re
from pathlib import Path
from typing import Any

# Try to load dotenv if available
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


def load_api_key(name: str) -> str | None:
    """Load an API key from environment or secrets file.

    Args:
        name: Key name prefix (e.g., "OPENAI" for OPENAI_API_KEY)

    Returns:
        API key string or None if not found
    """
    # 1. Environment variable (e.g., OPENAI_API_KEY)
    env_key = f"{name.upper()}_API_KEY"
    if key := os.environ.get(env_key):
        return key

    # 2. Secrets file fallback
    secrets_path = Path.home() / ".claude" / "secrets" / "KEYS_TOKENS_CLAUDE.md"
    if secrets_path.exists():
        return _parse_key_from_markdown(secrets_path, name)

    return None


def _parse_key_from_markdown(path: Path, name: str) -> str | None:
    """Parse an API key from the markdown secrets file.

    Supports patterns like:
    - "OpenAI API Key: sk-..."
    - "**OpenAI:** sk-..."
    - "Key: sk-..." under a ## OpenAI heading
    """
    content = path.read_text()
    name_lower = name.lower()

    # Pattern: Name followed by key-like string
    patterns = [
        rf"{name_lower}[:\s]+api[_\s]*key[:\s]+([A-Za-z0-9_-]+)",
        rf"\*\*{name_lower}[:\*\s]+([A-Za-z0-9_-]+)",
        rf"Key[:\s]+([A-Za-z0-9_-]+)",  # Generic, check context
    ]

    for pattern in patterns:
        if match := re.search(pattern, content, re.IGNORECASE):
            return match.group(1)

    return None


def load_config() -> dict[str, Any]:
    """Load plugin configuration.

    Returns:
        Configuration dictionary
    """
    from .paths import get_data_dir

    config: dict[str, Any] = {
        "data_dir": str(get_data_dir()),
        "verbose": os.environ.get("{{cookiecutter.plugin_name | upper}}_VERBOSE", "").lower()
        in ("1", "true", "yes"),
    }

    # Load any API keys if this plugin uses them
    {%- if cookiecutter.include_api_client %}
    config["api_key"] = load_api_key("{{cookiecutter.plugin_name | upper}}")
    {%- endif %}

    return config
