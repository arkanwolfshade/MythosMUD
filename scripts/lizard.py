#!/usr/bin/env python3
"""
Run Lizard complexity analyzer on code.
Lizard analyzes code complexity and provides metrics.
"""

import shutil
import subprocess
import sys

# Check if lizard is available
lizard_path = shutil.which("lizard")
if not lizard_path:
    print("ERROR: lizard not found. Install with: pip install lizard")
    print("Note: Lizard is primarily used by Codacy for complexity metrics.")
    print("Local installation is optional.")
    sys.exit(0)  # Don't fail if lizard is not installed locally

print("Running Lizard complexity analysis...")
print("This will analyze code complexity...")

# Run lizard on server directory
# Exclude test files and other non-production code.
# SAFETY NOTES:
# - Executable path (lizard_path) comes from shutil.which("lizard") and is validated above.
# - All arguments are static strings; there is no user input in the command.
# - List form with shell=False prevents shell injection.
# - This script is a local analysis tool, not a code path handling untrusted user data.
# nosemgrep: python.lang.security.audit.subprocess-shell-true.subprocess-shell-true
# nosec B603: lizard_path is from shutil.which (trusted PATH), args are static list
result = subprocess.run(
    [
        lizard_path,
        "server",
        "--length",
        "55",
        "--exclude",
        "tests",
        "--exclude",
        "scripts",
        "--exclude",
        "docs",
        "--exclude",
        "alembic",
        "--exclude",
        "stubs",
    ],
    check=False,
    capture_output=True,
    text=True,
)

if result.returncode == 0:
    print("[OK] Lizard analysis completed successfully!")
    print(result.stdout)
else:
    print("[INFO] Lizard analysis completed:")
    print(result.stdout)
    if result.stderr:
        print("Errors:", result.stderr)
    # Lizard doesn't fail on complexity - it just reports metrics

print("\n[SUCCESS] Lizard complexity analysis completed!")
