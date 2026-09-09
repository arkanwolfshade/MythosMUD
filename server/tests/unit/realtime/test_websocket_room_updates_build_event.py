"""
Unit tests for websocket room updates build event function.

Tests the build_room_update_event function in websocket_room_updates.py.
"""

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.room_update_event_builder import build_room_update_event


@pytest.fixture
def mock_room() -> MagicMock:
    """Create a mock room."""
    return MagicMock(
        to_dict=MagicMock(return_value={"id": "room_001", "name": "Test Room"}),
        get_players=MagicMock(return_value=[]),
        get_objects=MagicMock(return_value=[]),
        get_npcs=MagicMock(return_value=[]),
        get_occupant_count=MagicMock(return_value=0),
    )


@pytest.fixture
def mock_connection_manager() -> MagicMock:
    """Create a mock connection manager."""
    return MagicMock(
        convert_room_players_uuids_to_names=AsyncMock(return_value={"id": "room_001", "name": "Test Room"}),
        room_manager=MagicMock(list_room_drops=MagicMock(return_value=[])),
    )


@pytest.mark.asyncio
async def test_build_room_update_event(mock_room: MagicMock, mock_connection_manager: MagicMock):
    """Test build_room_update_event() creates room update event."""
    occupant_names = ["Player1", "NPC1"]
    result = await build_room_update_event(mock_room, "room_001", "player_001", occupant_names, mock_connection_manager)
    data = cast(dict[str, object], result["data"])
    assert "event_type" in result
    assert result["event_type"] == "room_update"
    assert "data" in result
    assert "room" in data
    assert "occupants" in data


@pytest.mark.asyncio
async def test_build_room_update_event_hallucinates_exits_for_deranged_viewer(
    mock_room: MagicMock, mock_connection_manager: MagicMock
):
    """#626/#714: viewer_id, when cached as deranged, replaces exits with the seeded lie."""
    viewer_id = str(uuid.uuid4())

    with (
        patch(
            "server.realtime.room_update_event_builder.lucidity_tier_cache.is_deranged",
            return_value=True,
        ),
        patch(
            "server.realtime.room_update_event_builder.get_hallucinated_exits",
            return_value=["east", "up"],
        ) as mock_get_hallucinated,
    ):
        result = await build_room_update_event(
            mock_room, "room_001", "player_001", ["Player1"], mock_connection_manager, viewer_id=viewer_id
        )

    mock_get_hallucinated.assert_called_once_with("room_001", viewer_id)
    data = cast(dict[str, object], result["data"])
    room_data = cast(dict[str, object], data["room"])
    assert room_data["exits"] == {"east": "?", "up": "?"}


@pytest.mark.asyncio
async def test_build_room_update_event_no_viewer_id_leaves_exits_untouched(
    mock_room: MagicMock, mock_connection_manager: MagicMock
):
    """The non-personalized fast path (no viewer_id) never triggers the exit override."""
    with patch("server.realtime.room_update_event_builder.get_hallucinated_exits") as mock_get_hallucinated:
        result = await build_room_update_event(mock_room, "room_001", "player_001", ["Player1"], mock_connection_manager)

    mock_get_hallucinated.assert_not_called()
    data = cast(dict[str, object], result["data"])
    room_data = cast(dict[str, object], data["room"])
    assert "exits" not in room_data
