"""
WebSocket message validation for MythosMUD.

This module provides comprehensive validation for incoming WebSocket messages,
including size limits, schema validation, CSRF protection, and JSON depth limits.
"""

import json
from typing import ClassVar, cast

from pydantic import BaseModel, ValidationError
from structlog.stdlib import BoundLogger

from ..structured_logging.enhanced_logging_config import get_logger

logger: BoundLogger = cast(BoundLogger, get_logger(__name__))


class MessageValidationError(Exception):
    """Raised when message validation fails."""

    message: str
    error_type: str

    def __init__(self, message: str, error_type: str = "validation_error") -> None:
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
    MAX_MESSAGE_SIZE: ClassVar[int] = 10 * 1024  # 10KB maximum message size
    MAX_JSON_DEPTH: ClassVar[int] = 10  # Maximum JSON nesting depth
    MAX_JSON_STRING_LENGTH: ClassVar[int] = 10000  # Maximum string length in JSON

    max_message_size: int
    max_json_depth: int

    def __init__(self, max_message_size: int | None = None, max_json_depth: int | None = None) -> None:
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

    def validate_json_structure(self, message: dict[str, object]) -> bool:
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

    def _calculate_depth(self, obj: object, current_depth: int = 0) -> int:
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
            mapping = cast(dict[str, object], obj)
            if not mapping:
                return current_depth
            return max(self._calculate_depth(v, current_depth + 1) for v in mapping.values())
        if isinstance(obj, list):
            seq = cast(list[object], obj)
            if not seq:
                return current_depth
            return max(self._calculate_depth(item, current_depth + 1) for item in seq)
        return current_depth

    def _validate_string_lengths(self, obj: object) -> None:
        """
        Validate that strings in the JSON structure don't exceed length limits.

        Args:
            obj: Object to validate

        Raises:
            MessageValidationError: If any string exceeds length limit
        """
        if isinstance(obj, dict):
            mapping = cast(dict[str, object], obj)
            for key, value in mapping.items():
                if len(key) > self.MAX_JSON_STRING_LENGTH:
                    raise MessageValidationError(
                        f"String key length {len(key)} exceeds maximum {self.MAX_JSON_STRING_LENGTH}",
                        error_type="string_length_exceeded",
                    )
                self._validate_string_lengths(value)
        elif isinstance(obj, list):
            seq = cast(list[object], obj)
            for item in seq:
                self._validate_string_lengths(item)
        elif isinstance(obj, str):
            if len(obj) > self.MAX_JSON_STRING_LENGTH:
                raise MessageValidationError(
                    f"String length {len(obj)} exceeds maximum {self.MAX_JSON_STRING_LENGTH}",
                    error_type="string_length_exceeded",
                )

    def validate_schema(self, message: dict[str, object], schema: type[BaseModel] | None = None) -> bool:
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
            # Basic validation - ensure required top-level fields exist
            if "type" not in message and "message" not in message:
                raise MessageValidationError(
                    "Message must contain 'type' or 'message' field",
                    error_type="missing_required_field",
                )
            return True

        try:
            # Validate against Pydantic schema
            _ = schema.model_validate(message)
            return True
        except ValidationError as e:
            logger.warning("Schema validation failed", errors=str(e), message_keys=list(message.keys()))
            raise MessageValidationError(
                f"Schema validation failed: {e}",
                error_type="schema_validation_failed",
            ) from e

    @staticmethod
    def _extract_csrf_token_string(message: dict[str, object]) -> str | None:
        """Return the first string CSRF token from known keys, or None if absent."""
        for key in ("csrfToken", "csrf_token"):
            raw = message.get(key)
            if raw is None:
                continue
            if isinstance(raw, str):
                return raw
            raise MessageValidationError(
                f"Field {key} must be a string when present",
                error_type="csrf_invalid_type",
            )
        return None

    def validate_csrf(self, message: dict[str, object], player_id: str, expected_token: str | None = None) -> bool:
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
        # Extract CSRF token from message (only string values count as tokens)
        csrf_token = self._extract_csrf_token_string(message)

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
                    token_present=True,
                    expected_present=bool(expected_token),
                )
                raise MessageValidationError("CSRF token mismatch", error_type="csrf_token_invalid")

        return True

    def _parse_outer_json_object(self, data: str, player_id: str) -> dict[str, object]:
        """Parse raw payload to a dict; validate size and outer JSON structure."""
        _ = self.validate_size(data)
        try:
            parsed = cast(object, json.loads(data))
        except json.JSONDecodeError as e:
            logger.warning("Invalid JSON in message", player_id=player_id, error=str(e))
            raise MessageValidationError(f"Invalid JSON: {e}", error_type="json_parse_error") from e
        if not isinstance(parsed, dict):
            raise MessageValidationError("Message must be a JSON object", error_type="invalid_type")
        message = cast(dict[str, object], parsed)
        _ = self.validate_json_structure(message)
        return message

    def _unwrap_string_inner_message_if_json(self, message: dict[str, object]) -> dict[str, object]:
        """
        If ``message["message"]`` is a JSON string, parse and validate inner object.

        On inner JSON decode failure, returns the outer ``message`` unchanged.
        """
        raw_inner = message.get("message")
        if not isinstance(raw_inner, str):
            return message
        try:
            _ = self.validate_size(raw_inner)
            inner_parsed = cast(object, json.loads(raw_inner))
            if not isinstance(inner_parsed, dict):
                raise MessageValidationError(
                    "Inner message must be a JSON object",
                    error_type="invalid_type",
                )
            inner_message = cast(dict[str, object], inner_parsed)
            _ = self.validate_json_structure(inner_message)
            outer_csrf = self._extract_csrf_token_string(message)
            if outer_csrf is not None and "csrfToken" not in inner_message and "csrf_token" not in inner_message:
                inner_message["csrfToken"] = outer_csrf
            return inner_message
        except json.JSONDecodeError:
            return message

    def parse_and_validate(
        self,
        data: str,
        player_id: str,
        schema: type[BaseModel] | None = None,
        csrf_token: str | None = None,
    ) -> dict[str, object]:
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
        message = self._parse_outer_json_object(data, player_id)
        if schema is not None:
            _ = self.validate_schema(message, schema)
        message = self._unwrap_string_inner_message_if_json(message)
        if schema is None:
            _ = self.validate_schema(message, schema)
        _ = self.validate_csrf(message, player_id, csrf_token)
        # csrfToken is validation-only; strip before returning payload to handlers
        _ = message.pop("csrfToken", None)
        _ = message.pop("csrf_token", None)
        msg_type = message.get("type")
        logger.debug(
            "Message validation successful",
            player_id=player_id,
            message_type=msg_type if isinstance(msg_type, str) else None,
        )
        return message


# Global validator instance
_message_validator = WebSocketMessageValidator()


def get_message_validator() -> WebSocketMessageValidator:
    """Get the global message validator instance."""
    return _message_validator
