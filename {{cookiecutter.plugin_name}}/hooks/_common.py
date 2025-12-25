"""Common utilities for Claude Code hooks.

Hooks receive JSON on stdin and must output JSON to stdout.
This module provides shared functionality for all hooks.
"""

import json
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


def setup_logging(hook_name: str) -> logging.Logger:
    """Set up logging for a hook.

    Args:
        hook_name: Name of the hook (for log file naming)

    Returns:
        Configured logger
    """
    # Import here to avoid circular dependency
    from {{cookiecutter.plugin_name}}.paths import get_log_dir

    log_dir = get_log_dir()
    log_file = log_dir / f"{hook_name}.log"

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_file),
        ],
    )
    return logging.getLogger(hook_name)


def read_hook_input() -> dict[str, Any]:
    """Read and parse JSON input from stdin.

    Returns:
        Parsed JSON as dictionary
    """
    try:
        return json.load(sys.stdin)
    except json.JSONDecodeError as e:
        return {"error": f"Invalid JSON input: {e}"}


def write_hook_output(result: dict[str, Any]) -> None:
    """Write JSON output to stdout.

    Args:
        result: Result dictionary to output
    """
    json.dump(result, sys.stdout)
    sys.stdout.flush()


def success(message: str = "", **kwargs) -> dict[str, Any]:
    """Create a success response.

    Args:
        message: Optional success message
        **kwargs: Additional fields to include

    Returns:
        Success response dictionary
    """
    result = {"status": "success"}
    if message:
        result["message"] = message
    result.update(kwargs)
    return result


def error(message: str, **kwargs) -> dict[str, Any]:
    """Create an error response.

    Args:
        message: Error message
        **kwargs: Additional fields to include

    Returns:
        Error response dictionary
    """
    result = {"status": "error", "error": message}
    result.update(kwargs)
    return result


def get_project_from_cwd(cwd: str) -> str:
    """Extract project name from working directory.

    Args:
        cwd: Current working directory path

    Returns:
        Project name (last component of path)
    """
    return Path(cwd).name


def timestamp() -> str:
    """Get current ISO timestamp.

    Returns:
        ISO format timestamp string
    """
    return datetime.now().isoformat()
