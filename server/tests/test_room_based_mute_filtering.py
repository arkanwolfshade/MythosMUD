"""
Tests for mute filtering across all room-based message types.

This module tests that mute filtering works consistently across all room-based
channels: say, local, emote, and pose. It verifies that the fix implemented
in _broadcast_to_room_with_filtering() applies to all room-based message types.
"""

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.nats_message_handler import NATSMessageHandler
from server.services.nats_service import NATSService


class TestRoomBasedMuteFiltering:
    """Test mute filtering across all room-based message types."""

    def setup_method(self):
        """Set up test fixtures."""
        self.mock_nats_service = MagicMock(spec=NATSService)
        self.handler = NATSMessageHandler(self.mock_nats_service)

        # Test data
        self.room_id = "earth_arkhamcity_sanitarium_room_hallway_001"
        self.sender_id = str(uuid.uuid4())
        self.receiver_id = str(uuid.uuid4())
        self.sender_name = "Ithaqua"
        self.receiver_name = "ArkanWolfshade"

    def create_chat_event(self, channel: str, content: str) -> dict:
        """Create a chat event for testing."""
        return {
            "type": "chat_message",
            "data": {
                "id": str(uuid.uuid4()),
                "sender_id": self.sender_id,
                "sender_name": self.sender_name,
                "channel": channel,
                "content": content,
                "timestamp": datetime.now(UTC).isoformat(),
            },
        }

    @pytest.mark.asyncio
    async def test_say_message_mute_filtering(self):
        """Test that say messages are properly filtered when sender is muted."""
        chat_event = self.create_chat_event("say", "Hello everyone!")

        with patch("server.realtime.nats_message_handler.connection_manager") as mock_conn_mgr:
            # Mock room subscriptions
            mock_conn_mgr.room_subscriptions = {self.room_id: {self.sender_id, self.receiver_id}}
            mock_conn_mgr._canonical_room_id.return_value = self.room_id
            mock_conn_mgr.send_personal_message = AsyncMock()

            # Mock player in room check
            with patch.object(self.handler, "_is_player_in_room", return_value=True):
                # Mock mute check - receiver has muted sender
                with patch.object(self.handler, "_is_player_muted_by_receiver_with_user_manager", return_value=True):
                    # Execute
                    await self.handler._broadcast_to_room_with_filtering(
                        self.room_id, chat_event, self.sender_id, "say"
                    )

                    # Verify that the muted receiver did not receive the message
                    mock_conn_mgr.send_personal_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_local_message_mute_filtering(self):
        """Test that local messages are properly filtered when sender is muted."""
        chat_event = self.create_chat_event("local", "Anyone in the area?")

        with patch("server.realtime.nats_message_handler.connection_manager") as mock_conn_mgr:
            # Mock room subscriptions
            mock_conn_mgr.room_subscriptions = {self.room_id: {self.sender_id, self.receiver_id}}
            mock_conn_mgr._canonical_room_id.return_value = self.room_id
            mock_conn_mgr.send_personal_message = AsyncMock()

            # Mock player in room check
            with patch.object(self.handler, "_is_player_in_room", return_value=True):
                # Mock mute check - receiver has muted sender
                with patch.object(self.handler, "_is_player_muted_by_receiver_with_user_manager", return_value=True):
                    # Execute
                    await self.handler._broadcast_to_room_with_filtering(
                        self.room_id, chat_event, self.sender_id, "local"
                    )

                    # Verify that the muted receiver did not receive the message
                    mock_conn_mgr.send_personal_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_emote_message_mute_filtering(self):
        """Test that emote messages are properly filtered when sender is muted."""
        chat_event = self.create_chat_event("emote", "dance")

        with patch("server.realtime.nats_message_handler.connection_manager") as mock_conn_mgr:
            # Mock room subscriptions
            mock_conn_mgr.room_subscriptions = {self.room_id: {self.sender_id, self.receiver_id}}
            mock_conn_mgr._canonical_room_id.return_value = self.room_id
            mock_conn_mgr.send_personal_message = AsyncMock()

            # Mock player in room check
            with patch.object(self.handler, "_is_player_in_room", return_value=True):
                # Mock mute check - receiver has muted sender
                with patch.object(self.handler, "_is_player_muted_by_receiver_with_user_manager", return_value=True):
                    # Execute
                    await self.handler._broadcast_to_room_with_filtering(
                        self.room_id, chat_event, self.sender_id, "emote"
                    )

                    # Verify that the muted receiver did not receive the message
                    mock_conn_mgr.send_personal_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_pose_message_mute_filtering(self):
        """Test that pose messages are properly filtered when sender is muted."""
        chat_event = self.create_chat_event("pose", "looks around nervously")

        with patch("server.realtime.nats_message_handler.connection_manager") as mock_conn_mgr:
            # Mock room subscriptions
            mock_conn_mgr.room_subscriptions = {self.room_id: {self.sender_id, self.receiver_id}}
            mock_conn_mgr._canonical_room_id.return_value = self.room_id
            mock_conn_mgr.send_personal_message = AsyncMock()

            # Mock player in room check
            with patch.object(self.handler, "_is_player_in_room", return_value=True):
                # Mock mute check - receiver has muted sender
                with patch.object(self.handler, "_is_player_muted_by_receiver_with_user_manager", return_value=True):
                    # Execute
                    await self.handler._broadcast_to_room_with_filtering(
                        self.room_id, chat_event, self.sender_id, "pose"
                    )

                    # Verify that the muted receiver did not receive the message
                    mock_conn_mgr.send_personal_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_all_room_based_channels_allow_unmuted_messages(self):
        """Test that all room-based channels allow messages when sender is not muted."""
        channels = ["say", "local", "emote", "pose"]
        contents = ["Hello!", "Anyone here?", "waves", "smiles"]

        for channel, content in zip(channels, contents, strict=False):
            chat_event = self.create_chat_event(channel, content)

            with patch("server.realtime.nats_message_handler.connection_manager") as mock_conn_mgr:
                # Mock room subscriptions
                mock_conn_mgr.room_subscriptions = {self.room_id: {self.sender_id, self.receiver_id}}
                mock_conn_mgr._canonical_room_id.return_value = self.room_id
                mock_conn_mgr.send_personal_message = AsyncMock()

                # Mock player in room check
                with patch.object(self.handler, "_is_player_in_room", return_value=True):
                    # Mock mute check - receiver has NOT muted sender
                    with patch.object(
                        self.handler, "_is_player_muted_by_receiver_with_user_manager", return_value=False
                    ):
                        # Execute
                        await self.handler._broadcast_to_room_with_filtering(
                            self.room_id, chat_event, self.sender_id, channel
                        )

                        # Verify that the receiver received the message
                        mock_conn_mgr.send_personal_message.assert_called_once_with(self.receiver_id, chat_event)

                        # Reset mock for next iteration
                        mock_conn_mgr.reset_mock()

    @pytest.mark.asyncio
    async def test_room_based_channels_use_same_filtering_logic(self):
        """Test that all room-based channels use the same filtering logic."""
        channels = ["say", "local", "emote", "pose"]

        with patch("server.realtime.nats_message_handler.connection_manager") as mock_conn_mgr:
            # Mock room subscriptions
            mock_conn_mgr.room_subscriptions = {self.room_id: {self.sender_id, self.receiver_id}}
            mock_conn_mgr._canonical_room_id.return_value = self.room_id
            mock_conn_mgr.send_personal_message = AsyncMock()

            # Mock player in room check
            with patch.object(self.handler, "_is_player_in_room", return_value=True):
                # Mock mute check - receiver has muted sender
                with patch.object(
                    self.handler, "_is_player_muted_by_receiver_with_user_manager", return_value=True
                ) as mock_mute_check:
                    for channel in channels:
                        chat_event = self.create_chat_event(channel, f"Test {channel} message")

                        # Execute
                        await self.handler._broadcast_to_room_with_filtering(
                            self.room_id, chat_event, self.sender_id, channel
                        )

                        # Verify that mute check was called for each channel
                        assert mock_mute_check.called

                        # Reset mock for next iteration
                        mock_mute_check.reset_mock()

    @pytest.mark.asyncio
    async def test_room_based_channels_handle_multiple_receivers(self):
        """Test that room-based channels handle multiple receivers correctly."""
        receiver_ids = [str(uuid.uuid4()) for _ in range(3)]
        all_player_ids = [self.sender_id] + receiver_ids

        chat_event = self.create_chat_event("say", "Hello everyone!")

        with patch("server.realtime.nats_message_handler.connection_manager") as mock_conn_mgr:
            # Mock room subscriptions with multiple receivers
            mock_conn_mgr.room_subscriptions = {self.room_id: set(all_player_ids)}
            mock_conn_mgr._canonical_room_id.return_value = self.room_id
            mock_conn_mgr.send_personal_message = AsyncMock()

            # Mock player in room check
            with patch.object(self.handler, "_is_player_in_room", return_value=True):
                # Mock mute check - first receiver muted sender, others didn't
                def mock_mute_check(user_manager, receiver_id, sender_id):
                    return receiver_id == receiver_ids[0]  # Only first receiver muted sender

                with patch.object(
                    self.handler, "_is_player_muted_by_receiver_with_user_manager", side_effect=mock_mute_check
                ):
                    # Execute
                    await self.handler._broadcast_to_room_with_filtering(
                        self.room_id, chat_event, self.sender_id, "say"
                    )

                    # Verify that only non-muted receivers got the message
                    expected_calls = [((receiver_id, chat_event),) for receiver_id in receiver_ids[1:]]
                    mock_conn_mgr.send_personal_message.assert_has_calls(expected_calls, any_order=True)

                    # Verify muted receiver didn't get the message
                    muted_calls = [
                        call
                        for call in mock_conn_mgr.send_personal_message.call_args_list
                        if call[0][0] == receiver_ids[0]
                    ]
                    assert len(muted_calls) == 0

    @pytest.mark.asyncio
    async def test_room_based_channels_handle_sender_not_receiving_own_message(self):
        """Test that room-based channels exclude sender from receiving their own message."""
        chat_event = self.create_chat_event("say", "Hello everyone!")

        with patch("server.realtime.nats_message_handler.connection_manager") as mock_conn_mgr:
            # Mock room subscriptions
            mock_conn_mgr.room_subscriptions = {self.room_id: {self.sender_id, self.receiver_id}}
            mock_conn_mgr._canonical_room_id.return_value = self.room_id
            mock_conn_mgr.send_personal_message = AsyncMock()

            # Mock player in room check
            with patch.object(self.handler, "_is_player_in_room", return_value=True):
                # Mock mute check - receiver has muted sender
                with patch.object(self.handler, "_is_player_muted_by_receiver_with_user_manager", return_value=True):
                    # Execute
                    await self.handler._broadcast_to_room_with_filtering(
                        self.room_id, chat_event, self.sender_id, "say"
                    )

                    # Verify that sender did NOT receive their own message (sender is excluded)
                    mock_conn_mgr.send_personal_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_room_based_channels_handle_players_not_in_room(self):
        """Test that room-based channels filter out players not in the room."""
        chat_event = self.create_chat_event("say", "Hello everyone!")

        with patch("server.realtime.nats_message_handler.connection_manager") as mock_conn_mgr:
            # Mock room subscriptions
            mock_conn_mgr.room_subscriptions = {self.room_id: {self.sender_id, self.receiver_id}}
            mock_conn_mgr._canonical_room_id.return_value = self.room_id
            mock_conn_mgr.send_personal_message = AsyncMock()

            # Mock player in room check - receiver is not in room
            with patch.object(self.handler, "_is_player_in_room", return_value=False):
                # Mock mute check - receiver has NOT muted sender
                with patch.object(self.handler, "_is_player_muted_by_receiver_with_user_manager", return_value=False):
                    # Execute
                    await self.handler._broadcast_to_room_with_filtering(
                        self.room_id, chat_event, self.sender_id, "say"
                    )

                    # Verify that no one received the message (sender excluded, receiver not in room)
                    mock_conn_mgr.send_personal_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_room_based_channels_performance_with_optimized_user_manager(self):
        """Test that room-based channels use optimized UserManager instance management."""
        chat_event = self.create_chat_event("say", "Hello everyone!")

        with patch("server.realtime.nats_message_handler.connection_manager") as mock_conn_mgr:
            # Mock room subscriptions
            mock_conn_mgr.room_subscriptions = {self.room_id: {self.sender_id, self.receiver_id}}
            mock_conn_mgr._canonical_room_id.return_value = self.room_id
            mock_conn_mgr.send_personal_message = AsyncMock()

            # Mock player in room check
            with patch.object(self.handler, "_is_player_in_room", return_value=True):
                # Mock mute check
                with patch.object(self.handler, "_is_player_muted_by_receiver_with_user_manager", return_value=False):
                    # Mock the global user_manager instance
                    with patch("server.services.user_manager.user_manager") as mock_user_manager:
                        # Execute
                        await self.handler._broadcast_to_room_with_filtering(
                            self.room_id, chat_event, self.sender_id, "say"
                        )

                        # Verify that mute data was pre-loaded for the receiver
                        mock_user_manager.load_player_mutes.assert_called_with(self.receiver_id)
