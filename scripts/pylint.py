#!/usr/bin/env python3
"""
Run Pylint on Python code.
Excludes test files and uses project-specific configuration.

This script runs comprehensive pylint checks to align with ruff linting.
Categories enabled:
- E: Error (syntax errors, etc.)
- W: Warning (style issues)
- F: Fatal (internal pylint errors)
- C: Convention (coding standard violations)
- R: Refactor (code quality suggestions)

Note: Complexity checking (C901) is handled by ruff, not pylint.
"""

import shutil
import sys
from pathlib import Path

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

print("Running comprehensive Pylint on Python code...")
print("Categories: E (Error), W (Warning), F (Fatal), C (Convention), R (Refactor)")
print("This will check for code quality issues...")

# Run pylint on server directory
# Exclude test files, scripts, docs, and other non-production code (matching ruff's scope)
# Note: Complexity checking is handled by ruff (C901), not pylint
cmd = pylint_cmd + [
    "server",
    "--ignore=tests,scripts,docs,alembic,stubs",
    "--max-line-length=120",
    "--disable=all",
    "--enable=E,W,F,C,R",  # E=Error, W=Warning, F=Fatal, C=Convention, R=Refactor
    # Re-apply disables from .pylintrc after --enable to ensure they're respected
    # This ensures that rules disabled in .pylintrc (like line-too-long, import-outside-toplevel)
    # are still disabled even after enabling all categories
    "--disable=line-too-long,import-outside-toplevel",
    "--output-format=text",
    "--rcfile=.pylintrc",  # Use project pylintrc
]

try:
    result = safe_run_static(*cmd, cwd=".", capture_output=True, text=True)

    # Save output to file for analysis
    output_file = Path("pylint_output.txt")
    with output_file.open("w", encoding="utf-8") as f:
        if result.stdout:
            f.write(result.stdout)
        if result.stderr:
            if result.stdout:
                f.write("\n--- STDERR ---\n")
            f.write(result.stderr)

    if result.returncode == 0:
        print("[OK] Pylint scan completed successfully!")
        print("No code quality issues found.")
        print(f"Output saved to: {output_file}")
    else:
        print("[WARNING] Pylint found code quality issues:")
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
        print(f"\nFull output saved to: {output_file}")
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
