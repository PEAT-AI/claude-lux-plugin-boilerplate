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


if __name__ == "__main__":
    main()
