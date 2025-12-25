"""Pytest fixtures for {{cookiecutter.plugin_display_name}}."""

import os
import tempfile
from pathlib import Path

import pytest


@pytest.fixture
def temp_dir():
    """Create a temporary directory for test data."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def mock_env(temp_dir, monkeypatch):
    """Set up environment variables for isolated testing."""
    # Override XDG paths to use temp directory
    monkeypatch.setenv("XDG_DATA_HOME", str(temp_dir / "data"))
    monkeypatch.setenv("XDG_STATE_HOME", str(temp_dir / "state"))
    monkeypatch.setenv("XDG_CONFIG_HOME", str(temp_dir / "config"))

    # Override plugin-specific paths
    monkeypatch.setenv("{{cookiecutter.plugin_name | upper}}_DATA_DIR", str(temp_dir / "plugin_data"))
    monkeypatch.setenv("{{cookiecutter.plugin_name | upper}}_LOG_DIR", str(temp_dir / "plugin_logs"))

    yield temp_dir


@pytest.fixture
def mock_claude_settings(temp_dir, monkeypatch):
    """Create a mock Claude Code settings environment."""
    claude_dir = temp_dir / ".claude"
    claude_dir.mkdir(parents=True)

    # Create empty settings.json
    settings_path = claude_dir / "settings.json"
    settings_path.write_text("{}")

    # Monkey-patch home directory for settings lookup
    # Note: This requires adjusting the register.py to use a configurable path
    monkeypatch.setenv("HOME", str(temp_dir))

    return settings_path
