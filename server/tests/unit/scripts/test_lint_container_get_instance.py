"""Unit tests for scripts/lint_container_get_instance.py.

Verifies the detection logic that matters most: a real `ApplicationContainer.get_instance()` call
is caught, the same text mentioned in a comment or docstring (several migrated files now carry
exactly that prose) is not, and the count-keyed allowlist catches both new sites and stale
(higher-than-actual) entries -- same self-cleaning shape as lint_raw_sql_in_python.py's
RAW_SQL_ALLOWLIST, adapted for this guard's no-target-date allowlist (see its module docstring for
why: most entries here are permanently sanctioned service location, not debt with a fix-by date).
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Protocol, cast

PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "lint_container_get_instance.py"


class _LintContainerGetInstanceModule(Protocol):
    """Typed surface of the loaded script, for the parts these tests exercise."""

    def _find_get_instance_lines(self, content: str) -> list[int]: ...
    def scan(self) -> tuple[list[str], int]: ...

    CONTAINER_GET_INSTANCE_ALLOWLIST: tuple[object, ...]
    AllowlistEntry: type


def _load_script() -> _LintContainerGetInstanceModule:
    spec = importlib.util.spec_from_file_location("lint_container_get_instance_for_tests", SCRIPT_PATH)
    assert spec is not None
    assert spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    # dataclass's forward-reference resolution looks the module up via sys.modules[__module__];
    # register before exec_module so @dataclass(frozen=True) on AllowlistEntry doesn't crash.
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return cast(_LintContainerGetInstanceModule, cast(object, mod))


def test_script_exists() -> None:
    assert SCRIPT_PATH.is_file()


def test_flags_real_get_instance_call() -> None:
    mod = _load_script()
    content = "container = ApplicationContainer.get_instance()"
    assert mod._find_get_instance_lines(content) == [1]


def test_flags_call_inside_a_method() -> None:
    mod = _load_script()
    content = "    def foo(self):\n        container = ApplicationContainer.get_instance()\n        return container"
    assert mod._find_get_instance_lines(content) == [2]


def test_does_not_flag_docstring_prose_mentioning_the_pattern() -> None:
    """Several migrated files (e.g. user_manager.py, health_service.py) now carry a docstring
    explaining what they moved *away* from -- that prose must never count as a hit."""
    mod = _load_script()
    content = '"""Injected by GameBundle instead of reached via ApplicationContainer.get_instance())."""'
    assert mod._find_get_instance_lines(content) == []


def test_does_not_flag_comment_mentioning_the_pattern() -> None:
    mod = _load_script()
    content = "# Falls back to ApplicationContainer.get_instance() only in tests"
    assert mod._find_get_instance_lines(content) == []


def test_does_not_flag_unrelated_get_instance_call() -> None:
    """A same-named get_instance() on some other class must not be confused with
    ApplicationContainer's -- the guard matches the full dotted call, not just the method name."""
    mod = _load_script()
    content = "widget = WidgetFactory.get_instance()"
    assert mod._find_get_instance_lines(content) == []


def test_flags_multiple_calls_on_separate_lines() -> None:
    mod = _load_script()
    content = "a = ApplicationContainer.get_instance()\nb = 1\nc = ApplicationContainer.get_instance()"
    assert mod._find_get_instance_lines(content) == [1, 3]


def test_unparsable_file_returns_no_hits_rather_than_raising() -> None:
    mod = _load_script()
    assert mod._find_get_instance_lines("def broken(:\n    pass") == []


def test_allowlist_entries_are_suppressed_and_counted(tmp_path, monkeypatch) -> None:
    mod = _load_script()
    server_dir = tmp_path / "server"
    target_file = server_dir / "sample_service.py"
    server_dir.mkdir()
    target_file.write_text("container = ApplicationContainer.get_instance()\n", encoding="utf-8")

    entry = mod.AllowlistEntry("server/sample_service.py", 1, "sanctioned for this test")
    monkeypatch.setattr(mod, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(mod, "CONTAINER_GET_INSTANCE_ALLOWLIST", (entry,))
    monkeypatch.setattr(mod, "_ALLOWLIST_BY_FILE", {entry.file: entry})

    new_violations, allowlisted_count = mod.scan()

    assert new_violations == []
    assert allowlisted_count == 1


def test_new_unallowlisted_site_is_reported(tmp_path, monkeypatch) -> None:
    mod = _load_script()
    server_dir = tmp_path / "server"
    target_file = server_dir / "sample_service.py"
    server_dir.mkdir()
    target_file.write_text("container = ApplicationContainer.get_instance()\n", encoding="utf-8")

    monkeypatch.setattr(mod, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(mod, "CONTAINER_GET_INSTANCE_ALLOWLIST", ())
    monkeypatch.setattr(mod, "_ALLOWLIST_BY_FILE", {})

    new_violations, allowlisted_count = mod.scan()

    assert len(new_violations) == 1
    assert "sample_service.py" in new_violations[0]
    assert allowlisted_count == 0


def test_count_exceeding_allowlist_is_reported(tmp_path, monkeypatch) -> None:
    """A file with more get_instance() calls than its allowlist entry expects fails -- a
    genuinely new site was added alongside sanctioned ones."""
    mod = _load_script()
    server_dir = tmp_path / "server"
    target_file = server_dir / "sample_service.py"
    server_dir.mkdir()
    target_file.write_text(
        "a = ApplicationContainer.get_instance()\nb = ApplicationContainer.get_instance()\n", encoding="utf-8"
    )

    entry = mod.AllowlistEntry("server/sample_service.py", 1, "sanctioned for this test")
    monkeypatch.setattr(mod, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(mod, "CONTAINER_GET_INSTANCE_ALLOWLIST", (entry,))
    monkeypatch.setattr(mod, "_ALLOWLIST_BY_FILE", {entry.file: entry})

    new_violations, allowlisted_count = mod.scan()

    assert len(new_violations) == 1
    assert "2 ApplicationContainer.get_instance() call(s) found, 1 allowlisted" in new_violations[0]
    assert allowlisted_count == 0


def test_count_under_allowlist_is_reported(tmp_path, monkeypatch) -> None:
    """A file with fewer get_instance() calls than its allowlist entry expects fails -- a site
    was migrated or removed and the allowlist entry was never lowered."""
    mod = _load_script()
    server_dir = tmp_path / "server"
    target_file = server_dir / "sample_service.py"
    server_dir.mkdir()
    target_file.write_text("container = ApplicationContainer.get_instance()\n", encoding="utf-8")

    entry = mod.AllowlistEntry("server/sample_service.py", 2, "sanctioned for this test")
    monkeypatch.setattr(mod, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(mod, "CONTAINER_GET_INSTANCE_ALLOWLIST", (entry,))
    monkeypatch.setattr(mod, "_ALLOWLIST_BY_FILE", {entry.file: entry})

    new_violations, allowlisted_count = mod.scan()

    assert len(new_violations) == 1
    assert "lower the allowlist count to 1" in new_violations[0]
    assert allowlisted_count == 0


def test_stale_entry_for_fully_migrated_file_is_reported(tmp_path, monkeypatch) -> None:
    """An allowlist entry for a file with zero remaining hits (fully migrated) must fail, telling
    the author to remove the entry -- mirrors lint_raw_sql_in_python.py's equivalent check."""
    mod = _load_script()
    server_dir = tmp_path / "server"
    server_dir.mkdir()
    (server_dir / "other_file.py").write_text("x = 1\n", encoding="utf-8")

    entry = mod.AllowlistEntry("server/sample_service.py", 1, "sanctioned for this test")
    monkeypatch.setattr(mod, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(mod, "CONTAINER_GET_INSTANCE_ALLOWLIST", (entry,))
    monkeypatch.setattr(mod, "_ALLOWLIST_BY_FILE", {entry.file: entry})

    new_violations, allowlisted_count = mod.scan()

    assert len(new_violations) == 1
    assert "remove this allowlist entry" in new_violations[0]
    assert allowlisted_count == 0


def test_drift_immune_to_unrelated_line_shift(tmp_path, monkeypatch) -> None:
    """A blank line inserted above the allowlisted site must not trip a violation -- the whole
    point of keying on a per-file count instead of (file, line)."""
    mod = _load_script()
    server_dir = tmp_path / "server"
    target_file = server_dir / "sample_service.py"
    server_dir.mkdir()
    target_file.write_text("\n\n\ncontainer = ApplicationContainer.get_instance()\n", encoding="utf-8")

    entry = mod.AllowlistEntry("server/sample_service.py", 1, "sanctioned for this test")
    monkeypatch.setattr(mod, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(mod, "CONTAINER_GET_INSTANCE_ALLOWLIST", (entry,))
    monkeypatch.setattr(mod, "_ALLOWLIST_BY_FILE", {entry.file: entry})

    new_violations, allowlisted_count = mod.scan()

    assert new_violations == []
    assert allowlisted_count == 1


def test_baseline_allowlist_matches_current_codebase() -> None:
    """The shipped CONTAINER_GET_INSTANCE_ALLOWLIST must exactly match what the scanner currently
    finds in server/ -- catches allowlist drift as a test failure rather than a silent pass/fail
    surprise in CI."""
    mod = _load_script()
    new_violations, allowlisted_count = mod.scan()
    assert new_violations == []
    assert allowlisted_count == len(mod.CONTAINER_GET_INSTANCE_ALLOWLIST)
