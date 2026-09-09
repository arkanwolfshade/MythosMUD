"""
Shared per-viewer hallucination visibility (#625, #626, #714).

Phantom hostiles are player-specific hallucinations: only the hallucinating player's own
`look`, room-occupants, and room-update payloads ever include them. This module is the single
place that answers "which phantom names should this exact viewer see in this exact room?" so
`look_room.py`, the realtime room-payload builders, and `game_state_provider.py` all agree.

It also hosts the combined fast-path gate for per-viewer payload fan-out: a room needs
personalizing when someone in it has an active phantom (#625) *or* is deranged enough to see
hallucinated exits (#626) -- either reason forces the fan-out path in the same way.
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
    Cheap, in-memory eligibility check: does anyone in this room need a personalized payload?

    True if any player has an active phantom (#625) or is cached as deranged (#626) -- both are
    in-memory lookups (phantom_hostile_service, lucidity_tier_cache), not DB round trips. Used as
    the fast-path gate for per-viewer room-payload fan-out (#714): when this is False, a single
    `broadcast_to_room` is exactly as correct as, and much cheaper than, personalizing the
    payload for every connected player.
    """
    from .lucidity_tier_cache import lucidity_tier_cache
    from .phantom_hostile_service import phantom_hostile_service

    return any(
        phantom_hostile_service.get_active_phantoms(player_id) or lucidity_tier_cache.is_deranged(player_id)
        for player_id in player_ids
    )


__all__ = ["get_viewer_phantom_names", "room_has_hallucinating_viewer"]
