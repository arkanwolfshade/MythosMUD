"""
Quest event subscriptions: room entry (trigger start), room exit (complete_activity progress).

Room-based quests are offered in two cases:
- Entering via exit: MovementService calls Room.player_entered() -> PlayerEnteredRoom event
  -> this module's handler runs and calls start_quest_by_trigger (this file).
- Spawning in room: Connection setup does not emit PlayerEnteredRoom; see
  player_connection_setup._trigger_quests_for_room_on_spawn() for the explicit spawn path.

Also wires PlayerLeftRoom (complete_activity) and NPCDied (kill_n). NPC/item triggers TBD.
"""

from __future__ import annotations

import uuid
from typing import Any

from server.events.event_types import NPCDied, PlayerEnteredRoom, PlayerLeftRoom
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

# Activity target for "exit room" goals: leave room R -> activity "exit_<R>"
EXIT_ACTIVITY_PREFIX = "exit_"

# Instanced room id format: instance_<uuid>_<stable_room_id>; quest_offers use stable id
INSTANCE_ROOM_PREFIX = "instance_"


def _entity_id_for_quest_offer(room_id: str) -> str:
    """Return entity_id for quest_offers lookup: strip instance_<uuid>_ prefix if present."""
    if room_id.startswith(INSTANCE_ROOM_PREFIX) and room_id.count("_") >= 2:
        parts = room_id.split("_", 2)
        if len(parts) > 2:
            return parts[2]
    return room_id


def subscribe_quest_events(container: Any) -> None:  # noqa: ANN001
    """
    Subscribe to room events for quest triggers and progress.

    - PlayerEnteredRoom: try to start quests offered by this room (trigger type "room").
    - PlayerLeftRoom: record complete_activity for target "exit_<room_id>".
    - NPCDied: when killer_id is set, record kill for kill_N goals (npc_id as target).

    Requires container.event_bus and container.quest_service. No-op if either is missing.
    """
    event_bus = getattr(container, "event_bus", None)
    quest_service = getattr(container, "quest_service", None)
    if not event_bus or not quest_service:
        logger.debug(
            "Quest events not subscribed: event_bus or quest_service missing",
            has_event_bus=event_bus is not None,
            has_quest_service=quest_service is not None,
        )
        return

    event_bus.subscribe(
        PlayerEnteredRoom,
        _make_on_player_entered(quest_service),
        service_id="quest_subsystem",
    )
    event_bus.subscribe(
        PlayerLeftRoom,
        _make_on_player_left(quest_service),
        service_id="quest_subsystem",
    )
    event_bus.subscribe(
        NPCDied,
        _make_on_npc_died(quest_service),
        service_id="quest_subsystem",
    )
    logger.info("Quest subsystem subscribed to PlayerEnteredRoom, PlayerLeftRoom, NPCDied")


def _make_on_player_entered(quest_service: Any) -> Any:  # noqa: ANN401
    """Return an async handler for PlayerEnteredRoom (entering via exit); starts room-offered quests."""

    async def _on_player_entered_room(event: PlayerEnteredRoom) -> None:
        try:
            player_id = _parse_player_id(event.player_id)
            if not player_id:
                return
            entity_id = _entity_id_for_quest_offer(event.room_id)
            await quest_service.start_quest_by_trigger(player_id, "room", entity_id)
        except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: Quest trigger must not crash room entry; log and continue
            logger.warning(
                "Quest trigger (room entry) failed",
                player_id=event.player_id,
                room_id=event.room_id,
                error=str(e),
            )

    return _on_player_entered_room


def _make_on_player_left(quest_service: Any) -> Any:  # noqa: ANN401
    """Return an async handler for PlayerLeftRoom that records exit_<room_id> activity."""

    async def _on_player_left_room(event: PlayerLeftRoom) -> None:
        try:
            player_id = _parse_player_id(event.player_id)
            if not player_id:
                return
            # Use stable room id so exit_<stable_id> matches quest goals (definitions use stable id, not instance id)
            stable_room_id = _entity_id_for_quest_offer(event.room_id)
            activity_target = f"{EXIT_ACTIVITY_PREFIX}{stable_room_id}"
            await quest_service.record_complete_activity(player_id, activity_target)
        except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: Quest progress must not crash room exit; log and continue
            logger.warning(
                "Quest progress (room exit) failed",
                player_id=event.player_id,
                room_id=event.room_id,
                error=str(e),
            )

    return _on_player_left_room


def _make_on_npc_died(quest_service: Any) -> Any:  # noqa: ANN401
    """Return an async handler for NPCDied that records kill for kill_N goals when killer is a player."""

    async def _on_npc_died(event: NPCDied) -> None:
        if not event.killer_id or not event.npc_id:
            return
        try:
            player_id = _parse_player_id(event.killer_id)
            if not player_id:
                return
            # npc_id from event (original string id) used as target; quest goals use same id format
            await quest_service.record_kill(player_id, str(event.npc_id))
        except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: Quest progress must not crash death handler; log and continue
            logger.warning(
                "Quest progress (NPC kill) failed",
                killer_id=event.killer_id,
                npc_id=event.npc_id,
                error=str(e),
            )

    return _on_npc_died


def _parse_player_id(player_id: str) -> uuid.UUID | None:
    """Parse player_id string to UUID. Returns None if invalid."""
    try:
        return uuid.UUID(player_id)
    except (ValueError, TypeError):
        return None
