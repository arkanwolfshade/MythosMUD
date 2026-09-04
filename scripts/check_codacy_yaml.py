#!/usr/bin/env python3
"""
Advisory check for .codacy/codacy.yaml (pre-commit).

Codacy (extension or CLI) often overwrites this file and strips it to a single tool.
This hook only warns when the file is missing or invalid; it never blocks the commit.
To restore: git checkout .codacy/codacy.yaml
"""

import sys
from pathlib import Path

# Pre-commit runs from repo root
REPO_ROOT = Path.cwd()
CODACY_YAML = REPO_ROOT / ".codacy" / "codacy.yaml"

REQUIRED_TOOLS = {
    "lizard@1.17.31": "NLOC/complexity analysis",
    "semgrep": "Security scanning",
    "eslint": "JavaScript/TypeScript linting",
    "ruff": "Python linter/formatter",
    "bandit": "Python security analysis",
    "node@": "Node.js runtime",
}


def _content_is_valid(content: str) -> tuple[bool, list[str]]:
    """Return (valid, list of reasons if invalid)."""
    reasons = []
    for tool, _ in REQUIRED_TOOLS.items():
        if tool not in content:
            reasons.append(f"missing {tool}")
    if "python@3.11.11" in content and "python@3.12.10" not in content:
        reasons.append("wrong Python version (3.11.11 instead of 3.12.10)")
    return (len(reasons) == 0, reasons)


def check_codacy_yaml() -> int:
    """Warn if .codacy/codacy.yaml is missing or invalid; never fail the commit."""
    if not CODACY_YAML.exists():
        print("[check_codacy_yaml] .codacy/codacy.yaml not found. Restore with: git checkout .codacy/codacy.yaml")
        return 0

    content = CODACY_YAML.read_text(encoding="utf-8")
    valid, reasons = _content_is_valid(content)
    if valid:
        return 0

    print(
        "[check_codacy_yaml] .codacy/codacy.yaml may have been overwritten by Codacy"
        f" ({', '.join(reasons)}). Restore with: git checkout .codacy/codacy.yaml"
    )
    return 0


if __name__ == "__main__":
    sys.exit(check_codacy_yaml())
