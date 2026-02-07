"""Equipment-related helper functions for inventory commands."""

from copy import deepcopy
from typing import Any, cast
from uuid import UUID

from ..models.player import Player
from ..services.inventory_service import InventoryStack
from ..structured_logging.enhanced_logging_config import get_logger
from .inventory_item_matching import match_inventory_item_by_name, normalize_slot_name
from .inventory_service_helpers import get_shared_services

logger = get_logger(__name__)


def resolve_equip_item_index(
    command_data: dict[str, Any], inventory: list[dict[str, Any]], player: Player, room_id: str
) -> tuple[int | None, dict[str, Any] | None]:
    """Resolve item index from command data for equip command."""
    index = command_data.get("index")
    search_term = command_data.get("search_term")

    if isinstance(index, int) and index >= 1:
        if index > len(inventory):
            return None, {"result": "You do not have an item in that slot."}
        resolved_index_zero = index - 1
        selected_stack = deepcopy(inventory[resolved_index_zero])
        if isinstance(selected_stack, dict):
            normalized_selected_slot = normalize_slot_name(selected_stack.get("slot_type"))
            if normalized_selected_slot:
                selected_stack["slot_type"] = normalized_selected_slot
        return resolved_index_zero, selected_stack
    if isinstance(search_term, str) and search_term.strip():
        match_index = match_inventory_item_by_name(inventory, search_term)
        if match_index is None:
            logger.info(
                "No matching inventory item found for equip",
                player=player.name,
                player_id=player.player_id,
                search_term=search_term,
                room_id=room_id,
            )
            return None, {"result": f"You do not have an item matching '{search_term}'."}
        resolved_index_zero = match_index
        logger.debug(
            "Equip resolved via fuzzy search",
            player=player.name,
            player_id=player.player_id,
            room_id=room_id,
            search_term=search_term,
            inventory_index=match_index + 1,
        )
        selected_stack = deepcopy(inventory[resolved_index_zero])
        if isinstance(selected_stack, dict):
            normalized_selected_slot = normalize_slot_name(selected_stack.get("slot_type"))
            if normalized_selected_slot:
                selected_stack["slot_type"] = normalized_selected_slot
        return resolved_index_zero, selected_stack
    return None, {"result": "Usage: equip <inventory-number|item-name> [slot]"}


def normalize_inventory_slots(inventory: list[dict[str, Any]]) -> None:
    """Normalize slot_type in inventory list in-place."""
    for stack_entry in inventory:
        if isinstance(stack_entry, dict):
            current_slot = stack_entry.get("slot_type")
            normalized_slot = normalize_slot_name(current_slot)
            if normalized_slot:
                stack_entry["slot_type"] = normalized_slot


def normalize_equipped_items(new_equipped: dict[str, InventoryStack]) -> dict[str, InventoryStack]:
    """Normalize slot names and slot_type in equipped items."""
    normalized_equipped: dict[str, InventoryStack] = {}
    for slot_name, stack in new_equipped.items():
        normalized_slot_name = normalize_slot_name(slot_name) or slot_name
        if isinstance(stack, dict):
            normalized_stack_slot = normalize_slot_name(stack.get("slot_type"))
            if normalized_stack_slot:
                stack["slot_type"] = normalized_stack_slot
        normalized_equipped[normalized_slot_name] = stack
    return normalized_equipped


def find_equipped_item_after_equip(
    target_slot: str | None, selected_stack: dict[str, Any], equipped_mapping: dict[str, Any]
) -> tuple[str, InventoryStack | None]:
    """Find the equipped slot and item after equipping."""
    equipped_slot: str | None = None
    equipped_item: InventoryStack | None = None

    preferred_slot = target_slot or selected_stack.get("slot_type")

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

    return equipped_slot, equipped_item


async def handle_wearable_container_on_equip(
    request: Any, player: Player, equipped_item: InventoryStack | None
) -> None:
    """Handle wearable container creation when equipping a container item."""
    if equipped_item and equipped_item.get("inner_container"):
        try:
            _, wearable_container_service, _ = get_shared_services(request)
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
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container creation errors unpredictable, not critical
            logger.warning(
                "Failed to create wearable container on equip",
                error=str(e),
                player_id=player.player_id,
                item_id=equipped_item.get("item_id"),
            )


def resolve_unequip_slot(
    command_data: dict[str, Any], equipped_mapping: dict[str, Any]
) -> tuple[str | None, dict[str, str] | None]:
    """Resolve slot from command data for unequip command."""
    from .inventory_item_matching import match_equipped_item_by_name

    slot = command_data.get("slot")
    search_term = command_data.get("search_term")
    normalized_slot = normalize_slot_name(slot) if isinstance(slot, str) else None

    if normalized_slot is None and not (isinstance(search_term, str) and search_term.strip()):
        return None, {"result": "Usage: unequip <slot|item-name>"}

    resolved_slot: str | None = None
    if normalized_slot and normalized_slot in equipped_mapping:
        resolved_slot = normalized_slot

    if resolved_slot is None and isinstance(search_term, str) and search_term.strip():
        match_slot = match_equipped_item_by_name(equipped_mapping, search_term)
        if match_slot is None:
            return None, {"result": f"You do not have an equipped item matching '{search_term}'."}
        resolved_slot = match_slot

    if resolved_slot is None:
        return None, {"result": "You do not have an item equipped in that slot."}

    return resolved_slot, None


async def handle_wearable_container_on_unequip(
    request: Any, player: Player, unequipped_item: dict[str, Any], persistence: Any
) -> None:
    """Handle wearable container preservation when unequipping a container item."""
    from .inventory_command_helpers import persist_player

    if unequipped_item.get("inner_container"):
        try:
            _, wearable_container_service, _ = get_shared_services(request)
            container_result = await wearable_container_service.handle_unequip_wearable_container(
                player_id=UUID(str(player.player_id)),
                item_stack=unequipped_item,
            )
            if container_result:
                inventory_view = player.get_inventory()
                for inv_item in inventory_view:
                    if inv_item.get("item_instance_id") == unequipped_item.get("item_instance_id"):
                        inv_item["inner_container"] = container_result["inner_container"]
                        player.set_inventory(inventory_view)
                        await persist_player(persistence, player)
                        logger.debug(
                            "Wearable container preserved on unequip",
                            player_id=player.player_id,
                            item_id=unequipped_item.get("item_id"),
                        )
                        break
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container preservation errors unpredictable, not critical
            logger.warning(
                "Failed to preserve wearable container on unequip",
                error=str(e),
                player_id=player.player_id,
                item_id=unequipped_item.get("item_id"),
            )
