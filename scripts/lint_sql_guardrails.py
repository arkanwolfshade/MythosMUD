"""
Lightweight guardrails for hand-maintained PostgreSQL SQL.

Warns on:
- select * (outside comments) in schema, verification, migrations, and server scripts
- not in ( with a subquery (select) in the same file
- a migration in the wrong directory: db/migrations/ holds DDL only, data/db/migrations/ (the data repo)
  holds DML only, and a version number is used once across both (dbmate keys its ledger on the version)

Scoped to developer-authored SQL only (db/schema, db/verification, db/migrations, data/db/migrations,
server/scripts). Auto-generated DDL/seed (db/schema.sql, data/db/seed.sql) are excluded.

Usage: python scripts/lint_sql_guardrails.py
Exit: 0 if no issues, 1 if any warning (so CI can enforce).
"""

import re
import sys
from pathlib import Path

# Project root: scripts/ -> project root
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Directories containing hand-maintained SQL (relative to project root)
# dbmate reads two migration directories as one ledger: DDL in db/migrations/, DML (world content) in
# data/db/migrations/ (the data repo). The per-environment files that lived in the latter before #811 are
# baselined into db/schema.sql / data/db/seed.sql.
DDL_MIGRATIONS_DIR = "db/migrations"
DML_MIGRATIONS_DIR = "data/db/migrations"
SQL_DIRS = [
    "db/schema",
    "db/verification",
    DDL_MIGRATIONS_DIR,
    DML_MIGRATIONS_DIR,
    "server/scripts",
]

# Files to skip (e.g. generated or legacy). db/schema.sql and data/db/seed.sql (#811) are
# pg_dump output, not hand-authored -- same reason the old per-environment dumps were skipped.
SKIP_FILES = {"schema.sql", "seed.sql"}


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


# Comments, string literals and dollar-quoted bodies (quest JSON, function text): none of it is statement text.
# One alternation scanned left to right, so an apostrophe inside a comment or a `--` inside a string is harmless.
_NOT_CODE = re.compile(r"--[^\n]*|/\*.*?\*/|'(?:[^']|'')*'|(\$[A-Za-z_]*\$).*?\1", re.DOTALL)
_DDL_VERBS = frozenset({"CREATE", "ALTER", "DROP", "COMMENT", "GRANT", "REVOKE"})
_DML_VERBS = frozenset({"INSERT", "UPDATE", "DELETE"})
_CTE_MAIN_VERB = re.compile(r"\)\s*(INSERT|UPDATE|DELETE)\b", re.IGNORECASE)


def _statement_verbs(content: str) -> set[str]:
    """The leading verb of every statement in ``content`` (for ``WITH``, the verb that follows the CTEs)."""
    verbs: set[str] = set()
    for statement in _NOT_CODE.sub(" ", content).split(";"):
        words = statement.split()
        if not words:
            continue
        verb = words[0].upper()
        if verb == "WITH" and (main := _CTE_MAIN_VERB.search(statement)):
            verb = main.group(1).upper()
        verbs.add(verb)
    return verbs


def check_migration_kind(path: Path, content: str) -> list[str]:
    """Flag DML in db/migrations/ and DDL in data/db/migrations/ (the file says which half to split off)."""
    directory = path.parent.relative_to(PROJECT_ROOT).as_posix()
    if directory == DDL_MIGRATIONS_DIR:
        wrong_verbs, wrong_kind, right_dir = _DML_VERBS, "DML", DML_MIGRATIONS_DIR
    elif directory == DML_MIGRATIONS_DIR:
        wrong_verbs, wrong_kind, right_dir = _DDL_VERBS, "DDL", DDL_MIGRATIONS_DIR
    else:
        return []
    found = sorted(_statement_verbs(content) & wrong_verbs)
    if not found:
        return []
    return [
        f"{path.relative_to(PROJECT_ROOT)}: {wrong_kind} statement(s) ({', '.join(found)}) belong in {right_dir}/ "
        f"(db/migrations/ is DDL only, data/db/migrations/ is DML only); split the migration"
    ]


def check_unique_migration_versions(files: list[Path]) -> list[str]:
    """Flag a migration version (the filename's leading timestamp) used twice across both directories."""
    first_use: dict[str, Path] = {}
    issues: list[str] = []
    for path in files:
        if path.parent.relative_to(PROJECT_ROOT).as_posix() not in (DDL_MIGRATIONS_DIR, DML_MIGRATIONS_DIR):
            continue
        version = path.name.partition("_")[0]
        if version in first_use:
            issues.append(
                f"{path.relative_to(PROJECT_ROOT)}: migration version {version} is already used by "
                f"{first_use[version].relative_to(PROJECT_ROOT)}; dbmate keys its ledger on the version"
            )
        first_use.setdefault(version, path)
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
        all_issues.extend(check_migration_kind(path, content))
    all_issues.extend(check_unique_migration_versions(files))

    for msg in all_issues:
        print(msg)
    if all_issues:
        print(f"\nTotal: {len(all_issues)} SQL guardrail warning(s). See docs/POSTGRESQL_CONTRIBUTOR_GUIDE.md")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
