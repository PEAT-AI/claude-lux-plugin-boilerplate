"""XDG-compliant path utilities for {{cookiecutter.plugin_display_name}}.

Data and state are stored outside the plugin directory, following XDG conventions:
- Data: ~/.local/share/{{cookiecutter.plugin_name}}/
- State/Logs: ~/.local/state/{{cookiecutter.plugin_name}}/logs/
- Config: ~/.config/{{cookiecutter.plugin_name}}/

These can be overridden via environment variables:
- XDG_DATA_HOME
- XDG_STATE_HOME
- XDG_CONFIG_HOME
- {{cookiecutter.plugin_name | upper}}_DATA_DIR (explicit override)
- {{cookiecutter.plugin_name | upper}}_LOG_DIR (explicit override)
"""

import os
from pathlib import Path

PLUGIN_NAME = "{{cookiecutter.plugin_name}}"


def get_data_dir() -> Path:
    """Get the data directory for persistent storage.

    Returns:
        Path to data directory (created if needed)
    """
    # Explicit override
    if override := os.environ.get(f"{PLUGIN_NAME.upper()}_DATA_DIR"):
        path = Path(override)
    else:
        # XDG_DATA_HOME or ~/.local/share
        base = os.environ.get("XDG_DATA_HOME", Path.home() / ".local" / "share")
        path = Path(base) / PLUGIN_NAME

    path.mkdir(parents=True, exist_ok=True)
    return path


def get_log_dir() -> Path:
    """Get the log directory.

    Returns:
        Path to log directory (created if needed)
    """
    # Explicit override
    if override := os.environ.get(f"{PLUGIN_NAME.upper()}_LOG_DIR"):
        path = Path(override)
    else:
        # XDG_STATE_HOME or ~/.local/state
        base = os.environ.get("XDG_STATE_HOME", Path.home() / ".local" / "state")
        path = Path(base) / PLUGIN_NAME / "logs"

    path.mkdir(parents=True, exist_ok=True)
    return path


def get_config_dir() -> Path:
    """Get the config directory.

    Returns:
        Path to config directory (created if needed)
    """
    # XDG_CONFIG_HOME or ~/.config
    base = os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config")
    path = Path(base) / PLUGIN_NAME

    path.mkdir(parents=True, exist_ok=True)
    return path


def get_plugin_dir() -> Path:
    """Get the plugin installation directory.

    Returns:
        Path to the plugin source directory
    """
    return Path(__file__).parent.parent
