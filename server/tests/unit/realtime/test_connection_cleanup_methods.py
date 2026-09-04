"""Unit tests for connection_cleanup_methods delegation wrappers."""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.connection_cleanup_methods import (
    check_and_cleanup_impl,
    cleanup_dead_connections_impl,
    cleanup_ghost_players_impl,
    cleanup_orphaned_data_impl,
    force_cleanup_impl,
    prune_stale_players_impl,
)


@pytest.fixture
def manager() -> MagicMock:
    mgr = MagicMock()
    mgr.connection_cleaner = MagicMock()
    mgr.connection_cleaner.cleanup_dead_connections = AsyncMock(return_value={"connections_cleaned": 1})
    mgr.connection_cleaner.check_and_cleanup = AsyncMock(return_value={})
    mgr.connection_cleaner.force_cleanup = AsyncMock(return_value={})
    mgr.connection_cleaner.cleanup_ghost_players = MagicMock()
    mgr.connection_cleaner.prune_stale_players = MagicMock()
    mgr.connection_cleaner.cleanup_orphaned_data = AsyncMock(return_value={})
    mgr.player_websockets = {}
    mgr.active_websockets = {}
    mgr.online_players = {}
    mgr.last_seen = {}
    mgr.connection_timestamps = {}
    mgr.cleanup_stats = {}
    mgr.last_active_update_times = {}
    mgr.connection_metadata = {}
    mgr.cleanup_orphaned_data = AsyncMock()
    mgr.prune_stale_players = MagicMock()
    return mgr


@pytest.mark.asyncio
async def test_cleanup_dead_connections_impl_delegates(manager: MagicMock) -> None:
    player_id = uuid.uuid4()
    result = await cleanup_dead_connections_impl(manager, player_id)
    assert result["connections_cleaned"] == 1
    manager.connection_cleaner.cleanup_dead_connections.assert_awaited_once()


@pytest.mark.asyncio
async def test_check_and_cleanup_impl_delegates(manager: MagicMock) -> None:
    await check_and_cleanup_impl(manager)
    manager.connection_cleaner.check_and_cleanup.assert_awaited_once()


@pytest.mark.asyncio
async def test_force_cleanup_impl_delegates(manager: MagicMock) -> None:
    await force_cleanup_impl(manager)
    manager.connection_cleaner.force_cleanup.assert_awaited_once()


def test_cleanup_ghost_players_impl_delegates(manager: MagicMock) -> None:
    cleanup_ghost_players_impl(manager)
    manager.connection_cleaner.cleanup_ghost_players.assert_called_once()


def test_prune_stale_players_impl_delegates(manager: MagicMock) -> None:
    prune_stale_players_impl(manager, max_age_seconds=120)
    manager.connection_cleaner.prune_stale_players.assert_called_once()


@pytest.mark.asyncio
async def test_cleanup_orphaned_data_impl_ages_sessions(manager: MagicMock) -> None:
    with patch("server.realtime.connection_cleanup_methods.age_off_disconnected_sessions", return_value=2):
        await cleanup_orphaned_data_impl(manager)
    manager.connection_cleaner.cleanup_orphaned_data.assert_awaited_once()


@pytest.mark.asyncio
async def test_cleanup_dead_connections_default_when_cleaner_missing() -> None:
    manager = MagicMock()
    manager.connection_cleaner = None
    manager.player_websockets = {}
    manager.active_websockets = {}
    result = await cleanup_dead_connections_impl(manager)
    assert result["connections_cleaned"] == 0
    assert "Connection cleaner not initialized" in result["errors"]
