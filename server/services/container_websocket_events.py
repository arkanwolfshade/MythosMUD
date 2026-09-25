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
from typing import Protocol
from uuid import UUID

from ..models.container import ContainerComponent
from ..realtime.envelope import build_event
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class ContainerConnectionManagerLike(Protocol):
    """Minimal shape these emitters need from a connection manager.

    sequence_counter is required so this satisfies build_event's own
    _SupportsEventSequence protocol.
    """

    sequence_counter: int

    async def send_personal_message(self, player_id: UUID, event: dict[str, object]) -> dict[str, object]:
        """Send event to a single player; returns delivery status."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body (not just a docstring) for a non-None Protocol return type

    async def broadcast_room_event(self, event_type: str, room_id: str, data: dict[str, object]) -> dict[str, object]:
        """Broadcast an event to everyone in a room; returns delivery stats."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body (not just a docstring) for a non-None Protocol return type


async def emit_container_opened(
    connection_manager: ContainerConnectionManagerLike,
    container: ContainerComponent,
    player_id: UUID,
    mutation_token: str,
    expires_at: datetime,
) -> dict[str, object]:
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

    event_data: dict[str, object] = {
        "container": container.model_dump(),
        "owner_id": str(container.owner_id) if container.owner_id else None,
        "mutation_token": mutation_token,
        "expires_at": expires_at.isoformat(),
    }

    event = build_event(
        event_type="container.opened",
        data=event_data,
        player_id=player_id,
        connection_manager=connection_manager,
    )

    delivery_status = await connection_manager.send_personal_message(player_id, event)

    logger.debug(
        "container.opened event delivered",
        container_id=str(container.container_id),
        player_id=str(player_id),
        delivery_status=delivery_status,
    )

    return delivery_status


async def emit_container_opened_to_room(
    connection_manager: ContainerConnectionManagerLike,
    container: ContainerComponent,
    room_id: str,
    actor_id: UUID,
) -> dict[str, object]:
    """
    Notify room occupants that someone opened a container.

    Deliberately omits mutation_token/expires_at: those are the opener's
    credentials for this session and must not be usable by anyone else.

    Args:
        connection_manager: ConnectionManager instance
        container: ContainerComponent that was opened
        room_id: Room ID where the container is located
        actor_id: UUID of the player who opened the container

    Returns:
        dict: Broadcast delivery statistics
    """
    logger.info(
        "Emitting container.opened event to room",
        container_id=str(container.container_id),
        room_id=room_id,
        actor_id=str(actor_id),
    )

    event_data: dict[str, object] = {
        "container": container.model_dump(),
        "owner_id": str(container.owner_id) if container.owner_id else None,
        "actor_id": str(actor_id),
    }

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

    return delivery_stats


async def emit_container_updated(
    connection_manager: ContainerConnectionManagerLike,
    container: ContainerComponent,
    actor_id: UUID,
) -> dict[str, object]:
    """
    Emit container.updated with the full container snapshot.

    Always sent personally to the actor (so wearable containers, which have no
    room_id, still reach the player who changed them), plus a room broadcast
    when the container has a room_id.

    Args:
        connection_manager: ConnectionManager instance
        container: ContainerComponent after the mutation
        actor_id: UUID of the player who made the change

    Returns:
        dict: Delivery status from the personal send
    """
    logger.info(
        "Emitting container.updated event",
        container_id=str(container.container_id),
        room_id=container.room_id,
        actor_id=str(actor_id),
    )

    event_data: dict[str, object] = {
        "container_id": str(container.container_id),
        "container": container.model_dump(),
        "actor_id": str(actor_id),
    }

    event = build_event(
        event_type="container.updated",
        data=event_data,
        player_id=actor_id,
        connection_manager=connection_manager,
    )
    delivery_status = await connection_manager.send_personal_message(actor_id, event)

    if container.room_id:
        _ = await connection_manager.broadcast_room_event(
            event_type="container.updated",
            room_id=container.room_id,
            data=event_data,
        )

    logger.debug(
        "container.updated event delivered",
        container_id=str(container.container_id),
        actor_id=str(actor_id),
        delivery_status=delivery_status,
    )

    return delivery_status


async def emit_container_closed(
    connection_manager: ContainerConnectionManagerLike,
    container_id: UUID,
    room_id: str | None,
    player_id: UUID,
) -> dict[str, object]:
    """
    Emit container.closed personally to the closer, plus a room broadcast
    when the container has a room_id.

    Args:
        connection_manager: ConnectionManager instance
        container_id: UUID of the container that was closed
        room_id: Room ID where the container is located, or None (e.g. wearables)
        player_id: UUID of the player who closed the container

    Returns:
        dict: Delivery status from the personal send
    """
    logger.info(
        "Emitting container.closed event",
        container_id=str(container_id),
        room_id=room_id,
        player_id=str(player_id),
    )

    event_data: dict[str, object] = {
        "container_id": str(container_id),
    }

    event = build_event(
        event_type="container.closed",
        data=event_data,
        player_id=player_id,
        connection_manager=connection_manager,
    )
    delivery_status = await connection_manager.send_personal_message(player_id, event)

    if room_id:
        _ = await connection_manager.broadcast_room_event(
            event_type="container.closed",
            room_id=room_id,
            data=event_data,
        )

    logger.debug(
        "container.closed event delivered",
        container_id=str(container_id),
        player_id=str(player_id),
        delivery_status=delivery_status,
    )

    return delivery_status


async def emit_container_created(
    connection_manager: ContainerConnectionManagerLike,
    container: ContainerComponent,
    room_id: str,
) -> dict[str, object]:
    """
    Emit container.created to room occupants (e.g. a fresh corpse).

    Args:
        connection_manager: ConnectionManager instance
        container: ContainerComponent that was created
        room_id: Room ID where the container now sits

    Returns:
        dict: Broadcast delivery statistics
    """
    logger.info(
        "Emitting container.created event",
        container_id=str(container.container_id),
        room_id=room_id,
    )

    event_data: dict[str, object] = {"container": container.model_dump()}

    delivery_stats = await connection_manager.broadcast_room_event(
        event_type="container.created",
        room_id=room_id,
        data=event_data,
    )

    logger.debug(
        "container.created event broadcast",
        container_id=str(container.container_id),
        room_id=room_id,
        delivery_stats=delivery_stats,
    )

    return delivery_stats


async def emit_container_decayed(
    connection_manager: ContainerConnectionManagerLike,
    container_id: UUID,
    room_id: str,
) -> dict[str, object]:
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

    event_data: dict[str, object] = {
        "container_id": str(container_id),
        "room_id": room_id,
    }

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

    return delivery_stats
