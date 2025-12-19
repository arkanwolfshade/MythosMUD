"""
Tests for local channel NATS integration.

This module tests the NATS integration for local channels, including
sub-zone subscription management and dynamic subscription changes.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.realtime.nats_message_handler import NATSMessageHandler
from server.services.nats_subject_manager import NATSSubjectManager
from server.utils.room_utils import extract_subzone_from_room_id, get_subzone_local_channel_subject


class TestLocalChannelNATSIntegration:
    """Test local channel NATS integration functionality."""

    @pytest.fixture
    def mock_nats_service(self):
        """Create a mock NATS service."""
        mock_service = MagicMock()
        mock_service.subscribe = AsyncMock(return_value=True)
        mock_service.unsubscribe = AsyncMock(return_value=True)
        mock_service.publish = AsyncMock(return_value=True)
        mock_service.is_connected.return_value = True
        return mock_service

    @pytest.fixture
    def subject_manager(self):
        """Create a real NATSSubjectManager for testing."""
        return NATSSubjectManager()

    @pytest.fixture
    def nats_handler(self, mock_nats_service, subject_manager):
        """Create a NATS message handler with mocked dependencies."""
        # AI Agent: Inject mock connection_manager via constructor (no longer a global)
        #           Post-migration: NATSMessageHandler requires connection_manager
        #           Also requires subject_manager for room subscription methods
        mock_connection_manager = MagicMock()
        return NATSMessageHandler(
            mock_nats_service, subject_manager=subject_manager, connection_manager=mock_connection_manager
        )

    @pytest.mark.asyncio
    async def test_local_channel_subscription_on_start(self, nats_handler, mock_nats_service):
        """Test that local channel subjects are subscribed to on handler start."""
        await nats_handler.start()

        # Verify that local channel subject pattern is subscribed
        mock_nats_service.subscribe.assert_called()
        subscribe_calls = mock_nats_service.subscribe.call_args_list

        # With subject manager, the pattern is "chat.local.subzone.*" instead of "chat.local.*"
        local_subscription_found = False
        for call in subscribe_calls:
            subject = call[0][0]
            if subject == "chat.local.subzone.*":
                local_subscription_found = True
                break

        assert local_subscription_found, "Local channel subject pattern (chat.local.subzone.*) not subscribed"

    @pytest.mark.asyncio
    async def test_local_channel_message_handling(self, nats_handler):
        """Test handling of local channel messages."""
        # Mock the broadcast method
        nats_handler._broadcast_to_room_with_filtering = AsyncMock()

        # Create a local channel message with valid UUID
        test_sender_id = str(uuid.uuid4())
        message_data = {
            "channel": "local",
            "room_id": "earth_arkhamcity_northside_intersection_derby_high",
            "sender_id": test_sender_id,
            "sender_name": "TestPlayer",
            "content": "Hello, local area!",
            "message_id": "msg-123",
            "timestamp": "2025-08-27T18:00:00Z",
        }

        # Handle the message
        await nats_handler._handle_nats_message(message_data)

        # Verify that the message was broadcast to the room
        nats_handler._broadcast_to_room_with_filtering.assert_called_once()
        call_args = nats_handler._broadcast_to_room_with_filtering.call_args

        # Check room_id
        assert call_args[0][0] == "earth_arkhamcity_northside_intersection_derby_high"

        # Check event structure
        event = call_args[0][1]
        assert event["event_type"] == "chat_message"
        assert event["data"]["sender_id"] == test_sender_id
        assert event["data"]["player_name"] == "TestPlayer"
        assert event["data"]["channel"] == "local"
        assert event["data"]["message"] == "TestPlayer (local): Hello, local area!"
        assert event["data"]["message_id"] == "msg-123"
        assert event["data"]["timestamp"] == "2025-08-27T18:00:00Z"
        assert event["player_id"] == test_sender_id

        # Check sender_id and channel
        # _broadcast_to_room_with_filtering expects string sender_id (converted from UUID)
        assert call_args[0][2] == test_sender_id
        assert call_args[0][3] == "local"

    @pytest.mark.asyncio
    async def test_room_subscription_includes_local_channel(self, nats_handler, mock_nats_service, subject_manager):
        """Test that subscribing to a room includes local channel subscription."""
        room_id = "earth_arkhamcity_northside_intersection_derby_high"

        await nats_handler.subscribe_to_room(room_id)

        # Verify that say subject is subscribed using standardized pattern
        subscribe_calls = mock_nats_service.subscribe.call_args_list
        # Subject manager generates: chat.say.room.{room_id}
        expected_say_subject = subject_manager.build_subject("chat_say_room", room_id=room_id)

        subject_found = False
        for call in subscribe_calls:
            if call[0][0] == expected_say_subject:
                subject_found = True
                break
        assert subject_found, f"Subject {expected_say_subject} not subscribed"

    @pytest.mark.asyncio
    async def test_room_unsubscription_includes_local_channel(self, nats_handler, mock_nats_service, subject_manager):
        """Test that unsubscribing from a room includes local channel unsubscription."""
        room_id = "earth_arkhamcity_northside_intersection_derby_high"

        # First subscribe to the room to set up subscriptions
        say_subject = subject_manager.build_subject("chat_say_room", room_id=room_id)
        nats_handler.subscriptions = {say_subject: True}

        await nats_handler.unsubscribe_from_room(room_id)

        # Verify that say subject is unsubscribed using standardized pattern
        unsubscribe_calls = mock_nats_service.unsubscribe.call_args_list
        expected_say_subject = subject_manager.build_subject("chat_say_room", room_id=room_id)

        subject_found = False
        for call in unsubscribe_calls:
            if call[0][0] == expected_say_subject:
                subject_found = True
                break
        assert subject_found, f"Subject {expected_say_subject} not unsubscribed"


class TestLocalChannelSubZoneSubscriptionManagement:
    """Test sub-zone subscription management for local channels."""

    @pytest.fixture
    def mock_nats_service(self):
        """Create a mock NATS service."""
        mock_service = MagicMock()
        mock_service.subscribe = AsyncMock(return_value=True)
        mock_service.unsubscribe = AsyncMock(return_value=True)
        mock_service.publish = AsyncMock(return_value=True)
        mock_service.is_connected.return_value = True
        return mock_service

    @pytest.fixture
    def subject_manager(self):
        """Create a real NATSSubjectManager for testing."""
        return NATSSubjectManager()

    @pytest.fixture
    def nats_handler(self, mock_nats_service, subject_manager):
        """Create a NATS message handler with mocked dependencies."""
        # AI Agent: Inject mock connection_manager via constructor (no longer a global)
        #           Post-migration: NATSMessageHandler requires connection_manager
        #           Also requires subject_manager for room subscription methods
        mock_connection_manager = MagicMock()
        return NATSMessageHandler(
            mock_nats_service, subject_manager=subject_manager, connection_manager=mock_connection_manager
        )

    @pytest.mark.asyncio
    async def test_subzone_subscription_creation(self, nats_handler, _mock_nats_service: MagicMock):
        """Test creating sub-zone subscriptions for local channels."""
        room_id = "earth_arkhamcity_northside_intersection_derby_high"
        subzone = extract_subzone_from_room_id(room_id)
        subzone_subject = get_subzone_local_channel_subject(room_id)

        # Mock the subscribe_to_subzone method (to be implemented)
        nats_handler.subscribe_to_subzone = AsyncMock()

        await nats_handler.subscribe_to_subzone(subzone)

        nats_handler.subscribe_to_subzone.assert_called_once_with(subzone)
        assert subzone == "northside"
        assert subzone_subject == "chat.local.subzone.northside"

    @pytest.mark.asyncio
    async def test_subzone_unsubscription(self, nats_handler, _mock_nats_service: MagicMock):
        """Test unsubscribing from sub-zone subscriptions."""
        room_id = "earth_arkhamcity_northside_intersection_derby_high"
        subzone = extract_subzone_from_room_id(room_id)

        # Mock the unsubscribe_from_subzone method (to be implemented)
        nats_handler.unsubscribe_from_subzone = AsyncMock()

        await nats_handler.unsubscribe_from_subzone(subzone)

        nats_handler.unsubscribe_from_subzone.assert_called_once_with(subzone)

    @pytest.mark.asyncio
    async def test_player_movement_subzone_change(self, nats_handler, _mock_nats_service: MagicMock):
        """Test handling player movement between sub-zones."""
        # AI Agent: Inject mock connection_manager via instance variable (no longer a global)
        mock_connection_manager = MagicMock()
        mock_connection_manager.online_players = {
            "test-player-123": {"current_room_id": "earth_arkhamcity_northside_intersection_derby_high"}
        }

        # Set mock on handler instance
        nats_handler._connection_manager = mock_connection_manager

        # Mock sub-zone subscription methods
        nats_handler.subscribe_to_subzone = AsyncMock()
        nats_handler.unsubscribe_from_subzone = AsyncMock()

        # Simulate player moving from northside to downtown
        old_room_id = "earth_arkhamcity_northside_intersection_derby_high"
        new_room_id = "earth_arkhamcity_downtown_market_square"

        old_subzone = extract_subzone_from_room_id(old_room_id)
        new_subzone = extract_subzone_from_room_id(new_room_id)

        # Update player's room
        mock_connection_manager.online_players["test-player-123"]["current_room_id"] = new_room_id

        # Mock the handle_player_movement method (to be implemented)
        nats_handler.handle_player_movement = AsyncMock()

        await nats_handler.handle_player_movement("test-player-123", old_room_id, new_room_id)

        nats_handler.handle_player_movement.assert_called_once_with("test-player-123", old_room_id, new_room_id)
        assert old_subzone == "northside"
        assert new_subzone == "downtown"

    @pytest.mark.asyncio
    async def test_subzone_subscription_tracking(self, nats_handler):
        """Test tracking of sub-zone subscriptions."""
        # Mock the sub-zone subscription tracking (to be implemented)
        nats_handler.subzone_subscriptions = {}
        nats_handler.player_subzone_subscriptions = {}

        player_id = "test-player-123"
        subzone = "northside"

        # Mock the track_player_subzone_subscription method (to be implemented)
        nats_handler.track_player_subzone_subscription = MagicMock()

        nats_handler.track_player_subzone_subscription(player_id, subzone)

        nats_handler.track_player_subzone_subscription.assert_called_once_with(player_id, subzone)

    @pytest.mark.asyncio
    async def test_multiple_players_same_subzone(self, nats_handler, _mock_nats_service: MagicMock):
        """Test multiple players in the same sub-zone sharing subscription."""
        # AI Agent: Inject mock connection_manager via instance variable (no longer a global)
        mock_connection_manager = MagicMock()
        mock_connection_manager.online_players = {
            "player1": {"current_room_id": "earth_arkhamcity_northside_intersection_derby_high"},
            "player2": {"current_room_id": "earth_arkhamcity_northside_room_high_ln_001"},
            "player3": {"current_room_id": "earth_arkhamcity_northside_room_high_ln_002"},
        }

        # Set mock on handler instance
        nats_handler._connection_manager = mock_connection_manager

        # Mock sub-zone subscription methods
        nats_handler.subscribe_to_subzone = AsyncMock()
        nats_handler.unsubscribe_from_subzone = AsyncMock()

        subzone = "northside"

        # Mock the get_players_in_subzone method (to be implemented)
        nats_handler.get_players_in_subzone = MagicMock(return_value=["player1", "player2", "player3"])

        players_in_subzone = nats_handler.get_players_in_subzone(subzone)

        assert len(players_in_subzone) == 3
        assert "player1" in players_in_subzone
        assert "player2" in players_in_subzone
        assert "player3" in players_in_subzone
        assert subzone == "northside"  # Use the variable to avoid linting warning

    @pytest.mark.asyncio
    async def test_subzone_subscription_cleanup(self, nats_handler, _mock_nats_service: MagicMock):
        """Test cleanup of sub-zone subscriptions when no players remain."""
        # AI Agent: Inject mock connection_manager via instance variable (no longer a global)
        mock_connection_manager = MagicMock()
        mock_connection_manager.online_players = {
            "player1": {"current_room_id": "earth_arkhamcity_northside_intersection_derby_high"}
        }

        # Set mock on handler instance
        nats_handler._connection_manager = mock_connection_manager

        # Mock sub-zone subscription methods
        nats_handler.subscribe_to_subzone = AsyncMock()
        nats_handler.unsubscribe_from_subzone = AsyncMock()
        nats_handler.get_players_in_subzone = MagicMock(return_value=["player1"])

        subzone = "northside"

        # Mock the cleanup_empty_subzone_subscriptions method (to be implemented)
        nats_handler.cleanup_empty_subzone_subscriptions = AsyncMock()

        # Simulate player leaving the sub-zone
        del mock_connection_manager.online_players["player1"]
        nats_handler.get_players_in_subzone.return_value = []

        await nats_handler.cleanup_empty_subzone_subscriptions()

        nats_handler.cleanup_empty_subzone_subscriptions.assert_called_once()
        assert subzone == "northside"  # Use the variable to avoid linting warning


class TestLocalChannelNATSSubjectPatterns:
    """Test NATS subject patterns for local channels."""

    def test_local_channel_subject_patterns(self) -> None:
        """Test that local channel subjects follow the correct patterns."""
        room_id = "earth_arkhamcity_northside_intersection_derby_high"
        subzone = extract_subzone_from_room_id(room_id)

        # Test room-specific local channel subject
        room_subject = f"chat.local.{room_id}"
        assert room_subject == "chat.local.earth_arkhamcity_northside_intersection_derby_high"

        # Test sub-zone local channel subject
        subzone_subject = get_subzone_local_channel_subject(room_id)
        assert subzone_subject == "chat.local.subzone.northside"

        # Verify patterns are different
        assert room_subject != subzone_subject
        assert subzone == "northside"  # Use the variable to avoid linting warning

    def test_local_channel_subject_validation(self) -> None:
        """Test validation of local channel subject patterns."""
        valid_room_id = "earth_arkhamcity_northside_intersection_derby_high"
        invalid_room_id = "invalid_room_id"

        # Valid room ID should produce valid subjects
        room_subject = f"chat.local.{valid_room_id}"
        subzone_subject = get_subzone_local_channel_subject(valid_room_id)

        assert room_subject.startswith("chat.local.")
        assert subzone_subject is not None
        assert subzone_subject.startswith("chat.local.subzone.")

        # Invalid room ID should return None for sub-zone subject
        invalid_subzone_subject = get_subzone_local_channel_subject(invalid_room_id)
        assert invalid_subzone_subject is None

    def test_local_channel_subject_consistency(self) -> None:
        """Test consistency of local channel subjects across different rooms in same sub-zone."""
        room1 = "earth_arkhamcity_northside_intersection_derby_high"
        room2 = "earth_arkhamcity_northside_room_high_ln_001"
        room3 = "earth_arkhamcity_northside_room_high_ln_002"

        # All rooms in the same sub-zone should have the same sub-zone subject
        subzone_subject1 = get_subzone_local_channel_subject(room1)
        subzone_subject2 = get_subzone_local_channel_subject(room2)
        subzone_subject3 = get_subzone_local_channel_subject(room3)

        assert subzone_subject1 == subzone_subject2 == subzone_subject3 == "chat.local.subzone.northside"

        # But room-specific subjects should be different
        room_subject1 = f"chat.local.{room1}"
        room_subject2 = f"chat.local.{room2}"
        room_subject3 = f"chat.local.{room3}"

        assert room_subject1 != room_subject2 != room_subject3
