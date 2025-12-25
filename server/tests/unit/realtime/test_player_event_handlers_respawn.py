"""
Tests for player respawn event handlers.

This module tests the PlayerRespawnEventHandler class which handles
player respawn and delirium respawn events.
"""

from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from server.realtime.player_event_handlers_respawn import PlayerRespawnEventHandler


class TestPlayerRespawnEventHandlerInit:
    """Test PlayerRespawnEventHandler initialization."""

    def test_init(self) -> None:
        """Test PlayerRespawnEventHandler initialization."""
        mock_connection_manager = MagicMock()
        mock_utils = MagicMock()
        mock_logger = MagicMock()

        handler = PlayerRespawnEventHandler(mock_connection_manager, mock_utils, mock_logger)

        assert handler.connection_manager == mock_connection_manager
        assert handler.utils == mock_utils
        assert handler._logger == mock_logger


class TestUpdateConnectionManagerPosition:
    """Test update_connection_manager_position method."""

    def test_update_connection_manager_position_success(self) -> None:
        """Test successfully updating connection manager position."""
        mock_connection_manager = MagicMock()
        mock_connection_manager.online_players = {uuid4(): {"position": "standing"}}
        mock_utils = MagicMock()
        mock_logger = MagicMock()

        handler = PlayerRespawnEventHandler(mock_connection_manager, mock_utils, mock_logger)

        player_id = uuid4()
        mock_connection_manager.online_players[player_id] = {"position": "standing"}

        handler.update_connection_manager_position(str(player_id), "sitting")

        assert mock_connection_manager.online_players[player_id]["position"] == "sitting"
        mock_logger.debug.assert_called_once()

    def test_update_connection_manager_position_no_online_players(self) -> None:
        """Test updating position when online_players doesn't exist."""
        mock_connection_manager = MagicMock()
        delattr(mock_connection_manager, "online_players")
        mock_utils = MagicMock()
        mock_logger = MagicMock()

        handler = PlayerRespawnEventHandler(mock_connection_manager, mock_utils, mock_logger)

        # Should not raise error
        handler.update_connection_manager_position(str(uuid4()), "sitting")

    def test_update_connection_manager_position_player_not_online(self) -> None:
        """Test updating position when player is not in online_players."""
        mock_connection_manager = MagicMock()
        mock_connection_manager.online_players = {}
        mock_utils = MagicMock()
        mock_logger = MagicMock()

        handler = PlayerRespawnEventHandler(mock_connection_manager, mock_utils, mock_logger)

        # Should not raise error
        handler.update_connection_manager_position(str(uuid4()), "sitting")


class TestGetPlayerDataForRespawn:
    """Test get_player_data_for_respawn method."""

    @pytest.mark.asyncio
    async def test_get_player_data_for_respawn_success(self) -> None:
        """Test successfully getting player data for respawn."""
        mock_connection_manager = MagicMock()
        mock_async_persistence = AsyncMock()
        mock_connection_manager.async_persistence = mock_async_persistence

        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_player.name = "TestPlayer"
        mock_player.level = 5
        mock_player.experience_points = 1000
        mock_player.get_stats.return_value = {
            "current_dp": 50,
            "max_dp": 100,
            "lucidity": 80,
            "max_lucidity": 100,
            "position": "sitting",
        }

        mock_async_persistence.get_player_by_id = AsyncMock(return_value=mock_player)

        mock_utils = MagicMock()
        mock_logger = MagicMock()

        handler = PlayerRespawnEventHandler(mock_connection_manager, mock_utils, mock_logger)

        player_id_str = str(mock_player.player_id)

        with patch.object(handler, "update_connection_manager_position"):
            result, position = await handler.get_player_data_for_respawn(player_id_str)

            assert result is not None
            assert result["id"] == str(mock_player.player_id)
            assert result["name"] == "TestPlayer"
            assert result["stats"]["position"] == "sitting"
            assert position == "sitting"

    @pytest.mark.asyncio
    async def test_get_player_data_for_respawn_no_connection_manager(self) -> None:
        """Test getting player data when connection manager is None."""
        mock_utils = MagicMock()
        mock_logger = MagicMock()

        handler = PlayerRespawnEventHandler(None, mock_utils, mock_logger)

        result, position = await handler.get_player_data_for_respawn(str(uuid4()))

        assert result is None
        assert position == "standing"

    @pytest.mark.asyncio
    async def test_get_player_data_for_respawn_no_persistence(self) -> None:
        """Test getting player data when persistence is not available."""
        mock_connection_manager = MagicMock()
        mock_connection_manager.async_persistence = None
        mock_utils = MagicMock()
        mock_logger = MagicMock()

        handler = PlayerRespawnEventHandler(mock_connection_manager, mock_utils, mock_logger)

        result, position = await handler.get_player_data_for_respawn(str(uuid4()))

        assert result is None
        assert position == "standing"

    @pytest.mark.asyncio
    async def test_get_player_data_for_respawn_player_not_found(self) -> None:
        """Test getting player data when player is not found."""
        mock_connection_manager = MagicMock()
        mock_async_persistence = AsyncMock()
        mock_connection_manager.async_persistence = mock_async_persistence
        mock_async_persistence.get_player_by_id = AsyncMock(return_value=None)

        mock_utils = MagicMock()
        mock_logger = MagicMock()

        handler = PlayerRespawnEventHandler(mock_connection_manager, mock_utils, mock_logger)

        result, position = await handler.get_player_data_for_respawn(str(uuid4()))

        assert result is None
        assert position == "standing"

    @pytest.mark.asyncio
    async def test_get_player_data_for_respawn_error(self) -> None:
        """Test getting player data when an error occurs."""
        mock_connection_manager = MagicMock()
        mock_async_persistence = AsyncMock()
        mock_connection_manager.async_persistence = mock_async_persistence
        mock_async_persistence.get_player_by_id = AsyncMock(side_effect=ValueError("Error"))

        mock_utils = MagicMock()
        mock_logger = MagicMock()

        handler = PlayerRespawnEventHandler(mock_connection_manager, mock_utils, mock_logger)

        with patch.object(handler, "_logger"):
            result, position = await handler.get_player_data_for_respawn(str(uuid4()))

            assert result is None
            assert position == "standing"


class TestSendRespawnEventWithRetry:
    """Test send_respawn_event_with_retry method."""

    @pytest.mark.asyncio
    async def test_send_respawn_event_with_retry_success(self) -> None:
        """Test successfully sending respawn event."""
        player_id = uuid4()
        mock_connection_manager = MagicMock()
        mock_connection_manager.player_websockets = {player_id: ["conn-1"]}
        mock_connection_manager.send_personal_message = AsyncMock(
            return_value={"websocket_delivered": 1, "active_connections": 1}
        )

        mock_utils = MagicMock()
        mock_logger = MagicMock()

        handler = PlayerRespawnEventHandler(mock_connection_manager, mock_utils, mock_logger)

        respawn_event = {"event_type": "player_respawned", "data": {}}

        await handler.send_respawn_event_with_retry(player_id, respawn_event)

        mock_connection_manager.send_personal_message.assert_called_once()

    @pytest.mark.asyncio
    async def test_send_respawn_event_with_retry_wait_for_connection(self) -> None:
        """Test sending respawn event when connection becomes available."""
        player_id = uuid4()
        mock_connection_manager = MagicMock()
        # Start with no connection, then add it
        mock_connection_manager.player_websockets = {}
        mock_connection_manager.send_personal_message = AsyncMock(
            return_value={"websocket_delivered": 1, "active_connections": 1}
        )

        mock_utils = MagicMock()
        mock_logger = MagicMock()

        handler = PlayerRespawnEventHandler(mock_connection_manager, mock_utils, mock_logger)

        respawn_event = {"event_type": "player_respawned", "data": {}}

        # Add connection after a short delay
        async def add_connection():
            await asyncio.sleep(0.1)
            mock_connection_manager.player_websockets[player_id] = ["conn-1"]

        import asyncio

        task = asyncio.create_task(add_connection())
        await handler.send_respawn_event_with_retry(player_id, respawn_event, max_wait_time=1.0)
        await task

        # Should have eventually sent the message
        assert mock_connection_manager.send_personal_message.called


class TestHandlePlayerRespawned:
    """Test handle_player_respawned method."""

    @pytest.mark.asyncio
    async def test_handle_player_respawned_success(self) -> None:
        """Test successfully handling player respawn event."""
        player_id = uuid4()
        mock_connection_manager = MagicMock()
        mock_async_persistence = AsyncMock()
        mock_connection_manager.async_persistence = mock_async_persistence

        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_player.name = "TestPlayer"
        mock_player.level = 5
        mock_player.experience_points = 1000
        mock_player.get_stats.return_value = {"position": "standing"}

        mock_async_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_connection_manager.player_websockets = {player_id: ["conn-1"]}
        mock_connection_manager.send_personal_message = AsyncMock(
            return_value={"websocket_delivered": 1, "active_connections": 1}
        )

        mock_utils = MagicMock()
        mock_logger = MagicMock()

        handler = PlayerRespawnEventHandler(mock_connection_manager, mock_utils, mock_logger)

        mock_event = MagicMock()
        mock_event.player_id = player_id
        mock_event.player_name = "TestPlayer"
        mock_event.respawn_room_id = "room-123"
        mock_event.old_dp = 0
        mock_event.new_dp = 100

        with patch("server.realtime.envelope.build_event") as mock_build_event:
            mock_build_event.return_value = {"event_type": "player_respawned"}
            with patch.object(handler, "_logger"):
                await handler.handle_player_respawned(mock_event)

                mock_build_event.assert_called_once()
                mock_connection_manager.send_personal_message.assert_called_once()


class TestGetCurrentLucidity:
    """Test get_current_lucidity method."""

    @pytest.mark.asyncio
    async def test_get_current_lucidity_success(self) -> None:
        """Test successfully getting current lucidity."""
        player_id = uuid4()
        mock_connection_manager = MagicMock()
        mock_utils = MagicMock()
        mock_logger = MagicMock()

        handler = PlayerRespawnEventHandler(mock_connection_manager, mock_utils, mock_logger)

        # Create mock lucidity record
        class MockLucidity:
            def __init__(self):
                self.current_lcd = 75

        mock_lucidity = MockLucidity()
        mock_session = AsyncMock()
        mock_session.get = AsyncMock(return_value=mock_lucidity)

        async def mock_session_generator():
            yield mock_session

        with patch("server.database.get_async_session", return_value=mock_session_generator()):
            result = await handler.get_current_lucidity(player_id, 50)

            assert result == 75

    @pytest.mark.asyncio
    async def test_get_current_lucidity_not_found(self) -> None:
        """Test getting current lucidity when record not found."""
        player_id = uuid4()
        mock_connection_manager = MagicMock()
        mock_utils = MagicMock()
        mock_logger = MagicMock()

        handler = PlayerRespawnEventHandler(mock_connection_manager, mock_utils, mock_logger)

        mock_session = AsyncMock()
        mock_session.get = AsyncMock(return_value=None)

        async def mock_session_generator():
            yield mock_session

        with patch("server.database.get_async_session", return_value=mock_session_generator()):
            result = await handler.get_current_lucidity(player_id, 50)

            assert result == 50  # Returns default


class TestGetPlayerDataForDeliriumRespawn:
    """Test get_player_data_for_delirium_respawn method."""

    @pytest.mark.asyncio
    async def test_get_player_data_for_delirium_respawn_success(self) -> None:
        """Test successfully getting player data for delirium respawn."""
        mock_connection_manager = MagicMock()
        mock_async_persistence = AsyncMock()
        mock_connection_manager.async_persistence = mock_async_persistence

        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_player.name = "TestPlayer"
        mock_player.level = 5
        mock_player.experience_points = 1000
        mock_player.get_stats.return_value = {
            "current_dp": 50,
            "max_dp": 100,
            "max_lucidity": 100,
            "position": "sitting",
        }

        mock_async_persistence.get_player_by_id = AsyncMock(return_value=mock_player)

        mock_utils = MagicMock()
        mock_logger = MagicMock()

        handler = PlayerRespawnEventHandler(mock_connection_manager, mock_utils, mock_logger)

        player_id_str = str(mock_player.player_id)

        # Mock get_current_lucidity
        with patch.object(handler, "get_current_lucidity", new_callable=AsyncMock, return_value=80):
            with patch.object(handler, "update_connection_manager_position"):
                result, position = await handler.get_player_data_for_delirium_respawn(player_id_str, 75)

                assert result is not None
                assert result["stats"]["lucidity"] == 80  # From get_current_lucidity
                assert position == "sitting"


class TestHandlePlayerDeliriumRespawned:
    """Test handle_player_delirium_respawned method."""

    @pytest.mark.asyncio
    async def test_handle_player_delirium_respawned_success(self) -> None:
        """Test successfully handling player delirium respawn event."""
        player_id = uuid4()
        mock_connection_manager = MagicMock()
        mock_async_persistence = AsyncMock()
        mock_connection_manager.async_persistence = mock_async_persistence

        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_player.name = "TestPlayer"
        mock_player.level = 5
        mock_player.experience_points = 1000
        mock_player.get_stats.return_value = {"position": "standing"}

        mock_async_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_connection_manager.player_websockets = {player_id: ["conn-1"]}
        mock_connection_manager.send_personal_message = AsyncMock(
            return_value={"websocket_delivered": 1, "active_connections": 1}
        )

        mock_utils = MagicMock()
        mock_logger = MagicMock()

        handler = PlayerRespawnEventHandler(mock_connection_manager, mock_utils, mock_logger)

        mock_event = MagicMock()
        mock_event.player_id = player_id
        mock_event.player_name = "TestPlayer"
        mock_event.respawn_room_id = "room-123"
        mock_event.old_lucidity = 0
        mock_event.new_lucidity = 100

        with patch("server.realtime.envelope.build_event") as mock_build_event:
            mock_build_event.return_value = {"event_type": "player_delirium_respawned"}
            with patch.object(handler, "get_current_lucidity", new_callable=AsyncMock, return_value=100):
                with patch.object(handler, "_logger"):
                    await handler.handle_player_delirium_respawned(mock_event)

                    mock_build_event.assert_called_once()
                    mock_connection_manager.send_personal_message.assert_called_once()
