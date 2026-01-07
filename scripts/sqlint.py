#!/usr/bin/env python3
"""
Run SQLint on SQL files.
SQLint provides additional SQL linting checks.

NOTE: sqlint is not installed by default due to dependency conflicts (requires click==7.0,
but project requires click>=8.1.8). Use sqlfluff instead for SQL linting, which is more
comprehensive and actively maintained.
"""

import shutil
import sys
from pathlib import Path

from utils.safe_subprocess import safe_run_static

# Check if sqlint is available
sqlint_path = shutil.which("sqlint")
if not sqlint_path:
    # Try with uv run
    result = safe_run_static("uv", "run", "--active", "sqlint", "--version", cwd=".")
    if result.returncode != 0:
        print("WARNING: sqlint not found.")
        print("sqlint is not installed due to dependency conflicts (requires click==7.0).")
        print("Use 'sqlfluff' instead for SQL linting: make sqlfluff")
        print("Skipping sqlint checks...")
        sys.exit(0)  # Exit successfully - sqlint is optional
    sqlint_cmd = ["uv", "run", "--active", "sqlint"]
else:
    sqlint_cmd = [sqlint_path]

print("Running SQLint on SQL files...")
print("This will check for SQL quality issues...")

# Find all SQL files in db/ and data/db/ directories
sql_dirs = ["db", "data/db"]
sql_files = []
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
        result = safe_run_static(*cmd, cwd=".")
        if result.returncode != 0:
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
