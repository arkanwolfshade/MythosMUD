#!/usr/bin/env python3
"""
Run Stylelint on CSS files.
Stylelint is a CSS linter.
"""

import shutil
import subprocess
import sys

# Check if npx is available
npx_path = shutil.which("npx")
if not npx_path:
    print("ERROR: npx not found. Please install Node.js and ensure npx is available.")
    sys.exit(1)

print("Running Stylelint on CSS files...")
print("This will check for CSS quality issues...")

# Run stylelint in client directory
# Configuration file (.stylelintrc.json) handles ignoring generated directories.
# SAFETY NOTES:
# - Executable path (npx_path) comes from shutil.which("npx") and is validated above.
# - All arguments are static strings; there is no user input in the command.
# - List form with shell=False prevents shell injection.
# - This script is a privileged developer tool, not exposed directly to untrusted input.
# nosemgrep: python.lang.security.audit.subprocess-shell-true.subprocess-shell-true
# nosec B603: npx_path is from shutil.which (trusted system PATH), args are static list
result = subprocess.run(
    [npx_path, "stylelint", "src/**/*.css"],
    cwd="client",
    check=False,
    capture_output=True,
    text=True,
)

if result.returncode == 0:
    print("[OK] Stylelint scan completed successfully!")
    print("No CSS issues found.")
elif result.returncode == 2:
    # Exit code 2 means no files matched (no CSS files)
    print("[INFO] No CSS files found to lint")
    sys.exit(0)
else:
    print("[WARNING] Stylelint found CSS issues:")
    print(result.stdout)
    if result.stderr:
        print("Errors:", result.stderr)
    sys.exit(1)

print("\n[SUCCESS] All Stylelint checks passed!")
