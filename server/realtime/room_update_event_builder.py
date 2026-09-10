"""
Room-update event construction, shared by the broadcast and per-viewer fan-out paths (#714).

Split out of `websocket_room_updates.py` so both that module and `room_viewer_fanout.py` can
depend on this leaf module without importing each other (a two-way import between them would be
a cycle).
"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypedDict, cast

from ..services.exit_hallucination import get_hallucinated_exits
from ..services.lucidity_tier_cache import lucidity_tier_cache
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.room_renderer import build_room_drop_summary, clone_room_drops
from .envelope import build_event
from .websocket_helpers import convert_uuids_to_strings

if TYPE_CHECKING:
    from ..models.room import Room
    from .connection_manager import ConnectionManager

logger = get_logger(__name__)


class RoomOccupancyPayload(TypedDict):
    """Shape of a `room_occupants` payload's data -- shared with the per-viewer fan-out (#714)."""

    occupants: list[str]
    count: int
    players: list[str]
    npcs: list[str]


async def build_room_update_event(
    room: Room,
    room_id: str,
    player_id: str,
    occupant_names: list[str],
    connection_manager: ConnectionManager,
    players: list[str] | None = None,
    npcs: list[str] | None = None,
    viewer_id: str | None = None,
) -> dict[str, object]:
    """
    Build room update event with room data and occupants (players/npcs for structured client UI).

    `viewer_id` is the actual recipient (distinct from `player_id`, the triggering mover) --
    when given and cached as deranged (#626, #714), this viewer's exits are replaced with their
    seeded hallucinated set. Omitted (None) on the non-personalized fast path, where by
    construction nobody in the room is hallucination-eligible.
    """
    # Room.to_dict() is pre-existing `dict[str, Any]` on the Room model itself; narrowing that
    # return type is outside this module's scope, so room_data is accepted as-is from here.
    room_data = room.to_dict()
    room_data = await connection_manager.convert_room_players_uuids_to_names(room_data)
    # convert_uuids_to_strings is a generic object -> object recursive walk; it preserves the
    # dict shape at runtime but can't say so statically, so narrow it back explicitly.
    room_data = cast(dict[str, object], convert_uuids_to_strings(room_data))
    if viewer_id is not None and lucidity_tier_cache.is_deranged(viewer_id):
        room_data["exits"] = dict.fromkeys(get_hallucinated_exits(room_id, viewer_id), "?")

    room_drops: list[dict[str, object]] = []
    try:
        room_drops = clone_room_drops(connection_manager.room_manager.list_room_drops(room_id))
    except (AttributeError, KeyError, TypeError, ValueError) as exc:
        logger.debug("Failed to collect room drops for broadcast", room_id=room_id, error=str(exc))

    drop_summary = build_room_drop_summary(room_drops)

    payload: dict[str, object] = {
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

    # room.id is untyped on the Room model (pre-existing); narrow it at this boundary rather
    # than letting Any leak into this module.
    event_room_id = cast(str, room.id) or room_id
    return build_event(
        "room_update",
        payload,
        player_id=player_id,
        room_id=event_room_id,
    )


__all__ = ["RoomOccupancyPayload", "build_room_update_event"]
