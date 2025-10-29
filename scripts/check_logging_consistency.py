#!/usr/bin/env python3
"""
Logging Consistency Checker for MythosMUD.

This script checks for improper usage of logging.getLogger() in service files
that should be using get_logger() from server.logging_config instead.

As documented in the Cultes des Goules, proper logging practices are essential
for maintaining the delicate balance between the mundane and the eldritch forces
that lurk in the shadows of our world.
"""

import re
import sys
from pathlib import Path


def check_file_for_logging_issues(file_path: Path) -> list[str]:
    """
    Check a single file for logging consistency issues.

    Args:
        file_path: Path to the file to check

    Returns:
        List of issues found in the file
    """
    issues = []

    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()
            lines = content.split("\n")

        # Check for logging.getLogger() usage
        for i, line in enumerate(lines, 1):
            if re.search(r"logging\.getLogger\(", line):
                # Check if this file imports get_logger
                if "from ..logging.enhanced_logging_config import get_logger" not in content:
                    issues.append(f"Line {i}: Uses logging.getLogger() but doesn't import get_logger()")

        # Check for context parameter usage with standard logger
        for i, line in enumerate(lines, 1):
            if re.search(r"logger\.(info|debug|warning|error|critical)\([^)]*context\s*=", line):
                if "from ..logging.enhanced_logging_config import get_logger" not in content:
                    issues.append(f"Line {i}: Uses context parameter but doesn't import get_logger()")

    except Exception as e:
        issues.append(f"Error reading file: {e}")

    return issues


def main():
    """Main function to check all service files for logging consistency."""
    project_root = Path(__file__).parent.parent
    server_dir = project_root / "server"

    # Files to check (service files and core modules)
    patterns_to_check = ["server/services/*.py", "server/npc/*.py", "server/game/*.py", "server/utils/*.py"]

    all_issues = []

    for pattern in patterns_to_check:
        for file_path in server_dir.glob(pattern.replace("server/", "")):
            if file_path.is_file() and file_path.suffix == ".py":
                issues = check_file_for_logging_issues(file_path)
                if issues:
                    all_issues.append(f"\n{file_path.relative_to(project_root)}:")
                    all_issues.extend([f"  {issue}" for issue in issues])

    if all_issues:
        print("LOGGING CONSISTENCY ISSUES FOUND:")
        for issue in all_issues:
            print(issue)
        print("\nSOLUTION:")
        print("Replace 'logging.getLogger(__name__)' with 'get_logger(__name__)'")
        print("Add import: 'from ..logging.enhanced_logging_config import get_logger'")
        print("Remove import: 'import logging'")
        sys.exit(1)
    else:
        print("All service files use proper logging configuration!")
        sys.exit(0)


if __name__ == "__main__":
    main()
