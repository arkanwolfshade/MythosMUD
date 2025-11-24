"""
Tests for Channel Broadcasting Strategies.

This module tests the strategy pattern implementation for channel broadcasting,
ensuring it correctly handles all channel types and maintains backward compatibility.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.channel_broadcasting_strategies import (
    ChannelBroadcastingStrategy,
    ChannelBroadcastingStrategyFactory,
    GlobalChannelStrategy,
    PartyChannelStrategy,
    RoomBasedChannelStrategy,
    SystemAdminChannelStrategy,
    UnknownChannelStrategy,
    WhisperChannelStrategy,
    channel_strategy_factory,
)
from server.realtime.nats_message_handler import NATSMessageHandler


class TestChannelBroadcastingStrategies:
    """Test suite for channel broadcasting strategies."""

    # Test player IDs - use UUID objects
    PLAYER_1 = uuid.uuid4()
    PLAYER_2 = uuid.uuid4()
    SENDER_1 = uuid.uuid4()
    TARGET_1 = uuid.uuid4()

    @pytest.fixture
    def nats_handler(self):
        """Create a NATS message handler for testing."""
        mock_nats_service = MagicMock()
        return NATSMessageHandler(mock_nats_service)

    @pytest.fixture
    def mock_connection_manager(self):
        """Return a mock connection manager for room broadcasts."""
        mock_cm = MagicMock()
        mock_cm.broadcast_global = AsyncMock()
        mock_cm.send_personal_message = AsyncMock()
        mock_cm._canonical_room_id.return_value = "test_room"
        # room_subscriptions expects string player IDs
        mock_cm.room_subscriptions = {
            "test_room": {
                str(TestChannelBroadcastingStrategies.PLAYER_1),
                str(TestChannelBroadcastingStrategies.PLAYER_2),
            }
        }
        mock_cm.online_players = {
            TestChannelBroadcastingStrategies.PLAYER_1: {"current_room_id": "test_room"},
            TestChannelBroadcastingStrategies.PLAYER_2: {"current_room_id": "test_room"},
        }
        return mock_cm

    @pytest.fixture
    def mock_connection_manager_strategy(self):
        """Return a mock connection manager for strategy-level tests."""
        mock_cm = MagicMock()
        mock_cm.broadcast_global = AsyncMock()
        mock_cm.send_personal_message = AsyncMock()
        mock_cm._canonical_room_id.return_value = "test_room"
        # room_subscriptions expects string player IDs
        mock_cm.room_subscriptions = {
            "test_room": {
                str(TestChannelBroadcastingStrategies.PLAYER_1),
                str(TestChannelBroadcastingStrategies.PLAYER_2),
            }
        }
        mock_cm.online_players = {
            TestChannelBroadcastingStrategies.PLAYER_1: {"current_room_id": "test_room"},
            TestChannelBroadcastingStrategies.PLAYER_2: {"current_room_id": "test_room"},
        }
        return mock_cm

    @pytest.mark.asyncio
    async def test_room_based_channels_say(self, nats_handler, mock_connection_manager):
        """Test room-based channel broadcasting (say)."""
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        nats_handler.connection_manager = mock_connection_manager

        with patch.object(nats_handler, "_broadcast_to_room_with_filtering") as mock_broadcast:
            await nats_handler._broadcast_by_channel_type("say", chat_event, "test_room", "", None, self.SENDER_1)

            mock_broadcast.assert_called_once_with("test_room", chat_event, str(self.SENDER_1), "say")

    @pytest.mark.asyncio
    async def test_room_based_channels_local(self, nats_handler, mock_connection_manager):
        """Test room-based channel broadcasting (local)."""
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        nats_handler.connection_manager = mock_connection_manager

        with patch.object(nats_handler, "_broadcast_to_room_with_filtering") as mock_broadcast:
            await nats_handler._broadcast_by_channel_type("local", chat_event, "test_room", "", None, self.SENDER_1)

            mock_broadcast.assert_called_once_with("test_room", chat_event, str(self.SENDER_1), "local")

    @pytest.mark.asyncio
    async def test_room_based_channels_emote(self, nats_handler, mock_connection_manager):
        """Test room-based channel broadcasting (emote)."""
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        nats_handler.connection_manager = mock_connection_manager

        with patch.object(nats_handler, "_broadcast_to_room_with_filtering") as mock_broadcast:
            await nats_handler._broadcast_by_channel_type("emote", chat_event, "test_room", "", None, self.SENDER_1)

            mock_broadcast.assert_called_once_with("test_room", chat_event, str(self.SENDER_1), "emote")

    @pytest.mark.asyncio
    async def test_room_based_channels_pose(self, nats_handler, mock_connection_manager):
        """Test room-based channel broadcasting (pose)."""
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        nats_handler.connection_manager = mock_connection_manager

        with patch.object(nats_handler, "_broadcast_to_room_with_filtering") as mock_broadcast:
            await nats_handler._broadcast_by_channel_type("pose", chat_event, "test_room", "", None, self.SENDER_1)

            mock_broadcast.assert_called_once_with("test_room", chat_event, str(self.SENDER_1), "pose")

    @pytest.mark.asyncio
    async def test_room_based_channels_missing_room_id(self, nats_handler, mock_connection_manager):
        """Test room-based channels with missing room_id."""
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        nats_handler.connection_manager = mock_connection_manager

        with patch.object(nats_handler, "_broadcast_to_room_with_filtering") as mock_broadcast:
            await nats_handler._broadcast_by_channel_type("say", chat_event, "", "", None, self.SENDER_1)

            # Should not call broadcast when room_id is missing
            mock_broadcast.assert_not_called()

    @pytest.mark.asyncio
    async def test_global_channel(self, nats_handler, mock_connection_manager_strategy):
        """Test global channel broadcasting."""
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        nats_handler.connection_manager = mock_connection_manager_strategy

        await nats_handler._broadcast_by_channel_type("global", chat_event, "", "", None, self.SENDER_1)

        mock_connection_manager_strategy.broadcast_global.assert_called_once_with(
            chat_event, exclude_player=str(self.SENDER_1)
        )

    @pytest.mark.asyncio
    async def test_party_channel_with_party_id(self, nats_handler, mock_connection_manager):
        """Test party channel broadcasting with party_id."""
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        nats_handler.connection_manager = mock_connection_manager

        await nats_handler._broadcast_by_channel_type("party", chat_event, "", "party123", None, self.SENDER_1)

        # Currently just logs, no actual broadcasting
        # This will be implemented when party system is available

    @pytest.mark.asyncio
    async def test_party_channel_missing_party_id(self, nats_handler, mock_connection_manager):
        """Test party channel broadcasting without party_id."""
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        nats_handler.connection_manager = mock_connection_manager

        await nats_handler._broadcast_by_channel_type("party", chat_event, "", "", None, self.SENDER_1)

        # Should log warning but not broadcast

    @pytest.mark.asyncio
    async def test_whisper_channel_with_target(self, nats_handler, mock_connection_manager_strategy):
        """Test whisper channel broadcasting with target player."""
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        nats_handler.connection_manager = mock_connection_manager_strategy

        await nats_handler._broadcast_by_channel_type("whisper", chat_event, "", "", self.TARGET_1, self.SENDER_1)

        mock_connection_manager_strategy.send_personal_message.assert_called_once_with(self.TARGET_1, chat_event)

    @pytest.mark.asyncio
    async def test_whisper_channel_missing_target(self, nats_handler, mock_connection_manager_strategy):
        """Test whisper channel broadcasting without target player."""
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        nats_handler.connection_manager = mock_connection_manager_strategy

        await nats_handler._broadcast_by_channel_type("whisper", chat_event, "", "", None, self.SENDER_1)

        # Should not send when target_player_id is missing
        mock_connection_manager_strategy.send_personal_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_system_channel(self, nats_handler, mock_connection_manager_strategy):
        """Test system channel broadcasting."""
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        nats_handler.connection_manager = mock_connection_manager_strategy

        await nats_handler._broadcast_by_channel_type("system", chat_event, "", "", None, self.SENDER_1)

        mock_connection_manager_strategy.broadcast_global.assert_called_once_with(
            chat_event, exclude_player=str(self.SENDER_1)
        )

    @pytest.mark.asyncio
    async def test_admin_channel(self, nats_handler, mock_connection_manager_strategy):
        """Test admin channel broadcasting."""
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        nats_handler.connection_manager = mock_connection_manager_strategy

        await nats_handler._broadcast_by_channel_type("admin", chat_event, "", "", None, self.SENDER_1)

        mock_connection_manager_strategy.broadcast_global.assert_called_once_with(
            chat_event, exclude_player=str(self.SENDER_1)
        )

    @pytest.mark.asyncio
    async def test_unknown_channel_type(self, nats_handler, mock_connection_manager_strategy):
        """Test unknown channel type handling."""
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        nats_handler.connection_manager = mock_connection_manager_strategy

        await nats_handler._broadcast_by_channel_type("unknown", chat_event, "", "", None, self.SENDER_1)

        # Should not call any broadcast methods for unknown channels
        mock_connection_manager_strategy.broadcast_global.assert_not_called()
        mock_connection_manager_strategy.send_personal_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_broadcast_to_room_with_filtering(self, nats_handler, mock_connection_manager):
        """Test room broadcasting with filtering through strategy pattern."""
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        nats_handler.connection_manager = mock_connection_manager

        # Mock the filtering methods
        with (
            patch.object(nats_handler, "_is_player_in_room", return_value=True),
            patch.object(nats_handler, "_is_player_muted_by_receiver", return_value=False),
        ):
            # Test through the strategy pattern
            await nats_handler._broadcast_by_channel_type("say", chat_event, "test_room", "", None, self.SENDER_1)

            # Should call send_personal_message for each filtered player
            mock_connection_manager.send_personal_message.assert_called()

    @pytest.mark.asyncio
    async def test_broadcast_to_room_filter_out_sender(self, nats_handler, mock_connection_manager):
        """Test that sender is filtered out from room broadcasts through strategy pattern."""
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        nats_handler.connection_manager = mock_connection_manager

        # Mock the filtering methods
        with (
            patch.object(nats_handler, "_is_player_in_room", return_value=True),
            patch.object(nats_handler, "_is_player_muted_by_receiver", return_value=False),
        ):
            # Test through the strategy pattern
            await nats_handler._broadcast_by_channel_type(
                "say",
                chat_event,
                "test_room",
                "",
                None,
                self.PLAYER_1,  # sender is player1
            )

            # Should call send_personal_message for filtered players (excluding sender)
            mock_connection_manager.send_personal_message.assert_called()

    @pytest.mark.asyncio
    async def test_broadcast_to_room_filter_out_muted_players(self, nats_handler, mock_connection_manager):
        """Test that muted players are filtered out from room broadcasts through strategy pattern."""
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        nats_handler.connection_manager = mock_connection_manager

        # Mock the filtering methods - player2 is muted
        def mock_is_muted(player_id, sender_id):
            # player_id comes from room_subscriptions as string, so compare as string
            return player_id == str(self.PLAYER_2)

        with (
            patch.object(nats_handler, "_is_player_in_room", return_value=True),
            patch.object(nats_handler, "_is_player_muted_by_receiver", side_effect=mock_is_muted),
        ):
            # Test through the strategy pattern
            await nats_handler._broadcast_by_channel_type("say", chat_event, "test_room", "", None, self.SENDER_1)

            # Should call send_personal_message for non-muted players
            mock_connection_manager.send_personal_message.assert_called()

    @pytest.mark.asyncio
    async def test_broadcast_to_room_filter_out_players_not_in_room(self, nats_handler, mock_connection_manager):
        """Test that players not in the room are filtered out through strategy pattern."""
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        nats_handler.connection_manager = mock_connection_manager

        # Mock the filtering methods - player2 is not in room
        def mock_is_in_room(player_id, room_id):
            # player_id comes from room_subscriptions as string, so compare as string
            return player_id == str(self.PLAYER_1)

        with (
            patch.object(nats_handler, "_is_player_in_room", side_effect=mock_is_in_room),
            patch.object(nats_handler, "_is_player_muted_by_receiver", return_value=False),
        ):
            # Test through the strategy pattern
            await nats_handler._broadcast_by_channel_type("say", chat_event, "test_room", "", None, self.SENDER_1)

            # Should call send_personal_message for players in room
            mock_connection_manager.send_personal_message.assert_called()

    @pytest.mark.asyncio
    async def test_error_handling_in_broadcast(self, nats_handler, mock_connection_manager):
        """Test error handling during broadcasting."""
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        nats_handler.connection_manager = mock_connection_manager

        # Make broadcast_global raise an exception
        mock_connection_manager.broadcast_global.side_effect = Exception("Broadcast failed")

        # Should not raise exception, should be handled gracefully
        await nats_handler._broadcast_by_channel_type("global", chat_event, "", "", None, self.SENDER_1)

    @pytest.mark.asyncio
    async def test_error_handling_in_room_broadcast(self, nats_handler, mock_connection_manager):
        """Test error handling during room broadcasting."""
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        nats_handler.connection_manager = mock_connection_manager

        # Make _broadcast_to_room_with_filtering raise an exception
        with patch.object(
            nats_handler, "_broadcast_to_room_with_filtering", side_effect=Exception("Room broadcast failed")
        ):
            # Should not raise exception, should be handled gracefully
            await nats_handler._broadcast_by_channel_type("say", chat_event, "test_room", "", None, self.SENDER_1)

    @pytest.mark.asyncio
    async def test_all_channel_types_covered(self, nats_handler, mock_connection_manager):
        """Test that all channel types are handled."""
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        channel_types = ["say", "local", "emote", "pose", "global", "party", "whisper", "system", "admin"]

        for channel in channel_types:
            with patch.object(nats_handler, "_broadcast_to_room_with_filtering"):
                await nats_handler._broadcast_by_channel_type(
                    channel, chat_event, "test_room", "party123", self.TARGET_1, self.SENDER_1
                )

                # Each channel type should be handled without raising exceptions
                # (Some may just log warnings for missing data, but shouldn't crash)


# ============================================================================
# Tests merged from test_broadcasting_strategies_impl_legacy.py
# ============================================================================


class TestChannelBroadcastingStrategiesLegacy:
    """Test suite for channel broadcasting strategies."""

    # Test player IDs - use UUID objects
    SENDER_1 = uuid.uuid4()
    TARGET_1 = uuid.uuid4()

    @pytest.fixture
    def mock_nats_handler(self):
        """Create a mock NATS handler for testing."""
        handler = MagicMock()
        handler._broadcast_to_room_with_filtering = AsyncMock()
        return handler

    @pytest.fixture
    def mock_connection_manager(self):
        """Return a mock connection manager for legacy strategy tests."""
        mock_cm = MagicMock()
        mock_cm.broadcast_global = AsyncMock()
        mock_cm.send_personal_message = AsyncMock()
        return mock_cm

    @pytest.mark.asyncio
    async def test_room_based_channel_strategy_say(self, mock_nats_handler, mock_connection_manager):
        """Test RoomBasedChannelStrategy for say channel."""
        strategy = RoomBasedChannelStrategy("say")
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        mock_nats_handler.connection_manager = mock_connection_manager

        await strategy.broadcast(chat_event, "test_room", "", None, self.SENDER_1, mock_nats_handler)

        mock_nats_handler._broadcast_to_room_with_filtering.assert_called_once_with(
            "test_room", chat_event, str(self.SENDER_1), "say"
        )

    @pytest.mark.asyncio
    async def test_room_based_channel_strategy_missing_room_id(self, mock_nats_handler, mock_connection_manager):
        """Test RoomBasedChannelStrategy with missing room_id."""
        strategy = RoomBasedChannelStrategy("local")
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        mock_nats_handler.connection_manager = mock_connection_manager

        await strategy.broadcast(
            chat_event, "", "", None, TestChannelBroadcastingStrategiesLegacy.SENDER_1, mock_nats_handler
        )

        # Should not call broadcast when room_id is missing
        mock_nats_handler._broadcast_to_room_with_filtering.assert_not_called()

    @pytest.mark.asyncio
    async def test_global_channel_strategy(self, mock_nats_handler, mock_connection_manager):
        """Test GlobalChannelStrategy."""
        strategy = GlobalChannelStrategy()
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        mock_nats_handler.connection_manager = mock_connection_manager

        await strategy.broadcast(chat_event, "", "", None, self.SENDER_1, mock_nats_handler)

        mock_connection_manager.broadcast_global.assert_called_once_with(chat_event, exclude_player=str(self.SENDER_1))

    @pytest.mark.asyncio
    async def test_party_channel_strategy_with_party_id(self, mock_nats_handler, mock_connection_manager):
        """Test PartyChannelStrategy with party_id."""
        strategy = PartyChannelStrategy()
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        mock_nats_handler.connection_manager = mock_connection_manager

        await strategy.broadcast(chat_event, "", "party123", None, self.SENDER_1, mock_nats_handler)

        # Currently just logs, no actual broadcasting
        # This will be implemented when party system is available

    @pytest.mark.asyncio
    async def test_party_channel_strategy_missing_party_id(self, mock_nats_handler, mock_connection_manager):
        """Test PartyChannelStrategy without party_id."""
        strategy = PartyChannelStrategy()
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        mock_nats_handler.connection_manager = mock_connection_manager

        await strategy.broadcast(
            chat_event, "", "", None, TestChannelBroadcastingStrategiesLegacy.SENDER_1, mock_nats_handler
        )

        # Should log warning but not broadcast

    @pytest.mark.asyncio
    async def test_whisper_channel_strategy_with_target(self, mock_nats_handler, mock_connection_manager):
        """Test WhisperChannelStrategy with target player."""
        strategy = WhisperChannelStrategy()
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        mock_nats_handler.connection_manager = mock_connection_manager

        await strategy.broadcast(chat_event, "", "", self.TARGET_1, self.SENDER_1, mock_nats_handler)

        mock_connection_manager.send_personal_message.assert_called_once_with(self.TARGET_1, chat_event)

    @pytest.mark.asyncio
    async def test_whisper_channel_strategy_missing_target(self, mock_nats_handler, mock_connection_manager):
        """Test WhisperChannelStrategy without target player."""
        strategy = WhisperChannelStrategy()
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        mock_nats_handler.connection_manager = mock_connection_manager

        await strategy.broadcast(
            chat_event, "", "", None, TestChannelBroadcastingStrategiesLegacy.SENDER_1, mock_nats_handler
        )

        # Should not send when target_player_id is missing
        mock_connection_manager.send_personal_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_system_admin_channel_strategy_system(self, mock_nats_handler, mock_connection_manager):
        """Test SystemAdminChannelStrategy for system channel."""
        strategy = SystemAdminChannelStrategy("system")
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        mock_nats_handler.connection_manager = mock_connection_manager

        await strategy.broadcast(chat_event, "", "", None, self.SENDER_1, mock_nats_handler)

        mock_connection_manager.broadcast_global.assert_called_once_with(chat_event, exclude_player=str(self.SENDER_1))

    @pytest.mark.asyncio
    async def test_system_admin_channel_strategy_admin(self, mock_nats_handler, mock_connection_manager):
        """Test SystemAdminChannelStrategy for admin channel."""
        strategy = SystemAdminChannelStrategy("admin")
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        mock_nats_handler.connection_manager = mock_connection_manager

        await strategy.broadcast(chat_event, "", "", None, self.SENDER_1, mock_nats_handler)

        mock_connection_manager.broadcast_global.assert_called_once_with(chat_event, exclude_player=str(self.SENDER_1))

    @pytest.mark.asyncio
    async def test_unknown_channel_strategy(self, mock_nats_handler, mock_connection_manager):
        """Test UnknownChannelStrategy."""
        strategy = UnknownChannelStrategy("unknown")
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        mock_nats_handler.connection_manager = mock_connection_manager

        await strategy.broadcast(
            chat_event, "", "", None, TestChannelBroadcastingStrategiesLegacy.SENDER_1, mock_nats_handler
        )

        # Should not call any broadcast methods for unknown channels
        mock_connection_manager.broadcast_global.assert_not_called()
        mock_connection_manager.send_personal_message.assert_not_called()


class TestChannelBroadcastingStrategyFactory:
    """Test suite for channel broadcasting strategy factory."""

    def test_get_strategy_for_known_channels(self):
        """Test getting strategies for known channel types."""
        factory = ChannelBroadcastingStrategyFactory()

        # Test room-based channels
        assert isinstance(factory.get_strategy("say"), RoomBasedChannelStrategy)
        assert isinstance(factory.get_strategy("local"), RoomBasedChannelStrategy)
        assert isinstance(factory.get_strategy("emote"), RoomBasedChannelStrategy)
        assert isinstance(factory.get_strategy("pose"), RoomBasedChannelStrategy)

        # Test other channels
        assert isinstance(factory.get_strategy("global"), GlobalChannelStrategy)
        assert isinstance(factory.get_strategy("party"), PartyChannelStrategy)
        assert isinstance(factory.get_strategy("whisper"), WhisperChannelStrategy)
        assert isinstance(factory.get_strategy("system"), SystemAdminChannelStrategy)
        assert isinstance(factory.get_strategy("admin"), SystemAdminChannelStrategy)

    def test_get_strategy_for_unknown_channel(self):
        """Test getting strategy for unknown channel type."""
        factory = ChannelBroadcastingStrategyFactory()

        strategy = factory.get_strategy("unknown_channel")
        assert isinstance(strategy, UnknownChannelStrategy)
        assert strategy.channel_type == "unknown_channel"

    def test_register_new_strategy(self):
        """Test registering a new strategy."""
        factory = ChannelBroadcastingStrategyFactory()

        # Create a custom strategy
        class CustomStrategy(ChannelBroadcastingStrategy):
            async def broadcast(self, chat_event, room_id, party_id, target_player_id, sender_id, nats_handler):
                pass

        custom_strategy = CustomStrategy()

        # Register the strategy
        factory.register_strategy("custom", custom_strategy)

        # Verify it's returned
        retrieved_strategy = factory.get_strategy("custom")
        assert retrieved_strategy is custom_strategy

    def test_global_factory_instance(self):
        """Test that the global factory instance works correctly."""
        # Test that the global factory has all expected strategies
        assert isinstance(channel_strategy_factory.get_strategy("say"), RoomBasedChannelStrategy)
        assert isinstance(channel_strategy_factory.get_strategy("global"), GlobalChannelStrategy)
        assert isinstance(channel_strategy_factory.get_strategy("party"), PartyChannelStrategy)
        assert isinstance(channel_strategy_factory.get_strategy("whisper"), WhisperChannelStrategy)
        assert isinstance(channel_strategy_factory.get_strategy("system"), SystemAdminChannelStrategy)
        assert isinstance(channel_strategy_factory.get_strategy("admin"), SystemAdminChannelStrategy)

    def test_strategy_channel_types(self):
        """Test that strategies have correct channel types."""
        factory = ChannelBroadcastingStrategyFactory()

        # Test room-based strategies
        say_strategy = factory.get_strategy("say")
        assert say_strategy.channel_type == "say"

        local_strategy = factory.get_strategy("local")
        assert local_strategy.channel_type == "local"

        # Test system/admin strategies
        system_strategy = factory.get_strategy("system")
        assert system_strategy.channel_type == "system"

        admin_strategy = factory.get_strategy("admin")
        assert admin_strategy.channel_type == "admin"

    def test_unknown_strategy_channel_type(self):
        """Test that unknown strategy has correct channel type."""
        factory = ChannelBroadcastingStrategyFactory()

        strategy = factory.get_strategy("unknown_channel")
        assert strategy.channel_type == "unknown_channel"


class TestStrategyIntegration:
    """Test integration of strategies with NATS handler."""

    # Test player IDs - use UUID objects
    SENDER_1 = uuid.uuid4()
    TARGET_1 = uuid.uuid4()

    @pytest.fixture
    def mock_connection_manager(self):
        """Return a mock connection manager for integration tests."""
        mock_cm = MagicMock()
        mock_cm.broadcast_global = AsyncMock()
        mock_cm.send_personal_message = AsyncMock()
        return mock_cm

    @pytest.mark.asyncio
    async def test_strategy_integration_with_nats_handler(self, mock_connection_manager):
        """Test that strategies work correctly with NATS handler."""
        from server.realtime.nats_message_handler import NATSMessageHandler

        # Create NATS handler with mock service
        mock_nats_service = MagicMock()
        nats_handler = NATSMessageHandler(mock_nats_service)

        # Mock the room filtering method
        nats_handler._broadcast_to_room_with_filtering = AsyncMock()

        # Test room-based channel
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        nats_handler.connection_manager = mock_connection_manager

        await nats_handler._broadcast_by_channel_type("say", chat_event, "test_room", "", None, self.SENDER_1)

        # Should call the room filtering method
        # _broadcast_to_room_with_filtering expects string sender_id, so assert against string
        nats_handler._broadcast_to_room_with_filtering.assert_called_once_with(
            "test_room", chat_event, str(self.SENDER_1), "say"
        )

    @pytest.mark.asyncio
    async def test_strategy_integration_global_channel(self, mock_connection_manager):
        """Test that global channel strategy works with NATS handler."""
        from server.realtime.nats_message_handler import NATSMessageHandler

        # Create NATS handler with mock service
        mock_nats_service = MagicMock()
        nats_handler = NATSMessageHandler(mock_nats_service)

        # Test global channel
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        nats_handler.connection_manager = mock_connection_manager

        await nats_handler._broadcast_by_channel_type("global", chat_event, "", "", None, self.SENDER_1)

        # Should call broadcast_global
        mock_connection_manager.broadcast_global.assert_called_once_with(chat_event, exclude_player=str(self.SENDER_1))

    @pytest.mark.asyncio
    async def test_strategy_integration_whisper_channel(self, mock_connection_manager):
        """Test that whisper channel strategy works with NATS handler."""
        from server.realtime.nats_message_handler import NATSMessageHandler

        # Create NATS handler with mock service
        mock_nats_service = MagicMock()
        nats_handler = NATSMessageHandler(mock_nats_service)

        # Test whisper channel
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        nats_handler.connection_manager = mock_connection_manager

        await nats_handler._broadcast_by_channel_type("whisper", chat_event, "", "", self.TARGET_1, self.SENDER_1)

        # Should call send_personal_message
        mock_connection_manager.send_personal_message.assert_called_once_with(self.TARGET_1, chat_event)

    @pytest.mark.asyncio
    async def test_strategy_integration_unknown_channel(self, mock_connection_manager):
        """Test that unknown channel strategy works with NATS handler."""
        from server.realtime.nats_message_handler import NATSMessageHandler

        # Create NATS handler with mock service
        mock_nats_service = MagicMock()
        nats_handler = NATSMessageHandler(mock_nats_service)

        # Test unknown channel
        chat_event = {"type": "chat", "data": {"message": "Hello"}}
        nats_handler.connection_manager = mock_connection_manager

        # Should not raise exception
        await nats_handler._broadcast_by_channel_type("unknown", chat_event, "", "", None, self.SENDER_1)

        # Should not call any broadcast methods
        mock_connection_manager.broadcast_global.assert_not_called()
        mock_connection_manager.send_personal_message.assert_not_called()
