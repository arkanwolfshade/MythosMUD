"""Regression tests for scripts/grype.py project-root anchoring and scan config."""

from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[4]
GRYPE_SCRIPT = PROJECT_ROOT / "scripts" / "grype.py"
GRYPE_CONFIG = PROJECT_ROOT / ".grype.yaml"


def test_grype_config_excludes_e2e_harness_paths() -> None:
    text = GRYPE_CONFIG.read_text(encoding="utf-8")
    assert "e2e-tests/**" in text
    assert "client/tests/**" in text
    assert "logs/**" in text


def test_grype_script_defines_repo_root_next_to_makefile() -> None:
    assert GRYPE_SCRIPT.is_file()
    source = GRYPE_SCRIPT.read_text(encoding="utf-8")
    assert "REPO_ROOT = Path(__file__).resolve().parents[1]" in source
    assert "cwd=str(REPO_ROOT)" in source


def test_makefile_codacy_tools_does_not_invoke_grype() -> None:
    makefile = (PROJECT_ROOT / "Makefile").read_text(encoding="utf-8")
    assert "codacy-tools:" in makefile
    codacy_line = next(line for line in makefile.splitlines() if line.startswith("codacy-tools:"))
    assert "grype" not in codacy_line
