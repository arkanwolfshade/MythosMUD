"""
Error handlers package for MythosMUD.

This package provides specialized error handlers for different types of errors
and error processing scenarios.

IMPORTANT NOTE ON LEGACY CODE:
This package was created during the Pydantic audit to provide modular error handling.
Legacy error handling functions are in server/legacy_error_handlers.py and should be
gradually migrated to use the new modular handlers.

For new code, use:
    from server.error_handlers import PydanticErrorHandler, StandardizedErrorResponse

For legacy code that needs the old functions:
    from server.legacy_error_handlers import create_error_response, sanitize_html_content, ...
"""

# Import from new modular handlers
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
    # New modular handlers
    "PydanticErrorHandler",
    "handle_pydantic_error",
    "convert_pydantic_error",
    "StandardizedErrorResponse",
    "create_standardized_error_response",
    "handle_api_error",
]
