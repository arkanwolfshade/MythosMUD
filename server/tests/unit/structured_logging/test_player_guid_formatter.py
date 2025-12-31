"""
Unit tests for PlayerGuidFormatter.

Tests the PlayerGuidFormatter class for converting player GUIDs to readable format.
"""

import logging
import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.structured_logging.player_guid_formatter import PlayerGuidFormatter


@pytest.fixture
def mock_player_service():
    """Create a mock player service."""
    service = MagicMock()
    service.get_player_by_id = AsyncMock()
    return service


@pytest.fixture
def formatter(mock_player_service):
    """Create a PlayerGuidFormatter instance."""
    return PlayerGuidFormatter(
        player_service=mock_player_service,
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def test_player_guid_formatter_init(mock_player_service):
    """Test PlayerGuidFormatter initialization."""
    formatter = PlayerGuidFormatter(mock_player_service)
    assert formatter.player_service == mock_player_service
    assert formatter.uuid_pattern is not None


def test_player_guid_formatter_init_with_format(mock_player_service):
    """Test PlayerGuidFormatter initialization with format string."""
    formatter = PlayerGuidFormatter(mock_player_service, fmt="%(message)s", datefmt="%Y-%m-%d")
    assert formatter.player_service == mock_player_service


def test_format_no_guids(formatter):
    """Test format() with message containing no GUIDs."""
    record = logging.LogRecord("test", logging.INFO, "", 0, "This is a test message", (), None)
    result = formatter.format(record)
    assert "This is a test message" in result
    assert result == formatter.formatMessage(record)


def test_format_with_guid_no_player_service():
    """Test format() with GUID when player service returns None."""
    mock_service = MagicMock()
    mock_service.get_player_by_id = AsyncMock(return_value=None)
    formatter = PlayerGuidFormatter(mock_service)
    test_uuid = str(uuid.uuid4())
    record = logging.LogRecord("test", logging.INFO, "", 0, f"Player {test_uuid} logged in", (), None)
    result = formatter.format(record)
    # Should still format the message, GUID may not be replaced if player not found
    assert "logged in" in result


def test_format_with_guid_player_found(formatter):
    """Test format() with GUID when player is found."""
    test_uuid = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_name = "TestPlayer"
    formatter.player_service.get_player_by_id = AsyncMock(return_value=mock_player)

    record = logging.LogRecord("test", logging.INFO, "", 0, f"Player {test_uuid} logged in", (), None)
    result = formatter.format(record)
    # The format method should handle the GUID replacement
    assert "logged in" in result


def test_format_multiple_guids(formatter):
    """Test format() with multiple GUIDs in message."""
    test_uuid1 = uuid.uuid4()
    test_uuid2 = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_name = "TestPlayer"
    formatter.player_service.get_player_by_id = AsyncMock(return_value=mock_player)

    record = logging.LogRecord(
        "test",
        logging.INFO,
        "",
        0,
        f"Player {test_uuid1} attacked {test_uuid2}",
        (),
        None,
    )
    result = formatter.format(record)
    assert "attacked" in result


def test_format_guid_at_start(formatter):
    """Test format() with GUID at start of message."""
    test_uuid = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_name = "TestPlayer"
    formatter.player_service.get_player_by_id = AsyncMock(return_value=mock_player)

    record = logging.LogRecord("test", logging.INFO, "", 0, f"{test_uuid} logged in", (), None)
    result = formatter.format(record)
    assert "logged in" in result


def test_format_guid_at_end(formatter):
    """Test format() with GUID at end of message."""
    test_uuid = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_name = "TestPlayer"
    formatter.player_service.get_player_by_id = AsyncMock(return_value=mock_player)

    record = logging.LogRecord("test", logging.INFO, "", 0, f"Player logged in: {test_uuid}", (), None)
    result = formatter.format(record)
    assert "logged in" in result


def test_format_guid_in_middle(formatter):
    """Test format() with GUID in middle of message."""
    test_uuid = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_name = "TestPlayer"
    formatter.player_service.get_player_by_id = AsyncMock(return_value=mock_player)

    record = logging.LogRecord("test", logging.INFO, "", 0, f"Player {test_uuid} is online", (), None)
    result = formatter.format(record)
    assert "is online" in result


def test_format_invalid_guid_format(formatter):
    """Test format() with invalid GUID format."""
    record = logging.LogRecord("test", logging.INFO, "", 0, "Player 12345 logged in", (), None)
    result = formatter.format(record)
    # Should not try to replace non-UUID strings
    assert "12345" in result


def test_format_guid_with_hyphens(formatter):
    """Test format() handles GUIDs with hyphens correctly."""
    test_uuid = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_name = "TestPlayer"
    formatter.player_service.get_player_by_id = AsyncMock(return_value=mock_player)

    # UUID should have hyphens
    uuid_str = str(test_uuid)
    assert "-" in uuid_str
    record = logging.LogRecord("test", logging.INFO, "", 0, f"Player {uuid_str} logged in", (), None)
    result = formatter.format(record)
    assert "logged in" in result


def test_format_player_service_error(formatter):
    """Test format() handles player service errors gracefully."""
    test_uuid = uuid.uuid4()
    formatter.player_service.get_player_by_id = AsyncMock(side_effect=Exception("Service error"))

    record = logging.LogRecord("test", logging.INFO, "", 0, f"Player {test_uuid} logged in", (), None)
    # Should not raise, should handle error gracefully
    result = formatter.format(record)
    assert "logged in" in result


def test_format_empty_message(formatter):
    """Test format() with empty message."""
    record = logging.LogRecord("test", logging.INFO, "", 0, "", (), None)
    result = formatter.format(record)
    assert isinstance(result, str)


def test_format_message_with_special_characters(formatter):
    """Test format() with message containing special characters."""
    record = logging.LogRecord("test", logging.INFO, "", 0, "Message with <tags> and & symbols", (), None)
    result = formatter.format(record)
    assert "<tags>" in result or "tags" in result


def test_uuid_pattern_matching(formatter):
    """Test UUID pattern correctly matches UUID format."""
    test_uuid = uuid.uuid4()
    uuid_str = str(test_uuid)
    match = formatter.uuid_pattern.search(uuid_str)
    assert match is not None
    assert match.group() == uuid_str


def test_uuid_pattern_not_matching_partial(formatter):
    """Test UUID pattern doesn't match partial UUIDs."""
    # Partial UUID (too short)
    partial = "12345678-1234-1234-1234-12345678901"
    match = formatter.uuid_pattern.search(partial)
    # Should not match incomplete UUIDs
    assert match is None or len(match.group()) != len(partial)


def test_uuid_pattern_case_insensitive(formatter):
    """Test UUID pattern is case insensitive."""
    # UUID with uppercase letters
    test_uuid = uuid.uuid4()
    uuid_upper = str(test_uuid).upper()
    match = formatter.uuid_pattern.search(uuid_upper)
    assert match is not None


def test_format_with_different_log_levels(formatter):
    """Test format() works with different log levels."""
    test_uuid = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_name = "TestPlayer"
    formatter.player_service.get_player_by_id = AsyncMock(return_value=mock_player)

    for level in [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]:
        record = logging.LogRecord("test", level, "", 0, f"Player {test_uuid} action", (), None)
        result = formatter.format(record)
        assert "action" in result
