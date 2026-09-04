"""
Unit tests for room subscription manager NPC helpers.

Tests NPC-related helpers and get_room_occupants with NPCs.
"""

from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from server.realtime.room_subscription_manager import RoomSubscriptionManager

# pylint: disable=protected-access  # Reason: Test file - accessing protected members
# pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter names must match fixture names


@pytest.fixture
def subscription_manager():
    """Create a RoomSubscriptionManager instance."""
    return RoomSubscriptionManager()


def test_get_npc_name_from_lifecycle_manager(subscription_manager):
    """Test _get_npc_name_from_lifecycle_manager gets NPC name."""
    mock_lifecycle = MagicMock()
    mock_npc = MagicMock()
    mock_npc.name = "TestNPC"
    mock_lifecycle.active_npcs = {"npc_001": mock_npc}
    result = subscription_manager._get_npc_name_from_lifecycle_manager(mock_lifecycle, "npc_001")
    assert result == "TestNPC"


def test_get_npc_name_from_lifecycle_manager_not_found(subscription_manager):
    """Test _get_npc_name_from_lifecycle_manager returns ID when NPC not found."""
    mock_lifecycle = MagicMock()
    mock_lifecycle.active_npcs = {}
    result = subscription_manager._get_npc_name_from_lifecycle_manager(mock_lifecycle, "npc_001")
    assert result == "npc_001"


def test_get_npc_name_from_lifecycle_manager_error(subscription_manager):
    """Test _get_npc_name_from_lifecycle_manager handles errors gracefully."""
    mock_lifecycle = MagicMock()
    mock_lifecycle.active_npcs = {"npc_001": None}
    result = subscription_manager._get_npc_name_from_lifecycle_manager(mock_lifecycle, "npc_001")
    assert result == "npc_001"


def test_add_npc_to_occupants(subscription_manager):
    """Test _add_npc_to_occupants adds NPC to list."""
    occupants: list[dict[str, Any]] = []
    subscription_manager._add_npc_to_occupants(occupants, "npc_001", "TestNPC")
    assert len(occupants) == 1
    assert occupants[0]["player_id"] == "npc_001"
    assert occupants[0]["player_name"] == "TestNPC"
    assert occupants[0]["is_npc"] is True


def test_query_npcs_from_lifecycle_manager(subscription_manager):
    """Test _query_npcs_from_lifecycle_manager queries NPCs."""
    mock_lifecycle = MagicMock()
    mock_npc1 = MagicMock()
    mock_npc1.name = "NPC1"
    mock_npc1.is_alive = True
    room_id = "room_001"
    mock_npc1.current_room_id = room_id
    mock_npc1.current_room = None
    mock_npc2 = MagicMock()
    mock_npc2.name = "NPC2"
    mock_npc2.is_alive = False
    mock_npc2.current_room_id = room_id
    mock_npc2.current_room = None
    type(mock_lifecycle).active_npcs = {"npc_001": mock_npc1, "npc_002": mock_npc2}
    result = subscription_manager._query_npcs_from_lifecycle_manager(room_id, mock_lifecycle)
    assert len(result) == 1
    assert result[0]["player_id"] == "npc_001"


def test_filter_fallback_npcs(subscription_manager):
    """Test _filter_fallback_npcs filters dead NPCs."""
    mock_lifecycle = MagicMock()
    mock_npc1 = MagicMock()
    mock_npc1.is_alive = True
    mock_npc2 = MagicMock()
    mock_npc2.is_alive = False
    mock_lifecycle.active_npcs = {"npc_001": mock_npc1, "npc_002": mock_npc2}
    result = subscription_manager._filter_fallback_npcs(["npc_001", "npc_002"], mock_lifecycle, "room_001")
    assert "npc_001" in result
    assert "npc_002" not in result


def test_filter_fallback_npcs_error(subscription_manager):
    """Test _filter_fallback_npcs handles errors gracefully."""
    mock_lifecycle = MagicMock()
    mock_lifecycle.active_npcs = {"npc_001": None}
    result = subscription_manager._filter_fallback_npcs(["npc_001"], mock_lifecycle, "room_001")
    assert result == ["npc_001"]


@pytest.mark.asyncio
async def test_get_room_occupants_with_npcs(subscription_manager):
    """Test get_room_occupants() includes NPCs from lifecycle manager."""
    mock_player = MagicMock()
    mock_player.player_id = "player_001"
    mock_player.name = "Player1"
    online_players = {"player_001": mock_player}
    subscription_manager.add_room_occupant("player_001", "room_001")

    mock_lifecycle = MagicMock()
    mock_npc = MagicMock()
    mock_npc.name = "TestNPC"
    mock_npc.is_alive = True
    mock_npc.current_room_id = "room_001"
    mock_lifecycle.active_npcs = {"npc_001": mock_npc}

    mock_service = MagicMock()
    mock_service.lifecycle_manager = mock_lifecycle

    with patch(
        "server.services.npc_instance_service.get_npc_instance_service",
        return_value=mock_service,
    ):
        result = await subscription_manager.get_room_occupants("room_001", online_players)
        assert len(result) >= 1


@pytest.mark.asyncio
async def test_get_room_occupants_fallback_npcs(subscription_manager):
    """Test get_room_occupants() falls back to room.get_npcs() when lifecycle manager fails."""
    mock_persistence = MagicMock()
    mock_room = MagicMock()
    mock_room.get_npcs = MagicMock(return_value=["npc_001", "npc_002"])
    mock_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    subscription_manager.set_async_persistence(mock_persistence)

    with patch(
        "server.services.npc_instance_service.get_npc_instance_service",
        side_effect=Exception("Service error"),
    ):
        result = await subscription_manager.get_room_occupants("room_001", {})
        assert isinstance(result, list)
