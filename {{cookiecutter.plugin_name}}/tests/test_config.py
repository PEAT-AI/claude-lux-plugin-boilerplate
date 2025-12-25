"""Tests for the config module."""


def test_load_config(mock_env):
    """Test loading full config."""
    from {{cookiecutter.plugin_name}}.config import load_config

    config = load_config()
    assert "data_dir" in config
    assert "verbose" in config


def test_load_config_verbose_flag(mock_env, monkeypatch):
    """Test verbose flag parsing."""
    from {{cookiecutter.plugin_name}}.config import load_config

    monkeypatch.setenv("{{cookiecutter.plugin_name | upper}}_VERBOSE", "true")
    config = load_config()
    assert config["verbose"] is True
