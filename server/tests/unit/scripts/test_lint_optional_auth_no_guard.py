"""Unit tests for scripts/lint_optional_auth_no_guard.py.

Verifies the detection logic that matters most: a route on the optional get_current_user
dependency with no downstream check is flagged; a direct current_user-is-None check, a
validate_permission/validate_admin_permission call (bare-name or attribute-call form), and
multi-hop delegation to a same-module helper are all recognized as guards; a required-dependency
or no-dependency route is never flagged; and the count-keyed allowlist behaves like its
lint_raw_sql_in_python.py sibling (new site fails, stale entry fails, drift-immune to line shifts).
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Protocol, cast

PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "lint_optional_auth_no_guard.py"


class _LintOptionalAuthModule(Protocol):
    """Typed surface of the loaded script, for the parts these tests exercise."""

    def scan(self) -> tuple[list[str], int]: ...

    OPTIONAL_AUTH_ALLOWLIST: tuple[object, ...]
    AllowlistEntry: type


def _load_script() -> _LintOptionalAuthModule:
    spec = importlib.util.spec_from_file_location("lint_optional_auth_no_guard_for_tests", SCRIPT_PATH)
    assert spec is not None
    assert spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return cast(_LintOptionalAuthModule, cast(object, mod))


def _write(tmp_path: Path, content: str) -> Path:
    api_dir = tmp_path / "server" / "api"
    api_dir.mkdir(parents=True)
    target = api_dir / "sample_api.py"
    target.write_text(content, encoding="utf-8")
    return target


def test_script_exists() -> None:
    assert SCRIPT_PATH.is_file()


def test_flags_optional_auth_with_no_guard(tmp_path, monkeypatch) -> None:
    mod = _load_script()
    _write(
        tmp_path,
        "from fastapi import Depends\n"
        "@router.get('/x')\n"
        "async def handler(current_user=Depends(get_current_user)):\n"
        "    return current_user.id\n",
    )
    monkeypatch.setattr(mod, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(mod, "OPTIONAL_AUTH_ALLOWLIST", ())
    monkeypatch.setattr(mod, "_ALLOWLIST_BY_FILE", {})

    violations, allowlisted = mod.scan()

    assert len(violations) == 1
    assert "1 unguarded" in violations[0]
    assert allowlisted == 0


def test_does_not_flag_required_dependency(tmp_path, monkeypatch) -> None:
    mod = _load_script()
    _write(
        tmp_path,
        "from fastapi import Depends\n"
        "@router.get('/x')\n"
        "async def handler(current_user=Depends(get_current_active_user)):\n"
        "    return current_user.id\n",
    )
    monkeypatch.setattr(mod, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(mod, "OPTIONAL_AUTH_ALLOWLIST", ())
    monkeypatch.setattr(mod, "_ALLOWLIST_BY_FILE", {})

    violations, _allowlisted = mod.scan()

    assert violations == []


def test_does_not_flag_no_auth_dependency_at_all(tmp_path, monkeypatch) -> None:
    mod = _load_script()
    _write(tmp_path, "@router.get('/x')\nasync def handler(room_id: str):\n    return room_id\n")
    monkeypatch.setattr(mod, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(mod, "OPTIONAL_AUTH_ALLOWLIST", ())
    monkeypatch.setattr(mod, "_ALLOWLIST_BY_FILE", {})

    violations, _allowlisted = mod.scan()

    assert violations == []


def test_recognizes_direct_current_user_is_none_check(tmp_path, monkeypatch) -> None:
    mod = _load_script()
    _write(
        tmp_path,
        "from fastapi import Depends\n"
        "@router.get('/x')\n"
        "async def handler(current_user=Depends(get_current_user)):\n"
        "    if current_user is None:\n"
        "        raise LoggedHTTPException(status_code=401)\n"
        "    return current_user.id\n",
    )
    monkeypatch.setattr(mod, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(mod, "OPTIONAL_AUTH_ALLOWLIST", ())
    monkeypatch.setattr(mod, "_ALLOWLIST_BY_FILE", {})

    violations, _allowlisted = mod.scan()

    assert violations == []


def test_recognizes_bare_name_validate_admin_permission_call(tmp_path, monkeypatch) -> None:
    mod = _load_script()
    _write(
        tmp_path,
        "from fastapi import Depends\n"
        "@router.post('/x')\n"
        "async def handler(current_user=Depends(get_current_user)):\n"
        "    validate_admin_permission(current_user, AdminAction.X, None)\n"
        "    return current_user.id\n",
    )
    monkeypatch.setattr(mod, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(mod, "OPTIONAL_AUTH_ALLOWLIST", ())
    monkeypatch.setattr(mod, "_ALLOWLIST_BY_FILE", {})

    violations, _allowlisted = mod.scan()

    assert violations == []


def test_recognizes_attribute_call_validate_permission(tmp_path, monkeypatch) -> None:
    mod = _load_script()
    _write(
        tmp_path,
        "from fastapi import Depends\n"
        "@router.post('/x')\n"
        "async def handler(current_user=Depends(get_current_user)):\n"
        "    get_admin_auth_service().validate_permission(current_user, AdminAction.X, None)\n"
        "    return current_user.id\n",
    )
    monkeypatch.setattr(mod, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(mod, "OPTIONAL_AUTH_ALLOWLIST", ())
    monkeypatch.setattr(mod, "_ALLOWLIST_BY_FILE", {})

    violations, _allowlisted = mod.scan()

    assert violations == []


def test_recognizes_two_hop_delegation(tmp_path, monkeypatch) -> None:
    """Mirrors rooms.py's real shape: handler -> helper -> helper -> validate_permission."""
    mod = _load_script()
    _write(
        tmp_path,
        "from fastapi import Depends\n"
        "def _inner_guard(current_user, request):\n"
        "    auth_service.validate_permission(current_user, AdminAction.X, request)\n"
        "def _outer_guard(current_user, request):\n"
        "    _inner_guard(current_user, request)\n"
        "@router.post('/x')\n"
        "async def handler(current_user=Depends(get_current_user)):\n"
        "    _outer_guard(current_user, None)\n"
        "    return current_user.id\n",
    )
    monkeypatch.setattr(mod, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(mod, "OPTIONAL_AUTH_ALLOWLIST", ())
    monkeypatch.setattr(mod, "_ALLOWLIST_BY_FILE", {})

    violations, _allowlisted = mod.scan()

    assert violations == []


def test_allowlist_entry_is_suppressed_and_counted(tmp_path, monkeypatch) -> None:
    mod = _load_script()
    _write(
        tmp_path,
        "from fastapi import Depends\n"
        "@router.get('/x')\n"
        "async def handler(current_user=Depends(get_current_user)):\n"
        "    return current_user.id\n",
    )
    entry = mod.AllowlistEntry("server/api/sample_api.py", 1, "intentionally public")
    monkeypatch.setattr(mod, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(mod, "OPTIONAL_AUTH_ALLOWLIST", (entry,))
    monkeypatch.setattr(mod, "_ALLOWLIST_BY_FILE", {entry.file: entry})

    violations, allowlisted = mod.scan()

    assert violations == []
    assert allowlisted == 1


def test_count_under_allowlist_is_reported(tmp_path, monkeypatch) -> None:
    """A route was fixed but the allowlist count wasn't lowered -- must fail, not pass silently."""
    mod = _load_script()
    _write(
        tmp_path,
        "from fastapi import Depends\n"
        "@router.get('/x')\n"
        "async def handler(current_user=Depends(get_current_user)):\n"
        "    if current_user is None:\n"
        "        raise LoggedHTTPException(status_code=401)\n"
        "    return current_user.id\n",
    )
    entry = mod.AllowlistEntry("server/api/sample_api.py", 1, "stale entry")
    monkeypatch.setattr(mod, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(mod, "OPTIONAL_AUTH_ALLOWLIST", (entry,))
    monkeypatch.setattr(mod, "_ALLOWLIST_BY_FILE", {entry.file: entry})

    violations, allowlisted = mod.scan()

    assert len(violations) == 1
    assert "lower the allowlist count to 0" in violations[0]
    assert allowlisted == 0


def test_baseline_allowlist_matches_current_codebase() -> None:
    """The shipped OPTIONAL_AUTH_ALLOWLIST must exactly match what the scanner currently finds --
    catches allowlist drift as a test failure rather than a silent CI surprise."""
    mod = _load_script()
    violations, allowlisted = mod.scan()
    assert violations == []
    assert allowlisted == len(mod.OPTIONAL_AUTH_ALLOWLIST)
