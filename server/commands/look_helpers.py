"""
Helper functions for look command.

This module contains utility functions used by the look command system,
including parsing, formatting, and label generation.
"""

import re
from typing import Any

from ..services.wearable_container_service import WearableContainerService
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def _get_wearable_container_service(request: Any) -> WearableContainerService:
    """
    Get shared WearableContainerService instance, initializing it lazily if needed.

    This ensures the service is initialized with proper dependencies from the application container.

    Args:
        request: FastAPI request object to access app state

    Returns:
        WearableContainerService instance
    """
    # Use function attribute instead of global variable to avoid global statement
    if (
        not hasattr(_get_wearable_container_service, "cached_instance")
        or _get_wearable_container_service.cached_instance is None
    ):
        # Get async_persistence from container
        app = getattr(request, "app", None)
        container = getattr(app.state, "container", None) if app else None
        async_persistence = getattr(container, "async_persistence", None) if container else None

        if async_persistence is None:
            raise ValueError("async_persistence is required but not available from container")

        _get_wearable_container_service.cached_instance = WearableContainerService(persistence=async_persistence)  # type: ignore[attr-defined]

    return _get_wearable_container_service.cached_instance  # type: ignore[attr-defined]


def _parse_instance_number(target: str) -> tuple[str, int | None]:
    """
    Parse instance number from target string.

    Supports two formats:
    - "backpack-2" (hyphen syntax)
    - "backpack 2" (space syntax)

    Args:
        target: Target string that may contain instance number

    Returns:
        Tuple of (target_name, instance_number) where instance_number is None if not found
    """
    # Try hyphen syntax first: "backpack-2"
    hyphen_match = re.match(r"^(.+)-(\d+)$", target)
    if hyphen_match:
        target_name = hyphen_match.group(1)
        instance_number = int(hyphen_match.group(2))
        return (target_name, instance_number)

    # Try space syntax: "backpack 2"
    space_match = re.match(r"^(.+)\s+(\d+)$", target)
    if space_match:
        target_name = space_match.group(1).rstrip()
        instance_number = int(space_match.group(2))
        return (target_name, instance_number)

    # No instance number found
    return (target, None)


def _get_health_label(stats: dict) -> str:
    """
    Get descriptive health label based on health percentage.

    Args:
        stats: Dictionary containing 'current_dp' and 'max_dp' keys

    Returns:
        Descriptive health label: "healthy", "wounded", "critical", or "mortally wounded"
    """
    health = stats.get("current_dp", 0)
    # Calculate max DP from CON + SIZ if available, otherwise use default
    constitution = stats.get("constitution", 50)
    size = stats.get("size", 50)
    max_dp = stats.get("max_dp", (constitution + size) // 5)  # DP max = (CON + SIZ) / 5
    if not max_dp:
        max_dp = 100  # Prevent division by zero
    if not max_dp:
        return "mortally wounded"

    health_percent = (health / max_dp) * 100

    if health_percent > 75:
        return "healthy"
    if health_percent >= 25:
        return "wounded"
    if health_percent > 0:
        return "critical"
    return "mortally wounded"


def _get_lucidity_label(stats: dict) -> str:
    """
    Get descriptive lucidity label based on lucidity percentage.

    Args:
        stats: Dictionary containing 'lucidity' and 'max_lucidity' keys

    Returns:
        Descriptive lucidity label: "lucid", "disturbed", "unstable", or "mad"
    """
    lucidity = stats.get("lucidity", 0)
    max_lucidity = stats.get("max_lucidity", 100)
    if not max_lucidity:
        return "mad"

    lucidity_percent = (lucidity / max_lucidity) * 100

    if lucidity_percent > 75:
        return "lucid"
    if lucidity_percent >= 25:
        return "disturbed"
    if lucidity_percent > 0:
        return "unstable"
    return "mad"


def _get_visible_equipment(player: Any) -> dict[str, dict]:
    """
    Get visible equipment from player, excluding internal/hidden slots.

    Visible slots: head, torso, legs, hands, feet, main_hand, off_hand
    Hidden slots: ring, amulet, belt, backpack

    Args:
        player: Player object with get_equipped_items() method

    Returns:
        Dictionary of visible equipment slots and their items
    """
    visible_slots = {"head", "torso", "legs", "hands", "feet", "main_hand", "off_hand"}
    all_equipped = player.get_equipped_items() if hasattr(player, "get_equipped_items") else {}
    return {slot: item for slot, item in all_equipped.items() if slot in visible_slots}


def _is_direction(target_lower: str) -> bool:
    """Check if target is a direction."""
    return target_lower in ["north", "south", "east", "west", "up", "down", "n", "s", "e", "w", "u", "d"]


__all__ = [
    "_get_wearable_container_service",
    "_parse_instance_number",
    "_get_health_label",
    "_get_lucidity_label",
    "_get_visible_equipment",
    "_is_direction",
]
