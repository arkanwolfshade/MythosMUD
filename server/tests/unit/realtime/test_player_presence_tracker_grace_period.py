"""
Unit tests for player presence tracker grace period integration.

Tests the integration of grace period system with player disconnect tracking,
including intentional vs unintentional disconnect handling.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.player_presence_tracker import track_player_disconnected_impl


@pytest.mark.asyncio
async def test_track_player_disconnected_intentional_no_grace_period():
    """Test intentional disconnect does NOT start grace period."""
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.disconnecting_players = set()
    mock_manager.disconnect_lock = AsyncMock()
    mock_manager.disconnect_lock.__aenter__ = AsyncMock(return_value=None)
    mock_manager.disconnect_lock.__aexit__ = AsyncMock(return_value=None)
    mock_manager.intentional_disconnects = {player_id}  # Marked as intentional
    # Accessing protected member is necessary to mock the method used by player_presence_tracker implementation
    mock_manager._get_player = AsyncMock(return_value=MagicMock())  # pylint: disable=protected-access
    # Accessing protected member is necessary to mock the method used by player_presence_tracker implementation
    mock_manager._cleanup_ghost_players = MagicMock()  # pylint: disable=protected-access

    with patch("server.realtime.player_presence_tracker._should_skip_disconnect", return_value=False):
        with patch("server.realtime.player_presence_tracker._acquire_disconnect_lock", return_value=True):
            with patch("server.realtime.player_presence_tracker.extract_player_name", return_value="TestPlayer"):
                with patch(
                    "server.realtime.player_presence_tracker._collect_disconnect_keys",
                    return_value=(set(), set()),
                ):
                    with patch(
                        "server.realtime.player_presence_tracker.handle_player_disconnect_broadcast",
                        new_callable=AsyncMock,
                    ):
                        with patch("server.realtime.player_presence_tracker._remove_player_from_online_tracking"):
                            with patch("server.realtime.player_presence_tracker._cleanup_player_references"):
                                with patch(
                                    "server.realtime.disconnect_grace_period.start_grace_period", new_callable=AsyncMock
                                ) as mock_start_grace:
                                    await track_player_disconnected_impl(player_id, mock_manager, connection_type=None)

                                    # Verify grace period was NOT started for intentional disconnect
                                    mock_start_grace.assert_not_called()


@pytest.mark.asyncio
async def test_track_player_disconnected_unintentional_starts_grace_period():
    """Test unintentional disconnect starts grace period."""
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.disconnecting_players = set()
    mock_manager.disconnect_lock = AsyncMock()
    mock_manager.disconnect_lock.__aenter__ = AsyncMock(return_value=None)
    mock_manager.disconnect_lock.__aexit__ = AsyncMock(return_value=None)
    mock_manager.intentional_disconnects = set()  # NOT marked as intentional
    mock_manager.grace_period_players = {}
    # Accessing protected member is necessary to mock the method used by player_presence_tracker implementation
    mock_manager._get_player = AsyncMock(return_value=MagicMock())  # pylint: disable=protected-access
    # Accessing protected member is necessary to mock the method used by player_presence_tracker implementation
    mock_manager._cleanup_ghost_players = MagicMock()  # pylint: disable=protected-access

    with patch("server.realtime.player_presence_tracker._should_skip_disconnect", return_value=False):
        with patch("server.realtime.player_presence_tracker._acquire_disconnect_lock", return_value=True):
            with patch(
                "server.realtime.player_presence_tracker.start_grace_period", new_callable=AsyncMock
            ) as mock_start_grace:
                await track_player_disconnected_impl(player_id, mock_manager, connection_type=None)

                # Verify grace period WAS started for unintentional disconnect
                mock_start_grace.assert_called_once_with(player_id, mock_manager)


@pytest.mark.asyncio
async def test_track_player_disconnected_removes_from_intentional_set():
    """Test intentional disconnect is removed from intentional_disconnects set."""
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.disconnecting_players = set()
    mock_manager.disconnect_lock = AsyncMock()
    mock_manager.disconnect_lock.__aenter__ = AsyncMock(return_value=None)
    mock_manager.disconnect_lock.__aexit__ = AsyncMock(return_value=None)
    mock_manager.intentional_disconnects = {player_id}  # Marked as intentional
    # Accessing protected member is necessary to mock the method used by player_presence_tracker implementation
    mock_manager._get_player = AsyncMock(return_value=MagicMock())  # pylint: disable=protected-access
    # Accessing protected member is necessary to mock the method used by player_presence_tracker implementation
    mock_manager._cleanup_ghost_players = MagicMock()  # pylint: disable=protected-access

    with patch("server.realtime.player_presence_tracker._should_skip_disconnect", return_value=False):
        with patch("server.realtime.player_presence_tracker._acquire_disconnect_lock", return_value=True):
            with patch("server.realtime.player_presence_tracker.extract_player_name", return_value="TestPlayer"):
                with patch(
                    "server.realtime.player_presence_tracker._collect_disconnect_keys",
                    return_value=(set(), set()),
                ):
                    with patch(
                        "server.realtime.player_presence_tracker.handle_player_disconnect_broadcast",
                        new_callable=AsyncMock,
                    ):
                        with patch("server.realtime.player_presence_tracker._remove_player_from_online_tracking"):
                            with patch("server.realtime.player_presence_tracker._cleanup_player_references"):
                                await track_player_disconnected_impl(player_id, mock_manager, connection_type=None)

                                # Verify player was removed from intentional_disconnects
                                assert player_id not in mock_manager.intentional_disconnects
