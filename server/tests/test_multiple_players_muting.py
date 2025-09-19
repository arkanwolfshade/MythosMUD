"""
Tests for multiple players muting the same person.

This module tests scenarios where multiple players have muted the same sender,
ensuring that the mute filtering works correctly for all muting players.
"""

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.nats_message_handler import NATSMessageHandler
from server.services.nats_service import NATSService


class TestMultiplePlayersMuting:
    """Test multiple players muting the same person."""

    def setup_method(self):
        """Set up test fixtures."""
        self.mock_nats_service = MagicMock(spec=NATSService)
        self.handler = NATSMessageHandler(self.mock_nats_service)

        # Test data
        self.room_id = "earth_arkham_city_sanitarium_room_hallway_001"
        self.sender_id = str(uuid.uuid4())
        self.sender_name = "Ithaqua"

        # Multiple receivers who have muted the sender
        self.muted_receivers = [str(uuid.uuid4()) for _ in range(3)]
        self.unmuted_receivers = [str(uuid.uuid4()) for _ in range(2)]

        # All players in the room
        self.all_players = [self.sender_id] + self.muted_receivers + self.unmuted_receivers

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
    async def test_multiple_players_muting_same_sender_say(self):
        """Test that multiple players muting the same sender works for say messages."""
        chat_event = self.create_chat_event("say", "Hello everyone!")

        with patch("server.realtime.nats_message_handler.connection_manager") as mock_conn_mgr:
            # Mock room subscriptions
            mock_conn_mgr.room_subscriptions = {self.room_id: set(self.all_players)}
            mock_conn_mgr._canonical_room_id.return_value = self.room_id
            mock_conn_mgr.send_personal_message = AsyncMock()

            # Mock player in room check
            with patch.object(self.handler, "_is_player_in_room", return_value=True):
                # Mock mute check - muted receivers have muted sender, unmuted receivers haven't
                def mock_mute_check(user_manager, receiver_id, sender_id):
                    return receiver_id in self.muted_receivers

                with patch.object(
                    self.handler, "_is_player_muted_by_receiver_with_user_manager", side_effect=mock_mute_check
                ):
                    # Execute
                    await self.handler._broadcast_to_room_with_filtering(
                        self.room_id, chat_event, self.sender_id, "say"
                    )

                    # Verify that only unmuted receivers got the message
                    expected_calls = [((receiver_id, chat_event),) for receiver_id in self.unmuted_receivers]
                    mock_conn_mgr.send_personal_message.assert_has_calls(expected_calls, any_order=True)

                    # Verify muted receivers didn't get the message
                    muted_calls = [
                        call
                        for call in mock_conn_mgr.send_personal_message.call_args_list
                        if call[0][0] in self.muted_receivers
                    ]
                    assert len(muted_calls) == 0

                    # Verify sender didn't get their own message
                    sender_calls = [
                        call
                        for call in mock_conn_mgr.send_personal_message.call_args_list
                        if call[0][0] == self.sender_id
                    ]
                    assert len(sender_calls) == 0

    @pytest.mark.asyncio
    async def test_multiple_players_muting_same_sender_emote(self):
        """Test that multiple players muting the same sender works for emote messages."""
        chat_event = self.create_chat_event("emote", "dance")

        with patch("server.realtime.nats_message_handler.connection_manager") as mock_conn_mgr:
            # Mock room subscriptions
            mock_conn_mgr.room_subscriptions = {self.room_id: set(self.all_players)}
            mock_conn_mgr._canonical_room_id.return_value = self.room_id
            mock_conn_mgr.send_personal_message = AsyncMock()

            # Mock player in room check
            with patch.object(self.handler, "_is_player_in_room", return_value=True):
                # Mock mute check - muted receivers have muted sender, unmuted receivers haven't
                def mock_mute_check(user_manager, receiver_id, sender_id):
                    return receiver_id in self.muted_receivers

                with patch.object(
                    self.handler, "_is_player_muted_by_receiver_with_user_manager", side_effect=mock_mute_check
                ):
                    # Execute
                    await self.handler._broadcast_to_room_with_filtering(
                        self.room_id, chat_event, self.sender_id, "emote"
                    )

                    # Verify that only unmuted receivers got the message
                    expected_calls = [((receiver_id, chat_event),) for receiver_id in self.unmuted_receivers]
                    mock_conn_mgr.send_personal_message.assert_has_calls(expected_calls, any_order=True)

                    # Verify muted receivers didn't get the message
                    muted_calls = [
                        call
                        for call in mock_conn_mgr.send_personal_message.call_args_list
                        if call[0][0] in self.muted_receivers
                    ]
                    assert len(muted_calls) == 0

    @pytest.mark.asyncio
    async def test_multiple_players_muting_same_sender_local(self):
        """Test that multiple players muting the same sender works for local messages."""
        chat_event = self.create_chat_event("local", "Anyone in the area?")

        with patch("server.realtime.nats_message_handler.connection_manager") as mock_conn_mgr:
            # Mock room subscriptions
            mock_conn_mgr.room_subscriptions = {self.room_id: set(self.all_players)}
            mock_conn_mgr._canonical_room_id.return_value = self.room_id
            mock_conn_mgr.send_personal_message = AsyncMock()

            # Mock player in room check
            with patch.object(self.handler, "_is_player_in_room", return_value=True):
                # Mock mute check - muted receivers have muted sender, unmuted receivers haven't
                def mock_mute_check(user_manager, receiver_id, sender_id):
                    return receiver_id in self.muted_receivers

                with patch.object(
                    self.handler, "_is_player_muted_by_receiver_with_user_manager", side_effect=mock_mute_check
                ):
                    # Execute
                    await self.handler._broadcast_to_room_with_filtering(
                        self.room_id, chat_event, self.sender_id, "local"
                    )

                    # Verify that only unmuted receivers got the message
                    expected_calls = [((receiver_id, chat_event),) for receiver_id in self.unmuted_receivers]
                    mock_conn_mgr.send_personal_message.assert_has_calls(expected_calls, any_order=True)

                    # Verify muted receivers didn't get the message
                    muted_calls = [
                        call
                        for call in mock_conn_mgr.send_personal_message.call_args_list
                        if call[0][0] in self.muted_receivers
                    ]
                    assert len(muted_calls) == 0

    @pytest.mark.asyncio
    async def test_multiple_players_muting_same_sender_pose(self):
        """Test that multiple players muting the same sender works for pose messages."""
        chat_event = self.create_chat_event("pose", "looks around nervously")

        with patch("server.realtime.nats_message_handler.connection_manager") as mock_conn_mgr:
            # Mock room subscriptions
            mock_conn_mgr.room_subscriptions = {self.room_id: set(self.all_players)}
            mock_conn_mgr._canonical_room_id.return_value = self.room_id
            mock_conn_mgr.send_personal_message = AsyncMock()

            # Mock player in room check
            with patch.object(self.handler, "_is_player_in_room", return_value=True):
                # Mock mute check - muted receivers have muted sender, unmuted receivers haven't
                def mock_mute_check(user_manager, receiver_id, sender_id):
                    return receiver_id in self.muted_receivers

                with patch.object(
                    self.handler, "_is_player_muted_by_receiver_with_user_manager", side_effect=mock_mute_check
                ):
                    # Execute
                    await self.handler._broadcast_to_room_with_filtering(
                        self.room_id, chat_event, self.sender_id, "pose"
                    )

                    # Verify that only unmuted receivers got the message
                    expected_calls = [((receiver_id, chat_event),) for receiver_id in self.unmuted_receivers]
                    mock_conn_mgr.send_personal_message.assert_has_calls(expected_calls, any_order=True)

                    # Verify muted receivers didn't get the message
                    muted_calls = [
                        call
                        for call in mock_conn_mgr.send_personal_message.call_args_list
                        if call[0][0] in self.muted_receivers
                    ]
                    assert len(muted_calls) == 0

    @pytest.mark.asyncio
    async def test_all_players_muting_same_sender(self):
        """Test scenario where all players have muted the same sender."""
        chat_event = self.create_chat_event("say", "Hello everyone!")

        with patch("server.realtime.nats_message_handler.connection_manager") as mock_conn_mgr:
            # Mock room subscriptions
            mock_conn_mgr.room_subscriptions = {self.room_id: set(self.all_players)}
            mock_conn_mgr._canonical_room_id.return_value = self.room_id
            mock_conn_mgr.send_personal_message = AsyncMock()

            # Mock player in room check
            with patch.object(self.handler, "_is_player_in_room", return_value=True):
                # Mock mute check - all receivers have muted sender
                def mock_mute_check(user_manager, receiver_id, sender_id):
                    return receiver_id != self.sender_id  # All receivers except sender have muted

                with patch.object(
                    self.handler, "_is_player_muted_by_receiver_with_user_manager", side_effect=mock_mute_check
                ):
                    # Execute
                    await self.handler._broadcast_to_room_with_filtering(
                        self.room_id, chat_event, self.sender_id, "say"
                    )

                    # Verify that no one received the message (all receivers muted, sender excluded)
                    mock_conn_mgr.send_personal_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_partial_muting_with_mixed_room_status(self):
        """Test partial muting where some players are not in the room."""
        chat_event = self.create_chat_event("say", "Hello everyone!")

        # Some players are in the room, some are not
        players_in_room = [self.sender_id] + self.muted_receivers[:2] + self.unmuted_receivers[:1]
        players_not_in_room = self.muted_receivers[2:] + self.unmuted_receivers[1:]

        with patch("server.realtime.nats_message_handler.connection_manager") as mock_conn_mgr:
            # Mock room subscriptions
            mock_conn_mgr.room_subscriptions = {
                self.room_id: set(self.all_players)  # All players are subscribed
            }
            mock_conn_mgr._canonical_room_id.return_value = self.room_id
            mock_conn_mgr.send_personal_message = AsyncMock()

            # Mock player in room check - some players are in room, some are not
            def mock_in_room_check(player_id, room_id):
                return player_id in players_in_room

            with patch.object(self.handler, "_is_player_in_room", side_effect=mock_in_room_check):
                # Mock mute check - muted receivers have muted sender
                def mock_mute_check(user_manager, receiver_id, sender_id):
                    return receiver_id in self.muted_receivers

                with patch.object(
                    self.handler, "_is_player_muted_by_receiver_with_user_manager", side_effect=mock_mute_check
                ):
                    # Execute
                    await self.handler._broadcast_to_room_with_filtering(
                        self.room_id, chat_event, self.sender_id, "say"
                    )

                    # Verify that only unmuted players who are in the room got the message
                    expected_recipients = [pid for pid in self.unmuted_receivers if pid in players_in_room]
                    expected_calls = [((receiver_id, chat_event),) for receiver_id in expected_recipients]
                    mock_conn_mgr.send_personal_message.assert_has_calls(expected_calls, any_order=True)

                    # Verify muted players didn't get the message (even if they're in the room)
                    muted_calls = [
                        call
                        for call in mock_conn_mgr.send_personal_message.call_args_list
                        if call[0][0] in self.muted_receivers
                    ]
                    assert len(muted_calls) == 0

                    # Verify players not in room didn't get the message
                    not_in_room_calls = [
                        call
                        for call in mock_conn_mgr.send_personal_message.call_args_list
                        if call[0][0] in players_not_in_room
                    ]
                    assert len(not_in_room_calls) == 0

    @pytest.mark.asyncio
    async def test_user_manager_efficiency_with_multiple_mutes(self):
        """Test that UserManager is used efficiently when multiple players have muted the same sender."""
        chat_event = self.create_chat_event("say", "Hello everyone!")

        with patch("server.realtime.nats_message_handler.connection_manager") as mock_conn_mgr:
            # Mock room subscriptions
            mock_conn_mgr.room_subscriptions = {self.room_id: set(self.all_players)}
            mock_conn_mgr._canonical_room_id.return_value = self.room_id
            mock_conn_mgr.send_personal_message = AsyncMock()

            # Mock player in room check
            with patch.object(self.handler, "_is_player_in_room", return_value=True):
                # Mock mute check
                def mock_mute_check(user_manager, receiver_id, sender_id):
                    return receiver_id in self.muted_receivers

                with patch.object(
                    self.handler, "_is_player_muted_by_receiver_with_user_manager", side_effect=mock_mute_check
                ):
                    # Mock UserManager to verify it's created only once
                    with patch("server.services.user_manager.UserManager") as mock_user_manager_class:
                        mock_user_manager = MagicMock()
                        mock_user_manager_class.return_value = mock_user_manager

                        # Execute
                        await self.handler._broadcast_to_room_with_filtering(
                            self.room_id, chat_event, self.sender_id, "say"
                        )

                        # Verify that UserManager was created only once (optimization)
                        mock_user_manager_class.assert_called_once()

                        # Verify that mute data was pre-loaded for all receivers
                        expected_receivers = [pid for pid in self.all_players if pid != self.sender_id]
                        for receiver_id in expected_receivers:
                            mock_user_manager.load_player_mutes.assert_any_call(receiver_id)
