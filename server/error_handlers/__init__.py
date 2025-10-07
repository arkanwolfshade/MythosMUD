"""
Error handlers package for MythosMUD.

This package provides specialized error handlers for different types of errors
and error processing scenarios.
"""

from .pydantic_error_handler import (
    PydanticErrorHandler,
    convert_pydantic_error,
    handle_pydantic_error,
)
from .standardized_responses import (
    StandardizedErrorResponse,
    create_standardized_error_response,
    handle_api_error,
)

__all__ = [
    "PydanticErrorHandler",
    "handle_pydantic_error",
    "convert_pydantic_error",
    "StandardizedErrorResponse",
    "create_standardized_error_response",
    "handle_api_error",
]
