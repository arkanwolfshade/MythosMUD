#!/usr/bin/env python3
"""
Run SQLint on SQL files.
SQLint provides additional SQL linting checks.

NOTE: sqlint is not installed by default due to dependency conflicts (requires click==7.0,
but project requires click>=8.1.8). sqlint<=0.2.4 also fails to import on Python 3.12+.
Use sqlfluff instead for SQL linting, which is more comprehensive and actively maintained.
"""

import shutil
import sys
from pathlib import Path

from utils.safe_subprocess import safe_run_static


def _is_tool_crash(result_stdout: str | None, result_stderr: str | None) -> bool:
    """Return True when sqlint failed to start rather than reporting SQL issues."""
    combined = f"{result_stdout or ''}{result_stderr or ''}"
    return "Traceback" in combined or "ImportError" in combined


def _skip_sqlint(reason: str) -> None:
    print(f"WARNING: {reason}")
    print("sqlint is optional; use 'make sqlfluff' for SQL linting.")
    print("Skipping sqlint checks...")
    sys.exit(0)


def _resolve_sqlint_cmd() -> list[str] | None:
    """Return sqlint command argv when the tool is installed and runnable."""
    candidates: list[list[str]] = []
    sqlint_path = shutil.which("sqlint")
    if sqlint_path:
        candidates.append([sqlint_path])
    candidates.append(["uv", "run", "--active", "sqlint"])

    for cmd in candidates:
        result = safe_run_static(*cmd, "--version", cwd=".", capture_output=True, text=True)
        if result.returncode == 0 and not _is_tool_crash(result.stdout, result.stderr):
            return cmd
    return None


sqlint_cmd = _resolve_sqlint_cmd()
if sqlint_cmd is None:
    _skip_sqlint(
        "sqlint is unavailable or incompatible with this Python version "
        "(known issue: sqlint<=0.2.4 breaks on Python 3.12+)."
    )

print("Running SQLint on SQL files...")
print("This will check for SQL quality issues...")

# Find all SQL files in db/ and data/db/ directories
sql_dirs = ["db", "data/db"]
sql_files: list[Path] = []
for sql_dir in sql_dirs:
    sql_path = Path(sql_dir)
    if sql_path.exists():
        sql_files.extend(sql_path.rglob("*.sql"))

if not sql_files:
    print("[WARNING] No SQL files found in db/ or data/db/ directories")
    sys.exit(0)

# Run sqlint on all SQL files
success = True
for sql_file in sql_files:
    cmd = sqlint_cmd + [str(sql_file)]
    try:
        result = safe_run_static(*cmd, cwd=".", capture_output=True, text=True)
        if result.returncode != 0:
            if _is_tool_crash(result.stdout, result.stderr):
                _skip_sqlint("sqlint crashed while linting; tool is incompatible with this environment.")
            print(f"[WARNING] SQLint found issues in {sql_file}:")
            print(result.stdout)
            if result.stderr:
                print("Errors:", result.stderr)
            success = False
    except Exception as e:
        print(f"[ERROR] Error running sqlint on {sql_file}: {e}")
        success = False

if not success:
    sys.exit(1)

print("\n[SUCCESS] All SQLint checks passed!")
