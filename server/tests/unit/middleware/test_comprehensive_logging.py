"""Unit tests for comprehensive logging middleware."""

from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import Request
from starlette.types import Scope

from server.middleware.comprehensive_logging import ComprehensiveLoggingMiddleware


@pytest.mark.asyncio
async def test_comprehensive_logging_passes_non_http() -> None:
    inner = AsyncMock()
    middleware = ComprehensiveLoggingMiddleware(inner)
    scope: Scope = {"type": "websocket"}
    receive = AsyncMock()
    send = AsyncMock()
    await middleware(scope, receive, send)
    inner.assert_awaited_once_with(scope, receive, send)


@pytest.mark.asyncio
async def test_comprehensive_logging_successful_request() -> None:
    inner = AsyncMock()

    async def inner_with_response(scope: Scope, receive: Any, send: Any) -> None:
        await send({"type": "http.response.start", "status": 200, "headers": []})

    inner.side_effect = inner_with_response
    middleware = ComprehensiveLoggingMiddleware(inner)
    scope: Scope = {
        "type": "http",
        "method": "GET",
        "path": "/health",
        "query_string": b"",
        "headers": [(b"user-agent", b"pytest")],
        "client": ("127.0.0.1", 12345),
        "scheme": "http",
        "server": ("localhost", 54768),
    }
    receive = AsyncMock()
    forwarded: list[Any] = []

    async def capture_send(message: Any) -> None:
        forwarded.append(message)

    with patch("server.middleware.comprehensive_logging.logger") as log_mock:
        await middleware(scope, receive, capture_send)

    inner.assert_awaited_once()
    assert any(m["type"] == "http.response.start" for m in forwarded)
    assert log_mock.info.call_count >= 2


@pytest.mark.asyncio
async def test_comprehensive_logging_reraises_exception() -> None:
    inner = AsyncMock(side_effect=RuntimeError("boom"))
    middleware = ComprehensiveLoggingMiddleware(inner)
    scope: Scope = {
        "type": "http",
        "method": "POST",
        "path": "/fail",
        "query_string": b"",
        "headers": [],
        "client": None,
        "scheme": "http",
        "server": ("localhost", 54768),
    }
    receive = AsyncMock()
    send = AsyncMock()

    with (
        patch("server.middleware.comprehensive_logging.logger") as log_mock,
        pytest.raises(RuntimeError, match="boom"),
    ):
        await middleware(scope, receive, send)

    log_mock.error.assert_called_once()


@pytest.mark.asyncio
async def test_comprehensive_logging_dispatch_success() -> None:
    middleware = ComprehensiveLoggingMiddleware(MagicMock())
    request = MagicMock(spec=Request)
    request.method = "GET"
    request.url = MagicMock()
    request.url.__str__ = MagicMock(return_value="http://localhost/health")
    request.url.path = "/health"
    request.client = MagicMock(host="127.0.0.1")
    request.headers = MagicMock()
    request.headers.get = MagicMock(return_value="pytest")
    response = MagicMock(status_code=200)
    call_next = AsyncMock(return_value=response)

    with patch("server.middleware.comprehensive_logging.logger"):
        result = await middleware.dispatch(request, call_next)

    assert result is response
    call_next.assert_awaited_once_with(request)


@pytest.mark.asyncio
async def test_comprehensive_logging_dispatch_error() -> None:
    middleware = ComprehensiveLoggingMiddleware(MagicMock())
    request = MagicMock(spec=Request)
    request.method = "DELETE"
    request.url = MagicMock()
    request.url.__str__ = MagicMock(return_value="http://localhost/api")
    request.url.path = "/api"
    request.client = None
    request.headers = MagicMock()
    request.headers.get = MagicMock(return_value="Not provided")
    call_next = AsyncMock(side_effect=ValueError("fail"))

    with (
        patch("server.middleware.comprehensive_logging.logger") as log_mock,
        pytest.raises(ValueError, match="fail"),
    ):
        await middleware.dispatch(request, call_next)

    log_mock.error.assert_called_once()


def test_log_request_start_long_auth_header() -> None:
    middleware = ComprehensiveLoggingMiddleware(MagicMock())
    request = MagicMock(spec=Request)
    request.method = "GET"
    request.url = MagicMock()
    request.url.__str__ = MagicMock(return_value="http://localhost/x")
    request.client = MagicMock(host="10.0.0.1")
    request.headers = MagicMock()
    request.headers.get = MagicMock(
        side_effect=lambda key, default=None: {
            "Authorization": "Bearer " + ("x" * 40),
            "user-agent": "pytest",
            "content-type": "application/json",
        }.get(key, default)
    )

    with patch("server.middleware.comprehensive_logging.logger") as log_mock:
        middleware._log_request_start(request)

    assert log_mock.info.called
    assert log_mock.debug.called
