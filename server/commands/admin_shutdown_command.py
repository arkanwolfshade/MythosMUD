"""
Admin shutdown command for MythosMUD.

This module provides the /shutdown command for administrators to gracefully
shut down the server with configurable countdown notifications.

As noted in the Necronomicon's appendices, proper termination rituals
are essential for maintaining the integrity of dimensional boundaries
during the closure of arcane gateways.
"""

import asyncio
import os
import signal
import threading
import time
from typing import Any

from ..alias_storage import AliasStorage
from ..exceptions import DatabaseError
from ..structured_logging.admin_actions_logger import AdminActionsLogger
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

# Initialize admin actions logger for audit trail
admin_logger = AdminActionsLogger()
# --- Process Termination Scheduling ---


def _schedule_process_termination(delay_seconds: float = 0.3) -> None:
    """Schedule a best-effort graceful process termination after a short delay.

    This signals the parent uvicorn process to exit after all shutdown phases
    complete. Guarded by the environment variable
    `MYTHOSMUD_DISABLE_PROCESS_EXIT` (set to "1" to disable), which is useful
    during tests.
    """
    if os.environ.get("MYTHOSMUD_DISABLE_PROCESS_EXIT") == "1":
        logger.info("Process termination scheduling disabled by environment variable")
        return

    def _terminator() -> None:
        try:
            logger.info("ProcessTerminator thread started", delay_seconds=delay_seconds)
            time.sleep(delay_seconds)
            pid = os.getpid()
            ppid = os.getppid()
            logger.info("ProcessTerminator attempting to terminate process", pid=pid, ppid=ppid)

            # Try to find and kill uvicorn processes specifically
            try:
                import psutil

                # Find all uvicorn processes
                uvicorn_processes = []
                for proc in psutil.process_iter(["pid", "name", "cmdline"]):
                    try:
                        if proc.info["name"] and "uvicorn" in proc.info["name"].lower():
                            uvicorn_processes.append(proc)
                            logger.info("Found uvicorn process", pid=proc.info["pid"], name=proc.info["name"])
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        continue

                # Terminate all uvicorn processes
                for proc in uvicorn_processes:
                    try:
                        logger.info("Terminating uvicorn process", pid=proc.info["pid"])
                        proc.terminate()
                    except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
                        logger.warning("Could not terminate uvicorn process", pid=proc.info["pid"], error=str(e))

                # Wait for processes to terminate
                time.sleep(1)

                # Kill any remaining uvicorn processes
                for proc in uvicorn_processes:
                    try:
                        if proc.is_running():
                            logger.warning("Killing stubborn uvicorn process", pid=proc.info["pid"])
                            proc.kill()
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        pass

                # Also try to terminate the current process and its children
                current_process = psutil.Process(pid)
                children = current_process.children(recursive=True)
                for child in children:
                    logger.info("Terminating child process", pid=child.pid, name=child.name())
                    try:
                        child.terminate()
                    except psutil.NoSuchProcess:
                        logger.warning("Child process already terminated", pid=child.pid)

                _gone, alive = psutil.wait_procs(children, timeout=2)
                for p in alive:
                    logger.warning("Child process did not terminate, killing", pid=p.pid, name=p.name())
                    try:
                        p.kill()
                    except psutil.NoSuchProcess:
                        logger.warning("Child process already terminated", pid=p.pid)

            except ImportError:
                logger.warning("psutil not available, falling back to signal-based termination")
                # Fallback to signal-based approach
                try:
                    logger.info("ProcessTerminator sending SIGINT to child")
                    os.kill(pid, signal.SIGINT)
                except OSError as e:
                    logger.warning("ProcessTerminator SIGINT(child) failed", error=str(e))

                try:
                    if ppid and ppid != 1:
                        logger.info("ProcessTerminator sending SIGINT to parent")
                        os.kill(ppid, signal.SIGINT)
                except OSError as e:
                    logger.warning("ProcessTerminator SIGINT(parent) failed", error=str(e))

                time.sleep(0.1)
                try:
                    logger.info("ProcessTerminator sending SIGTERM to child")
                    os.kill(pid, signal.SIGTERM)
                except OSError as e:
                    logger.warning("ProcessTerminator SIGTERM(child) failed", error=str(e))

                try:
                    if ppid and ppid != 1:
                        logger.info("ProcessTerminator sending SIGTERM to parent")
                        os.kill(ppid, signal.SIGTERM)
                except OSError as e:
                    logger.warning("ProcessTerminator SIGTERM(parent) failed", error=str(e))

            # As a last resort, force exit to avoid hanging processes
            time.sleep(0.2)
            logger.info("ProcessTerminator forcing exit with os._exit(0)")
            os._exit(0)
        except OSError as e:
            logger.error("ProcessTerminator error", error=str(e))
            # Final fallback - force exit
            logger.info("ProcessTerminator final fallback - os._exit(0)")
            os._exit(0)

    logger.info("Starting ProcessTerminator thread")
    threading.Thread(target=_terminator, name="MythosMUD-ProcessTerminator", daemon=True).start()


# --- Shutdown State Check Functions ---


def is_shutdown_pending(app: Any) -> bool:
    """
    Check if server shutdown is currently pending.

    Args:
        app: FastAPI application instance

    Returns:
        True if shutdown is pending, False otherwise
    """
    try:
        return getattr(app.state, "server_shutdown_pending", False)
    except (AttributeError, OSError):
        return False


def get_shutdown_blocking_message(context: str = "login") -> str:
    """
    Get appropriate shutdown blocking message for different contexts.

    Args:
        context: Context where blocking occurs (login, character_creation, etc.)

    Returns:
        Human-readable message explaining why action is blocked
    """
    messages = {
        "login": "Server is shutting down, please try again later",
        "character_creation": "Server is shutting down. Character creation unavailable.",
        "stats_rolling": "Server is shutting down. Please reconnect after restart.",
        "motd_progression": "Server is shutting down. Please reconnect later.",
    }

    return messages.get(context, "Server is shutting down, please try again later")


# --- Permission Validation ---


async def validate_shutdown_admin_permission(player: Any, player_name: str) -> bool:
    """
    Validate that a player has admin permissions for server shutdown.

    Args:
        player: Player object to check
        player_name: Player name for logging

    Returns:
        bool: True if player has admin permissions, False otherwise
    """
    try:
        if not player:
            logger.warning("Shutdown permission check failed - no player object", player_name=player_name)
            return False

        # Check if player has admin privileges
        if not hasattr(player, "is_admin") or not getattr(player, "is_admin", False):
            logger.warning("Shutdown permission check failed - player is not an admin", player_name=player_name)
            return False

        logger.debug("Shutdown permission check passed", player_name=player_name)
        return True

    except OSError as e:
        logger.error("Error checking shutdown admin permission", player_name=player_name, error=str(e))
        return False


# --- Countdown Notification Functions ---


def calculate_notification_times(countdown_seconds: int) -> list[int]:
    """
    Calculate notification times for countdown.

    Notifications occur:
    - Every 10 seconds when countdown > 10 seconds
    - Every second for final 10 seconds

    Args:
        countdown_seconds: Total countdown duration

    Returns:
        List of times (in seconds) when notifications should be sent, sorted descending
    """
    notification_times = set()

    # Add final 10 seconds (or all seconds if countdown <= 10)
    for i in range(1, min(11, countdown_seconds + 1)):
        notification_times.add(i)

    # Add 10-second intervals for countdown > 10
    if countdown_seconds > 10:
        current = (countdown_seconds // 10) * 10  # Round down to nearest 10
        while current >= 10:
            notification_times.add(current)
            current -= 10

    # Return sorted in descending order
    return sorted(notification_times, reverse=True)


async def broadcast_shutdown_notification(connection_manager: Any, seconds_remaining: int) -> bool:
    """
    Broadcast shutdown notification to all players.

    Args:
        connection_manager: Connection manager for broadcasting
        seconds_remaining: Seconds remaining in countdown

    Returns:
        True if broadcast successful, False otherwise
    """
    try:
        # Format message with proper singular/plural
        time_str = f"{seconds_remaining} second" if seconds_remaining == 1 else f"{seconds_remaining} seconds"
        message = f"The server will be shutting down in {time_str}"

        event_data = {
            "message": message,
            "seconds_remaining": seconds_remaining,
            "channel": "system",  # System channel for unignorable announcements
        }

        await connection_manager.broadcast_global_event("shutdown_notification", event_data)

        logger.info("Shutdown notification broadcast", seconds_remaining=seconds_remaining)
        return True

    except OSError as e:
        logger.error("Error broadcasting shutdown notification", error=str(e))
        return False


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
        # Phase 1: Persist all active player data
        logger.info("Phase 1: Persisting all active player data")
        if hasattr(app.state, "connection_manager") and app.state.connection_manager:
            try:
                # Derive connected player IDs from online players
                connected_players = [
                    p.get("player_id")
                    for p in app.state.connection_manager.get_online_players()
                    if p.get("player_id") is not None
                ]
                logger.info("Persisting connected players", count=len(connected_players))

                persistence = app.state.persistence
                for player_id in connected_players:
                    try:
                        # Get the player object first, then save it
                        player_obj = persistence.get_player(player_id)
                        if player_obj:
                            # save_player is async, so await it
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

        # Phase 2: Despawn all NPCs
        logger.info("Phase 2: Despawning all NPCs")
        if hasattr(app.state, "npc_spawning_service") and app.state.npc_spawning_service:
            try:
                npc_lifecycle_manager = getattr(app.state, "npc_lifecycle_manager", None)
                if npc_lifecycle_manager:
                    # Get all active NPC IDs from lifecycle manager
                    active_npcs = list(npc_lifecycle_manager.active_npcs.keys())
                    logger.info("Despawning active NPCs", count=len(active_npcs))

                    for npc_id in active_npcs:
                        try:
                            # despawn_npc is synchronous (returns bool)
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

        # Phase 3: Disconnect all players gracefully
        logger.info("Phase 3: Disconnecting all players")
        if hasattr(app.state, "connection_manager") and app.state.connection_manager:
            try:
                # Derive connected player IDs from online players
                connected_players = [
                    p.get("player_id")
                    for p in app.state.connection_manager.get_online_players()
                    if p.get("player_id") is not None
                ]
                logger.info("Disconnecting connected players", count=len(connected_players))

                for player_id in connected_players:
                    try:
                        # Convert string player_id to UUID if needed (force_disconnect_player expects UUID)
                        import uuid as uuid_module

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

        # Phase 4: Stop NATS message handler
        logger.info("Phase 4: Stopping NATS message handler")
        if hasattr(app.state, "nats_message_handler") and app.state.nats_message_handler:
            try:
                await app.state.nats_message_handler.stop()
                logger.info("Phase 4 complete: NATS message handler stopped")
            except OSError as e:
                logger.error("Error stopping NATS message handler", error=str(e), exc_info=True)
        else:
            logger.warning("No NATS message handler found, skipping")

        # Phase 5: Disconnect NATS service
        logger.info("Phase 5: Disconnecting NATS service")
        if hasattr(app.state, "nats_service") and app.state.nats_service:
            try:
                await app.state.nats_service.disconnect()
                logger.info("Phase 5 complete: NATS service disconnected")
            except OSError as e:
                logger.error("Error disconnecting NATS service", error=str(e), exc_info=True)
        else:
            logger.warning("No NATS service found, skipping")

        # Phase 6: Clean up connection manager
        logger.info("Phase 6: Cleaning up connection manager")
        if hasattr(app.state, "connection_manager") and app.state.connection_manager:
            try:
                await app.state.connection_manager.force_cleanup()
                logger.info("Phase 6 complete: Connection manager cleaned up")
            except OSError as e:
                logger.error("Error cleaning up connection manager", error=str(e), exc_info=True)
        else:
            logger.warning("No connection manager found, skipping cleanup")

        # Phase 7: Cancel remaining background tasks (excluding shutdown countdown)
        logger.info("Phase 7: Cancelling remaining background tasks")
        if hasattr(app.state, "task_registry") and app.state.task_registry:
            try:
                # Get the shutdown countdown task and unregister it to avoid recursion
                shutdown_data = getattr(app.state, "shutdown_data", None)
                shutdown_task = shutdown_data.get("task") if shutdown_data else None

                # Unregister the shutdown countdown task to prevent recursion
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

        logger.info("=== Graceful Shutdown Sequence Complete ===")

        # Ensure the hosting process exits after all phases complete
        logger.info("Scheduling process termination after graceful shutdown completion")
        _schedule_process_termination(0.3)

    except OSError as e:
        logger.error("Critical error during shutdown sequence", error=str(e), exc_info=True)
        raise


async def countdown_loop(app: Any, countdown_seconds: int, admin_username: str) -> None:
    """
    Main countdown loop that sends notifications and executes shutdown.

    Args:
        app: FastAPI application instance
        countdown_seconds: Total countdown duration
        admin_username: Username of admin who initiated shutdown
    """
    try:
        logger.info(
            "Shutdown countdown loop started",
            admin_username=admin_username,
            countdown_seconds=countdown_seconds,
        )

        # Calculate notification times
        notification_times = calculate_notification_times(countdown_seconds)
        start_time = time.time()
        end_time = start_time + countdown_seconds

        # Send notifications at calculated times
        for notify_at_seconds in notification_times:
            # Calculate how long to wait until this notification
            current_elapsed = time.time() - start_time
            time_until_notification = countdown_seconds - notify_at_seconds - current_elapsed

            if time_until_notification > 0:
                await asyncio.sleep(time_until_notification)

            # Check if shutdown was cancelled
            if not getattr(app.state, "server_shutdown_pending", False):
                logger.info("Shutdown countdown cancelled, exiting loop")
                return

            # Send notification
            await broadcast_shutdown_notification(app.state.connection_manager, notify_at_seconds)

        # Final wait to reach exact shutdown time
        remaining = end_time - time.time()
        if remaining > 0:
            await asyncio.sleep(remaining)

        # Check one last time if shutdown was cancelled
        if not getattr(app.state, "server_shutdown_pending", False):
            logger.info("Shutdown countdown cancelled before execution, exiting loop")
            return

        logger.info("Countdown complete, initiating shutdown sequence")

        # Execute the shutdown sequence
        await execute_shutdown_sequence(app)

    except asyncio.CancelledError:
        logger.info("Shutdown countdown cancelled by request")
        raise
    except OSError as e:
        logger.error("Error in shutdown countdown loop", error=str(e), exc_info=True)


async def initiate_shutdown_countdown(app: Any, countdown_seconds: int, admin_username: str) -> bool:
    """
    Initiate server shutdown countdown.

    Args:
        app: FastAPI application instance
        countdown_seconds: Countdown duration in seconds
        admin_username: Username of admin initiating shutdown

    Returns:
        True if countdown initiated successfully
    """
    try:
        # Cancel existing shutdown if present (superseding logic)
        if getattr(app.state, "server_shutdown_pending", False):
            existing_shutdown = getattr(app.state, "shutdown_data", None)
            if existing_shutdown and existing_shutdown.get("task"):
                logger.info("Cancelling existing shutdown to start new one")
                existing_task = existing_shutdown["task"]
                existing_task.cancel()
                try:
                    # Only await if it's actually a coroutine/task
                    if asyncio.iscoroutine(existing_task) or asyncio.isfuture(existing_task):
                        await existing_task
                except (asyncio.CancelledError, RuntimeError):
                    # Task was cancelled or already finished
                    pass

        # Set shutdown pending flag
        app.state.server_shutdown_pending = True

        # Create countdown coroutine
        countdown_coro = countdown_loop(app, countdown_seconds, admin_username)

        # Create countdown task - ensure coroutine is always turned into a task
        # to avoid "coroutine was never awaited" warnings
        # We must always create a task from the coroutine, even if register_task fails
        # This is critical to prevent RuntimeWarnings during garbage collection
        try:
            # Try to get the running event loop first
            loop = asyncio.get_running_loop()

            # Try to register with task_registry if available
            if hasattr(app.state, "task_registry") and app.state.task_registry:
                try:
                    countdown_task = app.state.task_registry.register_task(
                        countdown_coro,
                        "shutdown_countdown",
                        "system",
                    )
                    # Verify that register_task actually returned a task
                    if not isinstance(countdown_task, asyncio.Task):
                        # If register_task didn't create a task (e.g., it's a mock), create one
                        countdown_task = loop.create_task(countdown_coro)
                except (AttributeError, RuntimeError, TypeError):
                    # register_task failed or is a mock that doesn't handle coroutines
                    countdown_task = loop.create_task(countdown_coro)
            else:
                # No task_registry available, create task directly
                countdown_task = loop.create_task(countdown_coro)
        except RuntimeError:
            # No running event loop - this shouldn't happen in normal operation
            # but can occur in tests. Create task when loop becomes available.
            # Note: asyncio.create_task requires a running loop, so this will raise
            # but at least we tried. The coroutine will be garbage collected with a warning.
            try:
                countdown_task = asyncio.create_task(countdown_coro)
            except RuntimeError:
                # Still no loop - log warning and store coroutine
                # The caller should ensure there's a running loop
                logger.error("Cannot create countdown task: no running event loop")
                raise RuntimeError("Cannot create countdown task: no running event loop") from None

        # Store shutdown data
        app.state.shutdown_data = {
            "countdown_seconds": countdown_seconds,
            "start_time": time.time(),
            "end_time": time.time() + countdown_seconds,
            "admin_username": admin_username,
            "task": countdown_task,
        }

        # Log to audit trail
        admin_logger.log_admin_command(
            admin_name=admin_username,
            command="/shutdown",
            success=True,
            additional_data={
                "countdown_seconds": countdown_seconds,
                "scheduled_time": app.state.shutdown_data["end_time"],
            },
        )

        logger.info(
            "Shutdown countdown initiated",
            admin_username=admin_username,
            countdown_seconds=countdown_seconds,
        )

        return True

    except OSError as e:
        logger.error("Error initiating shutdown countdown", error=str(e), exc_info=True)
        # Clean up on failure
        app.state.server_shutdown_pending = False
        app.state.shutdown_data = None
        return False


async def cancel_shutdown_countdown(app: Any, admin_username: str) -> bool:
    """
    Cancel active shutdown countdown.

    Args:
        app: FastAPI application instance
        admin_username: Username of admin cancelling shutdown

    Returns:
        True if cancellation successful, False if no active shutdown
    """
    try:
        # Check if shutdown is active
        if not getattr(app.state, "server_shutdown_pending", False):
            logger.info("No active shutdown to cancel", admin_username=admin_username)
            return False

        shutdown_data = getattr(app.state, "shutdown_data", None)
        if not shutdown_data:
            logger.warning("Shutdown pending flag set but no shutdown_data found")
            app.state.server_shutdown_pending = False
            return False

        # Calculate remaining time for audit log
        remaining_seconds = max(0, shutdown_data["end_time"] - time.time())

        # Cancel the countdown task
        countdown_task = shutdown_data.get("task")
        if countdown_task:
            # Check if task is actually done before trying to cancel
            is_done = False
            try:
                is_done = countdown_task.done() if hasattr(countdown_task, "done") else False
            except (AttributeError, RuntimeError) as e:
                logger.error("Error checking countdown task status", error=str(e), error_type=type(e).__name__)

            if not is_done:
                countdown_task.cancel()
                try:
                    # Only await if it's actually a coroutine/task
                    if asyncio.iscoroutine(countdown_task) or asyncio.isfuture(countdown_task):
                        await countdown_task
                except (asyncio.CancelledError, RuntimeError):
                    # Task was cancelled or already finished
                    pass

        # Clear shutdown state
        app.state.server_shutdown_pending = False
        app.state.shutdown_data = None

        # Broadcast cancellation notification
        cancellation_message = "The scheduled server shutdown has been cancelled. The stars are right once more."
        event_data = {
            "message": cancellation_message,
            "channel": "system",
        }

        await app.state.connection_manager.broadcast_global_event("shutdown_cancelled", event_data)

        # Log to audit trail
        admin_logger.log_admin_command(
            admin_name=admin_username,
            command="/shutdown cancel",
            success=True,
            additional_data={
                "remaining_seconds": int(remaining_seconds),
                "cancelled_at": time.time(),
            },
        )

        logger.info("Shutdown cancelled", admin_username=admin_username, remaining_seconds=remaining_seconds)

        return True

    except OSError as e:
        logger.error("Error cancelling shutdown", error=str(e), exc_info=True)
        return False


# --- Parameter Parsing ---


def parse_shutdown_parameters(command_data: dict) -> tuple[str, int | None]:
    """
    Parse shutdown command parameters.

    Args:
        command_data: Command data dictionary containing args

    Returns:
        tuple: (action, seconds) where action is "initiate", "cancel", or "error"
               and seconds is the countdown duration or None
    """
    try:
        args = command_data.get("args", [])

        # No args - default to 10 seconds
        if not args:
            return ("initiate", 10)

        param = args[0].strip()

        # Check for cancel command
        if param.lower() == "cancel":
            return ("cancel", None)

        # Try to parse as integer
        try:
            seconds = int(param)
            if seconds <= 0:
                logger.warning("Invalid shutdown seconds (must be positive)", seconds=seconds)
                return ("error", None)
            return ("initiate", seconds)
        except ValueError:
            logger.warning("Invalid shutdown parameter (not a number or 'cancel')", param=param)
            return ("error", None)

    except OSError as e:
        logger.error("Error parsing shutdown parameters", error=str(e))
        return ("error", None)


# --- Main Command Handler ---


async def handle_shutdown_command(
    command_data: dict, _current_user: dict, request: Any, _alias_storage: AliasStorage | None, player_name: str
) -> dict[str, str]:
    """
    Handle the /shutdown command for administrators.

    Args:
        command_data: Command data dictionary containing validated command information
        _current_user: Current user information (unused)
        request: FastAPI request object
        _alias_storage: Alias storage instance (unused)
        player_name: Player name for logging

    Returns:
        dict: Shutdown command result with 'result' key
    """
    logger.debug("Processing shutdown command", player_name=player_name, command_data=command_data)

    # Get player object for permission check
    app = request.app if request else None
    player_service = app.state.player_service if app else None

    if not player_service:
        logger.warning("Shutdown command failed - no player service", player_name=player_name)
        return {"result": "Shutdown functionality is not available at this time."}

    # At this point, app must be non-None since player_service exists
    assert app is not None, "App should be available if player_service exists"

    # Get player object (use same method as other admin commands)
    player_obj = await player_service.get_player_by_name(player_name)
    if not player_obj:
        logger.warning("Shutdown command failed - player not found", player_name=player_name)
        return {"result": "Unable to verify your credentials. Shutdown unavailable."}

    # Check admin permission
    if not await validate_shutdown_admin_permission(player_obj, player_name):
        return {
            "result": (
                "You lack the proper authorization to invoke such rituals. "
                "Only those with the appropriate clearances may command these mechanisms."
            )
        }

    # Parse command parameters
    action, seconds = parse_shutdown_parameters(command_data)

    # Handle error in parsing
    if action == "error":
        return {
            "result": (
                "Invalid shutdown parameters. Usage: /shutdown [seconds] or /shutdown cancel. "
                "Seconds must be a positive number."
            )
        }

    # Handle cancel action
    if action == "cancel":
        success = await cancel_shutdown_countdown(app, player_name)
        if not success:
            return {"result": "There is no active shutdown to cancel."}
        return {"result": "Shutdown cancelled. Server will continue normal operation."}

    # Handle initiate action
    if action == "initiate":
        # AI Agent: Type guard - ensure seconds is not None for initiate action
        if seconds is None:
            return {"result": "Invalid shutdown configuration. Seconds must be specified."}

        # Check if superseding existing shutdown
        existing_shutdown = getattr(app.state, "shutdown_data", None)
        is_superseding = existing_shutdown is not None

        success = await initiate_shutdown_countdown(app, seconds, player_name)
        if not success:
            return {"result": "Error initiating server shutdown. Please try again."}

        if is_superseding:
            return {"result": f"Previous shutdown cancelled. Server will now shut down in {seconds} seconds..."}
        else:
            return {"result": f"Server shutdown initiated. Shutting down in {seconds} seconds..."}

    # Should not reach here
    logger.error("Unexpected action in shutdown command", action=action)
    return {"result": "An unexpected error occurred processing the shutdown command."}
