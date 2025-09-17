"""
Tests for temporary vs permanent mutes with emote filtering.

This module tests how the mute filtering system handles different types of mutes:
- Temporary mutes (with duration)
- Permanent mutes (no duration)
- Mute expiration behavior
- Emote filtering consistency across mute types
"""

import uuid
from unittest.mock import MagicMock, patch

import pytest

from server.game.chat_service import ChatService
from server.game.player_service import PlayerService


class TestTemporaryPermanentMutes:
    """Tests for temporary vs permanent mutes with emote filtering."""

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

    @pytest.mark.asyncio
    @patch("server.game.chat_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_temporary_mute_with_short_duration(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test temporary mute with short duration (5 minutes)."""
        # Setup mocks
        mock_nats_service.is_connected.return_value = True
        mock_nats_service.publish = MagicMock(return_value=True)
        # Make it async

        async def mock_publish(*args, **kwargs):
            return True

        mock_nats_service.publish = mock_publish
        mock_rate_limiter.check_rate_limit.return_value = True
        mock_user_manager.is_channel_muted.return_value = False
        mock_user_manager.is_globally_muted.return_value = False
        mock_user_manager.can_send_message.return_value = True
        mock_user_manager.load_player_mutes.return_value = True
        mock_user_manager.is_player_muted.return_value = False
        mock_user_manager.is_player_muted_by_others.return_value = False
        mock_user_manager.mute_player.return_value = True
        mock_user_manager.mute_global.return_value = True
        mock_user_manager.is_admin.return_value = True

        # Create chat service with mocked user manager
        chat_service = ChatService(
            persistence=self.mock_persistence,
            room_service=self.mock_room_service,
            player_service=self.mock_player_service,
            user_manager_instance=mock_user_manager,
        )

        # Replace services with mocks
        chat_service.nats_service = mock_nats_service
        chat_service.rate_limiter = mock_rate_limiter

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Apply temporary global mute (5 minutes) - this should prevent sending messages
        mute_result = mock_user_manager.mute_global(
            muter_id=self.muter_id,
            muter_name="admin",
            target_id=self.target_id,
            target_name=self.target_name,
            duration_minutes=5,
            reason="Test mute",
        )
        assert mute_result is True

        # Test emote is blocked when globally muted
        mock_user_manager.is_globally_muted.return_value = True
        emote_result = await chat_service.send_emote_message(self.target_id, "waves")
        assert emote_result["success"] is False
        assert "globally muted" in emote_result["error"].lower()

        # Simulate mute expiration (mock user manager to return False)
        mock_user_manager.is_globally_muted.return_value = False

        # Test emote is allowed after expiration
        emote_result = await chat_service.send_emote_message(self.target_id, "waves")
        assert emote_result["success"] is True
        assert emote_result["message"]["content"] == "waves"

    @pytest.mark.asyncio
    @patch("server.game.chat_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_temporary_mute_with_long_duration(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test temporary mute with long duration (1 hour)."""
        # Setup mocks
        mock_nats_service.is_connected.return_value = True
        mock_nats_service.publish = MagicMock(return_value=True)
        # Make it async

        async def mock_publish(*args, **kwargs):
            return True

        mock_nats_service.publish = mock_publish
        mock_rate_limiter.check_rate_limit.return_value = True
        mock_user_manager.is_channel_muted.return_value = False
        mock_user_manager.is_globally_muted.return_value = False
        mock_user_manager.can_send_message.return_value = True
        mock_user_manager.load_player_mutes.return_value = True
        mock_user_manager.is_player_muted.return_value = False
        mock_user_manager.is_player_muted_by_others.return_value = False
        mock_user_manager.mute_player.return_value = True
        mock_user_manager.mute_global.return_value = True
        mock_user_manager.is_admin.return_value = True

        # Create chat service with mocked user manager
        chat_service = ChatService(
            persistence=self.mock_persistence,
            room_service=self.mock_room_service,
            player_service=self.mock_player_service,
            user_manager_instance=mock_user_manager,
        )

        # Replace services with mocks
        chat_service.nats_service = mock_nats_service
        chat_service.rate_limiter = mock_rate_limiter

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Apply temporary global mute (1 hour) - this should prevent sending messages
        mute_result = mock_user_manager.mute_global(
            muter_id=self.muter_id,
            muter_name="admin",
            target_id=self.target_id,
            target_name=self.target_name,
            duration_minutes=60,
            reason="Test mute",
        )
        assert mute_result is True

        # Test emote is blocked when globally muted
        mock_user_manager.is_globally_muted.return_value = True
        emote_result = await chat_service.send_emote_message(self.target_id, "dances")
        assert emote_result["success"] is False
        assert "globally muted" in emote_result["error"].lower()

        # Test multiple emotes are blocked during mute period
        emote_result = await chat_service.send_emote_message(self.target_id, "laughs")
        assert emote_result["success"] is False

        emote_result = await chat_service.send_emote_message(self.target_id, "cries")
        assert emote_result["success"] is False

    @pytest.mark.asyncio
    @patch("server.game.chat_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_permanent_mute_behavior(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test permanent mute behavior (no duration)."""
        # Setup mocks
        mock_nats_service.is_connected.return_value = True
        mock_nats_service.publish = MagicMock(return_value=True)
        # Make it async

        async def mock_publish(*args, **kwargs):
            return True

        mock_nats_service.publish = mock_publish
        mock_rate_limiter.check_rate_limit.return_value = True
        mock_user_manager.is_channel_muted.return_value = False
        mock_user_manager.is_globally_muted.return_value = False
        mock_user_manager.can_send_message.return_value = True
        mock_user_manager.load_player_mutes.return_value = True
        mock_user_manager.is_player_muted.return_value = False
        mock_user_manager.is_player_muted_by_others.return_value = False
        mock_user_manager.mute_player.return_value = True
        mock_user_manager.mute_global.return_value = True
        mock_user_manager.is_admin.return_value = True

        # Create chat service with mocked user manager
        chat_service = ChatService(
            persistence=self.mock_persistence,
            room_service=self.mock_room_service,
            player_service=self.mock_player_service,
            user_manager_instance=mock_user_manager,
        )

        # Replace services with mocks
        chat_service.nats_service = mock_nats_service
        chat_service.rate_limiter = mock_rate_limiter

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Apply permanent global mute (no duration) - this should prevent sending messages
        mute_result = mock_user_manager.mute_global(
            muter_id=self.muter_id,
            muter_name="admin",
            target_id=self.target_id,
            target_name=self.target_name,
            duration_minutes=None,  # Permanent
            reason="Test permanent mute",
        )
        assert mute_result is True

        # Test emote is blocked when permanently globally muted
        mock_user_manager.is_globally_muted.return_value = True
        emote_result = await chat_service.send_emote_message(self.target_id, "waves")
        assert emote_result["success"] is False
        assert "globally muted" in emote_result["error"].lower()

        # Test multiple emotes are blocked (permanent mute persists)
        emote_result = await chat_service.send_emote_message(self.target_id, "dances")
        assert emote_result["success"] is False

        emote_result = await chat_service.send_emote_message(self.target_id, "laughs")
        assert emote_result["success"] is False

        # Test predefined emotes are also blocked
        with patch("server.game.emote_service.EmoteService") as mock_emote_service_class:
            mock_emote_service = MagicMock()
            mock_emote_service_class.return_value = mock_emote_service
            mock_emote_service.is_emote_alias.return_value = True
            mock_emote_service.format_emote_messages.return_value = ("You twibble.", f"{self.target_name} twibbles.")

            emote_result = await chat_service.send_predefined_emote(self.target_id, "twibble")
            assert emote_result["success"] is False
            assert "muted" in emote_result["error"].lower()

    @pytest.mark.asyncio
    @patch("server.game.chat_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_manual_unmute_after_permanent_mute(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test manual unmute after permanent mute."""
        # Setup mocks
        mock_nats_service.is_connected.return_value = True
        mock_nats_service.publish = MagicMock(return_value=True)
        # Make it async

        async def mock_publish(*args, **kwargs):
            return True

        mock_nats_service.publish = mock_publish
        mock_rate_limiter.check_rate_limit.return_value = True
        mock_user_manager.is_channel_muted.return_value = False
        mock_user_manager.is_globally_muted.return_value = False
        mock_user_manager.can_send_message.return_value = True
        mock_user_manager.load_player_mutes.return_value = True
        mock_user_manager.is_player_muted.return_value = False
        mock_user_manager.is_player_muted_by_others.return_value = False
        mock_user_manager.mute_player.return_value = True
        mock_user_manager.mute_global.return_value = True
        mock_user_manager.unmute_player.return_value = True
        mock_user_manager.is_admin.return_value = True

        # Create chat service with mocked user manager
        chat_service = ChatService(
            persistence=self.mock_persistence,
            room_service=self.mock_room_service,
            player_service=self.mock_player_service,
            user_manager_instance=mock_user_manager,
        )

        # Replace services with mocks
        chat_service.nats_service = mock_nats_service
        chat_service.rate_limiter = mock_rate_limiter

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Apply permanent mute
        mute_result = chat_service.mute_player(muter_id=self.muter_id, target_player_name=self.target_name)
        assert mute_result is True

        # Test emote is blocked
        mock_user_manager.is_player_muted.return_value = True
        mock_user_manager.is_player_muted_by_others.return_value = True
        emote_result = await chat_service.send_emote_message(self.target_id, "waves")
        assert emote_result["success"] is False

        # Manually unmute the player
        unmute_result = chat_service.unmute_player(muter_id=self.muter_id, target_player_name=self.target_name)
        assert unmute_result is True

        # Test emote is now allowed
        mock_user_manager.is_player_muted.return_value = False
        mock_user_manager.is_player_muted_by_others.return_value = False
        emote_result = await chat_service.send_emote_message(self.target_id, "waves")
        assert emote_result["success"] is True
        assert emote_result["message"]["content"] == "waves"

    @pytest.mark.asyncio
    @patch("server.game.chat_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_temporary_vs_permanent_mute_consistency(
        self, mock_user_manager, mock_rate_limiter, mock_nats_service
    ):
        """Test that temporary and permanent mutes behave consistently for emote filtering."""
        # Create chat service with mocked user manager
        chat_service = self._create_chat_service_with_mocks(mock_user_manager, mock_rate_limiter, mock_nats_service)

        # Setup mocks
        mock_nats_service.is_connected.return_value = True
        mock_nats_service.publish = MagicMock(return_value=True)
        # Make it async

        async def mock_publish(*args, **kwargs):
            return True

        mock_nats_service.publish = mock_publish
        mock_rate_limiter.check_rate_limit.return_value = True
        mock_user_manager.is_channel_muted.return_value = False
        mock_user_manager.is_globally_muted.return_value = False
        mock_user_manager.can_send_message.return_value = True
        mock_user_manager.load_player_mutes.return_value = True
        mock_user_manager.is_player_muted.return_value = False
        mock_user_manager.is_player_muted_by_others.return_value = False

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Test temporary mute
        mute_result = chat_service.mute_player(muter_id=self.muter_id, target_player_name=self.target_name)
        assert mute_result is True

        # Test emote is blocked with temporary mute
        mock_user_manager.is_player_muted.return_value = True
        emote_result = await chat_service.send_emote_message(self.target_id, "waves")
        assert emote_result["success"] is False
        assert "muted" in emote_result["error"].lower()

        # Unmute and test permanent mute
        unmute_result = chat_service.unmute_player(muter_id=self.muter_id, target_player_name=self.target_name)
        assert unmute_result is True

        # Apply permanent mute
        mute_result = chat_service.mute_player(muter_id=self.muter_id, target_player_name=self.target_name)
        assert mute_result is True

        # Test emote is blocked with permanent mute (same behavior)
        mock_user_manager.is_player_muted.return_value = True
        emote_result = await chat_service.send_emote_message(self.target_id, "waves")
        assert emote_result["success"] is False
        assert "muted" in emote_result["error"].lower()

    @pytest.mark.asyncio
    @patch("server.game.chat_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_global_temporary_vs_permanent_mute(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test global temporary vs permanent mutes with emotes."""
        # Create chat service with mocked user manager
        chat_service = self._create_chat_service_with_mocks(mock_user_manager, mock_rate_limiter, mock_nats_service)

        # Setup mocks
        mock_nats_service.is_connected.return_value = True
        mock_nats_service.publish = MagicMock(return_value=True)
        # Make it async

        async def mock_publish(*args, **kwargs):
            return True

        mock_nats_service.publish = mock_publish
        mock_rate_limiter.check_rate_limit.return_value = True
        mock_user_manager.is_channel_muted.return_value = False
        mock_user_manager.is_globally_muted.return_value = False
        mock_user_manager.can_send_message.return_value = True
        mock_user_manager.load_player_mutes.return_value = True
        mock_user_manager.is_player_muted.return_value = False
        mock_user_manager.is_player_muted_by_others.return_value = False

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Test global temporary mute
        global_mute_result = chat_service.mute_global(
            muter_id=self.muter_id,
            target_player_name=self.target_name,
            duration_minutes=30,
            reason="Temporary global mute test",
        )
        assert global_mute_result is True

        # Test emote is blocked with global temporary mute
        mock_user_manager.is_globally_muted.return_value = True
        emote_result = await chat_service.send_emote_message(self.target_id, "waves")
        assert emote_result["success"] is False
        assert "globally muted" in emote_result["error"].lower()

        # Simulate global mute expiration
        mock_user_manager.is_globally_muted.return_value = False

        # Test emote is allowed after global mute expiration
        emote_result = await chat_service.send_emote_message(self.target_id, "waves")
        assert emote_result["success"] is True

        # Test global permanent mute (no duration)
        global_mute_result = chat_service.mute_global(
            muter_id=self.muter_id,
            target_player_name=self.target_name,
            duration_minutes=None,
            reason="Permanent global mute test",
        )
        assert global_mute_result is True

        # Test emote is blocked with global permanent mute
        mock_user_manager.is_globally_muted.return_value = True
        emote_result = await chat_service.send_emote_message(self.target_id, "waves")
        assert emote_result["success"] is False
        assert "globally muted" in emote_result["error"].lower()

    @pytest.mark.asyncio
    @patch("server.game.chat_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_mute_duration_edge_cases(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test edge cases for mute durations."""
        # Create chat service with mocked user manager
        chat_service = self._create_chat_service_with_mocks(mock_user_manager, mock_rate_limiter, mock_nats_service)

        # Setup mocks
        mock_nats_service.is_connected.return_value = True
        mock_nats_service.publish = MagicMock(return_value=True)
        # Make it async

        async def mock_publish(*args, **kwargs):
            return True

        mock_nats_service.publish = mock_publish
        mock_rate_limiter.check_rate_limit.return_value = True
        mock_user_manager.is_channel_muted.return_value = False
        mock_user_manager.is_globally_muted.return_value = False
        mock_user_manager.can_send_message.return_value = True
        mock_user_manager.load_player_mutes.return_value = True
        mock_user_manager.is_player_muted.return_value = False
        mock_user_manager.is_player_muted_by_others.return_value = False

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Test very short duration (1 minute)
        global_mute_result = chat_service.mute_global(
            muter_id=self.muter_id,
            target_player_name=self.target_name,
            duration_minutes=1,
            reason="Very short mute test",
        )
        assert global_mute_result is True

        # Test emote is blocked
        mock_user_manager.is_globally_muted.return_value = True
        emote_result = await chat_service.send_emote_message(self.target_id, "waves")
        assert emote_result["success"] is False

        # Test very long duration (1 week)
        global_mute_result = chat_service.mute_global(
            muter_id=self.muter_id,
            target_player_name=self.target_name,
            duration_minutes=10080,  # 1 week
            reason="Very long mute test",
        )
        assert global_mute_result is True

        # Test emote is blocked
        emote_result = await chat_service.send_emote_message(self.target_id, "waves")
        assert emote_result["success"] is False

    @pytest.mark.asyncio
    @patch("server.game.chat_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_mute_type_priority_with_emotes(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test priority between different mute types with emotes."""
        # Create chat service with mocked user manager
        chat_service = self._create_chat_service_with_mocks(mock_user_manager, mock_rate_limiter, mock_nats_service)

        # Setup mocks
        mock_nats_service.is_connected.return_value = True
        mock_nats_service.publish = MagicMock(return_value=True)
        # Make it async

        async def mock_publish(*args, **kwargs):
            return True

        mock_nats_service.publish = mock_publish
        mock_rate_limiter.check_rate_limit.return_value = True
        mock_user_manager.is_channel_muted.return_value = False
        mock_user_manager.is_globally_muted.return_value = False
        mock_user_manager.can_send_message.return_value = True
        mock_user_manager.load_player_mutes.return_value = True
        mock_user_manager.is_player_muted.return_value = False
        mock_user_manager.is_player_muted_by_others.return_value = False

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Apply personal mute
        personal_mute_result = chat_service.mute_player(muter_id=self.muter_id, target_player_name=self.target_name)
        assert personal_mute_result is True

        # Apply global mute (should take priority)
        global_mute_result = chat_service.mute_global(
            muter_id=self.muter_id,
            target_player_name=self.target_name,
            duration_minutes=60,
            reason="Global mute priority test",
        )
        assert global_mute_result is True

        # Test emote is blocked by global mute (higher priority)
        mock_user_manager.is_globally_muted.return_value = True
        mock_user_manager.is_player_muted.return_value = True
        emote_result = await chat_service.send_emote_message(self.target_id, "waves")
        assert emote_result["success"] is False
        assert "globally muted" in emote_result["error"].lower()

        # Remove global mute, test personal mute still active
        mock_user_manager.is_globally_muted.return_value = False
        emote_result = await chat_service.send_emote_message(self.target_id, "waves")
        assert emote_result["success"] is False
        assert "muted" in emote_result["error"].lower()

    @pytest.mark.asyncio
    @patch("server.game.chat_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_mute_expiration_timing_with_emotes(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test mute expiration timing with emotes."""
        # Create chat service with mocked user manager
        chat_service = self._create_chat_service_with_mocks(mock_user_manager, mock_rate_limiter, mock_nats_service)

        # Setup mocks
        mock_nats_service.is_connected.return_value = True
        mock_nats_service.publish = MagicMock(return_value=True)
        # Make it async

        async def mock_publish(*args, **kwargs):
            return True

        mock_nats_service.publish = mock_publish
        mock_rate_limiter.check_rate_limit.return_value = True
        mock_user_manager.is_channel_muted.return_value = False
        mock_user_manager.is_globally_muted.return_value = False
        mock_user_manager.can_send_message.return_value = True
        mock_user_manager.load_player_mutes.return_value = True
        mock_user_manager.is_player_muted.return_value = False
        mock_user_manager.is_player_muted_by_others.return_value = False

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Apply temporary mute
        global_mute_result = chat_service.mute_global(
            muter_id=self.muter_id, target_player_name=self.target_name, duration_minutes=5, reason="Timing test"
        )
        assert global_mute_result is True

        # Test emote is blocked initially
        mock_user_manager.is_globally_muted.return_value = True
        emote_result = await chat_service.send_emote_message(self.target_id, "waves")
        assert emote_result["success"] is False

        # Simulate time passing but mute still active
        emote_result = await chat_service.send_emote_message(self.target_id, "dances")
        assert emote_result["success"] is False

        # Simulate mute expiration
        mock_user_manager.is_globally_muted.return_value = False

        # Test emote is now allowed
        emote_result = await chat_service.send_emote_message(self.target_id, "waves")
        assert emote_result["success"] is True
        assert emote_result["message"]["content"] == "waves"
