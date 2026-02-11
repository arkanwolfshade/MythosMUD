"""
Unit tests for channel broadcasting strategies.

Tests the channel_broadcasting_strategies module classes and functions.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.realtime.channel_broadcasting_strategies import (
    ChannelBroadcastingStrategyFactory,
    GlobalChannelStrategy,
    PartyChannelStrategy,
    RoomBasedChannelStrategy,
    UnknownChannelStrategy,
    WhisperChannelStrategy,
    channel_strategy_factory,
)


@pytest.mark.asyncio
async def test_room_based_channel_strategy_broadcast():
    """Test RoomBasedChannelStrategy.broadcast() broadcasts to room."""
    strategy = RoomBasedChannelStrategy("say")
    mock_nats_handler = MagicMock()
    # pylint: disable=protected-access  # Reason: Accessing protected member for testing internal NATS handler methods
    mock_nats_handler._broadcast_to_room_with_filtering = AsyncMock()
    chat_event = {"type": "chat", "message": "Hello"}
    room_id = "room_123"
    party_id = ""
    target_player_id = None
    sender_id = uuid.uuid4()

    await strategy.broadcast(chat_event, room_id, party_id, target_player_id, sender_id, mock_nats_handler)

    mock_nats_handler._broadcast_to_room_with_filtering.assert_called_once_with(
        room_id, chat_event, str(sender_id), "say"
    )


@pytest.mark.asyncio
async def test_room_based_channel_strategy_broadcast_no_room_id():
    """Test RoomBasedChannelStrategy.broadcast() handles missing room_id."""
    strategy = RoomBasedChannelStrategy("say")
    mock_nats_handler = MagicMock()
    # pylint: disable=protected-access  # Reason: Accessing protected member for testing internal NATS handler methods
    mock_nats_handler._broadcast_to_room_with_filtering = AsyncMock()
    chat_event = {"type": "chat", "message": "Hello"}
    room_id = None
    party_id = ""
    target_player_id = None
    sender_id = uuid.uuid4()

    await strategy.broadcast(chat_event, room_id, party_id, target_player_id, sender_id, mock_nats_handler)  # type: ignore[arg-type]  # Reason: Intentionally testing None handling for room_id

    mock_nats_handler._broadcast_to_room_with_filtering.assert_not_called()


@pytest.mark.asyncio
async def test_global_channel_strategy_broadcast():
    """Test GlobalChannelStrategy.broadcast() broadcasts globally."""
    strategy = GlobalChannelStrategy()
    mock_nats_handler = MagicMock()
    mock_nats_handler.connection_manager.broadcast_global = AsyncMock()
    chat_event = {"type": "chat", "message": "Hello"}
    room_id = ""
    party_id = ""
    target_player_id = None
    sender_id = uuid.uuid4()

    await strategy.broadcast(chat_event, room_id, party_id, target_player_id, sender_id, mock_nats_handler)

    mock_nats_handler.connection_manager.broadcast_global.assert_called_once_with(
        chat_event, exclude_player=str(sender_id)
    )


@pytest.mark.asyncio
async def test_party_channel_strategy_broadcast_sends_only_to_party_members():
    """Party chat is delivered only to current party members (visibility)."""
    strategy = PartyChannelStrategy()
    mock_nats_handler = MagicMock()
    # pylint: disable=protected-access  # Reason: Accessing protected member for testing internal NATS handler methods
    mock_nats_handler._apply_dampening_and_send_message = AsyncMock()
    mock_party = MagicMock()
    member_a = "player_a_id"
    member_b = "player_b_id"
    mock_party.member_ids = {member_a, member_b}
    mock_party_service = MagicMock()
    mock_party_service.get_party = MagicMock(return_value=mock_party)
    mock_nats_handler.party_service = mock_party_service

    chat_event = {"type": "chat_message", "message": "Hello party"}
    room_id = ""
    party_id = "party_123"
    target_player_id = None
    sender_id = uuid.uuid4()

    await strategy.broadcast(chat_event, room_id, party_id, target_player_id, sender_id, mock_nats_handler)

    assert mock_nats_handler._apply_dampening_and_send_message.await_count == 2
    calls = mock_nats_handler._apply_dampening_and_send_message.call_args_list
    member_ids_sent = {c[0][2] for c in calls}
    assert member_ids_sent == {member_a, member_b}
    for call in calls:
        assert call[0][1] == str(sender_id)
        assert call[0][3] == "party"


@pytest.mark.asyncio
async def test_party_channel_strategy_broadcast_no_party_service_no_send():
    """When party_service is missing on handler, no message is sent."""
    strategy = PartyChannelStrategy()
    mock_nats_handler = MagicMock()
    # pylint: disable=protected-access  # Reason: Accessing protected member for testing internal NATS handler methods
    mock_nats_handler._apply_dampening_and_send_message = AsyncMock()
    # Do not set party_service on handler

    chat_event = {"type": "chat", "message": "Hello"}
    party_id = "party_123"
    await strategy.broadcast(chat_event, "", party_id, None, uuid.uuid4(), mock_nats_handler)

    mock_nats_handler._apply_dampening_and_send_message.assert_not_called()


@pytest.mark.asyncio
async def test_party_channel_strategy_broadcast_party_not_found_no_send():
    """When party does not exist, no message is sent."""
    strategy = PartyChannelStrategy()
    mock_nats_handler = MagicMock()
    # pylint: disable=protected-access  # Reason: Accessing protected member for testing internal NATS handler methods
    mock_nats_handler._apply_dampening_and_send_message = AsyncMock()
    mock_party_service = MagicMock()
    mock_party_service.get_party = MagicMock(return_value=None)
    mock_nats_handler.party_service = mock_party_service

    chat_event = {"type": "chat", "message": "Hello"}
    party_id = "party_nonexistent"
    await strategy.broadcast(chat_event, "", party_id, None, uuid.uuid4(), mock_nats_handler)

    mock_nats_handler._apply_dampening_and_send_message.assert_not_called()


@pytest.mark.asyncio
async def test_party_channel_strategy_broadcast_no_party_id():
    """Test PartyChannelStrategy.broadcast() handles missing party_id."""
    strategy = PartyChannelStrategy()
    mock_nats_handler = MagicMock()
    chat_event = {"type": "chat", "message": "Hello"}
    room_id = ""
    party_id = None
    target_player_id = None
    sender_id = uuid.uuid4()

    await strategy.broadcast(chat_event, room_id, party_id, target_player_id, sender_id, mock_nats_handler)  # type: ignore[arg-type]  # Reason: Intentionally testing None handling for party_id

    # Should not raise, just log warning


@pytest.mark.asyncio
async def test_whisper_channel_strategy_broadcast():
    """Test WhisperChannelStrategy.broadcast() sends personal message."""
    strategy = WhisperChannelStrategy()
    mock_nats_handler = MagicMock()
    # pylint: disable=protected-access  # Reason: Accessing protected member for testing internal NATS handler methods
    mock_nats_handler._apply_dampening_and_send_message = AsyncMock()
    chat_event = {"type": "chat", "message": "Hello"}
    room_id = ""
    party_id = ""
    target_player_id = uuid.uuid4()
    sender_id = uuid.uuid4()

    await strategy.broadcast(chat_event, room_id, party_id, target_player_id, sender_id, mock_nats_handler)

    mock_nats_handler._apply_dampening_and_send_message.assert_called_once_with(
        chat_event, str(sender_id), str(target_player_id), "whisper"
    )


@pytest.mark.asyncio
async def test_whisper_channel_strategy_broadcast_no_target():
    """Test WhisperChannelStrategy.broadcast() handles missing target_player_id."""
    strategy = WhisperChannelStrategy()
    mock_nats_handler = MagicMock()
    mock_nats_handler.connection_manager.send_personal_message = AsyncMock()
    chat_event = {"type": "chat", "message": "Hello"}
    room_id = ""
    party_id = ""
    target_player_id = None
    sender_id = uuid.uuid4()

    await strategy.broadcast(chat_event, room_id, party_id, target_player_id, sender_id, mock_nats_handler)

    mock_nats_handler.connection_manager.send_personal_message.assert_not_called()


@pytest.mark.asyncio
async def test_system_admin_channel_strategy_broadcast():
    """Test SystemAdminChannelStrategy.broadcast() broadcasts globally."""
    from server.realtime.channel_broadcasting_strategies import SystemAdminChannelStrategy

    strategy = SystemAdminChannelStrategy("system")
    mock_nats_handler = MagicMock()
    mock_nats_handler.connection_manager.broadcast_global = AsyncMock()
    chat_event = {"type": "chat", "message": "Hello"}
    room_id = ""
    party_id = ""
    target_player_id = None
    sender_id = uuid.uuid4()

    await strategy.broadcast(chat_event, room_id, party_id, target_player_id, sender_id, mock_nats_handler)

    mock_nats_handler.connection_manager.broadcast_global.assert_called_once_with(
        chat_event, exclude_player=str(sender_id)
    )


@pytest.mark.asyncio
async def test_unknown_channel_strategy_broadcast():
    """Test UnknownChannelStrategy.broadcast() handles unknown channel."""
    strategy = UnknownChannelStrategy("unknown")
    mock_nats_handler = MagicMock()
    chat_event = {"type": "chat", "message": "Hello"}
    room_id = ""
    party_id = ""
    target_player_id = None
    sender_id = uuid.uuid4()

    await strategy.broadcast(chat_event, room_id, party_id, target_player_id, sender_id, mock_nats_handler)

    # Should not raise, just log warning


def test_channel_broadcasting_strategy_factory_init():
    """Test ChannelBroadcastingStrategyFactory.__init__() initializes with default strategies."""
    factory = ChannelBroadcastingStrategyFactory()

    # pylint: disable=protected-access  # Reason: Accessing protected member for testing internal factory strategy registration
    assert "say" in factory._strategies
    assert "local" in factory._strategies
    assert "emote" in factory._strategies
    assert "pose" in factory._strategies
    assert "global" in factory._strategies
    assert "party" in factory._strategies
    assert "whisper" in factory._strategies
    assert "system" in factory._strategies
    assert "admin" in factory._strategies


def test_channel_broadcasting_strategy_factory_get_strategy_known():
    """Test ChannelBroadcastingStrategyFactory.get_strategy() returns known strategy."""
    factory = ChannelBroadcastingStrategyFactory()

    strategy = factory.get_strategy("say")

    assert isinstance(strategy, RoomBasedChannelStrategy)
    assert strategy.channel_type == "say"


def test_channel_broadcasting_strategy_factory_get_strategy_unknown():
    """Test ChannelBroadcastingStrategyFactory.get_strategy() returns UnknownChannelStrategy for unknown."""
    factory = ChannelBroadcastingStrategyFactory()

    strategy = factory.get_strategy("unknown_channel")

    assert isinstance(strategy, UnknownChannelStrategy)
    assert strategy.channel_type == "unknown_channel"


def test_channel_broadcasting_strategy_factory_register_strategy():
    """Test ChannelBroadcastingStrategyFactory.register_strategy() registers new strategy."""
    factory = ChannelBroadcastingStrategyFactory()
    mock_strategy = MagicMock()

    factory.register_strategy("custom", mock_strategy)

    # pylint: disable=protected-access  # Reason: Accessing protected member for testing internal factory strategy registration
    assert factory._strategies["custom"] == mock_strategy


def test_global_channel_strategy_factory_instance():
    """Test global channel_strategy_factory instance exists."""
    assert isinstance(channel_strategy_factory, ChannelBroadcastingStrategyFactory)
