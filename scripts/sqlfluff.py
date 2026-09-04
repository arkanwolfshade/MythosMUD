#!/usr/bin/env python3
"""
Run SQLFluff on SQL files.
SQLFluff provides linting and formatting for SQL code.
"""

import shutil
import sys
from pathlib import Path

from utils.safe_subprocess import safe_run_static

# Check if sqlfluff is available
sqlfluff_path = shutil.which("sqlfluff")
if not sqlfluff_path:
    # Try with uv run
    result = safe_run_static("uv", "run", "--active", "sqlfluff", "--version", cwd=".")
    if result.returncode != 0:
        print("ERROR: sqlfluff not found. Install with: uv pip install sqlfluff")
        sys.exit(1)
    sqlfluff_cmd = ["uv", "run", "--active", "sqlfluff"]
else:
    sqlfluff_cmd = [sqlfluff_path]

print("Running SQLFluff on SQL files...")
print("This will check for SQL style and quality issues...")

# Find all SQL files in db/ and data/db/ directories
sql_dirs = ["db", "data/db"]
sql_files = []
exclude_patterns = [
    "db/databases/databases.sql",  # Contains psql meta-commands (\connect, \gexec)
    "db/mythos_dev_ddl.sql",  # Large generated DDL, skipped by SQLFluff
    "db/mythos_unit_ddl.sql",
    "db/mythos_e2e_ddl.sql",
    "data/db/",  # pg_dump DML (COPY ... FROM stdin); not parseable as SQL by sqlfluff
]
for sql_dir in sql_dirs:
    sql_path = Path(sql_dir)
    if sql_path.exists():
        for sql_file in sql_path.rglob("*.sql"):
            # Skip excluded files
            RELATIVE_PATH = str(sql_file).replace("\\", "/")
            if not any(RELATIVE_PATH.endswith(pattern) or pattern in RELATIVE_PATH for pattern in exclude_patterns):
                sql_files.append(sql_file)

if not sql_files:
    print("[WARNING] No SQL files found in db/ or data/db/ directories")
    sys.exit(0)

# Run sqlfluff on all SQL files
# Use PostgreSQL dialect and config file if it exists
cmd = sqlfluff_cmd + ["lint", "--dialect", "postgres"]
config_file = Path(".sqlfluff")
if config_file.exists():
    cmd.extend(["--config", str(config_file)])
cmd.extend([str(f) for f in sql_files])

try:
    result = safe_run_static(*cmd, cwd=".")
    if result.returncode == 0:
        print("[OK] SQLFluff scan completed successfully!")
        print("No SQL style issues found.")
    else:
        print("[WARNING] SQLFluff found SQL style issues:")
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
        sys.exit(1)
except (ValueError, OSError) as e:
    # ValueError: path/command validation in safe_run_static; OSError: executable not found, etc.
    print(f"[ERROR] Error running sqlfluff: {e}")
    sys.exit(1)

print("\n[SUCCESS] All SQLFluff checks passed!")
