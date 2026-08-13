"""Unit tests for standardized error response helpers beyond security regression."""

from __future__ import annotations

import json
import uuid
from unittest.mock import MagicMock

from fastapi import HTTPException, Request
from starlette.datastructures import URL, Headers

from server.error_handlers.standardized_responses import (
    StandardizedErrorResponse,
    _contains_file_path_in_exception,
    _contains_sensitive_exception_pattern,
    create_standardized_error_response,
    handle_api_error,
)
from server.error_types import ErrorType
from server.exceptions import DatabaseError, LoggedHTTPException, MythosMUDError, ResourceNotFoundError


def _response_body(response) -> dict:
    return json.loads(response.body)


def test_contains_sensitive_exception_pattern_detects_traceback() -> None:
    assert _contains_sensitive_exception_pattern("error traceback in server") is True
    assert _contains_sensitive_exception_pattern("player not found") is False


def test_contains_file_path_in_exception() -> None:
    assert _contains_file_path_in_exception("failed at C:\\server\\module.py", "c:\\server\\module.py") is True
    assert _contains_file_path_in_exception("no path here", "no path here") is False


def test_extract_context_without_request() -> None:
    handler = StandardizedErrorResponse()
    assert handler.context.user_id is None


def test_extract_user_id_from_state_dict_user() -> None:
    state = MagicMock()
    state.user = {"id": str(uuid.uuid4())}
    user_id = StandardizedErrorResponse._extract_user_id_from_state(state)
    assert user_id is not None


def test_map_status_code_to_error_type() -> None:
    handler = StandardizedErrorResponse()
    assert handler._map_status_code_to_error_type(404) == ErrorType.RESOURCE_NOT_FOUND
    assert handler._map_status_code_to_error_type(429) == ErrorType.RATE_LIMIT_EXCEEDED
    assert handler._map_status_code_to_error_type(999) == ErrorType.INTERNAL_ERROR


def test_handle_mythos_error_response() -> None:
    handler = StandardizedErrorResponse()
    error = ResourceNotFoundError("room missing")
    response = handler.handle_exception(error)
    body = _response_body(response)
    assert body["error"]["type"] == ErrorType.RESOURCE_NOT_FOUND.value
    assert response.status_code == 404


def test_handle_logged_http_exception() -> None:
    handler = StandardizedErrorResponse()
    exc = LoggedHTTPException(status_code=403, detail="forbidden zone")
    response = handler.handle_exception(exc)
    assert response.status_code == 403
    body = _response_body(response)
    assert "forbidden zone" not in body["error"]["message"]


def test_handle_http_exception_not_found() -> None:
    handler = StandardizedErrorResponse()
    response = handler.handle_exception(HTTPException(status_code=404, detail="missing"))
    assert response.status_code == 404


def test_sanitize_exception_message_strips_paths() -> None:
    handler = StandardizedErrorResponse()
    sanitized = handler._sanitize_exception_message("boom at /home/user/app.py line 12")
    assert "/home/" not in sanitized
    assert "line:" not in sanitized.lower()


def test_create_error_details_without_include() -> None:
    handler = StandardizedErrorResponse()
    error = MythosMUDError("bad input")
    details = handler._create_error_details(error, include_details=False)
    assert details == {}


def test_create_fallback_response() -> None:
    handler = StandardizedErrorResponse()
    response = handler._create_fallback_response(RuntimeError("x"), "http")
    assert response.status_code == 500


def test_create_standardized_error_response_factory() -> None:
    handler = create_standardized_error_response()
    assert isinstance(handler, StandardizedErrorResponse)


def test_handle_api_error_convenience() -> None:
    scope = {
        "type": "http",
        "method": "GET",
        "path": "/test",
        "headers": [],
    }
    request = Request(scope)
    request._url = URL("http://testserver/test")  # noqa: SLF001
    request._headers = Headers({})  # noqa: SLF001
    response = handle_api_error(HTTPException(status_code=400, detail="bad"), request=request)
    assert response.status_code == 400


def test_determine_error_type_from_exception_uses_attr() -> None:
    handler = StandardizedErrorResponse()
    error = DatabaseError("db down")
    assert handler._determine_error_type_from_exception(error) == ErrorType.DATABASE_ERROR
