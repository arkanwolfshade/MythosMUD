"""Unit tests for error_logging wrapper utilities."""

from unittest.mock import MagicMock, patch

import pytest
from fastapi import HTTPException, Request
from fastapi.websockets import WebSocket

from server.exceptions import MythosMUDError, ValidationError
from server.utils.error_logging import (
    create_context_from_request,
    create_context_from_websocket,
    create_error_context,
    create_logged_http_exception,
    log_and_raise,
    log_and_raise_http,
    log_error_with_context,
    wrap_third_party_exception,
)


def test_create_error_context():
    """Test create_error_context() creates error context."""
    context = create_error_context()
    assert context is not None
    assert hasattr(context, "to_dict")


def test_create_error_context_with_metadata():
    """Test create_error_context() can include metadata."""
    context = create_error_context()
    context.metadata = {"key": "value"}
    assert context.metadata == {"key": "value"}


def test_error_context_to_dict():
    """Test error context to_dict() method."""
    context = create_error_context()
    context.metadata = {"key": "value"}
    result = context.to_dict()
    assert isinstance(result, dict)
    assert "metadata" in result or "key" in result


def test_log_and_raise_delegates_to_enhanced() -> None:
    with patch("server.utils.error_logging.log_and_raise_enhanced") as mock_enhanced:
        mock_enhanced.side_effect = ValidationError("boom")
        with pytest.raises(ValidationError):
            log_and_raise(ValidationError, "boom", logger_name="test.module")
        mock_enhanced.assert_called_once()
        assert mock_enhanced.call_args.kwargs["skip_log_validation"] is False


def test_log_and_raise_http_delegates() -> None:
    with patch("server.utils.error_logging.log_and_raise_http_enhanced") as mock_http:
        mock_http.side_effect = HTTPException(status_code=400, detail="bad")
        with pytest.raises(HTTPException):
            log_and_raise_http(400, "bad", logger_name="test.module")
        mock_http.assert_called_once_with(400, "bad", logger_name="test.module")


def test_create_context_from_request_with_state() -> None:
    request = MagicMock(spec=Request)
    request.state.user_id = "user-1"
    request.state.session_id = "session-1"
    sentinel = MagicMock()
    with patch("server.utils.error_logging.create_enhanced_error_context", return_value=sentinel) as mock_ctx:
        result = create_context_from_request(request)
    assert result is sentinel
    mock_ctx.assert_called_once_with(request=request, user_id="user-1", session_id="session-1")


def test_create_context_from_request_none() -> None:
    sentinel = MagicMock()
    with patch("server.utils.error_logging.create_enhanced_error_context", return_value=sentinel) as mock_ctx:
        result = create_context_from_request(None)
    assert result is sentinel
    mock_ctx.assert_called_once_with(request=None, user_id=None, session_id=None)


def test_create_context_from_websocket() -> None:
    websocket = MagicMock(spec=WebSocket)
    websocket.state.user_id = "user-2"
    websocket.state.session_id = "session-2"
    sentinel = MagicMock()
    with patch("server.utils.error_logging.create_enhanced_error_context", return_value=sentinel) as mock_ctx:
        result = create_context_from_websocket(websocket)
    assert result is sentinel
    mock_ctx.assert_called_once_with(websocket=websocket, user_id="user-2", session_id="session-2")


def test_wrap_third_party_exception_delegates() -> None:
    exc = ValueError("upstream")
    wrapped = MagicMock(spec=MythosMUDError)
    with patch("server.utils.error_logging.wrap_third_party_exception_enhanced", return_value=wrapped) as mock_wrap:
        result = wrap_third_party_exception(exc, logger_name="test.module")
    assert result is wrapped
    mock_wrap.assert_called_once_with(exc, logger_name="test.module")


def test_log_error_with_context_delegates() -> None:
    exc = RuntimeError("fail")
    with patch("server.utils.error_logging.log_structured_error") as mock_log:
        log_error_with_context(exc, logger_name="test.module", level="warning", operation="x")
    mock_log.assert_called_once_with(exc, logger_name="test.module", level="warning", operation="x")


def test_create_logged_http_exception_delegates() -> None:
    http_exc = HTTPException(status_code=404, detail="missing")
    with patch(
        "server.utils.error_logging.create_logged_http_exception_enhanced",
        return_value=http_exc,
    ) as mock_create:
        result = create_logged_http_exception(404, "missing", logger_name="test.module")
    assert result is http_exc
    mock_create.assert_called_once_with(404, "missing", logger_name="test.module")
