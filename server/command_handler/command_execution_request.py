"""HTTP Request or WebSocketRequestContext for unified command processing."""

from __future__ import annotations

from fastapi import Request

from ..realtime.request_context import WebSocketRequestContext

CommandExecutionRequest = Request | WebSocketRequestContext


def command_request_app_state(request: CommandExecutionRequest) -> object | None:
    """
    Return app.state for HTTP Request or WebSocketRequestContext (duck-typed).

    Avoids request.app.state attribute access, which pyright cannot verify on the union.
    """
    app = getattr(request, "app", None)
    if app is None:
        return None
    return getattr(app, "state", None)
