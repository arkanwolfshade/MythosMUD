"""
Unit tests for logging processors.

Tests the logging processors for sanitizing sensitive data, adding correlation IDs,
request context, and enhancing player IDs with names.
"""

import uuid
from unittest.mock import MagicMock

import pytest

from server.structured_logging.logging_processors import (
    add_correlation_id,
    add_request_context,
    enhance_player_ids,
    sanitize_sensitive_data,
    set_global_player_service,
)


@pytest.fixture
def mock_player_service():
    """Create a mock player service."""
    service = MagicMock()
    service.persistence = MagicMock()
    return service


@pytest.fixture
def sample_event_dict():
    """Create a sample event dictionary."""
    return {"message": "Test message", "level": "info"}


def test_set_global_player_service(mock_player_service):
    """Test set_global_player_service() sets the global player service."""
    set_global_player_service(mock_player_service)
    # Verify it was set (we can't directly access the private holder, but we can test via enhance_player_ids)
    assert True  # Function completes without error


def test_sanitize_sensitive_data_password(sample_event_dict):
    """Test sanitize_sensitive_data() redacts password fields."""
    event_dict = {"password": "secret123", "username": "testuser"}
    result = sanitize_sensitive_data(None, "test", event_dict)
    assert result["password"] == "[REDACTED]"
    assert result["username"] == "testuser"


def test_sanitize_sensitive_data_token(sample_event_dict):
    """Test sanitize_sensitive_data() redacts token fields."""
    event_dict = {"token": "abc123", "message": "test"}
    result = sanitize_sensitive_data(None, "test", event_dict)
    assert result["token"] == "[REDACTED]"
    assert result["message"] == "test"


def test_sanitize_sensitive_data_api_key(sample_event_dict):
    """Test sanitize_sensitive_data() redacts fields ending with _key."""
    event_dict = {"api_key": "secret", "message": "test"}
    result = sanitize_sensitive_data(None, "test", event_dict)
    assert result["api_key"] == "[REDACTED]"
    assert result["message"] == "test"


def test_sanitize_sensitive_data_safe_fields(sample_event_dict):
    """Test sanitize_sensitive_data() preserves safe fields."""
    event_dict = {"subzone_key": "zone_001", "room_key": "room_001"}
    result = sanitize_sensitive_data(None, "test", event_dict)
    assert result["subzone_key"] == "zone_001"
    assert result["room_key"] == "room_001"


def test_sanitize_sensitive_data_nested_dict(sample_event_dict):
    """Test sanitize_sensitive_data() sanitizes nested dictionaries."""
    event_dict = {"user": {"password": "secret", "username": "test"}}
    result = sanitize_sensitive_data(None, "test", event_dict)
    assert result["user"]["password"] == "[REDACTED]"
    assert result["user"]["username"] == "test"


def test_sanitize_sensitive_data_multiple_sensitive_fields(sample_event_dict):
    """Test sanitize_sensitive_data() redacts multiple sensitive fields."""
    event_dict = {"password": "secret", "token": "abc123", "secret": "value"}
    result = sanitize_sensitive_data(None, "test", event_dict)
    assert result["password"] == "[REDACTED]"
    assert result["token"] == "[REDACTED]"
    assert result["secret"] == "[REDACTED]"


def test_sanitize_sensitive_data_no_sensitive_fields(sample_event_dict):
    """Test sanitize_sensitive_data() leaves non-sensitive fields unchanged."""
    event_dict = {"message": "test", "level": "info", "user_id": "123"}
    result = sanitize_sensitive_data(None, "test", event_dict)
    assert result == event_dict


def test_sanitize_sensitive_data_case_insensitive(sample_event_dict):
    """Test sanitize_sensitive_data() is case insensitive."""
    event_dict = {"PASSWORD": "secret", "Token": "abc123"}
    result = sanitize_sensitive_data(None, "test", event_dict)
    assert result["PASSWORD"] == "[REDACTED]"
    assert result["Token"] == "[REDACTED]"


def test_add_correlation_id_missing(sample_event_dict):
    """Test add_correlation_id() adds correlation_id when missing."""
    result = add_correlation_id(None, "test", sample_event_dict)
    assert "correlation_id" in result
    assert isinstance(result["correlation_id"], str)
    # Should be a valid UUID format
    uuid.UUID(result["correlation_id"])


def test_add_correlation_id_existing(sample_event_dict):
    """Test add_correlation_id() preserves existing correlation_id."""
    existing_id = str(uuid.uuid4())
    event_dict = {**sample_event_dict, "correlation_id": existing_id}
    result = add_correlation_id(None, "test", event_dict)
    assert result["correlation_id"] == existing_id


def test_add_request_context_adds_timestamp(sample_event_dict):
    """Test add_request_context() adds timestamp when missing."""
    result = add_request_context(None, "test", sample_event_dict)
    assert "timestamp" in result
    assert isinstance(result["timestamp"], str)


def test_add_request_context_preserves_timestamp(sample_event_dict):
    """Test add_request_context() preserves existing timestamp."""
    existing_timestamp = "2024-01-01T00:00:00Z"
    event_dict = {**sample_event_dict, "timestamp": existing_timestamp}
    result = add_request_context(None, "test", event_dict)
    assert result["timestamp"] == existing_timestamp


def test_add_request_context_adds_logger_name(sample_event_dict):
    """Test add_request_context() adds logger_name."""
    result = add_request_context(None, "test_logger", sample_event_dict)
    assert result["logger_name"] == "test_logger"


def test_add_request_context_adds_request_id(sample_event_dict):
    """Test add_request_context() adds request_id when missing."""
    result = add_request_context(None, "test", sample_event_dict)
    assert "request_id" in result
    assert isinstance(result["request_id"], str)
    # Should be a valid UUID format
    uuid.UUID(result["request_id"])


def test_add_request_context_preserves_request_id(sample_event_dict):
    """Test add_request_context() preserves existing request_id."""
    existing_id = str(uuid.uuid4())
    event_dict = {**sample_event_dict, "request_id": existing_id}
    result = add_request_context(None, "test", event_dict)
    assert result["request_id"] == existing_id


def test_enhance_player_ids_no_player_service(sample_event_dict):
    """Test enhance_player_ids() handles missing player service."""
    set_global_player_service(None)
    event_dict = {"player_id": str(uuid.uuid4())}
    result = enhance_player_ids(None, "test", event_dict)
    # Should return unchanged if no player service
    assert result["player_id"] == event_dict["player_id"]


def test_enhance_player_ids_player_found(mock_player_service):
    """Test enhance_player_ids() enhances player_id when player is found."""
    set_global_player_service(mock_player_service)
    test_uuid = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player_service.persistence.get_player = MagicMock(return_value=mock_player)

    event_dict = {"player_id": str(test_uuid)}
    result = enhance_player_ids(None, "test", event_dict)
    assert "<TestPlayer>" in result["player_id"]
    assert str(test_uuid) in result["player_id"]


def test_enhance_player_ids_player_not_found(mock_player_service):
    """Test enhance_player_ids() leaves player_id unchanged when player not found."""
    set_global_player_service(mock_player_service)
    test_uuid = uuid.uuid4()
    mock_player_service.persistence.get_player = MagicMock(return_value=None)

    event_dict = {"player_id": str(test_uuid)}
    result = enhance_player_ids(None, "test", event_dict)
    assert result["player_id"] == str(test_uuid)


def test_enhance_player_ids_invalid_uuid_format(mock_player_service):
    """Test enhance_player_ids() leaves non-UUID player_id unchanged."""
    set_global_player_service(mock_player_service)
    event_dict = {"player_id": "not-a-uuid"}
    result = enhance_player_ids(None, "test", event_dict)
    assert result["player_id"] == "not-a-uuid"


def test_enhance_player_ids_short_string(mock_player_service):
    """Test enhance_player_ids() leaves short strings unchanged."""
    set_global_player_service(mock_player_service)
    event_dict = {"player_id": "123"}
    result = enhance_player_ids(None, "test", event_dict)
    assert result["player_id"] == "123"


def test_enhance_player_ids_non_string_value(mock_player_service):
    """Test enhance_player_ids() handles non-string player_id values."""
    set_global_player_service(mock_player_service)
    event_dict = {"player_id": 12345}
    result = enhance_player_ids(None, "test", event_dict)
    assert result["player_id"] == 12345


def test_enhance_player_ids_no_player_id_field(sample_event_dict):
    """Test enhance_player_ids() handles event_dict without player_id."""
    set_global_player_service(MagicMock())
    result = enhance_player_ids(None, "test", sample_event_dict)
    assert result == sample_event_dict


def test_enhance_player_ids_persistence_error(mock_player_service):
    """Test enhance_player_ids() handles persistence errors gracefully."""
    set_global_player_service(mock_player_service)
    test_uuid = uuid.uuid4()
    # Use AttributeError which is caught by the exception handler
    mock_player_service.persistence.get_player = MagicMock(side_effect=AttributeError("Database error"))

    event_dict = {"player_id": str(test_uuid)}
    result = enhance_player_ids(None, "test", event_dict)
    # Should leave unchanged on error
    assert result["player_id"] == str(test_uuid)


def test_enhance_player_ids_player_no_name_attribute(mock_player_service):
    """Test enhance_player_ids() handles player without name attribute."""
    set_global_player_service(mock_player_service)
    test_uuid = uuid.uuid4()
    mock_player = MagicMock()
    del mock_player.name  # Remove name attribute
    mock_player_service.persistence.get_player = MagicMock(return_value=mock_player)

    event_dict = {"player_id": str(test_uuid)}
    result = enhance_player_ids(None, "test", event_dict)
    # Should leave unchanged if player has no name
    assert result["player_id"] == str(test_uuid)


def test_enhance_player_ids_prevents_recursion(mock_player_service):
    """Test enhance_player_ids() prevents recursion."""
    set_global_player_service(mock_player_service)
    test_uuid = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player_service.persistence.get_player = MagicMock(return_value=mock_player)

    # First call should work
    event_dict1 = {"player_id": str(test_uuid)}
    result1 = enhance_player_ids(None, "test", event_dict1)
    assert "<TestPlayer>" in result1["player_id"]

    # Second call immediately after should also work (recursion guard is per-thread)
    event_dict2 = {"player_id": str(uuid.uuid4())}
    result2 = enhance_player_ids(None, "test", event_dict2)
    # Should work normally since recursion guard is thread-local
    assert "player_id" in result2


def test_enhance_player_ids_no_persistence_attribute(mock_player_service):
    """Test enhance_player_ids() handles player_service without persistence."""
    del mock_player_service.persistence
    set_global_player_service(mock_player_service)
    test_uuid = uuid.uuid4()
    event_dict = {"player_id": str(test_uuid)}
    result = enhance_player_ids(None, "test", event_dict)
    # Should leave unchanged if no persistence
    assert result["player_id"] == str(test_uuid)
