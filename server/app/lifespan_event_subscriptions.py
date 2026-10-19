"""Event subscription setup for application startup.

Extracted from lifespan_startup to keep module line count under limit.
"""

import asyncio
import uuid as uuid_lib
from typing import cast

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


def subscribe_npc_dialogue_events(container: ApplicationContainer) -> None:
    """Open a conversation when an NPC that speaks first notices a player (NPCOpensDialogue)."""
    from server.async_persistence import AsyncPersistenceLayer
    from server.events.event_bus import EventBus
    from server.events.event_types import NPCOpensDialogue

    # The container's attributes are untyped; name what they are here.
    event_bus = cast(EventBus | None, getattr(container, "event_bus", None))
    if event_bus is None:
        return

    async def _on_npc_opens_dialogue(event: NPCOpensDialogue) -> None:
        from server.commands.quest_commands import npc_definition_id, npc_instance_in_room
        from server.commands.scripted_action_support import container_context
        from server.commands.talk_command import open_dialogue
        from server.game.dialogue import get_dialogue_service

        persistence = cast(AsyncPersistenceLayer | None, getattr(container, "async_persistence", None))
        try:
            player_id = uuid_lib.UUID(event.player_id)
            npc = npc_instance_in_room(event.npc_id, event.room_id)
            definition_id = npc_definition_id(npc) if npc is not None else None
            if persistence is None or definition_id is None:
                return
            cursor = get_dialogue_service().get_cursor(player_id)
            if cursor is not None and cursor.npc_id == event.npc_id:
                return  # already talking to this NPC; do not restart the conversation on re-entry
            player = await persistence.get_player_by_id(player_id)
            if player is None or player.current_room_id != event.room_id:
                return  # gone, or already moved on
            _ = await open_dialogue(
                player_id,
                npc_id=event.npc_id,
                npc_name=event.npc_name,
                definition_id=int(definition_id),
                ctx=container_context(container, player, persistence),
            )
        except (ValueError, TypeError, AttributeError) as e:
            logger.warning("NPC could not open its dialogue", npc_id=event.npc_id, error=str(e))

    event_bus.subscribe(NPCOpensDialogue, _on_npc_opens_dialogue, service_id="npc_opens_dialogue")


def subscribe_quest_events(container: ApplicationContainer) -> None:
    """Subscribe to room events for quest triggers and progress (start on enter, complete_activity on exit)."""
    from server.game.quest.quest_events import subscribe_quest_events as _subscribe_room_quest_events

    _subscribe_room_quest_events(container)

    # Push the updated quest log whenever it changes (start, progress, completion, abandon) so the Journal
    # panel refreshes without the player typing `journal`.
    event_bus = getattr(container, "event_bus", None)
    if not event_bus:
        return

    from server.events.event_types import QuestLogChanged
    from server.realtime.envelope import build_event

    async def _on_quest_log_changed_push_log(event: QuestLogChanged) -> None:
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
                "Failed to push quest log after a change",
                player_id=event.player_id,
                error=str(e),
            )

    event_bus.subscribe(QuestLogChanged, _on_quest_log_changed_push_log, service_id="quest_push_log")
