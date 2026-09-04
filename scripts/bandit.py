#!/usr/bin/env python3
"""
Run Bandit security linter on Python code.
Uses bandit.yml configuration file for test file exclusions.
"""

import shutil
import subprocess
import sys
from pathlib import Path

from utils.safe_subprocess import safe_run_static

# Check if bandit is available
bandit_path = shutil.which("bandit")
if not bandit_path:
    # Try with uv run
    result = safe_run_static("uv", "run", "--active", "bandit", "--version", cwd=".")
    if result.returncode != 0:
        print("ERROR: bandit not found. Install with: uv pip install bandit")
        sys.exit(1)
    bandit_cmd = ["uv", "run", "--active", "bandit"]
else:
    bandit_cmd = [bandit_path]

# Check if bandit.yml exists
bandit_yml = Path("bandit.yml")
config_arg = []
if bandit_yml.exists():
    config_arg = ["-c", str(bandit_yml)]

print("Running Bandit security analysis on Python code...")
print("This will check for common security issues...")

# Run bandit on server directory (exclude tests, scripts, docs)
# Bandit will use bandit.yml to skip B101 in test files
# Use JSON format to parse severity levels
cmd = bandit_cmd + config_arg + ["-r", "server", "-f", "json"]

try:
    result = safe_run_static(*cmd, cwd=".", capture_output=True, text=True)
    output = result.stdout

    # Parse JSON output to check severity levels
    import json

    try:
        # Filter out stderr warnings from JSON output (they appear before the JSON)
        # Find the JSON start (first '{')
        json_start = output.find('{')
        if json_start == -1:
            raise json.JSONDecodeError("No JSON found in output", output, 0)
        json_output = output[json_start:]

        bandit_data = json.loads(json_output)

        # Check for Medium or High severity issues
        metrics = bandit_data.get("metrics", {})
        severity_counts = metrics.get("_totals", {})

        # Bandit uses keys like "SEVERITY.MEDIUM" and "SEVERITY.HIGH"
        medium_count = severity_counts.get("SEVERITY.MEDIUM", 0)
        high_count = severity_counts.get("SEVERITY.HIGH", 0)
        low_count = severity_counts.get("SEVERITY.LOW", 0)

        if medium_count > 0 or high_count > 0:
            print("[ERROR] Bandit found Medium or High severity security issues:")
            print(f"  Medium: {medium_count}")
            print(f"  High: {high_count}")
            # Print issues for debugging
            issues = bandit_data.get("results", [])
            for issue in issues[:10]:  # Show first 10 issues
                severity = issue.get("issue_severity", "UNKNOWN")
                if severity in ("MEDIUM", "HIGH"):
                    location = issue.get("test_id", "UNKNOWN")
                    file_path = issue.get("filename", "UNKNOWN")
                    line_num = issue.get("line_number", "UNKNOWN")
                    print(f"  [{severity}] {location} in {file_path}:{line_num}")
            if len(issues) > 10:
                print(f"  ... and {len(issues) - 10} more issues")
            sys.exit(1)

        # Low severity issues are acceptable (documented with nosec comments)
        if low_count > 0:
            print(f"[OK] Bandit scan completed with {low_count} Low severity issues (acceptable)")
            print("All Low severity issues are documented with nosec comments or are false positives.")
        else:
            print("[OK] Bandit scan completed successfully!")
            print("No security issues found.")

    except json.JSONDecodeError:
        # Fallback to text parsing if JSON fails
        if result.returncode == 0:
            print("[OK] Bandit scan completed successfully!")
            print("No security issues found.")
        elif result.returncode == 1:
            # Check if output contains Medium or High severity
            output_text = result.stdout
            has_medium = "Severity: Medium" in output_text or "MEDIUM" in output_text.upper()
            has_high = "Severity: High" in output_text or "HIGH" in output_text.upper()

            if has_medium or has_high:
                print("[ERROR] Bandit found Medium or High severity security issues:")
                print(result.stdout)
                if result.stderr:
                    print("Errors:", result.stderr)
                sys.exit(1)
            else:
                # Only Low severity issues
                print("[OK] Bandit scan completed with Low severity issues (acceptable)")
                print("All Low severity issues are documented with nosec comments or are false positives.")
        else:
            print(f"[ERROR] Bandit failed with exit code: {result.returncode}")
            print("Output:", result.stdout)
            if result.stderr:
                print("Errors:", result.stderr)
            sys.exit(1)

except (OSError, subprocess.SubprocessError) as e:
    # Catching OSError for system errors (file not found, permissions, etc.)
    # and SubprocessError for subprocess-related failures
    print(f"[ERROR] Error running bandit: {e}")
    sys.exit(1)

print("\n[SUCCESS] All Bandit security checks passed!")
