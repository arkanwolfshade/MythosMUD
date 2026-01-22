"""
Unit tests for NATS message handler subzone and event handling.

Tests subzone subscriptions, player movement, cleanup, and event handlers.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.services.nats_exceptions import NATSError

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice


@pytest.mark.asyncio
async def test_unsubscribe_from_subzone_decrease_count(nats_message_handler, mock_subject_manager):
    """Test unsubscribe_from_subzone decreases count when > 1."""
    mock_subject_manager.build_subject = MagicMock(return_value="chat.local.subzone_001")
    nats_message_handler.subscriptions = {"chat.local.subzone_001": True}
    nats_message_handler.subzone_subscriptions = {"subzone_001": 2}
    result = await nats_message_handler.unsubscribe_from_subzone("subzone_001")
    assert result is True
    assert nats_message_handler.subzone_subscriptions["subzone_001"] == 1


@pytest.mark.asyncio
async def test_unsubscribe_from_subzone_not_subscribed(nats_message_handler, mock_subject_manager):
    """Test unsubscribe_from_subzone handles not subscribed case."""
    mock_subject_manager.build_subject = MagicMock(return_value="chat.local.subzone_001")
    result = await nats_message_handler.unsubscribe_from_subzone("subzone_001")
    assert result is False


@pytest.mark.asyncio
async def test_unsubscribe_from_subzone_error(nats_message_handler, mock_subject_manager):
    """Test unsubscribe_from_subzone handles errors."""
    mock_subject_manager.build_subject = MagicMock(return_value="chat.local.subzone_001")
    nats_message_handler.subscriptions = {"chat.local.subzone_001": True}
    nats_message_handler.subzone_subscriptions = {"subzone_001": 1}
    nats_message_handler._unsubscribe_from_subject = AsyncMock(side_effect=NATSError("Error"))
    result = await nats_message_handler.unsubscribe_from_subzone("subzone_001")
    assert result is False


def test_track_player_subzone_subscription_different_subzone(nats_message_handler):
    """Test track_player_subzone_subscription handles player moving to different subzone."""
    nats_message_handler.player_subzone_subscriptions = {"player_001": "old_subzone"}
    nats_message_handler.subzone_subscriptions = {"old_subzone": 2}
    nats_message_handler.track_player_subzone_subscription("player_001", "new_subzone")
    assert nats_message_handler.player_subzone_subscriptions["player_001"] == "new_subzone"
    assert nats_message_handler.subzone_subscriptions["old_subzone"] == 1


def test_get_players_in_subzone(nats_message_handler):
    """Test get_players_in_subzone returns players in subzone."""
    nats_message_handler.player_subzone_subscriptions = {
        "player_001": "subzone_001",
        "player_002": "subzone_002",
        "player_003": "subzone_001",
    }
    players = nats_message_handler.get_players_in_subzone("subzone_001")
    assert len(players) == 2
    assert "player_001" in players
    assert "player_003" in players


def test_get_players_in_subzone_empty(nats_message_handler):
    """Test get_players_in_subzone returns empty list for empty subzone."""
    nats_message_handler.player_subzone_subscriptions = {}
    players = nats_message_handler.get_players_in_subzone("subzone_001")
    assert players == []


@pytest.mark.asyncio
async def test_handle_player_movement_different_subzone(nats_message_handler):
    """Test handle_player_movement handles movement to different subzone."""
    nats_message_handler.unsubscribe_from_subzone = AsyncMock(return_value=True)
    nats_message_handler.subscribe_to_subzone = AsyncMock(return_value=True)
    nats_message_handler.track_player_subzone_subscription = MagicMock()
    with patch("server.utils.room_utils.extract_subzone_from_room_id") as mock_extract:
        mock_extract.side_effect = lambda x: "old_subzone" if x == "room_001" else "new_subzone"
        await nats_message_handler.handle_player_movement("player_001", "room_001", "room_002")
        nats_message_handler.unsubscribe_from_subzone.assert_awaited_once_with("old_subzone")
        nats_message_handler.subscribe_to_subzone.assert_awaited_once_with("new_subzone")


@pytest.mark.asyncio
async def test_handle_player_movement_same_subzone(nats_message_handler):
    """Test handle_player_movement handles movement within same subzone."""
    nats_message_handler.track_player_subzone_subscription = MagicMock()
    with patch("server.utils.room_utils.extract_subzone_from_room_id", return_value="same_subzone"):
        await nats_message_handler.handle_player_movement("player_001", "room_001", "room_002")
        nats_message_handler.track_player_subzone_subscription.assert_called_once()


@pytest.mark.asyncio
async def test_handle_player_movement_exception(nats_message_handler):
    """Test handle_player_movement handles exceptions."""
    with patch("server.utils.room_utils.extract_subzone_from_room_id", side_effect=NATSError("Error")):
        await nats_message_handler.handle_player_movement("player_001", "room_001", "room_002")


@pytest.mark.asyncio
async def test_cleanup_empty_subzone_subscriptions(nats_message_handler):
    """Test cleanup_empty_subzone_subscriptions cleans up empty subzones."""
    nats_message_handler.subzone_subscriptions = {"subzone_001": 0, "subzone_002": 1}
    nats_message_handler.get_players_in_subzone = MagicMock(side_effect=lambda x: [] if x == "subzone_001" else ["p1"])
    nats_message_handler.unsubscribe_from_subzone = AsyncMock(return_value=True)
    await nats_message_handler.cleanup_empty_subzone_subscriptions()
    nats_message_handler.unsubscribe_from_subzone.assert_awaited_once_with("subzone_001")


@pytest.mark.asyncio
async def test_subscribe_to_subzone_error(nats_message_handler, mock_subject_manager):
    """Test subscribe_to_subzone handles errors."""
    mock_subject_manager.build_subject = MagicMock(return_value="chat.local.subzone_001")
    nats_message_handler._subscribe_to_subject = AsyncMock(side_effect=NATSError("Error"))
    result = await nats_message_handler.subscribe_to_subzone("subzone_001")
    assert result is False


@pytest.mark.asyncio
async def test_subscribe_to_subzone_no_subject_manager(nats_message_handler):
    """Test subscribe_to_subzone raises error when subject manager unavailable."""
    nats_message_handler.subject_manager = None
    with pytest.raises(RuntimeError, match="required"):
        await nats_message_handler.subscribe_to_subzone("subzone_001")


@pytest.mark.asyncio
async def test_unsubscribe_from_event_subjects_partial(nats_message_handler, mock_subject_manager):
    """Test unsubscribe_from_event_subjects handles partial success."""
    mock_subject_manager.get_event_subscription_patterns.return_value = ["event.1", "event.2"]
    nats_message_handler.subscriptions = {"event.1": True, "event.2": True}
    nats_message_handler._unsubscribe_from_subject = AsyncMock(side_effect=[True, False])
    result = await nats_message_handler.unsubscribe_from_event_subjects()
    assert result is False


@pytest.mark.asyncio
async def test_subscribe_to_event_subjects_partial_failure(nats_message_handler, mock_subject_manager):
    """Test subscribe_to_event_subjects handles partial failure."""
    mock_subject_manager.get_event_subscription_patterns.return_value = ["event.1", "event.2"]
    nats_message_handler._subscribe_to_subject = AsyncMock(side_effect=[None, NATSError("Error")])
    result = await nats_message_handler.subscribe_to_event_subjects()
    assert result is False


def test_get_event_subscription_count(nats_message_handler):
    """Test get_event_subscription_count returns count."""
    nats_message_handler.subscriptions = {
        "events.player_entered.*": True,
        "events.player_left.*": True,
        "events.game_tick": True,
        "other.subject": True,
    }
    count = nats_message_handler.get_event_subscription_count()
    assert count == 3


def test_is_event_subscription_active(nats_message_handler):
    """Test is_event_subscription_active checks subscription."""
    nats_message_handler.subscriptions = {"events.player_entered.room_001": True}
    assert nats_message_handler.is_event_subscription_active("events.player_entered.room_001") is True
    assert nats_message_handler.is_event_subscription_active("events.nonexistent") is False


def test_get_user_manager_injected(nats_message_handler, mock_user_manager):
    """Test _get_user_manager returns injected manager."""
    assert nats_message_handler._get_user_manager() == mock_user_manager


def test_get_user_manager_fallback(nats_message_handler):
    """Test _get_user_manager falls back to global manager."""
    nats_message_handler.user_manager = None
    with patch("server.services.user_manager.user_manager", MagicMock()) as mock_global:
        result = nats_message_handler._get_user_manager()
        assert result == mock_global


@pytest.mark.asyncio
async def test_handle_player_movement_old_subzone_none(nats_message_handler, mock_subject_manager):
    """Test handle_player_movement handles None old_subzone."""
    mock_subject_manager.build_subject.return_value = "chat.local.new_subzone"
    nats_message_handler._subscribe_to_subject = AsyncMock(return_value=True)
    with patch("server.utils.room_utils.extract_subzone_from_room_id", side_effect=[None, "new_subzone"]):
        await nats_message_handler.handle_player_movement("player_001", "old_room", "new_room")


@pytest.mark.asyncio
async def test_handle_player_movement_new_subzone_none(nats_message_handler):
    """Test handle_player_movement handles None new_subzone."""
    with patch("server.utils.room_utils.extract_subzone_from_room_id", side_effect=["old_subzone", None]):
        await nats_message_handler.handle_player_movement("player_001", "old_room", "new_room")


@pytest.mark.asyncio
async def test_handle_player_movement_error(nats_message_handler):
    """Test handle_player_movement handles NATSError."""
    with patch("server.utils.room_utils.extract_subzone_from_room_id", side_effect=NATSError("Error")):
        await nats_message_handler.handle_player_movement("player_001", "old_room", "new_room")


@pytest.mark.asyncio
async def test_cleanup_empty_subzone_subscriptions_error(nats_message_handler):
    """Test cleanup_empty_subzone_subscriptions handles NATSError."""
    nats_message_handler.get_players_in_subzone = MagicMock(side_effect=NATSError("Error"))
    await nats_message_handler.cleanup_empty_subzone_subscriptions()


@pytest.mark.asyncio
async def test_subscribe_to_subzone_subscribe_failure(nats_message_handler, mock_subject_manager):
    """Test subscribe_to_subzone returns False when subscription fails."""
    mock_subject_manager.build_subject.return_value = "chat.local.subzone_test"
    nats_message_handler._subscribe_to_subject = AsyncMock(return_value=False)
    result = await nats_message_handler.subscribe_to_subzone("subzone_test")
    assert result is False


@pytest.mark.asyncio
async def test_unsubscribe_from_subzone_unsubscribe_failure(nats_message_handler, mock_subject_manager):
    """Test unsubscribe_from_subzone returns False when unsubscription fails."""
    mock_subject_manager.build_subject.return_value = "chat.local.subzone_test"
    nats_message_handler.subzone_subscriptions["subzone_test"] = 1
    nats_message_handler.subscriptions["chat.local.subzone_test"] = True
    nats_message_handler._unsubscribe_from_subject = AsyncMock(return_value=False)
    result = await nats_message_handler.unsubscribe_from_subzone("subzone_test")
    assert result is False


@pytest.mark.asyncio
async def test_handle_combat_started_event(nats_message_handler):
    """Test _handle_combat_started_event delegates to event handler."""
    nats_message_handler._event_handler = MagicMock()
    nats_message_handler._event_handler.handle_combat_started_event = AsyncMock()
    await nats_message_handler._handle_combat_started_event({"combat_id": "combat_001"})
    nats_message_handler._event_handler.handle_combat_started_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_combat_ended_event(nats_message_handler):
    """Test _handle_combat_ended_event delegates to event handler."""
    nats_message_handler._event_handler = MagicMock()
    nats_message_handler._event_handler.handle_combat_ended_event = AsyncMock()
    await nats_message_handler._handle_combat_ended_event({"combat_id": "combat_001"})
    nats_message_handler._event_handler.handle_combat_ended_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_player_attacked_event(nats_message_handler):
    """Test _handle_player_attacked_event delegates to event handler."""
    nats_message_handler._event_handler = MagicMock()
    nats_message_handler._event_handler.handle_player_attacked_event = AsyncMock()
    await nats_message_handler._handle_player_attacked_event({"player_id": "player_001"})
    nats_message_handler._event_handler.handle_player_attacked_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_npc_attacked_event(nats_message_handler):
    """Test _handle_npc_attacked_event delegates to event handler."""
    nats_message_handler._event_handler = MagicMock()
    nats_message_handler._event_handler.handle_npc_attacked_event = AsyncMock()
    await nats_message_handler._handle_npc_attacked_event({"npc_id": "npc_001"})
    nats_message_handler._event_handler.handle_npc_attacked_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_npc_took_damage_event(nats_message_handler):
    """Test _handle_npc_took_damage_event delegates to event handler."""
    nats_message_handler._event_handler = MagicMock()
    nats_message_handler._event_handler.handle_npc_took_damage_event = AsyncMock()
    await nats_message_handler._handle_npc_took_damage_event({"npc_id": "npc_001", "damage": 10})
    nats_message_handler._event_handler.handle_npc_took_damage_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_npc_died_event(nats_message_handler):
    """Test _handle_npc_died_event delegates to event handler."""
    nats_message_handler._event_handler = MagicMock()
    nats_message_handler._event_handler.handle_npc_died_event = AsyncMock()
    await nats_message_handler._handle_npc_died_event({"npc_id": "npc_001"})
    nats_message_handler._event_handler.handle_npc_died_event.assert_awaited_once()


def test_get_event_handler_map(nats_message_handler):
    """Test _get_event_handler_map delegates to event handler."""
    nats_message_handler._event_handler = MagicMock()
    nats_message_handler._event_handler.get_event_handler_map = MagicMock(return_value={"test": lambda x: x})
    result = nats_message_handler._get_event_handler_map()
    assert isinstance(result, dict)
    nats_message_handler._event_handler.get_event_handler_map.assert_called_once()


def test_validate_event_message(nats_message_handler):
    """Test _validate_event_message delegates to event handler."""
    nats_message_handler._event_handler = MagicMock()
    nats_message_handler._event_handler.validate_event_message = MagicMock(return_value=True)
    result = nats_message_handler._validate_event_message("test_event", {"data": "test"})
    assert result is True
    nats_message_handler._event_handler.validate_event_message.assert_called_once_with("test_event", {"data": "test"})


@pytest.mark.asyncio
async def test_handle_event_message(nats_message_handler):
    """Test _handle_event_message delegates to event handler."""
    nats_message_handler._event_handler = MagicMock()
    nats_message_handler._event_handler.handle_event_message = AsyncMock()
    await nats_message_handler._handle_event_message({"type": "test", "data": {}})
    nats_message_handler._event_handler.handle_event_message.assert_awaited_once()
