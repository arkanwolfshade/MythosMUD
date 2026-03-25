"""
Event handlers for NATS message handler.

This module handles all event-type messages from NATS and broadcasts them
to WebSocket clients.
"""

from __future__ import annotations

import uuid
from collections.abc import Awaitable, Callable, Mapping
from typing import Protocol, cast

from structlog.stdlib import BoundLogger

from server.events.event_types import NPCDied

from ..services.nats_exceptions import NATSError
from ..structured_logging.enhanced_logging_config import get_logger
from .connection_manager import ConnectionManager
from .envelope import build_event

# Protocol stub bodies use Ellipsis (PEP 544); Pylint W2301 conflicts with pyright if replaced with pass.
# pylint: disable=unnecessary-ellipsis


class _EventBusPublishPort(Protocol):
    """Minimal surface for publishing domain events from ConnectionManager.event_bus."""

    def publish(self, event: object) -> None:
        """Publish a single event to the in-process bus."""
        ...


logger: BoundLogger = cast(BoundLogger, get_logger("communications.event_handlers"))


def _as_event_data_dict(raw: object) -> dict[str, object]:
    """Normalize NATS event_data payload to a string-keyed dict."""
    if isinstance(raw, dict):
        return cast(dict[str, object], raw)
    return {}


def _participant_key_strings(participants: object) -> list[str]:
    """Keys from a participants mapping (NATS may send dict-like payloads)."""
    if not isinstance(participants, dict):
        return []
    raw = cast(dict[object, object], participants)
    return [str(k) for k in raw]


async def _send_combat_participant_updates(
    connection_manager: ConnectionManager,
    participants: object,
    *,
    in_combat: bool,
) -> None:
    """Push player_update to each combat participant (in_combat flag)."""
    for participant_id_str in _participant_key_strings(participants):
        try:
            participant_id_uuid = uuid.UUID(participant_id_str) if participant_id_str else None
            if participant_id_uuid is None:
                continue
            player = await connection_manager.get_player(participant_id_uuid)
            if player:
                player_update_event = build_event(
                    "player_update",
                    {
                        "player_id": participant_id_str,
                        "in_combat": in_combat,
                    },
                    player_id=participant_id_str,
                )
                _ = await connection_manager.send_personal_message(participant_id_uuid, player_update_event)
                logger.debug(
                    "Sent player update with in_combat flag", player_id=participant_id_str, in_combat=in_combat
                )
        except (NATSError, RuntimeError) as exc:
            logger.warning(
                "Error sending player update for combat",
                player_id=participant_id_str,
                error_message=str(exc),
            )


def _npc_died_ids_or_warn(data: dict[str, object]) -> tuple[str, str, str] | None:
    """Return (room_id, npc_id, npc_name) or None after logging warnings."""
    room_id_raw = data.get("room_id")
    npc_id_raw = data.get("npc_id")
    npc_name_raw = data.get("npc_name")

    if room_id_raw is None or (isinstance(room_id_raw, str) and not room_id_raw):
        logger.warning("NPC died event missing room_id", data=data)
        return None

    if npc_id_raw is None or (isinstance(npc_id_raw, str) and not npc_id_raw):
        logger.warning("NPC died event missing npc_id", data=data)
        return None

    room_id = str(room_id_raw)
    npc_id = str(npc_id_raw)
    npc_name = str(npc_name_raw) if npc_name_raw is not None else ""
    return (room_id, npc_id, npc_name)


def _publish_npc_died_to_event_bus(
    connection_manager: ConnectionManager,
    data: dict[str, object],
    room_id: str,
    npc_id: str,
    npc_name: str,
) -> None:
    """Publish NPCDied to the in-process EventBus when configured on ConnectionManager."""
    event_bus_raw = cast(object, connection_manager.event_bus)
    if event_bus_raw is None:
        return
    killer_raw = data.get("killer_id")
    cause_raw = data.get("cause", "combat")
    npc_died_event = NPCDied(
        npc_id=npc_id,
        room_id=room_id,
        cause=str(cause_raw) if cause_raw is not None else "combat",
        killer_id=str(killer_raw) if killer_raw is not None else None,
    )
    bus = cast(_EventBusPublishPort, event_bus_raw)
    bus.publish(npc_died_event)
    logger.info(
        "NPCDied event published to EventBus for respawn queue",
        npc_id=npc_id,
        npc_name=npc_name,
    )


async def _refresh_room_after_npc_death(
    connection_manager: ConnectionManager,
    data: dict[str, object],
    room_id: str,
    npc_id: str,
) -> None:
    """Best-effort room occupants refresh after NPC death."""
    try:
        from server.realtime.websocket_room_updates import broadcast_room_update

        killer_raw = data.get("killer_id")
        killer_id = str(killer_raw) if killer_raw is not None else None
        player_id = killer_id if killer_id else room_id
        await broadcast_room_update(
            player_id,
            room_id,
            connection_manager=connection_manager,
        )
        logger.debug("Room occupants broadcast after NPC death", room_id=room_id, npc_id=npc_id)
    except Exception as broadcast_err:  # pylint: disable=broad-exception-caught  # Non-fatal; must not break death flow
        logger.warning(
            "Failed to broadcast room occupants after NPC death (non-fatal)",
            room_id=room_id,
            npc_id=npc_id,
            error_message=str(broadcast_err),
        )


async def _npc_died_broadcast_and_bridge(
    connection_manager: ConnectionManager,
    data: dict[str, object],
) -> None:
    """Broadcast npc_died to WebSocket, publish NPCDied to EventBus, refresh room occupants."""
    ids = _npc_died_ids_or_warn(data)
    if ids is None:
        return
    room_id, npc_id, npc_name = ids

    npc_display = npc_name or "An unknown creature"
    broadcast_data = {**data, "message": f"The {npc_display} has been slain."}

    _ = await connection_manager.broadcast_room_event("npc_died", room_id, broadcast_data)
    logger.debug("NPC died event broadcasted", room_id=room_id, npc_id=npc_id, npc_name=npc_name)

    _publish_npc_died_to_event_bus(connection_manager, data, room_id, npc_id, npc_name)

    await _refresh_room_after_npc_death(connection_manager, data, room_id, npc_id)


class EventHandler:
    """Handler for NATS event messages."""

    connection_manager: ConnectionManager

    def __init__(self, connection_manager: ConnectionManager) -> None:
        """
        Initialize event handler.

        Args:
            connection_manager: ConnectionManager instance for broadcasting
        """
        self.connection_manager = connection_manager

    def get_event_handler_map(self) -> dict[str, Callable[[dict[str, object]], Awaitable[None]]]:
        """
        Get mapping of event types to their handler methods.

        Returns:
            Dictionary mapping event_type strings to handler coroutine methods
        """
        return {
            "player_entered": self.handle_player_entered_event,
            "player_left": self.handle_player_left_event,
            "game_tick": self.handle_game_tick_event,
            "combat_started": self.handle_combat_started_event,
            "combat_ended": self.handle_combat_ended_event,
            "player_attacked": self.handle_player_attacked_event,
            "npc_attacked": self.handle_npc_attacked_event,
            "npc_took_damage": self.handle_npc_took_damage_event,
            "npc_died": self.handle_npc_died_event,
        }

    def validate_event_message(self, event_type: str | None, data: dict[str, object]) -> bool:
        """
        Validate that event message has required fields.

        Args:
            event_type: Event type string
            data: Event data dictionary

        Returns:
            True if valid, False otherwise
        """
        if not event_type or not data:
            logger.warning("Invalid event message - missing required fields", event_type=event_type, data=data)
            return False
        return True

    async def handle_event_message(self, message_data: Mapping[str, object]) -> None:
        """
        Handle incoming event messages from NATS.

        Args:
            message_data: Event message data from NATS
        """
        try:
            logger.info("Handling event message", message_data=message_data)

            event_type_raw = message_data.get("event_type")
            data = _as_event_data_dict(message_data.get("event_data", {}))

            logger.debug("NATS message received", event_type=event_type_raw, data=data)

            event_type = event_type_raw if isinstance(event_type_raw, str) else None
            if not self.validate_event_message(event_type, data):
                return

            if event_type is None:
                raise ValueError("event_type should not be None after validation")
            event_type_str = event_type

            handler_map = self.get_event_handler_map()
            handler = handler_map.get(event_type_str)

            if handler:
                if event_type_str == "npc_attacked":
                    logger.debug("NPC attacked event received in NATS handler", data=data)
                await handler(data)
            else:
                logger.debug("Unknown event type received", event_type=event_type_str)

        except NATSError as exc:
            logger.error(
                "Error handling event message",
                error_message=str(exc),
                message_data=message_data,
            )

    async def handle_player_entered_event(self, data: dict[str, object]) -> None:
        """
        Handle player_entered event.

        Args:
            data: Event data containing player and room information
        """
        try:
            room_id_raw = data.get("room_id")
            if room_id_raw is None or (isinstance(room_id_raw, str) and not room_id_raw):
                logger.warning("Player entered event missing room_id", data=data)
                return

            room_id = str(room_id_raw)
            _ = await self.connection_manager.broadcast_room_event("player_entered", room_id, data)

            logger.debug(
                "Player entered event broadcasted",
                room_id=room_id,
                player_id=data.get("player_id"),
            )

        except NATSError as exc:
            logger.error("Error handling player entered event", error_message=str(exc), data=data)

    async def handle_player_left_event(self, data: dict[str, object]) -> None:
        """
        Handle player_left event.

        Args:
            data: Event data containing player and room information
        """
        try:
            room_id_raw = data.get("room_id")
            if room_id_raw is None or (isinstance(room_id_raw, str) and not room_id_raw):
                logger.warning("Player left event missing room_id", data=data)
                return

            room_id = str(room_id_raw)
            _ = await self.connection_manager.broadcast_room_event("player_left", room_id, data)

            logger.debug(
                "Player left event broadcasted",
                room_id=room_id,
                player_id=data.get("player_id"),
            )

        except NATSError as exc:
            logger.error("Error handling player left event", error_message=str(exc), data=data)

    async def handle_game_tick_event(self, data: dict[str, object]) -> None:
        """
        Handle game_tick event.

        Args:
            data: Event data containing tick information
        """
        try:
            _ = await self.connection_manager.broadcast_global_event("game_tick", data)

            logger.debug(
                "Game tick event broadcasted",
                tick_number=data.get("tick_number"),
            )

        except NATSError as exc:
            logger.error("Error handling game tick event", error_message=str(exc), data=data)

    async def handle_combat_started_event(self, data: dict[str, object]) -> None:
        """Handle combat_started event."""
        try:
            room_id_raw = data.get("room_id")
            if room_id_raw is None or (isinstance(room_id_raw, str) and not room_id_raw):
                logger.warning("Combat started event missing room_id", data=data)
                return

            room_id = str(room_id_raw)
            _ = await self.connection_manager.broadcast_room_event("combat_started", room_id, data)
            logger.debug("Combat started event broadcasted", room_id=room_id)

            await _send_combat_participant_updates(
                self.connection_manager,
                data.get("participants", {}),
                in_combat=True,
            )

        except NATSError as exc:
            logger.error("Error handling combat started event", error_message=str(exc), data=data)

    async def handle_combat_ended_event(self, data: dict[str, object]) -> None:
        """Handle combat_ended event."""
        try:
            room_id_raw = data.get("room_id")
            if room_id_raw is None or (isinstance(room_id_raw, str) and not room_id_raw):
                logger.warning("Combat ended event missing room_id", data=data)
                return

            room_id = str(room_id_raw)
            _ = await self.connection_manager.broadcast_room_event("combat_ended", room_id, data)
            logger.debug("Combat ended event broadcasted", room_id=room_id)

            await _send_combat_participant_updates(
                self.connection_manager,
                data.get("participants", {}),
                in_combat=False,
            )

        except NATSError as exc:
            logger.error("Error handling combat ended event", error_message=str(exc), data=data)

    async def handle_player_attacked_event(self, data: dict[str, object]) -> None:
        """Handle player_attacked event."""
        try:
            payload = _as_event_data_dict(data.get("event_data", data))
            room_id_raw = payload.get("room_id") or data.get("room_id")
            if room_id_raw is None or (isinstance(room_id_raw, str) and not room_id_raw):
                logger.warning("Player attacked event missing room_id", data=data)
                return

            room_id = str(room_id_raw)
            _ = await self.connection_manager.broadcast_room_event("player_attacked", room_id, payload)
            logger.debug("Player attacked event broadcasted", room_id=room_id)

        except NATSError as exc:
            logger.error("Error handling player attacked event", error_message=str(exc), data=data)

    async def handle_npc_attacked_event(self, data: dict[str, object]) -> None:
        """Handle npc_attacked event."""
        try:
            payload = _as_event_data_dict(data.get("event_data", data))
            room_id_raw = payload.get("room_id") or data.get("room_id")
            if room_id_raw is None or (isinstance(room_id_raw, str) and not room_id_raw):
                logger.warning("NPC attacked event missing room_id", data=data)
                return

            room_id = str(room_id_raw)
            _ = await self.connection_manager.broadcast_room_event("npc_attacked", room_id, payload)
            logger.debug("NPC attacked event broadcasted", room_id=room_id)

        except NATSError as exc:
            logger.error("Error handling NPC attacked event", error_message=str(exc), data=data)

    async def handle_npc_took_damage_event(self, data: dict[str, object]) -> None:
        """Handle npc_took_damage event."""
        try:
            payload = _as_event_data_dict(data.get("event_data", data))
            room_id_raw = payload.get("room_id") or data.get("room_id")
            if room_id_raw is None or (isinstance(room_id_raw, str) and not room_id_raw):
                logger.warning("NPC took damage event missing room_id", data=data)
                return

            room_id = str(room_id_raw)
            _ = await self.connection_manager.broadcast_room_event("npc_took_damage", room_id, payload)
            logger.debug("NPC took damage event broadcasted", room_id=room_id)

        except NATSError as exc:
            logger.error("Error handling NPC took damage event", error_message=str(exc), data=data)

    async def handle_npc_died_event(self, data: dict[str, object]) -> None:
        """
        Handle npc_died event - NATS to EventBus bridge pattern.

        ARCHITECTURE NOTE - Dual Event Path by Design:
        This handler implements the NATS to EventBus bridge pattern, which is NOT redundant:

        1. NATS Path (Inter-Service Communication):
           - CombatService publishes NPCDiedEvent to NATS to NATSMessageHandler (here)
           - Purpose: Broadcast death to WebSocket clients for UI updates

        2. EventBus Path (Internal Game Logic):
           - NATSMessageHandler publishes NPCDied to EventBus to NPCLifecycleManager
           - Purpose: Trigger respawn queue processing with configured delay

        This separation of concerns follows NATS.mdc best practices:
        - NATS handles distributed messaging and client broadcasting
        - EventBus handles internal domain logic and game state management
        - Bridge pattern prevents tight coupling between communication and domain layers

        AI Agent: This is the ONLY place that bridges NATS npc_died messages to EventBus.
                  CombatService publishes to NATS only, not EventBus directly.
                  Removing this bridge would break NPC respawning entirely!

        Note: NPC removal from room is handled by the NPCLeftRoom event published
        by the lifecycle manager. This handler broadcasts the death event to clients
        AND publishes to EventBus for respawn queue processing.
        """
        try:
            await _npc_died_broadcast_and_bridge(self.connection_manager, data)
        except NATSError as exc:
            logger.error("Error handling NPC died event", error_message=str(exc), data=data)
