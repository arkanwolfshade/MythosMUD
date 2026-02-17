"""
Lightweight guardrails for hand-maintained PostgreSQL SQL.

Warns on:
- select * (outside comments) in schema, verification, migrations, and server scripts
- not in ( with a subquery (select) in the same file

Scoped to developer-authored SQL only (db/schema, db/verification, db/migrations,
server/scripts). Auto-generated dumps (e.g. db/authoritative_schema.sql) are excluded.

Usage: python scripts/lint_sql_guardrails.py
Exit: 0 if no issues, 1 if any warning (so CI can enforce).
"""

import re
import sys
from pathlib import Path

# Project root: scripts/ -> project root
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Directories containing hand-maintained SQL (relative to project root)
SQL_DIRS = [
    "db/schema",
    "db/verification",
    "db/migrations",
    "data/db/migrations",
    "server/scripts",
]

# Files to skip (e.g. generated or legacy)
SKIP_FILES = {"authoritative_schema.sql"}


def _collect_sql_files() -> list[Path]:
    out: list[Path] = []
    for dir_rel in SQL_DIRS:
        dir_path = PROJECT_ROOT / dir_rel
        if not dir_path.is_dir():
            continue
        for path in dir_path.rglob("*.sql"):
            if path.name in SKIP_FILES:
                continue
            out.append(path)
    return sorted(out)


def _strip_line_comment(line: str) -> str:
    """Return line with line comment removed (-- ...)."""
    idx = line.find("--")
    if idx >= 0:
        return line[:idx]
    return line


def _strip_block_comments(content: str) -> str:
    """Return content with block comments /* ... */ removed (simple, no nested)."""
    return re.sub(r"/\*.*?\*/", "", content, flags=re.DOTALL)


def check_select_star(path: Path, content: str) -> list[str]:
    """Warn on select * outside comments."""
    issues: list[str] = []
    # Remove block comments so we don't flag commented-out examples
    no_block = _strip_block_comments(content)
    for i, line in enumerate(no_block.splitlines(), 1):
        code_part = _strip_line_comment(line)
        if re.search(r"\bselect\s+\*", code_part, re.IGNORECASE):
            issues.append(f"{path.relative_to(PROJECT_ROOT)}:{i}: avoid 'select *'; use explicit column list")
    return issues


def check_not_in_subquery(path: Path, content: str) -> list[str]:
    """Warn on 'not in (' when followed by a subquery (select)."""
    issues: list[str] = []
    # Simple heuristic: "not in (" then later "select" before the matching ")"
    no_block = _strip_block_comments(content)
    # Look for pattern: not in ( ... select ... )  (simplified: same line or few lines)
    if re.search(r"not\s+in\s*\(", no_block, re.IGNORECASE):
        # Check if there's a select in the same statement (e.g. next 500 chars)
        for m in re.finditer(r"not\s+in\s*\(\s*", no_block, re.IGNORECASE):
            start = m.end()
            chunk = no_block[start : start + 500]
            if re.search(r"\bselect\b", chunk, re.IGNORECASE):
                line_num = no_block[: m.start()].count("\n") + 1
                issues.append(
                    f"{path.relative_to(PROJECT_ROOT)}:{line_num}: prefer NOT EXISTS or LEFT JOIN ... IS NULL over NOT IN (subquery)"
                )
                break
    return issues


def main() -> int:
    """Run SQL guardrail checks and return 1 if any issues found, 0 otherwise."""
    files = _collect_sql_files()
    all_issues: list[str] = []
    for path in files:
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            all_issues.append(f"{path}: read error: {e}")
            continue
        all_issues.extend(check_select_star(path, content))
        all_issues.extend(check_not_in_subquery(path, content))

    for msg in all_issues:
        print(msg)
    if all_issues:
        print(f"\nTotal: {len(all_issues)} SQL guardrail warning(s). See docs/POSTGRESQL_CONTRIBUTOR_GUIDE.md")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
