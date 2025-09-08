"""
Tests for Channel Broadcasting Strategy Pattern Implementation.

This module tests the strategy pattern implementation for channel broadcasting,
ensuring it correctly handles all channel types and maintains backward compatibility.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from ..realtime.channel_broadcasting_strategies import (
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


class TestChannelBroadcastingStrategies:
    """Test suite for channel broadcasting strategies."""

    @pytest.fixture
    def mock_nats_handler(self):
        """Create a mock NATS handler for testing."""
        handler = MagicMock()
        handler._broadcast_to_room_with_filtering = AsyncMock()
        return handler

    @pytest.fixture
    def mock_connection_manager(self):
        """Mock the connection manager."""
        with patch("server.realtime.connection_manager.connection_manager") as mock_cm:
            mock_cm.broadcast_global = AsyncMock()
            mock_cm.send_personal_message = AsyncMock()
            yield mock_cm

    @pytest.mark.asyncio
    async def test_room_based_channel_strategy_say(self, mock_nats_handler, mock_connection_manager):
        """Test RoomBasedChannelStrategy for say channel."""
        strategy = RoomBasedChannelStrategy("say")
        chat_event = {"type": "chat", "data": {"message": "Hello"}}

        await strategy.broadcast(chat_event, "test_room", "", "", "sender1", mock_nats_handler)

        mock_nats_handler._broadcast_to_room_with_filtering.assert_called_once_with(
            "test_room", chat_event, "sender1", "say"
        )

    @pytest.mark.asyncio
    async def test_room_based_channel_strategy_missing_room_id(self, mock_nats_handler, mock_connection_manager):
        """Test RoomBasedChannelStrategy with missing room_id."""
        strategy = RoomBasedChannelStrategy("local")
        chat_event = {"type": "chat", "data": {"message": "Hello"}}

        await strategy.broadcast(chat_event, "", "", "", "sender1", mock_nats_handler)

        # Should not call broadcast when room_id is missing
        mock_nats_handler._broadcast_to_room_with_filtering.assert_not_called()

    @pytest.mark.asyncio
    async def test_global_channel_strategy(self, mock_nats_handler, mock_connection_manager):
        """Test GlobalChannelStrategy."""
        strategy = GlobalChannelStrategy()
        chat_event = {"type": "chat", "data": {"message": "Hello"}}

        await strategy.broadcast(chat_event, "", "", "", "sender1", mock_nats_handler)

        mock_connection_manager.broadcast_global.assert_called_once_with(chat_event, exclude_player="sender1")

    @pytest.mark.asyncio
    async def test_party_channel_strategy_with_party_id(self, mock_nats_handler, mock_connection_manager):
        """Test PartyChannelStrategy with party_id."""
        strategy = PartyChannelStrategy()
        chat_event = {"type": "chat", "data": {"message": "Hello"}}

        await strategy.broadcast(chat_event, "", "party123", "", "sender1", mock_nats_handler)

        # Currently just logs, no actual broadcasting
        # This will be implemented when party system is available

    @pytest.mark.asyncio
    async def test_party_channel_strategy_missing_party_id(self, mock_nats_handler, mock_connection_manager):
        """Test PartyChannelStrategy without party_id."""
        strategy = PartyChannelStrategy()
        chat_event = {"type": "chat", "data": {"message": "Hello"}}

        await strategy.broadcast(chat_event, "", "", "", "sender1", mock_nats_handler)

        # Should log warning but not broadcast

    @pytest.mark.asyncio
    async def test_whisper_channel_strategy_with_target(self, mock_nats_handler, mock_connection_manager):
        """Test WhisperChannelStrategy with target player."""
        strategy = WhisperChannelStrategy()
        chat_event = {"type": "chat", "data": {"message": "Hello"}}

        await strategy.broadcast(chat_event, "", "", "target1", "sender1", mock_nats_handler)

        mock_connection_manager.send_personal_message.assert_called_once_with("target1", chat_event)

    @pytest.mark.asyncio
    async def test_whisper_channel_strategy_missing_target(self, mock_nats_handler, mock_connection_manager):
        """Test WhisperChannelStrategy without target player."""
        strategy = WhisperChannelStrategy()
        chat_event = {"type": "chat", "data": {"message": "Hello"}}

        await strategy.broadcast(chat_event, "", "", "", "sender1", mock_nats_handler)

        # Should not send when target_player_id is missing
        mock_connection_manager.send_personal_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_system_admin_channel_strategy_system(self, mock_nats_handler, mock_connection_manager):
        """Test SystemAdminChannelStrategy for system channel."""
        strategy = SystemAdminChannelStrategy("system")
        chat_event = {"type": "chat", "data": {"message": "Hello"}}

        await strategy.broadcast(chat_event, "", "", "", "sender1", mock_nats_handler)

        mock_connection_manager.broadcast_global.assert_called_once_with(chat_event, exclude_player="sender1")

    @pytest.mark.asyncio
    async def test_system_admin_channel_strategy_admin(self, mock_nats_handler, mock_connection_manager):
        """Test SystemAdminChannelStrategy for admin channel."""
        strategy = SystemAdminChannelStrategy("admin")
        chat_event = {"type": "chat", "data": {"message": "Hello"}}

        await strategy.broadcast(chat_event, "", "", "", "sender1", mock_nats_handler)

        mock_connection_manager.broadcast_global.assert_called_once_with(chat_event, exclude_player="sender1")

    @pytest.mark.asyncio
    async def test_unknown_channel_strategy(self, mock_nats_handler, mock_connection_manager):
        """Test UnknownChannelStrategy."""
        strategy = UnknownChannelStrategy("unknown")
        chat_event = {"type": "chat", "data": {"message": "Hello"}}

        await strategy.broadcast(chat_event, "", "", "", "sender1", mock_nats_handler)

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

    @pytest.fixture
    def mock_connection_manager(self):
        """Mock the connection manager."""
        with patch("server.realtime.connection_manager.connection_manager") as mock_cm:
            mock_cm.broadcast_global = AsyncMock()
            mock_cm.send_personal_message = AsyncMock()
            yield mock_cm

    @pytest.mark.asyncio
    async def test_strategy_integration_with_nats_handler(self, mock_connection_manager):
        """Test that strategies work correctly with NATS handler."""
        from ..realtime.nats_message_handler import NATSMessageHandler

        # Create NATS handler with mock service
        mock_nats_service = MagicMock()
        nats_handler = NATSMessageHandler(mock_nats_service)

        # Mock the room filtering method
        nats_handler._broadcast_to_room_with_filtering = AsyncMock()

        # Test room-based channel
        chat_event = {"type": "chat", "data": {"message": "Hello"}}

        await nats_handler._broadcast_by_channel_type("say", chat_event, "test_room", "", "", "sender1")

        # Should call the room filtering method
        nats_handler._broadcast_to_room_with_filtering.assert_called_once_with(
            "test_room", chat_event, "sender1", "say"
        )

    @pytest.mark.asyncio
    async def test_strategy_integration_global_channel(self, mock_connection_manager):
        """Test that global channel strategy works with NATS handler."""
        from ..realtime.nats_message_handler import NATSMessageHandler

        # Create NATS handler with mock service
        mock_nats_service = MagicMock()
        nats_handler = NATSMessageHandler(mock_nats_service)

        # Test global channel
        chat_event = {"type": "chat", "data": {"message": "Hello"}}

        await nats_handler._broadcast_by_channel_type("global", chat_event, "", "", "", "sender1")

        # Should call broadcast_global
        mock_connection_manager.broadcast_global.assert_called_once_with(chat_event, exclude_player="sender1")

    @pytest.mark.asyncio
    async def test_strategy_integration_whisper_channel(self, mock_connection_manager):
        """Test that whisper channel strategy works with NATS handler."""
        from ..realtime.nats_message_handler import NATSMessageHandler

        # Create NATS handler with mock service
        mock_nats_service = MagicMock()
        nats_handler = NATSMessageHandler(mock_nats_service)

        # Test whisper channel
        chat_event = {"type": "chat", "data": {"message": "Hello"}}

        await nats_handler._broadcast_by_channel_type("whisper", chat_event, "", "", "target1", "sender1")

        # Should call send_personal_message
        mock_connection_manager.send_personal_message.assert_called_once_with("target1", chat_event)

    @pytest.mark.asyncio
    async def test_strategy_integration_unknown_channel(self, mock_connection_manager):
        """Test that unknown channel strategy works with NATS handler."""
        from ..realtime.nats_message_handler import NATSMessageHandler

        # Create NATS handler with mock service
        mock_nats_service = MagicMock()
        nats_handler = NATSMessageHandler(mock_nats_service)

        # Test unknown channel
        chat_event = {"type": "chat", "data": {"message": "Hello"}}

        # Should not raise exception
        await nats_handler._broadcast_by_channel_type("unknown", chat_event, "", "", "", "sender1")

        # Should not call any broadcast methods
        mock_connection_manager.broadcast_global.assert_not_called()
        mock_connection_manager.send_personal_message.assert_not_called()
