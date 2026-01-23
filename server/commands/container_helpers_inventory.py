"""Container-related helper functions for inventory commands."""

# pylint: disable=too-many-arguments,too-many-locals,too-many-lines  # Reason: Container helpers require many parameters and intermediate variables for complex item management logic. Container helpers require extensive functionality for complex container operations.

import json
from typing import Any, cast
from uuid import UUID

from ..models.player import Player
from ..structured_logging.enhanced_logging_config import get_logger
from .inventory_service_helpers import get_shared_services

logger = get_logger(__name__)


def match_container_to_slot(container_component: Any, equipped_view: dict[str, dict[str, Any]]) -> str | None:
    """Match a container component to an equipped slot. Returns slot name or None."""
    container_metadata = container_component.metadata if hasattr(container_component, "metadata") else {}
    container_item_name = container_metadata.get("item_name")
    container_item_id = container_metadata.get("item_id")

    for slot_name, equipped_item in equipped_view.items():
        equipped_item_name = equipped_item.get("item_name")
        equipped_item_id = equipped_item.get("item_id")
        if (container_item_name and equipped_item_name and container_item_name == equipped_item_name) or (  # pylint: disable=too-many-boolean-expressions  # Reason: Item matching requires multiple boolean expressions for name and ID comparison
            container_item_id and equipped_item_id and container_item_id == equipped_item_id
        ):
            logger.debug(
                "Found matching slot",
                matching_slot=slot_name,
                container_item_name=container_item_name,
                equipped_item_name=equipped_item_name,
            )
            return slot_name

    logger.debug(
        "No matching slot found for container",
        container_item_name=container_item_name,
        container_item_id=container_item_id,
        equipped_slots=list(equipped_view.keys()),
    )
    return None


async def get_container_data_for_inventory(  # pylint: disable=too-many-locals  # Reason: Container helpers require many intermediate variables for complex container data processing
    request: Any, player: Player, equipped_view: dict[str, dict[str, Any]]
) -> tuple[dict[str, list[dict[str, Any]]], dict[str, int], dict[str, str]]:
    """Get container contents, capacities, and lock states for equipped containers."""
    container_contents: dict[str, list[dict[str, Any]]] = {}
    container_capacities: dict[str, int] = {}
    container_lock_states: dict[str, str] = {}

    try:
        _, wearable_container_service, _ = get_shared_services(request)
        player_id_uuid = UUID(str(player.player_id))
        wearable_containers = await wearable_container_service.get_wearable_containers_for_player(player_id_uuid)
        logger.debug(
            "Getting container contents",
            player_id=str(player_id_uuid),
            wearable_containers_count=len(wearable_containers),
            equipped_slots=list(equipped_view.keys()),
        )

        for container_component in wearable_containers:
            container_metadata = container_component.metadata if hasattr(container_component, "metadata") else {}
            container_item_name = container_metadata.get("item_name")
            container_item_id = container_metadata.get("item_id")
            logger.debug(
                "Processing container component",
                container_item_name=container_item_name,
                container_item_id=container_item_id,
                container_items_count=len(container_component.items) if container_component.items else 0,
            )

            matching_slot = match_container_to_slot(container_component, equipped_view)
            if matching_slot:
                container_capacities[matching_slot] = container_component.capacity_slots
                lock_state = container_component.lock_state
                if hasattr(lock_state, "value"):
                    container_lock_states[matching_slot] = lock_state.value
                else:
                    container_lock_states[matching_slot] = str(lock_state)

                if container_component.items:
                    container_contents[matching_slot] = [
                        cast(dict[str, Any], item) for item in container_component.items
                    ]
                else:
                    container_contents[matching_slot] = []
                logger.debug(
                    "Container contents set",
                    matching_slot=matching_slot,
                    items_count=len(container_contents[matching_slot]),
                )
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container access errors unpredictable, optional display
        logger.debug(
            "Error getting container contents for inventory display",
            error=str(e),
            player=player.name,
        )

    return container_contents, container_capacities, container_lock_states


def update_equipped_with_container_info(
    equipped_view: dict[str, dict[str, Any]],
    container_contents: dict[str, list[dict[str, Any]]],
    container_capacities: dict[str, int],
    container_lock_states: dict[str, str],
) -> None:
    """Update equipped items' metadata to include container information."""
    for slot_name, equipped_item in equipped_view.items():
        if slot_name in container_contents:
            container_items = container_contents[slot_name]
            container_slots_used = len(container_items)

            if "metadata" not in equipped_item:
                equipped_item["metadata"] = {}
            if "container" not in equipped_item["metadata"]:
                equipped_item["metadata"]["container"] = {}

            container_dict = equipped_item["metadata"]["container"]
            if isinstance(container_dict, dict):
                container_dict = dict(container_dict)  # Make a copy
            else:
                container_dict = {}
            container_dict.update(
                {
                    "lock_state": container_lock_states.get(slot_name, "unlocked"),
                    "capacity_slots": container_capacities.get(slot_name, 20),
                    "slots_in_use": container_slots_used,
                }
            )
            equipped_item["metadata"]["container"] = container_dict


def find_item_in_inventory(inventory: list[dict[str, Any]], item_name: str) -> tuple[dict[str, Any] | None, int | None]:
    """Find an item in inventory by name or index."""
    # Try to parse as index first
    try:
        index = int(item_name)
        if 1 <= index <= len(inventory):
            item_index = index - 1
            return inventory[item_index], item_index
    except ValueError:
        pass

    # Search by name
    target_lower = item_name.lower()
    for idx, item in enumerate(inventory):
        item_name_check = str(item.get("item_name", item.get("name", ""))).lower()
        if target_lower in item_name_check:
            return item, idx

    return None, None


def check_item_matches_target(item: dict[str, Any], slot: str, target_lower: str) -> tuple[bool, bool]:
    """Check if item matches target. Returns (name_matches, slot_matches)."""
    item_name_check = str(item.get("item_name", item.get("name", ""))).lower()
    slot_lower = slot.lower()
    name_matches = target_lower in item_name_check
    slot_matches = target_lower == slot_lower or target_lower in slot_lower
    return name_matches, slot_matches


async def try_inner_container(persistence: Any, item: dict[str, Any]) -> tuple[dict[str, Any] | None, UUID | None]:
    """Try to get container from inner_container. Returns (container_data, container_id)."""
    inner_container_id = item.get("inner_container")
    if not inner_container_id:
        return None, None

    try:
        container_id = UUID(inner_container_id) if isinstance(inner_container_id, str) else inner_container_id
        container_data = persistence.get_container(container_id) if hasattr(persistence, "get_container") else None
        if container_data:
            return container_data, container_id
    except (ValueError, TypeError):
        pass

    return None, None


async def try_wearable_container_service(
    persistence: Any, request: Any, player: Player, slot: str, target_lower: str
) -> tuple[dict[str, Any] | None, UUID | None]:
    """Try to find container via wearable container service. Returns (container_data, container_id)."""
    try:
        _, wearable_container_service, _ = get_shared_services(request)
        player_id_uuid = UUID(str(player.player_id))
        wearable_containers = await wearable_container_service.get_wearable_containers_for_player(player_id_uuid)

        slot_lower = slot.lower()
        for container_component in wearable_containers:
            container_metadata = container_component.metadata if hasattr(container_component, "metadata") else {}
            container_metadata_name = str(container_metadata.get("name", "")).lower()
            container_slot = str(container_metadata.get("slot", "")).lower()

            if container_slot == slot_lower or target_lower in container_metadata_name:
                container_id_from_component = container_component.container_id
                if container_id_from_component:
                    container_data = (
                        persistence.get_container(container_id_from_component)
                        if hasattr(persistence, "get_container")
                        else None
                    )
                    if container_data:
                        return container_data, container_id_from_component
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container lookup errors unpredictable
        logger.debug("Error finding container via wearable container service", error=str(e), player=player.name)

    return None, None


async def find_wearable_container_for_put(
    persistence: Any,
    request: Any,
    player: Player,
    container_name: str,
) -> tuple[dict[str, Any] | None, UUID | None]:
    """Find a wearable container for put command, creating if necessary."""
    equipped = player.get_equipped_items()
    target_lower = container_name.lower()

    for slot, item in equipped.items():
        name_matches, slot_matches = check_item_matches_target(item, slot, target_lower)

        if not (name_matches or slot_matches):
            continue

        container_data, container_id = await try_inner_container(persistence, item)
        if container_data:
            return container_data, container_id

        container_data, container_id = await try_wearable_container_service(
            persistence, request, player, slot, target_lower
        )
        if container_data:
            return container_data, container_id

        if slot_matches:
            container_found, container_id = await create_wearable_container(persistence, request, player, slot, item)
            if container_found:
                return container_found, container_id

    return None, None


async def create_wearable_container(
    persistence: Any, request: Any, player: Player, slot: str, item: dict[str, Any]
) -> tuple[dict[str, Any] | None, UUID | None]:
    """Create a wearable container for an equipped item."""
    try:
        _, wearable_container_service, _ = get_shared_services(request)
        player_id_uuid = UUID(str(player.player_id))
        container_result = await wearable_container_service.handle_equip_wearable_container(
            player_id=player_id_uuid,
            item_stack=item,
        )

        if container_result and container_result.get("container_id"):
            container_id_created = container_result.get("container_id")
            container_data = (
                persistence.get_container(container_id_created) if hasattr(persistence, "get_container") else None
            )
            if container_data:
                return container_data, container_id_created

        # Fallback: create container directly
        item_name = item.get("item_name", item.get("name", "Unknown"))
        container_data_created = persistence.create_container(
            source_type="equipment",
            entity_id=player_id_uuid,
            capacity_slots=20,
            metadata_json={"name": item_name, "slot": slot, "item_id": item.get("item_id")},
        )
        if container_data_created and container_data_created.get("container_id"):
            return container_data_created, container_data_created.get("container_id")
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container creation errors unpredictable
        logger.debug("Failed to create container for equipped item", error=str(e), player=player.name)

    return None, None


async def transfer_item_to_container(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Container helpers require many parameters for context and item transfer
    container_service: Any,
    persistence: Any,
    player: Player,
    container_id: UUID,
    item_found: dict[str, Any],
    quantity: int | None,
) -> dict[str, Any]:
    """Transfer an item to container from player inventory."""
    player_id_uuid = UUID(str(player.player_id))
    mutation_token = container_service.get_container_token(container_id, player_id_uuid)

    if not mutation_token:
        try:
            open_result = await container_service.open_container(container_id, player_id_uuid)
            mutation_token = open_result.get("mutation_token")
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container access errors unpredictable
            return {"error": f"Cannot access container: {str(e)}"}

    try:
        transfer_quantity = quantity if quantity else item_found.get("quantity", 1)

        # Ensure item has required fields
        if not item_found.get("item_instance_id") and not item_found.get("item_id"):
            return {"error": "Error: Item is missing required identification fields."}

        # Ensure item instance exists
        item_instance_id = item_found.get("item_instance_id")
        prototype_id = item_found.get("prototype_id") or item_found.get("item_id")
        if item_instance_id and prototype_id:
            try:
                persistence.ensure_item_instance(
                    item_instance_id=item_instance_id,
                    prototype_id=prototype_id,
                    owner_type="player",
                    owner_id=str(player.player_id),
                    quantity=transfer_quantity,
                    metadata=item_found.get("metadata"),
                    origin_source="inventory",
                    origin_metadata={"player_id": str(player.player_id)},
                )
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Item instance errors unpredictable
                logger.warning("Failed to ensure item instance before transfer", error=str(e))

        await container_service.transfer_to_container(
            container_id=container_id,
            player_id=player_id_uuid,
            mutation_token=mutation_token,
            item=item_found,
            quantity=transfer_quantity,
        )

        return {"success": True, "transfer_quantity": transfer_quantity}
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container operation errors unpredictable
        logger.error("Error putting item in container", player=player.name, error=str(e))
        return {"error": str(e)}


async def validate_put_command_inputs(
    command_data: dict, request: Any, connection_manager: Any, player: Player
) -> tuple[str, str, int | None, Any, Any, dict[str, Any] | None, int | None] | dict[str, str]:
    """Validate and extract inputs for put command."""
    item_name = command_data.get("item", "").strip()
    container_name = command_data.get("container", "").strip()
    quantity = command_data.get("quantity")

    if not item_name or not container_name:
        logger.warning(
            "Put command validation failed",
            player=player.name,
            item_name=item_name,
            container_name=container_name,
            command_data=command_data,
        )
        return {"result": "Usage: put <item> [in] <container> [quantity]"}

    app = getattr(request, "app", None)
    container_service = getattr(app.state, "container_service", None) if app else None
    if not container_service:
        return {"result": "Container service is unavailable."}

    room_manager = getattr(connection_manager, "room_manager", None)
    if not room_manager:
        return {"result": "Room manager is unavailable."}

    # Find item in inventory
    inventory = player.get_inventory()
    item_found, item_index = find_item_in_inventory(inventory, item_name)

    if not item_found:
        logger.debug(
            "Item not found in inventory for put command",
            item_name=item_name,
            player=player.name,
            inventory_count=len(inventory),
        )
        return {"result": f"You don't have '{item_name}' in your inventory."}

    return item_name, container_name, quantity, container_service, room_manager, item_found, item_index


def find_container_in_room(
    room_manager: Any, room_id: str, container_name: str
) -> tuple[dict[str, Any] | None, UUID | None]:
    """Find a container in the room by name."""
    room_containers = room_manager.get_containers(room_id) if hasattr(room_manager, "get_containers") else []
    target_lower = container_name.lower()

    for container in room_containers:
        container_name_check = str(container.get("metadata", {}).get("name", container.get("container_id", ""))).lower()
        if target_lower in container_name_check:
            container_id = UUID(container.get("container_id"))
            return container, container_id

    return None, None


def find_matching_equipped_containers(
    equipped: dict[str, Any], container_name: str
) -> list[tuple[str, dict[str, Any]]]:
    """Find equipped items that match container name."""
    target_lower = container_name.lower()
    matching_containers = []

    for slot, item in equipped.items():
        equipped_item_name = str(item.get("item_name", item.get("name", ""))).lower()
        prototype_id = str(item.get("prototype_id", item.get("item_id", ""))).lower()
        item_id = str(item.get("item_id", "")).lower()
        name_matches = target_lower in equipped_item_name or target_lower in prototype_id or target_lower in item_id

        if item.get("inner_container") or name_matches:
            if name_matches:
                matching_containers.append((slot, item))

    return matching_containers


def try_inner_container_by_id(
    persistence: Any, inner_container_id: Any, slot: str, player_name: str
) -> tuple[dict[str, Any] | None, UUID | None]:
    """Try to get container via inner_container_id."""
    if not inner_container_id:
        return None, None

    try:
        container_id = UUID(inner_container_id) if isinstance(inner_container_id, str) else inner_container_id
        container_data = persistence.get_container(container_id) if hasattr(persistence, "get_container") else None
        if container_data:
            logger.debug(
                "Found container via inner_container for get command",
                container_id=str(container_id),
                slot=slot,
                player=player_name,
            )
            return container_data, container_id
    except (ValueError, TypeError):
        pass
    return None, None


async def try_wearable_container_service_by_instance_id(
    persistence: Any,
    wearable_containers: list[Any],
    item_instance_id: Any,
    player_name: str,
) -> tuple[dict[str, Any] | None, UUID | None]:
    """Try to find container via wearable container service using item_instance_id match."""
    if not item_instance_id:
        return None, None

    for container_component in wearable_containers:
        container_metadata = container_component.metadata if hasattr(container_component, "metadata") else {}
        container_item_instance_id = container_metadata.get("item_instance_id")

        if container_item_instance_id and str(item_instance_id) == str(container_item_instance_id):
            container_id_from_component = container_component.container_id
            if container_id_from_component:
                container_data = (
                    persistence.get_container(container_id_from_component)
                    if hasattr(persistence, "get_container")
                    else None
                )
                if container_data:
                    logger.debug(
                        "Found container via wearable container service (item_instance_id match) for get command",
                        container_id=str(container_id_from_component),
                        item_instance_id=item_instance_id,
                        player=player_name,
                    )
                    return container_data, container_id_from_component
    return None, None


async def try_wearable_container_service_by_name(
    persistence: Any,
    wearable_containers: list[Any],
    slot: str,
    target_lower: str,
    player_name: str,
) -> tuple[dict[str, Any] | None, UUID | None]:
    """Try to find container via wearable container service using name/slot match."""
    slot_lower = slot.lower() if slot else ""
    for container_component in wearable_containers:
        container_metadata = container_component.metadata if hasattr(container_component, "metadata") else {}
        container_item_name = str(container_metadata.get("item_name", "")).lower()
        container_slot = str(container_metadata.get("slot", "")).lower()

        if container_slot == slot_lower or target_lower in container_item_name or target_lower in container_slot:
            container_id_from_component = container_component.container_id
            if container_id_from_component:
                container_data = (
                    persistence.get_container(container_id_from_component)
                    if hasattr(persistence, "get_container")
                    else None
                )
                if container_data:
                    logger.debug(
                        "Found container via wearable container service (name/slot match) for get command",
                        container_id=str(container_id_from_component),
                        container_name=container_item_name,
                        slot=slot,
                        player=player_name,
                    )
                    return container_data, container_id_from_component
    return None, None


async def find_wearable_container(
    persistence: Any,
    request: Any,
    player: Player,
    container_name: str,
) -> tuple[dict[str, Any] | None, UUID | None]:
    """Find a wearable container by name."""
    equipped = player.get_equipped_items()
    target_lower = container_name.lower()
    matching_containers = find_matching_equipped_containers(equipped, container_name)

    if not matching_containers:
        return None, None

    slot, item = matching_containers[0]
    item_instance_id = item.get("item_instance_id")
    inner_container_id = item.get("inner_container")

    # Try inner_container first
    container_data, container_id = try_inner_container_by_id(persistence, inner_container_id, slot, player.name)
    if container_data:
        return container_data, container_id

    # Try wearable container service
    try:
        _, wearable_container_service, _ = get_shared_services(request)
        player_id_uuid = UUID(str(player.player_id))
        wearable_containers = await wearable_container_service.get_wearable_containers_for_player(player_id_uuid)

        # Try item_instance_id match first
        container_data, container_id = await try_wearable_container_service_by_instance_id(
            persistence, wearable_containers, item_instance_id, player.name
        )
        if container_data:
            return container_data, container_id

        # Fallback to name/slot match
        container_data, container_id = await try_wearable_container_service_by_name(
            persistence, wearable_containers, slot, target_lower, player.name
        )
        if container_data:
            return container_data, container_id
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container lookup errors unpredictable, fallback available
        logger.debug(
            "Error finding container via wearable container service for get command",
            error=str(e),
            player=player.name,
        )

    return None, None


def extract_items_from_container(container_found: Any, container_id: UUID | None) -> tuple[list[Any], UUID | None]:
    """
    Extract items and container ID from various container formats.

    Args:
        container_found: Container object (ContainerData, dict, or object with to_dict)
        container_id: Optional container ID

    Returns:
        Tuple of (container_items, container_id)
    """
    if hasattr(container_found, "items_json"):
        container_items = container_found.items_json or []
        if not container_id:
            container_id = container_found.container_instance_id
    elif isinstance(container_found, dict):
        container_items = container_found.get("items", [])
        if not container_id:
            container_id = UUID(container_found.get("container_id"))
    else:
        if hasattr(container_found, "to_dict"):
            container_found = container_found.to_dict()
            container_items = container_found.get("items", [])
            if not container_id:
                container_id = UUID(container_found.get("container_id"))
        else:
            container_items = []

    return container_items, container_id


def parse_json_string_items(
    container_items: Any, container_id: UUID | None, player: Player
) -> tuple[Any, UUID | None] | None:
    """
    Parse container_items if it's a JSON string.

    Args:
        container_items: Items to parse (may be JSON string)
        container_id: Container ID for logging
        player: Player for logging

    Returns:
        Parsed items and container_id, or None if parsing failed
    """
    if isinstance(container_items, str):
        try:
            container_items = json.loads(container_items)
        except (json.JSONDecodeError, ValueError) as e:
            logger.error(
                "Failed to parse container_items JSON string",
                player=player.name,
                container_id=str(container_id) if container_id else None,
                error=str(e),
                container_items=container_items,
            )
            return None
    return container_items, container_id


def filter_valid_items(container_items: list[Any], container_id: UUID | None, player: Player) -> list[dict[str, Any]]:
    """
    Filter out any non-dictionary items from container_items.

    Args:
        container_items: List of items to filter
        container_id: Container ID for logging
        player: Player for logging

    Returns:
        List of dictionary items
    """
    filtered_items = []
    for idx, item in enumerate(container_items):
        if not isinstance(item, dict):
            logger.error(
                "Non-dictionary item found in container_items",
                player=player.name,
                container_id=str(container_id) if container_id else None,
                item_index=idx,
                item_type=type(item).__name__,
                item=item,
                container_items_length=len(container_items),
            )
            continue
        filtered_items.append(item)

    if len(filtered_items) != len(container_items):
        logger.warning(
            "Filtered out non-dictionary items from container_items",
            player=player.name,
            container_id=str(container_id) if container_id else None,
            original_length=len(container_items),
            filtered_length=len(filtered_items),
        )

    return filtered_items


def parse_container_items(
    container_found: Any, container_id: UUID | None, player: Player
) -> tuple[list[dict[str, Any]], UUID | None]:
    """Parse and validate container items from various formats."""
    container_items, container_id = extract_items_from_container(container_found, container_id)

    parse_result = parse_json_string_items(container_items, container_id, player)
    if parse_result is None:
        return [], container_id
    container_items, container_id = parse_result

    if not isinstance(container_items, list):
        logger.error(
            "Container items is not a list",
            player=player.name,
            container_id=str(container_id) if container_id else None,
            container_items_type=type(container_items).__name__,
            container_items=container_items,
        )
        return [], container_id

    filtered_items = filter_valid_items(container_items, container_id, player)

    logger.debug(
        "Container items structure",
        player=player.name,
        container_id=str(container_id) if container_id else None,
        container_items_length=len(filtered_items),
        container_items_types=[type(item).__name__ for item in filtered_items[:5]],
        container_items_sample=[str(item)[:100] for item in filtered_items[:3]],
    )

    return filtered_items, container_id


def find_item_in_container(
    container_items: list[dict[str, Any]], item_name: str, _player: Player, _container_id: UUID | None
) -> tuple[dict[str, Any] | None, int | None]:
    """Find an item in container items by name or index."""
    # Try to parse as index first
    try:
        index = int(item_name)
        if 1 <= index <= len(container_items):
            item_index = index - 1
            item_found = container_items[item_index]
            return item_found, item_index
    except ValueError:
        pass

    # Search by name
    target_lower = item_name.lower()
    for idx, item in enumerate(container_items):
        item_name_check = str(item.get("item_name", item.get("name", ""))).lower()
        if target_lower in item_name_check:
            return item, idx

    return None, None


def resolve_container_id(container_found: Any, container_id: UUID | None) -> UUID | None:
    """Resolve container ID from container object."""
    if container_id:
        return container_id

    if hasattr(container_found, "container_instance_id"):
        return cast("UUID | None", container_found.container_instance_id)

    if isinstance(container_found, dict):
        return UUID(container_found.get("container_id"))

    return None


async def transfer_item_from_container(  # pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals  # Reason: Container helpers require many parameters and intermediate variables for complex item transfer logic
    container_service: Any,
    persistence: Any,
    player: Player,
    container_id: UUID,
    item_found: dict[str, Any],
    quantity: int | None,
) -> dict[str, Any]:
    """Transfer an item from container to player inventory."""
    from .inventory_command_helpers import persist_player

    player_id_uuid = UUID(str(player.player_id))
    mutation_token = container_service.get_container_token(container_id, player_id_uuid)

    if not mutation_token:
        try:
            open_result = await container_service.open_container(container_id, player_id_uuid)
            mutation_token = open_result.get("mutation_token")
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container access errors unpredictable, must return error message
            return {"error": f"Cannot access container: {str(e)}"}

    try:
        transfer_quantity = quantity if quantity else item_found.get("quantity", 1)
        result = await container_service.transfer_from_container(
            container_id=container_id,
            player_id=player_id_uuid,
            mutation_token=mutation_token,
            item=item_found,
            quantity=transfer_quantity,
        )

        new_inventory = result.get("player_inventory", player.get_inventory())
        player.set_inventory(new_inventory)
        persist_error = persist_player(persistence, player)
        if persist_error:
            return persist_error

        item_display_name = item_found.get("item_name") or item_found.get("item_id", "item")
        return {
            "success": True,
            "transfer_quantity": transfer_quantity,
            "item_display_name": item_display_name,
        }
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container operation errors unpredictable, must handle gracefully
        logger.error("Error getting item from container", player=player.name, error=str(e))
        return {"error": str(e)}


async def validate_get_command_inputs(
    command_data: dict, request: Any, connection_manager: Any
) -> tuple[str, str, int | None, Any, Any] | dict[str, str]:
    """Validate and extract inputs for get command."""
    item_name = command_data.get("item", "").strip()
    container_name = command_data.get("container", "").strip()
    quantity = command_data.get("quantity")

    if not item_name or not container_name:
        return {"result": "Usage: get <item> [from] <container> [quantity]"}

    app = getattr(request, "app", None)
    container_service = getattr(app.state, "container_service", None) if app else None
    if not container_service:
        return {"result": "Container service is unavailable."}

    room_manager = getattr(connection_manager, "room_manager", None)
    if not room_manager:
        return {"result": "Room manager is unavailable."}

    return item_name, container_name, quantity, container_service, room_manager
