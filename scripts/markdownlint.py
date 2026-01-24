#!/usr/bin/env python3
"""
Run markdownlint on Markdown files.
markdownlint is a Markdown linter.
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def safe_print(text: str) -> None:
    """Print text, handling Unicode encoding errors on Windows."""
    try:
        print(text)
    except UnicodeEncodeError:
        # Fallback: write directly to stdout buffer with UTF-8 encoding
        sys.stdout.buffer.write(text.encode("utf-8", errors="replace"))
        sys.stdout.buffer.write(b"\n")


# Check if npx is available
npx_path = shutil.which("npx")
if not npx_path:
    print("ERROR: npx not found. Please install Node.js and ensure npx is available.")
    sys.exit(1)

# Parse command line arguments
parser = argparse.ArgumentParser(description="Run markdownlint on Markdown files")
parser.add_argument(
    "--fix",
    action="store_true",
    help="Automatically fix auto-fixable markdownlint issues",
)
args = parser.parse_args()

# Get project root directory
project_root = Path(__file__).parent.parent
config_file = project_root / ".markdownlint.json"

print("Running markdownlint on Markdown files...")
if args.fix:
    print("Auto-fix mode enabled - will fix auto-fixable issues...")
else:
    print("This will check for Markdown quality issues...")

# Build command arguments
cmd_args = [
    npx_path,
    "markdownlint",
    "**/*.md",
    "--ignore",
    "**/node_modules/**",
    "--ignore",
    "**/dist/**",
    "--ignore",
    "**/build/**",
    "--ignore",
    "**/.git/**",
    "--ignore",
    "**/investigations/**",
    "--ignore",
    "**/.agent-os/**",
    "--ignore",
    "**/docs/archive/**",
    "--ignore",
    "**/test-results/**",
    "--ignore",
    "**/playwright-report/**",
    "--ignore",
    "**/playwright-report-data/**",
]

# Add config file if it exists
if config_file.exists():
    cmd_args.extend(["--config", str(config_file)])

# Add --fix flag if requested
if args.fix:
    cmd_args.append("--fix")

# Run markdownlint on all .md files
# Exclude node_modules, dist, build, investigations, archive, and generated test files
result = subprocess.run(
    cmd_args,
    check=False,
    capture_output=True,
    text=True,
    encoding="utf-8",
    errors="replace",
    cwd=str(project_root),
)

if result.returncode == 0:
    print("[OK] markdownlint scan completed successfully!")
    print("No Markdown issues found.")
elif result.returncode == 1:
    print("[WARNING] markdownlint found Markdown issues:")
    if result.stdout:
        safe_print(result.stdout)
    if result.stderr:
        safe_print(f"Errors: {result.stderr}")
    print("\n[NOTE] Continuing despite warnings (non-blocking mode)")
    sys.exit(0)  # Exit successfully even with warnings
else:
    print(f"[ERROR] markdownlint failed with exit code: {result.returncode}")
    if result.stdout:
        safe_print(f"Output: {result.stdout}")
    if result.stderr:
        safe_print(f"Errors: {result.stderr}")
    print("\n[NOTE] Continuing despite errors (non-blocking mode)")
    sys.exit(0)  # Exit successfully even with errors

print("\n[SUCCESS] All markdownlint checks passed!")
