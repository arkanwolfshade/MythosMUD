"""
Look command for MythosMUD.

This module handles the look command for examining surroundings.
"""

import re
import uuid
from typing import Any
from uuid import UUID

from ..alias_storage import AliasStorage
from ..logging.enhanced_logging_config import get_logger
from ..services.npc_instance_service import get_npc_instance_service
from ..services.wearable_container_service import WearableContainerService
from ..utils.command_parser import get_username_from_user
from ..utils.room_renderer import build_room_drop_summary, clone_room_drops, format_room_drop_lines

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
        stats: Dictionary containing 'current_health' and 'max_health' keys

    Returns:
        Descriptive health label: "healthy", "wounded", "critical", or "mortally wounded"
    """
    health = stats.get("current_health", 0)
    max_health = stats.get("max_health", 100)
    if max_health == 0:
        return "mortally wounded"

    health_percent = (health / max_health) * 100

    if health_percent > 75:
        return "healthy"
    elif health_percent >= 25:
        return "wounded"
    elif health_percent > 0:
        return "critical"
    else:
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
    if max_lucidity == 0:
        return "mad"

    lucidity_percent = (lucidity / max_lucidity) * 100

    if lucidity_percent > 75:
        return "lucid"
    elif lucidity_percent >= 25:
        return "disturbed"
    elif lucidity_percent > 0:
        return "unstable"
    else:
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


async def _get_players_in_room(room: Any, persistence: Any) -> list[Any]:
    """
    Get all Player objects currently in the room.

    Args:
        room: Room object with get_players() method
        persistence: AsyncPersistenceLayer object with get_player_by_id() method

    Returns:
        List of Player objects in the room (None players filtered out)
    """
    player_ids = room.get_players() if hasattr(room, "get_players") else []
    players = []
    for player_id_str in player_ids:
        try:
            # Convert string to UUID if needed
            player_id = uuid.UUID(player_id_str) if isinstance(player_id_str, str) else player_id_str
            # Use get_player_by_id (async method)
            player = await persistence.get_player_by_id(player_id) if hasattr(persistence, "get_player_by_id") else None
            if player:
                players.append(player)
        except (ValueError, AttributeError):
            # Invalid UUID format or persistence doesn't have get_player
            logger.debug("Failed to get player", player_id=player_id_str, error="Invalid UUID or missing method")
            continue
    return players


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


async def _find_matching_players(target_lower: str, room: Any, persistence: Any) -> list[Any]:
    """Find players in room matching the target name."""
    players_in_room = await _get_players_in_room(room, persistence)
    matching_players = []
    for p in players_in_room:
        if hasattr(p, "name") and target_lower in p.name.lower():
            matching_players.append(p)
    return matching_players


def _select_target_player(
    matching_players: list[Any],
    target: str,
    instance_number: int | None,
    player_name: str,
) -> tuple[Any, dict[str, str] | None]:
    """
    Select target player from matching players, handling instance numbers and multiple matches.

    Returns:
        tuple: (target_player, error_result) - error_result is None if selection succeeded
    """
    if not matching_players:
        return (None, {"result": f"You don't see anyone named '{target}' here."})

    if instance_number is not None:
        if instance_number < 1 or instance_number > len(matching_players):
            return (None, {"result": f"There aren't that many '{target}' here."})
        return (matching_players[instance_number - 1], None)

    if len(matching_players) == 1:
        return (matching_players[0], None)

    player_names = [p.name for p in matching_players if hasattr(p, "name")]
    logger.debug("Multiple players match target", player=player_name, target=target, matches=player_names)
    return (None, {"result": f"You see multiple players matching '{target}': {', '.join(player_names)}"})


def _format_player_look_display(target_player: Any) -> str:
    """Format the display text for looking at a player."""
    player_name_display = target_player.name if hasattr(target_player, "name") else "Unknown"
    stats = target_player.get_stats() if hasattr(target_player, "get_stats") else {}
    position = stats.get("position", "standing") if stats else "standing"

    health_label = _get_health_label(stats)
    lucidity_label = _get_lucidity_label(stats)
    visible_equipment = _get_visible_equipment(target_player)

    lines = [player_name_display]
    if visible_equipment:
        equipment_parts = []
        for slot, item in visible_equipment.items():
            item_name = item.get("item_name", "Unknown") if isinstance(item, dict) else str(item)
            equipment_parts.append(f"{slot}: {item_name}")
        if equipment_parts:
            lines.append(f"Visible Equipment: {', '.join(equipment_parts)}")

    lines.append(f"Position: {position}")
    lines.append(f"Health: {health_label}")
    lines.append(f"lucidity: {lucidity_label}")

    return "\n".join(lines)


async def _handle_player_look(
    target: str,
    target_lower: str,
    instance_number: int | None,
    room: Any,
    persistence: Any,
    player_name: str,
) -> dict[str, Any] | None:
    """Handle looking at a specific player."""
    logger.debug(
        "Looking at player", player=player_name, target=target, room_id=room.id if hasattr(room, "id") else None
    )

    matching_players = await _find_matching_players(target_lower, room, persistence)
    target_player, error_result = _select_target_player(matching_players, target, instance_number, player_name)

    if error_result:
        if not matching_players:
            logger.debug("No players match target", player=player_name, target=target)
        return error_result

    result_text = _format_player_look_display(target_player)
    player_name_display = target_player.name if hasattr(target_player, "name") else "Unknown"
    logger.debug("Player look completed", player=player_name, target=target, target_player=player_name_display)
    return {"result": result_text}


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


def _is_direction(target_lower: str) -> bool:
    """Check if target is a direction."""
    return target_lower in ["north", "south", "east", "west", "up", "down", "n", "s", "e", "w", "u", "d"]


async def _try_lookup_player_implicit(
    target: str,
    target_lower: str,
    instance_number: int | None,
    room: Any,
    persistence: Any,
    player_name: str,
) -> dict[str, Any] | None:
    """Try to find and display a player in implicit lookup."""
    matching_players = await _find_matching_players(target_lower, room, persistence)
    if not matching_players:
        return None

    target_player, error_result = _select_target_player(matching_players, target, instance_number, player_name)
    if error_result:
        return error_result

    result_text = _format_player_look_display(target_player)
    player_name_display = target_player.name if hasattr(target_player, "name") else "Unknown"
    logger.debug("Player look completed", player=player_name, target=target, target_player=player_name_display)
    return {"result": result_text}


def _find_matching_npcs(target_lower: str, npc_ids: list[Any]) -> list[Any]:
    """Find NPCs matching the target name."""
    matching_npcs = []
    for npc_id in npc_ids:
        npc_instance_service = get_npc_instance_service()
        if not hasattr(npc_instance_service, "lifecycle_manager"):
            continue

        lifecycle_manager = npc_instance_service.lifecycle_manager
        if not lifecycle_manager or npc_id not in lifecycle_manager.active_npcs:
            continue

        npc_instance = lifecycle_manager.active_npcs[npc_id]
        if npc_instance and target_lower in npc_instance.name.lower():
            matching_npcs.append(npc_instance)

    return matching_npcs


def _format_npc_description(npc: Any) -> str:
    """Format NPC description with fallback."""
    description = getattr(npc.definition, "description", None)
    if not description or description.strip() == "":
        return "You see nothing remarkable about them."
    return description


def _format_single_npc_result(npc: Any, player_name: str) -> dict[str, Any]:
    """Format result for a single matching NPC."""
    logger.debug("Found NPC to look at", player=player_name, npc_name=npc.name, npc_id=npc.npc_id)
    description = _format_npc_description(npc)
    return {"result": f"{npc.name}\n{description}"}


def _format_multiple_npcs_result(matching_npcs: list[Any], target_lower: str, player_name: str) -> dict[str, Any]:
    """Format result for multiple matching NPCs."""
    npc_names = [npc.name for npc in matching_npcs]
    logger.debug("Multiple NPCs match target", player=player_name, matches=npc_names)
    return {"result": f"You see multiple NPCs matching '{target_lower}': {', '.join(npc_names)}"}


async def _try_lookup_npc_implicit(target_lower: str, room: Any, player_name: str) -> dict[str, Any] | None:
    """Try to find and display an NPC in implicit lookup."""
    npc_ids = room.get_npcs()
    if not npc_ids:
        return None

    matching_npcs = _find_matching_npcs(target_lower, npc_ids)
    if not matching_npcs:
        return None

    if len(matching_npcs) == 1:
        return _format_single_npc_result(matching_npcs[0], player_name)

    return _format_multiple_npcs_result(matching_npcs, target_lower, player_name)


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


async def _handle_implicit_target_lookup(
    target: str,
    target_lower: str,
    instance_number: int | None,
    room: Any,
    player: Any,
    persistence: Any,
    room_drops: list[dict[str, Any]],
    app: Any,
    player_name: str,
) -> dict[str, Any] | None:
    """Handle implicit target lookup with priority resolution."""
    logger.debug("Looking at target", player=player_name, target=target)

    if _is_direction(target_lower):
        return None  # Will be handled as direction

    # Priority 1: Try players
    result = await _try_lookup_player_implicit(target, target_lower, instance_number, room, persistence, player_name)
    if result:
        return result

    # Priority 2: Try NPCs
    result = await _try_lookup_npc_implicit(target_lower, room, player_name)
    if result:
        return result

    # Priority 3: Try items
    prototype_registry = getattr(app.state, "prototype_registry", None) if app else None
    result = await _try_lookup_item_implicit(target_lower, instance_number, room_drops, player, prototype_registry)
    if result:
        return result

    # Priority 4: Try containers
    result = await _try_lookup_container_implicit(
        target, target_lower, instance_number, room, player, persistence, player_name
    )
    if result:
        return result

    logger.debug("No matches found for target", player=player_name, target=target, room_id=room.id)
    return {"result": f"You don't see any '{target}' here."}


async def _handle_direction_look(
    direction: str,
    room: Any,
    persistence: Any,
    player_name: str,
) -> dict[str, Any] | None:
    """Handle looking in a specific direction."""
    direction = direction.lower()
    logger.debug("Looking in direction", player=player_name, direction=direction)
    exits = room.exits
    target_room_id = exits.get(direction)
    if target_room_id:
        target_room = persistence.get_room_by_id(target_room_id)
        if target_room:
            name = str(target_room.name) if target_room.name is not None else "Unknown Room"
            desc = str(target_room.description) if target_room.description is not None else "You see nothing special."
            logger.debug(
                "Looked at room in direction",
                player=player_name,
                direction=direction,
                target_room_id=target_room_id,
            )
            return {"result": f"{name}\n{desc}"}
    logger.debug("No valid exit in direction", player=player_name, direction=direction)
    return {"result": "You see nothing special that way."}


async def _handle_room_look(
    room: Any,
    room_drops: list[dict[str, Any]],
    player_name: str,
) -> dict[str, Any]:
    """Handle looking at the current room."""
    name = str(room.name) if room.name is not None else "Unknown Room"
    desc = str(room.description) if room.description is not None else "You see nothing special."
    exits = room.exits
    valid_exits = [direction for direction, room_id in exits.items() if room_id is not None]
    exit_list = ", ".join(valid_exits) if valid_exits else "none"
    logger.debug(
        "Looked at current room",
        player=player_name,
        room_id=room.id if hasattr(room, "id") else None,
        exits=valid_exits,
    )

    drop_lines = format_room_drop_lines(room_drops)
    drop_summary = build_room_drop_summary(room_drops)
    lines = [name, desc, "", *[str(line) for line in drop_lines], "", f"Exits: {exit_list}"]
    rendered = "\n".join(lines)

    return {
        "result": rendered,
        "drop_summary": drop_summary,
        "room_drops": room_drops,
    }


async def _setup_look_command(
    request: Any, current_user: dict, player_name: str
) -> tuple[Any, Any, Any, Any, list[dict[str, Any]]] | None:
    """Setup and validate look command prerequisites."""
    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning("Look command failed - no persistence layer", player=player_name)
        return None

    player = await persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        logger.warning("Look command failed - player not found", player=player_name)
        return None

    room_id = player.current_room_id
    room = persistence.get_room_by_id(room_id)
    if not room:
        logger.warning("Look command failed - room not found", player=player_name, room_id=room_id)
        return None

    connection_manager = getattr(app.state, "connection_manager", None) if app else None
    room_manager = getattr(connection_manager, "room_manager", None) if connection_manager else None
    room_drops: list[dict[str, Any]] = []
    if room_manager and hasattr(room_manager, "list_room_drops"):
        try:
            drops = room_manager.list_room_drops(str(room_id))
            room_drops = clone_room_drops(drops)
        except (AttributeError, TypeError, ValueError) as exc:  # pragma: no cover - defensive logging path
            logger.debug("Failed to list room drops", player=player_name, room_id=room_id, error=str(exc))

    return (app, persistence, player, room, room_drops)


async def _route_look_command(
    command_data: dict,
    target: str | None,
    target_type: str | None,
    direction: str | None,
    instance_number: int | None,
    room: Any,
    player: Any,
    persistence: Any,
    room_drops: list[dict[str, Any]],
    app: Any,
    request: Any,
    player_name: str,
) -> dict[str, Any]:
    """Route look command to appropriate handler."""
    # Handle explicit player look
    if target_type == "player" and target:
        target_lower = target.lower()
        result = await _handle_player_look(target, target_lower, instance_number, room, persistence, player_name)
        if result:
            return result

    # Handle explicit item look
    if target_type == "item" and target:
        target_lower = target.lower()
        prototype_registry = getattr(app.state, "prototype_registry", None) if app else None
        result = await _handle_item_look(
            target, target_lower, instance_number, room_drops, player, prototype_registry, command_data, player_name
        )
        if result:
            return result

    # Handle explicit container look or container inspection
    if (target_type == "container" or command_data.get("look_in", False)) and target:
        target_lower = target.lower()
        prototype_registry = getattr(app.state, "prototype_registry", None) if app else None
        result = await _handle_container_look(
            target,
            target_lower,
            instance_number,
            room,
            player,
            persistence,
            prototype_registry,
            command_data,
            request,
            player_name,
        )
        if result:
            return result

    # Handle target lookups with priority resolution
    if target and not target_type:
        target_lower = target.lower()
        if target_lower in ["north", "south", "east", "west", "up", "down", "n", "s", "e", "w", "u", "d"]:
            direction = target_lower
        else:
            result = await _handle_implicit_target_lookup(
                target, target_lower, instance_number, room, player, persistence, room_drops, app, player_name
            )
            if result:
                return result

    # Handle direction lookups
    if direction:
        result = await _handle_direction_look(direction, room, persistence, player_name)
        if result:
            return result

    # Look at current room (default)
    return await _handle_room_look(room, room_drops, player_name)


async def handle_look_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, Any]:
    """
    Handle the look command for examining surroundings.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Look command result, including rendered text and room drop metadata
    """
    _ = alias_storage  # Unused parameter
    logger.debug("Processing look command", player=player_name, args=command_data)

    setup_result = await _setup_look_command(request, current_user, player_name)
    if not setup_result:
        return {"result": "You see nothing special."}

    app, persistence, player, room, room_drops = setup_result

    direction = command_data.get("direction")
    target = command_data.get("target")
    target_type = command_data.get("target_type")
    instance_number = command_data.get("instance_number")

    return await _route_look_command(
        command_data,
        target,
        target_type,
        direction,
        instance_number,
        room,
        player,
        persistence,
        room_drops,
        app,
        request,
        player_name,
    )


__all__ = ["handle_look_command"]
