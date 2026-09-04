"""
Unit tests for player connection setup grace period integration.

Tests that reconnection cancels grace period.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.player_connection_setup import handle_new_connection_setup


@pytest.mark.asyncio
async def test_reconnection_cancels_grace_period():
    """Test that reconnection cancels grace period."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.current_room_id = "room_123"
    mock_manager = MagicMock()
    # Player in grace period (task will be handled by patched cancel_grace_period)
    mock_manager.grace_period_players = {player_id: MagicMock()}  # Player in grace period
    mock_manager.processed_disconnects = set()
    mock_manager.processed_disconnect_lock = AsyncMock()
    mock_manager.processed_disconnect_lock.__aenter__ = AsyncMock(return_value=None)
    mock_manager.processed_disconnect_lock.__aexit__ = AsyncMock(return_value=None)
    mock_manager.message_queue = MagicMock()
    mock_manager.message_queue.remove_player_messages = MagicMock()
    mock_manager.room_manager = MagicMock()
    mock_manager.room_manager.add_room_occupant = MagicMock()
    mock_manager.room_manager.reconcile_room_presence = MagicMock()
    mock_manager.online_players = {}
    # Accessing protected member is necessary to mock the method used by player_connection_setup implementation
    mock_manager._send_initial_game_state = AsyncMock()  # pylint: disable=protected-access  # Reason: Accessing protected member is necessary to mock the method used by player_connection_setup implementation
    mock_manager.broadcast_to_room = AsyncMock()
    # Set up async_persistence for _update_player_last_active (even though it's patched, ensure it's available)
    mock_manager.async_persistence = AsyncMock()
    mock_manager.async_persistence.update_player_last_active = AsyncMock()
    # Set up app.state.container.real_time_event_handler for room occupants update
    mock_manager.app = MagicMock()
    mock_manager.app.state = MagicMock()
    mock_manager.app.state.container = MagicMock()
    mock_manager.app.state.container.real_time_event_handler = MagicMock()
    mock_manager.app.state.container.real_time_event_handler.send_room_occupants_update = AsyncMock()

    with patch("server.realtime.player_connection_setup._update_player_last_active", new_callable=AsyncMock):
        with patch("server.realtime.player_connection_setup._add_player_to_room_silently", new_callable=AsyncMock):
            with patch(
                "server.realtime.player_connection_setup._broadcast_player_entered_game", new_callable=AsyncMock
            ):
                with patch(
                    "server.realtime.player_connection_setup.cancel_grace_period", new_callable=AsyncMock
                ) as mock_cancel:
                    await handle_new_connection_setup(player_id, mock_player, "room_123", mock_manager)

                    # Verify grace period was cancelled
                    mock_cancel.assert_called_once_with(player_id, mock_manager)


@pytest.mark.asyncio
async def test_reconnection_no_grace_period():
    """Test that reconnection does nothing if player not in grace period."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.current_room_id = "room_123"
    mock_manager = MagicMock()
    mock_manager.grace_period_players = {}  # Player not in grace period
    mock_manager.processed_disconnects = set()
    mock_manager.processed_disconnect_lock = AsyncMock()
    mock_manager.processed_disconnect_lock.__aenter__ = AsyncMock(return_value=None)
    mock_manager.processed_disconnect_lock.__aexit__ = AsyncMock(return_value=None)
    mock_manager.message_queue = MagicMock()
    mock_manager.message_queue.remove_player_messages = MagicMock()
    mock_manager.room_manager = MagicMock()
    mock_manager.room_manager.add_room_occupant = MagicMock()
    mock_manager.room_manager.reconcile_room_presence = MagicMock()
    mock_manager.online_players = {}
    # Accessing protected member is necessary to mock the method used by player_connection_setup implementation
    mock_manager._send_initial_game_state = AsyncMock()  # pylint: disable=protected-access  # Reason: Accessing protected member is necessary to mock the method used by player_connection_setup implementation
    mock_manager.broadcast_to_room = AsyncMock()
    # Set up async_persistence for _update_player_last_active (even though it's patched, ensure it's available)
    mock_manager.async_persistence = AsyncMock()
    mock_manager.async_persistence.update_player_last_active = AsyncMock()
    # Set up app.state.container.real_time_event_handler for room occupants update
    mock_manager.app = MagicMock()
    mock_manager.app.state = MagicMock()
    mock_manager.app.state.container = MagicMock()
    mock_manager.app.state.container.real_time_event_handler = MagicMock()
    mock_manager.app.state.container.real_time_event_handler.send_room_occupants_update = AsyncMock()

    with patch("server.realtime.player_connection_setup._update_player_last_active", new_callable=AsyncMock):
        with patch("server.realtime.player_connection_setup._add_player_to_room_silently", new_callable=AsyncMock):
            with patch(
                "server.realtime.player_connection_setup._broadcast_player_entered_game", new_callable=AsyncMock
            ):
                with patch(
                    "server.realtime.player_connection_setup.cancel_grace_period", new_callable=AsyncMock
                ) as mock_cancel:
                    await handle_new_connection_setup(player_id, mock_player, "room_123", mock_manager)

                    # Verify grace period cancellation was NOT called (player not in grace period)
                    mock_cancel.assert_not_called()
