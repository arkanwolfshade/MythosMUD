"""
NPC Utility Functions.

This module provides utility functions for extracting metadata from NPC instances.
"""

from typing import Any


def extract_room_id_from_npc(npc_instance: Any) -> str:
    """
    Extract room ID from NPC instance with fallback logic.

    Args:
        npc_instance: The NPC instance to extract room ID from

    Returns:
        Room ID as string, or "unknown" if not found
    """
    room_id_value = getattr(npc_instance, "current_room", None)
    if room_id_value is None:
        room_id_value = getattr(npc_instance, "current_room_id", None)
    if room_id_value is None:
        room_id_value = getattr(npc_instance, "room_id", None)

    if isinstance(room_id_value, str):
        return room_id_value
    return "unknown"


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


def get_zone_key_from_room_id(room_id: str) -> str:
    """
    Extract zone key from room ID.

    Args:
        room_id: The room identifier

    Returns:
        Zone key in format "zone/sub_zone"
    """
    # Room IDs are in format: "plane_zone_sub_zone_[room_description]_number" or "plane_zone_sub_zone_[room_description]"
    # Examples: "earth_arkhamcity_downtown_001" -> "arkhamcity/downtown"
    #           "earth_arkhamcity_sanitarium_room_foyer_entrance_001" -> "arkhamcity/sanitarium"
    #           "earth_arkhamcity_downtown_intersection_derby_garrison" -> "arkhamcity/downtown"
    #           "earth_innsmouth_waterfront_dock_002" -> "innsmouth/waterfront"
    parts = room_id.split("_")
    if len(parts) >= 4:
        # We need exactly the zone (parts[1]) and sub_zone (parts[2])
        # Everything after parts[2] is room description (with or without numeric suffix)
        zone = parts[1]  # arkhamcity, innsmouth, katmandu
        sub_zone = parts[2]  # sanitarium, downtown, waterfront, etc.
        return f"{zone}/{sub_zone}"

    return "unknown/unknown"
