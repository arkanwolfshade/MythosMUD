"""Unit tests for correlation ID middleware."""

import uuid
from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from starlette.types import Scope

from server.middleware.correlation_middleware import (
    CorrelationMiddleware,
    WebSocketCorrelationMiddleware,
    _get_header,
    create_correlation_middleware,
    create_websocket_correlation_middleware,
)


def test_get_header_case_insensitive() -> None:
    scope: Scope = {
        "headers": [
            (b"x-correlation-id", b"corr-123"),
            (b"User-Agent", b"pytest"),
        ]
    }
    assert _get_header(scope, "X-Correlation-ID") == "corr-123"
    assert _get_header(scope, "user-agent") == "pytest"
    assert _get_header(scope, "missing") is None


def test_create_correlation_middleware_factory() -> None:
    factory = create_correlation_middleware("X-Trace-ID")
    inner = MagicMock()
    middleware = factory(inner)
    assert isinstance(middleware, CorrelationMiddleware)
    assert middleware.correlation_header == "X-Trace-ID"


def test_create_websocket_correlation_middleware() -> None:
    ws_middleware = create_websocket_correlation_middleware("X-Trace-ID")
    assert isinstance(ws_middleware, WebSocketCorrelationMiddleware)
    assert ws_middleware.correlation_header == "X-Trace-ID"


@pytest.mark.asyncio
async def test_correlation_middleware_passes_non_http() -> None:
    inner = AsyncMock()
    middleware = CorrelationMiddleware(inner)
    scope: Scope = {"type": "websocket"}
    receive = AsyncMock()
    send = AsyncMock()
    await middleware(scope, receive, send)
    inner.assert_awaited_once_with(scope, receive, send)


@pytest.mark.asyncio
async def test_correlation_middleware_generates_correlation_id() -> None:
    inner = AsyncMock()
    middleware = CorrelationMiddleware(inner)
    scope: Scope = {
        "type": "http",
        "method": "GET",
        "path": "/health",
        "query_string": b"",
        "headers": [],
        "client": ("127.0.0.1", 12345),
    }
    receive = AsyncMock()
    sent: list[Any] = []

    async def capture_send(message: Any) -> None:
        sent.append(message)

    with (
        patch("server.middleware.correlation_middleware.bind_request_context") as bind_ctx,
        patch("server.middleware.correlation_middleware.clear_request_context") as clear_ctx,
        patch(
            "server.middleware.correlation_middleware.uuid.uuid4",
            return_value=uuid.UUID("00000000-0000-0000-0000-000000000001"),
        ),
    ):
        await middleware(scope, receive, capture_send)

    inner.assert_awaited_once()
    bind_ctx.assert_called_once()
    clear_ctx.assert_called_once()
    assert bind_ctx.call_args.kwargs["correlation_id"] == "00000000-0000-0000-0000-000000000001"


@pytest.mark.asyncio
async def test_correlation_middleware_uses_existing_header() -> None:
    inner = AsyncMock()
    middleware = CorrelationMiddleware(inner)
    scope: Scope = {
        "type": "http",
        "method": "POST",
        "path": "/api",
        "query_string": b"q=1",
        "headers": [(b"x-correlation-id", b"existing-id")],
        "client": ("10.0.0.1", 80),
    }
    receive = AsyncMock()

    async def noop_send(_message: Any) -> None:
        return None

    with patch("server.middleware.correlation_middleware.bind_request_context") as bind_ctx:
        await middleware(scope, receive, noop_send)

    assert bind_ctx.call_args.kwargs["correlation_id"] == "existing-id"


@pytest.mark.asyncio
async def test_correlation_middleware_adds_response_header() -> None:
    inner = AsyncMock()

    async def inner_with_response(scope: Scope, receive: Any, send: Any) -> None:
        await send({"type": "http.response.start", "status": 200, "headers": []})

    inner.side_effect = inner_with_response
    middleware = CorrelationMiddleware(inner, "X-Correlation-ID")
    scope: Scope = {
        "type": "http",
        "method": "GET",
        "path": "/",
        "query_string": b"",
        "headers": [(b"x-correlation-id", b"resp-id")],
        "client": None,
    }
    receive = AsyncMock()
    forwarded: list[Any] = []

    async def capture_send(message: Any) -> None:
        forwarded.append(message)

    with patch("server.middleware.correlation_middleware.clear_request_context"):
        await middleware(scope, receive, capture_send)

    start_messages = [m for m in forwarded if m["type"] == "http.response.start"]
    assert start_messages
    header_names = [h[0].decode() for h in start_messages[0]["headers"]]
    assert "x-correlation-id" in header_names


@pytest.mark.asyncio
async def test_correlation_middleware_reraises_exception() -> None:
    inner = AsyncMock(side_effect=ValueError("boom"))
    middleware = CorrelationMiddleware(inner)
    scope: Scope = {
        "type": "http",
        "method": "GET",
        "path": "/fail",
        "query_string": b"",
        "headers": [],
        "client": None,
    }
    receive = AsyncMock()
    send = AsyncMock()

    with (
        patch("server.middleware.correlation_middleware.clear_request_context"),
        pytest.raises(ValueError, match="boom"),
    ):
        await middleware(scope, receive, send)


@pytest.mark.asyncio
async def test_websocket_correlation_middleware() -> None:
    websocket = MagicMock()
    websocket.headers = {"X-Correlation-ID": "ws-corr"}
    websocket.url = MagicMock(path="/ws/game")
    websocket.url.__str__ = MagicMock(return_value="ws://localhost/ws/game")
    websocket.query_params = {}
    websocket.client = MagicMock(host="127.0.0.1")
    call_next = AsyncMock(return_value={"ok": True})

    with (
        patch("server.middleware.correlation_middleware.bind_request_context") as bind_ctx,
        patch("server.middleware.correlation_middleware.clear_request_context") as clear_ctx,
    ):
        middleware = WebSocketCorrelationMiddleware()
        result = await middleware(websocket, call_next)

    assert result == {"ok": True}
    bind_ctx.assert_called_once()
    clear_ctx.assert_called_once()
    call_next.assert_awaited_once_with(websocket)


@pytest.mark.asyncio
async def test_websocket_correlation_middleware_generates_id() -> None:
    websocket = MagicMock()
    websocket.headers = {}
    websocket.url = MagicMock(path="/ws")
    websocket.url.__str__ = MagicMock(return_value="ws://localhost/ws")
    websocket.query_params = {}
    websocket.client = None
    call_next = AsyncMock(return_value=None)

    with (
        patch("server.middleware.correlation_middleware.bind_request_context") as bind_ctx,
        patch("server.middleware.correlation_middleware.clear_request_context"),
        patch(
            "server.middleware.correlation_middleware.uuid.uuid4",
            return_value=uuid.UUID("00000000-0000-0000-0000-000000000002"),
        ),
    ):
        middleware = WebSocketCorrelationMiddleware()
        await middleware(websocket, call_next)

    assert bind_ctx.call_args.kwargs["correlation_id"] == "00000000-0000-0000-0000-000000000002"
