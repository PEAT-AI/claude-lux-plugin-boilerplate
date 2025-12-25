"""Tests for the CLI module."""

from click.testing import CliRunner

from {{cookiecutter.plugin_name}}.cli import main


def test_cli_help():
    """Test that --help works."""
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "{{cookiecutter.plugin_display_name}}" in result.output


def test_cli_version():
    """Test that --version works."""
    runner = CliRunner()
    result = runner.invoke(main, ["--version"])
    assert result.exit_code == 0
    assert "0.1.0" in result.output


def test_status_command(mock_env):
    """Test the status command."""
    runner = CliRunner()
    result = runner.invoke(main, ["status"])
    assert result.exit_code == 0
    assert "{{cookiecutter.plugin_display_name}}" in result.output
    assert "Data directory" in result.output
