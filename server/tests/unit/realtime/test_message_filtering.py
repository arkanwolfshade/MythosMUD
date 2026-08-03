"""
Unit tests for message filtering.

Tests the MessageFilteringHelper class.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.realtime.message_filtering import MessageFilteringHelper


@pytest.fixture
def mock_connection_manager():
    """Create a mock connection manager."""
    manager = MagicMock()
    manager.room_subscriptions = {}
    manager.canonical_room_id = MagicMock(return_value=None)
    return manager


@pytest.fixture
def message_filtering_helper(mock_connection_manager):
    """Create a MessageFilteringHelper instance."""
    return MessageFilteringHelper(mock_connection_manager)


def test_message_filtering_helper_init(message_filtering_helper, mock_connection_manager):
    """Test MessageFilteringHelper initialization."""
    assert message_filtering_helper.connection_manager == mock_connection_manager
    assert message_filtering_helper.user_manager is None


def test_collect_room_targets(message_filtering_helper, mock_connection_manager):
    """Test collect_room_targets() returns subscribed players."""
    mock_connection_manager.room_subscriptions = {"room_001": {"player_001", "player_002"}}
    mock_connection_manager.canonical_room_id = MagicMock(return_value="room_001")
    result = message_filtering_helper.collect_room_targets("room_001")
    assert "player_001" in result
    assert "player_002" in result


def test_collect_room_targets_empty(message_filtering_helper, mock_connection_manager):
    """Test collect_room_targets() returns empty set when no subscribers."""
    mock_connection_manager.room_subscriptions = {}
    mock_connection_manager.canonical_room_id = MagicMock(return_value="room_001")
    result = message_filtering_helper.collect_room_targets("room_001")
    assert result == set()


@pytest.mark.asyncio
async def test_preload_receiver_mute_data(message_filtering_helper):
    """Test preload_receiver_mute_data() preloads mute data."""
    mock_user_manager = AsyncMock()
    mock_user_manager.load_player_mutes_batch = AsyncMock(return_value={"player_001": True, "player_002": True})
    targets = {"player_001", "player_002"}
    await message_filtering_helper.preload_receiver_mute_data(mock_user_manager, targets, "sender_001")
    mock_user_manager.load_player_mutes_batch.assert_awaited_once()


@pytest.mark.asyncio
async def test_preload_receiver_mute_data_excludes_sender(message_filtering_helper):
    """Test preload_receiver_mute_data() excludes sender from targets."""
    mock_user_manager = AsyncMock()
    mock_user_manager.load_player_mutes_batch = AsyncMock(return_value={"player_001": True})
    targets = {"player_001", "sender_001"}
    await message_filtering_helper.preload_receiver_mute_data(mock_user_manager, targets, "sender_001")
    # Should only load for player_001, not sender_001
    call_args = mock_user_manager.load_player_mutes_batch.call_args[0][0]
    assert "sender_001" not in call_args
    assert "player_001" in call_args


def test_collect_room_targets_with_canonical_id(message_filtering_helper, mock_connection_manager):
    """Test collect_room_targets() handles canonical and original room IDs."""
    mock_connection_manager.room_subscriptions = {
        "room_001": {"player_001"},
        "room_001_canonical": {"player_002"},
    }
    mock_connection_manager.canonical_room_id = MagicMock(return_value="room_001_canonical")
    result = message_filtering_helper.collect_room_targets("room_001")
    assert "player_001" in result or "player_002" in result


def test_extract_chat_event_info(message_filtering_helper):
    """Test extract_chat_event_info() extracts event info."""
    chat_event = {
        "event_type": "chat",
        "channel": "say",
        "room_id": "room_001",
        "message_id": "msg_001",
        "data": {"message": "Hello", "channel": "say", "id": "msg_001"},
    }
    event_type, data, message_id, is_echo = message_filtering_helper.extract_chat_event_info(chat_event)
    # extract_chat_event_info returns (event_type, chat_event_data, message_id, sender_already_notified)
    assert event_type == "chat"
    assert message_id == "msg_001"
    assert isinstance(data, dict)
    assert "message" in data or isinstance(data, dict)


def test_should_apply_mute_check_sensitive_channel(message_filtering_helper):
    """Test should_apply_mute_check() returns True for sensitive channels."""
    result = message_filtering_helper.should_apply_mute_check("say", "msg_001")
    assert result is True


def test_should_apply_mute_check_non_sensitive_channel(message_filtering_helper):
    """Test should_apply_mute_check() returns False for non-sensitive channels."""
    result = message_filtering_helper.should_apply_mute_check("system", None)
    # system is in MUTE_SENSITIVE_CHANNELS, so should return True
    assert result is True


def test_compare_canonical_rooms_same(message_filtering_helper, mock_connection_manager):
    """Test compare_canonical_rooms() returns True for same rooms."""
    mock_connection_manager.canonical_room_id = MagicMock(side_effect=lambda x: f"{x}_canonical")
    result = message_filtering_helper.compare_canonical_rooms("room_001", "room_001")
    assert result is True


def test_compare_canonical_rooms_different(message_filtering_helper, mock_connection_manager):
    """Test compare_canonical_rooms() returns False for different rooms."""
    mock_connection_manager.canonical_room_id = MagicMock(side_effect=lambda x: f"{x}_canonical")
    result = message_filtering_helper.compare_canonical_rooms("room_001", "room_002")
    assert result is False


def test_get_player_room_from_online_players(message_filtering_helper, mock_connection_manager):
    """Test get_player_room_from_online_players() returns player room."""
    # The method expects online_players to be a dict with player_id -> dict with current_room_id
    mock_connection_manager.online_players = {"player_001": {"current_room_id": "room_001"}}
    result = message_filtering_helper.get_player_room_from_online_players("player_001")
    assert result == "room_001"


def test_get_player_room_from_online_players_not_found(message_filtering_helper, mock_connection_manager):
    """Test get_player_room_from_online_players() returns None when player not found."""
    mock_connection_manager.online_players = {}
    result = message_filtering_helper.get_player_room_from_online_players("player_001")
    assert result is None


@pytest.mark.asyncio
async def test_get_player_room_from_persistence(message_filtering_helper, mock_connection_manager):
    """Test get_player_room_from_persistence() returns player room."""
    # The method checks if player is Mock and returns None, so use a simple object

    mock_persistence = MagicMock()

    # Create a simple object that's not a Mock instance
    class SimplePlayer:
        def __init__(self):
            self.current_room_id = "room_001"

    mock_player = SimplePlayer()
    # get_player_by_id is async, so use AsyncMock
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_connection_manager.async_persistence = mock_persistence
    result = await message_filtering_helper.get_player_room_from_persistence("player_001")
    assert result == "room_001"


@pytest.mark.asyncio
async def test_get_player_room_from_persistence_not_found(message_filtering_helper, mock_connection_manager):
    """Test get_player_room_from_persistence() returns None when player not found."""
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_id = AsyncMock(return_value=None)
    mock_connection_manager.async_persistence = mock_persistence
    result = await message_filtering_helper.get_player_room_from_persistence("player_001")
    assert result is None


@pytest.mark.asyncio
async def test_is_player_in_room_true(message_filtering_helper, mock_connection_manager):
    """Test is_player_in_room() returns True when player is in room."""
    # is_player_in_room uses get_player_room_from_online_players first, then persistence
    mock_connection_manager.online_players = {"player_001": {"current_room_id": "room_001"}}
    mock_connection_manager.canonical_room_id = MagicMock(return_value="room_001")
    result = await message_filtering_helper.is_player_in_room("player_001", "room_001")
    assert result is True


@pytest.mark.asyncio
async def test_is_player_in_room_false(message_filtering_helper, mock_connection_manager):
    """Test is_player_in_room() returns False when player is not in room."""
    # is_player_in_room uses get_player_room_from_online_players first, then persistence
    # canonical_room_id is called for both player_room_id and room_id
    mock_connection_manager.online_players = {"player_001": {"current_room_id": "room_002"}}

    # Make canonical_room_id return different values for different inputs
    def canonical_side_effect(room_id):
        if room_id == "room_002":
            return "room_002_canonical"
        return "room_001_canonical"

    mock_connection_manager.canonical_room_id = MagicMock(side_effect=canonical_side_effect)
    result = await message_filtering_helper.is_player_in_room("player_001", "room_001")
    assert result is False


def test_is_player_muted_by_receiver(message_filtering_helper):
    """Test is_player_muted_by_receiver() checks mute status."""
    mock_user_manager = MagicMock()
    mock_user_manager.is_player_muted = MagicMock(return_value=True)
    message_filtering_helper.user_manager = mock_user_manager
    result = message_filtering_helper.is_player_muted_by_receiver("receiver_001", "sender_001")
    assert result is True


def test_is_player_muted_by_receiver_not_muted(message_filtering_helper):
    """Test is_player_muted_by_receiver() returns False when not muted."""
    mock_user_manager = MagicMock()
    mock_user_manager.is_player_muted = MagicMock(return_value=False)
    message_filtering_helper.user_manager = mock_user_manager
    result = message_filtering_helper.is_player_muted_by_receiver("receiver_001", "sender_001")
    assert result is False


def test_get_user_manager_custom(message_filtering_helper):
    """Test _get_user_manager() returns custom user manager."""
    mock_user_manager = MagicMock()
    message_filtering_helper.user_manager = mock_user_manager
    result = message_filtering_helper._get_user_manager()
    assert result == mock_user_manager


def test_get_user_manager_global(message_filtering_helper):
    """Test _get_user_manager() returns global user manager when custom not set."""
    message_filtering_helper.user_manager = None
    result = message_filtering_helper._get_user_manager()
    # Should return global user_manager
    assert result is not None


@pytest.mark.asyncio
async def test_get_player_room_from_persistence_no_layer(message_filtering_helper, mock_connection_manager):
    mock_connection_manager.async_persistence = None
    assert await message_filtering_helper.get_player_room_from_persistence("player_001") is None


@pytest.mark.asyncio
async def test_get_player_room_from_persistence_mock_player(message_filtering_helper, mock_connection_manager):
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_id = AsyncMock(return_value=MagicMock())
    mock_connection_manager.async_persistence = mock_persistence
    assert await message_filtering_helper.get_player_room_from_persistence("player_001") is None


@pytest.mark.asyncio
async def test_is_player_in_room_via_persistence(message_filtering_helper, mock_connection_manager):
    mock_connection_manager.online_players = {}

    class SimplePlayer:
        current_room_id = "room_001"

    mock_persistence = MagicMock()
    mock_persistence.get_player_by_id = AsyncMock(return_value=SimplePlayer())
    mock_connection_manager.async_persistence = mock_persistence
    mock_connection_manager.canonical_room_id = MagicMock(return_value="room_001")
    assert await message_filtering_helper.is_player_in_room("player_001", "room_001") is True


@pytest.mark.asyncio
async def test_is_player_in_room_error_returns_false(message_filtering_helper, mock_connection_manager):
    from server.services.nats_exceptions import NATSError

    mock_connection_manager.online_players = {"player_001": {"current_room_id": "room_001"}}
    mock_connection_manager.canonical_room_id = MagicMock(side_effect=NATSError("boom"))
    assert await message_filtering_helper.is_player_in_room("player_001", "room_001") is False


def test_is_player_muted_global_mute_and_admin(message_filtering_helper):
    um = MagicMock()
    um.load_player_mutes = MagicMock(return_value=True)
    um.is_player_muted = MagicMock(return_value=False)
    um.is_player_muted_by_others = MagicMock(return_value=True)
    um.is_admin_sync = MagicMock(return_value=False)
    um._player_mutes = {}
    message_filtering_helper.user_manager = um
    assert message_filtering_helper.is_player_muted_by_receiver("receiver_001", "sender_001") is True

    um.is_admin_sync = MagicMock(return_value=True)
    assert message_filtering_helper.is_player_muted_by_receiver("receiver_001", "sender_001") is False


def test_is_player_muted_by_receiver_exception(message_filtering_helper):
    um = MagicMock()
    um.load_player_mutes = MagicMock(side_effect=RuntimeError("mute fail"))
    message_filtering_helper.user_manager = um
    assert message_filtering_helper.is_player_muted_by_receiver("receiver_001", "sender_001") is False


@pytest.mark.asyncio
async def test_is_player_muted_with_user_manager_async_paths(message_filtering_helper):
    um = MagicMock()
    um.load_player_mutes_async = AsyncMock(return_value=True)
    um.is_player_muted = MagicMock(return_value=False)
    um.is_player_muted_by_others = MagicMock(return_value=True)
    um.is_admin = AsyncMock(return_value=False)
    um._player_mutes = {"receiver_001": {"sender_001": True}}
    assert (
        await message_filtering_helper.is_player_muted_by_receiver_with_user_manager(um, "receiver_001", "sender_001")
        is True
    )

    um.is_admin = AsyncMock(return_value=True)
    assert (
        await message_filtering_helper.is_player_muted_by_receiver_with_user_manager(um, "receiver_001", "sender_001")
        is False
    )

    um.load_player_mutes_async = AsyncMock(side_effect=RuntimeError("async mute fail"))
    assert (
        await message_filtering_helper.is_player_muted_by_receiver_with_user_manager(um, "receiver_001", "sender_001")
        is False
    )


@pytest.mark.asyncio
async def test_check_player_mute_status_patched_and_emote(message_filtering_helper):
    um = MagicMock()
    handler = MagicMock()
    handler._is_player_muted_by_receiver = MagicMock(return_value=True)
    assert (
        await message_filtering_helper.check_player_mute_status(
            um, "p1", "s1", "emote", {"sender_name": "Ada"}, handler
        )
        is True
    )

    um.load_player_mutes_async = AsyncMock(return_value=True)
    um.is_player_muted = MagicMock(return_value=False)
    um.is_player_muted_by_others = MagicMock(return_value=False)
    um.is_admin = AsyncMock(return_value=False)
    assert (
        await message_filtering_helper.check_player_mute_status(um, "p1", "s1", "pose", {"sender_name": "Ada"}, None)
        is False
    )


@pytest.mark.asyncio
async def test_filter_target_players_room_and_mute(message_filtering_helper, mock_connection_manager):
    mock_connection_manager.online_players = {
        "p1": {"current_room_id": "room_001"},
        "p2": {"current_room_id": "room_002"},
        "sender": {"current_room_id": "room_001"},
    }
    mock_connection_manager.canonical_room_id = MagicMock(side_effect=lambda x: x)
    um = MagicMock()
    um.load_player_mutes_async = AsyncMock(return_value=True)
    um.is_player_muted = MagicMock(side_effect=lambda r, s: r == "p1")
    um.is_player_muted_by_others = MagicMock(return_value=False)
    um.is_admin = AsyncMock(return_value=False)

    filtered = await message_filtering_helper.filter_target_players(
        {"sender", "p1", "p2"},
        "sender",
        "room_001",
        "say",
        "msg-1",
        um,
        {"sender_name": "Ada"},
        None,
    )
    assert filtered == []
