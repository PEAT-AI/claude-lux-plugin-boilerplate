#!/usr/bin/env python3
"""Register {{cookiecutter.plugin_display_name}} with Claude Code.

This script adds the plugin's hooks to Claude Code's settings.json.
Run it with --unregister to remove the hooks.
"""

import argparse
import json
import sys
from pathlib import Path


def get_settings_path() -> Path:
    """Get the Claude Code settings path."""
    return Path.home() / ".claude" / "settings.json"


def get_plugin_dir() -> Path:
    """Get the plugin directory."""
    return Path(__file__).parent.parent


def load_plugin_manifest() -> dict:
    """Load the plugin.json manifest."""
    manifest_path = get_plugin_dir() / "plugin.json"
    if not manifest_path.exists():
        print(f"Error: plugin.json not found at {manifest_path}")
        sys.exit(1)
    return json.loads(manifest_path.read_text())


def load_settings() -> dict:
    """Load existing Claude Code settings."""
    settings_path = get_settings_path()
    if settings_path.exists():
        return json.loads(settings_path.read_text())
    return {}


def save_settings(settings: dict) -> None:
    """Save Claude Code settings."""
    settings_path = get_settings_path()
    settings_path.parent.mkdir(parents=True, exist_ok=True)
    settings_path.write_text(json.dumps(settings, indent=2))


def register() -> None:
    """Register plugin hooks with Claude Code."""
    manifest = load_plugin_manifest()
    settings = load_settings()
    plugin_dir = get_plugin_dir()

    # Get or create hooks section
    hooks = settings.setdefault("hooks", {})

    # Register each hook
    hooks_config = manifest.get("hooks", {})
    registered = []

    for hook_type, hook_path in hooks_config.items():
        absolute_path = str(plugin_dir / hook_path)

        # Get or create hook list for this type
        hook_list = hooks.setdefault(hook_type, [])

        # Add if not already registered
        if absolute_path not in hook_list:
            hook_list.append(absolute_path)
            registered.append(hook_type)

    save_settings(settings)

    if registered:
        print(f"Registered hooks: {', '.join(registered)}")
    else:
        print("All hooks already registered.")
    print(f"Settings saved to: {get_settings_path()}")


def unregister() -> None:
    """Remove plugin hooks from Claude Code."""
    manifest = load_plugin_manifest()
    settings = load_settings()
    plugin_dir = get_plugin_dir()

    hooks = settings.get("hooks", {})
    hooks_config = manifest.get("hooks", {})
    removed = []

    for hook_type, hook_path in hooks_config.items():
        absolute_path = str(plugin_dir / hook_path)

        if hook_type in hooks and absolute_path in hooks[hook_type]:
            hooks[hook_type].remove(absolute_path)
            removed.append(hook_type)

            # Clean up empty hook lists
            if not hooks[hook_type]:
                del hooks[hook_type]

    save_settings(settings)

    if removed:
        print(f"Removed hooks: {', '.join(removed)}")
    else:
        print("No hooks to remove.")


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Register {{cookiecutter.plugin_display_name}} with Claude Code"
    )
    parser.add_argument(
        "--unregister",
        action="store_true",
        help="Remove hooks instead of adding them",
    )
    args = parser.parse_args()

    if args.unregister:
        unregister()
    else:
        register()


if __name__ == "__main__":
    main()
