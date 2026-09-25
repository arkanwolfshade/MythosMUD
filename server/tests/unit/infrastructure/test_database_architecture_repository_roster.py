"""
Repository-roster parity check between server/persistence/repositories/*.py and
docs/architecture/DATABASE_ARCHITECTURE.md §3.1.

§3.1 documents every repository class, grouped by domain, but a repository class added or
removed without a doc update would otherwise drift silently -- the prior version of this doc
already missed `ItemCatalogRepository` once. Symmetric to
`test_db_design_table_roster.py`'s db/schema.sql-vs-PACKAGE_DB_DESIGN.md §5 check.
"""

import re
from pathlib import Path

# Project root: server/tests/unit/infrastructure -> unit -> tests -> server -> project root
_PROJECT_ROOT = Path(__file__).resolve().parents[4]
_REPOSITORIES_DIR = _PROJECT_ROOT / "server" / "persistence" / "repositories"
_ARCHITECTURE_DOC = _PROJECT_ROOT / "docs" / "architecture" / "DATABASE_ARCHITECTURE.md"

# `Repository` suffix already excludes Protocol stubs (`_ExperienceEventBus`, `_DialogueRow`),
# TypedDicts (`AddEffectInput`), dataclasses (`ItemPrototypeRow`, `ItemCatalogPage`,
# `InventoryPayload`) and helper classes (`PlayerSavePreparer`) -- no exclusion list needed.
_CLASS_REPOSITORY_RE = re.compile(r"^class (\w+Repository)\b", re.MULTILINE)
_BACKTICK_REPOSITORY_RE = re.compile(r"`(\w+Repository)`")


def _code_repositories() -> set[str]:
    names: set[str] = set()
    for path in _REPOSITORIES_DIR.glob("*.py"):
        names.update(_CLASS_REPOSITORY_RE.findall(path.read_text(encoding="utf-8")))
    return names


def _doc_section_3_1() -> str:
    content = _ARCHITECTURE_DOC.read_text(encoding="utf-8")
    match = re.search(r"^### 3\.1 Repository roster\n(.*?)^### 3\.2", content, re.MULTILINE | re.DOTALL)
    assert match, "DATABASE_ARCHITECTURE.md must have a '### 3.1 Repository roster' section followed by '### 3.2'"
    return match.group(1)


def _doc_repositories() -> set[str]:
    """Repository names from §3.1's roster table, "Repository" column only.

    Restricted to that one column deliberately: the "Notes" column also backtick-quotes
    unrelated file names (`container_persistence.py`, `_mappers.py`), and a naive whole-section
    scan would need to filter those against the code's own repository set -- which would make
    an *extra*, non-existent repository in the doc silently pass (nothing to filter it out with).
    """
    row_re = re.compile(r"^\|\s*([^|]+)\|\s*[^|]+\|\s*[^|]+\|\s*$", re.MULTILINE)
    names: set[str] = set()
    for row_match in row_re.finditer(_doc_section_3_1()):
        names.update(_BACKTICK_REPOSITORY_RE.findall(row_match.group(1)))
    return names


class TestDatabaseArchitectureRepositoryRoster:
    """DATABASE_ARCHITECTURE.md §3.1 must list exactly the repository classes the code defines."""

    def test_repositories_dir_exists(self) -> None:
        assert _REPOSITORIES_DIR.exists(), "server/persistence/repositories/ missing"

    def test_architecture_doc_exists(self) -> None:
        assert _ARCHITECTURE_DOC.exists(), "docs/architecture/DATABASE_ARCHITECTURE.md missing"

    def test_code_has_repositories(self) -> None:
        """Sanity check the extraction pattern still matches the repositories' class style."""
        assert len(_code_repositories()) > 0, (
            "No 'class *Repository' definitions found in server/persistence/repositories/"
        )

    def test_roster_matches_code(self) -> None:
        code_repositories = _code_repositories()
        doc_repositories = _doc_repositories()

        missing_from_doc = code_repositories - doc_repositories
        extra_in_doc = doc_repositories - code_repositories

        assert not missing_from_doc, (
            f"Repository class(es) in server/persistence/repositories/ but not documented in "
            f"DATABASE_ARCHITECTURE.md §3.1: {sorted(missing_from_doc)}"
        )
        assert not extra_in_doc, (
            f"Repository class(es) in DATABASE_ARCHITECTURE.md §3.1 that no longer exist in "
            f"server/persistence/repositories/: {sorted(extra_in_doc)}"
        )
