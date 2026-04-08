"""
Unit tests for enhanced_logging_config helpers.

Covers log_exception_once dedupe paths (public mark_logged vs setattr fallback).
"""

from typing import cast

from structlog.stdlib import BoundLogger

from server.exceptions import LoggedException
from server.structured_logging.enhanced_logging_config import log_exception_once


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
