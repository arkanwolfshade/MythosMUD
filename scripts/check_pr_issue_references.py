"""
Warn when a PR references an open issue without a GitHub closing keyword.

This project's remediation campaign for the 2026-08 design/implementation audit shipped six
fixes (issues #618, #619, #620, #621, #622, #626, #629) whose PRs never used a closing keyword --
they named the issue in prose ("(#620)", "fixes the guard from #620") instead of a recognized
keyword ("Closes #620"), so GitHub never auto-closed it and the issue sat open despite the fix
being live on main. See the #620/#621/#622/#629 closing comments for the concrete pattern.

Warn-only, always exits 0 -- mirrors scripts/lint_raw_sql_in_python.py's own documented rationale.
PRs legitimately cross-reference issues they do not close (e.g. PR #664 cross-referencing #627 on
purpose); a hard fail on that is a false-positive machine, and a guard that blocks on ordinary
correct behaviour is the guard everyone learns to bypass -- the "#651 coverage floor" pattern this
project has already hit once.

Usage: PR_TITLE=... PR_BODY=... python scripts/check_pr_issue_references.py
Exit: always 0. Prints a warning (or ::warning:: annotation under GITHUB_ACTIONS) naming any open
issue referenced without a closing keyword.
"""

from __future__ import annotations

import os
import re
import subprocess  # nosec B404 -- gh CLI, no shell, fixed argv, no untrusted input in argv
import sys

# GitHub's own closing-keyword list: https://docs.github.com/en/issues/tracking-your-work-with-issues/
# using-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword
_KEYWORD_PATTERN = re.compile(
    r"\b(?:close[sd]?|fix(?:e[sd])?|resolve[sd]?)\b\s*:?\s*((?:#\d+(?:\s*,\s*|\s+and\s+)?)+)",
    re.IGNORECASE,
)
_REF_PATTERN = re.compile(r"#(\d+)")

_GH_TIMEOUT_SECONDS = 15


def find_bare_references(text: str) -> set[int]:
    """Return issue numbers referenced in text that are NOT preceded by a closing keyword.

    "Closes #620, #621" links both 620 and 621. A bare "#620" elsewhere in the same text is
    still bare -- only the keyword-adjacent occurrence counts as linked.
    """
    linked: set[int] = set()
    for match in _KEYWORD_PATTERN.finditer(text):
        linked.update(_extract_numbers(match.group(1)))

    return _extract_numbers(text) - linked


def _extract_numbers(text: str) -> set[int]:
    """Return every #NNN issue number appearing in text, as an int set."""
    return {int(ref.group(1)) for ref in _REF_PATTERN.finditer(text)}


def _run_gh(args: list[str]) -> str | None:
    """Run a `gh` subcommand, returning stripped stdout, or None on any failure."""
    try:
        result = subprocess.run(  # nosec B603 -- fixed "gh" executable, args are our own list
            ["gh", *args], capture_output=True, text=True, timeout=_GH_TIMEOUT_SECONDS, check=False
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if result.returncode != 0:
        return None
    return result.stdout.strip()


def get_open_issue_numbers(candidates: set[int]) -> set[int] | None:
    """Return the subset of candidates that are currently open. None means the lookup failed."""
    if not candidates:
        return set()

    open_numbers: set[int] = set()
    for number in sorted(candidates):
        state = _run_gh(["issue", "view", str(number), "--json", "state", "-q", ".state"])
        if state is None:
            return None
        if state.upper() == "OPEN":
            open_numbers.add(number)
    return open_numbers


def _format_message(message: str) -> str:
    """Format as a GitHub Actions annotation in CI, plain text locally."""
    if os.environ.get("GITHUB_ACTIONS"):
        return f"::warning::{message}"
    return message


def main() -> int:
    """Warn about open issues referenced without a closing keyword. Always returns 0."""
    title = os.environ.get("PR_TITLE", "")
    body = os.environ.get("PR_BODY", "")
    text = f"{title}\n{body}"

    bare_refs = find_bare_references(text)
    if not bare_refs:
        print("No unlinked issue references found.")
        return 0

    open_bare = get_open_issue_numbers(bare_refs)
    if open_bare is None:
        print("Notice: could not query issue state via gh CLI; skipping issue-reference check.")
        return 0
    if not open_bare:
        print("All referenced issues are either closed or linked with a closing keyword.")
        return 0

    numbers = ", ".join(f"#{n}" for n in sorted(open_bare))
    message = (
        f"PR references open issue(s) without a closing keyword: {numbers}. "
        'If this PR fixes them, add "Closes #NNN" to the body. If it only cross-references them, '
        "ignore this."
    )
    print(_format_message(message))
    return 0


if __name__ == "__main__":
    sys.exit(main())
