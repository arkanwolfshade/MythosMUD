"""
Shutdown sequence execution for graceful server shutdown.

This module handles the phased shutdown sequence that ensures all server
components are properly cleaned up before termination.
"""

from typing import Any

from ..exceptions import DatabaseError
from ..structured_logging.enhanced_logging_config import get_logger
from .shutdown_process_termination import schedule_process_termination

logger = get_logger(__name__)


async def _persist_all_players(app: Any) -> None:
    """Phase 1: Persist all active player data."""
    logger.info("Phase 1: Persisting all active player data")
    if hasattr(app.state, "connection_manager") and app.state.connection_manager:
        try:
            connected_players = [
                p.get("player_id")
                for p in app.state.connection_manager.get_online_players()
                if p.get("player_id") is not None
            ]
            logger.info("Persisting connected players", count=len(connected_players))

            persistence = app.state.persistence
            for player_id in connected_players:
                try:
                    player_obj = persistence.get_player(player_id)
                    if player_obj:
                        await persistence.save_player(player_obj)
                        logger.debug("Persisted player", player_id=player_id)
                    else:
                        logger.warning("Player object not found for ID, skipping persistence", player_id=player_id)
                except DatabaseError as e:
                    logger.error("Failed to persist player", player_id=player_id, error=str(e))

            logger.info("Phase 1 complete: All player data persisted")
        except DatabaseError as e:
            logger.error("Error during player persistence phase", error=str(e), exc_info=True)
    else:
        logger.warning("No connection manager found, skipping player persistence")


async def _despawn_all_npcs(app: Any) -> None:
    """Phase 2: Despawn all NPCs."""
    logger.info("Phase 2: Despawning all NPCs")
    if hasattr(app.state, "npc_spawning_service") and app.state.npc_spawning_service:
        try:
            npc_lifecycle_manager = getattr(app.state, "npc_lifecycle_manager", None)
            if npc_lifecycle_manager:
                active_npcs = list(npc_lifecycle_manager.active_npcs.keys())
                logger.info("Despawning active NPCs", count=len(active_npcs))

                for npc_id in active_npcs:
                    try:
                        _ = npc_lifecycle_manager.despawn_npc(npc_id, reason="server_shutdown")
                        logger.debug("Despawned NPC", npc_id=npc_id)
                    except OSError as e:
                        logger.error("Failed to despawn NPC", npc_id=npc_id, error=str(e))

                logger.info("Phase 2 complete: All NPCs despawned")
            else:
                logger.warning("No NPC lifecycle manager found, skipping NPC despawn")
        except OSError as e:
            logger.error("Error during NPC despawn phase", error=str(e), exc_info=True)
    else:
        logger.warning("No NPC spawning service found, skipping NPC despawn")


async def _disconnect_all_players(app: Any) -> None:
    """Phase 3: Disconnect all players gracefully."""
    logger.info("Phase 3: Disconnecting all players")
    if hasattr(app.state, "connection_manager") and app.state.connection_manager:
        try:
            connected_players = [
                p.get("player_id")
                for p in app.state.connection_manager.get_online_players()
                if p.get("player_id") is not None
            ]
            logger.info("Disconnecting connected players", count=len(connected_players))

            import uuid as uuid_module

            for player_id in connected_players:
                try:
                    player_id_uuid = uuid_module.UUID(player_id) if isinstance(player_id, str) else player_id
                    await app.state.connection_manager.force_disconnect_player(player_id_uuid)
                    logger.debug("Disconnected player", player_id=player_id_uuid)
                except OSError as e:
                    logger.error("Failed to disconnect player", player_id=player_id, error=str(e))

            logger.info("Phase 3 complete: All players disconnected")
        except OSError as e:
            logger.error("Error during player disconnection phase", error=str(e), exc_info=True)
    else:
        logger.warning("No connection manager found, skipping player disconnection")


async def _stop_nats_message_handler(app: Any) -> None:
    """Phase 4: Stop NATS message handler."""
    logger.info("Phase 4: Stopping NATS message handler")
    if hasattr(app.state, "nats_message_handler") and app.state.nats_message_handler:
        try:
            await app.state.nats_message_handler.stop()
            logger.info("Phase 4 complete: NATS message handler stopped")
        except OSError as e:
            logger.error("Error stopping NATS message handler", error=str(e), exc_info=True)
    else:
        logger.warning("No NATS message handler found, skipping")


async def _disconnect_nats_service(app: Any) -> None:
    """Phase 5: Disconnect NATS service."""
    logger.info("Phase 5: Disconnecting NATS service")
    if hasattr(app.state, "nats_service") and app.state.nats_service:
        try:
            await app.state.nats_service.disconnect()
            logger.info("Phase 5 complete: NATS service disconnected")
        except OSError as e:
            logger.error("Error disconnecting NATS service", error=str(e), exc_info=True)
    else:
        logger.warning("No NATS service found, skipping")


async def _cleanup_connection_manager(app: Any) -> None:
    """Phase 6: Clean up connection manager."""
    logger.info("Phase 6: Cleaning up connection manager")
    if hasattr(app.state, "connection_manager") and app.state.connection_manager:
        try:
            await app.state.connection_manager.force_cleanup()
            logger.info("Phase 6 complete: Connection manager cleaned up")
        except OSError as e:
            logger.error("Error cleaning up connection manager", error=str(e), exc_info=True)
    else:
        logger.warning("No connection manager found, skipping cleanup")


async def _cancel_background_tasks(app: Any) -> None:
    """Phase 7: Cancel remaining background tasks."""
    logger.info("Phase 7: Cancelling remaining background tasks")
    if hasattr(app.state, "task_registry") and app.state.task_registry:
        try:
            shutdown_data = getattr(app.state, "shutdown_data", None)
            shutdown_task = shutdown_data.get("task") if shutdown_data else None

            if shutdown_task:
                task_name = "shutdown_countdown"
                unregistered = app.state.task_registry.unregister_task(task_name)
                if unregistered:
                    logger.debug("Unregistered shutdown countdown task to prevent recursion")
                else:
                    logger.warning("Failed to unregister shutdown countdown task")

            shutdown_success = await app.state.task_registry.shutdown_all(timeout=5.0)
            if shutdown_success:
                logger.info("Phase 7 complete: All background tasks cancelled gracefully")
            else:
                logger.warning("Phase 7: TaskRegistry shutdown reached timeout")
        except OSError as e:
            logger.error("Error during task registry shutdown", error=str(e), exc_info=True)
    else:
        logger.warning("No task registry found, skipping task cancellation")


async def execute_shutdown_sequence(app: Any) -> None:
    """
    Execute the graceful shutdown sequence.

    This function performs an orderly shutdown of all server services:
    1. Persist all active player data
    2. Despawn all NPCs (turn off AI, cancel spawning)
    3. Disconnect all players gracefully
    4. Stop NATS message handler
    5. Disconnect NATS service
    6. Clean up connection manager
    7. Cancel remaining background tasks

    Args:
        app: FastAPI application instance
    """
    logger.info("=== Beginning Graceful Shutdown Sequence ===")

    try:
        await _persist_all_players(app)
        await _despawn_all_npcs(app)
        await _disconnect_all_players(app)
        await _stop_nats_message_handler(app)
        await _disconnect_nats_service(app)
        await _cleanup_connection_manager(app)
        await _cancel_background_tasks(app)

        logger.info("=== Graceful Shutdown Sequence Complete ===")
        logger.info("Scheduling process termination after graceful shutdown completion")
        schedule_process_termination(0.3)

    except OSError as e:
        logger.error("Critical error during shutdown sequence", error=str(e), exc_info=True)
        raise
