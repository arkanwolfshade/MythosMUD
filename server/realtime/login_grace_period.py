"""
Login grace period management for MythosMUD.

This module handles the 10-second grace period after a player logs in,
providing immunity to damage and negative effects while allowing movement.

As documented in "Protective Wards Upon Entering the Realms" - Dr. Armitage, 1930,
the grace period provides a brief window of protection for newly arrived characters.
"""

import asyncio
import time
import uuid
from typing import Any, cast

from anyio import sleep

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

LOGIN_GRACE_PERIOD_DURATION = 10.0  # 10 seconds


def _remove_from_grace_period_tracking(player_id: uuid.UUID, manager: Any) -> None:
    """Remove player from grace period tracking dictionaries."""
    if player_id in manager.login_grace_period_players:
        del manager.login_grace_period_players[player_id]
    if (
        hasattr(manager, "login_grace_period_start_times")
        and player_id in manager.login_grace_period_start_times
    ):
        del manager.login_grace_period_start_times[player_id]


async def _trigger_room_occupants_update(player_id: uuid.UUID, manager: Any) -> None:
    """Trigger room occupants update after grace period expiration."""
    try:
        if not (hasattr(manager, "async_persistence") and manager.async_persistence):
            return

        player = await manager.get_player(player_id)
        if not (player and hasattr(player, "current_room_id") and player.current_room_id):
            return

        room_id = str(player.current_room_id)
        if not (hasattr(manager, "app") and manager.app):
            return

        try:
            if not hasattr(manager.app.state, "container"):
                return

            container = manager.app.state.container
            if not (container and hasattr(container, "real_time_event_handler")):
                return

            event_handler = container.real_time_event_handler
            if not (event_handler and hasattr(event_handler, "send_room_occupants_update")):
                return

            await event_handler.send_room_occupants_update(room_id)
            logger.info("Triggered room occupants update after grace period expiration", player_id=player_id, room_id=room_id)
        except (AttributeError, TypeError) as app_error:
            logger.debug("Could not access app state container", player_id=player_id, error=str(app_error))
    except (AttributeError, RuntimeError, ValueError, TypeError, KeyError) as e:
        logger.warning("Could not trigger room occupants update after grace period expiration", player_id=player_id, error=str(e))


async def _grace_period_expiration_handler(player_id: uuid.UUID, manager: Any) -> None:
    """Handle grace period expiration - remove tracking and trigger updates."""
    # Grace period expired - remove from tracking FIRST to prevent race condition
    # CRITICAL: Remove from tracking BEFORE triggering room occupants update
    # This ensures that when the update queries grace period status, it will correctly
    # return False, preventing "(warded)" from appearing after expiration
    logger.info("Login grace period expired", player_id=player_id)

    # Remove from grace period tracking BEFORE triggering update
    _remove_from_grace_period_tracking(player_id, manager)

    # Get player's current room to trigger occupants update
    # Now that player is removed from tracking, the grace period check will return False
    await _trigger_room_occupants_update(player_id, manager)


async def _grace_period_task(player_id: uuid.UUID, manager: Any) -> None:
    """Internal task that waits for grace period duration and handles expiration."""
    try:
        # Wait for grace period duration
        await sleep(LOGIN_GRACE_PERIOD_DURATION)

        # Check if player is still in grace period (task may have been cancelled)
        if player_id not in manager.login_grace_period_players:
            logger.debug("Login grace period cancelled", player_id=player_id)
            return

        await _grace_period_expiration_handler(player_id, manager)

    except asyncio.CancelledError:
        logger.debug("Login grace period task cancelled", player_id=player_id)
    except (AttributeError, RuntimeError, ValueError, TypeError, KeyError) as e:
        # Catching broad exceptions here is necessary because cleanup operations
        # can fail for various reasons and we must ensure the grace period task
        # is always removed from tracking
        logger.error("Error in login grace period task", player_id=player_id, error=str(e), exc_info=True)
    finally:
        # Ensure cleanup even if exception occurred (defensive cleanup)
        # Note: If expiration completed successfully, player was already removed above
        _remove_from_grace_period_tracking(player_id, manager)


async def start_login_grace_period(
    player_id: uuid.UUID,
    manager: Any,  # ConnectionManager
) -> None:
    """
    Start a login grace period for a player.

    During the grace period, the player:
    - Is immune to all damage and negative status effects
    - Cannot initiate combat
    - Hostile NPCs/mobs ignore them
    - Can move freely
    - Shows "(warded)" indicator to other players

    Args:
        player_id: The player's ID
        manager: ConnectionManager instance
    """
    # Check if already in grace period
    if player_id in manager.login_grace_period_players:
        logger.debug("Player already in login grace period", player_id=player_id)
        return

    logger.info("Starting login grace period for player", player_id=player_id, duration=LOGIN_GRACE_PERIOD_DURATION)

    # Store start timestamp for remaining time calculation
    start_time = time.time()
    manager.login_grace_period_start_times[player_id] = start_time

    # Store the task
    task = asyncio.create_task(_grace_period_task(player_id, manager))
    manager.login_grace_period_players[player_id] = task


async def cancel_login_grace_period(
    player_id: uuid.UUID,
    manager: Any,  # ConnectionManager
) -> None:
    """
    Cancel login grace period for a player (if needed).

    Args:
        player_id: The player's ID
        manager: ConnectionManager instance
    """
    if player_id not in manager.login_grace_period_players:
        return

    logger.info("Cancelling login grace period for player", player_id=player_id)

    task = manager.login_grace_period_players[player_id]
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        pass
    except (AttributeError, RuntimeError, ValueError, TypeError) as e:
        # Catching broad exceptions here is necessary because task cancellation
        # can fail for various reasons and we must ensure cleanup completes
        logger.error("Error cancelling login grace period task", player_id=player_id, error=str(e), exc_info=True)
    finally:
        _remove_from_grace_period_tracking(player_id, manager)


def is_player_in_login_grace_period(player_id: uuid.UUID, manager: Any) -> bool:
    """
    Check if a player is currently in login grace period.

    Args:
        player_id: The player's ID
        manager: ConnectionManager instance

    Returns:
        True if player is in login grace period, False otherwise
    """
    if not hasattr(manager, "login_grace_period_players"):
        return False

    return player_id in manager.login_grace_period_players


def get_login_grace_period_remaining(player_id: uuid.UUID, manager: Any) -> float:
    """
    Get the remaining time in seconds for a player's login grace period.

    Args:
        player_id: The player's ID
        manager: ConnectionManager instance

    Returns:
        Remaining time in seconds, or 0.0 if not in grace period or start time not found
    """
    if not is_player_in_login_grace_period(player_id, manager):
        return 0.0

    if not hasattr(manager, "login_grace_period_start_times"):
        return 0.0

    if player_id not in manager.login_grace_period_start_times:
        return 0.0

    start_time = manager.login_grace_period_start_times[player_id]
    elapsed = time.time() - start_time
    remaining: float = cast(float, max(0.0, LOGIN_GRACE_PERIOD_DURATION - elapsed))

    return remaining
