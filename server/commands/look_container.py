"""
Container look functionality for MythosMUD.

This module handles looking at containers, including finding containers in rooms
or equipped items, formatting container displays, and handling container look requests.
"""

from typing import Any
from uuid import UUID

from ..structured_logging.enhanced_logging_config import get_logger
from .look_helpers import _get_wearable_container_service

logger = get_logger(__name__)


def _find_container_in_room(
    containers: list[dict[str, Any]], target: str, instance_number: int | None = None
) -> dict[str, Any] | None:
    """
    Find a container in room containers by name or container_id.

    Args:
        containers: List of container dictionaries
        target: Container name or container_id to search for
        instance_number: Optional instance number for targeting specific containers

    Returns:
        Matching container dictionary or None if not found
    """
    target_lower = target.lower()
    matching_containers = []

    for container in containers:
        # Try to get name from metadata or use container_id as fallback
        container_name = str(container.get("metadata", {}).get("name", container.get("container_id", ""))).lower()
        container_id = str(container.get("container_id", "")).lower()

        if target_lower in container_name or target_lower in container_id:
            matching_containers.append(container)

    if not matching_containers:
        return None

    if instance_number is not None:
        if instance_number < 1 or instance_number > len(matching_containers):
            return None
        return matching_containers[instance_number - 1]

    if len(matching_containers) == 1:
        return matching_containers[0]

    # Multiple matches - return None to indicate ambiguity
    return None


def _find_container_wearable(
    equipped: dict[str, dict[str, Any]], target: str, instance_number: int | None = None
) -> tuple[str, dict[str, Any]] | None:
    """
    Find a wearable container in equipped items by name or prototype_id.

    This function finds items that are containers, either by checking for inner_container
    or by matching item names that suggest they are containers (e.g., "backpack", "bag").

    Args:
        equipped: Dictionary of equipped items (slot -> item dict)
        target: Container name or prototype_id to search for
        instance_number: Optional instance number for targeting specific containers

    Returns:
        Tuple of (slot, item_dict) or None if not found
    """
    target_lower = target.lower()
    matching_containers = []

    for slot, item in equipped.items():
        item_name = str(item.get("item_name", item.get("name", ""))).lower()
        prototype_id = str(item.get("prototype_id", item.get("item_id", ""))).lower()
        item_id = str(item.get("item_id", "")).lower()

        # Check if this item matches the target name
        name_matches = target_lower in item_name or target_lower in prototype_id or target_lower in item_id

        # Include items that:
        # 1. Have inner_container (explicit container)
        # 2. Match the target name (might be a container we need to look up)
        if item.get("inner_container") or name_matches:
            if name_matches:
                matching_containers.append((slot, item))

    if not matching_containers:
        return None

    if instance_number is not None:
        if instance_number < 1 or instance_number > len(matching_containers):
            return None
        return matching_containers[instance_number - 1]

    if len(matching_containers) == 1:
        return matching_containers[0]

    # Multiple matches - return None to indicate ambiguity
    return None


async def _find_container_via_inner_container(item: dict[str, Any], persistence: Any) -> dict[str, Any] | None:
    """Find container via inner_container_id from item."""
    inner_container_id = item.get("inner_container")
    if not inner_container_id:
        return None

    try:
        container_id = UUID(inner_container_id) if isinstance(inner_container_id, str) else inner_container_id
        container_data = (
            await persistence.get_container(container_id) if hasattr(persistence, "get_container") else None
        )
        return container_data
    except (ValueError, TypeError):
        return None


def _matches_item_instance_id(item_instance_id: Any, container_item_instance_id: Any) -> bool:
    """Check if item instance IDs match."""
    return item_instance_id and container_item_instance_id and str(item_instance_id) == str(container_item_instance_id)


def _matches_name_or_slot(container_slot: str, container_item_name: str, slot_lower: str, target_lower: str) -> bool:
    """Check if container matches by name or slot."""
    return container_slot == slot_lower or target_lower in container_item_name or target_lower in container_slot


async def _get_container_data_from_component(container_component: Any, persistence: Any) -> dict[str, Any] | None:
    """Get container data from component ID."""
    container_id_from_component = container_component.container_id
    if not container_id_from_component:
        return None

    container_data = (
        await persistence.get_container(container_id_from_component) if hasattr(persistence, "get_container") else None
    )
    return container_data


def _extract_container_metadata(container_component: Any) -> dict[str, Any]:
    """Extract metadata from container component."""
    container_metadata = container_component.metadata if hasattr(container_component, "metadata") else {}
    return {
        "item_name": str(container_metadata.get("item_name", "")).lower(),
        "slot": str(container_metadata.get("slot", "")).lower(),
        "item_instance_id": container_metadata.get("item_instance_id"),
    }


async def _try_match_container_component(
    container_component: Any,
    item_instance_id: Any,
    slot_lower: str,
    target_lower: str,
    persistence: Any,
    slot: str,
    player_name: str,
) -> dict[str, Any] | None:
    """Try to match a container component and return container data if found."""
    metadata = _extract_container_metadata(container_component)

    # Try item_instance_id match first
    if _matches_item_instance_id(item_instance_id, metadata["item_instance_id"]):
        container_data = await _get_container_data_from_component(container_component, persistence)
        if container_data:
            logger.debug(
                "Found container via wearable container service (item_instance_id match) for look command",
                container_id=str(container_component.container_id),
                slot=slot,
                item_instance_id=item_instance_id,
                player=player_name,
            )
            return container_data

    # Try name/slot match
    if _matches_name_or_slot(metadata["slot"], metadata["item_name"], slot_lower, target_lower):
        container_data = await _get_container_data_from_component(container_component, persistence)
        if container_data:
            logger.debug(
                "Found container via wearable container service (name match) for look command",
                container_id=str(container_component.container_id),
                slot=slot,
                player=player_name,
            )
            return container_data

    return None


async def _find_container_via_wearable_service(
    slot: str,
    item: dict[str, Any],
    target_lower: str,
    player: Any,
    persistence: Any,
    request: Any,
    player_name: str,
) -> dict[str, Any] | None:
    """Find container via wearable container service."""
    try:
        wearable_container_service = _get_wearable_container_service(request)
        player_id_uuid = UUID(str(player.player_id))
        wearable_containers = await wearable_container_service.get_wearable_containers_for_player(player_id_uuid)

        slot_lower = slot.lower() if slot else ""
        item_instance_id = item.get("item_instance_id")

        for container_component in wearable_containers:
            container_data = await _try_match_container_component(
                container_component, item_instance_id, slot_lower, target_lower, persistence, slot, player_name
            )
            if container_data:
                return container_data
    except (AttributeError, TypeError, ValueError) as e:
        logger.debug(
            "Error finding container via wearable container service for look command",
            error=str(e),
            slot=slot,
            player=player_name,
        )

    return None


async def _find_container_in_room_or_equipped(
    target_lower: str,
    instance_number: int | None,
    room: Any,
    player: Any,
    persistence: Any,
    request: Any,
    player_name: str,
) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    """
    Find container in room or equipped items.

    Returns:
        tuple: (container_found, container_item) - container_item is the equipped item if found
    """
    room_containers = room.get_containers() if hasattr(room, "get_containers") else []
    container_found = _find_container_in_room(room_containers, target_lower, instance_number)
    container_item = None

    if container_found:
        return (container_found, container_item)

    # Try equipped items
    equipped = player.get_equipped_items() if hasattr(player, "get_equipped_items") else {}
    wearable_result = _find_container_wearable(equipped, target_lower, instance_number)
    if not wearable_result:
        return (None, None)

    slot, item = wearable_result
    container_item = item

    # Try inner_container_id first
    container_found = await _find_container_via_inner_container(item, persistence)
    if container_found:
        return (container_found, container_item)

    # Try wearable container service
    container_found = await _find_container_via_wearable_service(
        slot, item, target_lower, player, persistence, request, player_name
    )
    return (container_found, container_item)


def _get_container_description(
    container_found: dict[str, Any], container_item: dict[str, Any] | None, prototype_registry: Any
) -> str | None:
    """Get container description from prototype registry."""
    if container_item:
        prototype_id = container_item.get("prototype_id") or container_item.get("item_id")
    else:
        prototype_id = container_found.get("metadata", {}).get("prototype_id") or container_found.get("prototype_id")

    if not prototype_registry or not prototype_id:
        return None

    try:
        prototype = prototype_registry.get(prototype_id)
        if prototype and hasattr(prototype, "long_description"):
            return prototype.long_description
    except (AttributeError, TypeError, KeyError):
        logger.debug("Failed to get prototype for container", prototype_id=prototype_id)

    return None


def _format_container_contents(items: list[dict[str, Any]]) -> list[str]:
    """Format container contents as list of lines."""
    lines = []
    if items:
        for idx, item_stack in enumerate(items, start=1):
            item_name = item_stack.get("item_name", item_stack.get("name", "Unknown Item"))
            quantity = item_stack.get("quantity", 1)
            if quantity > 1:
                lines.append(f"  {idx}. {item_name} x{quantity}")
            else:
                lines.append(f"  {idx}. {item_name}")
    else:
        lines.append("  (empty)")
    return lines


def _format_container_display(
    container_found: dict[str, Any],
    container_description: str | None,
    command_data: dict,
) -> str:
    """Format the complete container display text."""
    container_name = container_found.get("metadata", {}).get(
        "name", f"Container {str(container_found.get('container_id', 'Unknown'))[:8]}"
    )
    items = container_found.get("items", [])
    capacity_slots = container_found.get("capacity_slots", 0)
    lock_state = container_found.get("lock_state", "unlocked")

    lines = [container_name]

    if container_description:
        lines.append(container_description)

    if lock_state == "locked":
        lines.append("Locked")
    elif lock_state == "sealed":
        lines.append("Sealed")

    used_slots = len(items)
    lines.append(f"Capacity: {used_slots}/{capacity_slots} slots")

    if command_data.get("look_in", False) or command_data.get("target_type") == "container":
        lines.append("Contents:")
        lines.extend(_format_container_contents(items))

    return "\n".join(lines)


async def _handle_container_look(
    target: str,
    target_lower: str,
    instance_number: int | None,
    room: Any,
    player: Any,
    persistence: Any,
    prototype_registry: Any,
    command_data: dict,
    request: Any,
    player_name: str,
) -> dict[str, Any] | None:
    """Handle looking at a specific container."""
    logger.debug(
        "Looking at container",
        player=player_name,
        target=target,
        look_in=command_data.get("look_in", False),
    )

    container_found, container_item = await _find_container_in_room_or_equipped(
        target_lower, instance_number, room, player, persistence, request, player_name
    )

    if not container_found:
        logger.debug("Container not found", player=player_name, target=target)
        return {"result": f"You don't see any '{target}' here."}

    container_description = _get_container_description(container_found, container_item, prototype_registry)
    result_text = _format_container_display(container_found, container_description, command_data)

    container_name = container_found.get("metadata", {}).get(
        "name", f"Container {str(container_found.get('container_id', 'Unknown'))[:8]}"
    )
    logger.debug("Container look completed", player=player_name, target=target, container_name=container_name)
    return {"result": result_text}


async def _try_lookup_container_implicit(
    target: str,
    target_lower: str,
    instance_number: int | None,
    room: Any,
    player: Any,
    persistence: Any,
    player_name: str,
) -> dict[str, Any] | None:
    """Try to find and display a container in implicit lookup."""
    room_containers = room.get_containers() if hasattr(room, "get_containers") else []
    container_found = _find_container_in_room(room_containers, target_lower, instance_number)

    if not container_found:
        equipped = player.get_equipped_items() if hasattr(player, "get_equipped_items") else {}
        wearable_result = _find_container_wearable(equipped, target_lower, instance_number)
        if wearable_result:
            _slot, item = wearable_result
            inner_container_id = item.get("inner_container")
            if inner_container_id:
                container_data = (
                    await persistence.get_container(inner_container_id)
                    if hasattr(persistence, "get_container")
                    else None
                )
                if container_data:
                    container_found = container_data

    if not container_found:
        return None

    container_name = container_found.get("metadata", {}).get(
        "name", f"Container {str(container_found.get('container_id', 'Unknown'))[:8]}"
    )
    items = container_found.get("items", [])
    capacity_slots = container_found.get("capacity_slots", 0)
    lock_state = container_found.get("lock_state", "unlocked")

    lines = [container_name]
    if lock_state == "locked":
        lines.append("Locked")
    elif lock_state == "sealed":
        lines.append("Sealed")
    lines.append(f"Capacity: {len(items)}/{capacity_slots} slots")

    result_text = "\n".join(lines)
    logger.debug("Container look completed", player=player_name, target=target, container_name=container_name)
    return {"result": result_text}


__all__ = [
    "_find_container_in_room",
    "_find_container_wearable",
    "_find_container_via_inner_container",
    "_find_container_in_room_or_equipped",
    "_get_container_description",
    "_format_container_contents",
    "_format_container_display",
    "_handle_container_look",
    "_try_lookup_container_implicit",
]
