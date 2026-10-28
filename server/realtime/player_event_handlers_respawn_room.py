"""Room occupant enrichment for respawn WebSocket payloads."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, cast

from structlog.stdlib import BoundLogger

from ..constants.npc_disposition import DEFAULT_NPC_DISPOSITION, NpcOccupant
from ..models.room import Room
from .connection_utils import get_npc_disposition_from_instance, npc_disposition_from_row
from .player_event_handlers_respawn_types import (
    append_unique_npc_occupant,
    append_unique_valid_occupant,
    ensure_respawned_player_in_lists,
    is_npc_occupant_row,
    occupant_str_field,
)

if TYPE_CHECKING:
    from .connection_manager import ConnectionManager


class _RespawnRoomHost(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Handler surface required for room preparation helpers."""

    connection_manager: ConnectionManager | None


async def prepare_room_data_for_respawn(
    host: _RespawnRoomHost,
    room_id: str,
    respawned_player_name: str,
    logger: BoundLogger,
) -> tuple[dict[str, object] | None, list[NpcOccupant], list[str], list[str]]:
    """Prepare room data with NPC occupants and player names for a respawn event."""
    room_data = None
    occupant_names: list[str] = []
    npc_names: list[NpcOccupant] = []
    player_names: list[str] = []

    try:
        from ..container.async_persistence_access import get_container_async_persistence
        from .websocket_initial_state import prepare_room_data_with_occupants

        async_persistence = get_container_async_persistence()
        room = async_persistence.get_room_by_id(room_id)
        if not room:
            return None, npc_names, player_names, occupant_names

        connection_manager = host.connection_manager
        if connection_manager is None:
            return room_data_from_persistence_room(host, room, respawned_player_name)

        room_data, _ = await prepare_room_data_with_occupants(room, room_id, connection_manager)
        room_occupants = await connection_manager.get_room_occupants(room_id)
        if room_data:
            npc_names, player_names, occupant_names = await enrich_room_data_with_occupant_names(
                host, room_data, room_occupants, respawned_player_name
            )

    except (AttributeError, KeyError, ValueError, TypeError, ImportError) as room_err:
        logger.warning(
            "Could not get room data for respawn event",
            room_id=room_id,
            error=str(room_err),
        )

    return room_data, npc_names, player_names, occupant_names


def room_data_from_persistence_room(
    _host: _RespawnRoomHost, room: Room, respawned_player_name: str
) -> tuple[dict[str, object], list[NpcOccupant], list[str], list[str]]:
    """Build room payload from persistence when no live connection manager is available."""
    room_data = cast(dict[str, object], room.to_dict())
    npc_names, player_names, occupant_names = extract_occupant_names(None, respawned_player_name)
    return room_data, npc_names, player_names, occupant_names


async def enrich_room_data_with_occupant_names(
    host: _RespawnRoomHost,
    room_data: dict[str, object],
    room_occupants: list[dict[str, object]] | None,
    respawned_player_name: str,
) -> tuple[list[NpcOccupant], list[str], list[str]]:
    """Merge live occupants into room_data and return the NPC and name lists for the respawn payload."""
    npc_names, player_names, occupant_names = extract_occupant_names(room_occupants, respawned_player_name)
    npc_names = await convert_npc_ids_to_names(
        host, cast(list[object], room_data.get("npcs", [])), npc_names, occupant_names
    )
    player_names = merge_player_lists(cast(list[str], room_data.get("players", [])), player_names, occupant_names)
    room_data["npcs"] = npc_names
    room_data["players"] = player_names
    room_data["occupants"] = occupant_names
    room_data["occupant_count"] = len(occupant_names)
    return npc_names, player_names, occupant_names


def extract_occupant_names(
    room_occupants: list[dict[str, object]] | None, respawned_player_name: str
) -> tuple[list[NpcOccupant], list[str], list[str]]:
    """Extract NPC occupants and player names from room occupants."""
    from .websocket_helpers import validate_occupant_name

    npc_names: list[NpcOccupant] = []
    player_names: list[str] = []
    occupant_names: list[str] = []

    for occ in room_occupants or []:
        if is_npc_occupant_row(occ):
            npc_name = occupant_str_field(occ, ("npc_name", "name", "player_name"))
            append_unique_npc_occupant(
                npc_name, npc_disposition_from_row(occ), npcs=npc_names, occupant_names=occupant_names
            )
        else:
            player_name = occupant_str_field(occ, ("player_name", "name"))
            append_unique_valid_occupant(
                player_name,
                primary=player_names,
                occupant_names=occupant_names,
                validate_name=validate_occupant_name,
            )

    ensure_respawned_player_in_lists(
        respawned_player_name,
        player_names=player_names,
        occupant_names=occupant_names,
        validate_name=validate_occupant_name,
    )

    return npc_names, player_names, occupant_names


async def convert_npc_ids_to_names(
    host: _RespawnRoomHost, existing_npcs: list[object], npcs: list[NpcOccupant], occupant_names: list[str]
) -> list[NpcOccupant]:
    """
    Merge room_data's NPCs into the extracted ones.

    An entry is normally an ``NpcOccupant`` already (disposition included); a bare string is a legacy NPC id or
    name and is resolved through the lifecycle manager.
    """
    result = list(npcs)

    for entry in existing_npcs:
        if isinstance(entry, dict):
            fields = cast(dict[str, object], entry)
            name = fields.get("name")
            if isinstance(name, str):
                append_unique_npc_occupant(
                    name, npc_disposition_from_row(fields), npcs=result, occupant_names=occupant_names
                )
        elif isinstance(entry, str):
            if "_" in entry or len(entry) > 20:
                npc_name = get_npc_name_from_lifecycle_manager(host, entry)
                disposition = get_npc_disposition_from_instance(entry)
            else:
                npc_name, disposition = entry, DEFAULT_NPC_DISPOSITION
            append_unique_npc_occupant(npc_name, disposition, npcs=result, occupant_names=occupant_names)

    return result


def get_npc_name_from_lifecycle_manager(host: _RespawnRoomHost, npc_id: str) -> str | None:
    """Get NPC name from lifecycle manager."""
    if not host.connection_manager:
        return None

    from .websocket_initial_state import get_npc_lifecycle_manager_from_connection_manager

    npc_lifecycle_manager = get_npc_lifecycle_manager_from_connection_manager(host.connection_manager)
    if not npc_lifecycle_manager:
        return None

    npc = npc_lifecycle_manager.active_npcs.get(npc_id)
    if npc is None:
        return None
    return npc.name


def merge_player_lists(existing_players: list[str], player_names: list[str], occupant_names: list[str]) -> list[str]:
    """Merge existing player list with extracted player names."""
    result = list(player_names)

    for existing_player in existing_players:
        if existing_player not in result:
            result.append(existing_player)
            if existing_player not in occupant_names:
                occupant_names.append(existing_player)

    return result
