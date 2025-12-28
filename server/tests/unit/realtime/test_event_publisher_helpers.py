"""
Unit tests for event publisher helper functions.

Tests the helper functions in event_publisher.py.
"""

from unittest.mock import MagicMock, patch

import pytest

from server.realtime.event_publisher import EventPublisher


@pytest.fixture
def mock_nats_service():
    """Create a mock NATS service."""
    service = MagicMock()
    service.is_connected = MagicMock(return_value=True)
    service.publish = MagicMock(return_value=True)
    return service


@pytest.fixture
def event_publisher(mock_nats_service):
    """Create an EventPublisher instance."""
    return EventPublisher(mock_nats_service)


def test_create_event_message(event_publisher):
    """Test _create_event_message() creates event message."""
    event_data = {"player_id": "player_001", "room_id": "room_001"}
    result = event_publisher._create_event_message("player_entered", event_data)
    assert "event_type" in result
    assert "timestamp" in result
    assert "sequence_number" in result
    assert result["event_type"] == "player_entered"
    assert result["data"] == event_data


def test_get_next_sequence_number(event_publisher):
    """Test get_next_sequence_number() increments sequence."""
    initial = event_publisher.sequence_number
    result = event_publisher.get_next_sequence_number()
    assert result == initial + 1
    assert event_publisher.sequence_number == initial + 1


def test_reset_sequence_number(event_publisher):
    """Test reset_sequence_number() resets to 0."""
    event_publisher.sequence_number = 5
    event_publisher.reset_sequence_number()
    assert event_publisher.sequence_number == 0


def test_get_async_persistence(event_publisher):
    """Test _get_async_persistence() gets persistence from container."""
    with patch("server.container.ApplicationContainer.get_instance") as mock_get_instance:
        mock_container = MagicMock()
        mock_container.async_persistence = MagicMock()
        mock_get_instance.return_value = mock_container
        result = event_publisher._get_async_persistence()
        assert result == mock_container.async_persistence
