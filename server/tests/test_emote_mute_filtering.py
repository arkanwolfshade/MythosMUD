"""
Tests for emote message mute filtering functionality.

This module tests the critical bug where emote messages bypass the muting system.
The tests verify that muted players' emote messages are properly filtered out
during the broadcasting process.
"""

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, Mock, patch

import pytest

from ..game.chat_service import ChatService
from ..realtime.nats_message_handler import NATSMessageHandler


class TestEmoteMuteFiltering:
    """Test cases for emote message mute filtering functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        # Create mock dependencies
        self.mock_persistence = Mock()
        self.mock_room_service = Mock()
        self.mock_player_service = Mock()
        self.mock_connection_manager = Mock()

        # Create mock services
        self.mock_nats_service = Mock()
        self.mock_chat_logger = Mock()
        self.mock_rate_limiter = Mock()
        self.mock_user_manager = Mock()

        # Create the service instances
        self.chat_service = ChatService(self.mock_persistence, self.mock_room_service, self.mock_player_service)
        self.nats_handler = NATSMessageHandler(self.mock_nats_service)

        # Replace service dependencies with mocks
        self.chat_service.nats_service = self.mock_nats_service
        self.chat_service.chat_logger = self.mock_chat_logger
        self.chat_service.rate_limiter = self.mock_rate_limiter
        self.chat_service.user_manager = self.mock_user_manager

        # Create test players
        self.sender_player = Mock()
        self.sender_player.id = str(uuid.uuid4())
        self.sender_player.name = "Ithaqua"
        self.sender_player.current_room_id = "earth_arkhamcity_sanitarium_room_hallway_001"

        self.receiver_player = Mock()
        self.receiver_player.id = str(uuid.uuid4())
        self.receiver_player.name = "ArkanWolfshade"
        self.receiver_player.current_room_id = "earth_arkhamcity_sanitarium_room_hallway_001"

        # Test data from the bug report
        self.room_id = "earth_arkhamcity_sanitarium_room_hallway_001"
        self.sender_id = self.sender_player.id
        self.receiver_id = self.receiver_player.id

    @pytest.mark.asyncio
    async def test_emote_message_sent_successfully(self):
        """Test that emote messages are sent successfully when not muted."""
        # Setup
        action = "dance"

        self.mock_player_service.get_player_by_id.return_value = self.sender_player
        self.mock_rate_limiter.check_rate_limit.return_value = True
        self.mock_user_manager.is_channel_muted.return_value = False
        self.mock_user_manager.is_globally_muted.return_value = False
        self.mock_user_manager.can_send_message.return_value = True
        self.mock_nats_service.is_connected.return_value = True
        self.mock_nats_service.publish = AsyncMock(return_value=True)

        # Execute
        result = await self.chat_service.send_emote_message(self.sender_id, action)

        # Verify
        assert result["success"] is True
        assert "message" in result
        assert result["room_id"] == self.room_id
        assert result["message"]["channel"] == "emote"
        assert result["message"]["content"] == action

    @pytest.mark.asyncio
    async def test_emote_message_blocked_when_sender_muted(self):
        """Test that emote messages are blocked when sender is muted."""
        # Setup
        action = "dance"

        self.mock_player_service.get_player_by_id.return_value = self.sender_player
        self.mock_rate_limiter.check_rate_limit.return_value = True
        self.mock_user_manager.is_channel_muted.return_value = True  # Sender is muted

        # Execute
        result = await self.chat_service.send_emote_message(self.sender_id, action)

        # Verify
        assert result["success"] is False
        assert result["error"] == "You are muted in the say channel"

    @pytest.mark.asyncio
    async def test_emote_message_blocked_when_sender_globally_muted(self):
        """Test that emote messages are blocked when sender is globally muted."""
        # Setup
        action = "dance"

        self.mock_player_service.get_player_by_id.return_value = self.sender_player
        self.mock_rate_limiter.check_rate_limit.return_value = True
        self.mock_user_manager.is_channel_muted.return_value = False
        self.mock_user_manager.is_globally_muted.return_value = True  # Sender is globally muted

        # Execute
        result = await self.chat_service.send_emote_message(self.sender_id, action)

        # Verify
        assert result["success"] is False
        assert result["error"] == "You are globally muted and cannot send messages"

    @pytest.mark.asyncio
    async def test_broadcast_to_room_with_filtering_mutes_emote(self):
        """Test that _broadcast_to_room_with_filtering properly filters out muted players' emotes."""
        # Setup
        chat_event = {
            "type": "chat_message",
            "data": {
                "id": str(uuid.uuid4()),
                "sender_id": self.sender_id,
                "sender_name": "Ithaqua",
                "channel": "emote",
                "content": "dance",
                "timestamp": datetime.now(UTC).isoformat(),
            },
        }

        # Mock the global connection manager
        with patch("server.realtime.nats_message_handler.connection_manager") as mock_conn_mgr:
            # Mock room subscriptions
            mock_conn_mgr.room_subscriptions = {self.room_id: {self.sender_id, self.receiver_id}}
            mock_conn_mgr._canonical_room_id.return_value = self.room_id
            mock_conn_mgr.send_personal_message = AsyncMock()

            # Mock player in room check
            with patch.object(self.nats_handler, "_is_player_in_room", return_value=True):
                # Mock mute check - receiver has muted sender
                with patch.object(
                    self.nats_handler, "_is_player_muted_by_receiver_with_user_manager", return_value=True
                ):
                    # Execute
                    await self.nats_handler._broadcast_to_room_with_filtering(
                        self.room_id, chat_event, self.sender_id, "emote"
                    )

                    # Verify that the muted receiver did not receive the message
                    mock_conn_mgr.send_personal_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_broadcast_to_room_with_filtering_allows_unmuted_emote(self):
        """Test that _broadcast_to_room_with_filtering allows emotes to unmuted players."""
        # Setup
        chat_event = {
            "type": "chat_message",
            "data": {
                "id": str(uuid.uuid4()),
                "sender_id": self.sender_id,
                "sender_name": "Ithaqua",
                "channel": "emote",
                "content": "dance",
                "timestamp": datetime.now(UTC).isoformat(),
            },
        }

        # Mock the global connection manager
        with patch("server.realtime.nats_message_handler.connection_manager") as mock_conn_mgr:
            # Mock room subscriptions
            mock_conn_mgr.room_subscriptions = {self.room_id: {self.sender_id, self.receiver_id}}
            mock_conn_mgr._canonical_room_id.return_value = self.room_id
            mock_conn_mgr.send_personal_message = AsyncMock()

            # Mock player in room check
            with patch.object(self.nats_handler, "_is_player_in_room", return_value=True):
                # Mock mute check - receiver has NOT muted sender
                with patch.object(self.nats_handler, "_is_player_muted_by_receiver", return_value=False):
                    # Execute
                    await self.nats_handler._broadcast_to_room_with_filtering(
                        self.room_id, chat_event, self.sender_id, "emote"
                    )

                    # Verify that the unmuted receiver received the message
                    mock_conn_mgr.send_personal_message.assert_called_once_with(self.receiver_id, chat_event)

    def test_is_player_muted_by_receiver_returns_true_when_muted(self):
        """Test that _is_player_muted_by_receiver returns True when receiver has muted sender."""
        # Setup
        with patch("server.services.user_manager.user_manager") as mock_user_manager:
            mock_user_manager.is_player_muted.return_value = True
            mock_user_manager.is_player_muted_by_others.return_value = False
            mock_user_manager.is_admin.return_value = False

            # Execute
            result = self.nats_handler._is_player_muted_by_receiver(self.receiver_id, self.sender_id)

            # Verify
            assert result is True
            mock_user_manager.load_player_mutes.assert_called_once_with(self.receiver_id)
            mock_user_manager.is_player_muted.assert_called_once_with(self.receiver_id, self.sender_id)

    def test_is_player_muted_by_receiver_returns_false_when_not_muted(self):
        """Test that _is_player_muted_by_receiver returns False when receiver has not muted sender."""
        # Setup
        with patch("server.services.user_manager.user_manager") as mock_user_manager:
            mock_user_manager.is_player_muted.return_value = False
            mock_user_manager.is_player_muted_by_others.return_value = False
            mock_user_manager.is_admin.return_value = False

            # Execute
            result = self.nats_handler._is_player_muted_by_receiver(self.receiver_id, self.sender_id)

            # Verify
            assert result is False
            mock_user_manager.load_player_mutes.assert_called_once_with(self.receiver_id)
            mock_user_manager.is_player_muted.assert_called_once_with(self.receiver_id, self.sender_id)

    def test_is_player_muted_by_receiver_handles_global_mute(self):
        """Test that _is_player_muted_by_receiver handles global mute correctly."""
        # Setup
        with patch("server.services.user_manager.user_manager") as mock_user_manager:
            mock_user_manager.is_player_muted.return_value = False
            mock_user_manager.is_player_muted_by_others.return_value = True  # Sender is globally muted
            mock_user_manager.is_admin.return_value = False  # Receiver is not admin

            # Execute
            result = self.nats_handler._is_player_muted_by_receiver(self.receiver_id, self.sender_id)

            # Verify
            assert result is True
            mock_user_manager.is_player_muted_by_others.assert_called_once_with(self.sender_id)

    def test_is_player_muted_by_receiver_allows_admin_to_see_globally_muted(self):
        """Test that _is_player_muted_by_receiver allows admins to see globally muted players."""
        # Setup
        with patch("server.services.user_manager.user_manager") as mock_user_manager:
            mock_user_manager.is_player_muted.return_value = False
            mock_user_manager.is_player_muted_by_others.return_value = True  # Sender is globally muted
            mock_user_manager.is_admin.return_value = True  # Receiver is admin

            # Execute
            result = self.nats_handler._is_player_muted_by_receiver(self.receiver_id, self.sender_id)

            # Verify
            assert result is False  # Admin can see globally muted players
            mock_user_manager.is_admin.assert_called_once_with(self.receiver_id)

    def test_is_player_muted_by_receiver_handles_exception(self):
        """Test that _is_player_muted_by_receiver handles exceptions gracefully."""
        # Setup
        with patch("server.services.user_manager.user_manager") as mock_user_manager:
            mock_user_manager.load_player_mutes.side_effect = Exception("Database error")

            # Execute
            result = self.nats_handler._is_player_muted_by_receiver(self.receiver_id, self.sender_id)

            # Verify
            assert result is False  # Should return False on error

    @pytest.mark.asyncio
    async def test_emote_message_integration_mute_workflow(self):
        """Test the complete emote message mute workflow integration."""
        # Setup - Simulate the bug scenario from the bug report
        # 1. ArkanWolfshade mutes Ithaqua
        # 2. Ithaqua uses emote (should be filtered)
        # 3. ArkanWolfshade unmutes Ithaqua
        # 4. Ithaqua uses emote again (should be visible)

        # Step 1: Ithaqua sends emote while muted by ArkanWolfshade
        action = "dance"

        # Setup for emote sending
        self.mock_player_service.get_player_by_id.return_value = self.sender_player
        self.mock_rate_limiter.check_rate_limit.return_value = True
        self.mock_user_manager.is_channel_muted.return_value = False
        self.mock_user_manager.is_globally_muted.return_value = False
        self.mock_user_manager.can_send_message.return_value = True
        self.mock_nats_service.is_connected.return_value = True
        self.mock_nats_service.publish = AsyncMock(return_value=True)

        # Send emote message
        emote_result = await self.chat_service.send_emote_message(self.sender_id, action)
        assert emote_result["success"] is True

        # Step 2: Simulate NATS message processing with mute filtering
        chat_event = {"type": "chat_message", "data": emote_result["message"]}

        # Mock the global connection manager
        with patch("server.realtime.nats_message_handler.connection_manager") as mock_conn_mgr:
            # Mock room subscriptions
            mock_conn_mgr.room_subscriptions = {self.room_id: {self.sender_id, self.receiver_id}}
            mock_conn_mgr._canonical_room_id.return_value = self.room_id
            mock_conn_mgr.send_personal_message = AsyncMock()

            # Mock player in room check
            with patch.object(self.nats_handler, "_is_player_in_room", return_value=True):
                # Mock mute check - ArkanWolfshade has muted Ithaqua
                with patch.object(
                    self.nats_handler, "_is_player_muted_by_receiver_with_user_manager", return_value=True
                ):
                    # Process the emote message
                    await self.nats_handler._broadcast_to_room_with_filtering(
                        self.room_id, chat_event, self.sender_id, "emote"
                    )

                    # Verify that ArkanWolfshade did not receive the emote
                    mock_conn_mgr.send_personal_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_emote_message_integration_unmute_workflow(self):
        """Test the complete emote message unmute workflow integration."""
        # Setup - Simulate the unmute scenario from the bug report
        # ArkanWolfshade unmutes Ithaqua, then Ithaqua uses emote (should be visible)

        action = "dance"

        # Setup for emote sending
        self.mock_player_service.get_player_by_id.return_value = self.sender_player
        self.mock_rate_limiter.check_rate_limit.return_value = True
        self.mock_user_manager.is_channel_muted.return_value = False
        self.mock_user_manager.is_globally_muted.return_value = False
        self.mock_user_manager.can_send_message.return_value = True
        self.mock_nats_service.is_connected.return_value = True
        self.mock_nats_service.publish = AsyncMock(return_value=True)

        # Send emote message
        emote_result = await self.chat_service.send_emote_message(self.sender_id, action)
        assert emote_result["success"] is True

        # Simulate NATS message processing without mute filtering
        chat_event = {"type": "chat_message", "data": emote_result["message"]}

        # Mock the global connection manager
        with patch("server.realtime.nats_message_handler.connection_manager") as mock_conn_mgr:
            # Mock room subscriptions
            mock_conn_mgr.room_subscriptions = {self.room_id: {self.sender_id, self.receiver_id}}
            mock_conn_mgr._canonical_room_id.return_value = self.room_id
            mock_conn_mgr.send_personal_message = AsyncMock()

            # Mock player in room check
            with patch.object(self.nats_handler, "_is_player_in_room", return_value=True):
                # Mock mute check - ArkanWolfshade has NOT muted Ithaqua
                with patch.object(self.nats_handler, "_is_player_muted_by_receiver", return_value=False):
                    # Process the emote message
                    await self.nats_handler._broadcast_to_room_with_filtering(
                        self.room_id, chat_event, self.sender_id, "emote"
                    )

                    # Verify that ArkanWolfshade received the emote
                    mock_conn_mgr.send_personal_message.assert_called_once_with(self.receiver_id, chat_event)

    @pytest.mark.asyncio
    async def test_emote_message_uses_correct_channel_type(self):
        """Test that emote messages use the correct channel type for filtering."""
        # Setup
        action = "dance"

        self.mock_player_service.get_player_by_id.return_value = self.sender_player
        self.mock_rate_limiter.check_rate_limit.return_value = True
        self.mock_user_manager.is_channel_muted.return_value = False
        self.mock_user_manager.is_globally_muted.return_value = False
        self.mock_user_manager.can_send_message.return_value = True
        self.mock_nats_service.is_connected.return_value = True
        self.mock_nats_service.publish = AsyncMock(return_value=True)

        # Execute
        result = await self.chat_service.send_emote_message(self.sender_id, action)

        # Verify
        assert result["success"] is True
        assert result["message"]["channel"] == "emote"

    @pytest.mark.asyncio
    async def test_emote_message_rate_limiting(self):
        """Test that emote messages respect rate limiting."""
        # Setup
        action = "dance"

        self.mock_player_service.get_player_by_id.return_value = self.sender_player
        self.mock_rate_limiter.check_rate_limit.return_value = False  # Rate limited

        # Execute
        result = await self.chat_service.send_emote_message(self.sender_id, action)

        # Verify
        assert result["success"] is False
        assert result["error"] == "Rate limit exceeded. Please wait before sending another emote."
        assert result["rate_limited"] is True

    @pytest.mark.asyncio
    async def test_emote_message_validation(self):
        """Test emote message validation."""
        # Test empty action
        result = await self.chat_service.send_emote_message(self.sender_id, "")
        assert result["success"] is False
        assert result["error"] == "Action cannot be empty"

        # Test whitespace-only action
        result = await self.chat_service.send_emote_message(self.sender_id, "   \n\t   ")
        assert result["success"] is False
        assert result["error"] == "Action cannot be empty"

        # Test action too long
        long_action = "x" * 201  # Exceeds 200 character limit
        result = await self.chat_service.send_emote_message(self.sender_id, long_action)
        assert result["success"] is False
        assert result["error"] == "Action too long (max 200 characters)"

    @pytest.mark.asyncio
    async def test_emote_message_player_not_found(self):
        """Test emote message when player is not found."""
        # Setup
        action = "dance"
        self.mock_player_service.get_player_by_id.return_value = None

        # Execute
        result = await self.chat_service.send_emote_message(self.sender_id, action)

        # Verify
        assert result["success"] is False
        assert result["error"] == "Player not found"

    @pytest.mark.asyncio
    async def test_emote_message_player_not_in_room(self):
        """Test emote message when player is not in a room."""
        # Setup
        action = "dance"
        self.mock_player_service.get_player_by_id.return_value = self.sender_player
        self.mock_rate_limiter.check_rate_limit.return_value = True
        self.mock_user_manager.is_channel_muted.return_value = False
        self.mock_user_manager.is_globally_muted.return_value = False
        self.mock_user_manager.can_send_message.return_value = True
        self.sender_player.current_room_id = None  # Player not in room

        # Execute
        result = await self.chat_service.send_emote_message(self.sender_id, action)

        # Verify
        assert result["success"] is False
        assert result["error"] == "Player not in a room"
