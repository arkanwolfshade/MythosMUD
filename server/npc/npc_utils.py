"""
NPC Utility Functions.

This module provides utility functions for extracting metadata from NPC instances.
"""

from typing import Any, cast


def extract_room_id_from_npc(npc_instance: Any) -> str:
    """
    Extract room ID from NPC instance with fallback logic.

    Args:
        npc_instance: The NPC instance to extract room ID from

    Returns:
        Room ID as string, or "unknown" if not found
    """
    for attr in ("current_room", "current_room_id", "spawn_room_id", "room_id"):
        room_id_value = getattr(npc_instance, attr, None)
        if isinstance(room_id_value, str) and room_id_value and room_id_value != "unknown":
            return room_id_value
    return "unknown"


def _room_id_from_lifecycle_event(event: Any) -> str | None:
    """Return usable room_id from a single lifecycle event, if present."""
    if not isinstance(event, dict):
        return None
    details = event.get("details")
    if not isinstance(details, dict):
        return None
    room_id = details.get("room_id")
    if not isinstance(room_id, str) or not room_id or room_id == "unknown":
        return None
    return room_id


def extract_room_id_from_lifecycle_record(record: Any | None) -> str | None:
    """Return the latest non-unknown room_id from a lifecycle record's events, if any."""
    if record is None:
        return None
    for event in reversed(getattr(record, "events", None) or []):
        room_id = _room_id_from_lifecycle_event(event)
        if room_id is not None:
            return room_id
    return None


def extract_npc_metadata(npc_instance: Any) -> tuple[str, bool]:
    """
    Extract NPC type and required status from NPC instance.

    Args:
        npc_instance: The NPC instance to extract metadata from

    Returns:
        Tuple of (npc_type, is_required)
    """
    npc_type_value = getattr(npc_instance, "npc_type", None)
    npc_type = npc_type_value if isinstance(npc_type_value, str) else "unknown"

    is_required_value = getattr(npc_instance, "is_required", None)
    is_required = bool(is_required_value) if is_required_value is not None else False

    return (npc_type, is_required)


def extract_definition_id_from_npc(npc_instance: Any, npc_id: str, lifecycle_manager: Any | None) -> int | None:
    """
    Extract definition ID from NPC instance or lifecycle record.

    Args:
        npc_instance: The NPC instance to extract definition ID from
        npc_id: The NPC ID for looking up lifecycle records
        lifecycle_manager: The lifecycle manager to query for records

    Returns:
        Definition ID as integer, or None if not found
    """
    if hasattr(npc_instance, "definition_id"):
        definition_id_value = npc_instance.definition_id
        if isinstance(definition_id_value, int):
            return definition_id_value

    if not lifecycle_manager:
        return None

    lifecycle_records = getattr(lifecycle_manager, "lifecycle_records", {})
    if npc_id not in lifecycle_records:
        return None

    record = lifecycle_records[npc_id]
    if hasattr(record, "definition") and hasattr(record.definition, "id"):
        return int(record.definition.id)

    return None


def _stable_room_id_for_zone(room_id: str) -> str:
    """Return stable room id for zone parsing; strip instance_<uuid>_ prefix if present."""
    if room_id.startswith("instance_") and room_id.count("_") >= 2:
        parts = room_id.split("_", 2)
        if len(parts) > 2:
            return parts[2]
    return room_id


def spawn_npc_via_population_controller(
    manager: Any, definition: Any, room_id: str, reason: str
) -> tuple[str | None, str | None]:
    """
    Spawn an NPC through `population_controller.spawn_npc` when one is configured (#768).

    `NPCPopulationController._spawn_npc` delegates to `NPCLifecycleManager.spawn_npc` and then
    registers the new NPC in `population_stats` -- the only place that happens. Calling
    `manager.spawn_npc` directly (as the periodic optional-spawn check and respawn queue
    processing both used to) skips that registration, so `current_count` in the population-cap
    check always reads 0 and the cap never engages: optional NPCs spawn without limit. Falls
    back to `manager.spawn_npc` when no population controller is configured (e.g. minimal test
    setups), matching prior behavior there.

    Args:
        manager: NPCLifecycleManager instance (avoids circular import).
        definition: NPC definition to spawn.
        room_id: Room to spawn the NPC in.
        reason: Spawn reason, passed through to whichever spawn call is used.

    Returns:
        Tuple of (npc_id, failure_reason), as returned by the underlying spawn call.
    """
    population_controller = getattr(manager, "population_controller", None)
    if population_controller is not None:
        return cast(tuple[str | None, str | None], population_controller.spawn_npc(definition, room_id, reason))
    return cast(tuple[str | None, str | None], manager.spawn_npc(definition, room_id, reason))


def get_zone_key_from_room_id(room_id: str) -> str:
    """
    Extract zone key from room ID.

    Args:
        room_id: The room identifier (stable id or instance_<uuid>_<stable_id>)

    Returns:
        Zone key in format "zone/sub_zone"
    """
    # Instanced rooms: instance_<uuid>_<stable_id> -> use stable_id for zone lookup
    stable_id = _stable_room_id_for_zone(room_id)
    # Stable IDs: "plane_zone_sub_zone_[room_description]_number"
    # Examples: "earth_arkhamcity_downtown_001" -> "arkhamcity/downtown"
    #           "earth_arkhamcity_sanitarium_room_foyer_entrance_001" -> "arkhamcity/sanitarium"
    #           "earth_innsmouth_waterfront_dock_002" -> "innsmouth/waterfront"
    parts = stable_id.split("_")
    if len(parts) >= 4:
        # zone = parts[1], sub_zone = parts[2]; rest is room description
        zone = parts[1]  # arkhamcity, innsmouth, katmandu
        sub_zone = parts[2]  # sanitarium, downtown, waterfront, etc.
        return f"{zone}/{sub_zone}"

    return "unknown/unknown"
