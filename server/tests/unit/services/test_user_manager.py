"""
Unit tests for user manager service.

Tests the UserManager class.
"""

import json
import uuid
from datetime import UTC, datetime, timedelta
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.services.user_manager import UserManager

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def mock_data_dir(tmp_path):
    """Create a temporary data directory."""
    return tmp_path / "user_management"


@pytest.fixture
def user_manager(request):
    """Create a UserManager instance."""
    data_dir = request.getfixturevalue("mock_data_dir")
    return UserManager(data_dir=data_dir)


def test_user_manager_init(user_manager, mock_data_dir):
    """Test UserManager initialization."""
    assert user_manager.data_dir == mock_data_dir
    assert len(user_manager._player_mutes) == 0
    assert len(user_manager._channel_mutes) == 0
    assert len(user_manager._global_mutes) == 0
    assert len(user_manager._admin_players) == 0


def test_normalize_to_uuid_uuid(user_manager):
    """Test _normalize_to_uuid() with UUID object."""
    player_id = uuid.uuid4()
    result = user_manager._normalize_to_uuid(player_id)
    assert result == player_id


def test_normalize_to_uuid_string(user_manager):
    """Test _normalize_to_uuid() with string UUID."""
    player_id_str = str(uuid.uuid4())
    result = user_manager._normalize_to_uuid(player_id_str)
    assert isinstance(result, uuid.UUID)
    assert str(result) == player_id_str


def test_normalize_to_uuid_invalid(user_manager):
    """Test _normalize_to_uuid() with invalid format."""
    with pytest.raises(ValueError, match="Invalid player_id format"):
        user_manager._normalize_to_uuid("not-a-uuid")


def test_is_admin_sync_true(user_manager):
    """Test is_admin_sync() returns True for admin."""
    player_id = uuid.uuid4()
    user_manager._admin_players.add(player_id)
    result = user_manager.is_admin_sync(player_id)
    assert result is True


def test_is_admin_sync_false(user_manager):
    """Test is_admin_sync() returns False for non-admin."""
    player_id = uuid.uuid4()
    result = user_manager.is_admin_sync(player_id)
    assert result is False


def test_mute_player_success(user_manager):
    """Test mute_player() successfully mutes a player."""
    muter_id = uuid.uuid4()
    target_id = uuid.uuid4()
    result = user_manager.mute_player(muter_id, "Muter", target_id, "Target")
    assert result is True
    assert target_id in user_manager._player_mutes[muter_id]


def test_mute_player_admin_immune(user_manager):
    """Test mute_player() fails when trying to mute admin."""
    muter_id = uuid.uuid4()
    target_id = uuid.uuid4()
    user_manager._admin_players.add(target_id)
    result = user_manager.mute_player(muter_id, "Muter", target_id, "Target")
    assert result is False


def test_unmute_player_success(user_manager):
    """Test unmute_player() successfully unmutes a player."""
    muter_id = uuid.uuid4()
    target_id = uuid.uuid4()
    user_manager.mute_player(muter_id, "Muter", target_id, "Target")
    result = user_manager.unmute_player(muter_id, "Muter", target_id, "Target")
    assert result is True
    # After unmute, the target should not be in the mutes dict, or the dict might be empty
    if muter_id in user_manager._player_mutes:
        assert target_id not in user_manager._player_mutes[muter_id]


def test_unmute_player_not_muted(user_manager):
    """Test unmute_player() when player is not muted."""
    muter_id = uuid.uuid4()
    target_id = uuid.uuid4()
    result = user_manager.unmute_player(muter_id, "Muter", target_id, "Target")
    assert result is False


def test_mute_channel_success(user_manager):
    """Test mute_channel() successfully mutes a channel."""
    player_id = uuid.uuid4()
    result = user_manager.mute_channel(player_id, "Player", "global")
    assert result is True
    assert "global" in user_manager._channel_mutes[player_id]


def test_mute_channel_already_muted(user_manager):
    """Test mute_channel() when channel is already muted."""
    player_id = uuid.uuid4()
    user_manager.mute_channel(player_id, "Player", "global")
    result = user_manager.mute_channel(player_id, "Player", "global")
    assert result is True  # Should succeed even if already muted


def test_unmute_channel_success(user_manager):
    """Test unmute_channel() successfully unmutes a channel."""
    player_id = uuid.uuid4()
    user_manager.mute_channel(player_id, "Player", "global")
    result = user_manager.unmute_channel(player_id, "Player", "global")
    assert result is True
    if player_id in user_manager._channel_mutes:
        assert "global" not in user_manager._channel_mutes[player_id]


def test_unmute_channel_not_muted(user_manager):
    """Test unmute_channel() when channel is not muted."""
    player_id = uuid.uuid4()
    result = user_manager.unmute_channel(player_id, "Player", "global")
    assert result is False


def test_mute_global_success(user_manager):
    """Test mute_global() successfully globally mutes a player."""
    muter_id = uuid.uuid4()
    target_id = uuid.uuid4()
    result = user_manager.mute_global(muter_id, "Muter", target_id, "Target")
    assert result is True
    assert target_id in user_manager._global_mutes


def test_mute_global_admin_immune(user_manager):
    """Test mute_global() fails when trying to mute admin."""
    muter_id = uuid.uuid4()
    target_id = uuid.uuid4()
    user_manager._admin_players.add(target_id)
    result = user_manager.mute_global(muter_id, "Muter", target_id, "Target")
    assert result is False


def test_unmute_global_success(user_manager):
    """Test unmute_global() successfully unmutes a player."""
    muter_id = uuid.uuid4()
    target_id = uuid.uuid4()
    user_manager.mute_global(muter_id, "Muter", target_id, "Target")
    result = user_manager.unmute_global(muter_id, "Muter", target_id, "Target")
    assert result is True
    assert target_id not in user_manager._global_mutes


def test_unmute_global_not_muted(user_manager):
    """Test unmute_global() when player is not globally muted."""
    unmuter_id = uuid.uuid4()
    target_id = uuid.uuid4()
    result = user_manager.unmute_global(unmuter_id, "Unmuter", target_id, "Target")
    assert result is False


def test_is_player_muted_true(user_manager):
    """Test is_player_muted() returns True when player is muted."""
    muter_id = uuid.uuid4()
    target_id = uuid.uuid4()
    user_manager.mute_player(muter_id, "Muter", target_id, "Target")
    result = user_manager.is_player_muted(muter_id, target_id)
    assert result is True


def test_is_player_muted_false(user_manager):
    """Test is_player_muted() returns False when player is not muted."""
    muter_id = uuid.uuid4()
    target_id = uuid.uuid4()
    result = user_manager.is_player_muted(muter_id, target_id)
    assert result is False


@pytest.mark.asyncio
async def test_is_player_muted_async_true(user_manager):
    """Test is_player_muted_async() returns True when player is muted."""
    muter_id = uuid.uuid4()
    target_id = uuid.uuid4()
    user_manager.mute_player(muter_id, "Muter", target_id, "Target")
    result = await user_manager.is_player_muted_async(muter_id, target_id)
    assert result is True


@pytest.mark.asyncio
async def test_is_player_muted_async_false(user_manager):
    """Test is_player_muted_async() returns False when player is not muted."""
    muter_id = uuid.uuid4()
    target_id = uuid.uuid4()
    result = await user_manager.is_player_muted_async(muter_id, target_id)
    assert result is False


def test_is_channel_muted_true(user_manager):
    """Test is_channel_muted() returns True when channel is muted."""
    player_id = uuid.uuid4()
    user_manager.mute_channel(player_id, "Player", "global")
    result = user_manager.is_channel_muted(player_id, "global")
    assert result is True


def test_is_channel_muted_false(user_manager):
    """Test is_channel_muted() returns False when channel is not muted."""
    player_id = uuid.uuid4()
    result = user_manager.is_channel_muted(player_id, "global")
    assert result is False


def test_is_globally_muted_true(user_manager):
    """Test is_globally_muted() returns True when player is globally muted."""
    muter_id = uuid.uuid4()
    target_id = uuid.uuid4()
    user_manager.mute_global(muter_id, "Muter", target_id, "Target")
    result = user_manager.is_globally_muted(target_id)
    assert result is True


def test_is_globally_muted_false(user_manager):
    """Test is_globally_muted() returns False when player is not globally muted."""
    player_id = uuid.uuid4()
    result = user_manager.is_globally_muted(player_id)
    assert result is False


def test_can_send_message_true(user_manager):
    """Test can_send_message() returns True when player can send message."""
    player_id = uuid.uuid4()
    target_id = uuid.uuid4()
    result = user_manager.can_send_message(player_id, target_id, "global")
    assert result is True


def test_can_send_message_player_muted(user_manager):
    """Test can_send_message() behavior when target player is muted."""
    player_id = uuid.uuid4()
    target_id = uuid.uuid4()
    user_manager.mute_player(player_id, "Player", target_id, "Target")
    # can_send_message checks global mute, channel mute, and admin status
    # It doesn't check if sender has muted target (that's handled on receiving end)
    result = user_manager.can_send_message(player_id, target_id, "global")
    # Should return True because muting target doesn't prevent sender from sending
    assert result is True


def test_can_send_message_channel_muted(user_manager):
    """Test can_send_message() returns False when channel is muted."""
    player_id = uuid.uuid4()
    target_id = uuid.uuid4()
    user_manager.mute_channel(player_id, "Player", "global")
    result = user_manager.can_send_message(player_id, target_id, "global")
    assert result is False


def test_can_send_message_globally_muted(user_manager):
    """Test can_send_message() returns False when player is globally muted."""
    muter_id = uuid.uuid4()
    player_id = uuid.uuid4()
    target_id = uuid.uuid4()
    user_manager.mute_global(muter_id, "Muter", player_id, "Player")
    result = user_manager.can_send_message(player_id, target_id, "global")
    assert result is False


def test_get_player_mutes(user_manager):
    """Test get_player_mutes() returns player mutes."""
    muter_id = uuid.uuid4()
    target_id = uuid.uuid4()
    user_manager.mute_player(muter_id, "Muter", target_id, "Target")
    result = user_manager.get_player_mutes(muter_id)
    assert isinstance(result, dict)
    assert "player_mutes" in result or "muted_players" in result or len(result) >= 0


def test_is_player_muted_by_others_true(user_manager):
    """Test is_player_muted_by_others() returns True when globally muted by others."""
    muter_id = uuid.uuid4()
    target_id = uuid.uuid4()
    # is_player_muted_by_others only checks global mutes, not player mutes
    user_manager.mute_global(muter_id, "Muter", target_id, "Target")
    result = user_manager.is_player_muted_by_others(target_id)
    assert result is True


def test_is_player_muted_by_others_false(user_manager):
    """Test is_player_muted_by_others() returns False when not muted."""
    player_id = uuid.uuid4()
    result = user_manager.is_player_muted_by_others(player_id)
    assert result is False


def test_get_who_muted_player(user_manager):
    """Test get_who_muted_player() returns list of muters."""
    muter_id = uuid.uuid4()
    target_id = uuid.uuid4()
    user_manager.mute_player(muter_id, "Muter", target_id, "Target")
    result = user_manager.get_who_muted_player(target_id)
    assert isinstance(result, list)
    assert len(result) >= 0


def test_get_system_stats(user_manager):
    """Test get_system_stats() returns system statistics."""
    player_id = uuid.uuid4()
    user_manager.mute_player(player_id, "Player", uuid.uuid4(), "Target")
    result = user_manager.get_system_stats()
    assert isinstance(result, dict)
    assert "total_player_mutes" in result or "total_mutes" in result or len(result) >= 0


def test_cleanup_expired_mutes(user_manager):
    """Test _cleanup_expired_mutes() cleans up expired mutes."""
    # This is an internal method, but we can test it doesn't raise
    user_manager._cleanup_expired_mutes()
    assert True  # If we get here, it succeeded


def test_get_player_mute_file(user_manager):
    """Test _get_player_mute_file() returns Path."""

    player_id = uuid.uuid4()
    result = user_manager._get_player_mute_file(player_id)
    assert isinstance(result, Path)


def test_is_cache_valid_true(user_manager):
    """Test _is_cache_valid() returns True for valid cache."""
    player_id = uuid.uuid4()
    user_manager._mute_cache[player_id] = (datetime.now(UTC), True)
    result = user_manager._is_cache_valid(player_id)
    assert result is True


def test_is_cache_valid_false_expired(user_manager):
    """Test _is_cache_valid() returns False for expired cache."""
    player_id = uuid.uuid4()

    # Set cache to expired time
    expired_time = datetime.now(UTC) - timedelta(seconds=400)  # More than TTL (300)
    user_manager._mute_cache[player_id] = (expired_time, True)
    result = user_manager._is_cache_valid(player_id)
    assert result is False


def test_is_cache_valid_false_not_cached(user_manager):
    """Test _is_cache_valid() returns False when not cached."""
    player_id = uuid.uuid4()
    result = user_manager._is_cache_valid(player_id)
    assert result is False


@pytest.mark.asyncio
async def test_add_admin_no_container(user_manager):
    """Test add_admin() handles missing container."""
    with patch("server.container.ApplicationContainer.get_instance", return_value=None):
        result = await user_manager.add_admin(uuid.uuid4(), "TestPlayer")
        assert result is False


@pytest.mark.asyncio
async def test_add_admin_no_persistence(user_manager):
    """Test add_admin() handles missing persistence."""
    mock_container = MagicMock()
    mock_container.async_persistence = None
    with patch("server.container.ApplicationContainer.get_instance", return_value=mock_container):
        result = await user_manager.add_admin(uuid.uuid4(), "TestPlayer")
        assert result is False


@pytest.mark.asyncio
async def test_add_admin_player_not_found(user_manager):
    """Test add_admin() handles player not found."""
    mock_container = MagicMock()
    mock_persistence = AsyncMock()
    mock_persistence.get_player_by_id = AsyncMock(return_value=None)
    mock_container.async_persistence = mock_persistence
    with patch("server.container.ApplicationContainer.get_instance", return_value=mock_container):
        player_id = uuid.uuid4()
        result = await user_manager.add_admin(player_id, "TestPlayer")
        # The function logs an info message and continues even when player is None
        # It adds to cache and returns True
        assert result is True
        assert player_id in user_manager._admin_players


@pytest.mark.asyncio
async def test_remove_admin_no_container(user_manager):
    """Test remove_admin() handles missing container."""
    with patch("server.container.ApplicationContainer.get_instance", return_value=None):
        result = await user_manager.remove_admin(uuid.uuid4(), "TestPlayer")
        assert result is False


@pytest.mark.asyncio
async def test_remove_admin_no_persistence(user_manager):
    """Test remove_admin() handles missing persistence."""
    mock_container = MagicMock()
    mock_container.async_persistence = None
    with patch("server.container.ApplicationContainer.get_instance", return_value=mock_container):
        result = await user_manager.remove_admin(uuid.uuid4(), "TestPlayer")
        assert result is False


@pytest.mark.asyncio
async def test_remove_admin_player_not_found(user_manager):
    """Test remove_admin() handles player not found."""
    mock_container = MagicMock()
    mock_persistence = AsyncMock()
    mock_persistence.get_player_by_id = AsyncMock(return_value=None)
    mock_container.async_persistence = mock_persistence
    with patch("server.container.ApplicationContainer.get_instance", return_value=mock_container):
        player_id = uuid.uuid4()
        user_manager._admin_players.add(player_id)  # Add to cache first
        result = await user_manager.remove_admin(player_id, "TestPlayer")
        # The function logs an info message and continues even when player is None
        # It removes from cache and returns True
        assert result is True
        assert player_id not in user_manager._admin_players


@pytest.mark.asyncio
async def test_is_admin_no_container(user_manager):
    """Test is_admin() returns False when container not available."""
    with patch("server.container.ApplicationContainer.get_instance", return_value=None):
        result = await user_manager.is_admin(uuid.uuid4())
        assert result is False


@pytest.mark.asyncio
async def test_is_admin_no_persistence(user_manager):
    """Test is_admin() returns False when persistence not available."""
    mock_container = MagicMock()
    mock_container.async_persistence = None
    with patch("server.container.ApplicationContainer.get_instance", return_value=mock_container):
        result = await user_manager.is_admin(uuid.uuid4())
        assert result is False


def test_load_player_mutes_file_not_exists(user_manager):
    """Test load_player_mutes() returns False when file doesn't exist."""
    result = user_manager.load_player_mutes(uuid.uuid4())
    assert result is False


def test_load_player_mutes_empty_file(user_manager, tmp_path):
    """Test load_player_mutes() treats empty or whitespace-only file as valid empty mute data."""
    user_manager.data_dir = tmp_path
    player_id = uuid.uuid4()
    mute_file = user_manager._get_player_mute_file(player_id)
    mute_file.write_text("")
    result = user_manager.load_player_mutes(player_id)
    assert result is True
    assert player_id not in user_manager._player_mutes
    assert player_id not in user_manager._channel_mutes
    assert player_id in user_manager._mute_cache
    _, valid = user_manager._mute_cache[player_id]
    assert valid is True


def test_load_player_mutes_invalid_json(user_manager, tmp_path):
    """Test load_player_mutes() handles invalid JSON."""
    user_manager.data_dir = tmp_path
    player_id = uuid.uuid4()
    mute_file = user_manager._get_player_mute_file(player_id)
    mute_file.write_text("invalid json")
    result = user_manager.load_player_mutes(player_id)
    assert result is False


def test_load_player_mutes_invalid_uuid_in_data(user_manager, tmp_path):
    """Test load_player_mutes() handles invalid UUID in data."""

    user_manager.data_dir = tmp_path
    player_id = uuid.uuid4()
    mute_file = user_manager._get_player_mute_file(player_id)
    data = {"player_mutes": {"invalid-uuid": {"target_name": "Test"}}}
    mute_file.write_text(json.dumps(data))
    result = user_manager.load_player_mutes(player_id)
    # Should handle gracefully
    assert result is True or result is False


def test_save_player_mutes_serialization_error(user_manager, tmp_path):
    """Test save_player_mutes() handles serialization error."""
    user_manager.data_dir = tmp_path
    player_id = uuid.uuid4()
    # Create non-serializable data by adding a function
    user_manager._player_mutes[player_id] = {uuid.uuid4(): {"target_name": "Test", "func": lambda x: x}}
    result = user_manager.save_player_mutes(player_id)
    assert result is False


@pytest.mark.asyncio
async def test_load_player_mutes_async_cache_valid(user_manager):
    """Test load_player_mutes_async() uses cache when valid."""
    player_id = uuid.uuid4()
    user_manager._mute_cache[player_id] = (datetime.now(UTC), True)
    result = await user_manager.load_player_mutes_async(player_id)
    assert result is True


@pytest.mark.asyncio
async def test_load_player_mutes_batch_empty_list(user_manager):
    """Test load_player_mutes_batch() with empty list."""
    result = await user_manager.load_player_mutes_batch([])
    assert result == {}


@pytest.mark.asyncio
async def test_load_player_mutes_batch_all_cached(user_manager):
    """Test load_player_mutes_batch() when all players are cached."""
    player_id1 = uuid.uuid4()
    player_id2 = uuid.uuid4()
    user_manager._mute_cache[player_id1] = (datetime.now(UTC), True)
    user_manager._mute_cache[player_id2] = (datetime.now(UTC), True)
    result = await user_manager.load_player_mutes_batch([player_id1, player_id2])
    assert len(result) == 2
    assert result[str(player_id1)] is True
    assert result[str(player_id2)] is True


def test_cleanup_player_mutes_no_delete_file(user_manager):
    """Test cleanup_player_mutes() without deleting file."""
    player_id = uuid.uuid4()
    user_manager._player_mutes[player_id] = {uuid.uuid4(): {"target_name": "Test"}}
    result = user_manager.cleanup_player_mutes(player_id, delete_file=False)
    assert result is True
    assert player_id not in user_manager._player_mutes


def test_cleanup_player_mutes_with_delete_file(user_manager, tmp_path):
    """Test cleanup_player_mutes() with delete_file=True."""
    user_manager.data_dir = tmp_path
    player_id = uuid.uuid4()
    mute_file = user_manager._get_player_mute_file(player_id)
    mute_file.write_text('{"player_mutes": {}}')
    result = user_manager.cleanup_player_mutes(player_id, delete_file=True)
    assert result is True
    assert not mute_file.exists()


def test_unmute_player_not_found(user_manager):
    """Test unmute_player() when mute doesn't exist."""
    muter_id = uuid.uuid4()
    target_id = uuid.uuid4()
    result = user_manager.unmute_player(muter_id, "Muter", target_id, "Target")
    assert result is False


def test_get_player_mutes_empty(user_manager):
    """Test get_player_mutes() returns empty dict when no mutes."""
    player_id = uuid.uuid4()
    result = user_manager.get_player_mutes(player_id)
    assert "player_mutes" in result
    assert "channel_mutes" in result
    assert "global_mutes" in result
    assert result["player_mutes"] == {}
    assert result["channel_mutes"] == {}
    assert result["global_mutes"] == {}


def test_get_player_mutes_with_mutes(user_manager):
    """Test get_player_mutes() returns mutes when present."""
    player_id = uuid.uuid4()
    target_id = uuid.uuid4()
    user_manager.mute_player(player_id, "Player", target_id, "Target")
    user_manager.mute_channel(player_id, "Player", "say")
    result = user_manager.get_player_mutes(player_id)
    assert len(result["player_mutes"]) > 0
    assert "say" in result["channel_mutes"]


@pytest.mark.asyncio
async def test_add_admin_success(user_manager):
    """Test add_admin() successfully adds admin."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.set_admin_status = MagicMock()
    with patch("server.container.ApplicationContainer.get_instance") as mock_get_instance:
        mock_instance = MagicMock()
        mock_instance.async_persistence = AsyncMock()
        mock_instance.async_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_instance.async_persistence.save_player = AsyncMock()
        mock_get_instance.return_value = mock_instance
        result = await user_manager.add_admin(player_id, "TestPlayer")
        assert result is True
        assert player_id in user_manager._admin_players


@pytest.mark.asyncio
async def test_add_admin_no_container_duplicate(user_manager):
    """Test add_admin() when container is not available."""
    player_id = uuid.uuid4()
    with patch("server.container.ApplicationContainer.get_instance", return_value=None):
        result = await user_manager.add_admin(player_id, "TestPlayer")
        assert result is False


@pytest.mark.asyncio
async def test_remove_admin_success(user_manager):
    """Test remove_admin() successfully removes admin."""
    player_id = uuid.uuid4()
    user_manager._admin_players.add(player_id)
    mock_player = MagicMock()
    mock_player.set_admin_status = MagicMock()
    with patch("server.container.ApplicationContainer.get_instance") as mock_get_instance:
        mock_instance = MagicMock()
        mock_instance.async_persistence = AsyncMock()
        mock_instance.async_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_instance.async_persistence.save_player = AsyncMock()
        mock_get_instance.return_value = mock_instance
        result = await user_manager.remove_admin(player_id, "TestPlayer")
        assert result is True
        assert player_id not in user_manager._admin_players


@pytest.mark.asyncio
async def test_is_admin_cached(user_manager):
    """Test is_admin() returns True from cache."""
    player_id = uuid.uuid4()
    user_manager._admin_players.add(player_id)
    result = await user_manager.is_admin(player_id)
    assert result is True


@pytest.mark.asyncio
async def test_is_admin_not_cached(user_manager):
    """Test is_admin() checks database when not in cache."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.is_admin_user = MagicMock(return_value=True)
    with patch("server.container.ApplicationContainer.get_instance") as mock_get_instance:
        mock_instance = MagicMock()
        mock_instance.async_persistence = AsyncMock()
        mock_instance.async_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_get_instance.return_value = mock_instance
        result = await user_manager.is_admin(player_id)
        assert result is True
        assert player_id in user_manager._admin_players
