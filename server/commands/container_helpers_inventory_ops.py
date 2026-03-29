"""Transfer, validation, and parsing helpers for container inventory commands."""

from __future__ import annotations

import json
from collections.abc import Awaitable
from typing import cast
from uuid import UUID

from ..models.player import Player
from .container_helpers_inventory_find import find_item_in_inventory
from .container_helpers_inventory_logging import logger


async def _ensure_mutation_token(
    container_service: object, container_id: UUID, player_id_uuid: UUID
) -> tuple[object | None, dict[str, object] | None]:
    """Return (mutation_token, error_response). error_response is set only on hard failure."""
    get_token = getattr(container_service, "get_container_token", None)
    token = get_token(container_id, player_id_uuid) if callable(get_token) else None
    if token:
        return token, None
    open_container = getattr(container_service, "open_container", None)
    if not callable(open_container):
        return None, {"error": "Cannot access container: service unavailable"}
    try:
        open_result = await cast(
            Awaitable[object],
            open_container(container_id, player_id_uuid),
        )
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container access errors unpredictable
        return None, {"error": f"Cannot access container: {str(e)}"}
    new_token: object | None = None
    if isinstance(open_result, dict):
        new_token = cast(dict[str, object], open_result).get("mutation_token")
    return new_token, None


def _coerce_transfer_quantity(raw: object) -> int:
    """Parse quantity for transfers without using Any (inventory values may be str/int)."""
    if isinstance(raw, bool):
        return 1
    if isinstance(raw, int):
        return raw
    if isinstance(raw, str):
        stripped = raw.strip()
        if not stripped:
            return 1
        try:
            return int(stripped)
        except ValueError:
            return 1
    if isinstance(raw, float):
        return int(raw)
    return 1


def _int_transfer_qty(quantity: object | None, item_found: dict[str, object]) -> int:
    raw: object = quantity if quantity else item_found.get("quantity", 1)
    return _coerce_transfer_quantity(raw)


async def _ensure_item_instance_for_put(
    persistence: object, player: Player, item_found: dict[str, object], tq_int: int
) -> None:
    item_instance_id = item_found.get("item_instance_id")
    prototype_id = item_found.get("prototype_id") or item_found.get("item_id")
    ensure_item_instance = getattr(persistence, "ensure_item_instance", None)
    if not item_instance_id or not prototype_id or not callable(ensure_item_instance):
        return
    try:
        _ = ensure_item_instance(
            item_instance_id=item_instance_id,
            prototype_id=prototype_id,
            owner_type="player",
            owner_id=str(player.player_id),
            quantity=tq_int,
            metadata=item_found.get("metadata"),
            origin_source="inventory",
            origin_metadata={"player_id": str(player.player_id)},
        )
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Item instance errors unpredictable
        logger.warning("Failed to ensure item instance before transfer", error=str(e))


def _strip_cmd_field(value: object) -> str:
    return value.strip() if isinstance(value, str) else ""


def _app_state_container_service(request: object) -> object | None:
    app = cast(object | None, getattr(request, "app", None))
    if app is None:
        return None
    state = cast(object | None, getattr(app, "state", None))
    if state is None:
        return None
    return cast(object | None, getattr(state, "container_service", None))


def _extract_items_json_branch(container_found: object, container_id: UUID | None) -> tuple[object, UUID | None] | None:
    if not hasattr(container_found, "items_json"):
        return None
    items_json = getattr(container_found, "items_json", None)
    items: object = items_json or []
    cid = container_id
    if not cid:
        cid = cast(UUID | None, getattr(container_found, "container_instance_id", None))
    return items, cid


def _extract_items_dict_branch(data: dict[str, object], container_id: UUID | None) -> tuple[object, UUID | None]:
    items = data.get("items", [])
    cid = container_id
    if not cid:
        raw = data.get("container_id")
        cid = UUID(str(raw)) if raw is not None else None
    return items, cid


async def transfer_item_to_container(
    container_service: object,
    persistence: object,
    player: Player,
    container_id: UUID,
    item_found: dict[str, object],
    quantity: object | None,
) -> dict[str, object]:
    """Transfer an item to container from player inventory."""
    player_id_uuid = UUID(str(player.player_id))
    mutation_token, open_err = await _ensure_mutation_token(container_service, container_id, player_id_uuid)
    if open_err:
        return open_err

    try:
        if not item_found.get("item_instance_id") and not item_found.get("item_id"):
            return {"error": "Error: Item is missing required identification fields."}

        tq_int = _int_transfer_qty(quantity, item_found)
        await _ensure_item_instance_for_put(persistence, player, item_found, tq_int)

        transfer_to = getattr(container_service, "transfer_to_container", None)
        if not callable(transfer_to):
            return {"error": "Container transfer is unavailable."}
        _ = await cast(
            Awaitable[object],
            transfer_to(
                container_id=container_id,
                player_id=player_id_uuid,
                mutation_token=mutation_token,
                item=item_found,
                quantity=tq_int,
            ),
        )

        return {"success": True, "transfer_quantity": tq_int}
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container operation errors unpredictable
        logger.error("Error putting item in container", player=player.name, error=str(e))
        return {"error": str(e)}


async def validate_put_command_inputs(
    command_data: dict[str, object],
    request: object,
    connection_manager: object,
    player: Player,
) -> tuple[str, str, object | None, object, object, dict[str, object] | None, int | None] | dict[str, str]:
    """Validate and extract inputs for put command."""
    item_name = _strip_cmd_field(command_data.get("item", ""))
    container_name = _strip_cmd_field(command_data.get("container", ""))
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

    container_service = _app_state_container_service(request)
    if not container_service:
        return {"result": "Container service is unavailable."}

    room_manager = getattr(connection_manager, "room_manager", None)
    if not room_manager:
        return {"result": "Room manager is unavailable."}

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


def extract_items_from_container(container_found: object, container_id: UUID | None) -> tuple[object, UUID | None]:
    """
    Extract items and container ID from various container formats.

    Args:
        container_found: Container object (ContainerData, dict, or object with to_dict)
        container_id: Optional container ID

    Returns:
        Tuple of (container_items, container_id)
    """
    json_branch = _extract_items_json_branch(container_found, container_id)
    if json_branch is not None:
        return json_branch
    if isinstance(container_found, dict):
        return _extract_items_dict_branch(cast(dict[str, object], container_found), container_id)
    to_dict = getattr(container_found, "to_dict", None)
    if not callable(to_dict):
        return [], container_id
    as_dict = to_dict()
    if isinstance(as_dict, dict):
        return _extract_items_dict_branch(cast(dict[str, object], as_dict), container_id)
    return [], container_id


def parse_json_string_items(
    container_items: object, container_id: UUID | None, player: Player
) -> tuple[object, UUID | None] | None:
    """
    Parse container_items if it's a JSON string.

    Returns:
        Parsed items and container_id, or None if parsing failed
    """
    if isinstance(container_items, str):
        try:
            parsed: object = cast(object, json.loads(container_items))
        except (json.JSONDecodeError, ValueError) as e:
            logger.error(
                "Failed to parse container_items JSON string",
                player=player.name,
                container_id=str(container_id) if container_id else None,
                error=str(e),
                container_items=container_items,
            )
            return None
        return parsed, container_id
    return container_items, container_id


def filter_valid_items(
    container_items: list[object], container_id: UUID | None, player: Player
) -> list[dict[str, object]]:
    """Filter out any non-dictionary items from container_items."""
    filtered_items: list[dict[str, object]] = []
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
        filtered_items.append(cast(dict[str, object], item))

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
    container_found: object, container_id: UUID | None, player: Player
) -> tuple[list[dict[str, object]], UUID | None]:
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

    filtered_items = filter_valid_items(cast(list[object], container_items), container_id, player)

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
    container_items: list[dict[str, object]],
    item_name: str,
    _player: Player,
    _container_id: UUID | None,
) -> tuple[dict[str, object] | None, int | None]:
    """Find an item in container items by name or index."""
    try:
        index = int(item_name)
        if 1 <= index <= len(container_items):
            item_index = index - 1
            item_found = container_items[item_index]
            return item_found, item_index
    except ValueError:
        pass

    target_lower = item_name.lower()
    for idx, item in enumerate(container_items):
        item_name_check = str(item.get("item_name", item.get("name", ""))).lower()
        if target_lower in item_name_check:
            return item, idx

    return None, None


def _inventory_rows_from_transfer_result(result: object, fallback_inv: object) -> list[dict[str, object]]:
    """Build typed inventory rows from transfer_from_container result; invalid shapes fall back."""
    new_inventory: object = fallback_inv
    if isinstance(result, dict):
        res_d = cast(dict[str, object], result)
        candidate = res_d.get("player_inventory", fallback_inv)
        new_inventory = candidate if candidate is not None else fallback_inv
    rows_src: object = new_inventory
    if not isinstance(rows_src, list):
        rows_src = fallback_inv
    inv_rows: list[dict[str, object]] = []
    for row in cast(list[object], rows_src):
        if isinstance(row, dict):
            inv_rows.append(cast(dict[str, object], row))
    return inv_rows


def resolve_container_id(container_found: object, container_id: UUID | None) -> UUID | None:
    """Resolve container ID from container object."""
    if container_id:
        return container_id

    inst = getattr(container_found, "container_instance_id", None)
    if inst is not None:
        if isinstance(inst, UUID):
            return inst
        return UUID(str(cast(object, inst)))

    if isinstance(container_found, dict):
        cf = cast(dict[str, object], container_found)
        cid = cf.get("container_id")
        return UUID(str(cid)) if cid is not None else None

    return None


async def transfer_item_from_container(
    container_service: object,
    persistence: object,
    player: Player,
    container_id: UUID,
    item_found: dict[str, object],
    quantity: object | None,
) -> dict[str, object]:
    """Transfer an item from container to player inventory."""
    from .inventory_command_helpers import persist_player

    player_id_uuid = UUID(str(player.player_id))
    mutation_token, open_err = await _ensure_mutation_token(container_service, container_id, player_id_uuid)
    if open_err:
        return open_err

    try:
        tq_int = _int_transfer_qty(quantity, item_found)
        transfer_from = getattr(container_service, "transfer_from_container", None)
        if not callable(transfer_from):
            return {"error": "Container transfer is unavailable."}
        result = await cast(
            Awaitable[object],
            transfer_from(
                container_id=container_id,
                player_id=player_id_uuid,
                mutation_token=mutation_token,
                item=item_found,
                quantity=tq_int,
            ),
        )

        fallback_inv: object = player.get_inventory()
        inv_rows = _inventory_rows_from_transfer_result(result, fallback_inv)
        player.set_inventory(inv_rows)
        persist_error = await persist_player(persistence, player)
        if persist_error:
            return cast(dict[str, object], persist_error)

        item_display_name = item_found.get("item_name") or item_found.get("item_id", "item")
        return {
            "success": True,
            "transfer_quantity": tq_int,
            "item_display_name": item_display_name,
        }
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container operation errors unpredictable, must handle gracefully
        logger.error("Error getting item from container", player=player.name, error=str(e))
        return {"error": str(e)}


async def validate_get_command_inputs(
    command_data: dict[str, object], request: object, connection_manager: object
) -> tuple[str, str, object | None, object | None, object] | dict[str, str]:
    """Validate and extract inputs for get command."""
    item_name = _strip_cmd_field(command_data.get("item", ""))
    container_name = _strip_cmd_field(command_data.get("container", ""))
    quantity = command_data.get("quantity")

    if not item_name or not container_name:
        return {"result": "Usage: get <item> [from] <container> [quantity]"}

    room_manager = getattr(connection_manager, "room_manager", None)
    if not room_manager:
        return {"result": "Room manager is unavailable."}

    if container_name.lower() == "room":
        return item_name, container_name, quantity, None, room_manager

    container_service = _app_state_container_service(request)
    if not container_service:
        return {"result": "Container service is unavailable."}

    return item_name, container_name, quantity, container_service, room_manager
