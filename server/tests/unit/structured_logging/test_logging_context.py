"""Unit tests for logging_context utilities."""

from unittest.mock import MagicMock, patch

import structlog

from server.structured_logging.logging_context import (
    bind_request_context,
    clear_request_context,
    get_current_context,
    log_with_context,
)


def test_bind_request_context_generates_correlation_id() -> None:
    with patch("server.structured_logging.logging_context.bind_contextvars") as mock_bind:
        bind_request_context(user_id="user-1")
    mock_bind.assert_called_once()
    args = mock_bind.call_args.kwargs
    assert "correlation_id" in args
    assert args["user_id"] == "user-1"


def test_bind_request_context_omits_none_values() -> None:
    with patch("server.structured_logging.logging_context.bind_contextvars") as mock_bind:
        bind_request_context(correlation_id="corr-1", user_id=None, session_id="sess-1")
    mock_bind.assert_called_once_with(correlation_id="corr-1", session_id="sess-1")


def test_clear_request_context() -> None:
    with patch("server.structured_logging.logging_context.clear_contextvars") as mock_clear:
        clear_request_context()
    mock_clear.assert_called_once()


def test_get_current_context_returns_contextvars() -> None:
    with patch.object(structlog.contextvars, "get_contextvars", return_value={"correlation_id": "c1"}):
        assert get_current_context() == {"correlation_id": "c1"}


def test_get_current_context_returns_empty_on_error() -> None:
    with patch.object(structlog.contextvars, "get_contextvars", side_effect=AttributeError("no ctx")):
        assert get_current_context() == {}


def test_log_with_context_merges_context() -> None:
    bound_logger = MagicMock()
    with patch("server.structured_logging.logging_context.get_current_context", return_value={"correlation_id": "c1"}):
        log_with_context(bound_logger, "warning", "something happened", detail="x")
    bound_logger.warning.assert_called_once_with("something happened", correlation_id="c1", detail="x")
