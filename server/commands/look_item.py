"""
Item look functionality for MythosMUD.

This module handles looking at items, including finding items in various locations
(room drops, inventory, equipped items) and formatting item descriptions.
"""

from typing import Any

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def _find_item_in_room_drops(
    room_drops: list[dict[str, Any]], target: str, instance_number: int | None = None
) -> dict[str, Any] | None:
    """
    Find an item in room drops by name or prototype_id.

    Args:
        room_drops: List of room drop dictionaries
        target: Item name or prototype_id to search for
        instance_number: Optional instance number for targeting specific items

    Returns:
        Matching item dictionary or None if not found
    """
    target_lower = target.lower()
    matching_items = []

    for drop in room_drops:
        item_name = str(drop.get("item_name", "")).lower()
        prototype_id = str(drop.get("prototype_id", "")).lower()
        item_id = str(drop.get("item_id", "")).lower()

        if target_lower in item_name or target_lower in prototype_id or target_lower in item_id:
            matching_items.append(drop)

    if not matching_items:
        return None

    if instance_number is not None:
        if instance_number < 1 or instance_number > len(matching_items):
            return None
        return matching_items[instance_number - 1]

    if len(matching_items) == 1:
        return matching_items[0]

    # Multiple matches - return None to indicate ambiguity
    return None


def _find_item_in_inventory(
    inventory: list[dict[str, Any]], target: str, instance_number: int | None = None
) -> dict[str, Any] | None:
    """
    Find an item in player inventory by name or prototype_id.

    Args:
        inventory: List of inventory item dictionaries
        target: Item name or prototype_id to search for
        instance_number: Optional instance number for targeting specific items

    Returns:
        Matching item dictionary or None if not found
    """
    target_lower = target.lower()
    matching_items = []

    for item in inventory:
        item_name = str(item.get("item_name", item.get("name", ""))).lower()
        prototype_id = str(item.get("prototype_id", item.get("item_id", ""))).lower()
        item_id = str(item.get("item_id", "")).lower()

        if target_lower in item_name or target_lower in prototype_id or target_lower in item_id:
            matching_items.append(item)

    if not matching_items:
        return None

    if instance_number is not None:
        if instance_number < 1 or instance_number > len(matching_items):
            return None
        return matching_items[instance_number - 1]

    if len(matching_items) == 1:
        return matching_items[0]

    # Multiple matches - return None to indicate ambiguity
    return None


def _find_item_in_equipped(
    equipped: dict[str, dict[str, Any]], target: str, instance_number: int | None = None
) -> tuple[str, dict[str, Any]] | None:
    """
    Find an item in equipped items by name or prototype_id.

    Args:
        equipped: Dictionary of equipped items (slot -> item dict)
        target: Item name or prototype_id to search for
        instance_number: Optional instance number for targeting specific items

    Returns:
        Tuple of (slot, item_dict) or None if not found
    """
    target_lower = target.lower()
    matching_items = []

    for slot, item in equipped.items():
        item_name = str(item.get("item_name", item.get("name", ""))).lower()
        prototype_id = str(item.get("prototype_id", item.get("item_id", ""))).lower()
        item_id = str(item.get("item_id", "")).lower()

        if target_lower in item_name or target_lower in prototype_id or target_lower in item_id:
            matching_items.append((slot, item))

    if not matching_items:
        return None

    if instance_number is not None:
        if instance_number < 1 or instance_number > len(matching_items):
            return None
        return matching_items[instance_number - 1]

    if len(matching_items) == 1:
        return matching_items[0]

    # Multiple matches - return None to indicate ambiguity
    return None


def _get_item_description_from_prototype(
    item_found: dict[str, Any], prototype_registry: Any, fallback_name: str | None = None
) -> str | None:
    """
    Get item description from prototype registry.

    Returns:
        Formatted result string if successful, None if prototype not found
    """
    prototype_id = item_found.get("prototype_id") or item_found.get("item_id")
    if not prototype_registry or not prototype_id:
        return None

    try:
        prototype = prototype_registry.get(prototype_id)
        item_name = item_found.get("item_name", item_found.get("name", prototype.name if prototype else fallback_name))
        if not item_name:
            item_name = fallback_name or "Unknown Item"
        description = prototype.long_description if prototype else "You see nothing remarkable about it."
        return f"{item_name}\n{description}"
    except (AttributeError, TypeError, KeyError):
        item_name = item_found.get("item_name", item_found.get("name", fallback_name or "Unknown Item"))
        return f"{item_name}\nYou see nothing remarkable about it."


def _check_item_in_location(
    item_found: dict[str, Any] | None, prototype_registry: Any, location_name: str | None = None
) -> dict[str, str] | None:
    """Check if item found in a location and return formatted result."""
    if not item_found:
        return None

    result_text = _get_item_description_from_prototype(item_found, prototype_registry)
    if result_text:
        if location_name:
            # Extract item name from result for equipped items
            lines = result_text.split("\n", 1)
            if len(lines) == 2:
                return {"result": f"{lines[0]} ({location_name})\n{lines[1]}"}
        return {"result": result_text}

    # Fallback if no prototype found
    item_name = item_found.get("item_name", item_found.get("name", "Unknown Item"))
    if location_name:
        return {"result": f"{item_name} ({location_name})\nYou see nothing remarkable about it."}
    return {"result": f"{item_name}\nYou see nothing remarkable about it."}


def _check_equipped_item(
    player: Any, target_lower: str, instance_number: int | None, prototype_registry: Any
) -> dict[str, str] | None:
    """Check if item is equipped and return formatted result."""
    equipped = player.get_equipped_items() if hasattr(player, "get_equipped_items") else {}
    equipped_result = _find_item_in_equipped(equipped, target_lower, instance_number)
    if not equipped_result:
        return None

    slot, item_found = equipped_result
    return _check_item_in_location(item_found, prototype_registry, f"equipped in {slot}")


async def _handle_item_look(
    target: str,
    target_lower: str,
    instance_number: int | None,
    room_drops: list[dict[str, Any]],
    player: Any,
    prototype_registry: Any,
    command_data: dict,
    player_name: str,
) -> dict[str, Any] | None:
    """Handle looking at a specific item."""
    logger.debug("Looking at item", player=player_name, target=target)

    # Check room drops first
    item_found = _find_item_in_room_drops(room_drops, target_lower, instance_number)
    result = _check_item_in_location(item_found, prototype_registry)
    if result:
        return result

    # Check inventory
    inventory = player.get_inventory() if hasattr(player, "get_inventory") else []
    item_found = _find_item_in_inventory(inventory, target_lower, instance_number)
    result = _check_item_in_location(item_found, prototype_registry)
    if result:
        return result

    # Check equipped items (if not looking inside a container)
    if not command_data.get("look_in", False):
        result = _check_equipped_item(player, target_lower, instance_number, prototype_registry)
        if result:
            return result

    logger.debug("Item not found", player=player_name, target=target)
    return {"result": f"You don't see any '{target}' here."}


async def _try_lookup_item_implicit(
    target_lower: str,
    instance_number: int | None,
    room_drops: list[dict[str, Any]],
    player: Any,
    prototype_registry: Any,
) -> dict[str, Any] | None:
    """Try to find and display an item in implicit lookup."""
    # Check room drops
    item_found = _find_item_in_room_drops(room_drops, target_lower, instance_number)
    result = _check_item_in_location(item_found, prototype_registry)
    if result:
        return result

    # Check inventory
    inventory = player.get_inventory() if hasattr(player, "get_inventory") else []
    item_found = _find_item_in_inventory(inventory, target_lower, instance_number)
    result = _check_item_in_location(item_found, prototype_registry)
    if result:
        return result

    # Check equipped items
    equipped = player.get_equipped_items() if hasattr(player, "get_equipped_items") else {}
    equipped_result = _find_item_in_equipped(equipped, target_lower, instance_number)
    if equipped_result:
        equipped_slot, item_found = equipped_result
        result = _check_item_in_location(item_found, prototype_registry, f"equipped in {equipped_slot}")
        if result:
            return result

    return None


__all__ = [
    "_find_item_in_room_drops",
    "_find_item_in_inventory",
    "_find_item_in_equipped",
    "_get_item_description_from_prototype",
    "_check_item_in_location",
    "_check_equipped_item",
    "_handle_item_look",
    "_try_lookup_item_implicit",
]
