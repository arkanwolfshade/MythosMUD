#!/usr/bin/env python3
"""
Self-check for check_relative_links() in scripts/hads/validate.py.

Not collected by pytest — testpaths is scoped to server/tests (pyproject.toml,
server/pytest.ini), and this is repo-root tooling, not server/client code. Run directly:

    python scripts/hads/test_validate.py

Exits non-zero (via AssertionError) on failure.
"""

from __future__ import annotations

import tempfile
from pathlib import Path

from validate import check_relative_links


def demo() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "target.md").write_text("# Target\n", encoding="utf-8")

        # Resolving relative link -> no issues.
        lines = ["[ok](target.md)"]
        assert check_relative_links(lines, root) == []

        # Wrong-depth / missing target -> one issue.
        lines = ["[missing](does_not_exist.md)"]
        issues = check_relative_links(lines, root)
        assert len(issues) == 1
        assert issues[0][0] == 1
        assert "broken relative link" in issues[0][1]

        # Link target content wraps across a line: even though the collapsed path
        # resolves, the raw (unwrapped, whitespace-containing) target must NOT
        # resolve, so this must still fail as a broken relative link.
        lines = ["[wrapped](target", ".md)"]
        issues = check_relative_links(lines, root)
        assert len(issues) == 1
        assert "broken relative link" in issues[0][1]

        # ']' and '(' themselves split across a line: not valid CommonMark link
        # syntax at all (LINK_PATTERN requires them adjacent) — caught separately
        # by SPLIT_LINK_PATTERN.
        lines = ["[wrapped]", "(target.md)"]
        issues = check_relative_links(lines, root)
        assert len(issues) == 1
        assert "line wrap" in issues[0][1]

        # http(s) links are skipped entirely.
        lines = ["[ext](https://example.com/does/not/exist.md)"]
        assert check_relative_links(lines, root) == []

        # Angle-bracket autolinks are skipped.
        lines = ["[ext](<https://example.com/x#y>)"]
        assert check_relative_links(lines, root) == []

        # A link target inside a fenced code block is not checked.
        lines = ["```", "[fenced](does_not_exist.md)", "```"]
        assert check_relative_links(lines, root) == []

    print("check_relative_links self-check: all assertions passed")


if __name__ == "__main__":
    demo()
