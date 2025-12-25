#!/usr/bin/env python3
"""Post-generation hook for cookiecutter.

This runs after the project is generated to perform any cleanup
or additional setup.
"""

import os
import stat
from pathlib import Path


def make_executable(path: Path) -> None:
    """Make a file executable."""
    if path.exists():
        st = os.stat(path)
        os.chmod(path, st.st_mode | stat.S_IEXEC)


def main():
    """Run post-generation tasks."""
    project_dir = Path.cwd()

    # Make bin/run executable
    run_script = project_dir / "bin" / "run"
    make_executable(run_script)

    # Make hook scripts executable
    hooks_dir = project_dir / "hooks"
    if hooks_dir.exists():
        for hook in hooks_dir.glob("*.py"):
            if not hook.name.startswith("_"):
                make_executable(hook)

    print(f"\n✓ Created {{cookiecutter.plugin_name}} plugin")
    print(f"\nNext steps:")
    print(f"  cd {{cookiecutter.plugin_name}}")
    print(f"  make install")
    print(f"  source .venv/bin/activate")
    print(f"  {{cookiecutter.plugin_name}} status")


if __name__ == "__main__":
    main()
