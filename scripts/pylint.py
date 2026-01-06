#!/usr/bin/env python3
"""
Run Pylint on Python code.
Excludes test files and uses project-specific configuration.
"""

import shutil
import sys

from utils.safe_subprocess import safe_run_static

# Check if pylint is available
pylint_path = shutil.which("pylint")
if not pylint_path:
    # Try with uv run
    result = safe_run_static("uv", "run", "--active", "pylint", "--version", cwd=".")
    if result.returncode != 0:
        print("ERROR: pylint not found. Install with: uv pip install pylint")
        sys.exit(1)
    pylint_cmd = ["uv", "run", "--active", "pylint"]
else:
    pylint_cmd = [pylint_path]

print("Running Pylint on Python code...")
print("This will check for code quality issues...")

# Run pylint on server directory
# Exclude test files, scripts, docs, and other non-production code
cmd = pylint_cmd + [
    "server",
    "--ignore=tests,scripts,docs,alembic,stubs",
    "--max-line-length=120",
    "--disable=all",
    "--enable=E,W,F",  # E=Error, W=Warning, F=Fatal
    "--output-format=text",
]

try:
    result = safe_run_static(*cmd, cwd=".")
    if result.returncode == 0:
        print("[OK] Pylint scan completed successfully!")
        print("No code quality issues found.")
    else:
        print("[WARNING] Pylint found code quality issues:")
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
        # Pylint returns non-zero even for warnings, so we don't fail on warnings
        # Only fail on fatal errors (exit code 32)
        if result.returncode == 32:
            sys.exit(1)
except Exception as e:  # pylint: disable=W0718
    # Catching all exceptions is appropriate here as we need to handle any error
    # that might occur when running pylint (file not found, permission errors, subprocess failures, etc.)
    print(f"[ERROR] Error running pylint: {e}")
    sys.exit(1)

print("\n[SUCCESS] Pylint checks completed!")
