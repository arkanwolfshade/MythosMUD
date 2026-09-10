"""
Unit tests for enhanced_logging_config helpers.

Covers log_exception_once dedupe paths (public mark_logged vs setattr fallback), and the
configure_enhanced_structlog / setup_enhanced_logging control flow now that both take a typed
LoggingConfig end to end (#686): the disable_logging branch skips file logging / uvicorn config,
and the enabled branch wires them up and marks the module's _logging_state initialized.
"""

# pyright: reportPrivateUsage=false
# Reason: tests reset/assert on the module's _logging_state singleton directly.

from pathlib import Path
from typing import cast
from unittest.mock import MagicMock

import pytest
from structlog.stdlib import BoundLogger

from server.config.models.security_logging import LoggingConfig
from server.exceptions import LoggedException
from server.structured_logging import enhanced_logging_config
from server.structured_logging.enhanced_logging_config import (
    configure_enhanced_structlog,
    log_exception_once,
    setup_enhanced_logging,
)


class _StubBoundLogger:
    """Minimal stand-in for BoundLogger: only what log_exception_once touches for these tests."""

    def __init__(self) -> None:
        self.error_calls: list[tuple[str, dict[str, object]]] = []

    def error(self, message: str, **kwargs: object) -> None:
        self.error_calls.append((message, kwargs))


def _as_bound_logger(stub: _StubBoundLogger) -> BoundLogger:
    """Adapt test double to the function param type (structural use only)."""
    return cast(BoundLogger, cast(object, stub))


def test_log_exception_once_plain_exception_sets_flag_and_skips_repeat():
    """Plain exceptions get _already_logged via __setattr__ fallback; second log is suppressed."""
    stub = _StubBoundLogger()
    exc = ValueError("boom")
    log_exception_once(_as_bound_logger(stub), "error", "first", exc=exc)
    log_exception_once(_as_bound_logger(stub), "error", "second", exc=exc)
    assert len(stub.error_calls) == 1
    assert stub.error_calls[0][0] == "first"
    # ValueError has no _already_logged in stubs; getattr documents dynamic tag from log_exception_once.
    assert getattr(exc, "_already_logged", False) is True  # noqa: B009


def test_log_exception_once_logged_exception_uses_mark_logged():
    """LoggedException uses mark_logged(); repeat call does not log again."""
    stub = _StubBoundLogger()
    exc = LoggedException("x", already_logged=False)
    log_exception_once(_as_bound_logger(stub), "error", "once", exc=exc)
    assert exc.already_logged is True
    assert len(stub.error_calls) == 1
    assert stub.error_calls[0][0] == "once"
    log_exception_once(_as_bound_logger(stub), "error", "twice", exc=exc)
    assert len(stub.error_calls) == 1


@pytest.fixture(autouse=True)
def _reset_logging_state():  # pyright: ignore[reportUnusedFunction] - pytest autouse; not called directly
    """Snapshot/restore the module's _logging_state singleton around each test."""
    state = enhanced_logging_config._logging_state
    before_initialized, before_signature = state.initialized, state.signature
    state.initialized, state.signature = False, None
    yield
    state.initialized, state.signature = before_initialized, before_signature


def _disabled_config() -> LoggingConfig:
    return LoggingConfig(environment="unit_test", disable_logging=True)


def _enabled_config(tmp_path: Path) -> LoggingConfig:
    return LoggingConfig(environment="unit_test", log_base=str(tmp_path), disable_logging=False)


def test_configure_enhanced_structlog_skips_file_logging_when_disabled(monkeypatch: pytest.MonkeyPatch) -> None:
    """disable_logging=True must not call setup_enhanced_file_logging."""
    mock_file_logging = MagicMock()
    monkeypatch.setattr(enhanced_logging_config, "setup_enhanced_file_logging", mock_file_logging)
    configure_enhanced_structlog(_disabled_config())
    mock_file_logging.assert_not_called()


def test_configure_enhanced_structlog_configures_file_logging_when_enabled(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """disable_logging=False must call setup_enhanced_file_logging with the full typed config."""
    mock_file_logging = MagicMock()
    monkeypatch.setattr(enhanced_logging_config, "setup_enhanced_file_logging", mock_file_logging)
    config = _enabled_config(tmp_path)
    configure_enhanced_structlog(config, player_service=None, enable_async=False)
    mock_file_logging.assert_called_once_with(config, config.level, None, False)


def test_setup_enhanced_logging_disabled_skips_uvicorn_and_state(monkeypatch: pytest.MonkeyPatch) -> None:
    """The disabled branch still configures structlog but must not touch uvicorn or _logging_state."""
    mock_configure = MagicMock()
    mock_uvicorn = MagicMock()
    monkeypatch.setattr(enhanced_logging_config, "configure_enhanced_structlog", mock_configure)
    monkeypatch.setattr(enhanced_logging_config, "_configure_enhanced_uvicorn_logging", mock_uvicorn)
    config = _disabled_config()

    setup_enhanced_logging(config)

    mock_configure.assert_called_once_with(config, None, True)
    mock_uvicorn.assert_not_called()
    assert enhanced_logging_config._logging_state.initialized is False  # pylint: disable=protected-access  # Reason: verifying internal state left untouched by the disabled branch


def test_setup_enhanced_logging_enabled_configures_uvicorn_and_sets_state(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """The enabled branch must configure uvicorn/third-party levels and mark state initialized."""
    mock_configure = MagicMock()
    mock_uvicorn = MagicMock()
    mock_third_party = MagicMock()
    monkeypatch.setattr(enhanced_logging_config, "configure_enhanced_structlog", mock_configure)
    monkeypatch.setattr(enhanced_logging_config, "_configure_enhanced_uvicorn_logging", mock_uvicorn)
    monkeypatch.setattr(enhanced_logging_config, "_configure_third_party_log_levels", mock_third_party)
    config = _enabled_config(tmp_path)

    setup_enhanced_logging(config)

    mock_configure.assert_called_once_with(config, None, True)
    mock_uvicorn.assert_called_once()
    mock_third_party.assert_called_once()
    assert enhanced_logging_config._logging_state.initialized is True  # pylint: disable=protected-access  # Reason: verifying internal state set by the enabled branch
