"""
Tests for message validation functionality.

This module tests the MessageValidator class which enforces validation rules
for incoming WebSocket messages including size limits, JSON depth, and schema validation.
"""

import json

import pytest

from server.realtime.message_validator import (
    MessageValidationError,
    WebSocketMessageValidator,
    get_message_validator,
)


class TestMessageValidator:
    """Test cases for MessageValidator class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.validator = WebSocketMessageValidator(
            max_message_size=8192,  # 8KB
            max_json_depth=10,
        )
        self.player_id = "test_player_123"

    def test_valid_message(self):
        """Test validation of a valid message."""
        # Valid message structure: {message: "...", timestamp: ..., csrfToken: ...}
        outer_message = {
            "message": json.dumps({"type": "chat", "command": "say hello"}),
            "timestamp": 1234567890,
            "csrfToken": None,
        }
        data = json.dumps(outer_message)

        result = self.validator.parse_and_validate(data, self.player_id)

        assert result == {"type": "chat", "command": "say hello"}

    def test_message_too_large(self):
        """Test validation fails for message exceeding size limit."""
        # Create a message larger than 8KB
        large_content = "x" * 9000
        outer_message = {
            "message": json.dumps({"type": "chat", "command": large_content}),
            "timestamp": 1234567890,
        }
        data = json.dumps(outer_message)

        with pytest.raises(MessageValidationError) as exc_info:
            self.validator.parse_and_validate(data, self.player_id)

        assert exc_info.value.error_type == "size_limit_exceeded"

    def test_json_depth_exceeded(self):
        """Test validation fails for JSON exceeding depth limit."""
        # Create deeply nested JSON
        deep_json = {"level": 1}
        current = deep_json
        for i in range(2, 15):  # Exceeds max depth of 10
            current["nested"] = {"level": i}
            current = current["nested"]

        outer_message = {
            "message": json.dumps(deep_json),
            "timestamp": 1234567890,
        }
        data = json.dumps(outer_message)

        with pytest.raises(MessageValidationError) as exc_info:
            self.validator.parse_and_validate(data, self.player_id)

        assert exc_info.value.error_type == "depth_limit_exceeded"

    def test_invalid_outer_json(self):
        """Test validation fails for invalid outer JSON format."""
        invalid_json = "{invalid json}"

        with pytest.raises(MessageValidationError) as exc_info:
            self.validator.parse_and_validate(invalid_json, self.player_id)

        assert exc_info.value.error_type == "json_parse_error"

    def test_missing_inner_message(self):
        """Test validation fails when inner message is missing."""
        outer_message = {
            "timestamp": 1234567890,
            # Missing "message" field
        }
        data = json.dumps(outer_message)

        with pytest.raises(MessageValidationError):
            self.validator.parse_and_validate(data, self.player_id)

    def test_plain_text_command(self):
        """Test validation handles plain text commands (non-JSON inner message)."""
        outer_message = {
            "message": "say hello",  # Plain text, not JSON
            "timestamp": 1234567890,
        }
        data = json.dumps(outer_message)

        result = self.validator.parse_and_validate(data, self.player_id)

        # Plain text message should be parsed as-is (not converted)
        # The actual result depends on implementation
        assert isinstance(result, dict)

    def test_csrf_validation_disabled(self):
        """Test CSRF validation when disabled (default)."""
        outer_message = {
            "message": json.dumps({"type": "chat", "command": "say hello"}),
            "timestamp": 1234567890,
            "csrfToken": None,  # No CSRF token
        }
        data = json.dumps(outer_message)

        # Should pass when CSRF is disabled
        result = self.validator.parse_and_validate(data, self.player_id, csrf_token=None)
        assert result == {"type": "chat", "command": "say hello"}

    def test_csrf_validation_enabled_missing_token(self):
        """Test CSRF validation fails when enabled but token missing."""
        validator = WebSocketMessageValidator()
        outer_message = {
            "message": json.dumps({"type": "chat", "command": "say hello"}),
            "timestamp": 1234567890,
            # Missing csrfToken
        }
        data = json.dumps(outer_message)

        with pytest.raises(MessageValidationError) as exc_info:
            validator.parse_and_validate(data, self.player_id, csrf_token="expected_token")

        assert exc_info.value.error_type == "csrf_token_missing"

    def test_csrf_validation_enabled_invalid_token(self):
        """Test CSRF validation fails when token doesn't match."""
        validator = WebSocketMessageValidator()
        outer_message = {
            "message": json.dumps({"type": "chat", "command": "say hello"}),
            "timestamp": 1234567890,
            "csrfToken": "wrong_token",
        }
        data = json.dumps(outer_message)

        with pytest.raises(MessageValidationError) as exc_info:
            validator.parse_and_validate(data, self.player_id, csrf_token="expected_token")

        assert exc_info.value.error_type == "csrf_token_invalid"

    def test_csrf_validation_enabled_valid_token(self):
        """Test CSRF validation passes with valid token."""
        validator = WebSocketMessageValidator()
        expected_token = "valid_token_123"
        outer_message = {
            "message": json.dumps({"type": "chat", "command": "say hello"}),
            "timestamp": 1234567890,
            "csrfToken": expected_token,
        }
        data = json.dumps(outer_message)

        result = validator.parse_and_validate(data, self.player_id, csrf_token=expected_token)
        assert result == {"type": "chat", "command": "say hello"}

    def test_schema_validation(self):
        """Test Pydantic schema validation."""
        from server.schemas.websocket_messages import ClientWebSocketMessage

        # Valid schema
        outer_message = {
            "message": json.dumps({"type": "chat", "command": "say hello"}),
            "timestamp": 1234567890,
        }
        data = json.dumps(outer_message)

        result = self.validator.parse_and_validate(data, self.player_id, schema=ClientWebSocketMessage)
        assert result == {"type": "chat", "command": "say hello"}

    def test_get_message_validator_singleton(self):
        """Test get_message_validator returns singleton instance."""
        validator1 = get_message_validator()
        validator2 = get_message_validator()

        assert validator1 is validator2

    def test_custom_size_limit(self):
        """Test validator with custom size limit."""
        validator = WebSocketMessageValidator(max_message_size=1024)  # 1KB limit

        # Message just under limit should pass
        small_content = "x" * 500
        outer_message = {
            "message": json.dumps({"type": "chat", "command": small_content}),
            "timestamp": 1234567890,
        }
        data = json.dumps(outer_message)

        result = validator.parse_and_validate(data, self.player_id)
        assert result == {"type": "chat", "command": small_content}

        # Message over limit should fail
        large_content = "x" * 2000
        outer_message = {
            "message": json.dumps({"type": "chat", "command": large_content}),
            "timestamp": 1234567890,
        }
        data = json.dumps(outer_message)

        with pytest.raises(MessageValidationError) as exc_info:
            validator.parse_and_validate(data, self.player_id)

        assert exc_info.value.error_type == "size_limit_exceeded"
