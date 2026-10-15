#!/usr/bin/env python3
"""Run npm scripts in client/ for pre-commit (cross-platform; no /bin/sh).

Uses subprocess only to execute npm with a fixed argument list; the only variable
from the environment is the resolved npm executable path (see main()).
"""

from __future__ import annotations

import shutil
import subprocess  # nosec B404  # required to spawn npm; no shell, args are fixed (lint|format|knip) + resolved PATH
import sys
from pathlib import Path

CLIENT = Path(__file__).resolve().parent.parent / "client"

# npm scripts in client/package.json that CI also runs, so a hook can catch them before GitHub does.
SCRIPTS = ("lint", "format", "knip")


def _resolved_npm() -> str | None:
    """Return absolute path to npm (prefer npm.cmd on Windows), or None if not found."""
    if sys.platform == "win32":
        w = shutil.which("npm.cmd") or shutil.which("npm")
    else:
        w = shutil.which("npm")
    if w is None:
        return None
    return str(Path(w).resolve())


def main() -> int:
    script = sys.argv[1] if len(sys.argv) > 1 else ""
    if script not in SCRIPTS:
        print(f"usage: precommit_run_npm.py {'|'.join(SCRIPTS)}", file=sys.stderr)
        return 2
    npm = _resolved_npm()
    if npm is None:
        print(
            "[ERROR] npm not found on PATH. Install Node.js (or activate nvm) so git hooks can run client lint/format/knip.",
            file=sys.stderr,
        )
        return 127
    client = str(CLIENT)
    # List-form invocation: no shell; npm from shutil.which; script is validated against SCRIPTS above.
    return subprocess.call([npm, "run", script], cwd=client)  # nosec B603


if __name__ == "__main__":
    raise SystemExit(main())
