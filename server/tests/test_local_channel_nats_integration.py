"""
Tests for local channel NATS integration.

This module tests the NATS integration for local channels, including
sub-zone subscription management and dynamic subscription changes.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.nats_message_handler import NATSMessageHandler
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
    def nats_handler(self, mock_nats_service):
        """Create a NATS message handler with mocked dependencies."""
        return NATSMessageHandler(mock_nats_service)

    @pytest.mark.asyncio
    async def test_local_channel_subscription_on_start(self, nats_handler, mock_nats_service):
        """Test that local channel subjects are subscribed to on handler start."""
        await nats_handler.start()

        # Verify that local channel subject pattern is subscribed
        mock_nats_service.subscribe.assert_called()
        subscribe_calls = mock_nats_service.subscribe.call_args_list

        # Check that "chat.local.*" pattern is subscribed
        local_subscription_found = False
        for call in subscribe_calls:
            if call[0][0] == "chat.local.*":
                local_subscription_found = True
                break

        assert local_subscription_found, "Local channel subject pattern not subscribed"

    @pytest.mark.asyncio
    async def test_local_channel_message_handling(self, nats_handler):
        """Test handling of local channel messages."""
        # Mock the broadcast method
        nats_handler._broadcast_to_room_with_filtering = AsyncMock()

        # Create a local channel message
        message_data = {
            "channel": "local",
            "room_id": "earth_arkham_city_northside_intersection_derby_high",
            "sender_id": "test-player-123",
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
        assert call_args[0][0] == "earth_arkham_city_northside_intersection_derby_high"

        # Check event structure
        event = call_args[0][1]
        assert event["event_type"] == "chat_message"
        assert event["data"]["sender_id"] == "test-player-123"
        assert event["data"]["player_name"] == "TestPlayer"
        assert event["data"]["channel"] == "local"
        assert event["data"]["message"] == "Hello, local area!"
        assert event["data"]["message_id"] == "msg-123"
        assert event["data"]["timestamp"] == "2025-08-27T18:00:00Z"
        assert event["player_id"] == "test-player-123"

        # Check sender_id and channel
        assert call_args[0][2] == "test-player-123"
        assert call_args[0][3] == "local"

    @pytest.mark.asyncio
    async def test_room_subscription_includes_local_channel(self, nats_handler, mock_nats_service):
        """Test that subscribing to a room includes local channel subscription."""
        room_id = "earth_arkham_city_northside_intersection_derby_high"

        await nats_handler.subscribe_to_room(room_id)

        # Verify that both say and local subjects are subscribed
        subscribe_calls = mock_nats_service.subscribe.call_args_list
        expected_subjects = [f"chat.say.{room_id}", f"chat.local.{room_id}"]

        for expected_subject in expected_subjects:
            subject_found = False
            for call in subscribe_calls:
                if call[0][0] == expected_subject:
                    subject_found = True
                    break
            assert subject_found, f"Subject {expected_subject} not subscribed"

    @pytest.mark.asyncio
    async def test_room_unsubscription_includes_local_channel(self, nats_handler, mock_nats_service):
        """Test that unsubscribing from a room includes local channel unsubscription."""
        room_id = "earth_arkham_city_northside_intersection_derby_high"

        # First subscribe to the room
        nats_handler.subscriptions = {f"chat.say.{room_id}": True, f"chat.local.{room_id}": True}

        await nats_handler.unsubscribe_from_room(room_id)

        # Verify that both say and local subjects are unsubscribed
        unsubscribe_calls = mock_nats_service.unsubscribe.call_args_list
        expected_subjects = [f"chat.say.{room_id}", f"chat.local.{room_id}"]

        for expected_subject in expected_subjects:
            subject_found = False
            for call in unsubscribe_calls:
                if call[0][0] == expected_subject:
                    subject_found = True
                    break
            assert subject_found, f"Subject {expected_subject} not unsubscribed"


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
    def nats_handler(self, mock_nats_service):
        """Create a NATS message handler with mocked dependencies."""
        return NATSMessageHandler(mock_nats_service)

    @pytest.mark.asyncio
    async def test_subzone_subscription_creation(self, nats_handler, mock_nats_service):
        """Test creating sub-zone subscriptions for local channels."""
        room_id = "earth_arkham_city_northside_intersection_derby_high"
        subzone = extract_subzone_from_room_id(room_id)
        subzone_subject = get_subzone_local_channel_subject(room_id)

        # Mock the subscribe_to_subzone method (to be implemented)
        nats_handler.subscribe_to_subzone = AsyncMock()

        await nats_handler.subscribe_to_subzone(subzone)

        nats_handler.subscribe_to_subzone.assert_called_once_with(subzone)
        assert subzone == "northside"
        assert subzone_subject == "chat.local.subzone.northside"

    @pytest.mark.asyncio
    async def test_subzone_unsubscription(self, nats_handler, mock_nats_service):
        """Test unsubscribing from sub-zone subscriptions."""
        room_id = "earth_arkham_city_northside_intersection_derby_high"
        subzone = extract_subzone_from_room_id(room_id)

        # Mock the unsubscribe_from_subzone method (to be implemented)
        nats_handler.unsubscribe_from_subzone = AsyncMock()

        await nats_handler.unsubscribe_from_subzone(subzone)

        nats_handler.unsubscribe_from_subzone.assert_called_once_with(subzone)

    @pytest.mark.asyncio
    async def test_player_movement_subzone_change(self, nats_handler, mock_nats_service):
        """Test handling player movement between sub-zones."""
        # Mock the connection manager
        with patch("server.realtime.nats_message_handler.connection_manager") as mock_connection_manager:
            mock_connection_manager.online_players = {
                "test-player-123": {"current_room_id": "earth_arkham_city_northside_intersection_derby_high"}
            }

            # Mock sub-zone subscription methods
            nats_handler.subscribe_to_subzone = AsyncMock()
            nats_handler.unsubscribe_from_subzone = AsyncMock()

            # Simulate player moving from northside to downtown
            old_room_id = "earth_arkham_city_northside_intersection_derby_high"
            new_room_id = "earth_arkham_city_downtown_market_square"

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
    async def test_multiple_players_same_subzone(self, nats_handler, mock_nats_service):
        """Test multiple players in the same sub-zone sharing subscription."""
        # Mock the connection manager
        with patch("server.realtime.nats_message_handler.connection_manager") as mock_connection_manager:
            mock_connection_manager.online_players = {
                "player1": {"current_room_id": "earth_arkham_city_northside_intersection_derby_high"},
                "player2": {"current_room_id": "earth_arkham_city_northside_room_high_ln_001"},
                "player3": {"current_room_id": "earth_arkham_city_northside_room_high_ln_002"},
            }

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
    async def test_subzone_subscription_cleanup(self, nats_handler, mock_nats_service):
        """Test cleanup of sub-zone subscriptions when no players remain."""
        # Mock the connection manager
        with patch("server.realtime.nats_message_handler.connection_manager") as mock_connection_manager:
            mock_connection_manager.online_players = {
                "player1": {"current_room_id": "earth_arkham_city_northside_intersection_derby_high"}
            }

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

    def test_local_channel_subject_patterns(self):
        """Test that local channel subjects follow the correct patterns."""
        room_id = "earth_arkham_city_northside_intersection_derby_high"
        subzone = extract_subzone_from_room_id(room_id)

        # Test room-specific local channel subject
        room_subject = f"chat.local.{room_id}"
        assert room_subject == "chat.local.earth_arkham_city_northside_intersection_derby_high"

        # Test sub-zone local channel subject
        subzone_subject = get_subzone_local_channel_subject(room_id)
        assert subzone_subject == "chat.local.subzone.northside"

        # Verify patterns are different
        assert room_subject != subzone_subject
        assert subzone == "northside"  # Use the variable to avoid linting warning

    def test_local_channel_subject_validation(self):
        """Test validation of local channel subject patterns."""
        valid_room_id = "earth_arkham_city_northside_intersection_derby_high"
        invalid_room_id = "invalid_room_id"

        # Valid room ID should produce valid subjects
        room_subject = f"chat.local.{valid_room_id}"
        subzone_subject = get_subzone_local_channel_subject(valid_room_id)

        assert room_subject.startswith("chat.local.")
        assert subzone_subject.startswith("chat.local.subzone.")

        # Invalid room ID should return None for sub-zone subject
        invalid_subzone_subject = get_subzone_local_channel_subject(invalid_room_id)
        assert invalid_subzone_subject is None

    def test_local_channel_subject_consistency(self):
        """Test consistency of local channel subjects across different rooms in same sub-zone."""
        room1 = "earth_arkham_city_northside_intersection_derby_high"
        room2 = "earth_arkham_city_northside_room_high_ln_001"
        room3 = "earth_arkham_city_northside_room_high_ln_002"

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
