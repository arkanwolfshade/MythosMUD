"""
WebSocket room update and broadcast functions for MythosMUD real-time communication.

This module handles room updates and broadcasting to players.
"""

import uuid
from typing import TYPE_CHECKING, Any, cast

from ..services.npc_instance_service import get_npc_instance_service
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.room_renderer import build_room_drop_summary, clone_room_drops
from .envelope import build_event
from .occupant_display import format_occupant_display_name
from .running_app import connection_manager_from_running_app
from .websocket_helpers import convert_uuids_to_strings, get_npc_name_from_instance

if TYPE_CHECKING:
    from ..models.room import Room
    from .connection_manager import ConnectionManager

logger = get_logger(__name__)


def _looks_like_player_uuid(value: object) -> bool:
    """
    True if value is a str that parses as a UUID (i.e. a real player_id, not a room_id).

    Callers may pass a room_id in the player_id slot for room-only refreshes (e.g. after an NPC
    death via EventBus); this predicate is how those call sites are told apart from a real
    player_id, without swallowing exceptions raised by whatever real work follows the check.
    """
    if not isinstance(value, str):
        return False
    try:
        _ = uuid.UUID(value)
    except (ValueError, TypeError):
        return False
    return True


async def get_player_occupants(connection_manager: "ConnectionManager | Any", room_id: str) -> list[str]:
    """
    Get player occupant names from room.

    Includes "(linkdead)" indicator for players in grace period.
    """
    occupant_names = []
    try:
        room_occupants = await connection_manager.get_room_occupants(room_id)
        for occ in room_occupants or []:
            # Only include actual players: skip NPCs even if dict has player_name (e.g. merged format with is_npc).
            if occ.get("is_npc") or "npc_name" in occ:
                continue
            name_obj = occ.get("player_name") or occ.get("name")
            if not isinstance(name_obj, str):
                continue
            player_id_raw = occ.get("player_id")
            player_id: uuid.UUID | str | None
            if isinstance(player_id_raw, uuid.UUID | str) or player_id_raw is None:
                player_id = player_id_raw
            else:
                player_id = str(player_id_raw)
            occupant_names.append(format_occupant_display_name(name_obj, player_id, connection_manager))
    except (AttributeError, KeyError, TypeError, ValueError) as e:
        logger.error("Error transforming room occupants", room_id=room_id, error=str(e))
    return occupant_names


async def get_npc_occupants(room: "Room | Any", room_id: str) -> list[str]:
    """
    Get NPC occupant names for a room.

    Room membership comes from `room.get_npcs()` — the Room model's own authoritative list —
    filtered to NPCs the lifecycle manager still considers alive. On any lookup failure (missing
    service, missing lifecycle manager, missing active_npcs) this fails closed: logs a warning
    and returns no NPCs, rather than showing an unfiltered (possibly dead) occupant list.
    """
    occupant_names = []
    room_npc_ids = room.get_npcs()
    logger.debug("Room has NPCs", room_id=room_id, npc_ids=room_npc_ids)

    filtered_npc_ids: list[str] = []
    try:
        npc_instance_service = get_npc_instance_service()
        active_npcs = npc_instance_service.lifecycle_manager.active_npcs
        for npc_id in room_npc_ids:
            npc_instance = active_npcs.get(npc_id)
            if npc_instance is None:
                continue
            if npc_instance.is_alive:
                filtered_npc_ids.append(npc_id)
            else:
                logger.debug("Filtered dead NPC from room occupants", npc_id=npc_id, room_id=room_id)
    except (AttributeError, KeyError, TypeError, ValueError) as npc_query_error:
        logger.warning(
            "Error querying NPC lifecycle state for room occupants — returning no NPCs",
            room_id=room_id,
            error=str(npc_query_error),
        )
        return []

    for npc_id in filtered_npc_ids:
        npc_name = get_npc_name_from_instance(npc_id)
        if npc_name:
            occupant_names.append(npc_name)

    return occupant_names


async def build_room_update_event(
    room: "Room | Any",
    room_id: str,
    player_id: str,
    occupant_names: list[str],
    connection_manager: "ConnectionManager | Any",
    players: list[str] | None = None,
    npcs: list[str] | None = None,
) -> dict[str, Any]:
    """Build room update event with room data and occupants (players/npcs for structured client UI)."""
    room_data = room.to_dict() if hasattr(room, "to_dict") else room
    if isinstance(room_data, dict):
        room_data = await connection_manager.convert_room_players_uuids_to_names(room_data)

    room_data = convert_uuids_to_strings(room_data)

    room_drops: list[dict[str, Any]] = []
    room_manager = getattr(connection_manager, "room_manager", None)
    if room_manager and hasattr(room_manager, "list_room_drops"):
        try:
            room_drops = clone_room_drops(room_manager.list_room_drops(room_id))
        except (AttributeError, KeyError, TypeError, ValueError) as exc:
            logger.debug("Failed to collect room drops for broadcast", room_id=room_id, error=str(exc))

    drop_summary = build_room_drop_summary(room_drops)

    payload: dict[str, Any] = {
        "room": room_data,
        "entities": [],
        "occupants": occupant_names,
        "occupant_count": len(occupant_names),
        "room_drops": room_drops,
        "drop_summary": drop_summary,
    }
    if players is not None:
        payload["players"] = players
    if npcs is not None:
        payload["npcs"] = npcs

    event_room_id = getattr(room, "id", None) or room_id
    return build_event(
        "room_update",
        payload,
        player_id=player_id,
        room_id=event_room_id,
    )


async def _resolve_room_with_fallback(
    async_persistence: Any,
    connection_manager: "ConnectionManager | Any",
    player_id: str,
    room_id: str,
) -> tuple[Any, str, str]:
    """
    Resolve room by ID, optionally using player's current_room_id as fallback when room not found.

    Returns:
        Tuple of (room_or_none, effective_room_id, resolved_room_id for room_id variable).
    """
    room = async_persistence.get_room_by_id(room_id)
    effective_room_id = room_id
    resolved_room_id = room_id
    # Only a real player_id can have a current_room_id to fall back to (a room-only refresh may
    # pass room_id in this slot). Checking the shape explicitly — rather than treating
    # uuid.UUID()'s ValueError as the test — keeps this gate separate from the try/except below,
    # which stays broad by design (a fallback lookup that fails should degrade gracefully, not
    # crash room resolution) without also silently absorbing a genuine bug in that lookup.
    if room or not _looks_like_player_uuid(player_id):
        return room, effective_room_id, resolved_room_id
    try:
        player = await connection_manager.get_player(uuid.UUID(player_id))
        fallback_room_id = getattr(player, "current_room_id", None) if player else None
        if not fallback_room_id or fallback_room_id == room_id:
            return room, effective_room_id, resolved_room_id
        room = async_persistence.get_room_by_id(fallback_room_id)
        if room:
            resolved_room_id = fallback_room_id
            effective_room_id = fallback_room_id
            logger.debug(
                "Used killer current_room_id fallback for broadcast",
                original_room_id=room_id,
                fallback_room_id=fallback_room_id,
            )
        else:
            effective_room_id = fallback_room_id
    except (ValueError, TypeError, AttributeError) as fallback_error:
        logger.debug(
            "Killer current_room_id fallback lookup failed",
            room_id=room_id,
            player_id=player_id,
            error=str(fallback_error),
        )
    return room, effective_room_id, resolved_room_id


async def update_player_room_subscription(
    connection_manager: "ConnectionManager | Any", player_id: str, room_id: str
) -> None:
    """Update player's room subscription and current room."""
    player_id_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
    player = await connection_manager.get_player(player_id_uuid)
    if not player:
        return

    if hasattr(player, "current_room_id") and player.current_room_id and player.current_room_id != room_id:
        await connection_manager.unsubscribe_from_room(player_id_uuid, str(player.current_room_id))
        logger.debug("Player unsubscribed from old room", player_id=player_id, old_room_id=player.current_room_id)

    await connection_manager.subscribe_to_room(player_id_uuid, room_id)
    logger.debug("Player subscribed to new room", player_id=player_id, new_room_id=room_id)

    player.current_room_id = room_id


async def broadcast_room_update(  # pylint: disable=too-many-locals,too-many-statements  # Reason: Broadcast flow needs room/fallback/connection state; splitting would obscure control flow. Many sequential steps (resolve manager, load room, occupants, build event, broadcast) exceed statement limit.
    player_id: str, room_id: str, connection_manager: "ConnectionManager | None" = None
) -> None:
    """
    Broadcast a room update to all players in the room.

    Args:
        player_id: The player who triggered the update
        room_id: The room's ID
        connection_manager: ConnectionManager instance (optional, will resolve from app.state if not provided)
    """
    logger.debug("broadcast_room_update called", player_id=player_id, room_id=room_id)
    try:
        if connection_manager is None:
            resolved = connection_manager_from_running_app()
            if resolved is None:
                logger.warning("Connection manager not available for room update")
                return
            connection_manager = cast("ConnectionManager", resolved)

        async_persistence = getattr(connection_manager, "async_persistence", None) if connection_manager else None
        if not async_persistence:
            logger.warning("Async persistence layer not available for room update")
            return

        # async_persistence is Any (pre-existing, untyped persistence-facade boundary), so
        # _resolve_room_with_fallback's return is too; cast it here, once, rather than letting
        # Any leak into every downstream use — matching the connection_manager cast above.
        room, effective_room_id, room_id = cast(
            "tuple[Room | None, str, str]",
            await _resolve_room_with_fallback(async_persistence, connection_manager, player_id, room_id),
        )

        player_occupant_names = await get_player_occupants(connection_manager, effective_room_id)
        # NPC occupants need the resolved Room object (room.get_npcs() is the membership source);
        # if room resolution itself failed, there is no NPC list to derive — matches the
        # fail-closed handling inside get_npc_occupants for any other lookup failure.
        npc_occupants = await get_npc_occupants(room, effective_room_id) if room else []
        occupant_names = list(player_occupant_names) + list(npc_occupants)

        occ_payload = {
            "occupants": occupant_names,
            "count": len(occupant_names),
            "players": player_occupant_names,
            "npcs": npc_occupants,
        }
        if not room:
            logger.warning("Room not found for update - sending room_occupants only", room_id=effective_room_id)
            occ_event = build_event(
                "room_occupants",
                occ_payload,
                room_id=effective_room_id,
            )
            await connection_manager.broadcast_to_room(effective_room_id, occ_event)
            logger.debug("Room occupants broadcast (no room cache) completed", room_id=effective_room_id)
            return

        update_event = await build_room_update_event(
            room,
            room_id,
            player_id,
            occupant_names,
            connection_manager,
            players=player_occupant_names,
            npcs=npc_occupants,
        )

        # Only update a player's subscription when player_id is a valid UUID (e.g. killer).
        # When triggering a room-only refresh (e.g. after NPC death via EventBus), caller may pass
        # room_id as player_id; skip subscription update in that case. A genuine failure inside
        # update_player_room_subscription itself now propagates to this function's own outer
        # except below, instead of being misread as "player_id just wasn't a UUID".
        if _looks_like_player_uuid(player_id):
            await update_player_room_subscription(connection_manager, player_id, room_id)

        logger.debug("Broadcasting room update to room", room_id=room_id)
        await connection_manager.broadcast_to_room(room_id, update_event)
        logger.debug("Room update broadcast completed for room", room_id=room_id)

        event_room_id = getattr(room, "id", None) or room_id
        occ_event = build_event(
            "room_occupants",
            occ_payload,
            room_id=event_room_id,
        )
        await connection_manager.broadcast_to_room(room_id, occ_event)
        logger.debug("Room occupants broadcast completed for room", room_id=room_id)

    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
        logger.error("Error broadcasting room update for room", room_id=room_id, error=str(e))
