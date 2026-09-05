"""Tests for scripts/lint_imports.py ADR-001 wrapper."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Protocol, cast

PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPT = PROJECT_ROOT / "scripts" / "lint_imports.py"
SCRIPTS_ROOT = PROJECT_ROOT / "scripts"


class _LintImportsModule(Protocol):
    """Shape of scripts/lint_imports.py, loaded dynamically below (not a static import)."""

    def broken_contract_names(self, output: str) -> list[str]: ...
    def broken_contract_count(self, output: str) -> int: ...
    def lint_imports_failed(self, output: str, exit_code: int) -> bool: ...


def _load_module() -> _LintImportsModule:
    scripts_root_s = str(SCRIPTS_ROOT)
    added = scripts_root_s not in sys.path
    if added:
        sys.path.insert(0, scripts_root_s)
    try:
        spec = importlib.util.spec_from_file_location("lint_imports", SCRIPT)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return cast(_LintImportsModule, cast(object, module))
    finally:
        if added:
            sys.path.remove(scripts_root_s)


def test_broken_contract_names_parses_broken_lines() -> None:
    mod = _load_module()
    output = """
ADR-001: Domain layer (...) KEPT
ADR-001: Persistence layer (...) BROKEN
Contracts: 1 kept, 1 broken.
"""
    assert mod.broken_contract_names(output) == ["ADR-001: Persistence layer (...)"]


def test_broken_contract_count_parses_summary() -> None:
    mod = _load_module()
    assert mod.broken_contract_count("Contracts: 2 kept, 0 broken.") == 0
    assert mod.broken_contract_count("Contracts: 1 kept, 1 broken.") == 1


def test_lint_imports_failed_on_broken_summary_even_with_zero_exit() -> None:
    mod = _load_module()
    output = "Contracts: 1 kept, 1 broken.\nADR-001: Persistence layer (...) BROKEN\n"
    assert mod.lint_imports_failed(output, 0) is True


def test_lint_imports_failed_on_nonzero_exit() -> None:
    mod = _load_module()
    assert mod.lint_imports_failed("Contracts: 2 kept, 0 broken.", 1) is True


def test_lint_imports_ok_on_kept_contracts() -> None:
    mod = _load_module()
    output = """
ADR-001: Domain layer (...) KEPT
Contracts: 2 kept, 0 broken.
"""
    assert mod.lint_imports_failed(output, 0) is False


def test_utf8_env_forces_child_encoding_regardless_of_host_console() -> None:
    """import-linter's rich progress spinner renders emoji; on a non-UTF-8 Windows console
    (e.g. cp1252) that crashes mid-render with UnicodeEncodeError before printing any real
    contract results, and the crash's exit code was previously misreported as a broken
    contract. Forcing PYTHONUTF8/PYTHONIOENCODING for the child process only avoids that."""
    source = SCRIPT.read_text(encoding="utf-8")
    assert '"PYTHONUTF8": "1"' in source
    assert '"PYTHONIOENCODING": "utf-8"' in source
    assert source.count("env=_UTF8_ENV") == 2


def test_lint_imports_subprocess_calls_decode_as_utf8() -> None:
    """The parent must decode the child's output as UTF-8 too -- subprocess.run(text=True)
    without an explicit encoding falls back to the host locale's preferred encoding, which
    mismatches a child forced to emit UTF-8 and raises UnicodeDecodeError in the background
    reader thread even after the child-side fix above."""
    source = SCRIPT.read_text(encoding="utf-8")
    assert source.count('encoding="utf-8"') == 2
    assert source.count('errors="replace"') == 2


def test_makefile_runs_lint_imports_early_in_all() -> None:
    makefile = (PROJECT_ROOT / "Makefile").read_text(encoding="utf-8")
    all_line = next(line for line in makefile.splitlines() if line.startswith("ALL_STAGES :="))
    stages = all_line.split(":=", 1)[1].replace("\\", " ").split()
    assert stages[0] == "format"
    assert stages[1] == "lint-imports"
