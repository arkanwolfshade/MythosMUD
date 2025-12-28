"""
Pydantic error handler for consistent error processing.

This module provides a comprehensive error handler specifically designed
for processing Pydantic validation errors and converting them into
user-friendly messages and standardized error responses.

As noted in the Necronomicon: "The errors of the ancients must be
translated into terms the mortal mind can comprehend, lest madness take hold."
"""

from typing import Any

from pydantic import ValidationError

from ..error_types import (
    ErrorSeverity,
    ErrorType,
    create_sse_error_response,
    create_standard_error_response,
    create_websocket_error_response,
)
from ..exceptions import (
    ErrorContext,
    create_error_context,
)
from ..exceptions import (
    ValidationError as MythosValidationError,
)
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class PydanticErrorHandler:
    """
    Handler for processing Pydantic validation errors into user-friendly messages.

    This class provides methods to convert technical Pydantic validation errors
    into standardized error responses with appropriate user-friendly messages.
    """

    # Common field name mappings for user-friendly display
    FIELD_NAME_MAPPINGS = {
        "message": "message",
        "direction": "direction",
        "target_player": "target player",
        "alias_name": "alias name",
        "help_topic": "help topic",
        "filter_name": "filter name",
        "reason": "reason",
        "action": "action",
        "player_name": "player name",
        "command": "command",
    }

    # Common error type mappings
    ERROR_TYPE_MAPPINGS = {
        "missing": ErrorType.MISSING_REQUIRED_FIELD,
        "value_error": ErrorType.INVALID_INPUT,
        "type_error": ErrorType.INVALID_FORMAT,
        "extra_forbidden": ErrorType.VALIDATION_ERROR,
        "json_invalid": ErrorType.INVALID_FORMAT,
        "string_too_short": ErrorType.INVALID_INPUT,
        "string_too_long": ErrorType.INVALID_INPUT,
        "greater_than_equal": ErrorType.INVALID_INPUT,
        "less_than_equal": ErrorType.INVALID_INPUT,
    }

    def __init__(self, context: ErrorContext | None = None):
        """
        Initialize the Pydantic error handler.

        Args:
            context: Optional error context for logging and debugging
        """
        self.context = context or create_error_context()

    def handle_validation_error(
        self, error: ValidationError, model_class: type | None = None, response_type: str = "http"
    ) -> dict[str, Any]:
        """
        Handle a Pydantic ValidationError and convert it to a standardized response.

        Args:
            error: The Pydantic ValidationError to handle
            model_class: Optional model class for additional context
            response_type: Type of response ("http", "websocket", "sse")

        Returns:
            Standardized error response dictionary
        """
        try:
            # Extract error information
            error_info = self._extract_error_info(error, model_class)

            # Determine error type and severity
            error_type = self._determine_error_type(error_info)
            severity = self._determine_severity(error_info)

            # Generate user-friendly messages
            user_friendly = self._generate_user_friendly_message(error_info)

            # Create error details
            details = self._create_error_details(error_info, error)

            # Create appropriate response based on type
            if response_type == "websocket":
                return create_websocket_error_response(
                    error_type=error_type, message=error_info["message"], user_friendly=user_friendly, details=details
                )
            elif response_type == "sse":
                return create_sse_error_response(
                    error_type=error_type, message=error_info["message"], user_friendly=user_friendly, details=details
                )
            else:  # Default to HTTP
                return create_standard_error_response(
                    error_type=error_type,
                    message=error_info["message"],
                    user_friendly=user_friendly,
                    details=details,
                    severity=severity,
                )

        except Exception as e:
            # Fallback error handling
            logger.error("Error in PydanticErrorHandler", error=str(e), exc_info=True)
            return self._create_fallback_error_response(error, response_type)

    def _extract_error_info(self, error: ValidationError, model_class: type | None = None) -> dict[str, Any]:
        """
        Extract structured information from a Pydantic ValidationError.

        Args:
            error: The Pydantic ValidationError
            model_class: Optional model class for context

        Returns:
            Dictionary containing extracted error information
        """
        # AI Agent: Explicit typing to help mypy understand structure
        error_info: dict[str, Any] = {
            "message": str(error),
            "error_count": len(error.errors()),
            "errors": [],
            "model_class": model_class.__name__ if model_class else None,
            "fields_with_errors": set(),
        }

        for error_detail in error.errors():
            field_info = {
                "field": self._get_field_path(error_detail.get("loc", [])),  # type: ignore[arg-type]
                "error_type": error_detail.get("type", "unknown"),
                "message": error_detail.get("msg", "Unknown error"),
                "input_value": error_detail.get("input"),
                "context": error_detail.get("ctx", {}),
            }

            error_info["errors"].append(field_info)
            if field_info["field"]:
                error_info["fields_with_errors"].add(field_info["field"])

        return error_info

    def _get_field_path(self, location: list[str | int]) -> str:
        """
        Convert Pydantic error location to a readable field path.

        Args:
            location: Pydantic error location list

        Returns:
            Readable field path string
        """
        if not location:
            return ""

        # Filter out numeric indices and join with dots
        path_parts = [str(part) for part in location if not isinstance(part, int)]
        return ".".join(path_parts) if path_parts else ""

    def _determine_error_type(self, error_info: dict[str, Any]) -> ErrorType:
        """
        Determine the appropriate ErrorType based on error information.

        Args:
            error_info: Extracted error information

        Returns:
            Appropriate ErrorType enum value
        """
        # Check for specific error types
        for error in error_info["errors"]:
            error_type = error["error_type"]
            if error_type in self.ERROR_TYPE_MAPPINGS:
                return self.ERROR_TYPE_MAPPINGS[error_type]

        # Default to validation error
        return ErrorType.VALIDATION_ERROR

    def _determine_severity(self, error_info: dict[str, Any]) -> ErrorSeverity:
        """
        Determine the appropriate ErrorSeverity based on error information.

        Args:
            error_info: Extracted error information

        Returns:
            Appropriate ErrorSeverity enum value
        """
        # Check for critical errors
        for error in error_info["errors"]:
            error_type = error["error_type"]
            if error_type in ["extra_forbidden", "json_invalid"]:
                return ErrorSeverity.HIGH

        # Default to medium severity
        return ErrorSeverity.MEDIUM

    def _generate_user_friendly_message(self, error_info: dict[str, Any]) -> str:
        """
        Generate a user-friendly error message from error information.

        Args:
            error_info: Extracted error information

        Returns:
            User-friendly error message
        """
        if error_info["error_count"] == 1:
            # Single error - provide specific message
            error = error_info["errors"][0]
            field_name = self._get_display_field_name(error["field"])

            if error["error_type"] == "missing":
                return f"Please provide {field_name}"
            elif error["error_type"] == "value_error":
                return f"Invalid value for {field_name}"
            elif error["error_type"] == "type_error":
                return f"Invalid format for {field_name}"
            elif error["error_type"] == "string_too_short":
                min_length = error["context"].get("min_length", 1)
                return f"{field_name.capitalize()} must be at least {min_length} characters"
            elif error["error_type"] == "string_too_long":
                max_length = error["context"].get("max_length", 100)
                return f"{field_name.capitalize()} must be no more than {max_length} characters"
            elif error["error_type"] == "extra_forbidden":
                return "Invalid field provided"
            else:
                return f"Invalid {field_name}"
        else:
            # Multiple errors - provide general message
            field_count = len(error_info["fields_with_errors"])
            if field_count == 1:
                field_name = self._get_display_field_name(list(error_info["fields_with_errors"])[0])
                return f"Please check {field_name}"
            else:
                return f"Please check {field_count} fields"

    def _get_display_field_name(self, field_path: str) -> str:
        """
        Get a user-friendly display name for a field path.

        Args:
            field_path: Field path string

        Returns:
            User-friendly field name
        """
        if not field_path:
            return "input"

        # Use the last part of the path
        field_name = field_path.split(".")[-1]

        # Check for known mappings
        if field_name in self.FIELD_NAME_MAPPINGS:
            return self.FIELD_NAME_MAPPINGS[field_name]

        # Convert snake_case to readable format
        return field_name.replace("_", " ")

    def _create_error_details(self, error_info: dict[str, Any], original_error: ValidationError) -> dict[str, Any]:
        """
        Create detailed error information for debugging.

        Args:
            error_info: Extracted error information
            original_error: Original ValidationError

        Returns:
            Dictionary containing error details
        """
        details = {
            "validation_errors": [
                {
                    "field": error["field"],
                    "type": error["error_type"],
                    "message": error["message"],
                    "input": error["input_value"],
                }
                for error in error_info["errors"]
            ],
            "error_count": error_info["error_count"],
            "model_class": error_info["model_class"],
        }

        # Add context information
        if self.context:
            details["context"] = {
                "user_id": self.context.user_id,
                "session_id": self.context.session_id,
                "request_id": self.context.request_id,
            }

        return details

    def _create_fallback_error_response(self, error: ValidationError, response_type: str) -> dict[str, Any]:
        """
        Create a fallback error response when normal processing fails.

        Args:
            error: Original ValidationError
            response_type: Type of response to create

        Returns:
            Fallback error response
        """
        message = f"Validation error: {str(error)}"
        user_friendly = "Please check your input and try again"

        if response_type == "websocket":
            return create_websocket_error_response(
                error_type=ErrorType.VALIDATION_ERROR,
                message=message,
                user_friendly=user_friendly,
                details={"fallback": True},
            )
        elif response_type == "sse":
            return create_sse_error_response(
                error_type=ErrorType.VALIDATION_ERROR,
                message=message,
                user_friendly=user_friendly,
                details={"fallback": True},
            )
        else:
            return create_standard_error_response(
                error_type=ErrorType.VALIDATION_ERROR,
                message=message,
                user_friendly=user_friendly,
                details={"fallback": True},
                severity=ErrorSeverity.MEDIUM,
            )

    def convert_to_mythos_error(self, error: ValidationError, model_class: type | None = None) -> MythosValidationError:
        """
        Convert a Pydantic ValidationError to a MythosValidationError.

        Args:
            error: The Pydantic ValidationError
            model_class: Optional model class for context

        Returns:
            MythosValidationError instance
        """
        error_info = self._extract_error_info(error, model_class)
        user_friendly = self._generate_user_friendly_message(error_info)

        return MythosValidationError(
            message=str(error),
            context=self.context,
            details=self._create_error_details(error_info, error),
            user_friendly=user_friendly,
        )

    @classmethod
    def create_handler(cls, **context_kwargs) -> "PydanticErrorHandler":
        """
        Create a PydanticErrorHandler with specific context.

        Args:
            **context_kwargs: Context arguments for ErrorContext

        Returns:
            New PydanticErrorHandler instance
        """
        context = create_error_context(**context_kwargs)
        return cls(context=context)


# Convenience functions for common use cases
def handle_pydantic_error(
    error: ValidationError, model_class: type | None = None, response_type: str = "http", **context_kwargs
) -> dict[str, Any]:
    """
    Convenience function to handle a Pydantic ValidationError.

    Args:
        error: The Pydantic ValidationError to handle
        model_class: Optional model class for context
        response_type: Type of response ("http", "websocket", "sse")
        **context_kwargs: Context arguments for ErrorContext

    Returns:
        Standardized error response dictionary
    """
    handler = PydanticErrorHandler.create_handler(**context_kwargs)
    return handler.handle_validation_error(error, model_class, response_type)


def convert_pydantic_error(
    error: ValidationError, model_class: type | None = None, **context_kwargs
) -> MythosValidationError:
    """
    Convenience function to convert a Pydantic ValidationError to MythosValidationError.

    Args:
        error: The Pydantic ValidationError to convert
        model_class: Optional model class for context
        **context_kwargs: Context arguments for ErrorContext

    Returns:
        MythosValidationError instance
    """
    handler = PydanticErrorHandler.create_handler(**context_kwargs)
    return handler.convert_to_mythos_error(error, model_class)
