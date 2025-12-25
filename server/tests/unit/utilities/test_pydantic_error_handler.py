"""
Tests for PydanticErrorHandler.

This module tests the PydanticErrorHandler class to ensure it correctly
processes Pydantic validation errors and converts them to user-friendly
messages and standardized error responses.
"""

import pytest
from pydantic import ValidationError

from server.error_handlers.pydantic_error_handler import (
    PydanticErrorHandler,
    convert_pydantic_error,
    handle_pydantic_error,
)
from server.error_types import ErrorSeverity, ErrorType
from server.exceptions import ValidationError as MythosValidationError
from server.models.alias import Alias
from server.models.command import SayCommand


class TestPydanticErrorHandler:
    """Test PydanticErrorHandler functionality."""

    def test_pydantic_error_handler_initialization(self) -> None:
        """Test that PydanticErrorHandler initializes correctly."""
        handler = PydanticErrorHandler()
        assert handler is not None
        assert handler.context is not None

    def test_handle_validation_error_missing_field(self) -> None:
        """Test handling of ValidationError with missing required field."""
        # Create a ValidationError for missing required field
        with pytest.raises(ValidationError) as exc_info:
            SayCommand()  # type: ignore[call-arg]  # Missing required message field

        validation_error = exc_info.value
        handler = PydanticErrorHandler()

        response = handler.handle_validation_error(validation_error, SayCommand)

        assert "error" in response
        error = response["error"]
        assert error["type"] == "missing_required_field"
        assert "Please provide message" in error["user_friendly"]
        assert error["severity"] == "medium"

    def test_handle_validation_error_invalid_type(self) -> None:
        """Test handling of ValidationError with invalid data type."""
        # Create a ValidationError for invalid data type
        with pytest.raises(ValidationError) as exc_info:
            Alias(name=123, command=456)  # Wrong data types

        validation_error = exc_info.value
        handler = PydanticErrorHandler()

        response = handler.handle_validation_error(validation_error, Alias)

        assert "error" in response
        error = response["error"]
        assert error["type"] in ["invalid_format", "validation_error"]
        # With multiple errors, it should show a general message
        assert "Please check" in error["user_friendly"]

    def test_handle_validation_error_websocket_response(self) -> None:
        """Test handling of ValidationError with WebSocket response type."""
        with pytest.raises(ValidationError) as exc_info:
            SayCommand()  # type: ignore[call-arg]

        validation_error = exc_info.value
        handler = PydanticErrorHandler()

        response = handler.handle_validation_error(validation_error, SayCommand, "websocket")

        assert response["type"] == "error"
        assert response["error_type"] == "missing_required_field"
        assert "Please provide message" in response["user_friendly"]

    def test_handle_validation_error_sse_response(self) -> None:
        """Test handling of ValidationError with SSE response type."""
        with pytest.raises(ValidationError) as exc_info:
            SayCommand()  # type: ignore[call-arg]

        validation_error = exc_info.value
        handler = PydanticErrorHandler()

        response = handler.handle_validation_error(validation_error, SayCommand, "sse")

        assert response["type"] == "error"
        assert response["error_type"] == "missing_required_field"
        assert "Please provide message" in response["user_friendly"]

    def test_convert_to_mythos_error(self) -> None:
        """Test conversion of ValidationError to MythosValidationError."""
        with pytest.raises(ValidationError) as exc_info:
            SayCommand()  # type: ignore[call-arg]

        validation_error = exc_info.value
        handler = PydanticErrorHandler()

        mythos_error = handler.convert_to_mythos_error(validation_error, SayCommand)

        assert isinstance(mythos_error, MythosValidationError)
        assert mythos_error.message == str(validation_error)
        assert "Please provide message" in mythos_error.user_friendly
        assert mythos_error.context is not None

    def test_extract_error_info(self) -> None:
        """Test extraction of error information from ValidationError."""
        with pytest.raises(ValidationError) as exc_info:
            SayCommand()  # type: ignore[call-arg]

        validation_error = exc_info.value
        handler = PydanticErrorHandler()

        error_info = handler._extract_error_info(validation_error, SayCommand)

        assert error_info["message"] == str(validation_error)
        assert error_info["error_count"] > 0
        assert error_info["model_class"] == "SayCommand"
        assert len(error_info["errors"]) > 0
        assert len(error_info["fields_with_errors"]) > 0

    def test_get_field_path(self) -> None:
        """Test conversion of Pydantic error location to field path."""
        handler = PydanticErrorHandler()

        # Test simple field path
        assert handler._get_field_path(["message"]) == "message"

        # Test nested field path
        assert handler._get_field_path(["data", "message"]) == "data.message"

        # Test with numeric indices (should be filtered out)
        assert handler._get_field_path(["items", 0, "name"]) == "items.name"

        # Test empty location
        assert handler._get_field_path([]) == ""

    def test_determine_error_type(self) -> None:
        """Test determination of ErrorType from error information."""
        handler = PydanticErrorHandler()

        # Test missing field error
        error_info = {"errors": [{"error_type": "missing", "field": "message"}]}
        assert handler._determine_error_type(error_info) == ErrorType.MISSING_REQUIRED_FIELD

        # Test value error
        error_info = {"errors": [{"error_type": "value_error", "field": "message"}]}
        assert handler._determine_error_type(error_info) == ErrorType.INVALID_INPUT

        # Test type error
        error_info = {"errors": [{"error_type": "type_error", "field": "message"}]}
        assert handler._determine_error_type(error_info) == ErrorType.INVALID_FORMAT

        # Test unknown error type
        error_info = {"errors": [{"error_type": "unknown_error", "field": "message"}]}
        assert handler._determine_error_type(error_info) == ErrorType.VALIDATION_ERROR

    def test_determine_severity(self) -> None:
        """Test determination of ErrorSeverity from error information."""
        handler = PydanticErrorHandler()

        # Test high severity error
        error_info = {"errors": [{"error_type": "extra_forbidden", "field": "message"}]}
        assert handler._determine_severity(error_info) == ErrorSeverity.HIGH

        # Test medium severity error (default)
        error_info = {"errors": [{"error_type": "missing", "field": "message"}]}
        assert handler._determine_severity(error_info) == ErrorSeverity.MEDIUM

    def test_generate_user_friendly_message_single_error(self) -> None:
        """Test generation of user-friendly message for single error."""
        handler = PydanticErrorHandler()

        # Test missing field
        error_info = {
            "error_count": 1,
            "errors": [{"error_type": "missing", "field": "message"}],
            "fields_with_errors": {"message"},
        }
        message = handler._generate_user_friendly_message(error_info)
        assert "Please provide message" in message

        # Test value error
        error_info = {
            "error_count": 1,
            "errors": [{"error_type": "value_error", "field": "message"}],
            "fields_with_errors": {"message"},
        }
        message = handler._generate_user_friendly_message(error_info)
        assert "Invalid value for message" in message

        # Test type error
        error_info = {
            "error_count": 1,
            "errors": [{"error_type": "type_error", "field": "message"}],
            "fields_with_errors": {"message"},
        }
        message = handler._generate_user_friendly_message(error_info)
        assert "Invalid format for message" in message

    def test_generate_user_friendly_message_multiple_errors(self) -> None:
        """Test generation of user-friendly message for multiple errors."""
        handler = PydanticErrorHandler()

        # Test multiple fields
        error_info = {
            "error_count": 2,
            "errors": [{"error_type": "missing", "field": "message"}, {"error_type": "missing", "field": "target"}],
            "fields_with_errors": {"message", "target"},
        }
        message = handler._generate_user_friendly_message(error_info)
        assert "Please check 2 fields" in message

        # Test single field with multiple errors
        error_info = {
            "error_count": 2,
            "errors": [
                {"error_type": "missing", "field": "message"},
                {"error_type": "value_error", "field": "message"},
            ],
            "fields_with_errors": {"message"},
        }
        message = handler._generate_user_friendly_message(error_info)
        assert "Please check message" in message

    def test_get_display_field_name(self) -> None:
        """Test conversion of field names to display names."""
        handler = PydanticErrorHandler()

        # Test known mappings
        assert handler._get_display_field_name("message") == "message"
        assert handler._get_display_field_name("alias_name") == "alias name"
        assert handler._get_display_field_name("target_player") == "target player"

        # Test snake_case conversion
        assert handler._get_display_field_name("help_topic") == "help topic"
        assert handler._get_display_field_name("filter_name") == "filter name"

        # Test empty field
        assert handler._get_display_field_name("") == "input"

    def test_create_error_details(self) -> None:
        """Test creation of error details for debugging."""
        with pytest.raises(ValidationError) as exc_info:
            SayCommand()  # type: ignore[call-arg]

        validation_error = exc_info.value
        handler = PydanticErrorHandler()

        error_info = handler._extract_error_info(validation_error, SayCommand)
        details = handler._create_error_details(error_info, validation_error)

        assert "validation_errors" in details
        assert "error_count" in details
        assert "model_class" in details
        assert "context" in details

        assert details["error_count"] > 0
        assert details["model_class"] == "SayCommand"
        assert len(details["validation_errors"]) > 0

    def test_create_fallback_error_response(self) -> None:
        """Test creation of fallback error response."""
        with pytest.raises(ValidationError) as exc_info:
            SayCommand()  # type: ignore[call-arg]

        validation_error = exc_info.value
        handler = PydanticErrorHandler()

        # Test HTTP fallback
        response = handler._create_fallback_error_response(validation_error, "http")
        assert "error" in response
        assert response["error"]["type"] == "validation_error"
        assert "Please check your input" in response["error"]["user_friendly"]
        assert response["error"]["details"]["fallback"] is True

        # Test WebSocket fallback
        response = handler._create_fallback_error_response(validation_error, "websocket")
        assert response["type"] == "error"
        assert response["error_type"] == "validation_error"
        assert response["details"]["fallback"] is True

        # Test SSE fallback
        response = handler._create_fallback_error_response(validation_error, "sse")
        assert response["type"] == "error"
        assert response["error_type"] == "validation_error"
        assert response["details"]["fallback"] is True

    def test_create_handler_with_context(self) -> None:
        """Test creation of handler with specific context."""
        handler = PydanticErrorHandler.create_handler(user_id="test_user", session_id="test_session")

        assert handler.context.user_id == "test_user"
        assert handler.context.session_id == "test_session"

    def test_convenience_functions(self) -> None:
        """Test convenience functions for error handling."""
        with pytest.raises(ValidationError) as exc_info:
            SayCommand()  # type: ignore[call-arg]

        validation_error = exc_info.value

        # Test handle_pydantic_error convenience function
        response = handle_pydantic_error(
            validation_error, model_class=SayCommand, response_type="http", user_id="test_user"
        )

        assert "error" in response
        assert response["error"]["type"] == "missing_required_field"

        # Test convert_pydantic_error convenience function
        mythos_error = convert_pydantic_error(validation_error, model_class=SayCommand, user_id="test_user")

        assert isinstance(mythos_error, MythosValidationError)
        assert mythos_error.context.user_id == "test_user"

    def test_field_name_mappings(self) -> None:
        """Test that field name mappings are properly defined."""
        handler = PydanticErrorHandler()

        # Test that common field names are mapped
        expected_mappings = {
            "message",
            "direction",
            "target_player",
            "alias_name",
            "help_topic",
            "filter_name",
            "reason",
            "action",
            "player_name",
            "command",
        }

        for field_name in expected_mappings:
            assert field_name in handler.FIELD_NAME_MAPPINGS
            assert handler.FIELD_NAME_MAPPINGS[field_name] is not None

    def test_error_type_mappings(self) -> None:
        """Test that error type mappings are properly defined."""
        handler = PydanticErrorHandler()

        # Test that common error types are mapped
        expected_mappings = {
            "missing",
            "value_error",
            "type_error",
            "extra_forbidden",
            "json_invalid",
            "string_too_short",
            "string_too_long",
        }

        for error_type in expected_mappings:
            assert error_type in handler.ERROR_TYPE_MAPPINGS
            assert isinstance(handler.ERROR_TYPE_MAPPINGS[error_type], ErrorType)
