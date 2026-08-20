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

New sites fail the build immediately. Existing, already-known sites are grandfathered via
RAW_SQL_ALLOWLIST below -- each entry names the exact site, links the issue that owns fixing it,
and carries a target date. Past-deadline entries print a loud warning but do not fail the build:
a hard-fail tied to a guessed date for work with unpredictable upstream timing (see #633, which
depends on Phases 2-3 finishing first) risks becoming a rebuild of the exact
"pre-existing-debt-blocks-every-commit" pattern already hit twice in this project's history
(#651's coverage floor; the near-miss on #629's stale CRITICAL_FILES entry). No network calls --
pure local date comparison, staying offline-safe like every other hook here.

Usage: python scripts/lint_raw_sql_in_python.py
Exit: 0 if no new (non-allowlisted) sites found, 1 otherwise. Past-deadline allowlist entries warn
but never contribute to a nonzero exit.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Directories under server/ excluded entirely -- never scanned, never allowlisted.
EXCLUDED_DIR_PARTS = {
    "tests",
    "alembic",  # schema DDL/migration tooling; ADR-015's procedure mandate is about
    # application data access, not the tool whose entire job is schema migration.
    "scripts",  # one-off admin/migration CLI tools, not live request-serving paths.
    "graphify-out",  # vendored virtualenv checked into the tree by a different tool.
}


@dataclass(frozen=True)
class AllowlistEntry:
    """One grandfathered raw-SQL site: exact location, owning issue, target removal date."""

    file: str
    line: int
    issue: str
    target_date: date


# Baseline as of #618 (2026-08-20): 4 files, 11 sites, confirmed by direct scan. #633 (Phase 4 of
# the ranked plan) owns migrating these to stored procedures. Remove an entry here only when its
# site has actually been migrated -- do not bump the date without fixing the site.
RAW_SQL_ALLOWLIST: tuple[AllowlistEntry, ...] = (
    AllowlistEntry("server/game/room_service.py", 427, "#633", date(2026, 11, 1)),
    AllowlistEntry("server/persistence/container_persistence.py", 129, "#633", date(2026, 11, 1)),
    AllowlistEntry("server/persistence/container_persistence.py", 551, "#633", date(2026, 11, 1)),
    AllowlistEntry("server/persistence/item_instance_persistence.py", 25, "#633", date(2026, 11, 1)),
    AllowlistEntry("server/persistence/item_instance_persistence.py", 194, "#633", date(2026, 11, 1)),
    AllowlistEntry("server/services/exploration_service.py", 125, "#633", date(2026, 11, 1)),
    AllowlistEntry("server/services/exploration_service.py", 145, "#633", date(2026, 11, 1)),
    AllowlistEntry("server/services/exploration_service.py", 197, "#633", date(2026, 11, 1)),
    AllowlistEntry("server/services/exploration_service.py", 212, "#633", date(2026, 11, 1)),
    AllowlistEntry("server/services/exploration_service.py", 255, "#633", date(2026, 11, 1)),
    AllowlistEntry("server/services/exploration_service.py", 313, "#633", date(2026, 11, 1)),
)

_ALLOWLIST_BY_SITE: dict[tuple[str, int], AllowlistEntry] = {
    (entry.file, entry.line): entry for entry in RAW_SQL_ALLOWLIST
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
_SELECT_FROM_PATTERN = re.compile(r"\bSELECT\b.+?\bFROM\s+([A-Za-z_][A-Za-z0-9_]*)\s*(\()?")


def _strip_line_comment(line: str) -> str:
    """Return line with a trailing '# ...' comment removed, so prose mentioning SQL keywords in a
    comment (e.g. "avoids SELECT * anti-pattern") is never matched as embedded SQL."""
    idx = line.find("#")
    return line[:idx] if idx >= 0 else line


def _collect_python_files() -> list[Path]:
    out: list[Path] = []
    for path in (PROJECT_ROOT / "server").rglob("*.py"):
        rel_parts = set(path.relative_to(PROJECT_ROOT).parts)
        if rel_parts & EXCLUDED_DIR_PARTS:
            continue
        out.append(path)
    return sorted(out)


def _find_raw_sql_lines(content: str) -> list[int]:
    """Return 1-based line numbers containing a raw-SQL violation."""
    hits: set[int] = set()
    for i, raw_line in enumerate(content.splitlines(), 1):
        line = _strip_line_comment(raw_line)
        if _UNCONDITIONAL_PATTERN.search(line):
            hits.add(i)
            continue
        match = _SELECT_FROM_PATTERN.search(line)
        if match and match.group(2) is None:
            # FROM target has no following '(' -- a bare table name, not a procedure call.
            hits.add(i)
    return sorted(hits)


def scan() -> tuple[list[str], list[str], int]:
    """Scan server/ for raw SQL. Returns (new_violations, overdue_warnings, allowlisted_count)."""
    today = date.today()
    new_violations: list[str] = []
    overdue_warnings: list[str] = []
    allowlisted_seen: set[tuple[str, int]] = set()

    for path in _collect_python_files():
        rel = str(path.relative_to(PROJECT_ROOT)).replace("\\", "/")
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            new_violations.append(f"{rel}: read error: {e}")
            continue

        for line_num in _find_raw_sql_lines(content):
            site = (rel, line_num)
            entry = _ALLOWLIST_BY_SITE.get(site)
            if entry is None:
                new_violations.append(
                    f"{rel}:{line_num}: raw SQL string literal -- use a stored procedure "
                    f"(ADR-015), or add to RAW_SQL_ALLOWLIST with a linked issue if genuinely "
                    f"grandfathered"
                )
                continue
            allowlisted_seen.add(site)
            if entry.target_date < today:
                overdue_warnings.append(
                    f"OVERDUE: {rel}:{line_num}, target {entry.target_date}, see {entry.issue}"
                )

    return new_violations, overdue_warnings, len(allowlisted_seen)


def main() -> int:
    """Run the raw-SQL guard and return 1 if any new (non-allowlisted) site is found."""
    new_violations, overdue_warnings, allowlisted_count = scan()

    for msg in new_violations:
        print(msg)
    for msg in overdue_warnings:
        print(msg)

    remaining = len(RAW_SQL_ALLOWLIST)
    print(f"\nRaw-SQL allowlist: {allowlisted_count}/{remaining} grandfathered site(s) remain.")

    if new_violations:
        print(
            f"\n{len(new_violations)} new raw-SQL site(s) found. "
            "See docs/POSTGRESQL_CONTRIBUTOR_GUIDE.md and ADR-015."
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
