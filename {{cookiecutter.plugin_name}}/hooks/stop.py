#!/usr/bin/env python3
"""Stop hook for {{cookiecutter.plugin_display_name}}.

This hook is called when a Claude Code session ends normally.
Use it to save state, generate summaries, or clean up.

Input (stdin JSON):
{
    "session_id": "abc123",
    "cwd": "/path/to/project",
    "transcript": "full conversation transcript..."
}

Output (stdout JSON):
{
    "status": "success"
}
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from {{cookiecutter.plugin_name}}.hooks import (
    get_project_from_cwd,
    read_hook_input,
    setup_logging,
    success,
    write_hook_output,
)


def main() -> None:
    """Main hook entry point."""
    logger = setup_logging("stop")

    try:
        hook_input = read_hook_input()
        logger.debug(f"Received stop hook input")

        session_id = hook_input.get("session_id", "unknown")
        cwd = hook_input.get("cwd", "")
        transcript = hook_input.get("transcript", "")
        project = get_project_from_cwd(cwd)

        logger.info(f"Session ended: {session_id} in project {project}")

        # TODO: Add your session end logic here
        # Examples:
        # - Save session summary
        # - Process transcript for learnings
        # - Clean up temporary state

        process_session_end(
            session_id=session_id,
            project=project,
            transcript=transcript,
        )

        write_hook_output(success(message="Session ended"))

    except Exception as e:
        logger.exception("Error in stop hook")
        # Don't fail on hook errors
        write_hook_output(success())


def process_session_end(
    session_id: str,
    project: str,
    transcript: str,
) -> None:
    """Process session end event.

    Args:
        session_id: Session ID that ended
        project: Project name
        transcript: Full conversation transcript
    """
    # TODO: Customize this for your plugin
    # This could:
    # - Generate a session summary
    # - Extract and store learnings
    # - Update metrics
    pass


if __name__ == "__main__":
    main()
