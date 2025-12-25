"""CLI entry point for {{cookiecutter.plugin_display_name}}."""

import click

from . import __version__


@click.group()
@click.version_option(version=__version__)
@click.option("-v", "--verbose", is_flag=True, help="Enable verbose output")
@click.pass_context
def main(ctx: click.Context, verbose: bool) -> None:
    """{{cookiecutter.plugin_display_name}} - {{cookiecutter.plugin_description}}"""
    ctx.ensure_object(dict)
    ctx.obj["verbose"] = verbose


@main.command()
@click.pass_context
def status(ctx: click.Context) -> None:
    """Show plugin status and configuration."""
    from .config import load_config
    from .paths import get_data_dir, get_log_dir

    config = load_config()
    click.echo(f"{{cookiecutter.plugin_display_name}} v{__version__}")
    click.echo(f"Data directory: {get_data_dir()}")
    click.echo(f"Log directory: {get_log_dir()}")
    click.echo(f"Config loaded: {config is not None}")


@main.command()
@click.argument("message")
@click.pass_context
def echo(ctx: click.Context, message: str) -> None:
    """Echo a message (example command)."""
    verbose = ctx.obj.get("verbose", False)
    if verbose:
        click.echo(f"[verbose] Echoing message...")
    click.echo(message)


@main.command()
@click.pass_context
def test_connection(ctx: click.Context) -> None:
    """Test API connection (if configured)."""
    {%- if cookiecutter.include_api_client %}
    from .client import test_api_connection
    from .config import load_config

    config = load_config()
    if not config.get("api_key"):
        click.echo("No API key configured. Set it in .env or environment variables.")
        raise SystemExit(1)

    if test_api_connection(config["api_key"]):
        click.echo("API connection successful!")
    else:
        click.echo("API connection failed.")
        raise SystemExit(1)
    {%- else %}
    click.echo("API client not included in this plugin.")
    {%- endif %}


if __name__ == "__main__":
    main()
