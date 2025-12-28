"""Inventory and equipment command handlers for MythosMUD."""

from __future__ import annotations

import inspect
import uuid
from collections.abc import Mapping
from copy import deepcopy
from typing import Any, cast
from uuid import UUID

from ..alias_storage import AliasStorage
from ..exceptions import ValidationError as MythosValidationError
from ..structured_logging.enhanced_logging_config import get_logger
from ..models.player import Player
from ..realtime.envelope import build_event
from ..schemas.inventory_schema import InventorySchemaValidationError
from ..services.equipment_service import EquipmentCapacityError, EquipmentService, SlotValidationError
from ..services.inventory_service import (
    InventoryCapacityError,
    InventoryService,
    InventoryStack,
    InventoryValidationError,
)
from ..services.wearable_container_service import WearableContainerService
from ..utils.command_parser import get_username_from_user

logger = get_logger(__name__)

DEFAULT_SLOT_CAPACITY = 20

# Lazy-initialized shared services (initialized on first use)
_SHARED_INVENTORY_SERVICE: InventoryService | None = None
_SHARED_WEARABLE_CONTAINER_SERVICE: WearableContainerService | None = None
_SHARED_EQUIPMENT_SERVICE: EquipmentService | None = None


def _get_shared_services(request: Any) -> tuple[InventoryService, WearableContainerService, EquipmentService]:
    """
    Get shared service instances, initializing them lazily if needed.

    This ensures services are initialized with proper dependencies from the application container.

    Args:
        request: FastAPI request object to access app state

    Returns:
        Tuple of (inventory_service, wearable_container_service, equipment_service)
    """
    global _SHARED_INVENTORY_SERVICE, _SHARED_WEARABLE_CONTAINER_SERVICE, _SHARED_EQUIPMENT_SERVICE

    if _SHARED_INVENTORY_SERVICE is None:
        # Get async_persistence from container
        app = getattr(request, "app", None)
        container = getattr(app.state, "container", None) if app else None
        async_persistence = getattr(container, "async_persistence", None) if container else None

        if async_persistence is None:
            raise ValueError("async_persistence is required but not available from container")

        _SHARED_INVENTORY_SERVICE = InventoryService()
        _SHARED_WEARABLE_CONTAINER_SERVICE = WearableContainerService(persistence=async_persistence)
        _SHARED_EQUIPMENT_SERVICE = EquipmentService(
            inventory_service=_SHARED_INVENTORY_SERVICE,
            wearable_container_service=_SHARED_WEARABLE_CONTAINER_SERVICE,
        )

    # Type narrowing: After initialization, these are guaranteed to be non-None
    assert _SHARED_INVENTORY_SERVICE is not None
    assert _SHARED_WEARABLE_CONTAINER_SERVICE is not None
    assert _SHARED_EQUIPMENT_SERVICE is not None

    return _SHARED_INVENTORY_SERVICE, _SHARED_WEARABLE_CONTAINER_SERVICE, _SHARED_EQUIPMENT_SERVICE


def _match_room_drop_by_name(drop_list: list[dict[str, Any]], search_term: str) -> int | None:
    """
    Resolve a room drop index using Lovecraftian-grade fuzzy matching heuristics.

    Human collaborators: we prefer exact identifiers, then courteous prefix matches, before falling back
    to substring containment—echoing the cataloguing rites described in Dr. Wilmarth's Restricted Archives.
    Agentic aides: return a zero-based index for the best candidate or None if no alignment is found.
    """

    normalized = search_term.strip().lower()
    if not normalized:
        return None

    def _extract(stack: dict[str, Any], key: str) -> str | None:
        value = stack.get(key)
        if isinstance(value, str):
            stripped = value.strip()
            return stripped if stripped else None
        return None

    candidates: list[tuple[int, str | None, str | None, str | None]] = []
    for idx, stack in enumerate(drop_list):
        item_name = _extract(stack, "item_name")
        item_id = _extract(stack, "item_id")
        prototype_id = _extract(stack, "prototype_id")
        candidates.append((idx, item_name, item_id, prototype_id))

    for idx, item_name, item_id, prototype_id in candidates:
        for candidate in (item_name, item_id, prototype_id):
            if candidate and candidate.lower() == normalized:
                return idx

    for idx, item_name, _item_id, _prototype_id in candidates:
        if item_name and item_name.lower().startswith(normalized):
            return idx

    for idx, _item_name, item_id, prototype_id in candidates:
        for candidate in (item_id, prototype_id):
            if candidate and candidate.lower().startswith(normalized):
                return idx

    for idx, item_name, item_id, prototype_id in candidates:
        for candidate in (item_name, item_id, prototype_id):
            if candidate and normalized in candidate.lower():
                return idx

    return None


def _match_inventory_item_by_name(inventory: list[dict[str, Any]], search_term: str) -> int | None:
    """
    Resolve an inventory index from a fuzzy name search.

    Human scholars: this mirrors the ritual we employ for room drops, prioritising exact designations
    before leaning on sympathetic naming. Agentic aides: return a zero-based index when the augury aligns,
    otherwise yield None.
    """

    normalized = search_term.strip().lower()
    if not normalized:
        return None

    def _extract(stack: dict[str, Any], key: str) -> str | None:
        value = stack.get(key)
        if isinstance(value, str):
            stripped = value.strip()
            return stripped if stripped else None
        return None

    candidates: list[tuple[int, str | None, str | None, str | None]] = []
    for idx, stack in enumerate(inventory):
        item_name = _extract(stack, "item_name")
        item_id = _extract(stack, "item_id")
        prototype_id = _extract(stack, "prototype_id")
        candidates.append((idx, item_name, item_id, prototype_id))

    for idx, item_name, item_id, prototype_id in candidates:
        for candidate in (item_name, item_id, prototype_id):
            if candidate and candidate.lower() == normalized:
                return idx

    for idx, item_name, _item_id, _prototype_id in candidates:
        if item_name and item_name.lower().startswith(normalized):
            return idx

    for idx, _item_name, item_id, prototype_id in candidates:
        for candidate in (item_id, prototype_id):
            if candidate and candidate.lower().startswith(normalized):
                return idx

    for idx, item_name, item_id, prototype_id in candidates:
        for candidate in (item_name, item_id, prototype_id):
            if candidate and normalized in candidate.lower():
                return idx

    return None


def _normalize_slot_name(slot: str | None) -> str | None:
    """Normalize equipment slot identifiers to lowercase snake_case."""

    if slot is None:
        return None
    normalized = slot.strip().lower()
    return normalized or None


def _match_equipped_item_by_name(equipped: Mapping[str, Mapping[str, Any]], search_term: str) -> str | None:
    """
    Resolve an equipped slot identifier via fuzzy item name search.

    Scholars: we invoke the same sympathetic naming rites used for inventory and room drops.
    Agents: return the normalized slot key when a match is found; otherwise None.
    """

    normalized_term = search_term.strip().lower()
    if not normalized_term:
        return None

    candidates: list[tuple[str, str | None, str | None, str | None]] = []
    for slot_name, stack in equipped.items():
        item_name = stack.get("item_name")
        item_id = stack.get("item_id")
        prototype_id = stack.get("prototype_id")

        def _clean(value: str | None) -> str | None:
            if isinstance(value, str):
                stripped = value.strip()
                return stripped if stripped else None
            return None

        candidates.append(
            (
                _normalize_slot_name(slot_name) or slot_name,
                _clean(item_name),
                _clean(item_id),
                _clean(prototype_id),
            )
        )

    for slot_key, item_name, item_id, prototype_id in candidates:
        for candidate in (item_name, item_id, prototype_id):
            if candidate and candidate.lower() == normalized_term:
                return slot_key

    for slot_key, item_name, item_id, prototype_id in candidates:
        for candidate in (item_name, item_id, prototype_id):
            if candidate and candidate.lower().startswith(normalized_term):
                return slot_key

    for slot_key, item_name, item_id, prototype_id in candidates:
        for candidate in (item_name, item_id, prototype_id):
            if candidate and normalized_term in candidate.lower():
                return slot_key

    return None


def _resolve_state(request: Any) -> tuple[Any, Any]:
    app = getattr(request, "app", None)
    state = getattr(app, "state", None)
    persistence = getattr(state, "persistence", None)
    connection_manager = getattr(state, "connection_manager", None)
    return persistence, connection_manager


async def _resolve_player(
    persistence: Any,
    current_user: dict,
    fallback_player_name: str,
) -> tuple[Player | None, dict[str, str] | None]:
    if not persistence:
        logger.warning("Command invoked without persistence layer", player=fallback_player_name)
        return None, {"result": "Inventory information is not available."}

    try:
        username = get_username_from_user(current_user)
    except MythosValidationError as exc:
        logger.warning("Failed to resolve username for inventory command", player=fallback_player_name, error=str(exc))
        return None, {"result": str(exc)}

    try:
        player = await persistence.get_player_by_name(username)
    except Exception as exc:  # pragma: no cover - defensive logging path
        logger.error("Persistence error resolving player", player=username, error=str(exc))
        return None, {"result": f"Error resolving player: {str(exc)}"}

    if not player:
        logger.warning("Player not found when handling inventory command", player=username)
        return None, {"result": "Player information not found."}

    return player, None


def _format_metadata(metadata: Mapping[str, Any] | None) -> str:
    if not metadata:
        return ""
    try:
        components = []
        for key, value in sorted(metadata.items()):
            # Handle nested dicts (like container dict) by using repr() explicitly
            if isinstance(value, dict):
                components.append(f"{key}={value!r}")
            else:
                components.append(f"{key}={value}")
        if components:
            return f" [{', '.join(components)}]"
    except Exception as exc:  # pragma: no cover - metadata formatting should rarely fail
        logger.error("Failed to format metadata", error=str(exc), metadata=metadata, exc_info=True)
    return ""


def _render_inventory(
    inventory: list[dict[str, Any]],
    equipped: dict[str, Any],
    container_contents: dict[str, list[dict[str, Any]]] | None = None,
    container_capacities: dict[str, int] | None = None,
    container_lock_states: dict[str, str] | None = None,
) -> str:
    # Filter out equipped items from inventory slot calculation
    # Create a set of equipped item identifiers for efficient lookup
    equipped_item_ids: set[str] = set()
    equipped_item_instance_ids: set[str] = set()
    for equipped_item in equipped.values():
        item_id = equipped_item.get("item_id")
        item_instance_id = equipped_item.get("item_instance_id")
        if item_id:
            equipped_item_ids.add(str(item_id))
        if item_instance_id:
            equipped_item_instance_ids.add(str(item_instance_id))

    # Count only non-equipped items and items not in containers for regular inventory slots
    non_equipped_inventory = []
    for stack in inventory:
        stack_item_id = stack.get("item_id")
        stack_item_instance_id = stack.get("item_instance_id")
        slot_type = stack.get("slot_type", "unknown")
        # Check if this item is equipped by comparing item_id or item_instance_id
        is_equipped = False
        if stack_item_instance_id and str(stack_item_instance_id) in equipped_item_instance_ids:
            is_equipped = True
        elif stack_item_id and str(stack_item_id) in equipped_item_ids:
            is_equipped = True
        # Items stored in containers (e.g., slot_type='backpack') should not count toward regular inventory
        is_in_container = slot_type != "unknown" and slot_type != "inventory"
        if not is_equipped and not is_in_container:
            non_equipped_inventory.append(stack)

    slots_used = len(non_equipped_inventory)
    remaining = max(DEFAULT_SLOT_CAPACITY - slots_used, 0)

    lines: list[str] = [
        f"You are carrying {slots_used} / {DEFAULT_SLOT_CAPACITY} slots. Remaining capacity: {remaining}."
    ]

    if inventory:
        for index, stack in enumerate(inventory, start=1):
            item_name = stack.get("item_name") or stack.get("item_id", "Unknown Item")
            slot_type = stack.get("slot_type", "unknown")
            quantity = stack.get("quantity", 0)
            metadata_suffix = _format_metadata(stack.get("metadata"))
            lines.append(f"{index}. {item_name} ({slot_type}) x{quantity}{metadata_suffix}")
    else:
        lines.append("No items in your pockets or on your person.")

    lines.append("")
    lines.append("Equipped:")

    if equipped:
        for slot_name in sorted(equipped.keys()):
            item = equipped[slot_name]
            item_name = item.get("item_name") or item.get("item_id", "Unknown Item")
            quantity = item.get("quantity", 0)

            # Check if this slot has a container and update metadata with slot usage
            item_metadata = item.get("metadata") or {}
            logger.debug(
                "Processing equipped item",
                slot_name=slot_name,
                item_metadata=item_metadata,
                has_container_in_metadata="container" in item_metadata,
            )
            if container_contents is not None and slot_name in container_contents:
                container_items = container_contents[slot_name]
                container_capacity = container_capacities.get(slot_name, 20) if container_capacities else 20
                container_lock_state = (
                    container_lock_states.get(slot_name, "unlocked") if container_lock_states else "unlocked"
                )
                container_slots_used = len(container_items)

                # Create a fresh container dict with slot usage info (don't merge with existing)
                container_dict = {
                    "lock_state": container_lock_state,
                    "capacity_slots": container_capacity,
                    "slots_in_use": container_slots_used,
                }
                # Ensure slots_in_use is actually set (debug check)
                if "slots_in_use" not in container_dict:
                    logger.error("CRITICAL: slots_in_use missing from container_dict!", container_dict=container_dict)
                logger.debug(
                    "Container dict created",
                    container_dict=container_dict,
                    container_slots_used=container_slots_used,
                    container_items_count=len(container_items),
                    slots_in_use_in_dict="slots_in_use" in container_dict,
                )
                # Create a new metadata dict, ensuring container is our new dict
                updated_metadata = {}
                # Copy all non-container metadata
                for key, value in item_metadata.items():
                    if key != "container":
                        updated_metadata[key] = value
                # Set the container with our new dict that includes slots_in_use
                updated_metadata["container"] = container_dict
                logger.debug(
                    "Updated metadata before formatting",
                    updated_metadata=updated_metadata,
                    container_in_metadata=updated_metadata.get("container"),
                )
                # Format the updated metadata - this will include slots_in_use in the container dict
                # Verify container_dict has slots_in_use before formatting
                if "container" in updated_metadata:
                    container_check = updated_metadata["container"]
                    logger.info(
                        "About to format metadata",
                        container_dict=container_check,
                        has_slots_in_use="slots_in_use" in container_check
                        if isinstance(container_check, dict)
                        else False,
                        container_dict_keys=list(container_check.keys()) if isinstance(container_check, dict) else None,
                    )
                metadata_suffix = _format_metadata(updated_metadata)
                logger.info("Formatted metadata suffix", metadata_suffix=metadata_suffix)
            else:
                # No container, use original metadata
                metadata_suffix = _format_metadata(item_metadata)

            # Append the equipped item line with the formatted metadata
            lines.append(f"- {slot_name}: {item_name} x{quantity}{metadata_suffix}")

            # Show container contents if this slot has a container
            if container_contents is not None and slot_name in container_contents:
                container_items = container_contents[slot_name]

                if container_items:
                    for container_item in container_items:
                        container_item_name = container_item.get("item_name") or container_item.get(
                            "name", "Unknown Item"
                        )
                        container_item_quantity = container_item.get("quantity", 1)
                        if container_item_quantity > 1:
                            lines.append(f"    - {container_item_name} x{container_item_quantity}")
                        else:
                            lines.append(f"    - {container_item_name}")
    else:
        lines.append("- Nothing equipped.")

    return "\n".join(lines)


def _clone_inventory(player: Player) -> list[dict[str, Any]]:
    return deepcopy(player.get_inventory())


async def _broadcast_room_event(
    connection_manager: Any,
    room_id: str,
    event: dict[str, Any],
    *,
    exclude_player: str | None = None,
) -> None:
    if not connection_manager or not hasattr(connection_manager, "broadcast_to_room"):
        return

    try:
        result = connection_manager.broadcast_to_room(str(room_id), event, exclude_player=exclude_player)
        if inspect.isawaitable(result):
            await result
    except Exception as exc:  # pragma: no cover - broadcast failures logged but not fatal
        logger.warning("Failed to broadcast room event", room_id=room_id, error=str(exc))


def _persist_player(persistence: Any, player: Player) -> dict[str, str] | None:
    try:
        persistence.save_player(player)
        return None
    except InventorySchemaValidationError as exc:
        logger.error("Inventory schema validation during persistence", player=player.name, error=str(exc))
        return {"result": "Inventory data rejected by schema validation."}
    except Exception as exc:  # pragma: no cover - defensive logging path
        logger.error("Error saving player inventory", player=player.name, error=str(exc))
        return {"result": "An error occurred while saving your inventory."}


async def handle_inventory_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, Any]:
    """Display the player's inventory and equipped items, including container contents."""

    persistence, _connection_manager = _resolve_state(request)
    player, error = await _resolve_player(persistence, current_user, player_name)
    if error or not player:
        return error or {"result": "Player information not found."}

    inventory_view = player.get_inventory()
    equipped_view = player.get_equipped_items()

    # Get container contents, capacity, and lock state for equipped containers
    # Key by slot name to match with equipped items
    container_contents: dict[str, list[dict[str, Any]]] = {}
    container_capacities: dict[str, int] = {}
    container_lock_states: dict[str, str] = {}
    try:
        _, wearable_container_service, _ = _get_shared_services(request)
        player_id_uuid = UUID(str(player.player_id))
        wearable_containers = await wearable_container_service.get_wearable_containers_for_player(player_id_uuid)
        logger.debug(
            "Getting container contents",
            player_id=str(player_id_uuid),
            wearable_containers_count=len(wearable_containers),
            equipped_slots=list(equipped_view.keys()),
        )
        # Match containers to equipped items by item_name or item_id
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

            # Find matching slot in equipped items
            matching_slot = None
            for slot_name, equipped_item in equipped_view.items():
                equipped_item_name = equipped_item.get("item_name")
                equipped_item_id = equipped_item.get("item_id")
                if (container_item_name and equipped_item_name and container_item_name == equipped_item_name) or (
                    container_item_id and equipped_item_id and container_item_id == equipped_item_id
                ):
                    matching_slot = slot_name
                    logger.debug(
                        "Found matching slot",
                        matching_slot=slot_name,
                        container_item_name=container_item_name,
                        equipped_item_name=equipped_item_name,
                    )
                    break

            if matching_slot:
                # Store container capacity and lock state
                container_capacities[matching_slot] = container_component.capacity_slots
                # Get lock_state enum value as string
                lock_state = container_component.lock_state
                if hasattr(lock_state, "value"):
                    container_lock_states[matching_slot] = lock_state.value
                else:
                    container_lock_states[matching_slot] = str(lock_state)
                # Convert InventoryStack objects to dictionaries for display
                # InventoryStack is a TypedDict, so it's already dict-like, but we need to cast for mypy
                # ALWAYS set container_contents, even if empty, so we can calculate slots_in_use
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
            else:
                logger.debug(
                    "No matching slot found for container",
                    container_item_name=container_item_name,
                    container_item_id=container_item_id,
                    equipped_slots=list(equipped_view.keys()),
                )
    except Exception as e:
        logger.debug(
            "Error getting container contents for inventory display",
            error=str(e),
            player=player.name,
        )

    # Update equipped items' metadata to include slots_in_use for containers
    for slot_name, equipped_item in equipped_view.items():
        if slot_name in container_contents:
            container_items = container_contents[slot_name]
            container_slots_used = len(container_items)
            # Ensure metadata exists
            if "metadata" not in equipped_item:
                equipped_item["metadata"] = {}
            # Ensure container dict exists in metadata
            if "container" not in equipped_item["metadata"]:
                equipped_item["metadata"]["container"] = {}
            # Update container dict with slots_in_use
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

    logger.info(
        "Inventory displayed",
        player=player.name,
        slots_used=len(inventory_view),
        equipped_slots=len(equipped_view),
        containers_with_items=len(container_contents),
    )
    return {
        "result": _render_inventory(
            inventory_view, equipped_view, container_contents, container_capacities, container_lock_states
        ),
        "inventory": deepcopy(inventory_view),
        "equipped": deepcopy(equipped_view),
    }


async def handle_pickup_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, Any]:
    """Move an item stack from room drops into the player's inventory."""

    persistence, connection_manager = _resolve_state(request)
    player, error = await _resolve_player(persistence, current_user, player_name)
    if error or not player:
        return error or {"result": "Player information not found."}

    room_manager = getattr(connection_manager, "room_manager", None)
    if not room_manager:
        logger.warning(
            "Pickup attempted without room manager",
            player=player.name,
            # Structlog handles UUID objects automatically, no need to convert to string
            player_id=player.player_id,
            room_id=player.current_room_id,
        )
        return {"result": "Room inventory is unavailable."}

    desired_quantity = command_data.get("quantity")
    room_id = str(player.current_room_id)
    drop_list = room_manager.list_room_drops(room_id)

    index = command_data.get("index")
    search_term = command_data.get("search_term")
    resolved_index_zero: int | None = None

    if isinstance(index, int) and index >= 1:
        if index > len(drop_list):
            return {"result": "There is no such item to pick up."}
        resolved_index_zero = index - 1
    elif isinstance(search_term, str) and search_term.strip():
        match_index = _match_room_drop_by_name(drop_list, search_term)
        if match_index is None:
            logger.info(
                "No matching room drop found for pickup",
                player=player.name,
                # Structlog handles UUID objects automatically, no need to convert to string
                player_id=player.player_id,
                search_term=search_term,
                room_id=room_id,
            )
            return {"result": f"There is no item here matching '{search_term}'."}
        resolved_index_zero = match_index
        index = match_index + 1
        logger.debug(
            "Pickup resolved via fuzzy search",
            player=player.name,
            # Structlog handles UUID objects automatically, no need to convert to string
            player_id=player.player_id,
            room_id=room_id,
            search_term=search_term,
            resolved_index=index,
        )
    else:
        return {"result": "Usage: pickup <item-number|item-name> [quantity]"}

    if desired_quantity is None:
        desired_quantity = int(drop_list[resolved_index_zero].get("quantity", 1))
    if desired_quantity <= 0:
        return {"result": "Quantity must be a positive number."}

    extracted_stack = room_manager.take_room_drop(room_id, resolved_index_zero, desired_quantity)
    if not extracted_stack:
        return {"result": "That item is no longer available."}

    # Items picked up from the ground should go into general inventory,
    # not into equipped slots, even if they're equippable items.
    # Do NOT set slot_type='backpack' - items should only have slot_type='backpack'
    # when explicitly placed into containers via the 'put' command.
    # The slot_type is only preserved when removing items from containers
    # (if they were equipped before being put in the container).
    logger.debug(
        "Pickup: extracted_stack before processing",
        player=player.name,
        player_id=str(player.player_id),
        extracted_stack_type=type(extracted_stack).__name__,
        extracted_stack_keys=list(extracted_stack.keys()) if isinstance(extracted_stack, dict) else None,
        original_slot_type=extracted_stack.get("slot_type") if isinstance(extracted_stack, dict) else None,
    )
    if isinstance(extracted_stack, dict):
        extracted_stack = dict(extracted_stack)  # Create a copy to avoid mutating the original
        # Do NOT set slot_type - items go to general inventory
        # slot_type is only set when items are explicitly put into containers via 'put' command
        logger.debug(
            "Pickup: item will be added to general inventory",
            player=player.name,
            player_id=str(player.player_id),
            item_id=extracted_stack.get("item_id"),
            item_name=extracted_stack.get("item_name"),
        )

    # Ensure the item instance exists in the database for referential integrity
    # This is required for container operations and other systems that reference item_instances
    item_instance_id = extracted_stack.get("item_instance_id") if isinstance(extracted_stack, dict) else None
    prototype_id = (
        extracted_stack.get("prototype_id") or extracted_stack.get("item_id")
        if isinstance(extracted_stack, dict)
        else None
    )
    if item_instance_id and prototype_id:
        try:
            persistence.ensure_item_instance(
                item_instance_id=item_instance_id,
                prototype_id=prototype_id,
                owner_type="player",
                owner_id=str(player.player_id),
                quantity=extracted_stack.get("quantity", 1) if isinstance(extracted_stack, dict) else 1,
                metadata=extracted_stack.get("metadata") if isinstance(extracted_stack, dict) else None,
                origin_source="pickup",
                origin_metadata={"room_id": room_id} if isinstance(extracted_stack, dict) else None,
            )
            logger.debug(
                "Item instance ensured for picked up item",
                item_instance_id=item_instance_id,
                prototype_id=prototype_id,
                player_id=str(player.player_id),
            )
        except Exception as e:
            logger.warning(
                "Failed to ensure item instance for picked up item",
                item_instance_id=item_instance_id,
                prototype_id=prototype_id,
                error=str(e),
            )
            # Continue anyway - the item will still be added to inventory
            # but container operations may fail if the item instance doesn't exist

    previous_inventory = _clone_inventory(player)
    inventory_service = InventoryService()

    try:
        updated_inventory = inventory_service.add_stack(previous_inventory, extracted_stack)
    except (InventoryCapacityError, InventoryValidationError) as exc:
        room_manager.add_room_drop(room_id, extracted_stack)
        logger.info(
            "Pickup rejected",
            player=player.name,
            # Structlog handles UUID objects automatically, no need to convert to string
            player_id=player.player_id,
            reason=str(exc),
            room_id=room_id,
        )
        return {"result": f"You cannot pick that up: {str(exc)}"}

    player.set_inventory(cast(list[dict[str, Any]], updated_inventory))
    # Log inventory contents after set_inventory to verify item was added
    logger.info(
        "Pickup: inventory after set_inventory",
        player=player.name,
        player_id=str(player.player_id),
        inventory_length=len(updated_inventory),
        inventory_items=[
            {
                "item_name": item.get("item_name"),
                "item_id": item.get("item_id"),
                "slot_type": item.get("slot_type"),
                "quantity": item.get("quantity"),
            }
            for item in updated_inventory
        ],
    )
    persist_error = _persist_player(persistence, player)
    if persist_error:
        room_manager.add_room_drop(room_id, extracted_stack)
        player.set_inventory(previous_inventory)
        return persist_error

    quantity = extracted_stack.get("quantity", desired_quantity)
    item_name = extracted_stack.get("item_name") or extracted_stack.get("item_id", "item")

    event = build_event(
        "inventory_pickup",
        {
            "player_name": player.name,
            "item_id": extracted_stack.get("item_id"),
            "item_name": item_name,
            "quantity": quantity,
        },
        room_id=room_id,
        player_id=str(player.player_id),
        connection_manager=connection_manager,
    )

    await _broadcast_room_event(
        connection_manager,
        room_id,
        event,
        exclude_player=str(player.player_id) if getattr(player, "player_id", None) else None,
    )

    logger.info(
        "Item picked up",
        player=player.name,
        player_id=str(player.player_id),
        item_id=extracted_stack.get("item_id"),
        quantity=quantity,
        room_id=room_id,
    )
    return {
        "result": f"You pick up {quantity}x {item_name}.",
        "room_message": f"{player.name} picks up {quantity}x {item_name}.",
        "game_log_message": f"{player.name} picked up {quantity}x {item_name}",
        "game_log_channel": "game-log",
    }


async def handle_drop_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, Any]:
    """Drop an inventory stack into the current room."""

    persistence, connection_manager = _resolve_state(request)
    player, error = await _resolve_player(persistence, current_user, player_name)
    if error or not player:
        return error or {"result": "Player information not found."}

    room_manager = getattr(connection_manager, "room_manager", None)
    if not room_manager:
        logger.warning(
            "Drop attempted without room manager",
            player=player.name,
            # Structlog handles UUID objects automatically, no need to convert to string
            player_id=player.player_id,
            room_id=player.current_room_id,
        )
        return {"result": "Room inventory is unavailable."}

    room_id = str(player.current_room_id)
    index = command_data.get("index")
    if not isinstance(index, int) or index < 1:
        return {"result": "Usage: drop <inventory-number> [quantity]"}

    current_inventory = player.get_inventory()
    if index > len(current_inventory):
        return {"result": "You do not have an item in that slot."}

    stack = deepcopy(current_inventory[index - 1])
    quantity = command_data.get("quantity") or int(stack.get("quantity", 1))
    if quantity <= 0:
        return {"result": "Quantity must be a positive number."}
    if quantity > stack.get("quantity", 1):
        return {"result": "You do not have that many to drop."}

    previous_inventory = _clone_inventory(player)

    if quantity == stack.get("quantity", 1):
        updated_inventory = previous_inventory[: index - 1] + previous_inventory[index:]
    else:
        updated_inventory = deepcopy(previous_inventory)
        updated_inventory[index - 1]["quantity"] = previous_inventory[index - 1]["quantity"] - quantity

    player.set_inventory(updated_inventory)

    drop_stack = deepcopy(stack)
    drop_stack["quantity"] = quantity

    persist_error = _persist_player(persistence, player)
    if persist_error:
        player.set_inventory(previous_inventory)
        return persist_error

    room_manager.add_room_drop(room_id, drop_stack)

    item_name = drop_stack.get("item_name") or drop_stack.get("item_id", "item")

    event = build_event(
        "inventory_drop",
        {
            "player_name": player.name,
            "item_id": drop_stack.get("item_id"),
            "item_name": item_name,
            "quantity": quantity,
        },
        room_id=room_id,
        player_id=str(player.player_id),
        connection_manager=connection_manager,
    )

    await _broadcast_room_event(
        connection_manager,
        room_id,
        event,
        exclude_player=str(player.player_id) if getattr(player, "player_id", None) else None,
    )

    logger.info(
        "Item dropped",
        player=player.name,
        player_id=str(player.player_id),
        item_id=drop_stack.get("item_id"),
        quantity=quantity,
        room_id=room_id,
    )
    return {
        "result": f"You drop {quantity}x {item_name}.",
        "room_message": f"{player.name} drops {quantity}x {item_name}.",
        "game_log_message": f"{player.name} dropped {quantity}x {item_name}",
        "game_log_channel": "game-log",
    }


async def handle_equip_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, Any]:
    """Equip an item from inventory."""

    persistence, connection_manager = _resolve_state(request)
    player, error = await _resolve_player(persistence, current_user, player_name)
    if error or not player:
        return error or {"result": "Player information not found."}

    inventory = player.get_inventory()
    for stack_entry in inventory:
        if isinstance(stack_entry, dict):
            current_slot = stack_entry.get("slot_type")
            normalized_slot = _normalize_slot_name(current_slot)
            if normalized_slot:
                stack_entry["slot_type"] = normalized_slot

    room_id = str(player.current_room_id)
    index = command_data.get("index")
    search_term = command_data.get("search_term")
    target_slot = _normalize_slot_name(command_data.get("target_slot"))

    resolved_index_zero: int | None = None

    if isinstance(index, int) and index >= 1:
        if index > len(inventory):
            return {"result": "You do not have an item in that slot."}
        resolved_index_zero = index - 1
    elif isinstance(search_term, str) and search_term.strip():
        match_index = _match_inventory_item_by_name(inventory, search_term)
        if match_index is None:
            logger.info(
                "No matching inventory item found for equip",
                player=player.name,
                # Structlog handles UUID objects automatically, no need to convert to string
                player_id=player.player_id,
                search_term=search_term,
                room_id=room_id,
            )
            return {"result": f"You do not have an item matching '{search_term}'."}
        resolved_index_zero = match_index
        logger.debug(
            "Equip resolved via fuzzy search",
            player=player.name,
            # Structlog handles UUID objects automatically, no need to convert to string
            player_id=player.player_id,
            room_id=room_id,
            search_term=search_term,
            inventory_index=match_index + 1,
        )
    else:
        return {"result": "Usage: equip <inventory-number|item-name> [slot]"}

    selected_stack = deepcopy(inventory[resolved_index_zero])
    if isinstance(selected_stack, dict):
        normalized_selected_slot = _normalize_slot_name(selected_stack.get("slot_type"))
        if normalized_selected_slot:
            selected_stack["slot_type"] = normalized_selected_slot

    inventory_service, wearable_container_service, equipment_service = _get_shared_services(request)
    mutation_token = command_data.get("mutation_token")

    previous_inventory = _clone_inventory(player)
    previous_equipped = deepcopy(player.get_equipped_items())

    # Convert player.player_id to UUID | str for begin_mutation
    # SQLAlchemy Column[str] returns UUID at runtime, but mypy sees it as Column[str]
    # begin_mutation accepts UUID | str, so convert to string and let it handle
    player_id_value = player.player_id
    player_id_for_mutation: uuid.UUID | str = str(player_id_value)
    with inventory_service.begin_mutation(player_id_for_mutation, mutation_token) as decision:
        if not decision.should_apply:
            logger.info(
                "Equip suppressed by mutation guard",
                player=player.name,
                # Structlog handles UUID objects automatically, no need to convert to string
                player_id=player.player_id,
                requested_slot=target_slot,
                inventory_index=index,
                room_id=room_id,
                mutation_token=mutation_token,
            )
            return {"result": "That action is already being processed."}

        try:
            new_inventory, new_equipped = equipment_service.equip_from_inventory(
                inventory,
                player.get_equipped_items(),
                slot_index=resolved_index_zero,
                target_slot=target_slot,
            )
        except (SlotValidationError, EquipmentCapacityError, InventoryCapacityError) as exc:
            logger.info(
                "Equip rejected",
                player=player.name,
                # Structlog handles UUID objects automatically, no need to convert to string
                player_id=player.player_id,
                reason=str(exc),
                requested_slot=target_slot,
                inventory_index=index,
                room_id=room_id,
            )
            return {"result": str(exc)}

        for stack in new_inventory:
            if isinstance(stack, dict):
                normalized_stack_slot = _normalize_slot_name(stack.get("slot_type"))
                if normalized_stack_slot:
                    stack["slot_type"] = normalized_stack_slot

        normalized_equipped: dict[str, InventoryStack] = {}
        for slot_name, stack in new_equipped.items():
            normalized_slot_name = _normalize_slot_name(slot_name) or slot_name
            if isinstance(stack, dict):
                normalized_stack_slot = _normalize_slot_name(stack.get("slot_type"))
                if normalized_stack_slot:
                    stack["slot_type"] = normalized_stack_slot
            normalized_equipped[normalized_slot_name] = stack

        # Convert InventoryStack to dict[str, Any] for set_inventory
        player.set_inventory([cast(dict[str, Any], stack) for stack in new_inventory])
        player.set_equipped_items(cast(dict[str, Any], normalized_equipped))

        persist_error = _persist_player(persistence, player)
        if persist_error:
            player.set_inventory(previous_inventory)
            player.set_equipped_items(previous_equipped)
            return persist_error

    equipped_slot: str | None = None
    equipped_item: InventoryStack | None = None

    preferred_slot = target_slot or selected_stack.get("slot_type")
    equipped_mapping = player.get_equipped_items()

    if preferred_slot and preferred_slot in equipped_mapping:
        equipped_slot = preferred_slot
        equipped_item = equipped_mapping.get(preferred_slot)
    else:
        for slot_name, item in equipped_mapping.items():
            if item.get("item_id") == selected_stack.get("item_id"):
                equipped_slot = slot_name
                equipped_item = item
                break

    if equipped_slot is None:
        equipped_slot = preferred_slot or next(iter(equipped_mapping.keys()), "unknown")

    # Handle wearable container creation if this is a container item
    if equipped_item and equipped_item.get("inner_container"):
        try:
            _, wearable_container_service, _ = _get_shared_services(request)
            container_result = await wearable_container_service.handle_equip_wearable_container(
                player_id=UUID(str(player.player_id)),
                item_stack=cast(dict[str, Any], equipped_item),
            )
            if container_result:
                logger.debug(
                    "Wearable container created on equip",
                    player_id=player.player_id,
                    item_id=equipped_item.get("item_id"),
                    container_id=container_result.get("container_id"),
                )
        except Exception as e:
            # Log but don't fail - container creation is not critical
            logger.warning(
                "Failed to create wearable container on equip",
                error=str(e),
                player_id=player.player_id,
                item_id=equipped_item.get("item_id"),
            )

    fallback_item: dict[str, Any] = {}
    item_payload: dict[str, Any] = cast(dict[str, Any], equipped_item) if equipped_item is not None else fallback_item

    item_name = item_payload.get("item_name") or item_payload.get("item_id", "item")

    event = build_event(
        "inventory_equip",
        {
            "player_name": player.name,
            "item_id": item_payload.get("item_id"),
            "item_name": item_name,
            "slot": equipped_slot,
        },
        room_id=room_id,
        player_id=str(player.player_id),
        connection_manager=connection_manager,
    )

    await _broadcast_room_event(
        connection_manager,
        room_id,
        event,
        exclude_player=str(player.player_id) if getattr(player, "player_id", None) else None,
    )

    logger.info(
        "Item equipped",
        player=player.name,
        player_id=str(player.player_id),
        item_id=item_payload.get("item_id"),
        slot=equipped_slot,
        room_id=room_id,
        mutation_token=mutation_token,
    )
    return {
        "result": f"You equip {item_name}.",
        "room_message": f"{player.name} equips {item_name}.",
        "game_log_message": f"{player.name} equipped {item_name}",
        "game_log_channel": "game-log",
    }


async def handle_unequip_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, Any]:
    """Unequip an item into the player's inventory."""

    persistence, connection_manager = _resolve_state(request)
    player, error = await _resolve_player(persistence, current_user, player_name)
    if error or not player:
        return error or {"result": "Player information not found."}

    slot = command_data.get("slot")
    search_term = command_data.get("search_term")
    normalized_slot = _normalize_slot_name(slot) if isinstance(slot, str) else None

    if normalized_slot is None and not (isinstance(search_term, str) and search_term.strip()):
        return {"result": "Usage: unequip <slot|item-name>"}

    inventory_service, wearable_container_service, equipment_service = _get_shared_services(request)
    mutation_token = command_data.get("mutation_token")

    previous_inventory = _clone_inventory(player)
    previous_equipped = deepcopy(player.get_equipped_items())
    equipped_mapping = player.get_equipped_items()

    resolved_slot: str | None = None
    if normalized_slot and normalized_slot in equipped_mapping:
        resolved_slot = normalized_slot

    if resolved_slot is None and isinstance(search_term, str) and search_term.strip():
        match_slot = _match_equipped_item_by_name(equipped_mapping, search_term)
        if match_slot is None:
            return {"result": f"You do not have an equipped item matching '{search_term}'."}
        resolved_slot = match_slot

    if resolved_slot is None:
        return {"result": "You do not have an item equipped in that slot."}

    # Convert player.player_id to UUID | str for begin_mutation
    # SQLAlchemy Column[str] returns UUID at runtime, but mypy sees it as Column[str]
    # begin_mutation accepts UUID | str, so convert to string and let it handle
    player_id_value = player.player_id
    player_id_for_mutation: uuid.UUID | str = str(player_id_value)
    with inventory_service.begin_mutation(player_id_for_mutation, mutation_token) as decision:
        if not decision.should_apply:
            logger.info(
                "Unequip suppressed by mutation guard",
                player=player.name,
                # Structlog handles UUID objects automatically, no need to convert to string
                player_id=player.player_id,
                slot=resolved_slot,
                room_id=str(player.current_room_id),
                mutation_token=mutation_token,
            )
            return {"result": "That action is already being processed."}

        try:
            new_inventory, new_equipped = equipment_service.unequip_to_inventory(
                player.get_inventory(),
                player.get_equipped_items(),
                slot_type=resolved_slot,
            )
        except (SlotValidationError, EquipmentCapacityError, InventoryCapacityError) as exc:
            logger.info(
                "Unequip rejected",
                player=player.name,
                # Structlog handles UUID objects automatically, no need to convert to string
                player_id=player.player_id,
                reason=str(exc),
                slot=resolved_slot,
                room_id=str(player.current_room_id),
            )
            return {"result": str(exc)}

        for stack_entry in new_inventory:
            if isinstance(stack_entry, dict):
                normalized_stack_slot = _normalize_slot_name(stack_entry.get("slot_type"))
                if normalized_stack_slot:
                    stack_entry["slot_type"] = normalized_stack_slot

        normalized_equipped: dict[str, InventoryStack] = {}
        for slot_name, stack in new_equipped.items():
            normalized_slot_name = _normalize_slot_name(slot_name) or slot_name
            if isinstance(stack, dict):
                normalized_stack_slot = _normalize_slot_name(stack.get("slot_type"))
                if normalized_stack_slot:
                    stack["slot_type"] = normalized_stack_slot
            normalized_equipped[normalized_slot_name] = stack

        # Convert InventoryStack to dict[str, Any] for set_inventory
        player.set_inventory([cast(dict[str, Any], stack) for stack in new_inventory])
        player.set_equipped_items(cast(dict[str, Any], normalized_equipped))

        persist_error = _persist_player(persistence, player)
        if persist_error:
            player.set_inventory(previous_inventory)
            player.set_equipped_items(previous_equipped)
            return persist_error

    unequipped_item = previous_equipped.get(resolved_slot, {})

    # Handle wearable container preservation if this is a container item
    if unequipped_item.get("inner_container"):
        try:
            _, wearable_container_service, _ = _get_shared_services(request)
            container_result = await wearable_container_service.handle_unequip_wearable_container(
                player_id=UUID(str(player.player_id)),
                item_stack=cast(dict[str, Any], unequipped_item),
            )
            if container_result:
                # Update inventory item with preserved inner_container
                # Find the item in inventory and update it
                inventory_view = player.get_inventory()
                for inv_item in inventory_view:
                    if inv_item.get("item_instance_id") == unequipped_item.get("item_instance_id"):
                        inv_item["inner_container"] = container_result["inner_container"]
                        player.set_inventory(inventory_view)
                        _persist_player(persistence, player)
                        logger.debug(
                            "Wearable container preserved on unequip",
                            player_id=player.player_id,
                            item_id=unequipped_item.get("item_id"),
                        )
                        break
        except Exception as e:
            # Log but don't fail - container preservation is not critical
            logger.warning(
                "Failed to preserve wearable container on unequip",
                error=str(e),
                player_id=player.player_id,
                item_id=unequipped_item.get("item_id"),
            )
    item_name = unequipped_item.get("item_name") or unequipped_item.get("item_id", "item")

    room_id = str(player.current_room_id)

    event = build_event(
        "inventory_unequip",
        {
            "player_name": player.name,
            "item_id": unequipped_item.get("item_id"),
            "item_name": item_name,
            "slot": resolved_slot,
        },
        room_id=room_id,
        player_id=str(player.player_id),
        connection_manager=connection_manager,
    )

    await _broadcast_room_event(
        connection_manager,
        room_id,
        event,
        exclude_player=str(player.player_id) if getattr(player, "player_id", None) else None,
    )

    logger.info(
        "Item unequipped",
        player=player.name,
        player_id=str(player.player_id),
        slot=resolved_slot,
        item_id=unequipped_item.get("item_id"),
        room_id=room_id,
        mutation_token=mutation_token,
    )
    return {
        "result": f"You remove {item_name} from {resolved_slot}.",
        "room_message": f"{player.name} removes {item_name} from {resolved_slot}.",
        "game_log_message": f"{player.name} unequipped {item_name} from {resolved_slot}",
        "game_log_channel": "game-log",
    }


async def handle_put_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, Any]:
    """Put an item from inventory into a container."""

    persistence, connection_manager = _resolve_state(request)
    player, error = await _resolve_player(persistence, current_user, player_name)
    if error or not player:
        return error or {"result": "Player information not found."}

    app = getattr(request, "app", None)
    container_service = getattr(app.state, "container_service", None) if app else None
    if not container_service:
        return {"result": "Container service is unavailable."}

    item_name = command_data.get("item", "").strip()
    container_name = command_data.get("container", "").strip()
    quantity = command_data.get("quantity")

    logger.debug(
        "Put command received",
        player=player.name,
        command_data_keys=list(command_data.keys()),
        item_name=item_name,
        container_name=container_name,
        quantity=quantity,
    )

    if not item_name or not container_name:
        logger.warning(
            "Put command validation failed",
            player=player.name,
            item_name=item_name,
            container_name=container_name,
            command_data=command_data,
        )
        return {"result": "Usage: put <item> [in] <container> [quantity]"}

    # Find item in inventory
    inventory = player.get_inventory()
    item_found = None
    item_index = None

    # Try to parse as index first
    try:
        index = int(item_name)
        if index >= 1 and index <= len(inventory):
            item_index = index - 1
            item_found = inventory[item_index]
    except ValueError:
        # Not a number, search by name
        target_lower = item_name.lower()
        for idx, item in enumerate(inventory):
            item_name_check = str(item.get("item_name", item.get("name", ""))).lower()
            if target_lower in item_name_check:
                item_found = item
                item_index = idx
                break

    if not item_found:
        logger.debug(
            "Item not found in inventory for put command",
            item_name=item_name,
            player=player.name,
            inventory_count=len(inventory),
        )
        return {"result": f"You don't have '{item_name}' in your inventory."}

    logger.debug(
        "Item found for put command", item_name=item_name, item_found=item_found.get("item_name"), player=player.name
    )

    # Find container
    room_manager = getattr(connection_manager, "room_manager", None)
    if not room_manager:
        return {"result": "Room manager is unavailable."}

    room_id = str(player.current_room_id)
    room_containers = room_manager.get_containers(room_id) if hasattr(room_manager, "get_containers") else []

    container_found = None
    container_id = None

    # Check room containers
    target_lower = container_name.lower()
    for container in room_containers:
        container_name_check = str(container.get("metadata", {}).get("name", container.get("container_id", ""))).lower()
        if target_lower in container_name_check:
            container_found = container
            container_id = UUID(container.get("container_id"))
            break

    # Check wearable containers
    if not container_found:
        equipped = player.get_equipped_items()
        logger.debug(
            "Checking equipped items for container in put command",
            container_name=container_name,
            target_lower=target_lower,
            equipped_slots=list(equipped.keys()),
            equipped_count=len(equipped),
            player=player.name,
        )
        for slot, item in equipped.items():
            item_name_check = str(item.get("item_name", item.get("name", ""))).lower()
            slot_lower = slot.lower()
            has_inner_container = bool(item.get("inner_container"))
            name_matches = target_lower in item_name_check
            slot_matches = target_lower == slot_lower or target_lower in slot_lower

            logger.debug(
                "Checking equipped item in put command",
                slot=slot,
                item_name=item.get("item_name", item.get("name", "")),
                item_name_check=item_name_check,
                slot_lower=slot_lower,
                has_inner_container=has_inner_container,
                inner_container_id=item.get("inner_container"),
                target_lower=target_lower,
                name_matches=name_matches,
                slot_matches=slot_matches,
            )

            # Check if this item matches by name or slot
            if name_matches or slot_matches:
                # First try to get container from inner_container field
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
                            # Ensure container_id is set from container_data if it wasn't set
                            if container_data.get("container_id") and not container_id:
                                container_id = UUID(container_data.get("container_id"))
                            break
                    except (ValueError, TypeError) as e:
                        logger.debug(
                            "Failed to parse container ID for put command",
                            inner_container_id=inner_container_id,
                            error=str(e),
                        )
                        continue

                # If inner_container is not set, try to find container using wearable container service
                # This handles cases where the container exists but inner_container wasn't set on the item
                if not container_found:
                    try:
                        _, wearable_container_service, _ = _get_shared_services(request)
                        player_id_uuid = UUID(str(player.player_id))
                        wearable_containers = await wearable_container_service.get_wearable_containers_for_player(
                            player_id_uuid
                        )
                        logger.debug(
                            "Searching wearable containers for put command",
                            player_id=str(player_id_uuid),
                            wearable_containers_count=len(wearable_containers),
                            target_slot=slot,
                        )
                        for container_component in wearable_containers:
                            # Match by slot name or container metadata name
                            container_metadata = (
                                container_component.metadata if hasattr(container_component, "metadata") else {}
                            )
                            container_metadata_name = str(container_metadata.get("name", "")).lower()
                            container_slot = str(container_metadata.get("slot", "")).lower()

                            if (
                                container_slot == slot_lower
                                or target_lower in container_metadata_name
                                or (slot_matches and container_slot == slot_lower)
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
                                        container_id = container_id_from_component
                                        logger.debug(
                                            "Found container via wearable container service",
                                            container_id=str(container_id),
                                            slot=slot,
                                            player=player.name,
                                        )
                                        break
                    except Exception as e:
                        logger.debug(
                            "Error finding container via wearable container service",
                            error=str(e),
                            slot=slot,
                            player=player.name,
                        )
                        continue

                    if container_found:
                        break

                    # If we matched by slot but container doesn't exist, try to create it
                    # This handles cases where the item was equipped but container wasn't created
                    if slot_matches and not container_found:
                        try:
                            player_id_uuid = UUID(str(player.player_id))
                            logger.debug(
                                "Attempting to create container for equipped item in put command",
                                slot=slot,
                                item_id=item.get("item_id"),
                                has_inner_container=bool(item.get("inner_container")),
                                player=player.name,
                            )
                            # Try to create container for this equipped item
                            _, wearable_container_service, _ = _get_shared_services(request)
                            container_result = await wearable_container_service.handle_equip_wearable_container(
                                player_id=player_id_uuid,
                                item_stack=cast(dict[str, Any], item),
                            )
                            logger.debug(
                                "Container creation result",
                                container_result=container_result,
                                slot=slot,
                                player=player.name,
                            )
                            if container_result and container_result.get("container_id"):
                                container_id_created = container_result.get("container_id")
                                container_data = (
                                    persistence.get_container(container_id_created)
                                    if hasattr(persistence, "get_container")
                                    else None
                                )
                                if container_data:
                                    container_found = container_data
                                    container_id = container_id_created
                                    logger.debug(
                                        "Created container for equipped item in put command",
                                        container_id=str(container_id),
                                        slot=slot,
                                        player=player.name,
                                    )
                                    break
                            else:
                                logger.debug(
                                    "Container creation returned None or no container_id, trying direct creation",
                                    slot=slot,
                                    item_has_inner_container=bool(item.get("inner_container")),
                                    player=player.name,
                                )
                                # If handle_equip_wearable_container failed (no inner_container),
                                # try creating container directly with default capacity
                                try:
                                    player_id_uuid = UUID(str(player.player_id))
                                    item_name = item.get("item_name", item.get("name", "Unknown"))
                                    # Create container directly with default capacity
                                    container_data_created = persistence.create_container(
                                        source_type="equipment",
                                        entity_id=player_id_uuid,
                                        capacity_slots=20,
                                        metadata_json={
                                            "name": item_name,
                                            "slot": slot,
                                            "item_id": item.get("item_id"),
                                        },
                                    )
                                    if container_data_created and container_data_created.get("container_id"):
                                        container_found = container_data_created
                                        container_id = container_data_created.get("container_id")
                                        # Update item to include inner_container field for future lookups
                                        # Note: This requires updating the equipped item in the player's data
                                        logger.debug(
                                            "Created container directly for equipped item in put command",
                                            container_id=str(container_id),
                                            slot=slot,
                                            player=player.name,
                                        )
                                        break
                                except Exception as e2:
                                    logger.debug(
                                        "Failed to create container directly",
                                        error=str(e2),
                                        slot=slot,
                                        player=player.name,
                                    )
                        except Exception as e:
                            logger.debug(
                                "Failed to create container for equipped item in put command",
                                error=str(e),
                                slot=slot,
                                player=player.name,
                            )
                            # Continue to next equipped item
                            continue

    if not container_found:
        logger.debug("Container not found for put command", container_name=container_name, player=player.name)
        return {"result": f"You don't see any '{container_name}' here."}

    if not container_id:
        logger.error(
            "Container found but container_id is None for put command",
            container_name=container_name,
            player=player.name,
        )
        return {"result": f"Error: Container '{container_name}' has no valid ID."}

    # Get existing token if container is already open, otherwise open it
    player_id_uuid = UUID(str(player.player_id))
    mutation_token = container_service.get_container_token(container_id, player_id_uuid)

    if not mutation_token:
        # Container not open, open it now
        try:
            open_result = await container_service.open_container(container_id, player_id_uuid)
            mutation_token = open_result.get("mutation_token")
        except Exception as e:
            return {"result": f"Cannot access container: {str(e)}"}

    # Transfer item
    try:
        transfer_quantity = quantity if quantity else item_found.get("quantity", 1)

        # Ensure item has required fields for transfer
        # InventoryStack requires item_instance_id and item_id
        if not item_found.get("item_instance_id") and not item_found.get("item_id"):
            logger.error("Item missing required fields for transfer", item=item_found, player=player.name)
            return {"result": "Error: Item is missing required identification fields."}

        # Ensure the item instance exists in the database for referential integrity
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
                logger.debug(
                    "Item instance ensured before transfer to container",
                    item_instance_id=item_instance_id,
                    prototype_id=prototype_id,
                    player_id=str(player.player_id),
                )
            except Exception as e:
                logger.warning(
                    "Failed to ensure item instance before transfer to container",
                    item_instance_id=item_instance_id,
                    prototype_id=prototype_id,
                    error=str(e),
                )
                # Continue anyway - the transfer will fail with a foreign key error if the instance doesn't exist
                # but at least we tried to create it

        logger.debug(
            "Transferring item to container",
            player=player.name,
            item_name=item_found.get("item_name"),
            item_id=item_found.get("item_id"),
            item_instance_id=item_found.get("item_instance_id"),
            container_id=str(container_id),
            quantity=transfer_quantity,
        )
        await container_service.transfer_to_container(
            container_id=container_id,
            player_id=UUID(str(player.player_id)),
            mutation_token=mutation_token,
            item=item_found,
            quantity=transfer_quantity,
        )

        # Remove item from player inventory
        # The transfer method doesn't remove items, so we need to do it manually
        new_inventory = inventory.copy()
        if item_index is not None and 0 <= item_index < len(new_inventory):
            item_to_remove = new_inventory[item_index]
            current_quantity = item_to_remove.get("quantity", 1)
            if transfer_quantity >= current_quantity:
                # Remove entire stack
                new_inventory.pop(item_index)
            else:
                # Reduce quantity
                new_inventory[item_index] = item_to_remove.copy()
                new_inventory[item_index]["quantity"] = current_quantity - transfer_quantity

        player.set_inventory(new_inventory)
        persist_error = _persist_player(persistence, player)
        if persist_error:
            return persist_error

        item_display_name = item_found.get("item_name") or item_found.get("item_id", "item")
        return {
            "result": f"You put {transfer_quantity}x {item_display_name} into {container_name}.",
            "room_message": f"{player.name} puts {transfer_quantity}x {item_display_name} into {container_name}.",
            "game_log_message": f"{player.name} put {transfer_quantity}x {item_display_name} into {container_name}",
            "game_log_channel": "game-log",
        }
    except Exception as e:
        logger.error("Error putting item in container", player=player.name, error=str(e))
        return {"result": f"Error: {str(e)}"}


async def handle_get_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, Any]:
    """Get an item from a container into inventory."""

    persistence, connection_manager = _resolve_state(request)
    player, error = await _resolve_player(persistence, current_user, player_name)
    if error or not player:
        return error or {"result": "Player information not found."}

    app = getattr(request, "app", None)
    container_service = getattr(app.state, "container_service", None) if app else None
    if not container_service:
        return {"result": "Container service is unavailable."}

    item_name = command_data.get("item", "").strip()
    container_name = command_data.get("container", "").strip()
    quantity = command_data.get("quantity")

    logger.debug(
        "Get command received",
        player=player.name,
        item_name=item_name,
        container_name=container_name,
        quantity=quantity,
        command_data_keys=list(command_data.keys()),
        full_command_data=command_data,
    )

    if not item_name or not container_name:
        return {"result": "Usage: get <item> [from] <container> [quantity]"}

    # Find container
    room_manager = getattr(connection_manager, "room_manager", None)
    if not room_manager:
        return {"result": "Room manager is unavailable."}

    room_id = str(player.current_room_id)
    room_containers = room_manager.get_containers(room_id) if hasattr(room_manager, "get_containers") else []

    container_found = None
    container_id = None

    # Check room containers
    target_lower = container_name.lower()
    for container in room_containers:
        container_name_check = str(container.get("metadata", {}).get("name", container.get("container_id", ""))).lower()
        if target_lower in container_name_check:
            container_found = container
            container_id = UUID(container.get("container_id"))
            break

    # Check wearable containers - use same logic as "look in" command
    if not container_found:
        equipped = player.get_equipped_items()

        # Find matching containers by name (same logic as _find_container_wearable)
        matching_containers = []
        for slot, item in equipped.items():
            equipped_item_name = str(item.get("item_name", item.get("name", ""))).lower()
            prototype_id = str(item.get("prototype_id", item.get("item_id", ""))).lower()
            item_id = str(item.get("item_id", "")).lower()

            # Check if this item matches the target name
            name_matches = target_lower in equipped_item_name or target_lower in prototype_id or target_lower in item_id

            # Include items that:
            # 1. Have inner_container (explicit container)
            # 2. Match the target name (might be a container we need to look up)
            if item.get("inner_container") or name_matches:
                if name_matches:
                    matching_containers.append((slot, item))

        # Use first match if found
        if matching_containers:
            slot, item = matching_containers[0]
            item_instance_id = item.get("item_instance_id")

            # Try inner_container first if available
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
                        logger.debug(
                            "Found container via inner_container for get command",
                            container_id=str(container_id),
                            slot=slot,
                            player=player.name,
                        )
                except (ValueError, TypeError):
                    pass

            # If not found via inner_container, use wearable container service
            if not container_found:
                try:
                    _, wearable_container_service, _ = _get_shared_services(request)
                    player_id_uuid = UUID(str(player.player_id))
                    wearable_containers = await wearable_container_service.get_wearable_containers_for_player(
                        player_id_uuid
                    )

                    slot_lower = slot.lower() if slot else ""
                    for container_component in wearable_containers:
                        container_metadata = (
                            container_component.metadata if hasattr(container_component, "metadata") else {}
                        )
                        container_item_instance_id = container_metadata.get("item_instance_id")
                        container_item_name = str(container_metadata.get("item_name", "")).lower()
                        container_slot = str(container_metadata.get("slot", "")).lower()

                        # Match by item_instance_id first (most reliable)
                        if (
                            item_instance_id
                            and container_item_instance_id
                            and str(item_instance_id) == str(container_item_instance_id)
                        ):
                            container_id_from_component = container_component.container_id
                            if container_id_from_component:
                                container_data = (
                                    persistence.get_container(container_id_from_component)
                                    if hasattr(persistence, "get_container")
                                    else None
                                )
                                if container_data:
                                    container_found = container_data
                                    container_id = container_id_from_component
                                    logger.debug(
                                        "Found container via wearable container service (item_instance_id match) for get command",
                                        container_id=str(container_id_from_component),
                                        item_instance_id=item_instance_id,
                                        player=player.name,
                                    )
                                    break

                        # Fallback: match by slot name or container metadata item_name
                        if not container_found and (
                            container_slot == slot_lower
                            or target_lower in container_item_name
                            or target_lower in container_slot
                        ):
                            container_id_from_component = container_component.container_id
                            if container_id_from_component:
                                container_data = (
                                    persistence.get_container(container_id_from_component)
                                    if hasattr(persistence, "get_container")
                                    else None
                                )
                                if container_data:
                                    container_found = container_data
                                    container_id = container_id_from_component
                                    logger.debug(
                                        "Found container via wearable container service (name/slot match) for get command",
                                        container_id=str(container_id_from_component),
                                        container_name=container_item_name,
                                        slot=slot,
                                        player=player.name,
                                    )
                                    break
                except Exception as e:
                    logger.debug(
                        "Error finding container via wearable container service for get command",
                        error=str(e),
                        player=player.name,
                    )

    if not container_found:
        return {"result": f"You don't see any '{container_name}' here."}

    # Handle ContainerData objects vs dicts
    if hasattr(container_found, "items_json"):
        # ContainerData object
        container_items = container_found.items_json or []
        if not container_id:
            container_id = container_found.container_instance_id
    elif isinstance(container_found, dict):
        # Dict from room containers
        container_items = container_found.get("items", [])
        if not container_id:
            container_id = UUID(container_found.get("container_id"))
    else:
        # Fallback: try to convert to dict
        if hasattr(container_found, "to_dict"):
            container_found = container_found.to_dict()
            container_items = container_found.get("items", [])
            if not container_id:
                container_id = UUID(container_found.get("container_id"))
        else:
            container_items = []

    # Parse container_items if it's a JSON string
    if isinstance(container_items, str):
        try:
            import json

            container_items = json.loads(container_items)
        except (json.JSONDecodeError, ValueError) as e:
            logger.error(
                "Failed to parse container_items JSON string",
                player=player.name,
                container_id=str(container_id) if container_id else None,
                error=str(e),
                container_items=container_items,
            )
            return {"result": "Error: Invalid container data format."}

    item_found = None
    item_index = None

    # Ensure container_items is a list of dictionaries
    if not isinstance(container_items, list):
        logger.error(
            "Container items is not a list",
            player=player.name,
            container_id=str(container_id) if container_id else None,
            container_items_type=type(container_items).__name__,
            container_items=container_items,
        )
        return {"result": "Error: Invalid container data format."}

    # Filter out any non-dictionary items and log them
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

    # If we filtered out items, use the filtered list
    if len(filtered_items) != len(container_items):
        logger.warning(
            "Filtered out non-dictionary items from container_items",
            player=player.name,
            container_id=str(container_id) if container_id else None,
            original_length=len(container_items),
            filtered_length=len(filtered_items),
        )
        container_items = filtered_items

    # Debug: Log the structure of container_items
    logger.debug(
        "Container items structure",
        player=player.name,
        container_id=str(container_id) if container_id else None,
        container_items_length=len(container_items),
        container_items_types=[type(item).__name__ for item in container_items[:5]],  # First 5 items
        container_items_sample=[str(item)[:100] for item in container_items[:3]],  # First 3 items as strings
    )

    # Try to parse as index first
    try:
        index = int(item_name)
        if index >= 1 and index <= len(container_items):
            item_index = index - 1
            item_found = container_items[item_index]
            # Ensure item_found is a dictionary
            if not isinstance(item_found, dict):
                logger.error(
                    "Container item is not a dictionary",
                    player=player.name,
                    container_id=str(container_id) if container_id else None,
                    item_index=item_index,
                    item_type=type(item_found).__name__,
                    item=item_found,
                )
                return {"result": "Error: Invalid item data format."}
    except ValueError:
        # Not a number, search by name
        target_lower = item_name.lower()
        for idx, item in enumerate(container_items):
            # Ensure item is a dictionary before calling .get()
            if not isinstance(item, dict):
                logger.warning(
                    "Skipping non-dictionary item in container",
                    player=player.name,
                    container_id=str(container_id) if container_id else None,
                    item_index=idx,
                    item_type=type(item).__name__,
                    item=item,
                )
                continue
            item_name_check = str(item.get("item_name", item.get("name", ""))).lower()
            if target_lower in item_name_check:
                item_found = item
                item_index = idx
                break

    if not item_found:
        return {"result": f"You don't see '{item_name}' in {container_name}."}

    # Ensure item_found is a dictionary before using it
    if not isinstance(item_found, dict):
        logger.error(
            "Item found is not a dictionary",
            player=player.name,
            container_id=str(container_id) if container_id else None,
            item_name=item_name,
            item_type=type(item_found).__name__,
            item=item_found,
        )
        return {"result": "Error: Invalid item data format."}

    # Ensure container_id is set
    if not container_id:
        if hasattr(container_found, "container_instance_id"):
            container_id = container_found.container_instance_id
        elif isinstance(container_found, dict):
            container_id = UUID(container_found.get("container_id"))
        else:
            return {"result": "Error: Could not determine container ID."}

    # Get existing token if container is already open, otherwise open it
    player_id_uuid = UUID(str(player.player_id))
    mutation_token = container_service.get_container_token(container_id, player_id_uuid)

    if not mutation_token:
        # Container not open, open it now
        try:
            open_result = await container_service.open_container(container_id, player_id_uuid)
            mutation_token = open_result.get("mutation_token")
        except Exception as e:
            return {"result": f"Cannot access container: {str(e)}"}

    # Transfer item
    # Note: item_found is already validated as a dict at line 1827
    try:
        transfer_quantity = quantity if quantity else item_found.get("quantity", 1)
        result = await container_service.transfer_from_container(
            container_id=container_id,
            player_id=UUID(str(player.player_id)),
            mutation_token=mutation_token,
            item=item_found,
            quantity=transfer_quantity,
        )

        # Update player inventory
        new_inventory = result.get("player_inventory", player.get_inventory())
        player.set_inventory(new_inventory)
        persist_error = _persist_player(persistence, player)
        if persist_error:
            return persist_error

        item_display_name = item_found.get("item_name") or item_found.get("item_id", "item")
        return {
            "result": f"You get {transfer_quantity}x {item_display_name} from {container_name}.",
            "room_message": f"{player.name} gets {transfer_quantity}x {item_display_name} from {container_name}.",
            "game_log_message": f"{player.name} got {transfer_quantity}x {item_display_name} from {container_name}",
            "game_log_channel": "game-log",
        }
    except Exception as e:
        logger.error("Error getting item from container", player=player.name, error=str(e))
        return {"result": f"Error: {str(e)}"}


__all__ = [
    "handle_inventory_command",
    "handle_pickup_command",
    "handle_drop_command",
    "handle_put_command",
    "handle_get_command",
    "handle_equip_command",
    "handle_unequip_command",
]
