"""Unit tests for respawn room occupant enrichment helpers."""

# pyright: reportPrivateUsage=false
# Reason: Tests call module-private respawn room helpers directly.

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime import player_event_handlers_respawn_room as respawn_room


def _host(*, connection_manager: object | None = None) -> MagicMock:
    host: MagicMock = MagicMock()
    host.connection_manager = connection_manager
    return host


def test_extract_occupant_names_splits_npc_and_player() -> None:
    occupants: list[dict[str, object]] = [
        {"npc_id": "n1", "npc_name": "Cultist"},
        {"player_id": "p1", "player_name": "Investigator"},
    ]
    npc_names, player_names, occupant_names = respawn_room.extract_occupant_names(occupants, "Respawned")
    assert "Cultist" in npc_names
    assert "Investigator" in player_names
    assert "Respawned" in player_names
    assert "Cultist" in occupant_names
    assert "Investigator" in occupant_names
    assert "Respawned" in occupant_names


def test_merge_player_lists_appends_missing() -> None:
    occupant_names = ["Alice"]
    merged = respawn_room.merge_player_lists(["Bob"], ["Alice"], occupant_names)
    assert merged == ["Alice", "Bob"]
    assert "Bob" in occupant_names


@pytest.mark.asyncio
async def test_convert_npc_ids_to_names_resolves_lifecycle_and_short_ids() -> None:
    host = _host(connection_manager=MagicMock())
    with patch(
        "server.realtime.player_event_handlers_respawn_room.get_npc_name_from_lifecycle_manager",
        return_value="Deep One",
    ):
        names = await respawn_room.convert_npc_ids_to_names(
            host,
            ["npc_instance_aaaaaaaaaaaaaaaaaaaa", "Guard"],
            [],
            [],
        )
    assert "Deep One" in names
    assert "Guard" in names


def test_get_npc_name_from_lifecycle_manager_returns_name() -> None:
    npc: MagicMock = MagicMock()
    npc.name = "Ghoul"
    lifecycle: MagicMock = MagicMock()
    lifecycle.active_npcs = {"npc-1": npc}
    cm: MagicMock = MagicMock()
    host = _host(connection_manager=cm)
    with patch(
        "server.realtime.websocket_initial_state.get_npc_lifecycle_manager_from_connection_manager",
        return_value=lifecycle,
    ):
        assert respawn_room.get_npc_name_from_lifecycle_manager(host, "npc-1") == "Ghoul"


def test_get_npc_name_from_lifecycle_manager_no_connection_manager() -> None:
    assert respawn_room.get_npc_name_from_lifecycle_manager(_host(connection_manager=None), "npc-1") is None


def test_room_data_from_persistence_room() -> None:
    room: MagicMock = MagicMock()
    room.to_dict = MagicMock(return_value={"id": "room-1", "name": "Foyer"})
    room_data, npc_names, player_names, occupant_names = respawn_room.room_data_from_persistence_room(
        _host(), room, "Alice"
    )
    assert room_data["id"] == "room-1"
    assert npc_names == []
    assert "Alice" in player_names
    assert "Alice" in occupant_names


@pytest.mark.asyncio
async def test_enrich_room_data_with_occupant_names() -> None:
    host = _host(connection_manager=MagicMock())
    room_data: dict[str, object] = {"npcs": ["Guard"], "players": ["Bob"]}
    occupants: list[dict[str, object]] = [{"player_name": "Alice"}]
    npc_names, player_names, occupant_names = await respawn_room.enrich_room_data_with_occupant_names(
        host, room_data, occupants, "Alice"
    )
    assert room_data["npcs"] == npc_names
    assert room_data["players"] == player_names
    assert room_data["occupants"] == occupant_names
    assert room_data["occupant_count"] == len(occupant_names)
    assert "Alice" in player_names
    assert "Guard" in npc_names


@pytest.mark.asyncio
async def test_prepare_room_data_for_respawn_no_connection_manager() -> None:
    room: MagicMock = MagicMock()
    room.to_dict = MagicMock(return_value={"id": "room-1"})
    persistence: MagicMock = MagicMock()
    persistence.get_room_by_id = MagicMock(return_value=room)
    host = _host(connection_manager=None)
    logger: MagicMock = MagicMock()
    with patch(
        "server.container.async_persistence_access.get_container_async_persistence",
        return_value=persistence,
    ):
        room_data, _npc, players, occupants = await respawn_room.prepare_room_data_for_respawn(
            host, "room-1", "Alice", logger
        )
    assert room_data is not None
    assert room_data["id"] == "room-1"
    assert "Alice" in players
    assert "Alice" in occupants


@pytest.mark.asyncio
async def test_prepare_room_data_for_respawn_with_connection_manager() -> None:
    room: MagicMock = MagicMock()
    persistence: MagicMock = MagicMock()
    persistence.get_room_by_id = MagicMock(return_value=room)
    cm: MagicMock = MagicMock()
    cm.get_room_occupants = AsyncMock(return_value=[{"player_name": "Bob"}])
    host = _host(connection_manager=cm)
    logger: MagicMock = MagicMock()
    with (
        patch("server.container.async_persistence_access.get_container_async_persistence", return_value=persistence),
        patch(
            "server.realtime.websocket_initial_state.prepare_room_data_with_occupants",
            new_callable=AsyncMock,
            return_value=({"id": "room-1", "npcs": [], "players": []}, None),
        ),
    ):
        room_data, _npc, players, occupants = await respawn_room.prepare_room_data_for_respawn(
            host, "room-1", "Alice", logger
        )
    assert room_data is not None
    assert "Alice" in players
    assert "Bob" in players or "Alice" in occupants


@pytest.mark.asyncio
async def test_prepare_room_data_for_respawn_logs_on_error() -> None:
    logger: MagicMock = MagicMock()
    warning: MagicMock = MagicMock()
    logger.warning = warning
    host = _host(connection_manager=MagicMock())
    with patch(
        "server.container.async_persistence_access.get_container_async_persistence",
        side_effect=ImportError("missing"),
    ):
        room_data, npc_names, player_names, occupant_names = await respawn_room.prepare_room_data_for_respawn(
            host, "room-1", "Alice", logger
        )
    assert room_data is None
    assert npc_names == []
    assert player_names == []
    assert occupant_names == []
    warning.assert_called_once()
