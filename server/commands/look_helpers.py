"""
Helper functions for look command.

This module contains utility functions used by the look command system,
including parsing, formatting, and label generation.
"""

import re
from collections.abc import Mapping
from typing import Protocol, cast

from ..services.wearable_container_service import WearableContainerService
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class _WearableContainerServiceHolder:  # pylint: disable=too-few-public-methods  # Reason: mutable cache holder, not a behavior class
    """Mutable holder so we can cache the service without a ``global`` statement."""

    instance: WearableContainerService | None = None


_WEARABLE_CONTAINER_SERVICE_HOLDER = _WearableContainerServiceHolder()


class LookRequest(Protocol):  # pylint: disable=too-few-public-methods  # Reason: PEP 544 Protocol is a structural type, not a concrete class
    """Request-like surface the look commands need.

    HTTP requests arrive as fastapi.Request; in-game commands arrive over WebSocket as
    WebSocketRequestContext. Only `.app` is ever read, so accept either structurally.
    Narrowing this to a concrete Request silently disables look for every WebSocket
    command, since the WebSocket context is duck-typed and fails isinstance.
    """

    @property
    def app(self) -> object:
        """FastAPI/Starlette application (or duck-typed equivalent)."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: Protocol stub body required by basedpyright


class _ContainerWithPersistence(Protocol):  # pylint: disable=too-few-public-methods  # Reason: PEP 544 Protocol stub
    async_persistence: object | None


class _StateWithContainer(Protocol):  # pylint: disable=too-few-public-methods  # Reason: PEP 544 Protocol stub
    container: _ContainerWithPersistence | None


class _AppWithState(Protocol):  # pylint: disable=too-few-public-methods  # Reason: PEP 544 Protocol stub
    state: _StateWithContainer


class _EquippedPlayer(Protocol):  # pylint: disable=too-few-public-methods  # Reason: PEP 544 Protocol stub
    def get_equipped_items(self) -> Mapping[str, Mapping[str, object]]:
        """Return equipped slot -> item mappings."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: Protocol stub body required by basedpyright


def _async_persistence_from_app(app: object) -> object | None:
    if not hasattr(app, "state"):
        return None
    container = cast(_AppWithState, app).state.container
    if container is None:
        return None
    return container.async_persistence


def _get_wearable_container_service(request: LookRequest) -> WearableContainerService:
    """
    Get shared WearableContainerService instance, initializing it lazily if needed.

    This ensures the service is initialized with proper dependencies from the application container.

    Args:
        request: FastAPI request object to access app state

    Returns:
        WearableContainerService instance
    """
    if _WEARABLE_CONTAINER_SERVICE_HOLDER.instance is not None:
        return _WEARABLE_CONTAINER_SERVICE_HOLDER.instance

    async_persistence = _async_persistence_from_app(request.app)
    if async_persistence is None:
        raise ValueError("async_persistence is required but not available from container")

    _WEARABLE_CONTAINER_SERVICE_HOLDER.instance = WearableContainerService(persistence=async_persistence)
    return _WEARABLE_CONTAINER_SERVICE_HOLDER.instance


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


def _stat_number(stats: Mapping[str, object], key: str, default: float) -> float:
    raw = stats.get(key, default)
    if isinstance(raw, bool):
        return default
    if isinstance(raw, (int, float)):
        return float(raw)
    return default


def _get_health_label(stats: Mapping[str, object]) -> str:
    """
    Get descriptive health label based on health percentage.

    Args:
        stats: Dictionary containing 'current_dp' and 'max_dp' keys

    Returns:
        Descriptive health label: "healthy", "wounded", "critical", or "mortally wounded"
    """
    health = _stat_number(stats, "current_dp", 0.0)
    constitution = _stat_number(stats, "constitution", 50.0)
    size = _stat_number(stats, "size", 50.0)
    max_dp = _stat_number(stats, "max_dp", (constitution + size) // 5)
    if not max_dp:
        max_dp = 100.0  # Prevent division by zero
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


def _get_lucidity_label(stats: Mapping[str, object]) -> str:
    """
    Get descriptive lucidity label based on lucidity percentage.

    Args:
        stats: Dictionary containing 'lucidity' and 'max_lucidity' keys

    Returns:
        Descriptive lucidity label: "lucid", "disturbed", "unstable", or "mad"
    """
    lucidity = _stat_number(stats, "lucidity", 0.0)
    max_lucidity = _stat_number(stats, "max_lucidity", 100.0)
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


def _get_visible_equipment(player: _EquippedPlayer) -> dict[str, Mapping[str, object]]:
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
    all_equipped = player.get_equipped_items()
    return {slot: item for slot, item in all_equipped.items() if slot in visible_slots}


def _is_direction(target_lower: str) -> bool:
    """Check if target is a direction."""
    return target_lower in ["north", "south", "east", "west", "up", "down", "n", "s", "e", "w", "u", "d"]


__all__ = [
    "LookRequest",
    "_get_wearable_container_service",
    "_parse_instance_number",
    "_get_health_label",
    "_get_lucidity_label",
    "_get_visible_equipment",
    "_is_direction",
]
