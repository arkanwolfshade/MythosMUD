"""Execute a queued spawn request: instance + room registration."""

from collections.abc import Callable
from typing import cast

from structlog.stdlib import BoundLogger

from server.async_persistence import AsyncPersistenceLayer
from server.models.npc import NPCDefinition
from server.models.room import Room
from server.npc.behaviors import NPCBase
from server.npc.spawning_models import NPCSpawnRequest, NPCSpawnResult, SimpleNPCDefinition

from ..container import ApplicationContainer
from ..structured_logging.enhanced_logging_config import get_logger

logger: BoundLogger = get_logger(__name__)


def _room_from_persistence(room_id: str) -> Room | None:
    container = ApplicationContainer.get_instance()
    if not container:
        return None
    persistence = cast(AsyncPersistenceLayer | None, container.async_persistence)
    if persistence is None:
        return None
    return persistence.get_room_by_id(room_id)


def _spawn_success(request: NPCSpawnRequest, npc_id: str, npc_instance: NPCBase) -> NPCSpawnResult:
    definition_name = getattr(request.definition, "name", "Unknown NPC")
    logger.info("Successfully spawned NPC", npc_id=npc_id, npc_name=definition_name, room_id=request.room_id)
    return NPCSpawnResult(
        success=True,
        npc_id=npc_id,
        npc_instance=npc_instance,
        spawn_request=request,
    )


def spawn_npc_from_request(
    request: NPCSpawnRequest,
    *,
    create_npc_instance: Callable[[NPCDefinition, str, str | None], NPCBase | None],
    generate_npc_id: Callable[[NPCDefinition | SimpleNPCDefinition, str], str],
) -> NPCSpawnResult:
    """Create an NPC from a spawn request and register it in the target room."""
    try:
        npc_instance = create_npc_instance(request.definition, request.room_id, None)
        if not npc_instance:
            return NPCSpawnResult(
                success=False,
                error_message="Failed to create NPC instance",
                spawn_request=request,
            )

        npc_id = generate_npc_id(request.definition, request.room_id)
        room = _room_from_persistence(request.room_id)
        if not room:
            definition_name = getattr(request.definition, "name", "Unknown NPC")
            logger.warning("Room not found for NPC spawn", npc_name=definition_name, room_id=request.room_id)
            return NPCSpawnResult(success=False, error_message="Room not found", spawn_request=request)

        room.npc_entered(npc_id)
        return _spawn_success(request, npc_id, npc_instance)

    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: graceful spawn failure
        logger.error("Failed to spawn NPC from request", request=request, error=str(e))
        return NPCSpawnResult(success=False, error_message=str(e), spawn_request=request)
