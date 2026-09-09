"""
Per-viewer room-payload fan-out (#714).

`room_update`/`room_occupants` are ordinarily a single `broadcast_to_room` call -- every player
in the room sees the same NPC roster. That stops being true the moment a phantom hostile (#625)
is active for someone in the room: only the hallucinating player may see it. This module is the
path `broadcast_room_update` takes when that's the case, personalizing the NPC roster (and thus
the occupant list built from it) per recipient instead of trusting one shared payload.

Callers should gate on `phantom_visibility.room_has_hallucinating_viewer` first and only reach
for this module when it returns True -- the common case (nobody hallucinating) stays exactly as
cheap as the single broadcast it replaces.
"""

from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, cast

from ..services.phantom_visibility import get_viewer_phantom_names
from ..structured_logging.enhanced_logging_config import get_logger
from .envelope import build_event
from .room_update_event_builder import RoomOccupancyPayload, build_room_update_event

if TYPE_CHECKING:
    from ..models.room import Room
    from .connection_manager import ConnectionManager
    from .message_builders import MessageBuilder

logger = get_logger(__name__)


async def send_personalized_room_events(
    connection_manager: ConnectionManager,
    room: Room,
    room_id: str,
    triggering_player_id: str,
    player_ids: list[str],
    player_occupant_names: list[str],
    npc_occupants: list[str],
    occ_payload_base: RoomOccupancyPayload,
) -> None:
    """
    Send `room_update` and `room_occupants` to each connected player individually.

    A recipient with no active phantom gets exactly what the single-broadcast fast path would
    have sent them -- only a hallucinating viewer's own payload differs, gaining their own
    phantom names in `npcs`/`occupants`.
    """
    for viewer_id in player_ids:
        try:
            viewer_uuid = uuid.UUID(viewer_id)
        except ValueError:
            logger.debug("Skipping personalized room event for non-UUID player id", player_id=viewer_id)
            continue

        viewer_npcs = [*npc_occupants, *get_viewer_phantom_names(viewer_id, room_id)]
        viewer_occupants = [*player_occupant_names, *viewer_npcs]

        update_event = await build_room_update_event(
            room,
            room_id,
            triggering_player_id,
            viewer_occupants,
            connection_manager,
            players=player_occupant_names,
            npcs=viewer_npcs,
            viewer_id=viewer_id,
        )
        occ_event = build_event(
            "room_occupants",
            {
                **occ_payload_base,
                "npcs": viewer_npcs,
                "occupants": viewer_occupants,
                "count": len(viewer_occupants),
            },
            # room.id is untyped on the Room model (pre-existing); narrow it at this boundary
            # rather than letting Any leak into this module.
            room_id=cast(str, room.id) or room_id,
        )
        _ = await connection_manager.send_personal_message(viewer_uuid, update_event)
        _ = await connection_manager.send_personal_message(viewer_uuid, occ_event)


async def send_personalized_occupants_update(
    connection_manager: ConnectionManager,
    message_builder: MessageBuilder,
    room_id: str,
    player_ids: list[str],
    players: list[str],
    npc_occupants: list[str],
    all_occupants: list[str],
    exclude_player: str | None = None,
) -> None:
    """
    Send a `room_occupants` update to each connected player individually.

    Used by `RealTimeEventHandler._send_room_occupants_update_internal` when the room contains a
    hallucinating viewer (#714) -- same reasoning as `send_personalized_room_events`, but for the
    plain `room_occupants` message shape (no accompanying `room_update`).
    """
    for viewer_id in player_ids:
        if viewer_id == exclude_player:
            continue
        try:
            viewer_uuid = uuid.UUID(viewer_id)
        except ValueError:
            logger.debug("Skipping personalized occupants event for non-UUID player id", player_id=viewer_id)
            continue

        phantom_names = get_viewer_phantom_names(viewer_id, room_id)
        viewer_npcs = [*npc_occupants, *phantom_names]
        viewer_all_occupants = [*all_occupants, *phantom_names]
        message = message_builder.build_occupants_update_message(room_id, players, viewer_npcs, viewer_all_occupants)
        _ = await connection_manager.send_personal_message(viewer_uuid, message)


__all__ = ["send_personalized_occupants_update", "send_personalized_room_events"]
