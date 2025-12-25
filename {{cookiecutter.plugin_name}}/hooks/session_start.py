#!/usr/bin/env python3
"""SessionStart hook for {{cookiecutter.plugin_display_name}}.

This hook is called when a Claude Code session starts.
Use it to inject context, load state, or perform initialization.

Input (stdin JSON):
{
    "session_id": "abc123",
    "cwd": "/path/to/project",
    "user": "username"
}

Output (stdout JSON):
{
    "status": "success",
    "context": "Optional context to inject into session"
}
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from hooks._common import (
    get_project_from_cwd,
    read_hook_input,
    setup_logging,
    success,
    write_hook_output,
)


def main() -> None:
    """Main hook entry point."""
    logger = setup_logging("session_start")

    try:
        hook_input = read_hook_input()
        logger.debug(f"Received input: {hook_input}")

        session_id = hook_input.get("session_id", "unknown")
        cwd = hook_input.get("cwd", "")
        project = get_project_from_cwd(cwd)

        logger.info(f"Session started: {session_id} in project {project}")

        # TODO: Add your session start logic here
        # Examples:
        # - Load relevant context from a database
        # - Inject project-specific instructions
        # - Initialize state for the session

        context = get_startup_context(project)

        result = success(
            message=f"{{cookiecutter.plugin_display_name}} initialized",
            context=context,
        )
        write_hook_output(result)

    except Exception as e:
        logger.exception("Error in session_start hook")
        write_hook_output({"status": "error", "error": str(e)})


def get_startup_context(project: str) -> str:
    """Get context to inject at session start.

    Args:
        project: Project name

    Returns:
        Context string (can be markdown)
    """
    # TODO: Customize this for your plugin
    # This could load from a database, file, or API
    return ""


if __name__ == "__main__":
    main()
