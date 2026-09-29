"""
Unit tests for user manager service.

Tests the UserManager class. Mute persistence goes through PlayerMuteRepository (#681); these
tests swap in an in-memory fake. The real procedures are covered by
server/tests/integration/test_player_aliases_and_mutes_db.py.
"""

import uuid
from datetime import UTC, datetime, timedelta
from typing import override
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.exceptions import DatabaseError
from server.persistence.repositories.player_mute_repository import MuteType, PlayerMute, PlayerMuteRepository
from server.services.user_manager import UserManager

# pyright: reportPrivateUsage=false
# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


class _FakeMuteRepository(PlayerMuteRepository):
    """In-memory stand-in for the player_mutes procedures."""

    def __init__(self, active: list[PlayerMute] | None = None, *, fail: bool = False) -> None:
        self.rows: list[PlayerMute] = list(active or [])
        self.deleted: list[tuple[MuteType, uuid.UUID | None, uuid.UUID | None, str | None]] = []
        self.fail: bool = fail

    @override
    async def load_active(self) -> list[PlayerMute]:
        return list(self.rows)

    @override
    async def upsert(self, mute: PlayerMute) -> None:
        if self.fail:
            raise DatabaseError("db down")
        self.rows.append(mute)

    @override
    async def delete(
        self, mute_type: MuteType, muter_id: uuid.UUID | None, target_id: uuid.UUID | None, channel: str | None
    ) -> bool:
        if self.fail:
            raise DatabaseError("db down")
        self.deleted.append((mute_type, muter_id, target_id, channel))
        return True


@pytest.fixture
def mute_repo() -> _FakeMuteRepository:
    return _FakeMuteRepository()


@pytest.fixture
def user_manager(mute_repo: _FakeMuteRepository) -> UserManager:
    """Create a UserManager instance backed by the fake repository."""
    return UserManager(mute_repository=mute_repo)


def _mute(mute_type: MuteType, *, target: uuid.UUID | None = None, channel: str | None = None) -> PlayerMute:
    return PlayerMute(
        mute_type=mute_type,
        muter_id=uuid.uuid4(),
        muter_name="Muter",
        target_id=target,
        target_name="Target" if target else None,
        channel=channel,
        reason="",
        muted_at=datetime.now(UTC),
        expires_at=None,
    )


def test_user_manager_init(user_manager: UserManager):
    """Test UserManager initialization."""
    assert len(user_manager._player_mutes) == 0
    assert len(user_manager._channel_mutes) == 0
    assert len(user_manager._global_mutes) == 0
    assert len(user_manager._admin_players) == 0


def test_normalize_to_uuid_uuid(user_manager: UserManager):
    """Test _normalize_to_uuid() with UUID object."""
    player_id = uuid.uuid4()
    result = user_manager._normalize_to_uuid(player_id)
    assert result == player_id


def test_normalize_to_uuid_string(user_manager: UserManager):
    """Test _normalize_to_uuid() with string UUID."""
    player_id_str = str(uuid.uuid4())
    result = user_manager._normalize_to_uuid(player_id_str)
    assert isinstance(result, uuid.UUID)
    assert str(result) == player_id_str


def test_normalize_to_uuid_invalid(user_manager: UserManager):
    """Test _normalize_to_uuid() with invalid format."""
    with pytest.raises(ValueError, match="Invalid player_id format"):
        _ = user_manager._normalize_to_uuid("not-a-uuid")


def test_is_admin_sync_true(user_manager: UserManager):
    """Test is_admin_sync() returns True for admin."""
    player_id = uuid.uuid4()
    user_manager._admin_players.add(player_id)
    result = user_manager.is_admin_sync(player_id)
    assert result is True


def test_is_admin_sync_false(user_manager: UserManager):
    """Test is_admin_sync() returns False for non-admin."""
    player_id = uuid.uuid4()
    result = user_manager.is_admin_sync(player_id)
    assert result is False


@pytest.mark.asyncio
async def test_load_all_mutes_indexes_every_type(user_manager: UserManager, mute_repo: _FakeMuteRepository):
    """load_all_mutes() fills all three in-memory indexes from the repository."""
    target = uuid.uuid4()
    player_mute = _mute("player", target=target)
    channel_mute = _mute("channel", channel="ooc")
    global_mute = _mute("global", target=target)
    mute_repo.rows = [player_mute, channel_mute, global_mute]
    user_manager._global_mutes[uuid.uuid4()] = {}  # stale entry is replaced, not merged

    assert await user_manager.load_all_mutes() == 3

    assert user_manager.is_player_muted(player_mute.muter_id, target)
    assert user_manager.is_channel_muted(channel_mute.muter_id, "ooc")
    assert list(user_manager._global_mutes) == [target]
    # A global mute is visible without the muter ever being "loaded" (the JSON-era bug)
    assert user_manager.is_globally_muted(target)
    assert user_manager._global_mutes[target]["muted_by"] == global_mute.muter_id


@pytest.mark.asyncio
async def test_mute_player_success(user_manager: UserManager, mute_repo: _FakeMuteRepository):
    """Test mute_player() persists, then indexes the mute."""
    muter_id = uuid.uuid4()
    target_id = uuid.uuid4()
    result = await user_manager.mute_player(muter_id, "Muter", target_id, "Target", 5, "spam")
    assert result is True
    assert target_id in user_manager._player_mutes[muter_id]
    [persisted] = mute_repo.rows
    assert (persisted.mute_type, persisted.muter_id, persisted.target_id) == ("player", muter_id, target_id)
    assert persisted.reason == "spam"
    assert persisted.expires_at is not None
    assert persisted.expires_at - persisted.muted_at == timedelta(minutes=5)


@pytest.mark.asyncio
async def test_mute_player_database_failure_leaves_memory_untouched(mute_repo: _FakeMuteRepository):
    """A failed write must not leave a mute that would silently vanish on restart."""
    mute_repo.fail = True
    user_manager = UserManager(mute_repository=mute_repo)
    muter_id = uuid.uuid4()
    result = await user_manager.mute_player(muter_id, "Muter", uuid.uuid4(), "Target")
    assert result is False
    assert muter_id not in user_manager._player_mutes


@pytest.mark.asyncio
async def test_mute_player_admin_immune(user_manager: UserManager, mute_repo: _FakeMuteRepository):
    """Test mute_player() fails when trying to mute admin."""
    muter_id = uuid.uuid4()
    target_id = uuid.uuid4()
    user_manager._admin_players.add(target_id)
    result = await user_manager.mute_player(muter_id, "Muter", target_id, "Target")
    assert result is False
    assert not mute_repo.rows


@pytest.mark.asyncio
async def test_unmute_player_success(user_manager: UserManager, mute_repo: _FakeMuteRepository):
    """Test unmute_player() successfully unmutes a player."""
    muter_id = uuid.uuid4()
    target_id = uuid.uuid4()
    _ = await user_manager.mute_player(muter_id, "Muter", target_id, "Target")
    result = await user_manager.unmute_player(muter_id, "Muter", target_id, "Target")
    assert result is True
    assert muter_id not in user_manager._player_mutes
    assert mute_repo.deleted == [("player", muter_id, target_id, None)]


@pytest.mark.asyncio
async def test_unmute_player_not_muted(user_manager: UserManager, mute_repo: _FakeMuteRepository):
    """Test unmute_player() when player is not muted."""
    result = await user_manager.unmute_player(uuid.uuid4(), "Muter", uuid.uuid4(), "Target")
    assert result is False
    assert not mute_repo.deleted


@pytest.mark.asyncio
async def test_mute_channel_success(user_manager: UserManager, mute_repo: _FakeMuteRepository):
    """Test mute_channel() successfully mutes a channel."""
    player_id = uuid.uuid4()
    result = await user_manager.mute_channel(player_id, "Player", "global")
    assert result is True
    assert "global" in user_manager._channel_mutes[player_id]
    [persisted] = mute_repo.rows
    assert (persisted.mute_type, persisted.channel, persisted.target_id) == ("channel", "global", None)


@pytest.mark.asyncio
async def test_mute_channel_already_muted(user_manager: UserManager):
    """Test mute_channel() when channel is already muted."""
    player_id = uuid.uuid4()
    _ = await user_manager.mute_channel(player_id, "Player", "global")
    result = await user_manager.mute_channel(player_id, "Player", "global")
    assert result is True  # Should succeed even if already muted


@pytest.mark.asyncio
async def test_unmute_channel_success(user_manager: UserManager, mute_repo: _FakeMuteRepository):
    """Test unmute_channel() successfully unmutes a channel."""
    player_id = uuid.uuid4()
    _ = await user_manager.mute_channel(player_id, "Player", "global")
    result = await user_manager.unmute_channel(player_id, "Player", "global")
    assert result is True
    assert player_id not in user_manager._channel_mutes
    assert mute_repo.deleted == [("channel", player_id, None, "global")]


@pytest.mark.asyncio
async def test_unmute_channel_not_muted(user_manager: UserManager):
    """Test unmute_channel() when channel is not muted."""
    result = await user_manager.unmute_channel(uuid.uuid4(), "Player", "global")
    assert result is False


@pytest.mark.asyncio
async def test_mute_global_success(user_manager: UserManager, mute_repo: _FakeMuteRepository):
    """Test mute_global() successfully globally mutes a player."""
    muter_id = uuid.uuid4()
    target_id = uuid.uuid4()
    result = await user_manager.mute_global(muter_id, "Muter", target_id, "Target")
    assert result is True
    assert target_id in user_manager._global_mutes
    assert mute_repo.rows[0].mute_type == "global"


@pytest.mark.asyncio
async def test_mute_global_admin_immune(user_manager: UserManager):
    """Test mute_global() fails when trying to mute admin."""
    target_id = uuid.uuid4()
    user_manager._admin_players.add(target_id)
    result = await user_manager.mute_global(uuid.uuid4(), "Muter", target_id, "Target")
    assert result is False


@pytest.mark.asyncio
async def test_unmute_global_success(user_manager: UserManager, mute_repo: _FakeMuteRepository):
    """Test unmute_global() successfully unmutes a player."""
    muter_id = uuid.uuid4()
    target_id = uuid.uuid4()
    _ = await user_manager.mute_global(muter_id, "Muter", target_id, "Target")
    result = await user_manager.unmute_global(uuid.uuid4(), "Other admin", target_id, "Target")
    assert result is True
    assert target_id not in user_manager._global_mutes
    assert mute_repo.deleted == [("global", None, target_id, None)]


@pytest.mark.asyncio
async def test_unmute_global_not_muted(user_manager: UserManager):
    """Test unmute_global() when player is not globally muted."""
    result = await user_manager.unmute_global(uuid.uuid4(), "Unmuter", uuid.uuid4(), "Target")
    assert result is False


@pytest.mark.asyncio
async def test_is_player_muted_true(user_manager: UserManager):
    """Test is_player_muted() returns True when player is muted."""
    muter_id = uuid.uuid4()
    target_id = uuid.uuid4()
    _ = await user_manager.mute_player(muter_id, "Muter", target_id, "Target")
    assert user_manager.is_player_muted(muter_id, target_id) is True


def test_is_player_muted_false(user_manager: UserManager):
    """Test is_player_muted() returns False when player is not muted."""
    assert user_manager.is_player_muted(uuid.uuid4(), uuid.uuid4()) is False


def test_is_player_muted_expired(user_manager: UserManager):
    """An expired in-memory mute is dropped on read."""
    muter_id = uuid.uuid4()
    target_id = uuid.uuid4()
    user_manager._player_mutes[muter_id] = {target_id: {"expires_at": datetime.now(UTC) - timedelta(minutes=1)}}
    assert user_manager.is_player_muted(muter_id, target_id) is False
    assert muter_id not in user_manager._player_mutes


@pytest.mark.asyncio
async def test_is_player_muted_async_true(user_manager: UserManager):
    """Test is_player_muted_async() returns True when player is muted."""
    muter_id = uuid.uuid4()
    target_id = uuid.uuid4()
    _ = await user_manager.mute_player(muter_id, "Muter", target_id, "Target")
    assert await user_manager.is_player_muted_async(muter_id, target_id) is True


@pytest.mark.asyncio
async def test_is_player_muted_async_false(user_manager: UserManager):
    """Test is_player_muted_async() returns False when player is not muted."""
    assert await user_manager.is_player_muted_async(uuid.uuid4(), uuid.uuid4()) is False


@pytest.mark.asyncio
async def test_is_channel_muted_true(user_manager: UserManager):
    """Test is_channel_muted() returns True when channel is muted."""
    player_id = uuid.uuid4()
    _ = await user_manager.mute_channel(player_id, "Player", "global")
    assert user_manager.is_channel_muted(player_id, "global") is True


def test_is_channel_muted_false(user_manager: UserManager):
    """Test is_channel_muted() returns False when channel is not muted."""
    assert user_manager.is_channel_muted(uuid.uuid4(), "global") is False


@pytest.mark.asyncio
async def test_is_globally_muted_true(user_manager: UserManager):
    """Test is_globally_muted() returns True when player is globally muted."""
    target_id = uuid.uuid4()
    _ = await user_manager.mute_global(uuid.uuid4(), "Muter", target_id, "Target")
    assert user_manager.is_globally_muted(target_id) is True


def test_is_globally_muted_false(user_manager: UserManager):
    """Test is_globally_muted() returns False when player is not globally muted."""
    assert user_manager.is_globally_muted(uuid.uuid4()) is False


def test_can_send_message_true(user_manager: UserManager):
    """Test can_send_message() returns True when player can send message."""
    assert user_manager.can_send_message(uuid.uuid4(), uuid.uuid4(), "global") is True


@pytest.mark.asyncio
async def test_can_send_message_player_muted(user_manager: UserManager):
    """Test can_send_message() behavior when target player is muted."""
    player_id = uuid.uuid4()
    target_id = uuid.uuid4()
    _ = await user_manager.mute_player(player_id, "Player", target_id, "Target")
    # Muting a target doesn't prevent the muter from sending (filtering is receiver-side)
    assert user_manager.can_send_message(player_id, target_id, "global") is True


@pytest.mark.asyncio
async def test_can_send_message_channel_muted(user_manager: UserManager):
    """Test can_send_message() returns False when channel is muted."""
    player_id = uuid.uuid4()
    _ = await user_manager.mute_channel(player_id, "Player", "global")
    assert user_manager.can_send_message(player_id, uuid.uuid4(), "global") is False


@pytest.mark.asyncio
async def test_can_send_message_globally_muted(user_manager: UserManager):
    """Test can_send_message() returns False when player is globally muted."""
    player_id = uuid.uuid4()
    _ = await user_manager.mute_global(uuid.uuid4(), "Muter", player_id, "Player")
    assert user_manager.can_send_message(player_id, uuid.uuid4(), "global") is False


@pytest.mark.asyncio
async def test_is_player_muted_by_others_true(user_manager: UserManager):
    """Test is_player_muted_by_others() returns True when globally muted by others."""
    target_id = uuid.uuid4()
    # is_player_muted_by_others only checks global mutes, not player mutes
    _ = await user_manager.mute_global(uuid.uuid4(), "Muter", target_id, "Target")
    assert user_manager.is_player_muted_by_others(target_id) is True


def test_is_player_muted_by_others_false(user_manager: UserManager):
    """Test is_player_muted_by_others() returns False when not muted."""
    assert user_manager.is_player_muted_by_others(uuid.uuid4()) is False


@pytest.mark.asyncio
async def test_get_who_muted_player(user_manager: UserManager):
    """Test get_who_muted_player() lists personal and global muters."""
    target_id = uuid.uuid4()
    _ = await user_manager.mute_player(uuid.uuid4(), "Alice", target_id, "Target")
    _ = await user_manager.mute_global(uuid.uuid4(), "Bob", target_id, "Target")
    assert sorted(user_manager.get_who_muted_player(target_id)) == [("Alice", "personal"), ("Bob", "global")]


@pytest.mark.asyncio
async def test_get_system_stats(user_manager: UserManager):
    """Test get_system_stats() returns system statistics."""
    _ = await user_manager.mute_player(uuid.uuid4(), "Player", uuid.uuid4(), "Target")
    result = user_manager.get_system_stats()
    assert result["total_players_with_mutes"] == 1
    assert result["total_global_mutes"] == 0


def test_cleanup_expired_mutes(user_manager: UserManager):
    """Test _cleanup_expired_mutes() drops expired entries from every index."""
    past = datetime.now(UTC) - timedelta(minutes=1)
    pid = uuid.uuid4()
    user_manager._player_mutes[pid] = {uuid.uuid4(): {"expires_at": past}}
    user_manager._channel_mutes[pid] = {"ooc": {"expires_at": past}}
    user_manager._global_mutes[pid] = {"expires_at": past}
    user_manager._cleanup_expired_mutes()
    assert not user_manager._player_mutes
    assert not user_manager._channel_mutes
    assert not user_manager._global_mutes


def test_get_player_mutes_empty(user_manager: UserManager):
    """Test get_player_mutes() returns empty dict when no mutes."""
    result = user_manager.get_player_mutes(uuid.uuid4())
    assert result == {"player_mutes": {}, "channel_mutes": {}, "global_mutes": {}}


@pytest.mark.asyncio
async def test_get_player_mutes_with_mutes(user_manager: UserManager):
    """Test get_player_mutes() returns mutes applied by the player."""
    player_id = uuid.uuid4()
    target_id = uuid.uuid4()
    _ = await user_manager.mute_player(player_id, "Player", target_id, "Target")
    _ = await user_manager.mute_channel(player_id, "Player", "say")
    _ = await user_manager.mute_global(player_id, "Player", target_id, "Target")
    assert target_id in user_manager._player_mutes[player_id]
    assert "say" in user_manager._channel_mutes[player_id]
    result = user_manager.get_player_mutes(player_id)
    assert set(result) == {"player_mutes", "channel_mutes", "global_mutes"}
    assert result["global_mutes"] == {target_id: user_manager._global_mutes[target_id]}


@pytest.mark.asyncio
async def test_add_admin_no_persistence(user_manager: UserManager):
    """Test add_admin() handles missing persistence (#679: injected, not via container)."""
    user_manager._async_persistence = None
    result = await user_manager.add_admin(uuid.uuid4(), "TestPlayer")
    assert result is False


@pytest.mark.asyncio
async def test_add_admin_player_not_found(user_manager: UserManager):
    """Test add_admin() handles player not found."""
    mock_persistence = AsyncMock()
    mock_persistence.get_player_by_id = AsyncMock(return_value=None)
    user_manager._async_persistence = mock_persistence  # #679: injected, not via container
    player_id = uuid.uuid4()
    result = await user_manager.add_admin(player_id, "TestPlayer")
    # The function logs an info message and continues even when player is None
    # It adds to cache and returns True
    assert result is True
    assert player_id in user_manager._admin_players


@pytest.mark.asyncio
async def test_remove_admin_no_persistence(user_manager: UserManager):
    """Test remove_admin() handles missing persistence (#679: injected, not via container)."""
    user_manager._async_persistence = None
    result = await user_manager.remove_admin(uuid.uuid4(), "TestPlayer")
    assert result is False


@pytest.mark.asyncio
async def test_remove_admin_player_not_found(user_manager: UserManager):
    """Test remove_admin() handles player not found."""
    mock_persistence = AsyncMock()
    mock_persistence.get_player_by_id = AsyncMock(return_value=None)
    user_manager._async_persistence = mock_persistence  # #679: injected, not via container
    player_id = uuid.uuid4()
    user_manager._admin_players.add(player_id)  # Add to cache first
    result = await user_manager.remove_admin(player_id, "TestPlayer")
    # The function logs an info message and continues even when player is None
    # It removes from cache and returns True
    assert result is True
    assert player_id not in user_manager._admin_players


@pytest.mark.asyncio
async def test_is_admin_no_persistence(user_manager: UserManager):
    """Test is_admin() returns False when persistence not available (#679: injected)."""
    user_manager._async_persistence = None
    result = await user_manager.is_admin(uuid.uuid4())
    assert result is False


@pytest.mark.asyncio
async def test_add_admin_success(user_manager: UserManager):
    """Test add_admin() successfully adds admin."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.set_admin_status = MagicMock()
    mock_persistence = AsyncMock()
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.save_player = AsyncMock()
    user_manager._async_persistence = mock_persistence  # #679: injected, not via container
    result = await user_manager.add_admin(player_id, "TestPlayer")
    assert result is True
    assert player_id in user_manager._admin_players


@pytest.mark.asyncio
async def test_remove_admin_success(user_manager: UserManager):
    """Test remove_admin() successfully removes admin."""
    player_id = uuid.uuid4()
    user_manager._admin_players.add(player_id)
    mock_player = MagicMock()
    mock_player.set_admin_status = MagicMock()
    mock_persistence = AsyncMock()
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.save_player = AsyncMock()
    user_manager._async_persistence = mock_persistence  # #679: injected, not via container
    result = await user_manager.remove_admin(player_id, "TestPlayer")
    assert result is True
    assert player_id not in user_manager._admin_players


@pytest.mark.asyncio
async def test_is_admin_cached(user_manager: UserManager):
    """Test is_admin() returns True from cache."""
    player_id = uuid.uuid4()
    user_manager._admin_players.add(player_id)
    result = await user_manager.is_admin(player_id)
    assert result is True


@pytest.mark.asyncio
async def test_is_admin_not_cached(user_manager: UserManager):
    """Test is_admin() checks database when not in cache."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.is_admin_user = MagicMock(return_value=True)
    mock_persistence = AsyncMock()
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    user_manager._async_persistence = mock_persistence  # #679: injected, not via container
    result = await user_manager.is_admin(player_id)
    assert result is True
    assert player_id in user_manager._admin_players
