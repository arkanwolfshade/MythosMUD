"""Unit tests for unified command request app-state extraction."""

from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import MagicMock

from server.command_handler.command_execution_request import command_request_app_state
from server.realtime.request_context import WebSocketRequestContext


def test_command_request_app_state_from_http_request_like_object() -> None:
    """Returns app.state for HTTP/FastAPI-style request objects."""
    state = SimpleNamespace(persistence=object())
    request_like = SimpleNamespace(app=SimpleNamespace(state=state))
    assert command_request_app_state(request_like) is state


def test_command_request_app_state_from_websocket_request_context() -> None:
    """Returns app.state for WebSocketRequestContext."""
    app_state = MagicMock()
    ws_ctx = WebSocketRequestContext(app_state)
    assert command_request_app_state(ws_ctx) is app_state


def test_command_request_app_state_missing_app_or_state_returns_none() -> None:
    """Gracefully returns None when app or state is absent."""
    assert command_request_app_state(SimpleNamespace()) is None
    assert command_request_app_state(SimpleNamespace(app=SimpleNamespace())) is None
