"""
Shared per-viewer phantom hostile visibility (#625, #714).

Phantom hostiles are player-specific hallucinations: only the hallucinating player's own
`look`, room-occupants, and room-update payloads ever include them. This module is the single
place that answers "which phantom names should this exact viewer see in this exact room?" so
`look_room.py`, the realtime room-payload builders, and `game_state_provider.py` all agree.
"""

from __future__ import annotations

import uuid


def get_viewer_phantom_names(viewer_player_id: uuid.UUID | str | None, room_id: str | None) -> list[str]:
    """
    Return the viewer's own active phantom hostiles in this room, styled as NPC names.

    No other viewer, and no query without a viewer id, ever gets anything from this function.
    """
    if not viewer_player_id or not room_id:
        return []
    from .phantom_hostile_service import phantom_hostile_service

    names: list[str] = []
    for phantom_id in phantom_hostile_service.get_active_phantoms(viewer_player_id):
        data = phantom_hostile_service.get_phantom_data(phantom_id)
        if data and data["room_id"] == room_id:
            names.append(data["name"])
    return names


def room_has_hallucinating_viewer(player_ids: list[str]) -> bool:
    """
    Cheap, in-memory eligibility check: does any player in this room currently see a phantom?

    Used as the fast-path gate for per-viewer room-payload fan-out (#714) -- when this is False,
    a single `broadcast_to_room` is exactly as correct as, and much cheaper than, personalizing
    the payload for every connected player.
    """
    from .phantom_hostile_service import phantom_hostile_service

    return any(phantom_hostile_service.get_active_phantoms(player_id) for player_id in player_ids)


__all__ = ["get_viewer_phantom_names", "room_has_hallucinating_viewer"]
