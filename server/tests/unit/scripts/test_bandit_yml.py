"""Regression: Bandit must not scan generated graphify dumps or nested venvs."""

from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[4]
BANDIT_YML = PROJECT_ROOT / "bandit.yml"


def test_bandit_yml_excludes_generated_graphify_and_venvs() -> None:
    text = BANDIT_YML.read_text(encoding="utf-8")
    assert "exclude_dirs:" in text
    for name in ("graphify-out", ".venv", "site-packages"):
        assert f"  - {name}" in text
