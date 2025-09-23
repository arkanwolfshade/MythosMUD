"""
Integration tests for the complete mute/unmute workflow with emotes.

This module tests the end-to-end workflow of muting and unmuting players
and how it affects emote message filtering. It covers both custom and
predefined emotes, temporary and permanent mutes, and the complete
mute/unmute cycle.
"""

import uuid
from unittest.mock import MagicMock, patch

import pytest

from server.game.chat_service import ChatService
from server.game.player_service import PlayerService


class TestMuteUnmuteWorkflowIntegration:
    """Integration tests for complete mute/unmute workflow with emotes."""

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
    async def test_complete_mute_unmute_workflow_custom_emote(
        self, mock_user_manager, mock_rate_limiter, mock_nats_service
    ):
        """Test complete workflow: mute player -> emote blocked -> unmute -> emote allowed."""
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
        mock_user_manager.unmute_player.return_value = True

        # Replace services in the existing chat service instance
        chat_service.nats_service = mock_nats_service
        chat_service.rate_limiter = mock_rate_limiter
        chat_service.user_manager = mock_user_manager

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Step 1: Apply global mute to the target player
        global_mute_result = chat_service.mute_global(
            muter_id=self.muter_id, target_player_name=self.target_name, duration_minutes=60, reason="Test mute"
        )
        assert global_mute_result is True

        # Step 2: Target player tries to send custom emote (should be blocked by global mute)
        mock_user_manager.is_globally_muted.return_value = True  # Player is globally muted
        emote_result = await chat_service.send_emote_message(self.target_id, "dance")
        assert emote_result["success"] is False
        assert "globally muted" in emote_result["error"].lower()

        # Step 3: Remove global mute
        mock_user_manager.is_globally_muted.return_value = False  # Global mute removed

        # Step 4: Target player tries to send custom emote again (should be allowed)
        emote_result = await chat_service.send_emote_message(self.target_id, "dance")
        assert emote_result["success"] is True
        assert emote_result["message"]["channel"] == "emote"
        assert emote_result["message"]["content"] == "dance"

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_complete_mute_unmute_workflow_predefined_emote(
        self, mock_user_manager, mock_rate_limiter, mock_nats_service
    ):
        """Test complete workflow: mute player -> predefined emote blocked -> unmute -> predefined emote allowed."""
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
        mock_user_manager.unmute_player.return_value = True

        # Replace services in the existing chat service instance
        chat_service.nats_service = mock_nats_service
        chat_service.rate_limiter = mock_rate_limiter
        chat_service.user_manager = mock_user_manager

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Mock EmoteService
        with patch("server.game.emote_service.EmoteService") as mock_emote_service_class:
            mock_emote_service = MagicMock()
            mock_emote_service_class.return_value = mock_emote_service
            mock_emote_service.is_emote_alias.return_value = True
            mock_emote_service.format_emote_messages.return_value = ("You twibble.", f"{self.target_name} twibbles.")

        # Step 1: Apply global mute to the target player
        global_mute_result = chat_service.mute_global(
            muter_id=self.muter_id, target_player_name=self.target_name, duration_minutes=60, reason="Test mute"
        )
        assert global_mute_result is True

        # Step 2: Target player tries to send predefined emote (should be blocked by global mute)
        mock_user_manager.is_globally_muted.return_value = True  # Player is globally muted
        emote_result = await chat_service.send_predefined_emote(self.target_id, "twibble")
        assert emote_result["success"] is False
        assert "globally muted" in emote_result["error"].lower()

        # Step 3: Remove global mute
        mock_user_manager.is_globally_muted.return_value = False  # Global mute removed

        # Step 4: Target player tries to send predefined emote again (should be allowed)
        emote_result = await chat_service.send_predefined_emote(self.target_id, "twibble")
        assert emote_result["success"] is True
        assert emote_result["message"]["channel"] == "emote"
        assert "twibbles" in emote_result["message"]["content"]

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_temporary_mute_expiration_workflow(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test workflow where temporary mute expires and emotes become allowed again."""
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

        # Replace services in the existing chat service instance
        chat_service.nats_service = mock_nats_service
        chat_service.rate_limiter = mock_rate_limiter
        chat_service.user_manager = mock_user_manager

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Step 1: Apply temporary global mute (5 minutes)
        global_mute_result = chat_service.mute_global(
            muter_id=self.muter_id,
            target_player_name=self.target_name,
            duration_minutes=5,
            reason="Test temporary mute",
        )
        assert global_mute_result is True

        # Step 2: Target player tries to send emote (should be blocked by global mute)
        mock_user_manager.is_globally_muted.return_value = True  # Player is globally muted
        emote_result = await chat_service.send_emote_message(self.target_id, "wave")
        assert emote_result["success"] is False
        assert "globally muted" in emote_result["error"].lower()

        # Step 3: Simulate mute expiration (mock the user manager to return False)
        mock_user_manager.is_globally_muted.return_value = False  # Global mute has expired

        # Step 4: Target player tries to send emote again (should be allowed)
        emote_result = await chat_service.send_emote_message(self.target_id, "wave")
        assert emote_result["success"] is True
        assert emote_result["message"]["content"] == "wave"

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_permanent_mute_workflow(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test workflow with permanent mute (no duration specified)."""
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
        mock_user_manager.unmute_player.return_value = True

        # Replace services in the existing chat service instance
        chat_service.nats_service = mock_nats_service
        chat_service.rate_limiter = mock_rate_limiter
        chat_service.user_manager = mock_user_manager

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Step 1: Apply permanent global mute (no duration)
        global_mute_result = chat_service.mute_global(
            muter_id=self.muter_id,
            target_player_name=self.target_name,
            duration_minutes=None,
            reason="Test permanent mute",
        )
        assert global_mute_result is True

        # Step 2: Target player tries to send emote (should be blocked by global mute)
        mock_user_manager.is_globally_muted.return_value = True  # Player is permanently globally muted
        emote_result = await chat_service.send_emote_message(self.target_id, "laugh")
        assert emote_result["success"] is False
        assert "globally muted" in emote_result["error"].lower()

        # Step 3: Target player tries again later (should still be blocked - permanent global mute)
        emote_result = await chat_service.send_emote_message(self.target_id, "cry")
        assert emote_result["success"] is False

        # Step 4: Remove global mute
        mock_user_manager.is_globally_muted.return_value = False  # Global mute removed

        # Step 5: Now emotes should be allowed
        emote_result = await chat_service.send_emote_message(self.target_id, "smile")
        assert emote_result["success"] is True

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_global_mute_workflow_with_emotes(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test workflow with global mute affecting emotes."""
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

        # Replace services in the existing chat service instance
        chat_service.nats_service = mock_nats_service
        chat_service.rate_limiter = mock_rate_limiter
        chat_service.user_manager = mock_user_manager

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Step 1: Apply global mute
        global_mute_result = chat_service.mute_global(
            muter_id=self.muter_id, target_player_name=self.target_name, duration_minutes=60, reason="Global mute test"
        )
        assert global_mute_result is True

        # Step 2: Target player tries to send emote (should be blocked by global mute)
        mock_user_manager.is_globally_muted.return_value = True  # Player is globally muted
        emote_result = await chat_service.send_emote_message(self.target_id, "dance")
        assert emote_result["success"] is False
        assert "globally muted" in emote_result["error"].lower()

        # Step 3: Global mute expires or is removed
        mock_user_manager.is_globally_muted.return_value = False  # Global mute removed

        # Step 4: Target player tries to send emote again (should be allowed)
        emote_result = await chat_service.send_emote_message(self.target_id, "dance")
        assert emote_result["success"] is True

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_mute_workflow_with_different_emote_types(
        self, mock_user_manager, mock_rate_limiter, mock_nats_service
    ):
        """Test mute workflow with both custom and predefined emotes."""
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
        mock_user_manager.unmute_player.return_value = True

        # Replace services in the existing chat service instance
        chat_service.nats_service = mock_nats_service
        chat_service.rate_limiter = mock_rate_limiter
        chat_service.user_manager = mock_user_manager

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Mock EmoteService for predefined emotes
        with patch("server.game.emote_service.EmoteService") as mock_emote_service_class:
            mock_emote_service = MagicMock()
            mock_emote_service_class.return_value = mock_emote_service
            mock_emote_service.is_emote_alias.return_value = True
            mock_emote_service.format_emote_messages.return_value = ("You dance.", f"{self.target_name} dances.")

            # Step 1: Apply global mute to the target player
            global_mute_result = chat_service.mute_global(
                muter_id=self.muter_id, target_player_name=self.target_name, duration_minutes=60, reason="Test mute"
            )
            assert global_mute_result is True

            # Step 2: Test custom emote is blocked by global mute
            mock_user_manager.is_globally_muted.return_value = True
            custom_emote_result = await chat_service.send_emote_message(self.target_id, "custom action")
            assert custom_emote_result["success"] is False
            assert "globally muted" in custom_emote_result["error"].lower()

            # Step 3: Test predefined emote is blocked by global mute
            predefined_emote_result = await chat_service.send_predefined_emote(self.target_id, "dance")
            assert predefined_emote_result["success"] is False
            assert "globally muted" in predefined_emote_result["error"].lower()

            # Step 4: Remove global mute
            mock_user_manager.is_globally_muted.return_value = False  # Global mute removed

            # Step 5: Test both emote types are now allowed

            custom_emote_result = await chat_service.send_emote_message(self.target_id, "custom action")
            assert custom_emote_result["success"] is True
            assert custom_emote_result["message"]["content"] == "custom action"

            predefined_emote_result = await chat_service.send_predefined_emote(self.target_id, "dance")
            assert predefined_emote_result["success"] is True
            assert "dances" in predefined_emote_result["message"]["content"]

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_mute_workflow_error_handling(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test error handling in mute/unmute workflow."""
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

        # Test 1: Mute non-existent player
        self.mock_player_service.resolve_player_name.return_value = None
        mute_result = chat_service.mute_player(muter_id=self.muter_id, target_player_name="NonExistentPlayer")
        assert mute_result is False

        # Test 2: Unmute non-existent player
        unmute_result = chat_service.unmute_player(muter_id=self.muter_id, target_player_name="NonExistentPlayer")
        assert unmute_result is False

        # Test 3: Emote from non-existent player
        self.mock_player_service.get_player_by_id.return_value = None
        emote_result = await chat_service.send_emote_message("non-existent-id", "wave")
        assert emote_result["success"] is False
        assert "not found" in emote_result["error"].lower()

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_mute_workflow_with_rate_limiting(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test that rate limiting works correctly with mute workflow."""
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

        # Replace services in the existing chat service instance
        chat_service.nats_service = mock_nats_service
        chat_service.rate_limiter = mock_rate_limiter
        chat_service.user_manager = mock_user_manager

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Step 1: Mute the target player
        mute_result = chat_service.mute_player(muter_id=self.muter_id, target_player_name=self.target_name)
        assert mute_result is True

        # Step 2: Simulate rate limiting (player not muted but rate limited)
        mock_user_manager.is_player_muted.return_value = False  # Not muted
        mock_rate_limiter.check_rate_limit.return_value = False  # Rate limited

        emote_result = await chat_service.send_emote_message(self.target_id, "wave")
        assert emote_result["success"] is False
        assert "rate limit" in emote_result["error"].lower()

        # Step 3: Rate limit expires
        mock_rate_limiter.check_rate_limit.return_value = True  # No longer rate limited

        emote_result = await chat_service.send_emote_message(self.target_id, "wave")
        assert emote_result["success"] is True
