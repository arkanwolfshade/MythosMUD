"""
Exploration commands for MythosMUD.

This module contains handlers for exploration-related commands like look and go.
"""

import re
from typing import Any
from uuid import UUID

from ..alias_storage import AliasStorage
from ..logging.enhanced_logging_config import get_logger
from ..services.wearable_container_service import WearableContainerService
from ..utils.command_parser import get_username_from_user
from ..utils.room_renderer import build_room_drop_summary, clone_room_drops, format_room_drop_lines

logger = get_logger(__name__)

_SHARED_WEARABLE_CONTAINER_SERVICE = WearableContainerService()


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
        stats: Dictionary containing 'health' and 'max_health' keys

    Returns:
        Descriptive health label: "healthy", "wounded", "critical", or "mortally wounded"
    """
    health = stats.get("health", 0)
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


def _get_Lucidity_label(stats: dict) -> str:
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

    Lucidity_percent = (lucidity / max_lucidity) * 100

    if Lucidity_percent > 75:
        return "lucid"
    elif Lucidity_percent >= 25:
        return "disturbed"
    elif Lucidity_percent > 0:
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


def _get_players_in_room(room: Any, persistence: Any) -> list[Any]:
    """
    Get all Player objects currently in the room.

    Args:
        room: Room object with get_players() method
        persistence: PersistenceLayer object with get_player() method

    Returns:
        List of Player objects in the room (None players filtered out)
    """
    import uuid

    player_ids = room.get_players() if hasattr(room, "get_players") else []
    players = []
    for player_id_str in player_ids:
        try:
            # Convert string to UUID if needed
            player_id = uuid.UUID(player_id_str) if isinstance(player_id_str, str) else player_id_str
            # Use get_player (not get_player_by_id) as that's the actual method name
            player = persistence.get_player(player_id) if hasattr(persistence, "get_player") else None
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
    logger.debug("Processing look command", player=player_name, args=command_data)

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning("Look command failed - no persistence layer", player=player_name)
        return {"result": "You see nothing special."}

    player = persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        logger.warning("Look command failed - player not found", player=player_name)
        return {"result": "You see nothing special."}

    room_id = player.current_room_id
    room = persistence.get_room(room_id)
    if not room:
        logger.warning("Look command failed - room not found", player=player_name, room_id=room_id)
        return {"result": "You see nothing special."}

    connection_manager = getattr(app.state, "connection_manager", None) if app else None
    room_manager = getattr(connection_manager, "room_manager", None) if connection_manager else None
    room_drops: list[dict[str, Any]] = []
    if room_manager and hasattr(room_manager, "list_room_drops"):
        try:
            drops = room_manager.list_room_drops(str(room_id))
            room_drops = clone_room_drops(drops)
        except Exception as exc:  # pragma: no cover - defensive logging path
            logger.debug("Failed to list room drops", player=player_name, room_id=room_id, error=str(exc))

    # Extract command data
    direction = command_data.get("direction")
    target = command_data.get("target")
    target_type = command_data.get("target_type")
    instance_number = command_data.get("instance_number")

    # Handle explicit player look
    if target_type == "player" and target:
        target_lower = target.lower()
        logger.debug("Looking at player", player=player_name, target=target, room_id=room_id)

        # Get players in room
        players_in_room = _get_players_in_room(room, persistence)

        # Find matching players (case-insensitive partial match)
        matching_players = []
        for p in players_in_room:
            if hasattr(p, "name") and target_lower in p.name.lower():
                matching_players.append(p)

        if not matching_players:
            logger.debug("No players match target", player=player_name, target=target, room_id=room_id)
            return {"result": f"You don't see anyone named '{target}' here."}

        # Handle instance targeting
        if instance_number is not None:
            if instance_number < 1 or instance_number > len(matching_players):
                return {"result": f"There aren't that many '{target}' here."}
            target_player = matching_players[instance_number - 1]
        elif len(matching_players) == 1:
            target_player = matching_players[0]
        else:
            # Multiple matches - list them
            player_names = [p.name for p in matching_players if hasattr(p, "name")]
            logger.debug("Multiple players match target", player=player_name, target=target, matches=player_names)
            return {"result": f"You see multiple players matching '{target}': {', '.join(player_names)}"}

        # Display player information
        player_name_display = target_player.name if hasattr(target_player, "name") else "Unknown"
        stats = target_player.get_stats() if hasattr(target_player, "get_stats") else {}
        position = stats.get("position", "standing") if stats else "standing"

        health_label = _get_health_label(stats)
        Lucidity_label = _get_Lucidity_label(stats)
        visible_equipment = _get_visible_equipment(target_player)

        # Build display
        lines = [player_name_display]

        # Visible equipment
        if visible_equipment:
            equipment_parts = []
            for slot, item in visible_equipment.items():
                item_name = item.get("item_name", "Unknown") if isinstance(item, dict) else str(item)
                equipment_parts.append(f"{slot}: {item_name}")
            if equipment_parts:
                lines.append(f"Visible Equipment: {', '.join(equipment_parts)}")

        lines.append(f"Position: {position}")
        lines.append(f"Health: {health_label}")
        lines.append(f"lucidity: {Lucidity_label}")

        result_text = "\n".join(lines)
        logger.debug("Player look completed", player=player_name, target=target, target_player=player_name_display)
        return {"result": result_text}

    # Handle explicit item look
    if target_type == "item" and target:
        target_lower = target.lower()
        logger.debug("Looking at item", player=player_name, target=target, room_id=room_id)

        # Get prototype registry for item descriptions
        prototype_registry = getattr(app.state, "prototype_registry", None) if app else None

        # Try finding item in room drops first
        item_found = _find_item_in_room_drops(room_drops, target_lower, instance_number)
        if item_found:
            prototype_id = item_found.get("prototype_id") or item_found.get("item_id")
            if prototype_registry and prototype_id:
                try:
                    prototype = prototype_registry.get(prototype_id)
                    item_name = item_found.get("item_name", prototype.name)
                    description = prototype.long_description
                    return {"result": f"{item_name}\n{description}"}
                except Exception:
                    item_name = item_found.get("item_name", "Unknown Item")
                    return {"result": f"{item_name}\nYou see nothing remarkable about it."}

        # Try finding item in inventory
        inventory = player.get_inventory() if hasattr(player, "get_inventory") else []
        item_found = _find_item_in_inventory(inventory, target_lower, instance_number)
        if item_found:
            prototype_id = item_found.get("prototype_id") or item_found.get("item_id")
            if prototype_registry and prototype_id:
                try:
                    prototype = prototype_registry.get(prototype_id)
                    item_name = item_found.get("item_name", item_found.get("name", prototype.name))
                    description = prototype.long_description
                    return {"result": f"{item_name}\n{description}"}
                except Exception:
                    item_name = item_found.get("item_name", item_found.get("name", "Unknown Item"))
                    return {"result": f"{item_name}\nYou see nothing remarkable about it."}

        # Try finding item in equipped items
        # BUT: If look_in is True, skip item lookup and go straight to container lookup
        if not command_data.get("look_in", False):
            equipped = player.get_equipped_items() if hasattr(player, "get_equipped_items") else {}
            equipped_result = _find_item_in_equipped(equipped, target_lower, instance_number)
            if equipped_result:
                slot, item_found = equipped_result
                prototype_id = item_found.get("prototype_id") or item_found.get("item_id")
                if prototype_registry and prototype_id:
                    try:
                        prototype = prototype_registry.get(prototype_id)
                        item_name = item_found.get("item_name", item_found.get("name", prototype.name))
                        description = prototype.long_description
                        return {"result": f"{item_name} (equipped in {slot})\n{description}"}
                    except Exception:
                        item_name = item_found.get("item_name", item_found.get("name", "Unknown Item"))
                        return {"result": f"{item_name} (equipped in {slot})\nYou see nothing remarkable about it."}

        # Item not found
        logger.debug("Item not found", player=player_name, target=target, room_id=room_id)
        return {"result": f"You don't see any '{target}' here."}

    # Handle explicit container look or container inspection
    if (target_type == "container" or command_data.get("look_in", False)) and target:
        target_lower = target.lower()
        logger.debug(
            "Looking at container",
            player=player_name,
            target=target,
            room_id=room_id,
            look_in=command_data.get("look_in", False),
        )

        # Get prototype registry for container descriptions
        prototype_registry = getattr(app.state, "prototype_registry", None) if app else None

        # Get containers in room
        room_containers = room.get_containers() if hasattr(room, "get_containers") else []
        container_found = _find_container_in_room(room_containers, target_lower, instance_number)
        container_item = None  # Track the item for wearable containers to get prototype

        # Also check wearable containers
        if not container_found:
            equipped = player.get_equipped_items() if hasattr(player, "get_equipped_items") else {}
            wearable_result = _find_container_wearable(equipped, target_lower, instance_number)
            if wearable_result:
                slot, item = wearable_result
                container_item = item  # Store item to get prototype_id later
                # Try to get container from item's inner_container first
                inner_container_id = item.get("inner_container")
                if inner_container_id:
                    try:
                        container_id = (
                            UUID(inner_container_id) if isinstance(inner_container_id, str) else inner_container_id
                        )
                        container_data = (
                            persistence.get_container(container_id) if hasattr(persistence, "get_container") else None
                        )
                        if container_data:
                            container_found = container_data
                    except (ValueError, TypeError):
                        # inner_container might not be a valid UUID, try wearable container service
                        pass

                # If not found via inner_container, use wearable container service
                if not container_found:
                    try:
                        player_id_uuid = UUID(str(player.player_id))
                        wearable_containers = _SHARED_WEARABLE_CONTAINER_SERVICE.get_wearable_containers_for_player(
                            player_id_uuid
                        )
                        slot_lower = slot.lower() if slot else ""
                        item_instance_id = item.get("item_instance_id")

                        for container_component in wearable_containers:
                            # Match by item_instance_id (most reliable), slot name, or container metadata item_name
                            container_metadata = (
                                container_component.metadata if hasattr(container_component, "metadata") else {}
                            )
                            container_item_name = str(container_metadata.get("item_name", "")).lower()
                            container_slot = str(container_metadata.get("slot", "")).lower()
                            container_item_instance_id = container_metadata.get("item_instance_id")

                            # Match by item_instance_id first (most reliable)
                            if (
                                item_instance_id
                                and container_item_instance_id
                                and str(item_instance_id) == str(container_item_instance_id)
                            ):
                                # Found matching container, get full container data
                                container_id_from_component = container_component.container_id
                                if container_id_from_component:
                                    container_data = (
                                        persistence.get_container(container_id_from_component)
                                        if hasattr(persistence, "get_container")
                                        else None
                                    )
                                    if container_data:
                                        container_found = container_data
                                        logger.debug(
                                            "Found container via wearable container service (item_instance_id match) for look command",
                                            container_id=str(container_id_from_component),
                                            slot=slot,
                                            item_instance_id=item_instance_id,
                                            player=player_name,
                                        )
                                        break
                            # Fallback: match by slot name or container metadata item_name
                            elif (
                                container_slot == slot_lower
                                or target_lower in container_item_name
                                or target_lower in container_slot
                            ):
                                # Found matching container, get full container data
                                container_id_from_component = container_component.container_id
                                if container_id_from_component:
                                    container_data = (
                                        persistence.get_container(container_id_from_component)
                                        if hasattr(persistence, "get_container")
                                        else None
                                    )
                                    if container_data:
                                        container_found = container_data
                                        logger.debug(
                                            "Found container via wearable container service (name match) for look command",
                                            container_id=str(container_id_from_component),
                                            slot=slot,
                                            player=player_name,
                                        )
                                        break
                    except Exception as e:
                        logger.debug(
                            "Error finding container via wearable container service for look command",
                            error=str(e),
                            slot=slot,
                            player=player_name,
                        )

        if not container_found:
            logger.debug("Container not found", player=player_name, target=target, room_id=room_id)
            return {"result": f"You don't see any '{target}' here."}

        # Get container name from metadata or use fallback
        container_name = container_found.get("metadata", {}).get(
            "name", f"Container {str(container_found.get('container_id', 'Unknown'))[:8]}"
        )
        items = container_found.get("items", [])
        capacity_slots = container_found.get("capacity_slots", 0)
        lock_state = container_found.get("lock_state", "unlocked")

        # Build container display
        lines = [container_name]

        # Get and display container description from prototype
        container_description = None
        if container_item:
            # For wearable containers, get prototype from the item
            prototype_id = container_item.get("prototype_id") or container_item.get("item_id")
            if prototype_registry and prototype_id:
                try:
                    prototype = prototype_registry.get(prototype_id)
                    if prototype and hasattr(prototype, "long_description"):
                        container_description = prototype.long_description
                except Exception:
                    logger.debug("Failed to get prototype for container", prototype_id=prototype_id)
        else:
            # For room containers, try to get prototype from container metadata
            prototype_id = container_found.get("metadata", {}).get("prototype_id") or container_found.get(
                "prototype_id"
            )
            if prototype_registry and prototype_id:
                try:
                    prototype = prototype_registry.get(prototype_id)
                    if prototype and hasattr(prototype, "long_description"):
                        container_description = prototype.long_description
                except Exception:
                    logger.debug("Failed to get prototype for container", prototype_id=prototype_id)

        # Add description if available
        if container_description:
            lines.append(container_description)

        # Lock status
        if lock_state == "locked":
            lines.append("Locked")
        elif lock_state == "sealed":
            lines.append("Sealed")

        # Capacity information
        used_slots = len(items)
        lines.append(f"Capacity: {used_slots}/{capacity_slots} slots")

        # Contents (if look_in is True or explicit container look)
        if command_data.get("look_in", False) or target_type == "container":
            lines.append("Contents:")
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

        result_text = "\n".join(lines)
        logger.debug("Container look completed", player=player_name, target=target, container_name=container_name)
        return {"result": result_text}

    # Handle target lookups with priority resolution (Players > NPCs > Items > Containers > Directions)
    if target and not target_type:
        target_lower = target.lower()
        logger.debug("Looking at target", player=player_name, target=target, room_id=room_id)

        # Priority 1: Check if target is a direction (only if no explicit type)
        if target_lower in ["north", "south", "east", "west", "up", "down", "n", "s", "e", "w", "u", "d"]:
            direction = target_lower
        else:
            # Priority 2: Try players first
            players_in_room = _get_players_in_room(room, persistence)
            matching_players = []
            for p in players_in_room:
                if hasattr(p, "name") and target_lower in p.name.lower():
                    matching_players.append(p)

            if matching_players:
                # Handle instance targeting
                if instance_number is not None:
                    if instance_number < 1 or instance_number > len(matching_players):
                        return {"result": f"There aren't that many '{target}' here."}
                    target_player = matching_players[instance_number - 1]
                elif len(matching_players) == 1:
                    target_player = matching_players[0]
                else:
                    player_names = [p.name for p in matching_players if hasattr(p, "name")]
                    logger.debug(
                        "Multiple players match target", player=player_name, target=target, matches=player_names
                    )
                    return {"result": f"You see multiple players matching '{target}': {', '.join(player_names)}"}

                # Display player information
                player_name_display = target_player.name if hasattr(target_player, "name") else "Unknown"
                stats = target_player.get_stats() if hasattr(target_player, "get_stats") else {}
                position = stats.get("position", "standing") if stats else "standing"

                health_label = _get_health_label(stats)
                Lucidity_label = _get_Lucidity_label(stats)
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
                lines.append(f"lucidity: {Lucidity_label}")

                result_text = "\n".join(lines)
                logger.debug(
                    "Player look completed", player=player_name, target=target, target_player=player_name_display
                )
                return {"result": result_text}

            # Priority 3: Try NPCs
            npc_ids = room.get_npcs()
            if npc_ids:
                # Find matching NPCs (case-insensitive partial match)
                matching_npcs = []
                for npc_id in npc_ids:
                    # Get NPC instance to check name
                    from ..services.npc_instance_service import get_npc_instance_service

                    npc_instance_service = get_npc_instance_service()
                    # Use the same approach as combat system
                    if hasattr(npc_instance_service, "lifecycle_manager"):
                        lifecycle_manager = npc_instance_service.lifecycle_manager
                        if lifecycle_manager and npc_id in lifecycle_manager.active_npcs:
                            npc_instance = lifecycle_manager.active_npcs[npc_id]
                            if npc_instance and target_lower in npc_instance.name.lower():
                                matching_npcs.append(npc_instance)

                if len(matching_npcs) == 1:
                    npc = matching_npcs[0]
                    logger.debug("Found NPC to look at", player=player_name, npc_name=npc.name, npc_id=npc.npc_id)
                    description = getattr(npc.definition, "description", "Nothing remarkable about them.")
                    return {"result": f"You look at {npc.name}.\n{description}"}
                elif len(matching_npcs) > 1:
                    npc_names = [npc.name for npc in matching_npcs]
                    logger.debug("Multiple NPCs match target", player=player_name, target=target, matches=npc_names)
                    return {"result": f"You see multiple NPCs matching '{target}': {', '.join(npc_names)}"}

            # Priority 4: Try items
            # Get prototype registry for item descriptions
            prototype_registry = getattr(app.state, "prototype_registry", None) if app else None

            # Try finding item in room drops
            item_found = _find_item_in_room_drops(room_drops, target_lower, instance_number)
            if item_found:
                prototype_id = item_found.get("prototype_id") or item_found.get("item_id")
                if prototype_registry and prototype_id:
                    try:
                        prototype = prototype_registry.get(prototype_id)
                        item_name = item_found.get("item_name", prototype.name)
                        description = prototype.long_description
                        return {"result": f"{item_name}\n{description}"}
                    except Exception:
                        # Prototype not found, use fallback
                        item_name = item_found.get("item_name", "Unknown Item")
                        return {"result": f"{item_name}\nYou see nothing remarkable about it."}

            # Try finding item in inventory
            inventory = player.get_inventory() if hasattr(player, "get_inventory") else []
            item_found = _find_item_in_inventory(inventory, target_lower, instance_number)
            if item_found:
                prototype_id = item_found.get("prototype_id") or item_found.get("item_id")
                if prototype_registry and prototype_id:
                    try:
                        prototype = prototype_registry.get(prototype_id)
                        item_name = item_found.get("item_name", item_found.get("name", prototype.name))
                        description = prototype.long_description
                        return {"result": f"{item_name}\n{description}"}
                    except Exception:
                        item_name = item_found.get("item_name", item_found.get("name", "Unknown Item"))
                        return {"result": f"{item_name}\nYou see nothing remarkable about it."}

            # Try finding item in equipped items
            equipped = player.get_equipped_items() if hasattr(player, "get_equipped_items") else {}
            equipped_result = _find_item_in_equipped(equipped, target_lower, instance_number)
            if equipped_result:
                slot, item_found = equipped_result
                prototype_id = item_found.get("prototype_id") or item_found.get("item_id")
                if prototype_registry and prototype_id:
                    try:
                        prototype = prototype_registry.get(prototype_id)
                        item_name = item_found.get("item_name", item_found.get("name", prototype.name))
                        description = prototype.long_description
                        return {"result": f"{item_name} (equipped in {slot})\n{description}"}
                    except Exception:
                        item_name = item_found.get("item_name", item_found.get("name", "Unknown Item"))
                        return {"result": f"{item_name} (equipped in {slot})\nYou see nothing remarkable about it."}

            # Priority 5: Try containers
            room_containers = room.get_containers() if hasattr(room, "get_containers") else []
            container_found = _find_container_in_room(room_containers, target_lower, instance_number)

            # Also check wearable containers
            if not container_found:
                equipped = player.get_equipped_items() if hasattr(player, "get_equipped_items") else {}
                wearable_result = _find_container_wearable(equipped, target_lower, instance_number)
                if wearable_result:
                    slot, item = wearable_result
                    inner_container_id = item.get("inner_container")
                    if inner_container_id:
                        container_data = (
                            persistence.get_container(inner_container_id)
                            if hasattr(persistence, "get_container")
                            else None
                        )
                        if container_data:
                            container_found = container_data

            if container_found:
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
                logger.debug(
                    "Container look completed", player=player_name, target=target, container_name=container_name
                )
                return {"result": result_text}

            # Priority 6: Try directions (already handled above, but fall through if not a direction)
            logger.debug("No matches found for target", player=player_name, target=target, room_id=room_id)
            return {"result": f"You don't see any '{target}' here."}

    # Handle direction lookups
    if direction:
        direction = direction.lower()
        logger.debug("Looking in direction", player=player_name, direction=direction, room_id=room_id)
        exits = room.exits
        target_room_id = exits.get(direction)
        if target_room_id:
            target_room = persistence.get_room(target_room_id)
            if target_room:
                # Convert to strings to handle test mocks that might return MagicMock objects
                name = str(target_room.name) if target_room.name is not None else "Unknown Room"
                desc = (
                    str(target_room.description) if target_room.description is not None else "You see nothing special."
                )
                logger.debug(
                    "Looked at room in direction",
                    player=player_name,
                    direction=direction,
                    target_room_id=target_room_id,
                )
                return {"result": f"{name}\n{desc}"}
        logger.debug("No valid exit in direction", player=player_name, direction=direction, room_id=room_id)
        return {"result": "You see nothing special that way."}

    # Look at current room
    # Convert to strings to handle test mocks that might return MagicMock objects
    name = str(room.name) if room.name is not None else "Unknown Room"
    desc = str(room.description) if room.description is not None else "You see nothing special."
    exits = room.exits
    # Only include exits that have valid room IDs (not null)
    valid_exits = [direction for direction, room_id in exits.items() if room_id is not None]
    exit_list = ", ".join(valid_exits) if valid_exits else "none"
    logger.debug("Looked at current room", player=player_name, room_id=room_id, exits=valid_exits)

    drop_lines = format_room_drop_lines(room_drops)
    drop_summary = build_room_drop_summary(room_drops)
    # Ensure all items in lines are strings (handle test mocks)
    lines = [name, desc, "", *[str(line) for line in drop_lines], "", f"Exits: {exit_list}"]
    rendered = "\n".join(lines)

    return {
        "result": rendered,
        "drop_summary": drop_summary,
        "room_drops": room_drops,
    }


async def handle_go_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
) -> dict[str, str]:
    """
    Handle the go command for movement.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Go command result
    """
    logger.debug("Processing go command", player=player_name, args=command_data)

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning("Go command failed - no persistence layer", player=player_name)
        return {"result": "You can't go that way"}

    # Extract direction from command_data
    direction = command_data.get("direction")
    if not direction:
        logger.warning("Go command failed - no direction specified", player=player_name, command_data=command_data)
        return {"result": "Go where? Usage: go <direction>"}

    direction = direction.lower()
    logger.debug("Player attempting to move", player=player_name, direction=direction)

    player = persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        logger.warning("Go command failed - player not found", player=player_name)
        return {"result": "You can't go that way"}

    room_id = player.current_room_id
    room = persistence.get_room(room_id)
    if not room:
        logger.warning("Go command failed - current room not found", player=player_name, room_id=room_id)
        return {"result": "You can't go that way"}

    # Ensure room ID consistency - use room object's ID if it differs from player's current_room_id
    # This handles cases where room IDs might be stored in different formats
    if room.id != room_id:
        logger.warning(
            "Room ID mismatch detected",
            player=player_name,
            player_room_id=room_id,
            room_object_id=room.id,
        )
        # Use the room object's ID for consistency
        room_id = room.id

    # Enforce posture requirements before attempting movement
    position = "standing"
    if hasattr(player, "get_stats"):
        try:
            stats = player.get_stats() or {}
            position = str(stats.get("position", "standing") or "standing").lower()
        except Exception as exc:  # pragma: no cover - defensive logging path
            logger.warning(
                "Failed to read player stats during go command",
                player=player_name,
                error=str(exc),
                room_id=room_id,
            )
            position = "standing"

    if position != "standing":
        logger.info(
            "Movement blocked - player not standing",
            player=player_name,
            position=position,
            direction=direction,
            room_id=room_id,
        )
        return {"result": "You need to stand up before moving."}

    exits = room.exits
    # Ensure exits is a dictionary and not None
    if not exits:
        exits = {}
        logger.warning(
            "Room has no exits dictionary",
            player=player_name,
            room_id=room_id,
            room_object_id=room.id,
        )

    # Debug logging to diagnose movement bug
    logger.info(
        "DEBUG: Movement attempt",
        player=player_name,
        player_current_room_id=player.current_room_id,
        room_object_id=room.id,
        room_id_used=room_id,
        direction=direction,
        exits_dict=exits,
        exits_dict_keys=list(exits.keys()) if exits else [],
        exits_dict_type=type(exits).__name__,
    )
    target_room_id = exits.get(direction)
    if not target_room_id:
        # No exit in this direction - normal gameplay, just return error message to player
        return {"result": "You can't go that way"}

    target_room = persistence.get_room(target_room_id)
    if not target_room:
        logger.warning("Go command failed - target room not found", player=player_name, target_room_id=target_room_id)
        return {"result": "You can't go that way"}

    # Use movement service for the actual movement
    from ..game.movement_service import MovementService

    try:
        # Get player combat service from app state
        player_combat_service = getattr(app.state, "player_combat_service", None) if app else None

        # Pass the same event bus that persistence uses to ensure events are published correctly
        # Also pass player_combat_service to enforce combat state validation
        movement_service = MovementService(persistence._event_bus, player_combat_service=player_combat_service)
        success = movement_service.move_player(player.player_id, room_id, target_room_id)

        if success:
            logger.info("Player moved successfully", player=player_name, from_room=room_id, to_room=target_room_id)

            # CRITICAL FIX: Explicitly send room_update event to ensure Room Info panel updates
            # The EventBus flow should handle this, but we send it directly as a fallback
            # to ensure the client always receives the room update during movement
            try:
                connection_manager = getattr(app.state, "connection_manager", None) if app else None
                event_handler = getattr(app.state, "event_handler", None) if app else None

                if connection_manager and event_handler:
                    # Send room update directly to the moving player
                    await event_handler._send_room_update_to_player(player.player_id, target_room_id)
                    logger.debug(
                        "Sent explicit room_update after movement",
                        player=player_name,
                        room_id=target_room_id,
                    )
            except Exception as e:
                # Log but don't fail the movement if room update sending fails
                logger.warning(
                    "Failed to send room_update after movement",
                    player=player_name,
                    room_id=target_room_id,
                    error=str(e),
                )

            return {
                "result": f"You go {direction}.",
                "room_changed": True,
                "room_id": target_room_id,
            }
        else:
            logger.warning("Movement service failed", player=player_name, from_room=room_id, to_room=target_room_id)
            return {"result": "You can't go that way."}

    except Exception as e:
        logger.error(
            "Go command error",
            player=player_name,
            command_data=command_data,
            room_id=room_id,
            target_room_id=target_room_id,
            error_type=type(e).__name__,
            error_message=str(e),
            exc_info=True,
        )
        return {"result": f"Error during movement: {str(e)}"}
