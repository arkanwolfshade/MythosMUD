"""
WebSocket event emission helpers for container API endpoints.

This module contains functions to emit WebSocket events for container operations,
including opening, closing, transferring items, and loot-all operations.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any
from uuid import UUID

from ..models.container import ContainerComponent
from ..services.container_websocket_events import (
    emit_container_opened,
    emit_container_opened_to_room,
    emit_container_updated,
)
from ..structured_logging.enhanced_logging_config import get_logger
from .container_models import LootAllRequest

if TYPE_CHECKING:
    from .container_models import TransferContainerRequest

logger = get_logger(__name__)


async def emit_container_opened_events(
    connection_manager: Any, result: dict[str, Any], player_id: UUID, container_id: UUID
) -> None:
    """
    Emit WebSocket events for container opening.

    Args:
        connection_manager: ConnectionManager instance for emitting events
        result: Container operation result dictionary
        player_id: Player UUID
        container_id: Container UUID

    AI: Updated to accept connection_manager as parameter instead of accessing app.state.
        This enables proper dependency injection and testability.
    """
    try:
        if connection_manager:
            from datetime import UTC, datetime, timedelta

            container = ContainerComponent.model_validate(result["container"])
            mutation_token = result["mutation_token"]
            expires_at = (
                datetime.now(UTC) + timedelta(minutes=5)
            )  # TODO: Get actual expiry from mutation guard  # pylint: disable=fixme  # Reason: Placeholder until mutation guard expiry API is implemented

            await emit_container_opened(
                connection_manager=connection_manager,
                container=container,
                player_id=player_id,
                mutation_token=mutation_token,
                expires_at=expires_at,
            )

            if container.room_id:
                await emit_container_opened_to_room(
                    connection_manager=connection_manager,
                    container=container,
                    room_id=container.room_id,
                    actor_id=player_id,
                    mutation_token=mutation_token,
                    expires_at=expires_at,
                )
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Event emission errors unpredictable, must not fail request
        logger.warning(
            "Failed to emit container.opened event",
            error=str(e),
            container_id=str(container_id),
            player_id=str(player_id),
        )


async def emit_transfer_event(
    connection_manager: Any,
    request_data: TransferContainerRequest,
    result: dict[str, Any],
    player_id: UUID,
) -> None:
    """
    Emit WebSocket event for transfer operation.

    Args:
        connection_manager: ConnectionManager instance for emitting events
        request_data: Transfer request data
        result: Container operation result dictionary
        player_id: Player UUID

    AI: Updated to accept connection_manager as parameter instead of accessing app.state.
        This enables proper dependency injection and testability.
    """
    try:
        if connection_manager and result.get("container"):
            container = ContainerComponent.model_validate(result["container"])
            if container.room_id:
                diff = {
                    "items": {
                        "direction": request_data.direction,
                        "stack": request_data.stack,
                        "quantity": request_data.quantity,
                    },
                }
                await emit_container_updated(
                    connection_manager=connection_manager,
                    container_id=request_data.container_id,
                    room_id=container.room_id,
                    diff=diff,
                    actor_id=player_id,
                )
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Event emission errors unpredictable, must not fail request
        logger.warning(
            "Failed to emit container.updated event",
            error=str(e),
            container_id=str(request_data.container_id),
            player_id=str(player_id),
        )


async def _emit_close_container_event(
    connection_manager: Any,
    container_id: UUID,
    player_id: UUID,
    persistence: Any,
) -> None:
    """
    Emit WebSocket event for container closing.

    Args:
        connection_manager: ConnectionManager instance
        container_id: Container UUID
        player_id: Player UUID
        persistence: Persistence layer instance

    AI: Extracted to reduce complexity in close_container endpoint.
    """
    try:
        if connection_manager:
            # Get container to find room_id
            container_data = await persistence.get_container(container_id)
            if container_data:
                from ..services.container_websocket_events import emit_container_closed

                container = ContainerComponent.model_validate(container_data)
                if container.room_id:
                    await emit_container_closed(
                        connection_manager=connection_manager,
                        container_id=container_id,
                        room_id=container.room_id,
                        player_id=player_id,
                    )
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Event emission errors unpredictable, must not fail request
        logger.warning(
            "Failed to emit container.closed event",
            error=str(e),
            container_id=str(container_id),
            player_id=str(player_id),
        )


async def emit_loot_all_event(
    connection_manager: Any,
    request_data: LootAllRequest,
    final_container: ContainerComponent,
    player_id: UUID,
    container: ContainerComponent,
) -> None:
    """
    Emit WebSocket event for loot_all operation.

    Args:
        connection_manager: ConnectionManager instance for emitting events
        request_data: Loot all request data
        final_container: Final container state after looting
        player_id: Player UUID
        container: Original container component

    AI: Updated to accept connection_manager as parameter instead of accessing app.state.
        This enables proper dependency injection and testability.
    """
    try:
        if connection_manager and final_container.room_id:
            diff = {
                "items": {
                    "loot_all": True,
                    "items_removed": len(container.items) - len(final_container.items),
                },
            }
            await emit_container_updated(
                connection_manager=connection_manager,
                container_id=request_data.container_id,
                room_id=final_container.room_id,
                diff=diff,
                actor_id=player_id,
            )
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Event emission errors unpredictable, must not fail request
        logger.warning(
            "Failed to emit container.updated event for loot-all",
            error=str(e),
            container_id=str(request_data.container_id),
            player_id=str(player_id),
        )
