"""
Tests for mute filtering across all room-based message types.

This module tests that mute filtering works consistently across all room-based
channels: say, local, emote, and pose. It verifies that the fix implemented
in _broadcast_to_room_with_filtering() applies to all room-based message types.
"""

import uuid
from datetime import UTC, datetime
from unittest.mock import ANY, AsyncMock, MagicMock, call, patch

import pytest

from server.realtime.nats_message_handler import NATSMessageHandler
from server.services.nats_service import NATSService


class TestRoomBasedMuteFiltering:
    """Test mute filtering across all room-based message types."""

    def setup_method(self) -> None:
        """Set up shared fixtures for each test."""
        self.mock_nats_service = MagicMock(spec=NATSService)
        self.room_id = "earth_arkhamcity_sanitarium_room_hallway_001"
        self.sender_id = str(uuid.uuid4())
        self.receiver_id = str(uuid.uuid4())
        self.sender_name = "Ithaqua"
        self.receiver_name = "ArkanWolfshade"

        self.mock_connection_manager = MagicMock()
        self.handler = NATSMessageHandler(
            self.mock_nats_service,
            connection_manager=self.mock_connection_manager,
        )

    def _prepare_connection_manager(self, subscribers: set[str] | None = None) -> None:
        """Configure connection manager mocks for a given subscriber set."""
        subscribers = subscribers or {self.sender_id, self.receiver_id}
        self.mock_connection_manager._canonical_room_id = MagicMock(return_value=self.room_id)
        self.mock_connection_manager.room_subscriptions = {self.room_id: set(subscribers)}
        self.mock_connection_manager.send_personal_message = AsyncMock()

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
    async def test_say_message_mute_filtering(self) -> None:
        """Test that say messages are properly filtered when sender is muted."""
        chat_event = self.create_chat_event("say", "Hello everyone!")
        self._prepare_connection_manager()

        with (
            patch.object(self.handler, "_is_player_in_room", return_value=True),
            patch.object(self.handler, "_is_player_muted_by_receiver_with_user_manager", return_value=True),
        ):
            await self.handler._broadcast_to_room_with_filtering(self.room_id, chat_event, self.sender_id, "say")

        self.mock_connection_manager.send_personal_message.assert_called_once_with(self.sender_id, chat_event)

    @pytest.mark.asyncio
    async def test_local_message_mute_filtering(self) -> None:
        """Test that local messages are properly filtered when sender is muted."""
        chat_event = self.create_chat_event("local", "Anyone in the area?")
        self._prepare_connection_manager()

        with (
            patch.object(self.handler, "_is_player_in_room", return_value=True),
            patch.object(self.handler, "_is_player_muted_by_receiver_with_user_manager", return_value=True),
        ):
            await self.handler._broadcast_to_room_with_filtering(self.room_id, chat_event, self.sender_id, "local")

        self.mock_connection_manager.send_personal_message.assert_called_once_with(self.sender_id, chat_event)

    @pytest.mark.asyncio
    async def test_emote_message_mute_filtering(self) -> None:
        """Test that emote messages are properly filtered when sender is muted."""
        chat_event = self.create_chat_event("emote", "dance")
        self._prepare_connection_manager()

        with (
            patch.object(self.handler, "_is_player_in_room", return_value=True),
            patch.object(self.handler, "_is_player_muted_by_receiver_with_user_manager", return_value=True),
        ):
            await self.handler._broadcast_to_room_with_filtering(self.room_id, chat_event, self.sender_id, "emote")

        self.mock_connection_manager.send_personal_message.assert_called_once_with(self.sender_id, chat_event)

    @pytest.mark.asyncio
    async def test_pose_message_mute_filtering(self) -> None:
        """Test that pose messages are properly filtered when sender is muted."""
        chat_event = self.create_chat_event("pose", "looks around nervously")
        self._prepare_connection_manager()

        with (
            patch.object(self.handler, "_is_player_in_room", return_value=True),
            patch.object(self.handler, "_is_player_muted_by_receiver_with_user_manager", return_value=True),
        ):
            await self.handler._broadcast_to_room_with_filtering(self.room_id, chat_event, self.sender_id, "pose")

        self.mock_connection_manager.send_personal_message.assert_called_once_with(self.sender_id, chat_event)

    @pytest.mark.asyncio
    async def test_all_room_based_channels_allow_unmuted_messages(self) -> None:
        """Test that all room-based channels allow messages when sender is not muted."""
        channels = ["say", "local", "emote", "pose"]
        contents = ["Hello!", "Anyone here?", "waves", "smiles"]

        for channel, content in zip(channels, contents, strict=False):
            chat_event = self.create_chat_event(channel, content)
            self._prepare_connection_manager()

            with (
                patch.object(self.handler, "_is_player_in_room", return_value=True),
                patch.object(self.handler, "_is_player_muted_by_receiver_with_user_manager", return_value=False),
            ):
                await self.handler._broadcast_to_room_with_filtering(self.room_id, chat_event, self.sender_id, channel)

            expected_calls = [
                call(self.receiver_id, chat_event),
                call(self.sender_id, chat_event),
            ]
            self.mock_connection_manager.send_personal_message.assert_has_calls(expected_calls, any_order=True)
            self.mock_connection_manager.send_personal_message.reset_mock()

    @pytest.mark.asyncio
    async def test_room_based_channels_use_same_filtering_logic(self) -> None:
        """Test that all room-based channels use the same filtering logic."""
        channels = ["say", "local", "emote", "pose"]
        self._prepare_connection_manager()

        with (
            patch.object(self.handler, "_is_player_in_room", return_value=True),
            patch.object(
                self.handler, "_is_player_muted_by_receiver_with_user_manager", return_value=True
            ) as mock_mute_check,
        ):
            for channel in channels:
                chat_event = self.create_chat_event(channel, f"Test {channel} message")
                await self.handler._broadcast_to_room_with_filtering(self.room_id, chat_event, self.sender_id, channel)
                mock_mute_check.assert_called_with(ANY, self.receiver_id, self.sender_id)
                mock_mute_check.reset_mock()

    @pytest.mark.asyncio
    async def test_room_based_channels_handle_multiple_receivers(self) -> None:
        """Test that room-based channels handle multiple receivers correctly."""
        receiver_ids = [str(uuid.uuid4()) for _ in range(3)]
        all_player_ids = {self.sender_id, *receiver_ids}
        chat_event = self.create_chat_event("say", "Hello everyone!")

        self._prepare_connection_manager(all_player_ids)

        def mute_check(_, receiver_id, sender_id):
            del sender_id
            return receiver_id == receiver_ids[0]

        with (
            patch.object(self.handler, "_is_player_in_room", return_value=True),
            patch.object(self.handler, "_is_player_muted_by_receiver_with_user_manager", side_effect=mute_check),
        ):
            await self.handler._broadcast_to_room_with_filtering(self.room_id, chat_event, self.sender_id, "say")

        expected_calls = [call(receiver_id, chat_event) for receiver_id in receiver_ids[1:]]
        self.mock_connection_manager.send_personal_message.assert_has_calls(expected_calls, any_order=True)
        for recorded_call in self.mock_connection_manager.send_personal_message.call_args_list:
            assert recorded_call.args[0] != receiver_ids[0]

    @pytest.mark.asyncio
    async def test_room_based_channels_echo_sender_even_when_muted(self) -> None:
        """Test that the sender still receives an echo even when everyone else filters them out."""
        chat_event = self.create_chat_event("say", "Hello everyone!")
        self._prepare_connection_manager()

        with (
            patch.object(self.handler, "_is_player_in_room", return_value=True),
            patch.object(self.handler, "_is_player_muted_by_receiver_with_user_manager", return_value=True),
        ):
            await self.handler._broadcast_to_room_with_filtering(self.room_id, chat_event, self.sender_id, "say")

        self.mock_connection_manager.send_personal_message.assert_called_once_with(self.sender_id, chat_event)

    @pytest.mark.asyncio
    async def test_room_based_channels_handle_players_not_in_room(self) -> None:
        """Test that room-based channels filter out players not in the room."""
        chat_event = self.create_chat_event("say", "Hello everyone!")
        self._prepare_connection_manager()

        with (
            patch.object(self.handler, "_is_player_in_room", return_value=False),
            patch.object(self.handler, "_is_player_muted_by_receiver_with_user_manager", return_value=False),
        ):
            await self.handler._broadcast_to_room_with_filtering(self.room_id, chat_event, self.sender_id, "say")

        self.mock_connection_manager.send_personal_message.assert_called_once_with(self.sender_id, chat_event)

    @pytest.mark.asyncio
    async def test_room_based_channels_performance_with_optimized_user_manager(self) -> None:
        """Test that room-based channels use optimized UserManager instance management."""
        chat_event = self.create_chat_event("say", "Hello everyone!")
        self._prepare_connection_manager()

        with (
            patch.object(self.handler, "_is_player_in_room", return_value=True),
            patch.object(self.handler, "_is_player_muted_by_receiver_with_user_manager", return_value=False),
            patch("server.services.user_manager.user_manager") as mock_user_manager,
        ):
            await self.handler._broadcast_to_room_with_filtering(self.room_id, chat_event, self.sender_id, "say")

        mock_user_manager.load_player_mutes.assert_called_with(self.receiver_id)
