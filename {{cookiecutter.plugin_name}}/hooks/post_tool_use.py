#!/usr/bin/env python3
"""PostToolUse hook for {{cookiecutter.plugin_display_name}}.

This hook is called after Claude executes a tool (Read, Edit, Bash, etc.).
Use it to capture, log, or process tool execution data.

Input (stdin JSON):
{
    "session_id": "abc123",
    "cwd": "/path/to/project",
    "tool_name": "Read",
    "tool_input": {"file_path": "/path/to/file.py"},
    "tool_output": "file contents..."
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

from hooks._common import (
    get_project_from_cwd,
    read_hook_input,
    setup_logging,
    success,
    timestamp,
    write_hook_output,
)

# Tools to skip processing (low-value or meta tools)
SKIP_TOOLS = {
    "TodoWrite",
    "AskUserQuestion",
    "ListMcpResourcesTool",
    "Skill",
    "SlashCommand",
}


def main() -> None:
    """Main hook entry point."""
    logger = setup_logging("post_tool_use")

    try:
        hook_input = read_hook_input()

        tool_name = hook_input.get("tool_name", "")
        session_id = hook_input.get("session_id", "unknown")
        cwd = hook_input.get("cwd", "")

        # Skip low-value tools
        if tool_name in SKIP_TOOLS:
            logger.debug(f"Skipping tool: {tool_name}")
            write_hook_output(success())
            return

        project = get_project_from_cwd(cwd)
        tool_input = hook_input.get("tool_input", {})
        tool_output = hook_input.get("tool_output", "")

        logger.info(f"Tool executed: {tool_name} in {project}")

        # TODO: Add your post-tool processing here
        # Examples:
        # - Log tool usage to a database
        # - Extract learnings from tool output
        # - Update project state based on actions

        process_tool_execution(
            session_id=session_id,
            project=project,
            tool_name=tool_name,
            tool_input=tool_input,
            tool_output=tool_output,
        )

        write_hook_output(success())

    except Exception as e:
        logger.exception("Error in post_tool_use hook")
        # Don't block Claude on hook errors
        write_hook_output(success())


def process_tool_execution(
    session_id: str,
    project: str,
    tool_name: str,
    tool_input: dict,
    tool_output: str,
) -> None:
    """Process a tool execution event.

    Args:
        session_id: Current session ID
        project: Project name
        tool_name: Name of the tool that was executed
        tool_input: Tool input parameters
        tool_output: Tool output/result
    """
    # TODO: Customize this for your plugin
    # This could:
    # - Append to an event log
    # - Send to an external service
    # - Update local state
    pass


if __name__ == "__main__":
    main()
