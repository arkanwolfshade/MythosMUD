"""
Tests for the EventPublisher service module.

This module tests the EventPublisher class which handles publishing
player_entered, player_left, and game_tick events to NATS subjects.
"""

from datetime import datetime
from unittest.mock import AsyncMock, Mock

import pytest

from ..realtime.event_publisher import EventPublisher


class TestEventPublisher:
    """Test cases for EventPublisher class."""

    def setup_method(self):
        """Set up test fixtures."""
        # Create a mock NATS service
        self.mock_nats_service = Mock()
        self.mock_nats_service.publish = AsyncMock()
        self.mock_nats_service.is_connected = Mock(return_value=True)

        # Create the EventPublisher instance
        self.event_publisher = EventPublisher(self.mock_nats_service)

        # Test data
        self.test_player_id = "test_player_123"
        self.test_room_id = "arkham_1"
        self.test_timestamp = datetime.now().isoformat()

    def test_event_publisher_initialization(self):
        """Test EventPublisher initialization."""
        assert self.event_publisher.nats_service == self.mock_nats_service
        assert self.event_publisher.sequence_number == 0

    def test_event_publisher_initialization_with_sequence(self):
        """Test EventPublisher initialization with custom sequence number."""
        event_publisher = EventPublisher(self.mock_nats_service, initial_sequence=100)
        assert event_publisher.sequence_number == 100

    @pytest.mark.asyncio
    async def test_publish_player_entered_event_success(self):
        """Test successful publishing of player_entered event."""
        # Mock successful NATS publish
        self.mock_nats_service.publish.return_value = True

        # Call the method
        result = await self.event_publisher.publish_player_entered_event(
            player_id=self.test_player_id, room_id=self.test_room_id
        )

        # Verify result
        assert result is True

        # Verify NATS service was called correctly
        self.mock_nats_service.publish.assert_called_once()
        call_args = self.mock_nats_service.publish.call_args

        # Check subject
        assert call_args[0][0] == f"events.player_entered.{self.test_room_id}"

        # Check message data
        message_data = call_args[0][1]
        assert message_data["event_type"] == "player_entered"
        assert message_data["data"]["player_id"] == self.test_player_id
        assert message_data["data"]["room_id"] == self.test_room_id
        assert "timestamp" in message_data
        assert "sequence_number" in message_data
        assert message_data["sequence_number"] == 1

    @pytest.mark.asyncio
    async def test_publish_player_left_event_success(self):
        """Test successful publishing of player_left event."""
        # Mock successful NATS publish
        self.mock_nats_service.publish.return_value = True

        # Call the method
        result = await self.event_publisher.publish_player_left_event(
            player_id=self.test_player_id, room_id=self.test_room_id
        )

        # Verify result
        assert result is True

        # Verify NATS service was called correctly
        self.mock_nats_service.publish.assert_called_once()
        call_args = self.mock_nats_service.publish.call_args

        # Check subject
        assert call_args[0][0] == f"events.player_left.{self.test_room_id}"

        # Check message data
        message_data = call_args[0][1]
        assert message_data["event_type"] == "player_left"
        assert message_data["data"]["player_id"] == self.test_player_id
        assert message_data["data"]["room_id"] == self.test_room_id
        assert "timestamp" in message_data
        assert "sequence_number" in message_data
        assert message_data["sequence_number"] == 1

    @pytest.mark.asyncio
    async def test_publish_game_tick_event_success(self):
        """Test successful publishing of game_tick event."""
        # Mock successful NATS publish
        self.mock_nats_service.publish.return_value = True

        # Call the method
        result = await self.event_publisher.publish_game_tick_event()

        # Verify result
        assert result is True

        # Verify NATS service was called correctly
        self.mock_nats_service.publish.assert_called_once()
        call_args = self.mock_nats_service.publish.call_args

        # Check subject
        assert call_args[0][0] == "events.game_tick"

        # Check message data
        message_data = call_args[0][1]
        assert message_data["event_type"] == "game_tick"
        assert "timestamp" in message_data
        assert "sequence_number" in message_data
        assert message_data["sequence_number"] == 1

    @pytest.mark.asyncio
    async def test_publish_player_entered_event_nats_failure(self):
        """Test handling of NATS publish failure for player_entered event."""
        # Mock NATS publish failure
        self.mock_nats_service.publish.return_value = False

        # Call the method
        result = await self.event_publisher.publish_player_entered_event(
            player_id=self.test_player_id, room_id=self.test_room_id
        )

        # Verify result
        assert result is False

        # Verify NATS service was called
        self.mock_nats_service.publish.assert_called_once()

    @pytest.mark.asyncio
    async def test_publish_player_left_event_nats_failure(self):
        """Test handling of NATS publish failure for player_left event."""
        # Mock NATS publish failure
        self.mock_nats_service.publish.return_value = False

        # Call the method
        result = await self.event_publisher.publish_player_left_event(
            player_id=self.test_player_id, room_id=self.test_room_id
        )

        # Verify result
        assert result is False

        # Verify NATS service was called
        self.mock_nats_service.publish.assert_called_once()

    @pytest.mark.asyncio
    async def test_publish_game_tick_event_nats_failure(self):
        """Test handling of NATS publish failure for game_tick event."""
        # Mock NATS publish failure
        self.mock_nats_service.publish.return_value = False

        # Call the method
        result = await self.event_publisher.publish_game_tick_event()

        # Verify result
        assert result is False

        # Verify NATS service was called
        self.mock_nats_service.publish.assert_called_once()

    @pytest.mark.asyncio
    async def test_publish_player_entered_event_nats_exception(self):
        """Test handling of NATS publish exception for player_entered event."""
        # Mock NATS publish exception
        self.mock_nats_service.publish.side_effect = Exception("NATS connection error")

        # Call the method
        result = await self.event_publisher.publish_player_entered_event(
            player_id=self.test_player_id, room_id=self.test_room_id
        )

        # Verify result
        assert result is False

        # Verify NATS service was called
        self.mock_nats_service.publish.assert_called_once()

    @pytest.mark.asyncio
    async def test_publish_player_left_event_nats_exception(self):
        """Test handling of NATS publish exception for player_left event."""
        # Mock NATS publish exception
        self.mock_nats_service.publish.side_effect = Exception("NATS connection error")

        # Call the method
        result = await self.event_publisher.publish_player_left_event(
            player_id=self.test_player_id, room_id=self.test_room_id
        )

        # Verify result
        assert result is False

        # Verify NATS service was called
        self.mock_nats_service.publish.assert_called_once()

    @pytest.mark.asyncio
    async def test_publish_game_tick_event_nats_exception(self):
        """Test handling of NATS publish exception for game_tick event."""
        # Mock NATS publish exception
        self.mock_nats_service.publish.side_effect = Exception("NATS connection error")

        # Call the method
        result = await self.event_publisher.publish_game_tick_event()

        # Verify result
        assert result is False

        # Verify NATS service was called
        self.mock_nats_service.publish.assert_called_once()

    @pytest.mark.asyncio
    async def test_sequence_number_increment(self):
        """Test that sequence numbers increment correctly across multiple events."""
        # Mock successful NATS publish
        self.mock_nats_service.publish.return_value = True

        # Publish multiple events
        await self.event_publisher.publish_player_entered_event(
            player_id=self.test_player_id, room_id=self.test_room_id
        )
        await self.event_publisher.publish_player_left_event(player_id=self.test_player_id, room_id=self.test_room_id)
        await self.event_publisher.publish_game_tick_event()

        # Verify sequence numbers
        calls = self.mock_nats_service.publish.call_args_list
        assert calls[0][0][1]["sequence_number"] == 1
        assert calls[1][0][1]["sequence_number"] == 2
        assert calls[2][0][1]["sequence_number"] == 3

    @pytest.mark.asyncio
    async def test_message_format_consistency(self):
        """Test that all event messages have consistent format."""
        # Mock successful NATS publish
        self.mock_nats_service.publish.return_value = True

        # Publish all event types
        await self.event_publisher.publish_player_entered_event(
            player_id=self.test_player_id, room_id=self.test_room_id
        )
        await self.event_publisher.publish_player_left_event(player_id=self.test_player_id, room_id=self.test_room_id)
        await self.event_publisher.publish_game_tick_event()

        # Verify message format consistency
        calls = self.mock_nats_service.publish.call_args_list

        for call in calls:
            message_data = call[0][1]

            # Check required fields
            assert "event_type" in message_data
            assert "timestamp" in message_data
            assert "sequence_number" in message_data
            assert "data" in message_data
            assert "metadata" in message_data

            # Check data types
            assert isinstance(message_data["event_type"], str)
            assert isinstance(message_data["timestamp"], str)
            assert isinstance(message_data["sequence_number"], int)
            assert isinstance(message_data["data"], dict)
            assert isinstance(message_data["metadata"], dict)

    @pytest.mark.asyncio
    async def test_player_entered_event_data_structure(self):
        """Test that player_entered event has correct data structure."""
        # Mock successful NATS publish
        self.mock_nats_service.publish.return_value = True

        # Call the method
        await self.event_publisher.publish_player_entered_event(
            player_id=self.test_player_id, room_id=self.test_room_id
        )

        # Get the published message
        call_args = self.mock_nats_service.publish.call_args
        message_data = call_args[0][1]

        # Check data structure
        assert message_data["data"]["player_id"] == self.test_player_id
        assert message_data["data"]["room_id"] == self.test_room_id
        assert "player_name" in message_data["data"]
        assert "room_name" in message_data["data"]

    @pytest.mark.asyncio
    async def test_player_left_event_data_structure(self):
        """Test that player_left event has correct data structure."""
        # Mock successful NATS publish
        self.mock_nats_service.publish.return_value = True

        # Call the method
        await self.event_publisher.publish_player_left_event(player_id=self.test_player_id, room_id=self.test_room_id)

        # Get the published message
        call_args = self.mock_nats_service.publish.call_args
        message_data = call_args[0][1]

        # Check data structure
        assert message_data["data"]["player_id"] == self.test_player_id
        assert message_data["data"]["room_id"] == self.test_room_id
        assert "player_name" in message_data["data"]
        assert "room_name" in message_data["data"]

    @pytest.mark.asyncio
    async def test_game_tick_event_data_structure(self):
        """Test that game_tick event has correct data structure."""
        # Mock successful NATS publish
        self.mock_nats_service.publish.return_value = True

        # Call the method
        await self.event_publisher.publish_game_tick_event()

        # Get the published message
        call_args = self.mock_nats_service.publish.call_args
        message_data = call_args[0][1]

        # Check data structure
        assert "tick_number" in message_data["data"]
        assert "server_time" in message_data["data"]
        assert isinstance(message_data["data"]["tick_number"], int)
        assert isinstance(message_data["data"]["server_time"], str)

    @pytest.mark.asyncio
    async def test_nats_service_not_connected(self):
        """Test behavior when NATS service is not connected."""
        # Mock NATS service not connected
        self.mock_nats_service.is_connected.return_value = False

        # Call the method
        result = await self.event_publisher.publish_player_entered_event(
            player_id=self.test_player_id, room_id=self.test_room_id
        )

        # Verify result
        assert result is False

        # Verify NATS service publish was not called
        self.mock_nats_service.publish.assert_not_called()

    def test_get_next_sequence_number(self):
        """Test sequence number generation."""
        # Test initial sequence number
        assert self.event_publisher.get_next_sequence_number() == 1
        assert self.event_publisher.get_next_sequence_number() == 2
        assert self.event_publisher.get_next_sequence_number() == 3

    def test_reset_sequence_number(self):
        """Test sequence number reset."""
        # Increment sequence number
        self.event_publisher.get_next_sequence_number()
        self.event_publisher.get_next_sequence_number()

        # Reset sequence number
        self.event_publisher.reset_sequence_number()

        # Test that sequence starts from 1 again
        assert self.event_publisher.get_next_sequence_number() == 1

    @pytest.mark.asyncio
    async def test_publish_with_custom_timestamp(self):
        """Test publishing events with custom timestamp."""
        # Mock successful NATS publish
        self.mock_nats_service.publish.return_value = True

        custom_timestamp = "2024-01-01T12:00:00Z"

        # Call the method with custom timestamp
        result = await self.event_publisher.publish_player_entered_event(
            player_id=self.test_player_id, room_id=self.test_room_id, timestamp=custom_timestamp
        )

        # Verify result
        assert result is True

        # Verify custom timestamp was used
        call_args = self.mock_nats_service.publish.call_args
        message_data = call_args[0][1]
        assert message_data["timestamp"] == custom_timestamp

    @pytest.mark.asyncio
    async def test_publish_with_additional_metadata(self):
        """Test publishing events with additional metadata."""
        # Mock successful NATS publish
        self.mock_nats_service.publish.return_value = True

        additional_metadata = {"source": "test", "version": "1.0"}

        # Call the method with additional metadata
        result = await self.event_publisher.publish_player_entered_event(
            player_id=self.test_player_id, room_id=self.test_room_id, additional_metadata=additional_metadata
        )

        # Verify result
        assert result is True

        # Verify additional metadata was included
        call_args = self.mock_nats_service.publish.call_args
        message_data = call_args[0][1]
        assert message_data["metadata"]["source"] == "test"
        assert message_data["metadata"]["version"] == "1.0"
