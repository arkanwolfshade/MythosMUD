"""
Container WebSocket event emission for unified container system.

As documented in the restricted archives of Miskatonic University, container
WebSocket events provide real-time synchronization of container state across
all connected players. These events must be properly formatted and broadcast
to ensure consistent game state.
"""

# pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: WebSocket event emission requires many parameters for context and event routing

from __future__ import annotations

from datetime import datetime
from typing import Any, cast
from uuid import UUID

from ..models.container import ContainerComponent
from ..realtime.envelope import build_event
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


async def emit_container_opened(
    connection_manager: Any,
    container: ContainerComponent,
    player_id: UUID,
    mutation_token: str,
    expires_at: datetime,
) -> dict[str, Any]:
    """
    Emit container.opened event to the opening player.

    Args:
        connection_manager: ConnectionManager instance
        container: ContainerComponent that was opened
        player_id: UUID of the player who opened the container
        mutation_token: Mutation token for this container session
        expires_at: Timestamp when the mutation token expires

    Returns:
        dict: Delivery status from send_personal_message
    """
    logger.info(
        "Emitting container.opened event",
        container_id=str(container.container_id),
        player_id=str(player_id),
    )

    # Build event data
    event_data = {
        "container": container.model_dump(),
        "owner_id": str(container.owner_id) if container.owner_id else None,
        "mutation_token": mutation_token,
        "expires_at": expires_at.isoformat(),
    }

    # Build event envelope
    event = build_event(
        event_type="container.opened",
        data=event_data,
        player_id=player_id,
        connection_manager=connection_manager,
    )

    # Send to player
    delivery_status = await connection_manager.send_personal_message(player_id, event)

    logger.debug(
        "container.opened event delivered",
        container_id=str(container.container_id),
        player_id=str(player_id),
        delivery_status=delivery_status,
    )

    result: dict[str, Any] = cast(dict[str, Any], delivery_status)
    return result


async def emit_container_opened_to_room(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: WebSocket event emission requires many parameters for context and event routing
    connection_manager: Any,
    container: ContainerComponent,
    room_id: str,
    actor_id: UUID,
    mutation_token: str,
    expires_at: datetime,
) -> dict[str, Any]:
    """
    Emit container.opened event to all players in the room.

    This is used to notify other players that someone has opened a container,
    which may be relevant for environmental containers or corpse looting.

    Args:
        connection_manager: ConnectionManager instance
        container: ContainerComponent that was opened
        room_id: Room ID where the container is located
        actor_id: UUID of the player who opened the container
        mutation_token: Mutation token for this container session
        expires_at: Timestamp when the mutation token expires

    Returns:
        dict: Broadcast delivery statistics
    """
    logger.info(
        "Emitting container.opened event to room",
        container_id=str(container.container_id),
        room_id=room_id,
        actor_id=str(actor_id),
    )

    # Build event data
    event_data = {
        "container": container.model_dump(),
        "owner_id": str(container.owner_id) if container.owner_id else None,
        "actor_id": str(actor_id),
        "mutation_token": mutation_token,
        "expires_at": expires_at.isoformat(),
    }

    # Broadcast to room
    delivery_stats = await connection_manager.broadcast_room_event(
        event_type="container.opened",
        room_id=room_id,
        data=event_data,
    )

    logger.debug(
        "container.opened event broadcast to room",
        container_id=str(container.container_id),
        room_id=room_id,
        delivery_stats=delivery_stats,
    )

    result: dict[str, Any] = cast(dict[str, Any], delivery_stats)
    return result


async def emit_container_updated(
    connection_manager: Any,
    container_id: UUID,
    room_id: str,
    diff: dict[str, Any],
    actor_id: UUID,
) -> dict[str, Any]:
    """
    Emit container.updated event with diff to room occupants.

    Args:
        connection_manager: ConnectionManager instance
        container_id: UUID of the container that was updated
        room_id: Room ID where the container is located
        diff: Dictionary describing what changed (e.g., items added/removed)
        actor_id: UUID of the player who made the change

    Returns:
        dict: Broadcast delivery statistics
    """
    logger.info(
        "Emitting container.updated event",
        container_id=str(container_id),
        room_id=room_id,
        actor_id=str(actor_id),
    )

    # Build event data
    event_data = {
        "container_id": str(container_id),
        "diff": diff,
        "actor_id": str(actor_id),
    }

    # Broadcast to room
    delivery_stats = await connection_manager.broadcast_room_event(
        event_type="container.updated",
        room_id=room_id,
        data=event_data,
    )

    logger.debug(
        "container.updated event broadcast",
        container_id=str(container_id),
        room_id=room_id,
        delivery_stats=delivery_stats,
    )

    result: dict[str, Any] = cast(dict[str, Any], delivery_stats)
    return result


async def emit_container_closed(
    connection_manager: Any,
    container_id: UUID,
    room_id: str,
    player_id: UUID,
) -> dict[str, Any]:
    """
    Emit container.closed event to room occupants.

    Args:
        connection_manager: ConnectionManager instance
        container_id: UUID of the container that was closed
        room_id: Room ID where the container is located
        player_id: UUID of the player who closed the container

    Returns:
        dict: Broadcast delivery statistics
    """
    logger.info(
        "Emitting container.closed event",
        container_id=str(container_id),
        room_id=room_id,
        player_id=str(player_id),
    )

    # Build event data
    event_data = {
        "container_id": str(container_id),
    }

    # Broadcast to room
    delivery_stats = await connection_manager.broadcast_room_event(
        event_type="container.closed",
        room_id=room_id,
        data=event_data,
    )

    logger.debug(
        "container.closed event broadcast",
        container_id=str(container_id),
        room_id=room_id,
        delivery_stats=delivery_stats,
    )

    result: dict[str, Any] = cast(dict[str, Any], delivery_stats)
    return result


async def emit_container_decayed(
    connection_manager: Any,
    container_id: UUID,
    room_id: str,
) -> dict[str, Any]:
    """
    Emit container.decayed event to room occupants.

    This event is emitted when a corpse container decays and is cleaned up.

    Args:
        connection_manager: ConnectionManager instance
        container_id: UUID of the container that decayed
        room_id: Room ID where the container was located

    Returns:
        dict: Broadcast delivery statistics
    """
    logger.info(
        "Emitting container.decayed event",
        container_id=str(container_id),
        room_id=room_id,
    )

    # Build event data
    event_data = {
        "container_id": str(container_id),
        "room_id": room_id,
    }

    # Broadcast to room
    delivery_stats = await connection_manager.broadcast_room_event(
        event_type="container.decayed",
        room_id=room_id,
        data=event_data,
    )

    logger.debug(
        "container.decayed event broadcast",
        container_id=str(container_id),
        room_id=room_id,
        delivery_stats=delivery_stats,
    )

    result: dict[str, Any] = cast(dict[str, Any], delivery_stats)
    return result
