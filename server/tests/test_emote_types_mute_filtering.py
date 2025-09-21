"""
Tests for different emote types (predefined vs custom emotes) with mute filtering.

This module tests how the mute filtering system handles different types of emotes:
- Custom emotes (arbitrary text)
- Predefined emotes (triggered by specific commands like "twibble", "dance")
"""

import uuid
from unittest.mock import MagicMock, patch

import pytest

from server.game.chat_service import ChatService
from server.game.player_service import PlayerService


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
        self.room_id = "earth_arkham_city_sanitarium_room_hallway_001"

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
        global_mute_result = chat_service.mute_global(
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
            global_mute_result = chat_service.mute_global(
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
            global_mute_result = chat_service.mute_global(
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
            global_mute_result = chat_service.mute_global(
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
        global_mute_result = chat_service.mute_global(
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
