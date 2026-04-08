"""Tests for error handling middleware (user id extraction for logging context)."""

from typing import cast
from unittest.mock import MagicMock, patch

import pytest
from fastapi import Request
from starlette.types import Scope

from server.middleware.error_handling_middleware import (
    USER_ID_UNAVAILABLE,
    ErrorHandlingMiddleware,
    extract_user_id_from_non_mapping,
    request_id_from_scope,
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
