"""
Room utility functions for MythosMUD.

This module provides utility functions for room-related operations,
including sub-zone extraction for the Advanced Chat Channels feature.
"""


def extract_subzone_from_room_id(room_id: str) -> str | None:
    """
    Extract sub-zone from room ID.

    Room ID format: {plane}_{zone}_{sub_zone}_{room_name}
    Example: earth_arkhamcity_northside_intersection_derby_high

    Args:
        room_id: The room ID to extract sub-zone from

    Returns:
        The sub-zone name, or None if the room ID format is invalid

    Examples:
        >>> extract_subzone_from_room_id("earth_arkhamcity_northside_intersection_derby_high")
        'northside'
        >>> extract_subzone_from_room_id("earth_arkhamcity_downtown_market_square")
        'downtown'
        >>> extract_subzone_from_room_id("invalid_room_id")
        None
    """
    if not room_id:
        return None

    parts = room_id.split("_")
    if len(parts) < 4:
        return None

    # The sub-zone is the third part (index 2) for arkhamcity format
    # Format: earth_arkhamcity_northside_intersection_derby_high
    # Parts: [0]earth [1]arkhamcity [2]northside [3]intersection [4]derby [5]high
    return parts[2]


def get_zone_from_room_id(room_id: str) -> str | None:
    """
    Extract zone from room ID.

    Room ID format: {plane}_{zone}_{sub_zone}_{room_name}
    Example: earth_arkhamcity_northside_intersection_derby_high

    Args:
        room_id: The room ID to extract zone from

    Returns:
        The zone name, or None if the room ID format is invalid

    Examples:
        >>> get_zone_from_room_id("earth_arkhamcity_northside_intersection_derby_high")
        'arkhamcity'
        >>> get_zone_from_room_id("earth_innsmouth_docks_warehouse_1")
        'innsmouth'
    """
    if not room_id:
        return None

    parts = room_id.split("_")
    if len(parts) < 4:
        return None

    # The zone is the second part (index 1) for arkhamcity format
    # Format: earth_arkhamcity_northside_intersection_derby_high
    # Parts: [0]earth [1]arkhamcity [2]northside [3]intersection [4]derby [5]high
    return parts[1]


def get_plane_from_room_id(room_id: str) -> str | None:
    """
    Extract plane from room ID.

    Room ID format: {plane}_{zone}_{sub_zone}_{room_name}
    Example: earth_arkhamcity_northside_intersection_derby_high

    Args:
        room_id: The room ID to extract plane from

    Returns:
        The plane name, or None if the room ID format is invalid

    Examples:
        >>> get_plane_from_room_id("earth_arkhamcity_northside_intersection_derby_high")
        'earth'
        >>> get_plane_from_room_id("dream_innsmouth_docks_warehouse_1")
        'dream'
    """
    if not room_id:
        return None

    parts = room_id.split("_")
    if len(parts) < 4:
        return None

    # The plane is the first part (index 0)
    return parts[0]


def is_valid_room_id_format(room_id: str) -> bool:
    """
    Check if a room ID follows the expected format.

    Args:
        room_id: The room ID to validate

    Returns:
        True if the room ID format is valid, False otherwise

    Examples:
        >>> is_valid_room_id_format("earth_arkhamcity_northside_intersection_derby_high")
        True
        >>> is_valid_room_id_format("invalid_room_id")
        False
        >>> is_valid_room_id_format("")
        False
    """
    if not room_id:
        return False

    parts = room_id.split("_")
    return len(parts) >= 4


def get_local_channel_subject(room_id: str) -> str | None:
    """
    Generate NATS subject for local channel messages.

    Args:
        room_id: The room ID to generate subject for

    Returns:
        The NATS subject for local channel messages, or None if room ID is invalid

    Examples:
        >>> get_local_channel_subject("earth_arkhamcity_northside_intersection_derby_high")
        'chat.local.earth_arkhamcity_northside_intersection_derby_high'
    """
    if not is_valid_room_id_format(room_id):
        return None

    return f"chat.local.{room_id}"


def get_subzone_local_channel_subject(room_id: str) -> str | None:
    """
    Generate NATS subject for sub-zone local channel messages.

    This creates a subject that would be used for broadcasting to all rooms
    in the same sub-zone, rather than just the specific room.

    Args:
        room_id: The room ID to generate subject for

    Returns:
        The NATS subject for sub-zone local channel messages, or None if room ID is invalid

    Examples:
        >>> get_subzone_local_channel_subject("earth_arkhamcity_northside_intersection_derby_high")
        'chat.local.subzone.northside'
    """
    subzone = extract_subzone_from_room_id(room_id)
    if not subzone:
        return None

    return f"chat.local.subzone.{subzone}"
