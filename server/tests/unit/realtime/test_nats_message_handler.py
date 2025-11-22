"""
Tests for the NATS message handler functionality.

This module tests the NATSMessageHandler class which handles incoming NATS messages
and broadcasts them to WebSocket clients based on channel type and room subscriptions.
"""

import uuid
from datetime import datetime
from unittest.mock import AsyncMock, Mock, patch
from uuid import NAMESPACE_DNS, UUID, uuid5

import pytest

from server.realtime.nats_message_handler import NATSMessageHandler
from server.services.nats_service import NATSService


def _str_to_uuid(player_id_str: str) -> UUID:
    """Convert string player_id to UUID deterministically for tests."""
    return uuid5(NAMESPACE_DNS, player_id_str)


class TestNATSMessageHandler:
    """Test cases for NATSMessageHandler."""

    def setup_method(self):
        """Set up test fixtures."""
        # Create a mock NATS service
        self.mock_nats_service = Mock()
        self.mock_nats_service.subscribe = AsyncMock()
        self.mock_nats_service.unsubscribe = AsyncMock()

        # Create a mock subject manager with expected subscription patterns
        self.mock_subject_manager = Mock()
        self.mock_subject_manager.get_chat_subscription_patterns = Mock(
            return_value=[
                "chat.say.*",
                "chat.local.*",
                "chat.local.subzone.*",
                "chat.emote.*",
                "chat.pose.*",
                "chat.global",
                "chat.party.*",
                "chat.whisper.player.*",
                "chat.system",
                "chat.admin",
            ]
        )
        self.mock_subject_manager.get_event_subscription_patterns = Mock(
            return_value=[
                "events.player_entered.*",
                "events.player_left.*",
                "events.game_tick",
                "combat.attack.*",
                "combat.npc_attacked.*",
                "combat.npc_action.*",
                "combat.started.*",
                "combat.ended.*",
                "combat.npc_died.*",
                "events.player_mortally_wounded.*",
                "events.player_hp_decay.*",
                "events.player_died.*",
                "events.player_respawned.*",
            ]
        )

        # Create the handler instance with subject manager
        self.handler = NATSMessageHandler(self.mock_nats_service, subject_manager=self.mock_subject_manager)

        # Mock connection manager
        self.mock_connection_manager = Mock()
        self.mock_connection_manager.broadcast_global = AsyncMock()
        self.mock_connection_manager.send_personal_message = AsyncMock()
        self.mock_connection_manager._canonical_room_id = Mock(return_value=None)
        self.mock_connection_manager.room_subscriptions = {}
        self.mock_connection_manager.online_players = {}

    def test_initialization(self):
        """Test NATSMessageHandler initialization."""
        assert self.handler.nats_service == self.mock_nats_service
        assert self.handler.subscriptions == {}
        assert hasattr(self.handler, "start")
        assert hasattr(self.handler, "stop")

    @pytest.mark.asyncio
    async def test_start_success(self):
        """Test successful start of the message handler."""
        # Mock successful subscription
        self.mock_nats_service.subscribe.return_value = True

        await self.handler.start()

        # Verify subscriptions were created
        expected_chat_subjects = [
            "chat.say.*",
            "chat.local.*",
            "chat.local.subzone.*",
            "chat.emote.*",
            "chat.pose.*",
            "chat.global",
            "chat.party.*",
            "chat.whisper.player.*",  # Standardized whisper pattern with player segment
            "chat.system",
            "chat.admin",
        ]

        expected_event_subjects = [
            "events.player_entered.*",
            "events.player_left.*",
            "events.game_tick",
            "combat.attack.*",
            "combat.npc_attacked.*",
            "combat.npc_action.*",
            "combat.started.*",
            "combat.ended.*",
            "combat.npc_died.*",
            "events.player_mortally_wounded.*",
            "events.player_hp_decay.*",
            "events.player_died.*",
            "events.player_respawned.*",
        ]

        # Verify chat subscriptions
        for subject in expected_chat_subjects:
            assert subject in self.handler.subscriptions

        # Verify event subscriptions
        for subject in expected_event_subjects:
            assert subject in self.handler.subscriptions

        # Verify total count - remove duplicates since some combat subjects appear in both lists
        all_expected_subjects = set(expected_chat_subjects + expected_event_subjects)
        expected_total = len(all_expected_subjects)
        assert len(self.handler.subscriptions) == expected_total

        # Verify all subscriptions are active
        for subject in expected_chat_subjects + expected_event_subjects:
            assert self.handler.subscriptions[subject] is True

    @pytest.mark.asyncio
    async def test_start_with_subscription_failure(self):
        """Test start when some subscriptions fail."""

        # Mock some subscriptions to fail
        def mock_subscribe(subject, callback):
            if "whisper" in subject:
                return False
            return True

        self.mock_nats_service.subscribe.side_effect = mock_subscribe

        await self.handler.start()

        # Verify successful subscriptions were recorded
        assert "chat.say.*" in self.handler.subscriptions
        assert "chat.local.*" in self.handler.subscriptions
        assert "chat.global" in self.handler.subscriptions
        assert "chat.whisper.*" not in self.handler.subscriptions

    @pytest.mark.asyncio
    async def test_start_with_exception(self):
        """Test start when an exception occurs."""
        self.mock_nats_service.subscribe.side_effect = Exception("NATS connection failed")

        # Should not raise exception
        await self.handler.start()

        # Verify no subscriptions were created
        assert len(self.handler.subscriptions) == 0

    @pytest.mark.asyncio
    async def test_stop_success(self):
        """Test successful stop of the message handler."""
        # Set up some subscriptions
        self.handler.subscriptions = {"chat.say.room1": True, "chat.global": True, "chat.system": True}

        self.mock_nats_service.unsubscribe.return_value = True

        await self.handler.stop()

        # Verify all subscriptions were removed
        assert len(self.handler.subscriptions) == 0
        assert self.mock_nats_service.unsubscribe.call_count == 3

    @pytest.mark.asyncio
    async def test_stop_with_unsubscribe_failure(self):
        """Test stop when some unsubscriptions fail."""
        # Set up some subscriptions
        self.handler.subscriptions = {
            "chat.say.room1": True,
            "chat.global": True,
        }

        def mock_unsubscribe(subject):
            if "global" in subject:
                return False
            return True

        self.mock_nats_service.unsubscribe.side_effect = mock_unsubscribe

        await self.handler.stop()

        # Verify unsubscribe was called for all subjects
        assert self.mock_nats_service.unsubscribe.call_count == 2

    @pytest.mark.asyncio
    async def test_stop_with_exception(self):
        """Test stop when an exception occurs."""
        self.handler.subscriptions = {"chat.say.room1": True}
        self.mock_nats_service.unsubscribe.side_effect = Exception("NATS error")

        # Should not raise exception
        await self.handler.stop()

    @pytest.mark.asyncio
    async def test_handle_nats_message_valid_say(self):
        """Test handling a valid say message."""
        sender_id = uuid.uuid4()  # UUID object - convert to string only for NATS message data
        message_data = {
            "channel": "say",
            "room_id": "room_001",
            "sender_id": str(sender_id),  # NATS sends as string, but we use UUID object internally
            "sender_name": "TestPlayer",
            "content": "Hello, world!",
            "message_id": str(uuid.uuid4()),
            "timestamp": datetime.now().isoformat(),
        }

        with patch("server.realtime.nats_message_handler.connection_manager", self.mock_connection_manager):
            with patch.object(self.handler, "_broadcast_by_channel_type", new_callable=AsyncMock) as mock_broadcast:
                await self.handler._handle_nats_message(message_data)

                mock_broadcast.assert_called_once()
                call_args = mock_broadcast.call_args[0]
                assert call_args[0] == "say"  # channel
                assert call_args[2] == "room_001"  # room_id
                assert call_args[5] == sender_id  # sender_id as UUID object

    @pytest.mark.asyncio
    @pytest.mark.slow
    async def test_handle_nats_message_invalid_missing_fields(self):
        """Test handling a message with missing required fields."""
        message_data = {
            "channel": "say",
            "room_id": "room_001",
            # Missing sender_id, sender_name, content, message_id
        }

        with patch("server.realtime.nats_message_handler.connection_manager", self.mock_connection_manager):
            await self.handler._handle_nats_message(message_data)

            # Should not call broadcast methods
            self.mock_connection_manager.broadcast_global.assert_not_called()
            self.mock_connection_manager.send_personal_message.assert_not_called()

    @pytest.mark.asyncio
    @pytest.mark.slow
    async def test_handle_nats_message_with_exception(self):
        """Test handling a message when an exception occurs."""
        message_data = {
            "channel": "say",
            "sender_id": "player_001",
            "sender_name": "TestPlayer",
            "content": "Hello, world!",
            "message_id": str(uuid.uuid4()),
        }

        with patch("server.realtime.nats_message_handler.connection_manager", self.mock_connection_manager):
            with patch.object(self.handler, "_broadcast_by_channel_type", side_effect=Exception("Broadcast error")):
                # Should not raise exception
                await self.handler._handle_nats_message(message_data)

    @pytest.mark.asyncio
    async def test_broadcast_by_channel_type_say(self):
        """Test broadcasting say messages."""
        chat_event = {"event_type": "chat_message", "data": {"message": "Hello"}}

        with patch("server.realtime.nats_message_handler.connection_manager", self.mock_connection_manager):
            with patch.object(
                self.handler, "_broadcast_to_room_with_filtering", new_callable=AsyncMock
            ) as mock_room_broadcast:
                player_id_uuid = uuid.uuid4()
                await self.handler._broadcast_by_channel_type("say", chat_event, "room_001", None, None, player_id_uuid)

                # _broadcast_to_room_with_filtering expects string sender_id
                mock_room_broadcast.assert_called_once_with("room_001", chat_event, str(player_id_uuid), "say")

    @pytest.mark.asyncio
    async def test_broadcast_by_channel_type_local(self):
        """Test broadcasting local messages."""
        chat_event = {"event_type": "chat_message", "data": {"message": "Hello"}}

        with patch("server.realtime.nats_message_handler.connection_manager", self.mock_connection_manager):
            with patch.object(
                self.handler, "_broadcast_to_room_with_filtering", new_callable=AsyncMock
            ) as mock_room_broadcast:
                player_id_uuid = uuid.uuid4()
                await self.handler._broadcast_by_channel_type(
                    "local", chat_event, "room_001", None, None, player_id_uuid
                )

                # _broadcast_to_room_with_filtering expects string sender_id
                mock_room_broadcast.assert_called_once_with("room_001", chat_event, str(player_id_uuid), "local")

    @pytest.mark.asyncio
    async def test_broadcast_by_channel_type_global(self):
        """Test broadcasting global messages."""
        chat_event = {"event_type": "chat_message", "data": {"message": "Hello"}}

        self.handler.connection_manager = self.mock_connection_manager

        try:
            player_id_uuid = uuid.uuid4()
            await self.handler._broadcast_by_channel_type("global", chat_event, None, None, None, player_id_uuid)
            # broadcast_global expects string exclude_player
            self.mock_connection_manager.broadcast_global.assert_called_once_with(
                chat_event, exclude_player=str(player_id_uuid)
            )
        finally:
            self.handler.connection_manager = None

    @pytest.mark.asyncio
    async def test_broadcast_by_channel_type_whisper(self):
        """Test broadcasting whisper messages."""
        chat_event = {"event_type": "chat_message", "data": {"message": "Hello"}}

        self.handler.connection_manager = self.mock_connection_manager

        try:
            target_player_uuid = uuid.uuid4()
            player_id_uuid = uuid.uuid4()
            await self.handler._broadcast_by_channel_type(
                "whisper", chat_event, None, None, target_player_uuid, player_id_uuid
            )
            self.mock_connection_manager.send_personal_message.assert_called_once_with(target_player_uuid, chat_event)
        finally:
            self.handler.connection_manager = None

    @pytest.mark.asyncio
    async def test_broadcast_by_channel_type_system(self):
        """Test broadcasting system messages."""
        chat_event = {"event_type": "chat_message", "data": {"message": "Hello"}}

        self.handler.connection_manager = self.mock_connection_manager

        try:
            player_id_uuid = uuid.uuid4()
            await self.handler._broadcast_by_channel_type("system", chat_event, None, None, None, player_id_uuid)
            # broadcast_global expects string exclude_player
            self.mock_connection_manager.broadcast_global.assert_called_once_with(
                chat_event, exclude_player=str(player_id_uuid)
            )
        finally:
            self.handler.connection_manager = None

    @pytest.mark.asyncio
    async def test_broadcast_by_channel_type_admin(self):
        """Test broadcasting admin messages."""
        chat_event = {"event_type": "chat_message", "data": {"message": "Hello"}}

        self.handler.connection_manager = self.mock_connection_manager

        try:
            player_id_uuid = uuid.uuid4()
            await self.handler._broadcast_by_channel_type("admin", chat_event, None, None, None, player_id_uuid)
            # broadcast_global expects string exclude_player
            self.mock_connection_manager.broadcast_global.assert_called_once_with(
                chat_event, exclude_player=str(player_id_uuid)
            )
        finally:
            self.handler.connection_manager = None

    @pytest.mark.asyncio
    async def test_broadcast_by_channel_type_unknown(self):
        """Test broadcasting unknown channel type."""
        chat_event = {"event_type": "chat_message", "data": {"message": "Hello"}}

        self.handler.connection_manager = self.mock_connection_manager

        try:
            await self.handler._broadcast_by_channel_type("unknown", chat_event, None, None, None, "player_001")

            # Should not call any broadcast methods
            self.mock_connection_manager.broadcast_global.assert_not_called()
            self.mock_connection_manager.send_personal_message.assert_not_called()
        finally:
            self.handler.connection_manager = None

    @pytest.mark.asyncio
    async def test_broadcast_by_channel_type_with_exception(self):
        """Test broadcasting when an exception occurs."""
        chat_event = {"event_type": "chat_message", "data": {"message": "Hello"}}

        with patch("server.realtime.connection_manager.connection_manager", self.mock_connection_manager):
            self.mock_connection_manager.broadcast_global.side_effect = Exception("Broadcast error")

            # Should not raise exception
            await self.handler._broadcast_by_channel_type("global", chat_event, None, None, None, "player_001")

    @pytest.mark.asyncio
    async def test_broadcast_to_room_with_filtering_success(self):
        """Test room broadcasting with filtering."""
        chat_event = {"event_type": "chat_message", "data": {"message": "Hello"}}

        # Use valid UUID strings for player IDs
        player_001_id = str(uuid.uuid4())
        player_002_id = str(uuid.uuid4())
        player_003_id = str(uuid.uuid4())

        # Set up connection manager mocks
        self.mock_connection_manager.room_subscriptions = {"room_001": {player_001_id, player_002_id, player_003_id}}
        self.mock_connection_manager.online_players = {
            player_001_id: {"current_room_id": "room_001"},
            player_002_id: {"current_room_id": "room_001"},
            player_003_id: {"current_room_id": "room_002"},  # Different room
        }

        with patch("server.realtime.nats_message_handler.connection_manager", self.mock_connection_manager):
            with patch.object(
                self.handler, "_is_player_in_room", side_effect=lambda p, r: p in [player_001_id, player_002_id]
            ):
                with patch.object(self.handler, "_is_player_muted_by_receiver", return_value=False):
                    await self.handler._broadcast_to_room_with_filtering("room_001", chat_event, player_001_id, "say")

                    # Should send to player_002 (player_001 is sender, player_003 is in different room)
                    assert self.mock_connection_manager.send_personal_message.call_count == 1
                    self.mock_connection_manager.send_personal_message.assert_called_with(
                        uuid.UUID(player_002_id), chat_event
                    )

    @pytest.mark.asyncio
    async def test_broadcast_to_room_with_filtering_muted_player(self):
        """Test room broadcasting with muted player filtering."""
        chat_event = {"event_type": "chat_message", "data": {"message": "Hello"}}

        # Set up connection manager mocks
        self.mock_connection_manager.room_subscriptions = {"room_001": {"player_001", "player_002"}}
        self.mock_connection_manager.online_players = {
            "player_001": {"current_room_id": "room_001"},
            "player_002": {"current_room_id": "room_001"},
        }

        with patch("server.realtime.nats_message_handler.connection_manager", self.mock_connection_manager):
            with patch.object(self.handler, "_is_player_in_room", return_value=True):
                with patch.object(self.handler, "_is_player_muted_by_receiver_with_user_manager", return_value=True):
                    await self.handler._broadcast_to_room_with_filtering("room_001", chat_event, "player_001", "say")

                    # Should not send to muted player
                    self.mock_connection_manager.send_personal_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_broadcast_to_room_with_filtering_exception(self):
        """Test room broadcasting when an exception occurs."""
        chat_event = {"event_type": "chat_message", "data": {"message": "Hello"}}

        with patch("server.realtime.nats_message_handler.connection_manager", self.mock_connection_manager):
            with patch.object(self.handler, "_is_player_in_room", side_effect=Exception("Room check error")):
                # Should not raise exception
                await self.handler._broadcast_to_room_with_filtering("room_001", chat_event, "player_001", "say")

    def test_is_player_in_room_true(self):
        """Test checking if player is in room - returns True."""
        self.mock_connection_manager.online_players = {"player_001": {"current_room_id": "room_001"}}
        self.mock_connection_manager._canonical_room_id.return_value = "room_001"

        with patch("server.realtime.nats_message_handler.connection_manager", self.mock_connection_manager):
            result = self.handler._is_player_in_room("player_001", "room_001")
            assert result is True

    def test_is_player_in_room_false(self):
        """Test checking if player is in room - returns False."""
        self.mock_connection_manager.online_players = {"player_001": {"current_room_id": "room_002"}}
        self.mock_connection_manager._canonical_room_id.side_effect = lambda x: x

        with patch("server.realtime.nats_message_handler.connection_manager", self.mock_connection_manager):
            result = self.handler._is_player_in_room("player_001", "room_001")
            assert result is False

    def test_is_player_in_room_player_not_online(self):
        """Test checking if player is in room - player not online."""
        self.mock_connection_manager.online_players = {}

        with patch("server.realtime.nats_message_handler.connection_manager", self.mock_connection_manager):
            result = self.handler._is_player_in_room("player_001", "room_001")
            assert result is False

    def test_is_player_in_room_with_exception(self):
        """Test checking if player is in room when exception occurs."""
        with patch("server.realtime.nats_message_handler.connection_manager", self.mock_connection_manager):
            self.mock_connection_manager.online_players = {"player_001": {"current_room_id": "room_001"}}
            self.mock_connection_manager._canonical_room_id.side_effect = Exception("Canonical ID error")

            result = self.handler._is_player_in_room("player_001", "room_001")
            assert result is False

    def test_is_player_muted_by_receiver_true(self):
        """Test checking if player is muted by receiver - returns True."""
        mock_user_manager = Mock()
        mock_user_manager.is_player_muted.return_value = True
        mock_user_manager.is_player_muted_by_others.return_value = False
        mock_user_manager.is_admin.return_value = False

        with patch("server.services.user_manager.user_manager", mock_user_manager):
            result = self.handler._is_player_muted_by_receiver("receiver_001", "sender_001")
            assert result is True

    def test_is_player_muted_by_receiver_false(self):
        """Test checking if player is muted by receiver - returns False."""
        mock_user_manager = Mock()
        mock_user_manager.is_player_muted.return_value = False
        mock_user_manager.is_player_muted_by_others.return_value = False
        mock_user_manager.is_admin.return_value = False

        with patch("server.services.user_manager.UserManager", return_value=mock_user_manager):
            result = self.handler._is_player_muted_by_receiver("receiver_001", "sender_001")
            assert result is False

    def test_is_player_muted_by_receiver_with_exception(self):
        """Test checking if player is muted when exception occurs."""
        with patch("server.services.user_manager.UserManager", side_effect=Exception("User manager error")):
            result = self.handler._is_player_muted_by_receiver("receiver_001", "sender_001")
            assert result is False

    @pytest.mark.asyncio
    async def test_subscribe_to_room(self):
        """Test subscribing to room-specific subjects."""
        # Mock build_subject to return expected subject string
        self.mock_subject_manager.build_subject = Mock(return_value="chat.say.room_001")

        with patch.object(self.handler, "_subscribe_to_subject", new_callable=AsyncMock) as mock_subscribe:
            await self.handler.subscribe_to_room("room_001")

            # Should subscribe to room-specific subject
            assert mock_subscribe.call_count == 1
            assert mock_subscribe.call_args[0][0] == "chat.say.room_001"

    @pytest.mark.asyncio
    async def test_unsubscribe_from_room(self):
        """Test unsubscribing from room-specific subjects."""
        # Mock build_subject to return expected subject string
        self.mock_subject_manager.build_subject = Mock(return_value="chat.say.room_001")

        # Set up existing subscriptions
        self.handler.subscriptions = {"chat.say.room_001": True, "chat.global": True}

        with patch.object(self.handler, "_unsubscribe_from_subject", new_callable=AsyncMock) as mock_unsubscribe:
            await self.handler.unsubscribe_from_room("room_001")

            # Should unsubscribe from room-specific subject
            assert mock_unsubscribe.call_count == 1
            assert mock_unsubscribe.call_args[0][0] == "chat.say.room_001"

    def test_get_subscription_count(self):
        """Test getting subscription count."""
        self.handler.subscriptions = {"chat.say.room1": True, "chat.global": True, "chat.system": True}

        count = self.handler.get_subscription_count()
        assert count == 3

    def test_get_active_subjects(self):
        """Test getting active subscription subjects."""
        self.handler.subscriptions = {"chat.say.room1": True, "chat.global": True, "chat.system": True}

        subjects = self.handler.get_active_subjects()
        expected_subjects = ["chat.say.room1", "chat.global", "chat.system"]
        assert set(subjects) == set(expected_subjects)


class TestNATSMessageHandlerEventSubscription:
    """Test cases for NATSMessageHandler event subscription capabilities."""

    def setup_method(self):
        """Set up test fixtures."""
        # Create a mock NATS service
        self.mock_nats_service = Mock()
        self.mock_nats_service.subscribe = AsyncMock()
        self.mock_nats_service.unsubscribe = AsyncMock()

        # Create a mock subject manager with expected subscription patterns
        self.mock_subject_manager = Mock()
        self.mock_subject_manager.get_chat_subscription_patterns = Mock(
            return_value=[
                "chat.say.*",
                "chat.local.*",
                "chat.local.subzone.*",
                "chat.emote.*",
                "chat.pose.*",
                "chat.global",
                "chat.party.*",
                "chat.whisper.player.*",
                "chat.system",
                "chat.admin",
            ]
        )
        self.mock_subject_manager.get_event_subscription_patterns = Mock(
            return_value=[
                "events.player_entered.*",
                "events.player_left.*",
                "events.game_tick",
                "combat.attack.*",
                "combat.npc_attacked.*",
                "combat.npc_action.*",
                "combat.started.*",
                "combat.ended.*",
                "combat.npc_died.*",
                "events.player_mortally_wounded.*",
                "events.player_hp_decay.*",
                "events.player_died.*",
                "events.player_respawned.*",
            ]
        )

        # Create the handler instance
        self.handler = NATSMessageHandler(self.mock_nats_service, subject_manager=self.mock_subject_manager)

        # Mock connection manager
        self.mock_connection_manager = Mock()
        self.mock_connection_manager.broadcast_global = AsyncMock()
        self.mock_connection_manager.broadcast_room_event = AsyncMock()
        self.mock_connection_manager.broadcast_global_event = AsyncMock()
        self.mock_connection_manager.send_personal_message = AsyncMock()
        self.mock_connection_manager._canonical_room_id = Mock(return_value=None)
        self.mock_connection_manager.room_subscriptions = {}
        self.mock_connection_manager.online_players = {}

        # Test data
        self.test_room_id = "arkham_1"
        self.test_player_id = "test_player_123"

    @pytest.mark.asyncio
    async def test_subscribe_to_event_subjects_success(self):
        """Test successful subscription to event subjects."""
        # Mock successful subscription (AsyncMock already set up in setup_method)
        # Ensure it doesn't raise exceptions
        self.mock_nats_service.subscribe = AsyncMock(return_value=None)

        # Call the method
        result = await self.handler.subscribe_to_event_subjects()

        # Verify result
        assert result is True

        # Verify NATS service was called for all event subjects
        expected_calls = [
            "events.player_entered.*",
            "events.player_left.*",
            "events.game_tick",
            "combat.attack.*",
            "combat.npc_attacked.*",
            "combat.npc_action.*",
            "combat.started.*",
            "combat.ended.*",
            "combat.npc_died.*",
            "events.player_mortally_wounded.*",
            "events.player_hp_decay.*",
            "events.player_died.*",
            "events.player_respawned.*",
        ]

        assert self.mock_nats_service.subscribe.call_count == len(expected_calls)

        # Check that all expected subjects were subscribed to
        call_args_list = self.mock_nats_service.subscribe.call_args_list
        subscribed_subjects = [call[0][0] for call in call_args_list]

        for expected_subject in expected_calls:
            assert expected_subject in subscribed_subjects

    @pytest.mark.asyncio
    async def test_subscribe_to_event_subjects_failure(self):
        """Test handling of subscription failure for event subjects."""
        # Mock subscription failure by raising exception
        self.mock_nats_service.subscribe = AsyncMock(side_effect=Exception("NATS connection error"))

        # Call the method
        result = await self.handler.subscribe_to_event_subjects()

        # Verify result
        assert result is False

        # Verify NATS service was called (will fail on first call, but may continue)
        assert self.mock_nats_service.subscribe.call_count > 0

    @pytest.mark.asyncio
    async def test_subscribe_to_event_subjects_exception(self):
        """Test handling of subscription exception for event subjects."""
        # Mock subscription exception
        self.mock_nats_service.subscribe = AsyncMock(side_effect=Exception("NATS connection error"))

        # Call the method
        result = await self.handler.subscribe_to_event_subjects()

        # Verify result
        assert result is False

        # Verify NATS service was called (will fail on first call, but may continue)
        assert self.mock_nats_service.subscribe.call_count > 0

    @pytest.mark.asyncio
    async def test_unsubscribe_from_event_subjects_success(self):
        """Test successful unsubscription from event subjects."""
        # Mock successful unsubscription
        self.mock_nats_service.unsubscribe = AsyncMock(return_value=True)

        # Add some mock subscriptions matching the event patterns
        event_patterns = self.mock_subject_manager.get_event_subscription_patterns()
        self.handler.subscriptions = dict.fromkeys(event_patterns, True)

        # Call the method
        result = await self.handler.unsubscribe_from_event_subjects()

        # Verify result
        assert result is True

        # Verify NATS service was called for all event subjects
        assert self.mock_nats_service.unsubscribe.call_count == len(event_patterns)

    @pytest.mark.asyncio
    async def test_unsubscribe_from_event_subjects_failure(self):
        """Test handling of unsubscription failure for event subjects."""
        # Mock unsubscription failure
        self.mock_nats_service.unsubscribe = AsyncMock(return_value=False)

        # Add some mock subscriptions matching the event patterns
        event_patterns = self.mock_subject_manager.get_event_subscription_patterns()
        # Use first 3 patterns for this test
        self.handler.subscriptions = dict.fromkeys(event_patterns[:3], True)

        # Call the method
        result = await self.handler.unsubscribe_from_event_subjects()

        # Verify result
        assert result is False

        # Verify NATS service was called
        assert self.mock_nats_service.unsubscribe.call_count == 3

    @pytest.mark.asyncio
    async def test_handle_event_message_player_entered(self):
        """Test handling of player_entered event message."""
        # Mock connection manager methods directly
        with patch(
            "server.realtime.nats_message_handler.connection_manager.broadcast_room_event",
            self.mock_connection_manager.broadcast_room_event,
        ):
            # Create test event message
            event_message = {
                "event_type": "player_entered",
                "event_data": {
                    "player_id": self.test_player_id,
                    "room_id": self.test_room_id,
                    "player_name": "TestPlayer",
                    "room_name": "TestRoom",
                },
                "timestamp": "2024-01-01T12:00:00Z",
                "sequence_number": 1,
            }

            # Call the method
            await self.handler._handle_event_message(event_message)

            # Verify connection manager was called
            self.mock_connection_manager.broadcast_room_event.assert_called_once()
            call_args = self.mock_connection_manager.broadcast_room_event.call_args

            # Check event type and room ID
            assert call_args[0][0] == "player_entered"
            assert call_args[0][1] == self.test_room_id
            assert call_args[0][2] == event_message["event_data"]

    @pytest.mark.asyncio
    async def test_handle_event_message_player_left(self):
        """Test handling of player_left event message."""
        # Mock connection manager methods directly
        with patch(
            "server.realtime.nats_message_handler.connection_manager.broadcast_room_event",
            self.mock_connection_manager.broadcast_room_event,
        ):
            # Create test event message
            event_message = {
                "event_type": "player_left",
                "event_data": {
                    "player_id": self.test_player_id,
                    "room_id": self.test_room_id,
                    "player_name": "TestPlayer",
                    "room_name": "TestRoom",
                },
                "timestamp": "2024-01-01T12:00:00Z",
                "sequence_number": 1,
            }

            # Call the method
            await self.handler._handle_event_message(event_message)

            # Verify connection manager was called
            self.mock_connection_manager.broadcast_room_event.assert_called_once()
            call_args = self.mock_connection_manager.broadcast_room_event.call_args

            # Check event type and room ID
            assert call_args[0][0] == "player_left"
            assert call_args[0][1] == self.test_room_id
            assert call_args[0][2] == event_message["event_data"]

    @pytest.mark.asyncio
    async def test_handle_event_message_game_tick(self):
        """Test handling of game_tick event message."""
        # Mock connection manager methods directly
        with patch(
            "server.realtime.nats_message_handler.connection_manager.broadcast_global_event",
            self.mock_connection_manager.broadcast_global_event,
        ):
            # Create test event message
            event_message = {
                "event_type": "game_tick",
                "event_data": {
                    "tick_number": 1,
                    "server_time": "2024-01-01T12:00:00Z",
                },
                "timestamp": "2024-01-01T12:00:00Z",
                "sequence_number": 1,
            }

            # Call the method
            await self.handler._handle_event_message(event_message)

            # Verify connection manager was called
            self.mock_connection_manager.broadcast_global_event.assert_called_once()
            call_args = self.mock_connection_manager.broadcast_global_event.call_args

            # Check event type and data
            assert call_args[0][0] == "game_tick"
            assert call_args[0][1] == event_message["event_data"]

    @pytest.mark.asyncio
    async def test_handle_event_message_unknown_event_type(self):
        """Test handling of unknown event type."""
        # Mock connection manager
        with patch("server.realtime.nats_message_handler.connection_manager", self.mock_connection_manager):
            # Create test event message with unknown event type
            event_message = {
                "event_type": "unknown_event",
                "event_data": {"test": "data"},
                "timestamp": "2024-01-01T12:00:00Z",
                "sequence_number": 1,
            }

            # Call the method
            await self.handler._handle_event_message(event_message)

            # Verify connection manager was not called
            self.mock_connection_manager.broadcast_room_event.assert_not_called()
            self.mock_connection_manager.broadcast_global_event.assert_not_called()

    @pytest.mark.asyncio
    async def test_handle_event_message_missing_data(self):
        """Test handling of event message with missing data."""
        # Mock connection manager
        with patch("server.realtime.nats_message_handler.connection_manager", self.mock_connection_manager):
            # Create test event message with missing data
            event_message = {
                "event_type": "player_entered",
                "timestamp": "2024-01-01T12:00:00Z",
                "sequence_number": 1,
            }

            # Call the method
            await self.handler._handle_event_message(event_message)

            # Verify connection manager was not called
            self.mock_connection_manager.broadcast_room_event.assert_not_called()

    @pytest.mark.asyncio
    async def test_handle_event_message_exception(self):
        """Test handling of exception in event message processing."""
        # Mock connection manager to raise exception
        self.mock_connection_manager.broadcast_room_event.side_effect = Exception("Broadcast error")

        with patch(
            "server.realtime.nats_message_handler.connection_manager.broadcast_room_event",
            self.mock_connection_manager.broadcast_room_event,
        ):
            # Create test event message
            event_message = {
                "event_type": "player_entered",
                "event_data": {
                    "player_id": self.test_player_id,
                    "room_id": self.test_room_id,
                    "player_name": "TestPlayer",
                    "room_name": "TestRoom",
                },
                "timestamp": "2024-01-01T12:00:00Z",
                "sequence_number": 1,
            }

            # Call the method (should not raise exception)
            await self.handler._handle_event_message(event_message)

            # Verify connection manager was called
            self.mock_connection_manager.broadcast_room_event.assert_called_once()

    @pytest.mark.asyncio
    async def test_start_with_event_subscriptions(self):
        """Test starting handler with event subscriptions enabled."""
        # Mock successful subscription
        self.mock_nats_service.subscribe.return_value = True

        # Call the method with event subscriptions enabled
        result = await self.handler.start(enable_event_subscriptions=True)

        # Verify result
        assert result is True

        # Verify both chat and event subjects were subscribed to
        call_args_list = self.mock_nats_service.subscribe.call_args_list
        subscribed_subjects = [call[0][0] for call in call_args_list]

        # Check chat subjects
        assert "chat.say.*" in subscribed_subjects
        assert "chat.global" in subscribed_subjects

        # Check event subjects
        assert "events.player_entered.*" in subscribed_subjects
        assert "events.player_left.*" in subscribed_subjects
        assert "events.game_tick" in subscribed_subjects

    @pytest.mark.asyncio
    async def test_start_without_event_subscriptions(self):
        """Test starting handler without event subscriptions."""
        # Mock successful subscription
        self.mock_nats_service.subscribe.return_value = True

        # Call the method without event subscriptions
        result = await self.handler.start(enable_event_subscriptions=False)

        # Verify result
        assert result is True

        # Verify only chat subjects were subscribed to
        call_args_list = self.mock_nats_service.subscribe.call_args_list
        subscribed_subjects = [call[0][0] for call in call_args_list]

        # Check chat subjects
        assert "chat.say.*" in subscribed_subjects
        assert "chat.global" in subscribed_subjects

        # Check event subjects are not present
        assert "events.player_entered.*" not in subscribed_subjects
        assert "events.player_left.*" not in subscribed_subjects
        assert "events.game_tick" not in subscribed_subjects

    @pytest.mark.asyncio
    async def test_stop_with_event_subscriptions(self):
        """Test stopping handler with event subscriptions."""
        # Add some mock subscriptions
        self.handler.subscriptions = {
            "chat.say.*": True,
            "chat.global": True,
            "events.player_entered.*": True,
            "events.player_left.*": True,
            "events.game_tick": True,
        }

        # Mock successful unsubscription
        self.mock_nats_service.unsubscribe.return_value = True

        # Call the method
        result = await self.handler.stop()

        # Verify result
        assert result is True

        # Verify all subscriptions were unsubscribed from
        assert self.mock_nats_service.unsubscribe.call_count == 5

    def test_get_event_subscription_count(self):
        """Test getting count of event subscriptions."""
        # Add some mock subscriptions
        self.handler.subscriptions = {
            "chat.say.*": True,
            "chat.global": True,
            "events.player_entered.*": True,
            "events.player_left.*": True,
            "events.game_tick": True,
        }

        # Call the method
        count = self.handler.get_event_subscription_count()

        # Verify count
        assert count == 3

    def test_get_event_subscription_count_no_events(self):
        """Test getting count when no event subscriptions exist."""
        # Add only chat subscriptions
        self.handler.subscriptions = {
            "chat.say.*": True,
            "chat.global": True,
        }

        # Call the method
        count = self.handler.get_event_subscription_count()

        # Verify count
        assert count == 0

    def test_is_event_subscription_active(self):
        """Test checking if event subscription is active."""
        # Add some mock subscriptions
        self.handler.subscriptions = {
            "events.player_entered.*": True,
            "events.game_tick": True,
        }

        # Test active subscription
        assert self.handler.is_event_subscription_active("events.player_entered.*") is True
        assert self.handler.is_event_subscription_active("events.game_tick") is True

        # Test inactive subscription
        assert self.handler.is_event_subscription_active("events.player_left.*") is False
        assert self.handler.is_event_subscription_active("chat.say.*") is False


# ============================================================================
# Tests merged from test_nats_message_handler_subzone_legacy.py
# ============================================================================


"""
Tests for NATS message handler sub-zone subscription functionality.

These tests cover the dynamic subscription management for local channels
when players move between sub-zones.
"""


class TestNATSMessageHandlerSubZoneSubscriptions:
    """Test sub-zone subscription management in NATS message handler."""

    @pytest.fixture
    def mock_nats_service(self):
        """Create a mock NATS service."""
        mock_service = AsyncMock(spec=NATSService)
        mock_service.subscribe = AsyncMock(return_value=True)
        mock_service.unsubscribe = AsyncMock(return_value=True)
        return mock_service

    @pytest.fixture
    def nats_handler(self, mock_nats_service):
        """Create NATS message handler with mock service."""
        # Create mock subject manager for this test
        mock_subject_manager = Mock()
        mock_subject_manager.get_chat_subscription_patterns = Mock(return_value=[])
        mock_subject_manager.get_event_subscription_patterns = Mock(return_value=[])

        # Mock build_subject to return expected subject strings
        def build_subject_mock(subject_type, **kwargs):
            """Build subject string from type and kwargs."""
            if subject_type == "chat_local_subzone" and "subzone" in kwargs:
                return f"chat.local.subzone.{kwargs['subzone']}"
            elif subject_type == "chat_say_room" and "room_id" in kwargs:
                return f"chat.say.{kwargs['room_id']}"
            return f"{subject_type}.{'.'.join(str(v) for v in kwargs.values())}"

        mock_subject_manager.build_subject = Mock(side_effect=build_subject_mock)

        handler = NATSMessageHandler(mock_nats_service, subject_manager=mock_subject_manager)
        # Initialize subscriptions dict to track subscribed subjects
        handler.subscriptions = {}

        # Create mock functions that track calls
        handler._subscribe_calls = []
        handler._unsubscribe_calls = []

        async def mock_subscribe(subject):
            handler._subscribe_calls.append(subject)
            handler.subscriptions[subject] = True
            return True

        async def mock_unsubscribe(subject):
            handler._unsubscribe_calls.append(subject)
            if subject in handler.subscriptions:
                del handler.subscriptions[subject]
            return True

        handler._subscribe_to_subject = mock_subscribe
        handler._unsubscribe_from_subject = mock_unsubscribe
        return handler

    @pytest.mark.asyncio
    async def test_subscribe_to_subzone_new_subscription(self, nats_handler):
        """Test subscribing to a new sub-zone."""
        subzone = "docks"

        result = await nats_handler.subscribe_to_subzone(subzone)

        assert result is True
        assert subzone in nats_handler.subzone_subscriptions
        assert nats_handler.subzone_subscriptions[subzone] == 1
        assert "chat.local.subzone.docks" in nats_handler._subscribe_calls

    @pytest.mark.asyncio
    async def test_subscribe_to_subzone_existing_subscription(self, nats_handler):
        """Test subscribing to an already subscribed sub-zone."""
        subzone = "docks"

        # First subscription
        result1 = await nats_handler.subscribe_to_subzone(subzone)
        assert result1 is True
        assert nats_handler.subzone_subscriptions[subzone] == 1

        # Second subscription (should increase count)
        result2 = await nats_handler.subscribe_to_subzone(subzone)
        assert result2 is True
        assert nats_handler.subzone_subscriptions[subzone] == 2

        # Should only call _subscribe_to_subject once
        assert nats_handler._subscribe_calls.count("chat.local.subzone.docks") == 1

    @pytest.mark.asyncio
    async def test_subscribe_to_subzone_failure(self, nats_handler):
        """Test subscribing to sub-zone when NATS subscription fails."""
        subzone = "docks"

        # Override the mock to return False
        async def mock_subscribe_fail(subject):
            return False

        nats_handler._subscribe_to_subject = mock_subscribe_fail

        result = await nats_handler.subscribe_to_subzone(subzone)

        assert result is False
        assert subzone not in nats_handler.subzone_subscriptions

    @pytest.mark.asyncio
    async def test_unsubscribe_from_subzone_decrease_count(self, nats_handler):
        """Test unsubscribing from sub-zone decreases count but doesn't unsubscribe from NATS."""
        subzone = "docks"

        # Subscribe twice
        await nats_handler.subscribe_to_subzone(subzone)
        await nats_handler.subscribe_to_subzone(subzone)
        assert nats_handler.subzone_subscriptions[subzone] == 2

        # Unsubscribe once
        result = await nats_handler.unsubscribe_from_subzone(subzone)

        assert result is True
        assert nats_handler.subzone_subscriptions[subzone] == 1
        # Should not call _unsubscribe_from_subject yet
        assert "chat.local.subzone.docks" not in nats_handler._unsubscribe_calls

    @pytest.mark.asyncio
    async def test_unsubscribe_from_subzone_final_unsubscribe(self, nats_handler):
        """Test unsubscribing from sub-zone when count reaches zero."""
        subzone = "docks"

        # Subscribe once
        await nats_handler.subscribe_to_subzone(subzone)
        assert nats_handler.subzone_subscriptions[subzone] == 1

        # Unsubscribe (should remove from NATS)
        result = await nats_handler.unsubscribe_from_subzone(subzone)

        assert result is True
        assert subzone not in nats_handler.subzone_subscriptions
        assert "chat.local.subzone.docks" in nats_handler._unsubscribe_calls

    @pytest.mark.asyncio
    async def test_unsubscribe_from_subzone_not_subscribed(self, nats_handler):
        """Test unsubscribing from a sub-zone that's not subscribed."""
        subzone = "docks"

        result = await nats_handler.unsubscribe_from_subzone(subzone)

        assert result is False
        assert len(nats_handler._unsubscribe_calls) == 0

    @pytest.mark.asyncio
    async def test_unsubscribe_from_subzone_nats_failure(self, nats_handler):
        """Test unsubscribing from sub-zone when NATS unsubscribe fails."""
        subzone = "docks"

        # Override the mock to return False
        async def mock_unsubscribe_fail(subject):
            return False

        nats_handler._unsubscribe_from_subject = mock_unsubscribe_fail

        # Subscribe once
        await nats_handler.subscribe_to_subzone(subzone)

        # Try to unsubscribe
        result = await nats_handler.unsubscribe_from_subzone(subzone)

        assert result is False
        # Should still be in subscriptions since NATS unsubscribe failed
        assert subzone in nats_handler.subzone_subscriptions

    def test_track_player_subzone_subscription_new_player(self, nats_handler):
        """Test tracking a new player's sub-zone subscription."""
        player_id = "player1"
        subzone = "docks"

        nats_handler.track_player_subzone_subscription(player_id, subzone)

        assert nats_handler.player_subzone_subscriptions[player_id] == subzone

    def test_track_player_subzone_subscription_same_subzone(self, nats_handler):
        """Test tracking player movement within same sub-zone."""
        player_id = "player1"
        subzone = "docks"

        # Initial subscription
        nats_handler.track_player_subzone_subscription(player_id, subzone)
        assert nats_handler.player_subzone_subscriptions[player_id] == subzone

        # Move within same sub-zone
        nats_handler.track_player_subzone_subscription(player_id, subzone)
        assert nats_handler.player_subzone_subscriptions[player_id] == subzone

    def test_track_player_subzone_subscription_different_subzone(self, nats_handler):
        """Test tracking player movement to different sub-zone."""
        player_id = "player1"
        old_subzone = "docks"
        new_subzone = "warehouse"

        # Subscribe to old sub-zone
        nats_handler.subzone_subscriptions[old_subzone] = 2

        # Initial subscription
        nats_handler.track_player_subzone_subscription(player_id, old_subzone)
        assert nats_handler.player_subzone_subscriptions[player_id] == old_subzone
        assert nats_handler.subzone_subscriptions[old_subzone] == 2

        # Move to different sub-zone
        nats_handler.track_player_subzone_subscription(player_id, new_subzone)
        assert nats_handler.player_subzone_subscriptions[player_id] == new_subzone
        # Should decrease count for old sub-zone
        assert nats_handler.subzone_subscriptions[old_subzone] == 1

    def test_get_players_in_subzone(self, nats_handler):
        """Test getting players in a specific sub-zone."""
        # Set up player subscriptions
        nats_handler.player_subzone_subscriptions = {
            "player1": "docks",
            "player2": "docks",
            "player3": "warehouse",
            "player4": "docks",
        }

        players = nats_handler.get_players_in_subzone("docks")

        assert set(players) == {"player1", "player2", "player4"}

    def test_get_players_in_subzone_empty(self, nats_handler):
        """Test getting players in a sub-zone with no players."""
        nats_handler.player_subzone_subscriptions = {"player1": "docks", "player2": "warehouse"}

        players = nats_handler.get_players_in_subzone("northside")

        assert players == []

    @pytest.mark.asyncio
    async def test_handle_player_movement_same_subzone(self, nats_handler):
        """Test handling player movement within same sub-zone."""
        player_id = "player1"
        old_room_id = "earth_arkham_docks_warehouse_1"
        new_room_id = "earth_arkham_docks_warehouse_2"

        # Mock sub-zone extraction
        with patch("server.utils.room_utils.extract_subzone_from_room_id") as mock_extract:
            mock_extract.side_effect = lambda x: "docks" if "docks" in x else None

            await nats_handler.handle_player_movement(player_id, old_room_id, new_room_id)

            # Should not subscribe/unsubscribe since same sub-zone
            assert len(nats_handler._subscribe_calls) == 0
            assert len(nats_handler._unsubscribe_calls) == 0

            # Should track the subscription
            assert nats_handler.player_subzone_subscriptions[player_id] == "docks"

    @pytest.mark.asyncio
    async def test_handle_player_movement_different_subzone(self, nats_handler):
        """Test handling player movement between different sub-zones."""
        player_id = "player1"
        old_room_id = "earth_arkham_docks_warehouse_1"
        new_room_id = "earth_arkham_northside_mansion_1"

        # Set up initial state - player is already in docks sub-zone
        nats_handler.subzone_subscriptions["docks"] = 1
        nats_handler.player_subzone_subscriptions[player_id] = "docks"
        nats_handler.subscriptions["chat.local.subzone.docks"] = True

        # Mock sub-zone extraction
        with patch("server.utils.room_utils.extract_subzone_from_room_id") as mock_extract:
            mock_extract.side_effect = lambda x: "docks" if "docks" in x else "northside"

            await nats_handler.handle_player_movement(player_id, old_room_id, new_room_id)

            # Should unsubscribe from old sub-zone and subscribe to new one
            assert "chat.local.subzone.docks" in nats_handler._unsubscribe_calls
            assert "chat.local.subzone.northside" in nats_handler._subscribe_calls

            # Should track the new subscription
            assert nats_handler.player_subzone_subscriptions[player_id] == "northside"

    @pytest.mark.asyncio
    async def test_handle_player_movement_from_no_room(self, nats_handler):
        """Test handling player movement from no room to a room."""
        player_id = "player1"
        old_room_id = None
        new_room_id = "earth_arkham_docks_warehouse_1"

        # Mock sub-zone extraction
        with patch("server.utils.room_utils.extract_subzone_from_room_id") as mock_extract:
            mock_extract.return_value = "docks"

            await nats_handler.handle_player_movement(player_id, old_room_id, new_room_id)

            # Should only subscribe to new sub-zone
            assert "chat.local.subzone.docks" in nats_handler._subscribe_calls
            assert len(nats_handler._unsubscribe_calls) == 0

            # Should track the subscription
            assert nats_handler.player_subzone_subscriptions[player_id] == "docks"

    @pytest.mark.asyncio
    async def test_handle_player_movement_to_no_room(self, nats_handler):
        """Test handling player movement from a room to no room."""
        player_id = "player1"
        old_room_id = "earth_arkham_docks_warehouse_1"
        new_room_id = None

        # Set up initial state - player is already in docks sub-zone
        nats_handler.subzone_subscriptions["docks"] = 1
        nats_handler.player_subzone_subscriptions[player_id] = "docks"
        nats_handler.subscriptions["chat.local.subzone.docks"] = True

        # Mock sub-zone extraction
        with patch("server.utils.room_utils.extract_subzone_from_room_id") as mock_extract:
            mock_extract.return_value = "docks"

            await nats_handler.handle_player_movement(player_id, old_room_id, new_room_id)

            # Should only unsubscribe from old sub-zone
            assert "chat.local.subzone.docks" in nats_handler._unsubscribe_calls
            assert len(nats_handler._subscribe_calls) == 0

    @pytest.mark.asyncio
    async def test_cleanup_empty_subzone_subscriptions(self, nats_handler):
        """Test cleaning up empty sub-zone subscriptions."""
        # Set up sub-zones with different states
        nats_handler.subzone_subscriptions = {
            "docks": 0,  # Empty, should be cleaned up
            "warehouse": 1,  # Has players, should not be cleaned up
            "northside": -1,  # Negative count, should be cleaned up
        }

        # Set up player subscriptions
        nats_handler.player_subzone_subscriptions = {
            "player1": "warehouse"  # Only player is in warehouse
        }

        await nats_handler.cleanup_empty_subzone_subscriptions()

        # Should unsubscribe from empty sub-zones
        assert len(nats_handler._unsubscribe_calls) == 2
        assert "chat.local.subzone.docks" in nats_handler._unsubscribe_calls
        assert "chat.local.subzone.northside" in nats_handler._unsubscribe_calls

        # Should not unsubscribe from warehouse (has players)
        assert "chat.local.subzone.warehouse" not in nats_handler._unsubscribe_calls

    @pytest.mark.asyncio
    async def test_cleanup_empty_subzone_subscriptions_no_cleanup_needed(self, nats_handler):
        """Test cleanup when no sub-zones need cleaning up."""
        # Set up sub-zones with active players
        nats_handler.subzone_subscriptions = {"docks": 1, "warehouse": 2}

        nats_handler.player_subzone_subscriptions = {"player1": "docks", "player2": "warehouse", "player3": "warehouse"}

        await nats_handler.cleanup_empty_subzone_subscriptions()

        # Should not unsubscribe from any sub-zones
        assert len(nats_handler._unsubscribe_calls) == 0

    @pytest.mark.asyncio
    async def test_subscribe_to_subzone_exception_handling(self, nats_handler):
        """Test exception handling in subscribe_to_subzone."""
        subzone = "docks"

        # Override the mock to raise exception
        async def mock_subscribe_exception(subject):
            raise Exception("NATS error")

        nats_handler._subscribe_to_subject = mock_subscribe_exception

        result = await nats_handler.subscribe_to_subzone(subzone)

        assert result is False
        assert subzone not in nats_handler.subzone_subscriptions

    @pytest.mark.asyncio
    async def test_unsubscribe_from_subzone_exception_handling(self, nats_handler):
        """Test exception handling in unsubscribe_from_subzone."""
        subzone = "docks"
        nats_handler.subzone_subscriptions[subzone] = 1

        # Override the mock to raise exception
        async def mock_unsubscribe_exception(subject):
            raise Exception("NATS error")

        nats_handler._unsubscribe_from_subject = mock_unsubscribe_exception

        result = await nats_handler.unsubscribe_from_subzone(subzone)

        assert result is False
        # Should still be in subscriptions since unsubscribe failed
        assert subzone in nats_handler.subzone_subscriptions

    def test_track_player_subzone_subscription_exception_handling(self, nats_handler):
        """Test exception handling in track_player_subzone_subscription."""
        player_id = "player1"
        subzone = "docks"

        # Cause an exception by making subzone_subscriptions a non-dict
        nats_handler.subzone_subscriptions = None

        # Should not raise exception
        nats_handler.track_player_subzone_subscription(player_id, subzone)

        # Should still track the player subscription
        assert nats_handler.player_subzone_subscriptions[player_id] == subzone

    def test_get_players_in_subzone_exception_handling(self, nats_handler):
        """Test exception handling in get_players_in_subzone."""
        subzone = "docks"

        # Cause an exception by making player_subzone_subscriptions a non-dict
        nats_handler.player_subzone_subscriptions = None

        players = nats_handler.get_players_in_subzone(subzone)

        assert players == []

    @pytest.mark.asyncio
    async def test_handle_player_movement_exception_handling(self, nats_handler):
        """Test exception handling in handle_player_movement."""
        player_id = "player1"
        old_room_id = "earth_arkham_docks_warehouse_1"
        new_room_id = "earth_arkham_northside_mansion_1"

        # Mock sub-zone extraction to raise exception
        with patch("server.utils.room_utils.extract_subzone_from_room_id") as mock_extract:
            mock_extract.side_effect = Exception("Room parsing error")

            # Should not raise exception
            await nats_handler.handle_player_movement(player_id, old_room_id, new_room_id)

            # Should not make any subscription calls
            assert len(nats_handler._subscribe_calls) == 0
            assert len(nats_handler._unsubscribe_calls) == 0

    @pytest.mark.asyncio
    async def test_cleanup_empty_subzone_subscriptions_exception_handling(self, nats_handler):
        """Test exception handling in cleanup_empty_subzone_subscriptions."""
        nats_handler.subzone_subscriptions = {"docks": 0}

        # Override the mock to raise exception
        async def mock_unsubscribe_exception(subject):
            raise Exception("NATS error")

        nats_handler._unsubscribe_from_subject = mock_unsubscribe_exception

        # Should not raise exception
        await nats_handler.cleanup_empty_subzone_subscriptions()

        # Should still be in subscriptions since cleanup failed
        assert "docks" in nats_handler.subzone_subscriptions
