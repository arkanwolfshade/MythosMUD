"""
Unit tests for the per-viewer room-payload fan-out (#714).

Split out of test_websocket_room_updates.py to keep that module under the project's
too-many-lines limit -- mirrors the existing split for test_websocket_room_updates_build_event.py.
"""

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.websocket_room_updates import broadcast_room_update

TEST_PLAYER_ID_STR = str(uuid.UUID("12345678-1234-5678-1234-567812345678"))


def _same_room_data(room_data: dict[str, object]) -> dict[str, object]:
    """Pass room_data through unchanged -- stands in for real UUID-to-name conversion."""
    return room_data


@pytest.fixture
def mock_connection_manager() -> AsyncMock:
    """Create a mock connection manager."""
    manager = AsyncMock()
    manager.get_room_occupants = AsyncMock(return_value=[])
    manager.convert_room_players_uuids_to_names = AsyncMock(side_effect=_same_room_data)
    manager.broadcast_to_room = AsyncMock()
    return manager


def _phantom_data_for(player_id: str, room_id: str) -> dict[str, object]:
    """Shared phantom data fixture for the hallucinating-viewer fan-out test."""
    return {
        "phantom_id": "phantom_1",
        "player_id": player_id,
        "room_id": room_id,
        "name": "Shambling Horror",
        "tier": "fractured",
        "max_dp": 1,
        "current_dp": 1,
        "is_non_damaging": True,
    }


def _make_mock_room(room_id: str, player_ids: list[str]) -> MagicMock:
    """Build a mock Room with its attributes set via constructor kwargs, not post-hoc reads."""
    return MagicMock(
        id=room_id,
        to_dict=MagicMock(return_value={"id": room_id, "name": "Test Room"}),
        get_players=MagicMock(return_value=player_ids),
        get_npcs=MagicMock(return_value=[]),
    )


def _has_phantom_for(only_player_id: str):
    """side_effect for get_active_phantoms: only_player_id sees one phantom, nobody else does."""

    def _get_active_phantoms(player_id: object) -> list[str]:
        return ["phantom_1"] if str(player_id) == only_player_id else []

    return _get_active_phantoms


def _sent_events(mock: AsyncMock) -> list[tuple[str, dict[str, object]]]:
    """Read back (recipient_id, event) pairs from send_personal_message's call history."""
    return [(str(cast("object", c.args[0])), cast("dict[str, object]", c.args[1])) for c in mock.call_args_list]


def _setup_hallucinating_room(mock_connection_manager: AsyncMock, player_id: str, room_id: str) -> str:
    """Wire mock_connection_manager for a room where only `player_id` sees a phantom."""
    other_player_id = str(uuid.uuid4())
    mock_connection_manager.get_player = AsyncMock(return_value=MagicMock(current_room_id=room_id))
    mock_connection_manager.send_personal_message = AsyncMock(return_value={})
    mock_connection_manager.async_persistence = MagicMock(
        get_room_by_id=MagicMock(return_value=_make_mock_room(room_id, [player_id, other_player_id]))
    )
    return other_player_id


@pytest.mark.asyncio
async def test_broadcast_room_update_personalizes_for_hallucinating_viewer(mock_connection_manager: AsyncMock):
    """#714: a room with an active phantom fans out per-viewer instead of one broadcast."""
    player_id = TEST_PLAYER_ID_STR
    room_id = "room_123"
    other_player_id = _setup_hallucinating_room(mock_connection_manager, player_id, room_id)

    with (
        patch("server.realtime.websocket_room_updates.get_player_occupants", AsyncMock(return_value=["P1", "P2"])),
        patch("server.realtime.websocket_room_updates.get_npc_occupants", AsyncMock(return_value=[])),
        patch("server.realtime.websocket_room_updates.get_npc_instance_service", return_value=MagicMock()),
        patch(
            "server.services.phantom_hostile_service.phantom_hostile_service.get_active_phantoms",
            side_effect=_has_phantom_for(player_id),
        ),
        patch(
            "server.services.phantom_hostile_service.phantom_hostile_service.get_phantom_data",
            return_value=_phantom_data_for(player_id, room_id),
        ),
    ):
        await broadcast_room_update(player_id, room_id, mock_connection_manager)

    broadcast_to_room = cast(AsyncMock, mock_connection_manager.broadcast_to_room)
    send_personal_message = cast(AsyncMock, mock_connection_manager.send_personal_message)

    # Personalized fan-out replaces the broadcast entirely: one room_update + one
    # room_occupants per connected player (2 players).
    broadcast_to_room.assert_not_called()
    assert send_personal_message.call_count == 4

    sent = _sent_events(send_personal_message)
    sent_to_hallucinator = [event for recipient, event in sent if recipient == player_id]
    sent_to_other = [event for recipient, event in sent if recipient == other_player_id]

    def npcs_of(event: dict[str, object]) -> object:
        return cast("dict[str, object]", event["data"]).get("npcs", [])

    assert any("Shambling Horror" in cast("list[object]", npcs_of(event)) for event in sent_to_hallucinator)
    assert all("Shambling Horror" not in cast("list[object]", npcs_of(event)) for event in sent_to_other)


@pytest.mark.asyncio
async def test_broadcast_room_update_no_hallucinators_uses_broadcast(mock_connection_manager: AsyncMock):
    """The fast path: an empty phantom roster still broadcasts once, unchanged (#714)."""
    player_id = TEST_PLAYER_ID_STR
    room_id = "room_123"

    mock_connection_manager.get_player = AsyncMock(return_value=MagicMock(current_room_id=room_id))
    mock_connection_manager.send_personal_message = AsyncMock(return_value={})
    mock_connection_manager.async_persistence = MagicMock(
        get_room_by_id=MagicMock(return_value=_make_mock_room(room_id, [player_id]))
    )

    with (
        patch("server.realtime.websocket_room_updates.get_player_occupants", AsyncMock(return_value=["P1"])),
        patch("server.realtime.websocket_room_updates.get_npc_occupants", AsyncMock(return_value=[])),
        patch("server.realtime.websocket_room_updates.get_npc_instance_service", return_value=MagicMock()),
        patch(
            "server.services.phantom_hostile_service.phantom_hostile_service.get_active_phantoms",
            return_value=[],
        ),
    ):
        await broadcast_room_update(player_id, room_id, mock_connection_manager)

    broadcast_to_room = cast(AsyncMock, mock_connection_manager.broadcast_to_room)
    send_personal_message = cast(AsyncMock, mock_connection_manager.send_personal_message)
    assert broadcast_to_room.call_count == 2
    send_personal_message.assert_not_called()
