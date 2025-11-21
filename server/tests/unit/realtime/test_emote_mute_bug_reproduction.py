"""
Unit test to reproduce the emote mute filtering bug.

This test reproduces the bug where muted players' emotes are not properly
filtered during broadcasting. The test uses real UserManager instances to
catch actual implementation bugs rather than just testing mocked behavior.
"""

import uuid
from datetime import UTC, datetime
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import AsyncMock, Mock, patch

import pytest

from server.realtime.nats_message_handler import NATSMessageHandler
from server.services.user_manager import UserManager


class TestEmoteMuteBugReproduction:
    """Test to reproduce the emote mute filtering bug."""

    def setup_method(self):
        """Set up test fixtures with real UserManager instance."""
        # Create temporary directory for mute files
        self.temp_dir = TemporaryDirectory()
        self.data_dir = Path(self.temp_dir.name)

        # Create real UserManager instance (not mocked)
        # Use cache_ttl=0 to force reload from disk each time (simulating real server behavior)
        self.user_manager = UserManager(data_dir=self.data_dir, mute_cache_ttl=0)

        # Create test player IDs
        self.muter_id = uuid.uuid4()
        self.muter_name = "ArkanWolfshade"
        self.muted_id = uuid.uuid4()
        self.muted_name = "Ithaqua"

        # Create mock NATS service
        self.mock_nats_service = Mock()
        self.mock_nats_service.is_connected.return_value = True

        # Create mock connection manager
        self.mock_connection_manager = Mock()
        self.room_id = "earth_arkhamcity_sanitarium_room_foyer_001"
        self.mock_connection_manager._canonical_room_id.return_value = self.room_id
        self.mock_connection_manager.room_subscriptions = {self.room_id: {str(self.muter_id), str(self.muted_id)}}
        self.mock_connection_manager.send_personal_message = AsyncMock()

        # Create NATS message handler
        self.nats_handler = NATSMessageHandler(
            nats_service=self.mock_nats_service, connection_manager=self.mock_connection_manager
        )

        # Inject real UserManager into handler
        self.nats_handler._get_user_manager = lambda: self.user_manager

    def teardown_method(self):
        """Clean up temporary directory."""
        self.temp_dir.cleanup()

    @pytest.mark.asyncio
    async def test_emote_mute_filtering_bug_reproduction(self):
        """
        Reproduce the bug: muted player's emote should be filtered but isn't.

        This test reproduces the exact scenario from the bug report:
        1. ArkanWolfshade mutes Ithaqua
        2. Ithaqua sends an emote
        3. ArkanWolfshade should NOT receive the emote (but currently does)
        """
        # Step 1: Mute Ithaqua (muted_id) by ArkanWolfshade (muter_id)
        mute_result = self.user_manager.mute_player(
            muter_id=str(self.muter_id),
            muter_name=self.muter_name,
            target_id=str(self.muted_id),
            target_name=self.muted_name,
            duration_minutes=None,  # Permanent mute
        )
        assert mute_result is True, "Mute command should succeed"

        # Verify mute was stored in memory
        mute_check = self.user_manager.is_player_muted(str(self.muter_id), str(self.muted_id))
        assert mute_check is True, "Mute should be stored and retrievable"

        # CRITICAL: Simulate real server behavior - clear in-memory cache to force reload from disk
        # This simulates the scenario where mute is saved to disk, but when checking,
        # the UserManager might have stale cache or need to reload from disk
        self.user_manager._player_mutes.clear()
        self.user_manager._mute_cache.clear()

        # Verify mute can still be loaded from disk
        mute_check_after_clear = self.user_manager.is_player_muted(str(self.muter_id), str(self.muted_id))
        assert mute_check_after_clear is True, "Mute should be loadable from disk after clearing cache"

        # Step 2: Create emote chat event (as if sent by Ithaqua)
        chat_event = {
            "type": "chat_message",
            "data": {
                "id": str(uuid.uuid4()),
                "sender_id": str(self.muted_id),
                "sender_name": self.muted_name,
                "channel": "emote",
                "content": "dances like no one is watching",
                "timestamp": datetime.now(UTC).isoformat(),
            },
        }

        # Step 3: Mock player in room check
        with patch.object(self.nats_handler, "_is_player_in_room", return_value=True):
            # Step 4: Broadcast emote message
            await self.nats_handler._broadcast_to_room_with_filtering(
                self.room_id, chat_event, str(self.muted_id), "emote"
            )

        # Step 5: Verify ArkanWolfshade (muter) did NOT receive the emote
        # The bug is that send_personal_message is called for muter_id when it shouldn't be
        calls = self.mock_connection_manager.send_personal_message.call_args_list

        # Extract player IDs from calls
        called_player_ids = {str(call[0][0]) for call in calls}

        # ArkanWolfshade (muter_id) should NOT be in the called list
        assert str(self.muter_id) not in called_player_ids, (
            f"BUG REPRODUCED: ArkanWolfshade (muter) received emote from muted player Ithaqua. "
            f"Calls made to: {called_player_ids}"
        )

        # Ithaqua (muted_id) should receive their own echo
        assert str(self.muted_id) in called_player_ids, "Sender should receive echo of their own emote"

    @pytest.mark.asyncio
    async def test_emote_mute_filtering_works_when_unmuted(self):
        """
        Verify that emotes work correctly when player is NOT muted.

        This is the positive test case to ensure the filtering logic works
        when there's no mute in place.
        """
        # Do NOT mute Ithaqua

        # Create emote chat event
        chat_event = {
            "type": "chat_message",
            "data": {
                "id": str(uuid.uuid4()),
                "sender_id": str(self.muted_id),
                "sender_name": self.muted_name,
                "channel": "emote",
                "content": "dances like no one is watching",
                "timestamp": datetime.now(UTC).isoformat(),
            },
        }

        # Mock player in room check
        with patch.object(self.nats_handler, "_is_player_in_room", return_value=True):
            # Broadcast emote message
            await self.nats_handler._broadcast_to_room_with_filtering(
                self.room_id, chat_event, str(self.muted_id), "emote"
            )

        # Verify ArkanWolfshade (muter) DID receive the emote (not muted)
        calls = self.mock_connection_manager.send_personal_message.call_args_list
        called_player_ids = {str(call[0][0]) for call in calls}

        assert str(self.muter_id) in called_player_ids, "Unmuted player should receive emote"
        assert str(self.muted_id) in called_player_ids, "Sender should receive echo"

    @pytest.mark.asyncio
    async def test_emote_mute_filtering_after_unmute(self):
        """
        Verify that emotes work correctly after unmuting.

        This tests the unmute workflow:
        1. Mute player
        2. Emote is blocked
        3. Unmute player
        4. Emote is allowed
        """
        # Step 1: Mute Ithaqua
        self.user_manager.mute_player(
            muter_id=str(self.muter_id),
            muter_name=self.muter_name,
            target_id=str(self.muted_id),
            target_name=self.muted_name,
        )

        # Step 2: Send emote while muted (should be blocked)
        chat_event = {
            "type": "chat_message",
            "data": {
                "id": str(uuid.uuid4()),
                "sender_id": str(self.muted_id),
                "sender_name": self.muted_name,
                "channel": "emote",
                "content": "dances",
                "timestamp": datetime.now(UTC).isoformat(),
            },
        }

        with patch.object(self.nats_handler, "_is_player_in_room", return_value=True):
            await self.nats_handler._broadcast_to_room_with_filtering(
                self.room_id, chat_event, str(self.muted_id), "emote"
            )

        # Verify muter did NOT receive emote
        self.mock_connection_manager.send_personal_message.reset_mock()
        calls = self.mock_connection_manager.send_personal_message.call_args_list
        called_player_ids = {str(call[0][0]) for call in calls}
        assert str(self.muter_id) not in called_player_ids, "Muted player's emote should be blocked"

        # Step 3: Unmute Ithaqua
        unmute_result = self.user_manager.unmute_player(
            unmuter_id=str(self.muter_id),
            unmuter_name=self.muter_name,
            target_id=str(self.muted_id),
            target_name=self.muted_name,
        )
        assert unmute_result is True, "Unmute should succeed"

        # Step 4: Send emote after unmute (should be allowed)
        chat_event2 = {
            "type": "chat_message",
            "data": {
                "id": str(uuid.uuid4()),
                "sender_id": str(self.muted_id),
                "sender_name": self.muted_name,
                "channel": "emote",
                "content": "dances again",
                "timestamp": datetime.now(UTC).isoformat(),
            },
        }

        with patch.object(self.nats_handler, "_is_player_in_room", return_value=True):
            await self.nats_handler._broadcast_to_room_with_filtering(
                self.room_id, chat_event2, str(self.muted_id), "emote"
            )

        # Verify muter DID receive emote after unmute
        calls = self.mock_connection_manager.send_personal_message.call_args_list
        called_player_ids = {str(call[0][0]) for call in calls}
        assert str(self.muter_id) in called_player_ids, "Unmuted player's emote should be visible"
