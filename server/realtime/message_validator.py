"""
WebSocket message validation for MythosMUD.

This module provides comprehensive validation for incoming WebSocket messages,
including size limits, schema validation, CSRF protection, and JSON depth limits.
"""

import json
from typing import Any

from pydantic import BaseModel, ValidationError

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class MessageValidationError(Exception):
    """Raised when message validation fails."""

    def __init__(self, message: str, error_type: str = "validation_error"):
        self.message = message
        self.error_type = error_type
        super().__init__(self.message)


class WebSocketMessageValidator:
    """
    Validates WebSocket messages for security and correctness.

    Implements:
    - Message size limits (DoS protection)
    - JSON depth limits (prevent stack overflow)
    - Schema validation (type safety)
    - CSRF token validation (security)
    """

    # Configuration constants
    MAX_MESSAGE_SIZE = 10 * 1024  # 10KB maximum message size
    MAX_JSON_DEPTH = 10  # Maximum JSON nesting depth
    MAX_JSON_STRING_LENGTH = 10000  # Maximum string length in JSON

    def __init__(self, max_message_size: int | None = None, max_json_depth: int | None = None):
        """
        Initialize the message validator.

        Args:
            max_message_size: Maximum message size in bytes (default: 10KB)
            max_json_depth: Maximum JSON nesting depth (default: 10)
        """
        self.max_message_size = max_message_size or self.MAX_MESSAGE_SIZE
        self.max_json_depth = max_json_depth or self.MAX_JSON_DEPTH

    def validate_size(self, data: str) -> bool:
        """
        Validate message size.

        Args:
            data: Raw message data as string

        Returns:
            bool: True if size is within limits

        Raises:
            MessageValidationError: If message exceeds size limit
        """
        size = len(data.encode("utf-8"))
        if size > self.max_message_size:
            logger.warning(
                "Message size exceeds limit",
                size=size,
                max_size=self.max_message_size,
                size_exceeded_by=size - self.max_message_size,
            )
            raise MessageValidationError(
                f"Message size {size} bytes exceeds maximum {self.max_message_size} bytes",
                error_type="size_limit_exceeded",
            )
        return True

    def validate_json_structure(self, message: dict[str, Any]) -> bool:
        """
        Validate JSON structure including depth limits.

        Args:
            message: Parsed JSON message

        Returns:
            bool: True if structure is valid

        Raises:
            MessageValidationError: If JSON structure is invalid
        """
        depth = self._calculate_depth(message)
        if depth > self.max_json_depth:
            logger.warning(
                "JSON depth exceeds limit",
                depth=depth,
                max_depth=self.max_json_depth,
            )
            raise MessageValidationError(
                f"JSON depth {depth} exceeds maximum {self.max_json_depth}",
                error_type="depth_limit_exceeded",
            )

        # Check for excessively long strings
        self._validate_string_lengths(message)

        return True

    def _calculate_depth(self, obj: Any, current_depth: int = 0) -> int:
        """
        Calculate the maximum nesting depth of a JSON structure.

        Args:
            obj: Object to calculate depth for
            current_depth: Current depth level

        Returns:
            int: Maximum depth found
        """
        if current_depth > self.max_json_depth:
            return current_depth

        if isinstance(obj, dict):
            if not obj:
                return current_depth
            return max(self._calculate_depth(v, current_depth + 1) for v in obj.values())
        if isinstance(obj, list):
            if not obj:
                return current_depth
            return max(self._calculate_depth(item, current_depth + 1) for item in obj)
        return current_depth

    def _validate_string_lengths(self, obj: Any) -> None:
        """
        Validate that strings in the JSON structure don't exceed length limits.

        Args:
            obj: Object to validate

        Raises:
            MessageValidationError: If any string exceeds length limit
        """
        if isinstance(obj, dict):
            for key, value in obj.items():
                if isinstance(key, str) and len(key) > self.MAX_JSON_STRING_LENGTH:
                    raise MessageValidationError(
                        f"String key length {len(key)} exceeds maximum {self.MAX_JSON_STRING_LENGTH}",
                        error_type="string_length_exceeded",
                    )
                self._validate_string_lengths(value)
        elif isinstance(obj, list):
            for item in obj:
                self._validate_string_lengths(item)
        elif isinstance(obj, str):
            if len(obj) > self.MAX_JSON_STRING_LENGTH:
                raise MessageValidationError(
                    f"String length {len(obj)} exceeds maximum {self.MAX_JSON_STRING_LENGTH}",
                    error_type="string_length_exceeded",
                )

    def validate_schema(self, message: dict[str, Any], schema: type[BaseModel] | None = None) -> bool:
        """
        Validate message against Pydantic schema.

        Args:
            message: Parsed JSON message
            schema: Pydantic model class to validate against

        Returns:
            bool: True if message matches schema

        Raises:
            MessageValidationError: If message doesn't match schema
        """
        if schema is None:
            # Basic validation - ensure required fields exist
            if not isinstance(message, dict):
                raise MessageValidationError("Message must be a JSON object", error_type="invalid_type")

            # Check for required top-level fields
            if "type" not in message and "message" not in message:
                raise MessageValidationError(
                    "Message must contain 'type' or 'message' field",
                    error_type="missing_required_field",
                )
            return True

        try:
            # Validate against Pydantic schema
            schema.model_validate(message)
            return True
        except ValidationError as e:
            logger.warning("Schema validation failed", errors=str(e), message_keys=list(message.keys()))
            raise MessageValidationError(
                f"Schema validation failed: {e}",
                error_type="schema_validation_failed",
            ) from e

    def validate_csrf(self, message: dict[str, Any], player_id: str, expected_token: str | None = None) -> bool:
        """
        Validate CSRF token in message.

        Args:
            message: Parsed JSON message
            player_id: Player ID for token validation
            expected_token: Expected CSRF token (if available)

        Returns:
            bool: True if CSRF token is valid

        Raises:
            MessageValidationError: If CSRF token is missing or invalid
        """
        # Extract CSRF token from message
        csrf_token = message.get("csrfToken") or message.get("csrf_token")

        # If no token is present and no token is expected, allow (for backward compatibility)
        if csrf_token is None and expected_token is None:
            logger.debug("No CSRF token in message, allowing (backward compatibility)", player_id=player_id)
            return True

        # If token is expected but not present, reject
        if expected_token is not None and csrf_token is None:
            logger.warning("CSRF token missing from message", player_id=player_id)
            raise MessageValidationError("CSRF token is required", error_type="csrf_token_missing")

        # If token is present, validate it
        if csrf_token is not None:
            if expected_token is None:
                # Token present but no expected token - log warning but allow for now
                # TODO: Implement proper CSRF token validation  # pylint: disable=fixme  # Reason: Security enhancement placeholder for CSRF protection
                logger.debug(
                    "CSRF token present but no expected token available",
                    player_id=player_id,
                    has_token=True,
                )
                return True

            if csrf_token != expected_token:
                logger.warning(
                    "CSRF token mismatch",
                    player_id=player_id,
                    token_present=bool(csrf_token),
                    expected_present=bool(expected_token),
                )
                raise MessageValidationError("CSRF token mismatch", error_type="csrf_token_invalid")

        return True

    def parse_and_validate(
        self,
        data: str,
        player_id: str,
        schema: type[BaseModel] | None = None,
        csrf_token: str | None = None,
    ) -> dict[str, Any]:
        """
        Parse and validate a complete WebSocket message.

        This is the main entry point for message validation.

        Args:
            data: Raw message data as string
            player_id: Player ID for validation context
            schema: Optional Pydantic schema to validate against
            csrf_token: Optional CSRF token for validation

        Returns:
            dict: Parsed and validated message

        Raises:
            MessageValidationError: If validation fails at any stage
        """
        # Step 1: Validate size
        self.validate_size(data)

        # Step 2: Parse JSON
        try:
            message = json.loads(data)
        except json.JSONDecodeError as e:
            logger.warning("Invalid JSON in message", player_id=player_id, error=str(e))
            raise MessageValidationError(f"Invalid JSON: {e}", error_type="json_parse_error") from e

        # Step 3: Validate JSON structure (depth, string lengths)
        self.validate_json_structure(message)

        # Step 4: Validate schema against outer message if schema is provided
        # This must happen before extracting inner message, as the schema (e.g., WrappedMessage)
        # expects the outer message structure
        if schema is not None:
            self.validate_schema(message, schema)

        # Step 5: Handle nested message format (from useWebSocketConnection)
        if "message" in message and isinstance(message["message"], str):
            try:
                # Parse inner message
                inner_data = message["message"]
                # Validate inner message size
                self.validate_size(inner_data)
                inner_message = json.loads(inner_data)
                # Validate inner message structure
                self.validate_json_structure(inner_message)
                # Use inner message, preserve CSRF token from outer if present and not None
                # Human reader: Only copy csrfToken if it exists in outer message and is not None
                # AI reader: Copy csrfToken from outer to inner message only if it has a non-None value
                outer_csrf = message.get("csrfToken") or message.get("csrf_token")
                if outer_csrf is not None and "csrfToken" not in inner_message and "csrf_token" not in inner_message:
                    inner_message["csrfToken"] = outer_csrf
                message = inner_message
            except json.JSONDecodeError:
                # If inner message is not JSON, use outer message as-is
                pass

        # Step 6: Validate schema against inner message if no schema was provided earlier
        # (This allows schema validation of inner messages when no outer schema is specified)
        if schema is None:
            self.validate_schema(message, schema)

        # Step 6: Validate CSRF token
        self.validate_csrf(message, player_id, csrf_token)

        # Step 7: Remove CSRF token from result (it's only needed for validation)
        # Human reader: csrfToken is a validation field, not part of the actual message content
        # AI reader: Remove csrfToken and csrf_token from the returned message after validation
        message.pop("csrfToken", None)
        message.pop("csrf_token", None)

        logger.debug("Message validation successful", player_id=player_id, message_type=message.get("type"))

        return message


# Global validator instance
_message_validator = WebSocketMessageValidator()


def get_message_validator() -> WebSocketMessageValidator:
    """Get the global message validator instance."""
    return _message_validator
