"""Configuration loading for {{cookiecutter.plugin_display_name}}.

Configuration sources (in order of precedence):
1. Environment variables
2. .env file in plugin directory (if python-dotenv installed)
"""

import os
from typing import Any

# Try to load dotenv if available
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


def load_config() -> dict[str, Any]:
    """Load plugin configuration.

    Returns:
        Configuration dictionary
    """
    from .paths import get_data_dir

    return {
        "data_dir": str(get_data_dir()),
        "verbose": os.environ.get("{{cookiecutter.plugin_name | upper}}_VERBOSE", "").lower()
        in ("1", "true", "yes"),
    }
