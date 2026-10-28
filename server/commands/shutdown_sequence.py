"""
Shutdown sequence execution for graceful server shutdown.

This module handles the phased shutdown sequence that ensures all server
components are properly cleaned up before termination.
"""

import uuid
from collections.abc import Awaitable, Callable
from typing import Any, Protocol

from ..exceptions import DatabaseError
from ..models.player import Player
from ..structured_logging.enhanced_logging_config import get_logger
from .shutdown_process_termination import schedule_process_termination

logger = get_logger(__name__)


class _ConnectionManager(Protocol):
    def get_online_players(self) -> list[dict[str, object]]:
        """Return currently connected players."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: Protocol stub body for basedpyright

    async def force_disconnect_player(self, player_id: uuid.UUID) -> None:
        """Disconnect one player."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: Protocol stub body for basedpyright


class _PlayerStore(Protocol):
    async def get_player_by_id(self, player_id: uuid.UUID) -> Player | None:
        """Load a player by ID."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: Protocol stub body for basedpyright

    async def save_player(self, player: Player) -> None:
        """Persist a player."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: Protocol stub body for basedpyright


class _PlayerShutdownState(Protocol):
    @property
    def connection_manager(self) -> _ConnectionManager | None:
        """Connection manager, if running."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: Protocol stub body for basedpyright

    @property
    def persistence(self) -> _PlayerStore:
        """Player persistence layer."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: Protocol stub body for basedpyright


class _PlayerShutdownApp(Protocol):
    @property
    def state(self) -> _PlayerShutdownState:
        """Application state."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: Protocol stub body for basedpyright


def _online_player_ids(connection_manager: _ConnectionManager) -> list[uuid.UUID]:
    """Return connected player IDs as UUIDs, skipping (and logging) any that are malformed."""
    ids: list[uuid.UUID] = []
    for p in connection_manager.get_online_players():
        raw = p.get("player_id")
        if raw is None:
            continue
        try:
            ids.append(raw if isinstance(raw, uuid.UUID) else uuid.UUID(str(raw)))
        except ValueError:
            logger.warning("Skipping malformed player ID during shutdown", player_id=raw)
    return ids


async def _persist_all_players(app: _PlayerShutdownApp) -> None:
    """Phase 1: Persist all active player data."""
    logger.info("Phase 1: Persisting all active player data")
    connection_manager = app.state.connection_manager
    if connection_manager:
        try:
            connected_players = _online_player_ids(connection_manager)
            logger.info("Persisting connected players", count=len(connected_players))

            persistence = app.state.persistence
            for player_id in connected_players:
                try:
                    player_obj = await persistence.get_player_by_id(player_id)
                    if player_obj:
                        await persistence.save_player(player_obj)
                        logger.debug("Persisted player", player_id=player_id)
                    else:
                        logger.warning("Player object not found for ID, skipping persistence", player_id=player_id)
                except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: one bad player must not stop the rest being saved
                    logger.error("Failed to persist player", player_id=player_id, error=str(e), exc_info=True)

            logger.info("Phase 1 complete: All player data persisted")
        except DatabaseError as e:
            logger.error("Error during player persistence phase", error=str(e), exc_info=True)
    else:
        logger.warning("No connection manager found, skipping player persistence")


async def _despawn_all_npcs(app: Any) -> None:
    """Phase 2: Despawn all NPCs."""
    logger.info("Phase 2: Despawning all NPCs")
    # Prefer container, fallback to app.state for backward compatibility
    npc_spawning_service = None
    npc_lifecycle_manager = None
    if app and hasattr(app.state, "container") and app.state.container:
        npc_spawning_service = app.state.container.npc_spawning_service
        npc_lifecycle_manager = app.state.container.npc_lifecycle_manager
    else:
        npc_spawning_service = getattr(app.state, "npc_spawning_service", None)
        npc_lifecycle_manager = getattr(app.state, "npc_lifecycle_manager", None)

    if npc_spawning_service:
        try:
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


async def _disconnect_all_players(app: _PlayerShutdownApp) -> None:
    """Phase 3: Disconnect all players gracefully."""
    logger.info("Phase 3: Disconnecting all players")
    connection_manager = app.state.connection_manager
    if connection_manager:
        try:
            connected_players = _online_player_ids(connection_manager)
            logger.info("Disconnecting connected players", count=len(connected_players))

            for player_id in connected_players:
                try:
                    await connection_manager.force_disconnect_player(player_id)
                    logger.debug("Disconnected player", player_id=player_id)
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


async def execute_shutdown_sequence(app: _PlayerShutdownApp) -> None:
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

    phases: list[Callable[[_PlayerShutdownApp], Awaitable[None]]] = [
        _persist_all_players,
        _despawn_all_npcs,
        _disconnect_all_players,
        _stop_nats_message_handler,
        _disconnect_nats_service,
        _cleanup_connection_manager,
        _cancel_background_tasks,
    ]
    try:
        for phase in phases:
            try:
                await phase(app)
            except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: a failed phase must not block the remaining phases or process exit
                logger.error("Shutdown phase failed, continuing", phase=phase.__name__, error=str(e), exc_info=True)
        logger.info("=== Graceful Shutdown Sequence Complete ===")
    finally:
        logger.info("Scheduling process termination after graceful shutdown completion")
        schedule_process_termination(0.3)
