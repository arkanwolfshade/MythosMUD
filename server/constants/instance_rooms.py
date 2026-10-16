"""
Shared identifiers for instanced rooms.

Kept import-free so persistence, NPC, movement and realtime code can all use it without import cycles.
"""

# Instance room ids: instance_{instance_uuid}_{template_stable_id}
INSTANCE_ROOM_PREFIX: str = "instance_"

# players.tutorial_instance_id of a player whose tutorial instance has not been built yet (a new
# character, before first connect). It names no live instance, so the reconnect path creates one.
PENDING_INSTANCE_ID: str = "pending"


def is_instance_room_id(room_id: str) -> bool:
    """True for per-player instance rooms (instance_<uuid>_<stable_id>), false for world and template ids."""
    return room_id.startswith(INSTANCE_ROOM_PREFIX) and room_id.count("_") >= 2
