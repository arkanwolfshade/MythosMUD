"""Inventory and equipment command handlers for MythosMUD."""

# pylint: disable=too-many-locals,too-many-return-statements,too-many-lines  # Reason: Inventory commands require many intermediate variables for complex item management logic and multiple return statements for early validation returns. Inventory commands require extensive handlers for complex item operations.

from __future__ import annotations

import uuid
from copy import deepcopy
from typing import Any, cast
from uuid import UUID

from ..alias_storage import AliasStorage
from ..services.equipment_service import EquipmentCapacityError, SlotValidationError
from ..services.inventory_service import InventoryCapacityError, InventoryService
from ..structured_logging.enhanced_logging_config import get_logger
from .container_helpers_inventory import (
    find_container_in_room,
    find_item_in_container,
    find_wearable_container,
    find_wearable_container_for_put,
    get_container_data_for_inventory,
    parse_container_items,
    resolve_container_id,
    transfer_item_from_container,
    transfer_item_to_container,
    update_equipped_with_container_info,
    validate_get_command_inputs,
    validate_put_command_inputs,
)
from .equipment_helpers import (
    find_equipped_item_after_equip,
    handle_wearable_container_on_equip,
    handle_wearable_container_on_unequip,
    normalize_equipped_items,
    normalize_inventory_slots,
    resolve_equip_item_index,
    resolve_unequip_slot,
)
from .inventory_command_helpers import (
    add_pickup_to_inventory,
    build_and_broadcast_inventory_event,
    clone_inventory,
    ensure_item_instance_for_pickup,
    get_room_manager,
    persist_player,
    prepare_extracted_stack,
    remove_item_from_inventory,
    resolve_pickup_item_index,
    resolve_state_and_player,
)
from .inventory_display_helpers import render_inventory
from .inventory_item_matching import normalize_slot_name
from .inventory_service_helpers import get_shared_services

logger = get_logger(__name__)


async def handle_inventory_command(
    _command_data: dict[str, Any],  # pylint: disable=unused-argument  # Reason: Command data not used in this handler
    current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, Any]:
    """Display the player's inventory and equipped items, including container contents."""

    _persistence, _connection_manager, player, error = await resolve_state_and_player(
        request, current_user, player_name
    )
    if error or not player:
        return error or {"result": "Player information not found."}

    inventory_view = player.get_inventory()
    equipped_view = player.get_equipped_items()

    container_contents, container_capacities, container_lock_states = await get_container_data_for_inventory(
        request, player, equipped_view
    )

    update_equipped_with_container_info(equipped_view, container_contents, container_capacities, container_lock_states)

    logger.info(
        "Inventory displayed",
        player=player.name,
        slots_used=len(inventory_view),
        equipped_slots=len(equipped_view),
        containers_with_items=len(container_contents),
    )
    return {
        "result": render_inventory(
            inventory_view, equipped_view, container_contents, container_capacities, container_lock_states
        ),
        "inventory": deepcopy(inventory_view),
        "equipped": deepcopy(equipped_view),
    }


async def handle_pickup_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, Any]:
    """Move an item stack from room drops into the player's inventory."""

    persistence, connection_manager, player, error = await resolve_state_and_player(request, current_user, player_name)
    if error or not player:
        return error or {"result": "Player information not found."}

    room_manager, room_error = get_room_manager(connection_manager, player)
    if room_error:
        return room_error

    desired_quantity = command_data.get("quantity")
    room_id = str(player.current_room_id)
    drop_list = room_manager.list_room_drops(room_id)

    # Resolve item index
    player_id_uuid: uuid.UUID = UUID(player.player_id) if isinstance(player.player_id, str) else player.player_id
    resolved_index_zero, _, index_error = resolve_pickup_item_index(
        command_data, drop_list, player.name, player_id_uuid, room_id
    )
    if index_error:
        return index_error

    # Determine quantity
    if desired_quantity is None:
        desired_quantity = int(drop_list[resolved_index_zero].get("quantity", 1))
    if desired_quantity <= 0:
        return {"result": "Quantity must be a positive number."}

    # Extract stack from room
    extracted_stack = room_manager.take_room_drop(room_id, resolved_index_zero, desired_quantity)
    if not extracted_stack:
        return {"result": "That item is no longer available."}

    logger.debug("Pickup: extracted_stack before processing", player=player.name, player_id=str(player.player_id))

    # Prepare extracted stack (reuse player_id_uuid from above)
    extracted_stack = prepare_extracted_stack(extracted_stack, player.name, player_id_uuid)

    # Ensure item instance exists
    ensure_item_instance_for_pickup(persistence, extracted_stack, player, room_id)

    # Save previous inventory for rollback if persistence fails
    previous_inventory = clone_inventory(player)

    # Add to inventory
    inventory_service = InventoryService()
    updated_inventory, inventory_error = await add_pickup_to_inventory(
        inventory_service, player, extracted_stack, room_manager, room_id
    )
    if inventory_error:
        return inventory_error

    if updated_inventory is None:
        return {"result": "Failed to update inventory."}
    # updated_inventory is list[dict[str, Any]] after None check
    player.set_inventory(updated_inventory)
    logger.info(
        "Pickup: inventory after set_inventory",
        player=player.name,
        player_id=str(player.player_id),
        inventory_length=len(updated_inventory),
    )
    persist_error = persist_player(persistence, player)
    if persist_error:
        room_manager.add_room_drop(room_id, extracted_stack)
        player.set_inventory(previous_inventory)
        return persist_error

    quantity = extracted_stack.get("quantity", desired_quantity)
    item_name = extracted_stack.get("item_name") or extracted_stack.get("item_id", "item")

    await build_and_broadcast_inventory_event(
        connection_manager,
        player,
        room_id,
        "inventory_pickup",
        {
            "player_name": player.name,
            "item_id": extracted_stack.get("item_id"),
            "item_name": item_name,
            "quantity": quantity,
        },
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
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, Any]:
    """Drop an inventory stack into the current room."""

    persistence, connection_manager, player, error = await resolve_state_and_player(request, current_user, player_name)
    if error or not player:
        return error or {"result": "Player information not found."}

    room_manager, room_error = get_room_manager(connection_manager, player)
    if room_error:
        return room_error

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

    previous_inventory = clone_inventory(player)

    if quantity == stack.get("quantity", 1):
        updated_inventory = previous_inventory[: index - 1] + previous_inventory[index:]
    else:
        updated_inventory = deepcopy(previous_inventory)
        updated_inventory[index - 1]["quantity"] = previous_inventory[index - 1]["quantity"] - quantity

    player.set_inventory(updated_inventory)

    drop_stack = deepcopy(stack)
    drop_stack["quantity"] = quantity

    persist_error = persist_player(persistence, player)
    if persist_error:
        player.set_inventory(previous_inventory)
        return persist_error

    room_manager.add_room_drop(room_id, drop_stack)

    item_name = drop_stack.get("item_name") or drop_stack.get("item_id", "item")

    await build_and_broadcast_inventory_event(
        connection_manager,
        player,
        room_id,
        "inventory_drop",
        {
            "player_name": player.name,
            "item_id": drop_stack.get("item_id"),
            "item_name": item_name,
            "quantity": quantity,
        },
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
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, Any]:
    """Equip an item from inventory."""

    persistence, connection_manager, player, error = await resolve_state_and_player(request, current_user, player_name)
    if error or not player:
        return error or {"result": "Player information not found."}

    inventory = player.get_inventory()
    normalize_inventory_slots(inventory)

    room_id = str(player.current_room_id)
    target_slot = normalize_slot_name(command_data.get("target_slot"))

    resolved_index_zero, error_or_stack = resolve_equip_item_index(command_data, inventory, player, room_id)
    if resolved_index_zero is None:
        return error_or_stack or {"result": "Failed to resolve item index."}
    selected_stack = error_or_stack

    inventory_service, _, equipment_service = get_shared_services(request)
    mutation_token = command_data.get("mutation_token")

    previous_inventory = clone_inventory(player)
    previous_equipped = deepcopy(player.get_equipped_items())

    player_id_value = player.player_id
    player_id_for_mutation: uuid.UUID | str = str(player_id_value)
    with inventory_service.begin_mutation(player_id_for_mutation, mutation_token) as decision:
        if not decision.should_apply:
            logger.info(
                "Equip suppressed by mutation guard",
                player=player.name,
                player_id=player.player_id,
                requested_slot=target_slot,
                inventory_index=command_data.get("index"),
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
                player_id=player.player_id,
                reason=str(exc),
                requested_slot=target_slot,
                inventory_index=command_data.get("index"),
                room_id=room_id,
            )
            return {"result": str(exc)}

        normalize_inventory_slots(cast(list[dict[str, Any]], new_inventory))
        normalized_equipped = normalize_equipped_items(new_equipped)

        player.set_inventory([cast(dict[str, Any], stack) for stack in new_inventory])
        player.set_equipped_items(cast(dict[str, Any], normalized_equipped))

        persist_error = persist_player(persistence, player)
        if persist_error:
            player.set_inventory(previous_inventory)
            player.set_equipped_items(previous_equipped)
            return persist_error

    if selected_stack is None or not isinstance(selected_stack, dict):
        return {"result": "Selected item is invalid."}
    equipped_mapping = player.get_equipped_items()
    equipped_slot, equipped_item = find_equipped_item_after_equip(target_slot, selected_stack, equipped_mapping)

    await handle_wearable_container_on_equip(request, player, equipped_item)

    fallback_item: dict[str, Any] = {}
    item_payload: dict[str, Any] = cast(dict[str, Any], equipped_item) if equipped_item is not None else fallback_item

    item_name = item_payload.get("item_name") or item_payload.get("item_id", "item")

    await build_and_broadcast_inventory_event(
        connection_manager,
        player,
        room_id,
        "inventory_equip",
        {
            "player_name": player.name,
            "item_id": item_payload.get("item_id"),
            "item_name": item_name,
            "slot": equipped_slot,
        },
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
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, Any]:
    """Unequip an item into the player's inventory."""

    persistence, connection_manager, player, error = await resolve_state_and_player(request, current_user, player_name)
    if error or not player:
        return error or {"result": "Player information not found."}

    equipped_mapping = player.get_equipped_items()
    resolved_slot, error_result = resolve_unequip_slot(command_data, equipped_mapping)
    if resolved_slot is None:
        return error_result or {"result": "Failed to resolve slot."}

    inventory_service, _, equipment_service = get_shared_services(request)
    mutation_token = command_data.get("mutation_token")

    previous_inventory = clone_inventory(player)
    previous_equipped = deepcopy(player.get_equipped_items())

    player_id_value = player.player_id
    player_id_for_mutation: uuid.UUID | str = str(player_id_value)
    with inventory_service.begin_mutation(player_id_for_mutation, mutation_token) as decision:
        if not decision.should_apply:
            logger.info(
                "Unequip suppressed by mutation guard",
                player=player.name,
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
                player_id=player.player_id,
                reason=str(exc),
                slot=resolved_slot,
                room_id=str(player.current_room_id),
            )
            return {"result": str(exc)}

        normalize_inventory_slots(cast(list[dict[str, Any]], new_inventory))
        normalized_equipped = normalize_equipped_items(new_equipped)

        player.set_inventory([cast(dict[str, Any], stack) for stack in new_inventory])
        player.set_equipped_items(cast(dict[str, Any], normalized_equipped))

        persist_error = persist_player(persistence, player)
        if persist_error:
            player.set_inventory(previous_inventory)
            player.set_equipped_items(previous_equipped)
            return persist_error

    unequipped_item = previous_equipped.get(resolved_slot, {})
    await handle_wearable_container_on_unequip(request, player, unequipped_item, persistence)

    item_name = unequipped_item.get("item_name") or unequipped_item.get("item_id", "item")
    room_id = str(player.current_room_id)

    await build_and_broadcast_inventory_event(
        connection_manager,
        player,
        room_id,
        "inventory_unequip",
        {
            "player_name": player.name,
            "item_id": unequipped_item.get("item_id"),
            "item_name": item_name,
            "slot": resolved_slot,
        },
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
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, Any]:
    """Put an item from inventory into a container."""

    persistence, connection_manager, player, error = await resolve_state_and_player(request, current_user, player_name)
    if error or not player:
        return error or {"result": "Player information not found."}

    validation_result = await validate_put_command_inputs(command_data, request, connection_manager, player)
    if isinstance(validation_result, dict):
        return validation_result

    item_name, container_name, quantity, container_service, room_manager, item_found, item_index = validation_result

    logger.debug(
        "Put command received",
        player=player.name,
        command_data_keys=list(command_data.keys()),
        item_name=item_name,
        container_name=container_name,
        quantity=quantity,
    )

    if item_found is None:
        return {"result": f"'{item_name}' not found in your inventory."}
    logger.debug(
        "Item found for put command", item_name=item_name, item_found=item_found.get("item_name"), player=player.name
    )

    # Find container
    room_id = str(player.current_room_id)
    container_found, container_id = find_container_in_room(room_manager, room_id, container_name)

    # Check wearable containers
    if not container_found:
        container_found, container_id = await find_wearable_container_for_put(
            persistence, request, player, container_name
        )

    if not container_found:
        logger.debug("Container not found for put command", container_name=container_name, player=player.name)
        return {"result": f"You don't see any '{container_name}' here."}

    container_id = resolve_container_id(container_found, container_id)
    if not container_id:
        logger.error(
            "Container found but container_id is None for put command",
            container_name=container_name,
            player=player.name,
        )
        return {"result": f"Error: Container '{container_name}' has no valid ID."}

    # Transfer item to container
    transfer_result = await transfer_item_to_container(
        container_service, persistence, player, container_id, item_found, quantity
    )

    if "error" in transfer_result:
        return {"result": transfer_result["error"]}

    if not transfer_result.get("success"):
        return {"result": "Error: Failed to transfer item."}

    # Remove item from player inventory
    transfer_quantity = transfer_result["transfer_quantity"]
    remove_item_from_inventory(player, item_index, transfer_quantity)
    persist_error = persist_player(persistence, player)
    if persist_error:
        return persist_error

    item_display_name = item_found.get("item_name") or item_found.get("item_id", "item")
    return {
        "result": f"You put {transfer_quantity}x {item_display_name} into {container_name}.",
        "room_message": f"{player.name} puts {transfer_quantity}x {item_display_name} into {container_name}.",
        "game_log_message": f"{player.name} put {transfer_quantity}x {item_display_name} into {container_name}",
        "game_log_channel": "game-log",
    }


async def handle_get_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, Any]:
    """Get an item from a container into inventory."""

    persistence, connection_manager, player, error = await resolve_state_and_player(request, current_user, player_name)
    if error or not player:
        return error or {"result": "Player information not found."}

    validation_result = await validate_get_command_inputs(command_data, request, connection_manager)
    if isinstance(validation_result, dict):
        return validation_result

    item_name, container_name, quantity, container_service, room_manager = validation_result

    logger.debug(
        "Get command received",
        player=player.name,
        item_name=item_name,
        container_name=container_name,
        quantity=quantity,
    )

    # Find container
    room_id = str(player.current_room_id)
    container_found, container_id = find_container_in_room(room_manager, room_id, container_name)

    # Check wearable containers if not found in room
    if not container_found:
        container_found, container_id = await find_wearable_container(persistence, request, player, container_name)

    if not container_found:
        return {"result": f"You don't see any '{container_name}' here."}

    # Parse and validate container items
    container_items, container_id = parse_container_items(container_found, container_id, player)
    if not container_items and container_id:
        return {"result": "Error: Invalid container data format."}

    # Find item in container
    item_found, _ = find_item_in_container(container_items, item_name, player, container_id)
    if not item_found:
        return {"result": f"You don't see '{item_name}' in {container_name}."}

    # Ensure container_id is set
    container_id = resolve_container_id(container_found, container_id)
    if not container_id:
        return {"result": "Error: Could not determine container ID."}

    # Transfer item from container
    transfer_result = await transfer_item_from_container(
        container_service, persistence, player, container_id, item_found, quantity
    )

    if "error" in transfer_result:
        return {"result": transfer_result["error"]}

    if not transfer_result.get("success"):
        return {"result": "Error: Failed to transfer item."}

    transfer_quantity = transfer_result["transfer_quantity"]
    item_display_name = transfer_result["item_display_name"]

    return {
        "result": f"You get {transfer_quantity}x {item_display_name} from {container_name}.",
        "room_message": f"{player.name} gets {transfer_quantity}x {item_display_name} from {container_name}.",
        "game_log_message": f"{player.name} got {transfer_quantity}x {item_display_name} from {container_name}",
        "game_log_channel": "game-log",
    }


__all__ = [
    "handle_inventory_command",
    "handle_pickup_command",
    "handle_drop_command",
    "handle_put_command",
    "handle_get_command",
    "handle_equip_command",
    "handle_unequip_command",
]
