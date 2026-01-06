#!/usr/bin/env python3
"""
Run markdownlint on Markdown files.
markdownlint is a Markdown linter.
"""

import shutil
import subprocess
import sys


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

print("Running markdownlint on Markdown files...")
print("This will check for Markdown quality issues...")

# Run markdownlint on all .md files
# Exclude node_modules, dist, build, investigations, and archive directories
result = subprocess.run(
    [
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
        "investigations/**",
        "--ignore",
        "docs/archive/**",
    ],
    check=False,
    capture_output=True,
    text=True,
    encoding="utf-8",
    errors="replace",
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
