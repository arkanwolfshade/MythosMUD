#!/usr/bin/env python3
"""
Pre-commit hook to check if .codacy/codacy.yaml has been modified.
Warns if the file was changed, as it should be manually managed.
"""

import sys
from pathlib import Path

CODACY_YAML = Path(".codacy/codacy.yaml")


def check_codacy_yaml():
    """Check if codacy.yaml exists and contains required tools."""
    if not CODACY_YAML.exists():
        print("⚠️  WARNING: .codacy/codacy.yaml not found!")
        return 0  # Don't fail, just warn

    content = CODACY_YAML.read_text(encoding="utf-8")

    # Check for required tools (lizard is critical - manually added)
    required_tools = {
        "lizard@1.17.31": "Manually added for NLOC/complexity analysis",
        "semgrep": "Security scanning tool",
        "eslint": "JavaScript/TypeScript linting",
        "ruff": "Python linter/formatter (replaces flake8, isort, black)",
        "bandit": "Python security analysis",
        "node@": "Node.js runtime (version may vary)",
    }
    missing_tools = []

    for tool, description in required_tools.items():
        if tool not in content:
            missing_tools.append(f"{tool} ({description})")

    if missing_tools:
        print("⚠️  WARNING: .codacy/codacy.yaml may have been auto-modified!")
        print(f"   Missing expected tools: {', '.join(missing_tools)}")
        print("   This file should be manually managed.")
        print("   Check if Codacy extension auto-discovery is disabled.")
        print("   Restore from git if needed: git checkout .codacy/codacy.yaml")
        return 1  # Fail the commit to draw attention

    # Check if Python version was downgraded (common auto-modification issue)
    if "python@3.11.11" in content and "python@3.12.10" not in content:
        print("⚠️  WARNING: .codacy/codacy.yaml has wrong Python version (3.11.11 instead of 3.12.10)")
        print("   This file may have been auto-modified by Codacy extension.")
        print("   Project uses Python 3.12.10 - update the file manually.")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(check_codacy_yaml())
