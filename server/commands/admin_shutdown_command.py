"""
Admin shutdown command for MythosMUD.

This module provides the /shutdown command for administrators to gracefully
shut down the server with configurable countdown notifications.

As noted in the Necronomicon's appendices, proper termination rituals
are essential for maintaining the integrity of dimensional boundaries
during the closure of arcane gateways.
"""

# pylint: disable=too-many-lines  # Reason: Shutdown command requires extensive countdown logic, notification handling, and graceful shutdown procedures

import asyncio
import time
from typing import Any

from anyio import sleep

from ..alias_storage import AliasStorage
from ..structured_logging.admin_actions_logger import AdminActionsLogger
from ..structured_logging.enhanced_logging_config import get_logger
from .shutdown_sequence import execute_shutdown_sequence

logger = get_logger(__name__)

# Initialize admin actions logger for audit trail
admin_logger = AdminActionsLogger()


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
        if hasattr(app.state, "container") and app.state.container:
            return app.state.container.server_shutdown_pending
        # Fallback to app.state for backward compatibility
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

        # Handle case where connection_manager might be a mock in tests
        broadcast_method = getattr(connection_manager, "broadcast_global_event", None)
        if broadcast_method is not None:
            try:
                await broadcast_method("shutdown_notification", event_data)
            except TypeError:
                # Handle case where broadcast_method is a MagicMock that can't be awaited
                # This happens in tests - silently skip the broadcast
                logger.debug("Skipping shutdown notification broadcast (mock connection manager)")
                return False

        logger.info("Shutdown notification broadcast", seconds_remaining=seconds_remaining)
        return True

    except OSError as e:
        logger.error("Error broadcasting shutdown notification", error=str(e))
        return False


async def _cancel_existing_shutdown_task(app: Any) -> None:
    """
    Cancel existing shutdown task if present.

    Args:
        app: FastAPI application instance
    """
    if not getattr(app.state, "server_shutdown_pending", False):
        return

    existing_shutdown = getattr(app.state, "shutdown_data", None)
    if not existing_shutdown or not existing_shutdown.get("task"):
        return

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


def _set_shutdown_pending_flag(app: Any) -> None:
    """
    Set shutdown pending flag in container and app.state.

    Args:
        app: FastAPI application instance
    """
    if hasattr(app.state, "container") and app.state.container:
        app.state.container.server_shutdown_pending = True
    # Backward compatibility: also set in app.state
    app.state.server_shutdown_pending = True


async def _create_countdown_task(app: Any, countdown_coro: Any) -> asyncio.Task:
    """
    Create countdown task from coroutine, handling task registry if available.

    Args:
        app: FastAPI application instance
        countdown_coro: Countdown coroutine to wrap in task

    Returns:
        asyncio.Task: The created countdown task

    Raises:
        RuntimeError: If no running event loop is available
    """
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
                return countdown_task
            except (AttributeError, RuntimeError, TypeError):
                # register_task failed or is a mock that doesn't handle coroutines
                return loop.create_task(countdown_coro)
        else:
            # No task_registry available, create task directly
            return loop.create_task(countdown_coro)
    except RuntimeError:
        # No running event loop - this shouldn't happen in normal operation
        # but can occur in tests. Create task when loop becomes available.
        # Note: asyncio.create_task requires a running loop, so this will raise
        # but at least we tried. The coroutine will be garbage collected with a warning.
        try:
            return asyncio.create_task(countdown_coro)
        except RuntimeError:
            # Still no loop - log warning and raise error
            # The caller should ensure there's a running loop
            logger.error("Cannot create countdown task: no running event loop")
            raise RuntimeError("Cannot create countdown task: no running event loop") from None


def _store_shutdown_data(
    app: Any, countdown_seconds: int, admin_username: str, countdown_task: asyncio.Task
) -> dict[str, Any]:
    """
    Store shutdown data in container and app.state.

    Args:
        app: FastAPI application instance
        countdown_seconds: Countdown duration in seconds
        admin_username: Username of admin initiating shutdown
        countdown_task: The countdown task

    Returns:
        dict: The shutdown data dictionary
    """
    shutdown_data = {
        "countdown_seconds": countdown_seconds,
        "start_time": time.time(),
        "end_time": time.time() + countdown_seconds,
        "admin_username": admin_username,
        "task": countdown_task,
    }
    if hasattr(app.state, "container") and app.state.container:
        app.state.container.shutdown_data = shutdown_data
    # Backward compatibility: also set in app.state
    app.state.shutdown_data = shutdown_data
    return shutdown_data


def _clear_shutdown_state(app: Any) -> None:
    """
    Clear shutdown state in container and app.state.

    Args:
        app: FastAPI application instance
    """
    if hasattr(app.state, "container") and app.state.container:
        app.state.container.server_shutdown_pending = False
        app.state.container.shutdown_data = None
    # Backward compatibility: also clear in app.state
    app.state.server_shutdown_pending = False
    app.state.shutdown_data = None


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
                await sleep(time_until_notification)

            # Check if shutdown was cancelled
            if not getattr(app.state, "server_shutdown_pending", False):
                logger.info("Shutdown countdown cancelled, exiting loop")
                return

            # Send notification
            await broadcast_shutdown_notification(app.state.connection_manager, notify_at_seconds)

        # Final wait to reach exact shutdown time
        remaining = end_time - time.time()
        if remaining > 0:
            await sleep(remaining)

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
        await _cancel_existing_shutdown_task(app)

        # Set shutdown pending flag in container
        _set_shutdown_pending_flag(app)

        # Create countdown coroutine and task
        countdown_coro = countdown_loop(app, countdown_seconds, admin_username)
        countdown_task = await _create_countdown_task(app, countdown_coro)

        # Store shutdown data in container
        shutdown_data = _store_shutdown_data(app, countdown_seconds, admin_username, countdown_task)

        # Log to audit trail
        admin_logger.log_admin_command(
            admin_name=admin_username,
            command="/shutdown",
            success=True,
            additional_data={
                "countdown_seconds": countdown_seconds,
                "scheduled_time": shutdown_data["end_time"],
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
        _clear_shutdown_state(app)
        return False


def _get_shutdown_state(app: Any) -> tuple[bool, dict[str, Any] | None]:
    """
    Get shutdown state from container or app.state.

    Args:
        app: FastAPI application instance

    Returns:
        tuple: (shutdown_pending, shutdown_data)
    """
    if hasattr(app.state, "container") and app.state.container:
        return (
            app.state.container.server_shutdown_pending,
            app.state.container.shutdown_data,
        )
    # Fallback to app.state for backward compatibility
    return (
        getattr(app.state, "server_shutdown_pending", False),
        getattr(app.state, "shutdown_data", None),
    )


async def _cancel_countdown_task(countdown_task: Any) -> None:
    """
    Cancel countdown task if it's not already done.

    Args:
        countdown_task: The countdown task to cancel
    """
    if not countdown_task:
        return

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


async def _broadcast_shutdown_cancellation(connection_manager: Any) -> None:
    """
    Broadcast shutdown cancellation notification.

    Args:
        connection_manager: Connection manager for broadcasting
    """
    cancellation_message = "The scheduled server shutdown has been cancelled. The stars are right once more."
    event_data = {
        "message": cancellation_message,
        "channel": "system",
    }

    await connection_manager.broadcast_global_event("shutdown_cancelled", event_data)


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
        # Check if shutdown is active (prefer container, fallback to app.state)
        shutdown_pending, shutdown_data = _get_shutdown_state(app)

        if not shutdown_pending:
            logger.info("No active shutdown to cancel", admin_username=admin_username)
            return False
        if not shutdown_data:
            logger.warning("Shutdown pending flag set but no shutdown_data found")
            _clear_shutdown_state(app)
            return False

        # Calculate remaining time for audit log
        remaining_seconds = max(0, shutdown_data["end_time"] - time.time())

        # Cancel the countdown task
        countdown_task = shutdown_data.get("task")
        await _cancel_countdown_task(countdown_task)

        # Clear shutdown state in container
        _clear_shutdown_state(app)

        # Broadcast cancellation notification
        await _broadcast_shutdown_cancellation(app.state.connection_manager)

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


async def _get_shutdown_services(request: Any) -> tuple[Any, Any]:
    """Get app and player_service from request. Returns (app, player_service)."""
    app = request.app if request else None
    player_service = app.state.player_service if app else None
    return app, player_service


async def _validate_shutdown_context(
    app: Any, player_service: Any, player_name: str
) -> tuple[Any, dict[str, str] | None]:
    """Validate shutdown context and get player. Returns (player_obj, error_dict)."""
    if not player_service:
        logger.warning("Shutdown command failed - no player service", player_name=player_name)
        return None, {"result": "Shutdown functionality is not available at this time."}

    if app is None:
        raise RuntimeError("App should be available if player_service exists")

    player_obj = await player_service.get_player_by_name(player_name)
    if not player_obj:
        logger.warning("Shutdown command failed - player not found", player_name=player_name)
        return None, {"result": "Unable to verify your credentials. Shutdown unavailable."}

    if not await validate_shutdown_admin_permission(player_obj, player_name):
        return None, {
            "result": (
                "You lack the proper authorization to invoke such rituals. "
                "Only those with the appropriate clearances may command these mechanisms."
            )
        }

    return player_obj, None


async def _handle_shutdown_cancel(app: Any, player_name: str) -> dict[str, str]:
    """Handle shutdown cancel action. Returns result dict."""
    success = await cancel_shutdown_countdown(app, player_name)
    if not success:
        return {"result": "There is no active shutdown to cancel."}
    return {"result": "Shutdown cancelled. Server will continue normal operation."}


async def _handle_shutdown_initiate(app: Any, seconds: int, player_name: str) -> dict[str, str]:
    """Handle shutdown initiate action. Returns result dict."""
    existing_shutdown = getattr(app.state, "shutdown_data", None)
    is_superseding = existing_shutdown is not None

    success = await initiate_shutdown_countdown(app, seconds, player_name)
    if not success:
        return {"result": "Error initiating server shutdown. Please try again."}

    if is_superseding:
        return {"result": f"Previous shutdown cancelled. Server will now shut down in {seconds} seconds..."}
    return {"result": f"Server shutdown initiated. Shutting down in {seconds} seconds..."}


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

    app, player_service = await _get_shutdown_services(request)

    _, error_result = await _validate_shutdown_context(app, player_service, player_name)
    if error_result:
        return error_result

    action, seconds = parse_shutdown_parameters(command_data)

    if action == "error":
        return {
            "result": (
                "Invalid shutdown parameters. Usage: /shutdown [seconds] or /shutdown cancel. "
                "Seconds must be a positive number."
            )
        }

    if action == "cancel":
        return await _handle_shutdown_cancel(app, player_name)

    if action == "initiate":
        if seconds is None:
            return {"result": "Invalid shutdown configuration. Seconds must be specified."}
        return await _handle_shutdown_initiate(app, seconds, player_name)

    logger.error("Unexpected action in shutdown command", action=action)
    return {"result": "An unexpected error occurred processing the shutdown command."}
