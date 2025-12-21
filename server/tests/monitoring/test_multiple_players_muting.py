"""
Tests for multiple players muting the same person.

This module tests scenarios where multiple players have muted the same sender,
ensuring that the mute filtering works correctly for all muting players.
"""

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, call, patch

import pytest

from server.realtime.nats_message_handler import NATSMessageHandler
from server.services.nats_service import NATSService


class TestMultiplePlayersMuting:
    """Test multiple players muting the same person."""

    # Type annotations for instance attributes (satisfies linter without requiring __init__)
    # Attributes are initialized in setup_method() per pytest best practices
    mock_nats_service: MagicMock
    mock_connection_manager: MagicMock
    mock_async_persistence: MagicMock
    handler: NATSMessageHandler
    room_id: str
    sender_id: str
    sender_name: str
    muted_receivers: list[str]
    unmuted_receivers: list[str]
    all_players: list[str]

    def setup_method(self) -> None:
        """Set up test fixtures."""
        self.mock_nats_service = MagicMock(spec=NATSService)
        # AI Agent: Inject mock connection_manager via constructor (no longer a global)
        #           Post-migration: NATSMessageHandler requires connection_manager
        self.mock_connection_manager = MagicMock()
        # Mock async_persistence for filtering helper's is_player_in_room method
        self.mock_async_persistence = MagicMock()
        self.mock_async_persistence.get_player_by_id = AsyncMock(return_value=None)
        self.mock_connection_manager.async_persistence = self.mock_async_persistence
        # Mock canonical_room_id method used by filtering helper
        self.mock_connection_manager.canonical_room_id = MagicMock(side_effect=lambda room_id: room_id)
        self.handler = NATSMessageHandler(self.mock_nats_service, connection_manager=self.mock_connection_manager)

        # Test data
        self.room_id = "earth_arkhamcity_sanitarium_room_hallway_001"
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
    async def test_multiple_players_muting_same_sender_say(self) -> None:
        """Say channel should ignore personal mutes so everyone in the room hears the message."""
        chat_event = self.create_chat_event("say", "Hello everyone!")

        # AI Agent: Use mock from setup_method (injected via constructor)
        self.mock_connection_manager.room_subscriptions = {self.room_id: set(self.all_players)}
        self.mock_connection_manager._canonical_room_id.return_value = self.room_id
        self.mock_connection_manager.send_personal_message = AsyncMock()

        # Mock player in room check - patch filtering helper's method directly
        with patch.object(self.handler._filtering_helper, "is_player_in_room", return_value=True):
            await self.handler._broadcast_to_room_with_filtering(self.room_id, chat_event, self.sender_id, "say")

        # send_personal_message receives UUID objects, not strings
        expected_calls = [call(uuid.UUID(player_id), chat_event) for player_id in self.all_players]
        self.mock_connection_manager.send_personal_message.assert_has_calls(expected_calls, any_order=True)
        assert self.mock_connection_manager.send_personal_message.await_count == len(self.all_players)

    @pytest.mark.asyncio
    async def test_multiple_players_muting_same_sender_emote(self) -> None:
        """Test that multiple players muting the same sender works for emote messages."""
        chat_event = self.create_chat_event("emote", "dance")

        # AI Agent: Use mock from setup_method (injected via constructor)
        self.mock_connection_manager.room_subscriptions = {self.room_id: set(self.all_players)}
        self.mock_connection_manager._canonical_room_id.return_value = self.room_id
        self.mock_connection_manager.send_personal_message = AsyncMock()

        # Mock player in room check - patch filtering helper's method directly
        with patch.object(self.handler._filtering_helper, "is_player_in_room", return_value=True):
            # Mock mute check - muted receivers have muted sender, unmuted receivers haven't
            # Patch _is_player_muted_by_receiver (not _with_user_manager) as the code checks this first
            def mock_mute_check(receiver_id, _sender_id):
                return receiver_id in self.muted_receivers

            with patch.object(self.handler, "_is_player_muted_by_receiver", side_effect=mock_mute_check):
                # Execute
                await self.handler._broadcast_to_room_with_filtering(self.room_id, chat_event, self.sender_id, "emote")

                # Verify that only unmuted receivers got the message
                # send_personal_message receives UUID objects, not strings
                expected_calls = [call(uuid.UUID(receiver_id), chat_event) for receiver_id in self.unmuted_receivers]
                expected_calls.append(call(uuid.UUID(self.sender_id), chat_event))
                self.mock_connection_manager.send_personal_message.assert_has_calls(expected_calls, any_order=True)

                # Verify muted receivers didn't get the message
                muted_calls = [
                    call
                    for call in self.mock_connection_manager.send_personal_message.call_args_list
                    if call[0][0] in self.muted_receivers
                ]
                assert len(muted_calls) == 0

    @pytest.mark.asyncio
    async def test_multiple_players_muting_same_sender_local(self) -> None:
        """Test that multiple players muting the same sender works for local messages."""
        chat_event = self.create_chat_event("local", "Anyone in the area?")

        # AI Agent: Use mock from setup_method (injected via constructor)
        self.mock_connection_manager.room_subscriptions = {self.room_id: set(self.all_players)}
        self.mock_connection_manager._canonical_room_id.return_value = self.room_id
        self.mock_connection_manager.send_personal_message = AsyncMock()

        # Mock player in room check - patch filtering helper's method directly
        with patch.object(self.handler._filtering_helper, "is_player_in_room", return_value=True):
            # Mock mute check - muted receivers have muted sender, unmuted receivers haven't
            # Patch _is_player_muted_by_receiver (not _with_user_manager) as the code checks this first
            def mock_mute_check(receiver_id, _sender_id):
                return receiver_id in self.muted_receivers

            with patch.object(self.handler, "_is_player_muted_by_receiver", side_effect=mock_mute_check):
                # Execute
                await self.handler._broadcast_to_room_with_filtering(self.room_id, chat_event, self.sender_id, "local")

                # Verify that only unmuted receivers got the message
                # send_personal_message receives UUID objects, not strings
                expected_calls = [call(uuid.UUID(receiver_id), chat_event) for receiver_id in self.unmuted_receivers]
                expected_calls.append(call(uuid.UUID(self.sender_id), chat_event))
                self.mock_connection_manager.send_personal_message.assert_has_calls(expected_calls, any_order=True)

                # Verify muted receivers didn't get the message
                muted_calls = [
                    call
                    for call in self.mock_connection_manager.send_personal_message.call_args_list
                    if call[0][0] in self.muted_receivers
                ]
                assert len(muted_calls) == 0

    @pytest.mark.asyncio
    async def test_multiple_players_muting_same_sender_pose(self) -> None:
        """Test that multiple players muting the same sender works for pose messages."""
        chat_event = self.create_chat_event("pose", "looks around nervously")

        # AI Agent: Use mock from setup_method (injected via constructor)
        self.mock_connection_manager.room_subscriptions = {self.room_id: set(self.all_players)}
        self.mock_connection_manager._canonical_room_id.return_value = self.room_id
        self.mock_connection_manager.send_personal_message = AsyncMock()

        # Mock player in room check - patch filtering helper's method directly
        with patch.object(self.handler._filtering_helper, "is_player_in_room", return_value=True):
            # Mock mute check - muted receivers have muted sender, unmuted receivers haven't
            # Patch _is_player_muted_by_receiver (not _with_user_manager) as the code checks this first
            def mock_mute_check(receiver_id, _sender_id):
                return receiver_id in self.muted_receivers

            with patch.object(self.handler, "_is_player_muted_by_receiver", side_effect=mock_mute_check):
                # Execute
                await self.handler._broadcast_to_room_with_filtering(self.room_id, chat_event, self.sender_id, "pose")

                # Verify that only unmuted receivers got the message
                # send_personal_message receives UUID objects, not strings
                expected_calls = [call(uuid.UUID(receiver_id), chat_event) for receiver_id in self.unmuted_receivers]
                expected_calls.append(call(uuid.UUID(self.sender_id), chat_event))
                self.mock_connection_manager.send_personal_message.assert_has_calls(expected_calls, any_order=True)

                # Verify muted receivers didn't get the message
                muted_calls = [
                    call
                    for call in self.mock_connection_manager.send_personal_message.call_args_list
                    if call[0][0] in self.muted_receivers
                ]
                assert len(muted_calls) == 0

    @pytest.mark.asyncio
    async def test_all_players_muting_same_sender(self) -> None:
        """Test scenario where all players have muted the same sender."""
        chat_event = self.create_chat_event("local", "Hello everyone!")

        # AI Agent: Use mock from setup_method (injected via constructor)
        self.mock_connection_manager.room_subscriptions = {self.room_id: set(self.all_players)}
        self.mock_connection_manager._canonical_room_id.return_value = self.room_id
        self.mock_connection_manager.send_personal_message = AsyncMock()

        # Mock player in room check - patch filtering helper's method directly
        with patch.object(self.handler._filtering_helper, "is_player_in_room", return_value=True):
            # Mock mute check - all receivers have muted sender
            # Patch _is_player_muted_by_receiver (not _with_user_manager) as the code checks this first
            # The method signature is (receiver_id, sender_id), not (user_manager, receiver_id, sender_id)
            def mock_mute_check(receiver_id, _sender_id):
                return receiver_id != self.sender_id  # All receivers except sender have muted

            with patch.object(self.handler, "_is_player_muted_by_receiver", side_effect=mock_mute_check):
                # Execute
                await self.handler._broadcast_to_room_with_filtering(self.room_id, chat_event, self.sender_id, "local")

                # Only sender should receive the echo
                # send_personal_message receives UUID object, not string
                self.mock_connection_manager.send_personal_message.assert_called_once_with(
                    uuid.UUID(self.sender_id), chat_event
                )

    @pytest.mark.asyncio
    async def test_partial_muting_with_mixed_room_status(self) -> None:
        """Test partial muting where some players are not in the room."""
        chat_event = self.create_chat_event("local", "Hello everyone!")

        # Some players are in the room, some are not
        players_in_room = [self.sender_id] + self.muted_receivers[:2] + self.unmuted_receivers[:1]
        players_not_in_room = self.muted_receivers[2:] + self.unmuted_receivers[1:]

        # AI Agent: Use mock from setup_method (injected via constructor)
        self.mock_connection_manager.room_subscriptions = {
            self.room_id: set(self.all_players)  # All players are subscribed
        }
        self.mock_connection_manager._canonical_room_id.return_value = self.room_id
        self.mock_connection_manager.send_personal_message = AsyncMock()

        # Mock player in room check - some players are in room, some are not
        def mock_in_room_check(player_id, _room_id):
            return player_id in players_in_room

        with patch.object(self.handler._filtering_helper, "is_player_in_room", side_effect=mock_in_room_check):
            # Mock mute check - muted receivers have muted sender
            def mock_mute_check(_user_manager, receiver_id, _sender_id):
                return receiver_id in self.muted_receivers

            with patch.object(
                self.handler, "_is_player_muted_by_receiver_with_user_manager", side_effect=mock_mute_check
            ):
                # Execute
                await self.handler._broadcast_to_room_with_filtering(self.room_id, chat_event, self.sender_id, "local")

                # Verify that only unmuted players who are in the room got the message
                # send_personal_message receives UUID objects, not strings
                expected_recipients = [pid for pid in self.unmuted_receivers if pid in players_in_room]
                expected_calls = [call(uuid.UUID(receiver_id), chat_event) for receiver_id in expected_recipients]
                expected_calls.append(call(uuid.UUID(self.sender_id), chat_event))
                self.mock_connection_manager.send_personal_message.assert_has_calls(expected_calls, any_order=True)

                # Verify muted players didn't get the message (even if they're in the room)
                muted_calls = [
                    call
                    for call in self.mock_connection_manager.send_personal_message.call_args_list
                    if call[0][0] in self.muted_receivers
                ]
                assert len(muted_calls) == 0

                # Verify players not in room didn't get the message
                not_in_room_calls = [
                    call
                    for call in self.mock_connection_manager.send_personal_message.call_args_list
                    if call[0][0] in players_not_in_room
                ]
                assert len(not_in_room_calls) == 0

    @pytest.mark.asyncio
    async def test_user_manager_efficiency_with_multiple_mutes(self) -> None:
        """Test that UserManager is used efficiently when multiple players have muted the same sender."""
        chat_event = self.create_chat_event("local", "Hello everyone!")

        # AI Agent: Use mock from setup_method (injected via constructor)
        self.mock_connection_manager.room_subscriptions = {self.room_id: set(self.all_players)}
        self.mock_connection_manager._canonical_room_id.return_value = self.room_id
        self.mock_connection_manager.send_personal_message = AsyncMock()

        # Mock player in room check - patch filtering helper's method directly
        with patch.object(self.handler._filtering_helper, "is_player_in_room", return_value=True):
            # Mock the global user_manager instance
            with patch("server.services.user_manager.user_manager") as mock_user_manager:
                # Mock batch loading method (implementation now uses batch loading for efficiency)
                # Return mutes for muted_receivers
                mock_mutes = {receiver_id: {self.sender_id} for receiver_id in self.muted_receivers}
                mock_user_manager.load_player_mutes_batch = AsyncMock(return_value=mock_mutes)
                # Also mock load_player_mutes_async which is called by is_player_muted_by_receiver_with_user_manager
                mock_user_manager.load_player_mutes_async = AsyncMock(return_value=set())

                # Execute
                await self.handler._broadcast_to_room_with_filtering(self.room_id, chat_event, self.sender_id, "local")

                # Verify that mute data was pre-loaded for all receivers using batch loading
                expected_receivers = [pid for pid in self.all_players if pid != self.sender_id]
                # Implementation now uses load_player_mutes_batch instead of individual calls
                mock_user_manager.load_player_mutes_batch.assert_called_once()
                call_args = mock_user_manager.load_player_mutes_batch.call_args[0][0]
                assert set(call_args) == set(expected_receivers), "Batch load should include all expected receivers"
