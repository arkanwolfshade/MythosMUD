"""Event subscription setup for application startup.

Extracted from lifespan_startup to keep module line count under limit.
"""

import asyncio
import uuid as uuid_lib

from ..container import ApplicationContainer
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger("server.lifespan.events")


def subscribe_room_occupants_refresh(container: ApplicationContainer) -> None:
    """Subscribe to RoomOccupantsRefreshRequested so Occupants panel updates after NPC death."""
    if not container.event_bus or not container.connection_manager:
        return

    from server.events.event_types import RoomOccupantsRefreshRequested
    from server.realtime.websocket_room_updates import broadcast_room_update

    def _on_room_occupants_refresh(event: RoomOccupantsRefreshRequested) -> None:
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            return
        conn_mgr = container.connection_manager
        if not conn_mgr:
            return
        loop.create_task(broadcast_room_update(event.room_id, event.room_id, connection_manager=conn_mgr))

    container.event_bus.subscribe(
        RoomOccupantsRefreshRequested, _on_room_occupants_refresh, service_id="room_occupants_refresh"
    )
    logger.debug("Subscribed to RoomOccupantsRefreshRequested for Occupants panel updates")


def subscribe_quest_events(container: ApplicationContainer) -> None:
    """Subscribe to room events for quest triggers and progress (start on enter, complete_activity on exit)."""
    from server.game.quest.quest_events import subscribe_quest_events as _subscribe_room_quest_events

    _subscribe_room_quest_events(container)

    # Push updated quest log to player when a quest completes so Journal panel refreshes
    event_bus = getattr(container, "event_bus", None)
    if not event_bus:
        return

    from server.events.event_types import QuestCompleted
    from server.realtime.envelope import build_event

    async def _on_quest_completed_push_log(event: QuestCompleted) -> None:
        quest_service = getattr(container, "quest_service", None)
        conn_mgr = getattr(container, "connection_manager", None)
        if not quest_service or not conn_mgr:
            return
        try:
            player_id = uuid_lib.UUID(event.player_id)
            log = await quest_service.get_quest_log(player_id, include_completed=True)
            ev = build_event("quest_log_updated", {"quest_log": log}, player_id=event.player_id)
            await conn_mgr.send_personal_message(player_id, ev)
        except (ValueError, TypeError, AttributeError) as e:
            logger.warning(
                "Failed to push quest log after completion",
                player_id=event.player_id,
                error=str(e),
            )

    event_bus.subscribe(QuestCompleted, _on_quest_completed_push_log, service_id="quest_push_log")
