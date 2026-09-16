"""
Table-roster parity check between db/schema.sql and docs/packages/PACKAGE_DB_DESIGN.md.

PACKAGE_DB_DESIGN.md §5 documents every table in the schema, grouped by domain, but deliberately
does not mirror column definitions (those live in db/schema.sql and nothing would catch a
duplicated copy going stale — see that doc's §5 note). The table *names* are the one part of that
roster this test can mechanically hold current: a table added to the schema without a matching
doc update fails here.
"""

import re
from pathlib import Path

# Project root: server/tests/unit/infrastructure -> unit -> tests -> server -> project root
_PROJECT_ROOT = Path(__file__).resolve().parents[4]
_SCHEMA_FILE = _PROJECT_ROOT / "db" / "schema.sql"
_DESIGN_DOC = _PROJECT_ROOT / "docs" / "packages" / "PACKAGE_DB_DESIGN.md"

_CREATE_TABLE_RE = re.compile(r"^CREATE TABLE (\w+) \($", re.MULTILINE)
# Table names appear inside doc prose as `table_name` (backtick-quoted, snake_case).
_BACKTICK_TABLE_RE = re.compile(r"`([a-z][a-z0-9_]*)`")


def _schema_tables() -> set[str]:
    content = _SCHEMA_FILE.read_text(encoding="utf-8")
    return set(_CREATE_TABLE_RE.findall(content))


def _doc_section_5() -> str:
    content = _DESIGN_DOC.read_text(encoding="utf-8")
    match = re.search(r"^## 5\. Data model\n(.*?)^## 6\.", content, re.MULTILINE | re.DOTALL)
    assert match, "PACKAGE_DB_DESIGN.md must have a '## 5. Data model' section followed by '## 6.'"
    return match.group(1)


def _doc_tables() -> set[str]:
    """Table names from §5's domain-grouping markdown table, "Tables" column only.

    Restricted to that one column deliberately: the "Key FK edges" column also
    backtick-quotes dotted refs (`players.player_id`), and a naive whole-section scan
    would need to filter those against the schema's own table set -- which would make an
    *extra*, non-existent table in the doc silently pass (nothing to filter it out with).
    """
    # Header/separator rows ("| Domain | Tables | Key FK edges |", "| --- | --- | --- |")
    # contain no backtick-quoted tokens, so they naturally contribute nothing below.
    row_re = re.compile(r"^\|\s*[^|]+\|\s*([^|]+)\|\s*[^|]+\|\s*$", re.MULTILINE)
    tables: set[str] = set()
    for row_match in row_re.finditer(_doc_section_5()):
        tables.update(_BACKTICK_TABLE_RE.findall(row_match.group(1)))
    return tables


class TestDbDesignTableRoster:
    """PACKAGE_DB_DESIGN.md §5 must list exactly the tables db/schema.sql defines."""

    def test_schema_file_exists(self):
        assert _SCHEMA_FILE.exists(), "db/schema.sql missing"

    def test_design_doc_exists(self):
        assert _DESIGN_DOC.exists(), "docs/packages/PACKAGE_DB_DESIGN.md missing"

    def test_schema_has_tables(self):
        """Sanity check the extraction pattern still matches db/schema.sql's CREATE TABLE style."""
        assert len(_schema_tables()) > 0, "No 'CREATE TABLE name (' statements found in db/schema.sql"

    def test_roster_matches_schema(self):
        schema_tables = _schema_tables()
        doc_tables = _doc_tables()

        missing_from_doc = schema_tables - doc_tables
        extra_in_doc = doc_tables - schema_tables

        assert not missing_from_doc, (
            f"Table(s) in db/schema.sql but not documented in PACKAGE_DB_DESIGN.md §5: {sorted(missing_from_doc)}"
        )
        assert not extra_in_doc, (
            f"Table(s) in PACKAGE_DB_DESIGN.md §5 that no longer exist in db/schema.sql: {sorted(extra_in_doc)}"
        )
