"""Regression test for scripts/run_quality_fragmentation_guard.py's git-output decoding.

The git-invoking helpers (`_run_git`, `_changed_files_between`, `_local_changed_files`) capture
subprocess output via `safe_run(..., capture_output=True, text=True)`. Without an explicit
`encoding=`, Python falls back to the platform's preferred encoding -- cp1252 on Windows. A
changed file whose path contains a byte cp1252 leaves undefined (e.g. 0x8D, hit by "Í") then
raises UnicodeDecodeError inside the subprocess reader thread, which the outer `make` pipeline's
fail-fast logic (any traceback in output = failure) turns into a spurious build failure even
though the guard's own pass/fail computation never ran -- this repo's own `graphify-out/wiki/`
directory has emoji-named files that can trigger the same class of failure.

Asserting the real byte-for-byte crash isn't portable here: whether cp1252 actually is the
ambient "preferred encoding" depends on the shell/locale the test happens to run under (this
project's dev environment already runs UTF-8-clean, so calling `safe_run` with no `encoding=`
would not reproduce the bug in every environment that runs this suite). Instead this pins the fix
at the boundary that matters -- the actual keyword arguments passed to `safe_run` -- which is
still a real, non-mock-testing-mock assertion: it fails if the encoding/errors handling
regresses, independent of whichever encoding a given CI box's locale happens to prefer.
"""

# pyright: reportAny=false
# TEST_MOCK: `mod` is a dynamically-loaded module (importlib.util.spec_from_file_location, same
# pattern as test_run_make_stages.py) and MagicMock's call_args/kwargs are inherently untyped --
# every attribute read through either resolves to Any, matching this suite's established
# mock-typing-noise convention (see test_passive_corruption_flux_service.py).

from __future__ import annotations

import importlib.util
from collections.abc import Mapping
from pathlib import Path
from unittest.mock import MagicMock, patch

PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPT = PROJECT_ROOT / "scripts" / "run_quality_fragmentation_guard.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("run_quality_fragmentation_guard", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _fake_result(stdout: str = "") -> MagicMock:
    result = MagicMock()
    result.returncode = 0
    result.stdout = stdout
    return result


def _assert_utf8_replace(kwargs: Mapping[str, object]) -> None:
    assert kwargs.get("capture_output") is True
    assert kwargs.get("text") is True
    assert kwargs.get("encoding") == "utf-8", (
        "must decode git output as utf-8, not the platform default (cp1252 on Windows)"
    )
    assert kwargs.get("errors") == "replace", "a lone undecodable byte must not crash the whole guard"


def test_run_git_passes_utf8_replace_encoding() -> None:
    mod = _load_module()
    with patch.object(mod, "safe_run", return_value=_fake_result("abc123\n")) as mock_run:
        result = mod._run_git(["rev-parse", "HEAD"])  # pylint: disable=protected-access

    assert result == "abc123"
    _assert_utf8_replace(mock_run.call_args.kwargs)


def test_changed_files_between_passes_utf8_replace_encoding() -> None:
    mod = _load_module()
    with patch.object(mod, "safe_run", return_value=_fake_result("a.py\nb.py\n")) as mock_run:
        result = mod._changed_files_between("base", "head")  # pylint: disable=protected-access

    assert result == ["a.py", "b.py"]
    _assert_utf8_replace(mock_run.call_args.kwargs)


def test_local_changed_files_passes_utf8_replace_encoding() -> None:
    mod = _load_module()
    with patch.object(mod, "safe_run", return_value=_fake_result("a.py\n")) as mock_run:
        result = mod._local_changed_files()  # pylint: disable=protected-access

    assert result == ["a.py"]
    for call in mock_run.call_args_list:
        _assert_utf8_replace(call.kwargs)
