"""Inventory and equipment command handlers for MythosMUD."""

from __future__ import annotations

import inspect
from collections.abc import Mapping
from copy import deepcopy
from typing import Any, cast

from ..alias_storage import AliasStorage
from ..exceptions import ValidationError as MythosValidationError
from ..logging.enhanced_logging_config import get_logger
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
from ..utils.command_parser import get_username_from_user

logger = get_logger(__name__)

DEFAULT_SLOT_CAPACITY = 20

_SHARED_INVENTORY_SERVICE = InventoryService()
_SHARED_EQUIPMENT_SERVICE = EquipmentService(inventory_service=_SHARED_INVENTORY_SERVICE)


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


def _resolve_state(request: Any) -> tuple[Any, Any]:
    app = getattr(request, "app", None)
    state = getattr(app, "state", None)
    persistence = getattr(state, "persistence", None)
    connection_manager = getattr(state, "connection_manager", None)
    return persistence, connection_manager


def _resolve_player(
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
        player = persistence.get_player_by_name(username)
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
        components = [f"{key}={value}" for key, value in sorted(metadata.items())]
        if components:
            return f" [{', '.join(components)}]"
    except Exception as exc:  # pragma: no cover - metadata formatting should rarely fail
        logger.debug("Failed to format metadata", error=str(exc))
    return ""


def _render_inventory(inventory: list[dict[str, Any]], equipped: dict[str, Any]) -> str:
    slots_used = len(inventory)
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
        lines.append("No items in your pack.")

    lines.append("")
    lines.append("Equipped:")

    if equipped:
        for slot_name in sorted(equipped.keys()):
            item = equipped[slot_name]
            item_name = item.get("item_name") or item.get("item_id", "Unknown Item")
            quantity = item.get("quantity", 0)
            metadata_suffix = _format_metadata(item.get("metadata"))
            lines.append(f"- {slot_name}: {item_name} x{quantity}{metadata_suffix}")
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
    """Display the player's inventory and equipped items."""

    persistence, _connection_manager = _resolve_state(request)
    player, error = _resolve_player(persistence, current_user, player_name)
    if error or not player:
        return error or {"result": "Player information not found."}

    inventory_view = player.get_inventory()
    equipped_view = player.get_equipped_items()
    logger.info(
        "Inventory displayed",
        player=player.name,
        slots_used=len(inventory_view),
        equipped_slots=len(equipped_view),
    )
    return {
        "result": _render_inventory(inventory_view, equipped_view),
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
    player, error = _resolve_player(persistence, current_user, player_name)
    if error or not player:
        return error or {"result": "Player information not found."}

    room_manager = getattr(connection_manager, "room_manager", None)
    if not room_manager:
        logger.warning(
            "Pickup attempted without room manager",
            player=player.name,
            player_id=str(player.player_id),
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
                player_id=str(player.player_id),
                search_term=search_term,
                room_id=room_id,
            )
            return {"result": f"There is no item here matching '{search_term}'."}
        resolved_index_zero = match_index
        index = match_index + 1
        logger.debug(
            "Pickup resolved via fuzzy search",
            player=player.name,
            player_id=str(player.player_id),
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

    previous_inventory = _clone_inventory(player)
    inventory_service = InventoryService()

    try:
        updated_inventory = inventory_service.add_stack(previous_inventory, extracted_stack)
    except (InventoryCapacityError, InventoryValidationError) as exc:
        room_manager.add_room_drop(room_id, extracted_stack)
        logger.info(
            "Pickup rejected",
            player=player.name,
            player_id=str(player.player_id),
            reason=str(exc),
            room_id=room_id,
        )
        return {"result": f"You cannot pick that up: {str(exc)}"}

    player.set_inventory(cast(list[dict[str, Any]], updated_inventory))
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
    player, error = _resolve_player(persistence, current_user, player_name)
    if error or not player:
        return error or {"result": "Player information not found."}

    room_manager = getattr(connection_manager, "room_manager", None)
    if not room_manager:
        logger.warning(
            "Drop attempted without room manager",
            player=player.name,
            player_id=str(player.player_id),
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
    player, error = _resolve_player(persistence, current_user, player_name)
    if error or not player:
        return error or {"result": "Player information not found."}

    inventory = player.get_inventory()
    room_id = str(player.current_room_id)
    index = command_data.get("index")
    search_term = command_data.get("search_term")
    target_slot = command_data.get("target_slot")

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
                player_id=str(player.player_id),
                search_term=search_term,
                room_id=room_id,
            )
            return {"result": f"You do not have an item matching '{search_term}'."}
        resolved_index_zero = match_index
        logger.debug(
            "Equip resolved via fuzzy search",
            player=player.name,
            player_id=str(player.player_id),
            room_id=room_id,
            search_term=search_term,
            inventory_index=match_index + 1,
        )
    else:
        return {"result": "Usage: equip <inventory-number|item-name> [slot]"}

    selected_stack = deepcopy(inventory[resolved_index_zero])

    inventory_service = _SHARED_INVENTORY_SERVICE
    equipment_service = _SHARED_EQUIPMENT_SERVICE
    mutation_token = command_data.get("mutation_token")

    previous_inventory = _clone_inventory(player)
    previous_equipped = deepcopy(player.get_equipped_items())

    with inventory_service.begin_mutation(str(player.player_id), mutation_token) as decision:
        if not decision.should_apply:
            logger.info(
                "Equip suppressed by mutation guard",
                player=player.name,
                player_id=str(player.player_id),
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
                player_id=str(player.player_id),
                reason=str(exc),
                requested_slot=target_slot,
                inventory_index=index,
                room_id=room_id,
            )
            return {"result": str(exc)}

        player.set_inventory(cast(list[dict[str, Any]], new_inventory))
        player.set_equipped_items(cast(dict[str, Any], new_equipped))

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
    player, error = _resolve_player(persistence, current_user, player_name)
    if error or not player:
        return error or {"result": "Player information not found."}

    slot = command_data.get("slot")
    if not isinstance(slot, str) or not slot:
        return {"result": "Usage: unequip <slot>"}

    inventory_service = _SHARED_INVENTORY_SERVICE
    equipment_service = _SHARED_EQUIPMENT_SERVICE
    mutation_token = command_data.get("mutation_token")

    previous_inventory = _clone_inventory(player)
    previous_equipped = deepcopy(player.get_equipped_items())

    with inventory_service.begin_mutation(str(player.player_id), mutation_token) as decision:
        if not decision.should_apply:
            logger.info(
                "Unequip suppressed by mutation guard",
                player=player.name,
                player_id=str(player.player_id),
                slot=slot,
                room_id=str(player.current_room_id),
                mutation_token=mutation_token,
            )
            return {"result": "That action is already being processed."}

        try:
            new_inventory, new_equipped = equipment_service.unequip_to_inventory(
                player.get_inventory(),
                player.get_equipped_items(),
                slot_type=slot,
            )
        except (SlotValidationError, EquipmentCapacityError, InventoryCapacityError) as exc:
            logger.info(
                "Unequip rejected",
                player=player.name,
                player_id=str(player.player_id),
                reason=str(exc),
                slot=slot,
                room_id=str(player.current_room_id),
            )
            return {"result": str(exc)}

        player.set_inventory(cast(list[dict[str, Any]], new_inventory))
        player.set_equipped_items(cast(dict[str, Any], new_equipped))

        persist_error = _persist_player(persistence, player)
        if persist_error:
            player.set_inventory(previous_inventory)
            player.set_equipped_items(previous_equipped)
            return persist_error

    unequipped_item = previous_equipped.get(slot, {})
    item_name = unequipped_item.get("item_name") or unequipped_item.get("item_id", "item")

    room_id = str(player.current_room_id)

    event = build_event(
        "inventory_unequip",
        {
            "player_name": player.name,
            "item_id": unequipped_item.get("item_id"),
            "item_name": item_name,
            "slot": slot,
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
        slot=slot,
        item_id=unequipped_item.get("item_id"),
        room_id=room_id,
        mutation_token=mutation_token,
    )
    return {
        "result": f"You remove {item_name} from {slot}.",
        "room_message": f"{player.name} removes {item_name} from {slot}.",
        "game_log_message": f"{player.name} unequipped {item_name} from {slot}",
        "game_log_channel": "game-log",
    }


__all__ = [
    "handle_inventory_command",
    "handle_pickup_command",
    "handle_drop_command",
    "handle_equip_command",
    "handle_unequip_command",
]
