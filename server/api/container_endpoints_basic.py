"""
Basic container operation endpoints (open, transfer, close).

These endpoints handle the core container interaction workflow:
opening containers, transferring items, and closing containers.
"""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any, cast

from fastapi import APIRouter, Depends, Request
from pydantic import ValidationError

from ..auth.users import get_current_user
from ..dependencies import AsyncPersistenceDep, ConnectionManagerDep
from ..models.user import User
from ..schemas.containers import (
    ContainerCloseResponse,
    ContainerOpenResponse,
    ContainerTransferResponse,
)
from ..schemas.containers.container_data import ContainerData, InventoryStack
from ..schemas.game.weapon import WeaponStats
from ..structured_logging.enhanced_logging_config import get_logger
from .container_events import (
    _emit_close_container_event,
    emit_container_opened_events,
    emit_transfer_event,
)
from .container_exception_handlers import (
    handle_close_container_exceptions,
    handle_open_container_exceptions,
    handle_transfer_items_exceptions,
)
from .container_helpers import (
    apply_rate_limiting_for_close_container,
    apply_rate_limiting_for_open_container,
    apply_rate_limiting_for_transfer,
    execute_transfer,
    get_container_service,
    get_player_id_from_user,
    validate_user_for_close_container,
    validate_user_for_open_container,
    validate_user_for_transfer,
)
from .container_models import CloseContainerRequest, OpenContainerRequest, TransferContainerRequest


def _convert_uuid_to_string(value: Any) -> str | None:
    """Convert UUID-like object to string if it has __str__ method."""
    if value and hasattr(value, "__str__"):
        return str(value)
    return cast(str | None, value)


def _convert_datetime_to_iso(value: Any) -> str | None:
    """Convert datetime object to ISO format string."""
    if isinstance(value, datetime):
        return value.isoformat()
    return cast(str | None, value)


def _build_container_data_from_dict(
    container_dict: dict[str, Any],
    container_id: str,
    owner_id: str | None,
    entity_id: str | None,
    decay_at: str | None,
    created_at: str | None,
    updated_at: str | None,
    inventory_stacks: list[InventoryStack],
) -> ContainerData:
    """Build ContainerData model from dictionary and converted values."""
    return ContainerData(
        container_id=container_id,
        source_type=container_dict.get("source_type"),
        owner_id=owner_id,
        room_id=container_dict.get("room_id"),
        entity_id=entity_id,
        lock_state=container_dict.get("lock_state"),
        capacity_slots=container_dict.get("capacity_slots"),
        weight_limit=container_dict.get("weight_limit"),
        decay_at=decay_at,
        allowed_roles=container_dict.get("allowed_roles", []),
        items=inventory_stacks,
        metadata=container_dict.get("metadata", {}),
        created_at=created_at,
        updated_at=updated_at,
    )


def _convert_container_dict_to_container_data(container_dict: dict[str, Any]) -> ContainerData:
    """Convert container dictionary from ContainerComponent.model_dump() to ContainerData model."""
    # Handle UUID conversion and datetime serialization
    container_id = _convert_uuid_to_string(container_dict.get("container_id")) or ""
    owner_id = _convert_uuid_to_string(container_dict.get("owner_id"))
    entity_id = _convert_uuid_to_string(container_dict.get("entity_id"))
    decay_at = _convert_datetime_to_iso(container_dict.get("decay_at"))
    created_at = _convert_datetime_to_iso(container_dict.get("created_at"))
    updated_at = _convert_datetime_to_iso(container_dict.get("updated_at"))

    # Convert items to InventoryStack models
    items = container_dict.get("items", [])
    inventory_stacks = _convert_inventory_list_to_inventory_stacks(items)

    return _build_container_data_from_dict(
        container_dict, container_id, owner_id, entity_id, decay_at, created_at, updated_at, inventory_stacks
    )


def _convert_inventory_list_to_inventory_stacks(inventory_list: list[dict[str, Any]]) -> list[InventoryStack]:
    """Convert list of inventory dicts to InventoryStack models."""
    stacks: list[InventoryStack] = []
    for item in inventory_list:
        if isinstance(item, dict):
            item_copy = dict(item)
            # Expand minimal format (item_id, quantity) to full InventoryStack schema
            item_id = item_copy.get("item_id", "")
            if "item_instance_id" not in item_copy:
                item_copy["item_instance_id"] = item_id
            if "prototype_id" not in item_copy:
                item_copy["prototype_id"] = item_id
            if "item_name" not in item_copy:
                item_copy["item_name"] = "Unknown"
            if "slot_type" not in item_copy:
                item_copy["slot_type"] = "backpack"
            # Convert weapon dict to WeaponStats if present
            if "weapon" in item_copy and isinstance(item_copy["weapon"], dict):
                try:
                    item_copy["weapon"] = WeaponStats(**item_copy["weapon"])
                except (ValidationError, TypeError):
                    # If weapon dict doesn't match WeaponStats, keep as dict (will be filtered by model)
                    # ValidationError: Pydantic validation failed
                    # TypeError: Invalid argument types for model construction
                    pass
            stacks.append(InventoryStack(**item_copy))
    return stacks


if TYPE_CHECKING:
    from ..async_persistence import AsyncPersistenceLayer
    from ..realtime.connection_manager import ConnectionManager

logger = get_logger(__name__)


async def open_container(
    request_data: OpenContainerRequest,
    request: Request,
    current_user: User = Depends(get_current_user),
    persistence: AsyncPersistenceLayer = AsyncPersistenceDep,
    connection_manager: ConnectionManager = ConnectionManagerDep,
) -> ContainerOpenResponse:
    """
    Open a container for interaction.

    Initiates interaction with a container in the player's current room or inventory.
    Returns container data and a mutation token for subsequent operations.

    Rate limited to 20 requests per 60 seconds per player.

    Args:
        request_data: OpenContainerRequest with container_id
        request: FastAPI Request object
        current_user: Current authenticated user
        persistence: Persistence layer instance

    Returns:
        dict containing container data and mutation_token

    Raises:
        HTTPException(404): Container not found
        HTTPException(403): Access denied
        HTTPException(409): Container already open
        HTTPException(423): Container is locked
        HTTPException(429): Rate limit exceeded
    """
    validate_user_for_open_container(current_user, request)
    apply_rate_limiting_for_open_container(current_user, request)

    try:
        player_id = await get_player_id_from_user(current_user, persistence)
        container_service = get_container_service(persistence)

        result = await container_service.open_container(request_data.container_id, player_id)

        await emit_container_opened_events(connection_manager, result, player_id, request_data.container_id)

        logger.info(
            "Container opened",
            container_id=str(request_data.container_id),
            player_id=str(player_id),
            user_id=str(current_user.id),
        )

        # Convert container dict to ContainerData model
        container_data = _convert_container_dict_to_container_data(result["container"])

        return ContainerOpenResponse(
            container=container_data,
            mutation_token=result["mutation_token"],
        )

    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container operation errors unpredictable, must create error context
        handle_open_container_exceptions(e, request, current_user, request_data.container_id)
        raise AssertionError(
            "handle_open_container_exceptions should always raise"
        ) from e  # Reason: Exception handler always raises, but mypy needs explicit return path


async def transfer_items(
    request_data: TransferContainerRequest,
    request: Request,
    current_user: User = Depends(get_current_user),
    persistence: AsyncPersistenceLayer = AsyncPersistenceDep,
    connection_manager: ConnectionManager = ConnectionManagerDep,
) -> ContainerTransferResponse:
    """
    Transfer items between container and player inventory.

    Moves items bidirectionally between container and player inventory.
    Requires a valid mutation token from open_container.

    Rate limited to 20 requests per 60 seconds per player.

    Args:
        request_data: TransferContainerRequest with container_id, mutation_token, direction, stack, quantity
        request: FastAPI Request object
        current_user: Current authenticated user
        persistence: Persistence layer instance

    Returns:
        dict containing updated container and player_inventory

    Raises:
        HTTPException(400): Invalid stack or token
        HTTPException(403): Access denied
        HTTPException(409): Capacity exceeded
        HTTPException(412): Stale mutation token
        HTTPException(429): Rate limit exceeded
    """
    validate_user_for_transfer(current_user, request)
    apply_rate_limiting_for_transfer(current_user, request)

    try:
        player_id = await get_player_id_from_user(current_user, persistence)
        container_service = get_container_service(persistence)

        result = await execute_transfer(container_service, request_data, player_id)
        await emit_transfer_event(connection_manager, request_data, result, player_id)

        logger.info(
            "Items transferred",
            container_id=str(request_data.container_id),
            player_id=str(player_id),
            direction=request_data.direction,
            quantity=request_data.quantity,
        )

        # Convert container and inventory dicts to models
        container_data = _convert_container_dict_to_container_data(result["container"])
        player_inventory_stacks = _convert_inventory_list_to_inventory_stacks(result["player_inventory"])

        return ContainerTransferResponse(
            container=container_data,
            player_inventory=player_inventory_stacks,
        )

    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container operation errors unpredictable, must create error context
        handle_transfer_items_exceptions(e, request, current_user, request_data.container_id)
        raise AssertionError(
            "handle_transfer_items_exceptions should always raise"
        ) from e  # Reason: Exception handler always raises, but mypy needs explicit return path


async def close_container(
    request_data: CloseContainerRequest,
    request: Request,
    current_user: User = Depends(get_current_user),
    persistence: AsyncPersistenceLayer = AsyncPersistenceDep,
    connection_manager: ConnectionManager = ConnectionManagerDep,
) -> ContainerCloseResponse:
    """
    Close a container and release the mutation guard.

    Releases the mutation guard and closes the container UI.
    Requires a valid mutation token from open_container.

    Rate limited to 20 requests per 60 seconds per player.

    Args:
        request_data: CloseContainerRequest with container_id and mutation_token
        request: FastAPI Request object
        current_user: Current authenticated user
        persistence: Persistence layer instance

    Returns:
        dict with status="closed"

    Raises:
        HTTPException(400): Invalid token
        HTTPException(404): Container not found
        HTTPException(429): Rate limit exceeded
    """
    validate_user_for_close_container(current_user, request)
    apply_rate_limiting_for_close_container(current_user, request)

    try:
        # Get player_id from user
        player_id = await get_player_id_from_user(current_user, persistence)

        # Get container service
        container_service = get_container_service(persistence)

        # Close container
        await container_service.close_container(request_data.container_id, player_id, request_data.mutation_token)

        # Emit WebSocket event
        await _emit_close_container_event(connection_manager, request_data.container_id, player_id, persistence)

        logger.info(
            "Container closed",
            container_id=str(request_data.container_id),
            player_id=str(player_id),
            user_id=str(current_user.id),
        )

        return ContainerCloseResponse(status="closed")

    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container operation errors unpredictable, must create error context
        handle_close_container_exceptions(e, request, current_user, request_data.container_id)
        raise AssertionError(
            "handle_close_container_exceptions should always raise"
        ) from e  # Reason: Exception handler always raises, but mypy needs explicit return path


def register_basic_endpoints(router: APIRouter) -> None:
    """Register basic container operation endpoints (open, transfer, close) to the router."""
    router.post("/open", response_model=ContainerOpenResponse)(open_container)
    router.post("/transfer", response_model=ContainerTransferResponse)(transfer_items)
    router.post("/close", response_model=ContainerCloseResponse)(close_container)
