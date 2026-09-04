"""Equipment-related helper functions for inventory commands."""

from collections.abc import Mapping
from copy import deepcopy
from typing import cast
from uuid import UUID

from structlog.stdlib import BoundLogger

from ..models.player import Player
from ..services.inventory_service import InventoryStack
from ..structured_logging.enhanced_logging_config import get_logger
from .inventory_item_matching import match_equipped_item_by_name, match_inventory_item_by_name, normalize_slot_name
from .inventory_service_helpers import get_shared_services

logger: BoundLogger = get_logger(__name__)


def _equip_stack_from_inventory_index(
    inventory: list[dict[str, object]], resolved_index_zero: int
) -> dict[str, object]:
    """Deep-copy inventory stack at index and normalize slot_type."""
    selected_stack = deepcopy(inventory[resolved_index_zero])
    normalized_selected_slot = normalize_slot_name(cast(str | None, selected_stack.get("slot_type")))
    if normalized_selected_slot:
        selected_stack["slot_type"] = normalized_selected_slot
    return selected_stack


def resolve_equip_item_index(
    command_data: dict[str, object], inventory: list[dict[str, object]], player: Player, room_id: str
) -> tuple[int | None, dict[str, object] | None]:
    """Resolve item index from command data for equip command."""
    index = command_data.get("index")
    search_term = command_data.get("search_term")

    if isinstance(index, int) and index >= 1:
        if index > len(inventory):
            return None, {"result": "You do not have an item in that slot."}
        resolved_index_zero = index - 1
        return resolved_index_zero, _equip_stack_from_inventory_index(inventory, resolved_index_zero)

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
        logger.debug(
            "Equip resolved via fuzzy search",
            player=player.name,
            player_id=player.player_id,
            room_id=room_id,
            search_term=search_term,
            inventory_index=match_index + 1,
        )
        return match_index, _equip_stack_from_inventory_index(inventory, match_index)

    return None, {"result": "Usage: equip <inventory-number|item-name> [slot]"}


def normalize_inventory_slots(inventory: list[dict[str, object]]) -> None:
    """Normalize slot_type in inventory list in-place."""
    for stack_entry in inventory:
        current_slot = stack_entry.get("slot_type")
        normalized_slot = normalize_slot_name(cast(str | None, current_slot))
        if normalized_slot:
            stack_entry["slot_type"] = normalized_slot


def normalize_equipped_items(new_equipped: dict[str, InventoryStack]) -> dict[str, InventoryStack]:
    """Normalize slot names and slot_type in equipped items."""
    normalized_equipped: dict[str, InventoryStack] = {}
    for slot_name, stack in new_equipped.items():
        normalized_slot_name = normalize_slot_name(slot_name) or slot_name
        normalized_stack_slot = normalize_slot_name(stack.get("slot_type"))
        if normalized_stack_slot:
            stack["slot_type"] = normalized_stack_slot
        normalized_equipped[normalized_slot_name] = stack
    return normalized_equipped


def _find_equipped_by_item_id(
    equipped_mapping: Mapping[str, object],
    item_id: object,
) -> tuple[str | None, InventoryStack | None]:
    for slot_name, item_raw in equipped_mapping.items():
        item = cast(Mapping[str, object], item_raw)
        if item.get("item_id") == item_id:
            return slot_name, cast(InventoryStack | None, item_raw)
    return None, None


def find_equipped_item_after_equip(
    target_slot: str | None,
    selected_stack: dict[str, object],
    equipped_mapping: Mapping[str, object],
) -> tuple[str | None, InventoryStack | None]:
    """Find the equipped slot and item after equipping."""
    preferred_raw = target_slot if target_slot is not None else selected_stack.get("slot_type")
    preferred_slot = preferred_raw if isinstance(preferred_raw, str) else None

    if preferred_slot is not None and preferred_slot in equipped_mapping:
        return preferred_slot, cast(InventoryStack | None, equipped_mapping.get(preferred_slot))

    slot_hit, item_hit = _find_equipped_by_item_id(equipped_mapping, selected_stack.get("item_id"))
    if slot_hit is not None:
        return slot_hit, item_hit

    equipped_slot = preferred_slot or next(iter(equipped_mapping.keys()), "unknown")
    return equipped_slot, None


async def handle_wearable_container_on_equip(
    request: object, player: Player, equipped_item: InventoryStack | None
) -> None:
    """Handle wearable container creation when equipping a container item."""
    if equipped_item and equipped_item.get("inner_container"):
        try:
            _, wearable_container_service, _ = get_shared_services(request)
            container_result = await wearable_container_service.handle_equip_wearable_container(
                player_id=UUID(str(player.player_id)),
                item_stack=dict(equipped_item),
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


def _unequip_usage_missing_slot(normalized_slot: str | None, search_term: object) -> bool:
    return normalized_slot is None and not (isinstance(search_term, str) and search_term.strip())


def _try_resolve_unequip_slot_key(normalized_slot: str | None, equipped_mapping: Mapping[str, object]) -> str | None:
    if normalized_slot and normalized_slot in equipped_mapping:
        return normalized_slot
    return None


def _try_resolve_unequip_by_search(
    search_term: object, equipped_mapping: Mapping[str, object]
) -> tuple[str | None, dict[str, str] | None]:
    if not (isinstance(search_term, str) and search_term.strip()):
        return None, None
    equipped_typed = cast(Mapping[str, Mapping[str, object]], equipped_mapping)
    match_slot = match_equipped_item_by_name(equipped_typed, search_term)
    if match_slot is None:
        return None, {"result": f"You do not have an equipped item matching '{search_term}'."}
    return match_slot, None


def resolve_unequip_slot(
    command_data: dict[str, object], equipped_mapping: Mapping[str, object]
) -> tuple[str | None, dict[str, str] | None]:
    """Resolve slot from command data for unequip command."""
    slot = command_data.get("slot")
    search_term = command_data.get("search_term")
    normalized_slot = normalize_slot_name(slot) if isinstance(slot, str) else None

    if _unequip_usage_missing_slot(normalized_slot, search_term):
        return None, {"result": "Usage: unequip <slot|item-name>"}

    resolved = _try_resolve_unequip_slot_key(normalized_slot, equipped_mapping)
    if resolved is not None:
        return resolved, None

    found, search_err = _try_resolve_unequip_by_search(search_term, equipped_mapping)
    if search_err is not None:
        return None, search_err
    if found is not None:
        return found, None

    return None, {"result": "You do not have an item equipped in that slot."}


async def handle_wearable_container_on_unequip(
    request: object, player: Player, unequipped_item: dict[str, object], persistence: object
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
                        _ = await persist_player(persistence, player)
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
