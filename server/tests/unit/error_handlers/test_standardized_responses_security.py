"""
Regression tests: API error responses must not leak raw exception text.

Covers CodeQL alerts #75, #76, #131 (information exposure through an exception).
"""

import json

import pytest
from fastapi import HTTPException
from pydantic import BaseModel, Field, ValidationError

from server.error_handlers.pydantic_error_handler import PydanticErrorHandler
from server.error_handlers.standardized_responses import StandardizedErrorResponse
from server.error_types import ErrorMessages


class _SampleModel(BaseModel):
    name: str = Field(min_length=3)


def _response_message(response) -> str:
    body = json.loads(response.body)
    return body["error"]["message"]


class TestStandardizedResponsesSecurity:
    """Public error.message must not echo exception strings or paths."""

    def test_generic_exception_does_not_expose_internal_message(self):
        handler = StandardizedErrorResponse()
        secret = "secret/path/to/db.py line 99"
        response = handler.handle_exception(RuntimeError(secret), include_details=True)

        message = _response_message(response)
        assert secret not in message
        assert message == ErrorMessages.INTERNAL_ERROR

    def test_http_exception_does_not_expose_raw_detail_in_message(self):
        handler = StandardizedErrorResponse()
        detail = "Internal failure at C:\\server\\module.py:42"
        response = handler.handle_exception(HTTPException(status_code=400, detail=detail))

        message = _response_message(response)
        assert detail not in message
        assert "module.py" not in message

    def test_pydantic_validation_error_does_not_expose_str_error_in_message(self):
        handler = StandardizedErrorResponse()
        with pytest.raises(ValidationError) as exc_info:
            _SampleModel(name="ab")

        response = handler.handle_exception(exc_info.value)
        message = _response_message(response)
        assert str(exc_info.value) not in message
        assert "ValidationError" not in message

    def test_generic_exception_does_not_expose_internal_message_in_details(self):
        handler = StandardizedErrorResponse()
        secret = "secret/path/to/db.py line 99"
        response = handler.handle_exception(RuntimeError(secret), include_details=True)

        body = json.loads(response.body)
        details = body["error"].get("details", {})
        details_blob = json.dumps(details)
        assert secret not in details_blob
        assert "exception_message" not in details

    def test_pydantic_convert_to_mythos_error_does_not_use_str_error_as_message(self):
        with pytest.raises(ValidationError) as exc_info:
            _SampleModel(name="ab")

        mythos_error = PydanticErrorHandler().convert_to_mythos_error(exc_info.value)
        assert str(exc_info.value) not in mythos_error.message
        assert mythos_error.message == ErrorMessages.INVALID_INPUT
