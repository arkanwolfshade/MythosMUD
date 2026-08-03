"""Tests for error handling middleware (user id extraction for logging context)."""

from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from starlette.types import Scope

from server.exceptions import LoggedHTTPException, MythosMUDError
from server.middleware.error_handling_middleware import (
    USER_ID_UNAVAILABLE,
    ErrorHandlingMiddleware,
    add_error_handling_middleware,
    extract_user_id_from_non_mapping,
    register_error_handlers,
    request_id_from_scope,
    setup_error_handling,
)


def _error_log_kwargs(log_mock: object) -> dict[str, object]:
    """Keyword args passed to logger.error from a unittest.mock patch (no MagicMock Any chain)."""
    err = cast(object | None, getattr(log_mock, "error", None))
    call_args = cast(object | None, getattr(err, "call_args", None)) if err is not None else None
    raw_kw = cast(object | None, getattr(call_args, "kwargs", None)) if call_args is not None else None
    if raw_kw is None:
        return {}
    return cast(dict[str, object], raw_kw)


class _UserWithId:
    id: object

    def __init__(self, uid: object) -> None:
        self.id = uid


class _UserWithGet:
    _result: object | BaseException

    def __init__(self, result: object | BaseException) -> None:
        self._result = result

    def get(self, key: str) -> object:
        if isinstance(self._result, BaseException):
            raise self._result
        if key == "id":
            return self._result
        return None


@pytest.mark.parametrize(
    ("scope", "expected"),
    [
        ({}, None),
        ({"state": "not-a-mapping"}, None),
        ({"state": {"request_id": "rid-1"}}, "rid-1"),
        ({"state": {"request_id": None}}, None),
    ],
)
def test_request_id_from_scope(scope: Scope, expected: str | None) -> None:
    assert request_id_from_scope(scope) == expected


def test_request_id_from_scope_non_str_coerced() -> None:
    scope: Scope = {"state": {"request_id": 99}}
    assert request_id_from_scope(scope) == "99"


@pytest.mark.parametrize(
    ("user", "expected"),
    [
        (_UserWithId("player-1"), "player-1"),
        (_UserWithGet("player-2"), "player-2"),
        (_UserWithGet(KeyError("id")), USER_ID_UNAVAILABLE),
        (_UserWithGet(TypeError("bad")), USER_ID_UNAVAILABLE),
        (object(), USER_ID_UNAVAILABLE),
    ],
)
def test_extract_user_id_from_non_mapping(user: object, expected: object) -> None:
    result = extract_user_id_from_non_mapping(user)
    if expected is USER_ID_UNAVAILABLE:
        assert result is USER_ID_UNAVAILABLE
    else:
        assert result == expected


def test_log_exception_adds_user_id_for_mapping_user() -> None:
    mw = ErrorHandlingMiddleware(MagicMock())
    scope: Scope = {
        "type": "http",
        "asgi": {"version": "3.0", "spec_version": "2.3"},
        "http_version": "1.1",
        "method": "GET",
        "scheme": "http",
        "path": "/",
        "raw_path": b"/",
        "query_string": b"",
        "headers": [],
        "client": ("127.0.0.1", 50000),
        "server": ("testserver", 80),
        "state": {"request_id": "req-1"},
    }
    request = Request(scope)
    request.state.user = {"id": "from-dict"}

    with patch("server.middleware.error_handling_middleware.logger") as log_mock:
        mw.log_exception(request, ValueError("boom"), 500)

    kwargs = _error_log_kwargs(log_mock)
    assert kwargs.get("user_id") == "from-dict"


def test_log_exception_mapping_user_missing_id_sets_none() -> None:
    mw = ErrorHandlingMiddleware(MagicMock())
    scope: Scope = {
        "type": "http",
        "asgi": {"version": "3.0", "spec_version": "2.3"},
        "http_version": "1.1",
        "method": "GET",
        "scheme": "http",
        "path": "/",
        "raw_path": b"/",
        "query_string": b"",
        "headers": [],
        "client": ("127.0.0.1", 50000),
        "server": ("testserver", 80),
        "state": {"request_id": "req-2"},
    }
    request = Request(scope)
    request.state.user = {}

    with patch("server.middleware.error_handling_middleware.logger") as log_mock:
        mw.log_exception(request, ValueError("boom"), 500)

    kwargs = _error_log_kwargs(log_mock)
    assert "user_id" in kwargs
    assert kwargs["user_id"] is None


def _http_scope() -> Scope:
    return {
        "type": "http",
        "asgi": {"version": "3.0", "spec_version": "2.3"},
        "http_version": "1.1",
        "method": "GET",
        "scheme": "http",
        "path": "/",
        "raw_path": b"/",
        "query_string": b"",
        "headers": [],
        "client": ("127.0.0.1", 50000),
        "server": ("testserver", 80),
        "state": {},
    }


@pytest.mark.asyncio
async def test_call_passes_through_non_http() -> None:
    app = AsyncMock()
    mw = ErrorHandlingMiddleware(app)
    scope: Scope = {"type": "websocket"}
    receive = AsyncMock()
    send = AsyncMock()
    await mw(scope, receive, send)
    app.assert_awaited_once_with(scope, receive, send)


@pytest.mark.asyncio
async def test_call_sets_request_id_and_success() -> None:
    app = AsyncMock()
    mw = ErrorHandlingMiddleware(app)
    scope = _http_scope()
    await mw(scope, AsyncMock(), AsyncMock())
    assert "request_id" in scope["state"]
    app.assert_awaited_once()


@pytest.mark.asyncio
async def test_call_handles_exception() -> None:
    async def boom(_scope: Scope, _receive: object, _send: object) -> None:
        raise ValueError("explode")

    mw = ErrorHandlingMiddleware(boom)
    send = AsyncMock()
    await mw(_http_scope(), AsyncMock(), send)
    assert send.await_count >= 2


@pytest.mark.asyncio
async def test_handle_exception_fallback_when_handler_fails() -> None:
    mw = ErrorHandlingMiddleware(MagicMock())
    send = AsyncMock()
    with patch(
        "server.middleware.error_handling_middleware.StandardizedErrorResponse",
        side_effect=RuntimeError("handler broken"),
    ):
        await mw._handle_exception(_http_scope(), AsyncMock(), send, ValueError("orig"))
    assert send.await_count >= 2


@pytest.mark.asyncio
async def test_dispatch_success_and_exception() -> None:
    mw = ErrorHandlingMiddleware(MagicMock())
    request = Request(_http_scope())

    async def ok(_req: Request) -> JSONResponse:
        return JSONResponse({"ok": True})

    response = await mw.dispatch(request, ok)
    assert response.status_code == 200

    async def fail(_req: Request) -> JSONResponse:
        raise ValueError("dispatch boom")

    err_response = await mw.dispatch(request, fail)
    assert err_response.status_code >= 400


def test_log_exception_levels_and_session() -> None:
    mw = ErrorHandlingMiddleware(MagicMock())
    request = Request(_http_scope())
    request.state.request_id = "r1"
    request.state.session_id = "s1"
    request.state.user = _UserWithId("u1")

    with patch("server.middleware.error_handling_middleware.logger") as log_mock:
        mw.log_exception(request, ValueError("client"), 400)
        log_mock.warning.assert_called()
        mw.log_exception(request, ValueError("info"), 200)
        log_mock.info.assert_called()
        mw.log_exception(request, MythosMUDError("already logged"), 500)


def test_add_register_setup_error_handling() -> None:
    app = FastAPI()
    add_error_handling_middleware(app, include_details=True)
    register_error_handlers(app, include_details=False)
    setup_error_handling(FastAPI(), include_details=True)


@pytest.mark.asyncio
async def test_registered_exception_handlers_return_json() -> None:
    app = FastAPI()
    register_error_handlers(app, include_details=True)
    request = Request(_http_scope())

    mythos_handler = app.exception_handlers[MythosMUDError]
    resp = await mythos_handler(request, MythosMUDError("x"))
    assert isinstance(resp, JSONResponse)

    http_handler = app.exception_handlers[HTTPException]
    resp2 = await http_handler(request, HTTPException(status_code=404, detail="missing"))
    assert isinstance(resp2, JSONResponse)

    logged_handler = app.exception_handlers[LoggedHTTPException]
    resp3 = await logged_handler(request, LoggedHTTPException(status_code=400, detail="bad"))
    assert isinstance(resp3, JSONResponse)

    generic = app.exception_handlers[Exception]
    resp4 = await generic(request, RuntimeError("generic"))
    assert isinstance(resp4, JSONResponse)
