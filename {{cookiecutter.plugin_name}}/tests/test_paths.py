"""Tests for the paths module."""

from pathlib import Path


def test_get_data_dir(mock_env):
    """Test data directory creation."""
    from {{cookiecutter.plugin_name}}.paths import get_data_dir

    data_dir = get_data_dir()
    assert data_dir.exists()
    assert data_dir.is_dir()


def test_get_log_dir(mock_env):
    """Test log directory creation."""
    from {{cookiecutter.plugin_name}}.paths import get_log_dir

    log_dir = get_log_dir()
    assert log_dir.exists()
    assert log_dir.is_dir()


def test_get_config_dir(mock_env):
    """Test config directory creation."""
    from {{cookiecutter.plugin_name}}.paths import get_config_dir

    config_dir = get_config_dir()
    assert config_dir.exists()
    assert config_dir.is_dir()


def test_get_plugin_dir():
    """Test plugin directory detection."""
    from {{cookiecutter.plugin_name}}.paths import get_plugin_dir

    plugin_dir = get_plugin_dir()
    assert plugin_dir.exists()
    assert (plugin_dir / "pyproject.toml").exists() or (plugin_dir / "plugin.json").exists()


def test_data_dir_override(temp_dir, monkeypatch):
    """Test explicit data directory override."""
    from {{cookiecutter.plugin_name}}.paths import get_data_dir

    custom_dir = temp_dir / "custom_data"
    monkeypatch.setenv("{{cookiecutter.plugin_name | upper}}_DATA_DIR", str(custom_dir))

    data_dir = get_data_dir()
    assert data_dir == custom_dir
    assert data_dir.exists()


def test_log_dir_override(temp_dir, monkeypatch):
    """Test explicit log directory override."""
    from {{cookiecutter.plugin_name}}.paths import get_log_dir

    custom_dir = temp_dir / "custom_logs"
    monkeypatch.setenv("{{cookiecutter.plugin_name | upper}}_LOG_DIR", str(custom_dir))

    log_dir = get_log_dir()
    assert log_dir == custom_dir
    assert log_dir.exists()
