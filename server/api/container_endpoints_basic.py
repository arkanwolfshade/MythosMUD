"""
Basic container operation endpoints (open, transfer, close).

These endpoints handle the core container interaction workflow:
opening containers, transferring items, and closing containers.
"""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Annotated, cast

from fastapi import APIRouter, Depends, Request
from pydantic import ValidationError

from ..auth.users import get_current_user
from ..dependencies import get_async_persistence, get_connection_manager
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
    emit_close_container_event,
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

if TYPE_CHECKING:
    from ..async_persistence import AsyncPersistenceLayer
    from ..realtime.connection_manager import ConnectionManager


def _convert_uuid_to_string(value: object) -> str | None:
    """Convert UUID-like object to string if truthy."""
    if value:
        return str(value)
    return cast(str | None, value)


def _convert_datetime_to_iso(value: object) -> str | None:
    """Convert datetime object to ISO format string."""
    if isinstance(value, datetime):
        return value.isoformat()
    return cast(str | None, value)


def _optional_str_field(value: object) -> str | None:
    """Return None or str for optional ContainerData string fields."""
    if value is None:
        return None
    return str(value)


def _optional_int_field(value: object) -> int | None:
    """Return None or int for optional ContainerData int fields."""
    if value is None:
        return None
    if isinstance(value, int) and not isinstance(value, bool):
        return value
    if isinstance(value, float):
        return int(value)
    return None


def _as_str_list(value: object) -> list[str]:
    """Coerce allowed_roles-style payloads to list[str]."""
    if not isinstance(value, list):
        return []
    # isinstance(list) leaves element types unknown to the checker
    items = cast(list[object], value)
    return [str(item) for item in items]


def _as_str_object_dict(value: object) -> dict[str, object]:
    """Coerce metadata-style payloads to dict[str, object]."""
    if not isinstance(value, dict):
        return {}
    raw = cast(dict[object, object], value)
    return {str(key): val for key, val in raw.items()}


def _as_inventory_dicts(value: object) -> list[dict[str, object]]:
    """Coerce items payload to list of string-keyed dicts."""
    if not isinstance(value, list):
        return []
    result: list[dict[str, object]] = []
    for item in cast(list[object], value):
        if isinstance(item, dict):
            raw = cast(dict[object, object], item)
            result.append({str(key): val for key, val in raw.items()})
    return result


def _as_str_object_mapping(value: object) -> dict[str, object]:
    """Coerce a service result payload to dict[str, object]."""
    if not isinstance(value, dict):
        return {}
    raw = cast(dict[object, object], value)
    return {str(key): val for key, val in raw.items()}


def _build_container_data_from_dict(
    container_dict: dict[str, object],
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
        source_type=_optional_str_field(container_dict.get("source_type")),
        owner_id=owner_id,
        room_id=_optional_str_field(container_dict.get("room_id")),
        entity_id=entity_id,
        lock_state=_optional_str_field(container_dict.get("lock_state")),
        capacity_slots=_optional_int_field(container_dict.get("capacity_slots")),
        weight_limit=_optional_int_field(container_dict.get("weight_limit")),
        decay_at=decay_at,
        allowed_roles=_as_str_list(container_dict.get("allowed_roles", [])),
        items=inventory_stacks,
        metadata=_as_str_object_dict(container_dict.get("metadata", {})),
        created_at=created_at,
        updated_at=updated_at,
    )


def _convert_container_dict_to_container_data(container_dict: dict[str, object]) -> ContainerData:
    """Convert container dictionary from ContainerComponent.model_dump() to ContainerData model."""
    container_id = _convert_uuid_to_string(container_dict.get("container_id")) or ""
    owner_id = _convert_uuid_to_string(container_dict.get("owner_id"))
    entity_id = _convert_uuid_to_string(container_dict.get("entity_id"))
    decay_at = _convert_datetime_to_iso(container_dict.get("decay_at"))
    created_at = _convert_datetime_to_iso(container_dict.get("created_at"))
    updated_at = _convert_datetime_to_iso(container_dict.get("updated_at"))

    inventory_stacks = _convert_inventory_list_to_inventory_stacks(_as_inventory_dicts(container_dict.get("items", [])))

    return _build_container_data_from_dict(
        container_dict, container_id, owner_id, entity_id, decay_at, created_at, updated_at, inventory_stacks
    )


def _convert_inventory_list_to_inventory_stacks(inventory_list: list[dict[str, object]]) -> list[InventoryStack]:
    """Convert list of inventory dicts to InventoryStack models."""
    stacks: list[InventoryStack] = []
    for item in inventory_list:
        item_copy: dict[str, object] = dict(item)
        # Expand minimal format (item_id, quantity) to full InventoryStack schema
        item_id = str(item_copy.get("item_id", "") or "")
        if "item_instance_id" not in item_copy:
            item_copy["item_instance_id"] = item_id
        if "prototype_id" not in item_copy:
            item_copy["prototype_id"] = item_id
        if "item_name" not in item_copy:
            item_copy["item_name"] = "Unknown"
        if "slot_type" not in item_copy:
            item_copy["slot_type"] = "backpack"
        # Convert weapon dict to WeaponStats if present
        weapon_raw = item_copy.get("weapon")
        if isinstance(weapon_raw, dict):
            try:
                item_copy["weapon"] = WeaponStats.model_validate(weapon_raw)
            except (ValidationError, TypeError):
                # If weapon dict doesn't match WeaponStats, keep as dict (model may drop it)
                pass
        stacks.append(InventoryStack.model_validate(item_copy))
    return stacks


logger = get_logger(__name__)


def _build_open_container_response(result: object) -> ContainerOpenResponse:
    """Map open_container service result to API response model."""
    result_map = _as_str_object_mapping(result)
    container_data = _convert_container_dict_to_container_data(_as_str_object_mapping(result_map.get("container")))
    return ContainerOpenResponse(
        container=container_data,
        mutation_token=str(result_map.get("mutation_token") or ""),
    )


def _build_transfer_response(result: object) -> ContainerTransferResponse:
    """Map transfer service result to API response model."""
    result_map = _as_str_object_mapping(result)
    container_data = _convert_container_dict_to_container_data(_as_str_object_mapping(result_map.get("container")))
    player_inventory_stacks = _convert_inventory_list_to_inventory_stacks(
        _as_inventory_dicts(result_map.get("player_inventory"))
    )
    return ContainerTransferResponse(
        container=container_data,
        player_inventory=player_inventory_stacks,
    )


async def open_container(
    request_data: OpenContainerRequest,
    request: Request,
    current_user: Annotated[User, Depends(get_current_user)],
    persistence: Annotated[AsyncPersistenceLayer, Depends(get_async_persistence)],
    connection_manager: Annotated[ConnectionManager, Depends(get_connection_manager)],
) -> ContainerOpenResponse:
    """Open a container; returns container data and mutation_token (rate limited)."""
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
        return _build_open_container_response(result)

    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container operation errors unpredictable, must create error context
        handle_open_container_exceptions(e, request, current_user, request_data.container_id)
        raise AssertionError(
            "handle_open_container_exceptions should always raise"
        ) from e  # Reason: Exception handler always raises, but mypy needs explicit return path


async def transfer_items(
    request_data: TransferContainerRequest,
    request: Request,
    current_user: Annotated[User, Depends(get_current_user)],
    persistence: Annotated[AsyncPersistenceLayer, Depends(get_async_persistence)],
    connection_manager: Annotated[ConnectionManager, Depends(get_connection_manager)],
) -> ContainerTransferResponse:
    """Transfer items between container and player inventory (rate limited; requires mutation_token)."""
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
        return _build_transfer_response(result)

    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container operation errors unpredictable, must create error context
        handle_transfer_items_exceptions(e, request, current_user, request_data.container_id)
        raise AssertionError(
            "handle_transfer_items_exceptions should always raise"
        ) from e  # Reason: Exception handler always raises, but mypy needs explicit return path


async def close_container(
    request_data: CloseContainerRequest,
    request: Request,
    current_user: Annotated[User, Depends(get_current_user)],
    persistence: Annotated[AsyncPersistenceLayer, Depends(get_async_persistence)],
    connection_manager: Annotated[ConnectionManager, Depends(get_connection_manager)],
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
        await emit_close_container_event(connection_manager, request_data.container_id, player_id, persistence)

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
    # FastAPI's decorator-style registration returns the endpoint; discard intentionally.
    _ = router.post("/open", response_model=ContainerOpenResponse)(open_container)
    _ = router.post("/transfer", response_model=ContainerTransferResponse)(transfer_items)
    _ = router.post("/close", response_model=ContainerCloseResponse)(close_container)
