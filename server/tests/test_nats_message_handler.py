"""
Tests for the NATS message handler functionality.

This module tests the NATSMessageHandler class which handles incoming NATS messages
and broadcasts them to WebSocket clients based on channel type and room subscriptions.
"""

import uuid
from datetime import datetime
from unittest.mock import AsyncMock, Mock, patch

import pytest

from ..realtime.nats_message_handler import NATSMessageHandler, get_nats_message_handler


class TestNATSMessageHandler:
    """Test cases for NATSMessageHandler."""

    def setup_method(self):
        """Set up test fixtures."""
        # Create a mock NATS service
        self.mock_nats_service = Mock()
        self.mock_nats_service.subscribe = AsyncMock()
        self.mock_nats_service.unsubscribe = AsyncMock()

        # Create the handler instance
        self.handler = NATSMessageHandler(self.mock_nats_service)

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
            "chat.whisper.*",
            "chat.system",
            "chat.admin",
        ]

        expected_event_subjects = [
            "events.player_entered.*",
            "events.player_left.*",
            "events.game_tick",
        ]

        # Verify chat subscriptions
        for subject in expected_chat_subjects:
            assert subject in self.handler.subscriptions

        # Verify event subscriptions
        for subject in expected_event_subjects:
            assert subject in self.handler.subscriptions

        # Verify total count
        assert len(self.handler.subscriptions) == len(expected_chat_subjects) + len(expected_event_subjects)

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
        message_data = {
            "channel": "say",
            "room_id": "room_001",
            "sender_id": "player_001",
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
                assert call_args[5] == "player_001"  # sender_id

    @pytest.mark.asyncio
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
                await self.handler._broadcast_by_channel_type("say", chat_event, "room_001", None, None, "player_001")

                mock_room_broadcast.assert_called_once_with("room_001", chat_event, "player_001", "say")

    @pytest.mark.asyncio
    async def test_broadcast_by_channel_type_local(self):
        """Test broadcasting local messages."""
        chat_event = {"event_type": "chat_message", "data": {"message": "Hello"}}

        with patch("server.realtime.nats_message_handler.connection_manager", self.mock_connection_manager):
            with patch.object(
                self.handler, "_broadcast_to_room_with_filtering", new_callable=AsyncMock
            ) as mock_room_broadcast:
                await self.handler._broadcast_by_channel_type("local", chat_event, "room_001", None, None, "player_001")

                mock_room_broadcast.assert_called_once_with("room_001", chat_event, "player_001", "local")

    @pytest.mark.asyncio
    async def test_broadcast_by_channel_type_global(self):
        """Test broadcasting global messages."""
        chat_event = {"event_type": "chat_message", "data": {"message": "Hello"}}

        with patch("server.realtime.connection_manager.connection_manager", self.mock_connection_manager):
            await self.handler._broadcast_by_channel_type("global", chat_event, None, None, None, "player_001")

            self.mock_connection_manager.broadcast_global.assert_called_once_with(
                chat_event, exclude_player="player_001"
            )

    @pytest.mark.asyncio
    async def test_broadcast_by_channel_type_whisper(self):
        """Test broadcasting whisper messages."""
        chat_event = {"event_type": "chat_message", "data": {"message": "Hello"}}

        with patch("server.realtime.connection_manager.connection_manager", self.mock_connection_manager):
            await self.handler._broadcast_by_channel_type(
                "whisper", chat_event, None, None, "target_player", "player_001"
            )

            self.mock_connection_manager.send_personal_message.assert_called_once_with("target_player", chat_event)

    @pytest.mark.asyncio
    async def test_broadcast_by_channel_type_system(self):
        """Test broadcasting system messages."""
        chat_event = {"event_type": "chat_message", "data": {"message": "Hello"}}

        with patch("server.realtime.connection_manager.connection_manager", self.mock_connection_manager):
            await self.handler._broadcast_by_channel_type("system", chat_event, None, None, None, "player_001")

            self.mock_connection_manager.broadcast_global.assert_called_once_with(
                chat_event, exclude_player="player_001"
            )

    @pytest.mark.asyncio
    async def test_broadcast_by_channel_type_admin(self):
        """Test broadcasting admin messages."""
        chat_event = {"event_type": "chat_message", "data": {"message": "Hello"}}

        with patch("server.realtime.connection_manager.connection_manager", self.mock_connection_manager):
            await self.handler._broadcast_by_channel_type("admin", chat_event, None, None, None, "player_001")

            self.mock_connection_manager.broadcast_global.assert_called_once_with(
                chat_event, exclude_player="player_001"
            )

    @pytest.mark.asyncio
    async def test_broadcast_by_channel_type_unknown(self):
        """Test broadcasting unknown channel type."""
        chat_event = {"event_type": "chat_message", "data": {"message": "Hello"}}

        with patch("server.realtime.connection_manager.connection_manager", self.mock_connection_manager):
            await self.handler._broadcast_by_channel_type("unknown", chat_event, None, None, None, "player_001")

            # Should not call any broadcast methods
            self.mock_connection_manager.broadcast_global.assert_not_called()
            self.mock_connection_manager.send_personal_message.assert_not_called()

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

        # Set up connection manager mocks
        self.mock_connection_manager.room_subscriptions = {"room_001": {"player_001", "player_002", "player_003"}}
        self.mock_connection_manager.online_players = {
            "player_001": {"current_room_id": "room_001"},
            "player_002": {"current_room_id": "room_001"},
            "player_003": {"current_room_id": "room_002"},  # Different room
        }

        with patch("server.realtime.nats_message_handler.connection_manager", self.mock_connection_manager):
            with patch.object(
                self.handler, "_is_player_in_room", side_effect=lambda p, r: p in ["player_001", "player_002"]
            ):
                with patch.object(self.handler, "_is_player_muted_by_receiver", return_value=False):
                    await self.handler._broadcast_to_room_with_filtering("room_001", chat_event, "player_001", "say")

                    # Should send to player_002 (player_001 is sender, player_003 is in different room)
                    assert self.mock_connection_manager.send_personal_message.call_count == 1
                    self.mock_connection_manager.send_personal_message.assert_called_with("player_002", chat_event)

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

        with patch("server.services.user_manager.UserManager", return_value=mock_user_manager):
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
        with patch.object(self.handler, "_subscribe_to_subject", new_callable=AsyncMock) as mock_subscribe:
            await self.handler.subscribe_to_room("room_001")

            # Should subscribe to room-specific subjects
            expected_calls = [(("chat.say.room_001",),), (("chat.local.room_001",),)]
            assert mock_subscribe.call_args_list == expected_calls

    @pytest.mark.asyncio
    async def test_unsubscribe_from_room(self):
        """Test unsubscribing from room-specific subjects."""
        # Set up existing subscriptions
        self.handler.subscriptions = {"chat.say.room_001": True, "chat.local.room_001": True, "chat.global": True}

        with patch.object(self.handler, "_unsubscribe_from_subject", new_callable=AsyncMock) as mock_unsubscribe:
            await self.handler.unsubscribe_from_room("room_001")

            # Should unsubscribe from room-specific subjects
            expected_calls = [(("chat.say.room_001",),), (("chat.local.room_001",),)]
            assert mock_unsubscribe.call_args_list == expected_calls

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


class TestNATSMessageHandlerGlobal:
    """Test cases for global NATS message handler functions."""

    def test_get_nats_message_handler_creates_new_instance(self):
        """Test getting NATS message handler creates new instance."""
        mock_nats_service = Mock()

        # Reset global instance
        import server.realtime.nats_message_handler as nats_module

        nats_module.nats_message_handler = None

        handler = get_nats_message_handler(mock_nats_service)

        assert handler is not None
        assert isinstance(handler, NATSMessageHandler)
        assert handler.nats_service == mock_nats_service

    def test_get_nats_message_handler_returns_existing_instance(self):
        """Test getting NATS message handler returns existing instance."""
        mock_nats_service = Mock()

        # Create initial instance
        handler1 = get_nats_message_handler(mock_nats_service)

        # Get again without nats_service
        handler2 = get_nats_message_handler()

        assert handler1 is handler2

    def test_get_nats_message_handler_no_service_returns_none(self):
        """Test getting NATS message handler without service returns None."""
        # Reset global instance
        import server.realtime.nats_message_handler as nats_module

        nats_module.nats_message_handler = None

        handler = get_nats_message_handler()

        assert handler is None


class TestNATSMessageHandlerEventSubscription:
    """Test cases for NATSMessageHandler event subscription capabilities."""

    def setup_method(self):
        """Set up test fixtures."""
        # Create a mock NATS service
        self.mock_nats_service = Mock()
        self.mock_nats_service.subscribe = AsyncMock()
        self.mock_nats_service.unsubscribe = AsyncMock()

        # Create the handler instance
        self.handler = NATSMessageHandler(self.mock_nats_service)

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
        # Mock successful subscription
        self.mock_nats_service.subscribe.return_value = True

        # Call the method
        result = await self.handler.subscribe_to_event_subjects()

        # Verify result
        assert result is True

        # Verify NATS service was called for all event subjects
        expected_calls = [
            "events.player_entered.*",
            "events.player_left.*",
            "events.game_tick",
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
        # Mock subscription failure
        self.mock_nats_service.subscribe.return_value = False

        # Call the method
        result = await self.handler.subscribe_to_event_subjects()

        # Verify result
        assert result is False

        # Verify NATS service was called
        assert self.mock_nats_service.subscribe.call_count == 3

    @pytest.mark.asyncio
    async def test_subscribe_to_event_subjects_exception(self):
        """Test handling of subscription exception for event subjects."""
        # Mock subscription exception
        self.mock_nats_service.subscribe.side_effect = Exception("NATS connection error")

        # Call the method
        result = await self.handler.subscribe_to_event_subjects()

        # Verify result
        assert result is False

        # Verify NATS service was called
        assert self.mock_nats_service.subscribe.call_count == 3

    @pytest.mark.asyncio
    async def test_unsubscribe_from_event_subjects_success(self):
        """Test successful unsubscription from event subjects."""
        # Mock successful unsubscription
        self.mock_nats_service.unsubscribe.return_value = True

        # Add some mock subscriptions
        self.handler.subscriptions = {
            "events.player_entered.*": True,
            "events.player_left.*": True,
            "events.game_tick": True,
        }

        # Call the method
        result = await self.handler.unsubscribe_from_event_subjects()

        # Verify result
        assert result is True

        # Verify NATS service was called for all event subjects
        assert self.mock_nats_service.unsubscribe.call_count == 3

    @pytest.mark.asyncio
    async def test_unsubscribe_from_event_subjects_failure(self):
        """Test handling of unsubscription failure for event subjects."""
        # Mock unsubscription failure
        self.mock_nats_service.unsubscribe.return_value = False

        # Add some mock subscriptions
        self.handler.subscriptions = {
            "events.player_entered.*": True,
            "events.player_left.*": True,
            "events.game_tick": True,
        }

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
                "data": {
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
            assert call_args[0][2] == event_message["data"]

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
                "data": {
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
            assert call_args[0][2] == event_message["data"]

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
                "data": {
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
            assert call_args[0][1] == event_message["data"]

    @pytest.mark.asyncio
    async def test_handle_event_message_unknown_event_type(self):
        """Test handling of unknown event type."""
        # Mock connection manager
        with patch("server.realtime.nats_message_handler.connection_manager", self.mock_connection_manager):
            # Create test event message with unknown event type
            event_message = {
                "event_type": "unknown_event",
                "data": {"test": "data"},
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
                "data": {
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
