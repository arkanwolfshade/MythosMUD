"""
Tests for WebSocket room update and broadcast functions.

This module tests functions for handling room updates and broadcasting
to players in real-time.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.websocket_room_updates import (
    broadcast_room_update,
    build_room_update_event,
    get_npc_occupants_fallback,
    get_npc_occupants_from_lifecycle_manager,
    get_player_occupants,
    update_player_room_subscription,
)


class TestGetPlayerOccupants:
    """Test get_player_occupants function."""

    @pytest.mark.asyncio
    async def test_get_player_occupants_success(self) -> None:
        """Test successfully getting player occupants."""
        mock_connection_manager = AsyncMock()
        mock_connection_manager.get_room_occupants = AsyncMock(
            return_value=[{"player_name": "Player1"}, {"name": "Player2"}]
        )

        result = await get_player_occupants(mock_connection_manager, "room-123")

        assert len(result) == 2
        assert "Player1" in result
        assert "Player2" in result

    @pytest.mark.asyncio
    async def test_get_player_occupants_empty(self) -> None:
        """Test getting player occupants when room is empty."""
        mock_connection_manager = AsyncMock()
        mock_connection_manager.get_room_occupants = AsyncMock(return_value=[])

        result = await get_player_occupants(mock_connection_manager, "room-123")

        assert result == []

    @pytest.mark.asyncio
    async def test_get_player_occupants_error(self) -> None:
        """Test getting player occupants when error occurs."""
        mock_connection_manager = AsyncMock()
        mock_connection_manager.get_room_occupants = AsyncMock(side_effect=AttributeError("Error"))

        with patch("server.realtime.websocket_room_updates.logger"):
            result = await get_player_occupants(mock_connection_manager, "room-123")

            assert result == []


class TestGetNpcOccupantsFromLifecycleManager:
    """Test get_npc_occupants_from_lifecycle_manager function."""

    @pytest.mark.asyncio
    async def test_get_npc_occupants_success(self) -> None:
        """Test successfully getting NPC occupants."""
        room_id = "room-123"

        mock_npc1 = MagicMock()
        mock_npc1.is_alive = True
        mock_npc1.current_room = None  # Explicitly set to None so current_room_id is used
        mock_npc1.current_room_id = room_id
        mock_npc1.name = "NPC1"

        mock_npc2 = MagicMock()
        mock_npc2.is_alive = True
        mock_npc2.current_room = None  # Explicitly set to None so current_room_id is used
        mock_npc2.current_room_id = room_id
        mock_npc2.name = "NPC2"

        mock_lifecycle_manager = MagicMock()
        mock_lifecycle_manager.active_npcs = {"npc-1": mock_npc1, "npc-2": mock_npc2}

        mock_npc_service = MagicMock()
        mock_npc_service.lifecycle_manager = mock_lifecycle_manager

        with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=mock_npc_service):
            # Patch get_npc_name_from_instance to return names directly
            with patch("server.realtime.websocket_room_updates.get_npc_name_from_instance") as mock_get_name:

                def get_name_side_effect(npc_id):
                    return {"npc-1": "NPC1", "npc-2": "NPC2"}.get(npc_id)

                mock_get_name.side_effect = get_name_side_effect
                with patch("server.realtime.websocket_room_updates.logger"):
                    result = await get_npc_occupants_from_lifecycle_manager(room_id)

                    # The function gets names from npc_instance.name attribute
                    assert len(result) == 2
                    assert "NPC1" in result
                    assert "NPC2" in result

    @pytest.mark.asyncio
    async def test_get_npc_occupants_filters_dead_npcs(self) -> None:
        """Test that dead NPCs are filtered out."""
        room_id = "room-123"

        mock_npc1 = MagicMock()
        mock_npc1.is_alive = True
        mock_npc1.current_room = None
        mock_npc1.current_room_id = room_id

        mock_npc2 = MagicMock()
        mock_npc2.is_alive = False  # Dead NPC
        mock_npc2.current_room = None
        mock_npc2.current_room_id = room_id

        mock_lifecycle_manager = MagicMock()
        mock_lifecycle_manager.active_npcs = {"npc-1": mock_npc1, "npc-2": mock_npc2}

        mock_npc_service = MagicMock()
        mock_npc_service.lifecycle_manager = mock_lifecycle_manager

        with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=mock_npc_service):
            with patch("server.realtime.websocket_room_updates.get_npc_name_from_instance", return_value="NPC1"):
                with patch("server.realtime.websocket_room_updates.logger"):
                    result = await get_npc_occupants_from_lifecycle_manager(room_id)

                    # Only alive NPC should be included
                    assert len(result) == 1
                    assert "NPC1" in result

    @pytest.mark.asyncio
    async def test_get_npc_occupants_no_service(self) -> None:
        """Test getting NPC occupants when service is not available."""
        with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=None):
            with patch("server.realtime.websocket_room_updates.logger"):
                result = await get_npc_occupants_from_lifecycle_manager("room-123")

                assert result == []


class TestGetNpcOccupantsFallback:
    """Test get_npc_occupants_fallback function."""

    @pytest.mark.asyncio
    async def test_get_npc_occupants_fallback_success(self) -> None:
        """Test successfully getting NPC occupants using fallback."""
        mock_room = MagicMock()
        mock_room.get_npcs.return_value = ["npc-1", "npc-2"]

        mock_npc1 = MagicMock()
        mock_npc1.is_alive = True

        mock_npc2 = MagicMock()
        mock_npc2.is_alive = True

        mock_lifecycle_manager = MagicMock()
        mock_lifecycle_manager.active_npcs = {"npc-1": mock_npc1, "npc-2": mock_npc2}

        mock_npc_service = MagicMock()
        mock_npc_service.lifecycle_manager = mock_lifecycle_manager

        with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=mock_npc_service):
            with patch("server.realtime.websocket_room_updates.get_npc_name_from_instance") as mock_get_name:
                # get_npc_name_from_instance is called for each npc_id
                def get_name_side_effect(npc_id):
                    names = {"npc-1": "NPC1", "npc-2": "NPC2"}
                    return names.get(npc_id, None)

                mock_get_name.side_effect = get_name_side_effect
                with patch("server.realtime.websocket_room_updates.logger"):
                    result = await get_npc_occupants_fallback(mock_room, "room-123")

                    assert len(result) == 2
                    assert "NPC1" in result
                    assert "NPC2" in result

    @pytest.mark.asyncio
    async def test_get_npc_occupants_fallback_filters_dead(self) -> None:
        """Test that fallback filters out dead NPCs."""
        mock_room = MagicMock()
        mock_room.get_npcs.return_value = ["npc-1", "npc-2"]

        mock_npc1 = MagicMock()
        mock_npc1.is_alive = True

        mock_npc2 = MagicMock()
        mock_npc2.is_alive = False  # Dead

        mock_lifecycle_manager = MagicMock()
        mock_lifecycle_manager.active_npcs = {"npc-1": mock_npc1, "npc-2": mock_npc2}

        mock_npc_service = MagicMock()
        mock_npc_service.lifecycle_manager = mock_lifecycle_manager

        with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=mock_npc_service):
            with patch("server.realtime.websocket_room_updates.get_npc_name_from_instance", return_value="NPC1"):
                with patch("server.realtime.websocket_room_updates.logger"):
                    result = await get_npc_occupants_fallback(mock_room, "room-123")

                    assert len(result) == 1
                    assert "NPC1" in result


class TestBuildRoomUpdateEvent:
    """Test build_room_update_event function."""

    @pytest.mark.asyncio
    async def test_build_room_update_event_success(self) -> None:
        """Test successfully building room update event."""
        mock_room = MagicMock()
        mock_room.to_dict.return_value = {"room_id": "room-123", "name": "Test Room"}
        mock_room.get_players.return_value = []
        mock_room.get_objects.return_value = []
        mock_room.get_npcs.return_value = []
        mock_room.get_occupant_count.return_value = 0

        mock_connection_manager = AsyncMock()
        mock_connection_manager.convert_room_players_uuids_to_names = AsyncMock(
            return_value={"room_id": "room-123", "name": "Test Room"}
        )
        mock_connection_manager.room_manager = None

        occupant_names = ["Player1", "Player2"]

        with patch("server.realtime.websocket_room_updates.logger"):
            result = await build_room_update_event(
                mock_room, "room-123", "player-123", occupant_names, mock_connection_manager
            )

            assert result["event_type"] == "room_update"
            assert result["data"]["occupants"] == occupant_names
            assert result["data"]["occupant_count"] == 2

    @pytest.mark.asyncio
    async def test_build_room_update_event_with_room_drops(self) -> None:
        """Test building room update event with room drops."""
        mock_room = MagicMock()
        mock_room.to_dict.return_value = {"room_id": "room-123", "name": "Test Room"}
        mock_room.get_players.return_value = []
        mock_room.get_objects.return_value = []
        mock_room.get_npcs.return_value = []
        mock_room.get_occupant_count.return_value = 0

        mock_room_manager = MagicMock()
        mock_room_manager.list_room_drops.return_value = [{"item_id": "item-1"}]

        mock_connection_manager = AsyncMock()
        mock_connection_manager.convert_room_players_uuids_to_names = AsyncMock(
            return_value={"room_id": "room-123", "name": "Test Room"}
        )
        mock_connection_manager.room_manager = mock_room_manager

        with patch("server.realtime.websocket_room_updates.logger"):
            result = await build_room_update_event(mock_room, "room-123", "player-123", [], mock_connection_manager)

            assert "room_drops" in result["data"]
            assert "drop_summary" in result["data"]


class TestUpdatePlayerRoomSubscription:
    """Test update_player_room_subscription function."""

    @pytest.mark.asyncio
    async def test_update_player_room_subscription_new_room(self) -> None:
        """Test updating subscription when player moves to new room."""
        mock_connection_manager = AsyncMock()
        mock_player = MagicMock()
        mock_player.current_room_id = "room-1"
        mock_connection_manager.get_player = AsyncMock(return_value=mock_player)
        mock_connection_manager.unsubscribe_from_room = AsyncMock()
        mock_connection_manager.subscribe_to_room = AsyncMock()

        with patch("server.realtime.websocket_room_updates.logger"):
            await update_player_room_subscription(mock_connection_manager, "player-123", "room-2")

            mock_connection_manager.unsubscribe_from_room.assert_called_once_with("player-123", "room-1")
            mock_connection_manager.subscribe_to_room.assert_called_once_with("player-123", "room-2")
            assert mock_player.current_room_id == "room-2"

    @pytest.mark.asyncio
    async def test_update_player_room_subscription_same_room(self) -> None:
        """Test updating subscription when player stays in same room."""
        mock_connection_manager = AsyncMock()
        mock_player = MagicMock()
        mock_player.current_room_id = "room-1"
        mock_connection_manager.get_player = AsyncMock(return_value=mock_player)
        mock_connection_manager.unsubscribe_from_room = AsyncMock()
        mock_connection_manager.subscribe_to_room = AsyncMock()

        with patch("server.realtime.websocket_room_updates.logger"):
            await update_player_room_subscription(mock_connection_manager, "player-123", "room-1")

            mock_connection_manager.unsubscribe_from_room.assert_not_called()
            mock_connection_manager.subscribe_to_room.assert_called_once()

    @pytest.mark.asyncio
    async def test_update_player_room_subscription_no_player(self) -> None:
        """Test updating subscription when player is not found."""
        mock_connection_manager = AsyncMock()
        mock_connection_manager.get_player = AsyncMock(return_value=None)

        await update_player_room_subscription(mock_connection_manager, "player-123", "room-1")

        # Should return early without doing anything


class TestBroadcastRoomUpdate:
    """Test broadcast_room_update function."""

    @pytest.mark.asyncio
    async def test_broadcast_room_update_success(self) -> None:
        """Test successfully broadcasting room update."""
        mock_connection_manager = AsyncMock()
        mock_connection_manager.get_room_occupants = AsyncMock(return_value=[{"player_name": "Player1"}])
        mock_connection_manager.convert_room_players_uuids_to_names = AsyncMock(
            return_value={"room_id": "room-123", "name": "Test Room"}
        )
        mock_connection_manager.broadcast_to_room = AsyncMock()
        mock_connection_manager.get_player = AsyncMock(return_value=MagicMock())
        mock_connection_manager.subscribe_to_room = AsyncMock()
        mock_connection_manager.room_manager = None

        mock_room = MagicMock()
        mock_room.to_dict.return_value = {"room_id": "room-123", "name": "Test Room"}
        mock_room.get_players.return_value = []
        mock_room.get_objects.return_value = []
        mock_room.get_npcs.return_value = []
        mock_room.get_occupant_count.return_value = 0

        mock_async_persistence = MagicMock()
        mock_async_persistence.get_room_by_id.return_value = mock_room

        with patch("server.async_persistence.get_async_persistence", return_value=mock_async_persistence):
            with patch(
                "server.realtime.websocket_room_updates.get_npc_occupants_from_lifecycle_manager",
                new_callable=AsyncMock,
            ) as mock_npc:
                mock_npc.return_value = []
                with patch("server.realtime.websocket_room_updates.logger"):
                    await broadcast_room_update("player-123", "room-123", mock_connection_manager)

                    mock_connection_manager.broadcast_to_room.assert_called_once()

    @pytest.mark.asyncio
    async def test_broadcast_room_update_no_room(self) -> None:
        """Test broadcasting room update when room is not found."""
        mock_connection_manager = AsyncMock()

        mock_async_persistence = MagicMock()
        mock_async_persistence.get_room_by_id.return_value = None

        with patch("server.async_persistence.get_async_persistence", return_value=mock_async_persistence):
            with patch("server.realtime.websocket_room_updates.logger"):
                await broadcast_room_update("player-123", "room-123", mock_connection_manager)

                mock_connection_manager.broadcast_to_room.assert_not_called()

    @pytest.mark.asyncio
    async def test_broadcast_room_update_npc_fallback(self) -> None:
        """Test broadcasting room update with NPC fallback."""
        mock_connection_manager = AsyncMock()
        mock_connection_manager.get_room_occupants = AsyncMock(return_value=[])
        mock_connection_manager.convert_room_players_uuids_to_names = AsyncMock(
            return_value={"room_id": "room-123", "name": "Test Room"}
        )
        mock_connection_manager.broadcast_to_room = AsyncMock()
        mock_connection_manager.get_player = AsyncMock(return_value=MagicMock())
        mock_connection_manager.subscribe_to_room = AsyncMock()
        mock_connection_manager.room_manager = None

        mock_room = MagicMock()
        mock_room.to_dict.return_value = {"room_id": "room-123", "name": "Test Room"}
        mock_room.get_players.return_value = []
        mock_room.get_objects.return_value = []
        mock_room.get_npcs.return_value = []
        mock_room.get_occupant_count.return_value = 0

        mock_async_persistence = MagicMock()
        mock_async_persistence.get_room_by_id.return_value = mock_room

        with patch("server.async_persistence.get_async_persistence", return_value=mock_async_persistence):
            with patch(
                "server.realtime.websocket_room_updates.get_npc_occupants_from_lifecycle_manager",
                new_callable=AsyncMock,
            ) as mock_npc:
                mock_npc.side_effect = AttributeError("Error")
                with patch(
                    "server.realtime.websocket_room_updates.get_npc_occupants_fallback", new_callable=AsyncMock
                ) as mock_fallback:
                    mock_fallback.return_value = []
                    with patch("server.realtime.websocket_room_updates.logger"):
                        await broadcast_room_update("player-123", "room-123", mock_connection_manager)

                        mock_connection_manager.broadcast_to_room.assert_called_once()
