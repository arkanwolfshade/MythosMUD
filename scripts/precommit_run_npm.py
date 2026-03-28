#!/usr/bin/env python3
"""Run npm scripts in client/ for pre-commit (cross-platform; no /bin/sh)."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

CLIENT = Path(__file__).resolve().parent.parent / "client"


def main() -> int:
    script = sys.argv[1] if len(sys.argv) > 1 else ""
    if script not in ("lint", "format"):
        print("usage: precommit_run_npm.py lint|format", file=sys.stderr)
        return 2
    if shutil.which("npm") is None and shutil.which("npm.cmd") is None:
        print(
            "[ERROR] npm not found on PATH. Install Node.js (or activate nvm) so git hooks can run client lint/format.",
            file=sys.stderr,
        )
        return 127
    client = str(CLIENT)
    # Windows: npm is npm.cmd; list-form CreateProcess cannot spawn it without cmd.exe.
    if sys.platform == "win32":
        # Literal "cmd.exe" (PATH resolution); avoids ComSpec env false positives from static scanners.
        if script == "lint":
            return subprocess.call(["cmd.exe", "/c", "npm run lint"], cwd=client)
        return subprocess.call(["cmd.exe", "/c", "npm run format"], cwd=client)
    if script == "lint":
        return subprocess.call(["npm", "run", "lint"], cwd=client)
    return subprocess.call(["npm", "run", "format"], cwd=client)


if __name__ == "__main__":
    raise SystemExit(main())
