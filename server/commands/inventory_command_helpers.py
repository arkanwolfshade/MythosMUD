"""Command helper functions for inventory operations."""

import inspect
from copy import deepcopy
from typing import Any, cast
from uuid import UUID

from ..exceptions import ValidationError as MythosValidationError
from ..models.player import Player
from ..schemas.inventory_schema import InventorySchemaValidationError
from ..services.inventory_service import InventoryCapacityError, InventoryService, InventoryValidationError
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user
from .inventory_item_matching import match_room_drop_by_name

logger = get_logger(__name__)


def resolve_state(request: Any) -> tuple[Any, Any]:
    """Resolve persistence and connection manager from request."""
    app = getattr(request, "app", None)
    state = getattr(app, "state", None)
    persistence = getattr(state, "persistence", None)
    connection_manager = getattr(state, "connection_manager", None)
    return persistence, connection_manager


async def resolve_player(
    persistence: Any,
    current_user: dict,
    fallback_player_name: str,
) -> tuple[Player | None, dict[str, str] | None]:
    """Resolve player from persistence and current user."""
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
    except Exception as exc:  # noqa: B904  # pragma: no cover - defensive logging path  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Persistence errors unpredictable, must handle gracefully
        logger.error("Persistence error resolving player", player=username, error=str(exc))
        return None, {"result": f"Error resolving player: {str(exc)}"}

    if not player:
        logger.warning("Player not found when handling inventory command", player=username)
        return None, {"result": "Player information not found."}

    return player, None


def clone_inventory(player: Player) -> list[dict[str, Any]]:
    """Clone player inventory for rollback purposes."""
    return deepcopy(player.get_inventory())


async def broadcast_room_event(
    connection_manager: Any,
    room_id: str,
    event: dict[str, Any],
    *,
    exclude_player: str | None = None,
) -> None:
    """Broadcast event to room, excluding optional player."""
    if not connection_manager or not hasattr(connection_manager, "broadcast_to_room"):
        return

    try:
        result = connection_manager.broadcast_to_room(str(room_id), event, exclude_player=exclude_player)
        if inspect.isawaitable(result):
            await result
    except Exception as exc:  # noqa: B904  # pragma: no cover - broadcast failures logged but not fatal  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Broadcast errors unpredictable, must not fail command
        logger.warning("Failed to broadcast room event", room_id=room_id, error=str(exc))


def persist_player(persistence: Any, player: Player) -> dict[str, str] | None:
    """Persist player changes, returning error dict on failure."""
    try:
        persistence.save_player(player)
        return None
    except InventorySchemaValidationError as exc:
        logger.error("Inventory schema validation during persistence", player=player.name, error=str(exc))
        return {"result": "Inventory data rejected by schema validation."}
    except Exception as exc:  # noqa: B904  # pragma: no cover - defensive logging path  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Persistence errors unpredictable, must handle gracefully
        logger.error("Error saving player inventory", player=player.name, error=str(exc))
        return {"result": "An error occurred while saving your inventory."}


def resolve_pickup_item_index(
    command_data: dict, drop_list: list[dict[str, Any]], player_name: str, player_id: UUID, room_id: str
) -> tuple[int | None, int | None, dict[str, str] | None]:
    """Resolve item index for pickup by index or search term."""
    index = command_data.get("index")
    search_term = command_data.get("search_term")
    resolved_index_zero: int | None = None

    if isinstance(index, int) and index >= 1:
        if index > len(drop_list):
            return None, None, {"result": "There is no such item to pick up."}
        resolved_index_zero = index - 1
        return resolved_index_zero, index, None
    if isinstance(search_term, str) and search_term.strip():
        match_index = match_room_drop_by_name(drop_list, search_term)
        if match_index is None:
            logger.info(
                "No matching room drop found for pickup",
                player=player_name,
                player_id=player_id,
                search_term=search_term,
                room_id=room_id,
            )
            return None, None, {"result": f"There is no item here matching '{search_term}'."}
        resolved_index_zero = match_index
        index = match_index + 1
        logger.debug(
            "Pickup resolved via fuzzy search",
            player=player_name,
            player_id=player_id,
            room_id=room_id,
            search_term=search_term,
            resolved_index=index,
        )
        return resolved_index_zero, index, None
    return None, None, {"result": "Usage: pickup <item-number|item-name> [quantity]"}


def prepare_extracted_stack(extracted_stack: dict[str, Any], player_name: str, player_id: UUID) -> dict[str, Any]:
    """Prepare extracted stack for inventory addition, ensuring it's a dict copy."""
    if isinstance(extracted_stack, dict):
        extracted_stack = dict(extracted_stack)  # Create a copy to avoid mutating the original
        logger.debug(
            "Pickup: item will be added to general inventory",
            player=player_name,
            player_id=player_id,
            item_id=extracted_stack.get("item_id"),
            item_name=extracted_stack.get("item_name"),
        )
    return extracted_stack


def ensure_item_instance_for_pickup(
    persistence: Any, extracted_stack: dict[str, Any], player: Player, room_id: str
) -> None:
    """Ensure item instance exists in database for picked up item."""
    item_instance_id = extracted_stack.get("item_instance_id")
    prototype_id = extracted_stack.get("prototype_id") or extracted_stack.get("item_id")

    if item_instance_id and prototype_id:
        try:
            persistence.ensure_item_instance(
                item_instance_id=item_instance_id,
                prototype_id=prototype_id,
                owner_type="player",
                owner_id=str(player.player_id),
                quantity=extracted_stack.get("quantity", 1),
                metadata=extracted_stack.get("metadata"),
                origin_source="pickup",
                origin_metadata={"room_id": room_id},
            )
            logger.debug(
                "Item instance ensured for picked up item",
                item_instance_id=item_instance_id,
                prototype_id=prototype_id,
                player_id=str(player.player_id),
            )
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Item instance errors unpredictable, must not fail pickup
            logger.warning(
                "Failed to ensure item instance for picked up item",
                item_instance_id=item_instance_id,
                prototype_id=prototype_id,
                error=str(e),
            )


async def add_pickup_to_inventory(
    inventory_service: InventoryService,
    player: Player,
    extracted_stack: dict[str, Any],
    room_manager: Any,
    room_id: str,
) -> tuple[list[dict[str, Any]] | None, dict[str, str] | None]:
    """Add picked up item to inventory, returning updated inventory or error."""
    previous_inventory = clone_inventory(player)

    try:
        updated_inventory = inventory_service.add_stack(previous_inventory, extracted_stack)
        return cast(list[dict[str, Any]], updated_inventory), None
    except (InventoryCapacityError, InventoryValidationError) as exc:
        room_manager.add_room_drop(room_id, extracted_stack)
        logger.info(
            "Pickup rejected",
            player=player.name,
            player_id=player.player_id,
            reason=str(exc),
            room_id=room_id,
        )
        return None, {"result": f"You cannot pick that up: {str(exc)}"}


async def build_and_broadcast_inventory_event(
    connection_manager: Any,
    player: Player,
    room_id: str,
    event_type: str,
    event_data: dict[str, Any],
) -> None:
    """Build and broadcast an inventory-related event to the room."""
    from ..realtime.envelope import build_event

    event = build_event(
        event_type,
        event_data,
        room_id=room_id,
        player_id=str(player.player_id),
        connection_manager=connection_manager,
    )

    await broadcast_room_event(
        connection_manager,
        room_id,
        event,
        exclude_player=str(player.player_id) if getattr(player, "player_id", None) else None,
    )


async def resolve_state_and_player(
    request: Any, current_user: dict, player_name: str
) -> tuple[Any, Any, Player | None, dict[str, str] | None]:
    """Resolve state and player, returning (persistence, connection_manager, player, error)."""
    persistence, connection_manager = resolve_state(request)
    player, error = await resolve_player(persistence, current_user, player_name)
    return persistence, connection_manager, player, error


def get_room_manager(connection_manager: Any, player: Player) -> tuple[Any, dict[str, str] | None]:
    """Get room manager from connection manager, returning (room_manager, error)."""
    room_manager = getattr(connection_manager, "room_manager", None)
    if not room_manager:
        logger.warning(
            "Room manager unavailable", player=player.name, player_id=player.player_id, room_id=player.current_room_id
        )
        return None, {"result": "Room inventory is unavailable."}
    return room_manager, None


def remove_item_from_inventory(player: Player, item_index: int | None, transfer_quantity: int) -> None:
    """Remove or update item quantity in player inventory after transfer."""
    inventory = player.get_inventory()
    new_inventory = inventory.copy()
    if item_index is not None and 0 <= item_index < len(new_inventory):
        item_to_remove = new_inventory[item_index]
        current_quantity = item_to_remove.get("quantity", 1)
        if transfer_quantity >= current_quantity:
            new_inventory.pop(item_index)
        else:
            new_inventory[item_index] = item_to_remove.copy()
            new_inventory[item_index]["quantity"] = current_quantity - transfer_quantity
    player.set_inventory(new_inventory)
