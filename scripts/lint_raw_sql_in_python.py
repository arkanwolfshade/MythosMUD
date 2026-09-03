"""
Guard against raw table CRUD SQL string literals inside Python source.

Replaces the previously-inert .semgrep.yml rules (semgrep was never installed or wired into this
project's toolchain, and the rules' languages: [python] declaration wouldn't have matched SQL-text
patterns against Python's AST even if it were). See issue #618.

ADR-015: all Python<->PostgreSQL access goes through stored procedures/functions, called as
`SELECT fn(:arg)` (no FROM at all) or `SELECT col1, col2 FROM fn(:arg)` (FROM present, but the
target is a function call). Direct table access -- `SELECT ... FROM <bare table name>`,
`INSERT INTO`, `UPDATE ... SET`, `DELETE FROM`, `SELECT *` -- is what this guard flags. Getting the
FROM-target distinction wrong (flagging legitimate procedure calls) is how a guard like this ends
up disabled and ignored, which is exactly the fate the semgrep rules already met.

Any raw-SQL site fails the build. The grandfathered allowlist was emptied by #633 (2026-08-25) and
removed once every site was on stored procedures.

Usage: python scripts/lint_raw_sql_in_python.py
Exit: 0 if server/ has no raw-SQL sites, 1 otherwise.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Directories under server/ excluded entirely -- never scanned.
EXCLUDED_DIR_PARTS = {
    "tests",
    "alembic",  # schema DDL/migration tooling; ADR-015's procedure mandate is about
    # application data access, not the tool whose entire job is schema migration.
    "scripts",  # one-off admin/migration CLI tools, not live request-serving paths.
    "graphify-out",  # vendored virtualenv checked into the tree by a different tool.
}

# SELECT */INSERT/UPDATE-SET/DELETE-FROM: no legitimate ADR-015 procedure-call syntax in this
# codebase uses these forms, so they are flagged unconditionally.
#
# Case-sensitive by design: every real embedded-SQL site in this codebase writes keywords in
# UPPERCASE (PostgreSQL convention -- "SELECT stable_id FROM rooms", "INSERT INTO containers").
# Case-insensitive matching false-positives on ordinary English prose in comments/docstrings that
# happens to contain the words "select"/"from"/"update"/"delete" (e.g. a docstring reading "Select
# target player from matching players").
_UNCONDITIONAL_PATTERN = re.compile(
    r"\bSELECT\s+\*|\bINSERT\s+INTO\s+\w|\bUPDATE\s+\w+\s+SET\b|\bDELETE\s+FROM\s+\w"
)

# SELECT ... FROM <target>: only a bare identifier (no following '(') is a table name. A function
# call -- SELECT col FROM fn(:id), or SELECT fn(:id) with no FROM at all -- is a procedure call and
# must not be flagged.
#
# DOTALL + a bounded gap: real embedded SQL in this codebase is routinely written as a multi-line
# triple-quoted string with SELECT and FROM on separate lines (e.g. emote_service.py's own
# queries) -- a naive per-line match makes that shape invisible. The 500-char bound keeps a SELECT
# in one query from spuriously pairing with a FROM in a distant, unrelated one later in the file.
_SELECT_FROM_PATTERN = re.compile(r"\bSELECT\b.{0,500}?\bFROM\s+([A-Za-z_][A-Za-z0-9_]*)\s*(\()?", re.DOTALL)


def _strip_line_comment(line: str) -> str:
    """Return line with a trailing '# ...' comment removed, so prose mentioning SQL keywords in a
    comment (e.g. "avoids SELECT * anti-pattern") is never matched as embedded SQL."""
    idx = line.find("#")
    return line[:idx] if idx >= 0 else line


def _strip_comments(content: str) -> str:
    """Return content with every '# ...' line comment blanked out, preserving line structure (so
    position-based line-number math against the returned string stays correct)."""
    return "\n".join(_strip_line_comment(line) for line in content.splitlines())


def _collect_python_files() -> list[Path]:
    out: list[Path] = []
    for path in (PROJECT_ROOT / "server").rglob("*.py"):
        rel_parts = set(path.relative_to(PROJECT_ROOT).parts)
        if rel_parts & EXCLUDED_DIR_PARTS:
            continue
        out.append(path)
    return sorted(out)


def _find_raw_sql_lines(content: str) -> list[int]:
    """Return 1-based line numbers containing a raw-SQL violation.

    Matches against the whole (comment-stripped) file content rather than line-by-line, so
    multi-line SQL string literals -- SELECT and FROM on separate lines, a common style in this
    codebase -- aren't invisible to the scan. An earlier per-line version of this function missed
    emote_service.py's own queries for exactly this reason.
    """
    hits: set[int] = set()
    stripped = _strip_comments(content)

    for match in _UNCONDITIONAL_PATTERN.finditer(stripped):
        hits.add(stripped[: match.start()].count("\n") + 1)

    for match in _SELECT_FROM_PATTERN.finditer(stripped):
        if match.group(2) is None:
            # FROM target has no following '(' -- a bare table name, not a procedure call.
            hits.add(stripped[: match.start()].count("\n") + 1)

    return sorted(hits)


def scan() -> list[str]:
    """Scan server/ for raw SQL. Returns a list of violation messages."""
    violations: list[str] = []

    for path in _collect_python_files():
        rel = str(path.relative_to(PROJECT_ROOT)).replace("\\", "/")
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            violations.append(f"{rel}: read error: {e}")
            continue

        line_nums = _find_raw_sql_lines(content)
        if line_nums:
            violations.append(
                f"{rel}: {len(line_nums)} raw SQL site(s) at line(s) "
                f"{', '.join(str(n) for n in line_nums)} -- use a stored procedure (ADR-015)"
            )

    return violations


def main() -> int:
    """Run the raw-SQL guard and return 1 if any raw-SQL site is found."""
    violations = scan()

    for msg in violations:
        print(msg)

    if violations:
        print(
            f"\n{len(violations)} file(s) with raw SQL found. "
            "See docs/POSTGRESQL_CONTRIBUTOR_GUIDE.md and ADR-015."
        )
        return 1

    print("\nRaw-SQL guard: no raw SQL sites found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
