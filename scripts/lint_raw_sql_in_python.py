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
RAW_SQL_ALLOWLIST below -- each entry names one file's *expected count* of sites (not individual
line numbers), links the issue that owns fixing it, and carries a target date. Past-deadline
entries print a loud warning but do not fail the build: a hard-fail tied to a guessed date for
work with unpredictable upstream timing (see #633, which depends on Phases 2-3 finishing first)
risks becoming a rebuild of the exact "pre-existing-debt-blocks-every-commit" pattern already hit
twice in this project's history (#651's coverage floor; the near-miss on #629's stale
CRITICAL_FILES entry). No network calls -- pure local date comparison, staying offline-safe like
every other hook here.

Keyed on an expected *count* per file, not (file, line): a line inserted anywhere above a
grandfathered site used to shift its line number and make an unrelated commit fail as if it
introduced a new violation (#618 hardening). A count can't shift under unrelated edits. The
allowlist can only tighten: found-more-than-expected fails as a new site, found-fewer-than-expected
fails too, telling you to lower the count once the migration that removed a site is in -- silent
allowlist drift (an entry nobody lowered after its site was fixed) would otherwise never be
caught. Known blind spot, accepted: removing one raw-SQL site and adding a different one in the
same file nets to the same count and passes unnoticed -- acceptable, since the commit still goes
through code review.

Usage: python scripts/lint_raw_sql_in_python.py
Exit: 0 if every file's raw-SQL count matches its allowlist entry (or has no entry and zero
sites), 1 otherwise. Past-deadline allowlist entries warn but never contribute to a nonzero exit.
"""

from __future__ import annotations

import os
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
    """One file's grandfathered raw-SQL debt: expected site count, owning issue, target date."""

    file: str
    count: int
    issue: str
    target_date: date


# Baseline as of #618 hardening (2026-08-20): 13 files, 30 sites -- re-derived by grouping the
# previous (file, line) baseline by file, not hand-counted. #633 (Phase 4 of the ranked plan) owns
# migrating these to stored procedures. Lower a file's count only when a site in it has actually
# been migrated -- do not bump the date without fixing a site.
RAW_SQL_ALLOWLIST: tuple[AllowlistEntry, ...] = (
    AllowlistEntry("server/auth/endpoints.py", 1, "#633", date(2026, 11, 1)),
    AllowlistEntry("server/npc/zone_config_loader.py", 2, "#633", date(2026, 11, 1)),
    AllowlistEntry("server/persistence/container_helpers.py", 2, "#633", date(2026, 11, 1)),
    AllowlistEntry("server/persistence/container_persistence.py", 3, "#633", date(2026, 11, 1)),
    AllowlistEntry("server/persistence/container_query_helpers.py", 3, "#633", date(2026, 11, 1)),
    AllowlistEntry("server/persistence/item_instance_persistence.py", 3, "#633", date(2026, 11, 1)),
    AllowlistEntry("server/persistence/repositories/emote_repository.py", 2, "#633", date(2026, 11, 1)),
    AllowlistEntry("server/services/coordinate_generator.py", 2, "#633", date(2026, 11, 1)),
    AllowlistEntry("server/services/coordinate_validator.py", 2, "#633", date(2026, 11, 1)),
    AllowlistEntry("server/services/exploration_service.py", 6, "#633", date(2026, 11, 1)),
    AllowlistEntry("server/services/holiday_service.py", 1, "#633", date(2026, 11, 1)),
    AllowlistEntry("server/services/passive_lucidity_flux/rate_overrides.py", 2, "#633", date(2026, 11, 1)),
    AllowlistEntry("server/services/schedule_service.py", 1, "#633", date(2026, 11, 1)),
)

_ALLOWLIST_BY_FILE: dict[str, AllowlistEntry] = {entry.file: entry for entry in RAW_SQL_ALLOWLIST}

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


def _overdue_message(rel: str, entry: AllowlistEntry) -> str:
    """Format an overdue-allowlist-entry message, as a GitHub Actions annotation in CI (so it
    surfaces on the PR's Files-changed tab instead of scrolling past in stdout) or plain text
    locally."""
    detail = f"OVERDUE: {rel}, target {entry.target_date}, see {entry.issue}"
    if os.environ.get("GITHUB_ACTIONS"):
        return f"::warning file={rel}::{detail}"
    return detail


def scan() -> tuple[list[str], list[str], int]:
    """Scan server/ for raw SQL. Returns (new_violations, overdue_warnings, allowlisted_count).

    allowlisted_count is the number of allowlist entries whose file's actual site count matched
    its expected count -- i.e. entries confirmed still accurate, not merely "present"."""
    today = date.today()
    new_violations: list[str] = []
    overdue_warnings: list[str] = []
    allowlisted_confirmed = 0
    counts_by_file: dict[str, int] = {}

    for path in _collect_python_files():
        rel = str(path.relative_to(PROJECT_ROOT)).replace("\\", "/")
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            new_violations.append(f"{rel}: read error: {e}")
            continue

        line_nums = _find_raw_sql_lines(content)
        if line_nums:
            counts_by_file[rel] = len(line_nums)

    for rel, found_count in counts_by_file.items():
        entry = _ALLOWLIST_BY_FILE.get(rel)
        expected_count = entry.count if entry is not None else 0

        if found_count > expected_count:
            new_violations.append(
                f"{rel}: {found_count} raw SQL site(s) found, {expected_count} allowlisted -- "
                f"use a stored procedure (ADR-015), or raise RAW_SQL_ALLOWLIST's count for this "
                f"file with a linked issue if genuinely grandfathered"
            )
        elif entry is not None and found_count < expected_count:
            new_violations.append(
                f"{rel}: {found_count} raw SQL site(s) found, but RAW_SQL_ALLOWLIST expects "
                f"{expected_count} -- a site was migrated; lower the allowlist count to {found_count}"
            )
        elif entry is not None:
            allowlisted_confirmed += 1
            if entry.target_date < today:
                overdue_warnings.append(_overdue_message(rel, entry))

    for entry in RAW_SQL_ALLOWLIST:
        if entry.file not in counts_by_file:
            new_violations.append(
                f"{entry.file}: RAW_SQL_ALLOWLIST expects {entry.count} raw SQL site(s), 0 found "
                f"-- all sites were migrated; remove this allowlist entry"
            )

    return new_violations, overdue_warnings, allowlisted_confirmed


def main() -> int:
    """Run the raw-SQL guard and return 1 if any file's raw-SQL count doesn't match its allowlist
    entry (or has an unlisted site)."""
    new_violations, overdue_warnings, allowlisted_count = scan()

    for msg in new_violations:
        print(msg)
    for msg in overdue_warnings:
        print(msg)

    remaining = len(RAW_SQL_ALLOWLIST)
    print(f"\nRaw-SQL allowlist: {allowlisted_count}/{remaining} grandfathered file(s) confirmed accurate.")

    if new_violations:
        print(
            f"\n{len(new_violations)} raw-SQL allowlist mismatch(es) found. "
            "See docs/POSTGRESQL_CONTRIBUTOR_GUIDE.md and ADR-015."
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
