"""
Tests for emote message mute filtering functionality.

This module tests the critical bug where emote messages bypass the muting system.
The tests verify that muted players' emote messages are properly filtered out
during the broadcasting process.
"""

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, Mock, call, patch

import pytest

from server.game.chat_service import ChatService
from server.game.player_service import PlayerService
from server.realtime.nats_message_handler import NATSMessageHandler


class TestEmoteMuteFiltering:
    """Test cases for emote message mute filtering functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        # Create mock dependencies
        self.mock_persistence = Mock()
        self.mock_room_service = Mock()
        self.mock_player_service = AsyncMock()
        self.mock_connection_manager = Mock()
        self.mock_connection_manager._canonical_room_id = Mock(
            return_value="earth_arkhamcity_sanitarium_room_hallway_001"
        )
        self.mock_connection_manager.room_subscriptions = {self.mock_connection_manager._canonical_room_id(): set()}
        self.mock_connection_manager.send_personal_message = AsyncMock()

        # Create the service instances
        self.mock_nats_service = Mock()
        self.mock_chat_logger = Mock()
        self.mock_rate_limiter = Mock()
        self.mock_user_manager = Mock()

        self.chat_service = ChatService(self.mock_persistence, self.mock_room_service, self.mock_player_service)
        self.nats_handler = NATSMessageHandler(self.mock_nats_service, connection_manager=self.mock_connection_manager)

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

        # AI Agent: Inject mock connection_manager via instance variable (no longer a global)
        #           Post-migration: connection_manager is injected via constructor
        mock_conn_mgr = Mock()
        mock_conn_mgr.room_subscriptions = {self.room_id: {self.sender_id, self.receiver_id}}
        mock_conn_mgr._canonical_room_id.return_value = self.room_id
        mock_conn_mgr.send_personal_message = AsyncMock()

        # Set mock on handler instance
        self.nats_handler.connection_manager = mock_conn_mgr

        # Mock player in room check
        with patch.object(self.nats_handler, "_is_player_in_room", return_value=True):
            # Mock mute check - receiver has muted sender
            with patch.object(self.nats_handler, "_is_player_muted_by_receiver_with_user_manager", return_value=True):
                # Execute
                await self.nats_handler._broadcast_to_room_with_filtering(
                    self.room_id, chat_event, self.sender_id, "emote"
                )

                # Verify sender gets echo but muted receiver does not
                # send_personal_message receives UUID object, not string
                mock_conn_mgr.send_personal_message.assert_called_once_with(uuid.UUID(self.sender_id), chat_event)

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

        connection_manager = self.nats_handler.connection_manager
        connection_manager.room_subscriptions = {self.room_id: {self.sender_id, self.receiver_id}}
        connection_manager._canonical_room_id.return_value = self.room_id
        connection_manager.send_personal_message = AsyncMock()

        # Mock player in room check
        with patch.object(self.nats_handler, "_is_player_in_room", return_value=True):
            # Mock mute check - ArkanWolfshade has NOT muted Ithaqua
            with patch.object(self.nats_handler, "_is_player_muted_by_receiver", return_value=False):
                # Process the emote message
                await self.nats_handler._broadcast_to_room_with_filtering(
                    self.room_id, chat_event, self.sender_id, "emote"
                )

                # Verify both sender echo and receiver delivery
                # send_personal_message receives UUID objects, not strings
                expected_calls = [
                    call(uuid.UUID(self.receiver_id), chat_event),
                    call(uuid.UUID(self.sender_id), chat_event),
                ]
                connection_manager.send_personal_message.assert_has_calls(expected_calls, any_order=True)
                connection_manager.send_personal_message.reset_mock()

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

        # AI Agent: Inject mock connection_manager via instance variable (no longer a global)
        mock_conn_mgr = Mock()
        mock_conn_mgr.room_subscriptions = {self.room_id: {self.sender_id, self.receiver_id}}
        mock_conn_mgr._canonical_room_id.return_value = self.room_id
        mock_conn_mgr.send_personal_message = AsyncMock()

        # Set mock on handler instance
        self.nats_handler._connection_manager = mock_conn_mgr

        # Mock player in room check
        with patch.object(self.nats_handler, "_is_player_in_room", return_value=True):
            # Mock mute check - ArkanWolfshade has muted Ithaqua
            with patch.object(self.nats_handler, "_is_player_muted_by_receiver_with_user_manager", return_value=True):
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

        connection_manager = self.nats_handler.connection_manager
        connection_manager.room_subscriptions = {self.room_id: {self.sender_id, self.receiver_id}}
        connection_manager._canonical_room_id.return_value = self.room_id
        connection_manager.send_personal_message = AsyncMock()

        # Mock player in room check
        with patch.object(self.nats_handler, "_is_player_in_room", return_value=True):
            # Mock mute check - ArkanWolfshade has NOT muted Ithaqua
            with patch.object(self.nats_handler, "_is_player_muted_by_receiver", return_value=False):
                # Process the emote message
                await self.nats_handler._broadcast_to_room_with_filtering(
                    self.room_id, chat_event, self.sender_id, "emote"
                )

                # Verify that ArkanWolfshade received the emote
                # send_personal_message receives UUID objects, not strings
                expected_calls = [
                    call(uuid.UUID(self.receiver_id), chat_event),
                    call(uuid.UUID(self.sender_id), chat_event),
                ]
                connection_manager.send_personal_message.assert_has_calls(expected_calls, any_order=True)

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


# ============================================================================
# Tests merged from test_emote_types_filtering_legacy.py
# ============================================================================


class TestEmoteTypesMuteFiltering:
    """Tests for different emote types with mute filtering."""

    def setup_method(self):
        """Set up test fixtures."""
        # Mock services
        self.mock_persistence = MagicMock()
        self.mock_room_service = MagicMock()
        self.mock_player_service = MagicMock(spec=PlayerService)

        # Test data
        self.muter_id = str(uuid.uuid4())
        self.muter_name = "ArkanWolfshade"
        self.target_id = str(uuid.uuid4())
        self.target_name = "Ithaqua"
        self.room_id = "earth_arkhamcity_sanitarium_room_hallway_001"

        # Mock player objects
        self.muter_player = MagicMock()
        self.muter_player.id = self.muter_id
        self.muter_player.name = self.muter_name
        self.muter_player.current_room_id = self.room_id

        self.target_player = MagicMock()
        self.target_player.id = self.target_id
        self.target_player.name = self.target_name
        self.target_player.current_room_id = self.room_id

    def _create_chat_service_with_mocks(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Helper method to create ChatService with mocked dependencies."""
        chat_service = ChatService(
            persistence=self.mock_persistence,
            room_service=self.mock_room_service,
            player_service=self.mock_player_service,
            user_manager_instance=mock_user_manager,
        )

        # Replace services with mocks
        chat_service.nats_service = mock_nats_service
        chat_service.rate_limiter = mock_rate_limiter

        return chat_service

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_custom_emote_mute_filtering(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test that custom emotes are properly filtered when player is muted."""
        # Create chat service with mocked user manager
        chat_service = self._create_chat_service_with_mocks(mock_user_manager, mock_rate_limiter, mock_nats_service)

        # Setup mocks
        mock_nats_service.is_connected.return_value = True

        # Make NATS publish async
        async def mock_publish(*args, **kwargs):
            return True

        mock_nats_service.publish = mock_publish

        mock_rate_limiter.check_rate_limit.return_value = True
        mock_user_manager.is_channel_muted.return_value = False
        mock_user_manager.is_globally_muted.return_value = False
        mock_user_manager.can_send_message.return_value = True
        mock_user_manager.load_player_mutes.return_value = True
        mock_user_manager.is_player_muted.return_value = False
        mock_user_manager.mute_player.return_value = True
        mock_user_manager.mute_global.return_value = True
        mock_user_manager.is_admin.return_value = True

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Test custom emote when not muted
        emote_result = await chat_service.send_emote_message(self.target_id, "waves hello")
        assert emote_result["success"] is True
        assert emote_result["message"]["channel"] == "emote"
        assert emote_result["message"]["content"] == "waves hello"

        # Apply global mute to the player
        global_mute_result = await chat_service.mute_global(
            muter_id=self.muter_id,
            target_player_name=self.target_name,
            duration_minutes=60,
            reason="Test mute filtering",
        )
        assert global_mute_result is True

        # Test custom emote when globally muted
        mock_user_manager.is_globally_muted.return_value = True
        emote_result = await chat_service.send_emote_message(self.target_id, "waves goodbye")
        assert emote_result["success"] is False
        assert "globally muted" in emote_result["error"].lower()

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_predefined_emote_mute_filtering(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test that predefined emotes are properly filtered when player is muted."""
        # Create chat service with mocked user manager
        chat_service = self._create_chat_service_with_mocks(mock_user_manager, mock_rate_limiter, mock_nats_service)

        # Setup mocks
        mock_nats_service.is_connected.return_value = True

        # Make NATS publish async
        async def mock_publish(*args, **kwargs):
            return True

        mock_nats_service.publish = mock_publish

        mock_rate_limiter.check_rate_limit.return_value = True
        mock_user_manager.is_channel_muted.return_value = False
        mock_user_manager.is_globally_muted.return_value = False
        mock_user_manager.can_send_message.return_value = True
        mock_user_manager.load_player_mutes.return_value = True
        mock_user_manager.is_player_muted.return_value = False
        mock_user_manager.mute_global.return_value = True
        mock_user_manager.is_admin.return_value = True

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Mock EmoteService for predefined emotes
        with patch("server.game.emote_service.EmoteService") as mock_emote_service_class:
            mock_emote_service = MagicMock()
            mock_emote_service_class.return_value = mock_emote_service
            mock_emote_service.is_emote_alias.return_value = True
            mock_emote_service.format_emote_messages.return_value = ("You twibble.", f"{self.target_name} twibbles.")

            # Test predefined emote when not muted
            emote_result = await chat_service.send_predefined_emote(self.target_id, "twibble")
            assert emote_result["success"] is True
            assert emote_result["message"]["channel"] == "emote"
            assert "twibbles" in emote_result["message"]["content"]

            # Apply global mute to the player
            global_mute_result = await chat_service.mute_global(
                muter_id=self.muter_id,
                target_player_name=self.target_name,
                duration_minutes=60,
                reason="Test predefined emote mute filtering",
            )
            assert global_mute_result is True

            # Test predefined emote when globally muted
            mock_user_manager.is_globally_muted.return_value = True
            emote_result = await chat_service.send_predefined_emote(self.target_id, "twibble")
            assert emote_result["success"] is False
            assert "globally muted" in emote_result["error"].lower()

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_multiple_predefined_emotes_mute_filtering(
        self, mock_user_manager, mock_rate_limiter, mock_nats_service
    ):
        """Test that multiple predefined emotes are properly filtered when player is muted."""
        # Create chat service with mocked user manager
        chat_service = self._create_chat_service_with_mocks(mock_user_manager, mock_rate_limiter, mock_nats_service)

        # Setup mocks
        mock_nats_service.is_connected.return_value = True

        # Make NATS publish async
        async def mock_publish(*args, **kwargs):
            return True

        mock_nats_service.publish = mock_publish

        mock_rate_limiter.check_rate_limit.return_value = True
        mock_user_manager.is_channel_muted.return_value = False
        mock_user_manager.is_globally_muted.return_value = False
        mock_user_manager.can_send_message.return_value = True
        mock_user_manager.load_player_mutes.return_value = True
        mock_user_manager.is_player_muted.return_value = False
        mock_user_manager.mute_global.return_value = True
        mock_user_manager.is_admin.return_value = True

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Mock EmoteService for predefined emotes
        with patch("server.game.emote_service.EmoteService") as mock_emote_service_class:
            mock_emote_service = MagicMock()
            mock_emote_service_class.return_value = mock_emote_service
            mock_emote_service.is_emote_alias.return_value = True

            # Test different predefined emotes when not muted
            predefined_emotes = [
                ("twibble", "twibbles"),
                ("dance", "dances"),
                ("laugh", "laughs"),
                ("cry", "cries"),
                ("wave", "waves"),
            ]

            for emote_command, emote_action in predefined_emotes:
                mock_emote_service.format_emote_messages.return_value = (
                    f"You {emote_action}.",
                    f"{self.target_name} {emote_action}.",
                )

                emote_result = await chat_service.send_predefined_emote(self.target_id, emote_command)
                assert emote_result["success"] is True
                assert emote_result["message"]["channel"] == "emote"
                assert emote_action in emote_result["message"]["content"]

            # Apply global mute to the player
            global_mute_result = await chat_service.mute_global(
                muter_id=self.muter_id,
                target_player_name=self.target_name,
                duration_minutes=60,
                reason="Test multiple predefined emotes mute filtering",
            )
            assert global_mute_result is True

            # Test all predefined emotes when globally muted
            mock_user_manager.is_globally_muted.return_value = True
            for emote_command, _emote_action in predefined_emotes:
                emote_result = await chat_service.send_predefined_emote(self.target_id, emote_command)
                assert emote_result["success"] is False
                assert "globally muted" in emote_result["error"].lower()

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_custom_vs_predefined_emote_consistency(
        self, mock_user_manager, mock_rate_limiter, mock_nats_service
    ):
        """Test that custom and predefined emotes are handled consistently for mute filtering."""
        # Create chat service with mocked user manager
        chat_service = self._create_chat_service_with_mocks(mock_user_manager, mock_rate_limiter, mock_nats_service)

        # Setup mocks
        mock_nats_service.is_connected.return_value = True

        # Make NATS publish async
        async def mock_publish(*args, **kwargs):
            return True

        mock_nats_service.publish = mock_publish

        mock_rate_limiter.check_rate_limit.return_value = True
        mock_user_manager.is_channel_muted.return_value = False
        mock_user_manager.is_globally_muted.return_value = False
        mock_user_manager.can_send_message.return_value = True
        mock_user_manager.load_player_mutes.return_value = True
        mock_user_manager.is_player_muted.return_value = False
        mock_user_manager.mute_global.return_value = True
        mock_user_manager.is_admin.return_value = True

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Mock EmoteService for predefined emotes
        with patch("server.game.emote_service.EmoteService") as mock_emote_service_class:
            mock_emote_service = MagicMock()
            mock_emote_service_class.return_value = mock_emote_service
            mock_emote_service.is_emote_alias.return_value = True
            mock_emote_service.format_emote_messages.return_value = ("You dance.", f"{self.target_name} dances.")

            # Test both emote types when not muted
            custom_emote_result = await chat_service.send_emote_message(self.target_id, "dances")
            assert custom_emote_result["success"] is True
            assert custom_emote_result["message"]["content"] == "dances"

            predefined_emote_result = await chat_service.send_predefined_emote(self.target_id, "dance")
            assert predefined_emote_result["success"] is True
            assert "dances" in predefined_emote_result["message"]["content"]

            # Apply global mute to the player
            global_mute_result = await chat_service.mute_global(
                muter_id=self.muter_id,
                target_player_name=self.target_name,
                duration_minutes=60,
                reason="Test emote consistency mute filtering",
            )
            assert global_mute_result is True

            # Test both emote types when globally muted - both should be blocked
            mock_user_manager.is_globally_muted.return_value = True

            custom_emote_result = await chat_service.send_emote_message(self.target_id, "dances")
            assert custom_emote_result["success"] is False
            assert "globally muted" in custom_emote_result["error"].lower()

            predefined_emote_result = await chat_service.send_predefined_emote(self.target_id, "dance")
            assert predefined_emote_result["success"] is False
            assert "globally muted" in predefined_emote_result["error"].lower()

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_emote_type_error_handling(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test error handling for different emote types."""
        # Create chat service with mocked user manager
        chat_service = self._create_chat_service_with_mocks(mock_user_manager, mock_rate_limiter, mock_nats_service)

        # Setup mocks
        mock_nats_service.is_connected.return_value = True
        mock_nats_service.publish.return_value = True
        mock_rate_limiter.check_rate_limit.return_value = True
        mock_user_manager.is_channel_muted.return_value = False
        mock_user_manager.is_globally_muted.return_value = False
        mock_user_manager.can_send_message.return_value = True
        mock_user_manager.load_player_mutes.return_value = True
        mock_user_manager.is_player_muted.return_value = False

        # Test custom emote with non-existent player
        self.mock_player_service.get_player_by_id.return_value = None
        custom_emote_result = await chat_service.send_emote_message("non-existent-id", "waves")
        assert custom_emote_result["success"] is False
        assert "not found" in custom_emote_result["error"].lower()

        # Test predefined emote with non-existent player
        predefined_emote_result = await chat_service.send_predefined_emote("non-existent-id", "twibble")
        assert predefined_emote_result["success"] is False
        assert "not found" in predefined_emote_result["error"].lower()

        # Test custom emote with empty content
        self.mock_player_service.get_player_by_id.return_value = self.target_player
        custom_emote_result = await chat_service.send_emote_message(self.target_id, "")
        assert custom_emote_result["success"] is False
        assert "empty" in custom_emote_result["error"].lower()

        # Test predefined emote with invalid command
        with patch("server.game.emote_service.EmoteService") as mock_emote_service_class:
            mock_emote_service = MagicMock()
            mock_emote_service_class.return_value = mock_emote_service
            mock_emote_service.is_emote_alias.return_value = False  # Invalid emote command

            predefined_emote_result = await chat_service.send_predefined_emote(self.target_id, "invalid_emote")
            assert predefined_emote_result["success"] is False
            assert "unknown emote" in predefined_emote_result["error"].lower()

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_emote_type_global_mute_filtering(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test that both custom and predefined emotes are filtered by global mutes."""
        # Create chat service with mocked user manager
        chat_service = self._create_chat_service_with_mocks(mock_user_manager, mock_rate_limiter, mock_nats_service)

        # Setup mocks
        mock_nats_service.is_connected.return_value = True
        mock_nats_service.publish.return_value = True
        mock_rate_limiter.check_rate_limit.return_value = True
        mock_user_manager.is_channel_muted.return_value = False
        mock_user_manager.is_globally_muted.return_value = False
        mock_user_manager.can_send_message.return_value = True
        mock_user_manager.load_player_mutes.return_value = True
        mock_user_manager.is_player_muted.return_value = False
        mock_user_manager.mute_global.return_value = True
        mock_user_manager.is_admin.return_value = True

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Apply global mute
        global_mute_result = await chat_service.mute_global(
            muter_id=self.muter_id, target_player_name=self.target_name, duration_minutes=60, reason="Global mute test"
        )
        assert global_mute_result is True

        # Test both emote types when globally muted
        mock_user_manager.is_globally_muted.return_value = True

        custom_emote_result = await chat_service.send_emote_message(self.target_id, "waves")
        assert custom_emote_result["success"] is False
        assert "globally muted" in custom_emote_result["error"].lower()

        with patch("server.game.emote_service.EmoteService") as mock_emote_service_class:
            mock_emote_service = MagicMock()
            mock_emote_service_class.return_value = mock_emote_service
            mock_emote_service.is_emote_alias.return_value = True
            mock_emote_service.format_emote_messages.return_value = ("You twibble.", f"{self.target_name} twibbles.")

            predefined_emote_result = await chat_service.send_predefined_emote(self.target_id, "twibble")
            assert predefined_emote_result["success"] is False
            assert "globally muted" in predefined_emote_result["error"].lower()

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_emote_type_rate_limiting(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test that rate limiting works consistently for both emote types."""
        # Create chat service with mocked user manager
        chat_service = self._create_chat_service_with_mocks(mock_user_manager, mock_rate_limiter, mock_nats_service)

        # Setup mocks
        mock_nats_service.is_connected.return_value = True
        mock_nats_service.publish.return_value = True
        mock_rate_limiter.check_rate_limit.return_value = True
        mock_user_manager.is_channel_muted.return_value = False
        mock_user_manager.is_globally_muted.return_value = False
        mock_user_manager.can_send_message.return_value = True
        mock_user_manager.load_player_mutes.return_value = True
        mock_user_manager.is_player_muted.return_value = False

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Test both emote types when rate limited
        mock_rate_limiter.check_rate_limit.return_value = False  # Rate limited

        custom_emote_result = await chat_service.send_emote_message(self.target_id, "waves")
        assert custom_emote_result["success"] is False
        assert "rate limit" in custom_emote_result["error"].lower()

        with patch("server.game.emote_service.EmoteService") as mock_emote_service_class:
            mock_emote_service = MagicMock()
            mock_emote_service_class.return_value = mock_emote_service
            mock_emote_service.is_emote_alias.return_value = True
            mock_emote_service.format_emote_messages.return_value = ("You twibble.", f"{self.target_name} twibbles.")

            predefined_emote_result = await chat_service.send_predefined_emote(self.target_id, "twibble")
            assert predefined_emote_result["success"] is False
            assert "rate limit" in predefined_emote_result["error"].lower()
