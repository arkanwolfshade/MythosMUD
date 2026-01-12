"""
Disconnect grace period management for MythosMUD.

This module handles the 30-second grace period after unintentional disconnects,
allowing characters to remain in-game in a "zombie" state where they can be
attacked and will auto-attack back, but cannot take other actions.

As documented in "Temporal Mechanics of Eldritch Disconnection" - Dr. Armitage, 1930,
the grace period provides a window for reconnection while maintaining game integrity.
"""

import asyncio
import uuid
from typing import Any

from ..structured_logging.enhanced_logging_config import get_logger
from .player_disconnect_handlers import (
    _cleanup_player_references,
    _collect_disconnect_keys,
    _remove_player_from_online_tracking,
    handle_player_disconnect_broadcast,
)
from .player_presence_utils import extract_player_name

logger = get_logger(__name__)

GRACE_PERIOD_DURATION = 30.0  # 30 seconds


async def start_grace_period(
    player_id: uuid.UUID,
    manager: Any,  # ConnectionManager
) -> None:
    """
    Start a grace period for a disconnected player.

    During the grace period, the player remains in-game in a zombie state:
    - Can be attacked and will auto-attack back
    - Cannot move, use commands, or take other actions
    - Shows "(linkdead)" indicator to other players
    - Reconnection cancels the grace period immediately

    Args:
        player_id: The player's ID
        manager: ConnectionManager instance
    """
    # Check if already in grace period
    if player_id in manager.grace_period_players:
        logger.debug("Player already in grace period", player_id=player_id)
        return

    logger.info("Starting grace period for player", player_id=player_id, duration=GRACE_PERIOD_DURATION)

    # Create grace period task
    async def grace_period_task() -> None:
        try:
            # Wait for grace period duration
            await asyncio.sleep(GRACE_PERIOD_DURATION)

            # Check if player reconnected (task may have been cancelled)
            if player_id not in manager.grace_period_players:
                logger.debug("Grace period cancelled (player reconnected)", player_id=player_id)
                return

            # Grace period expired - perform normal disconnect cleanup
            logger.info("Grace period expired, performing disconnect cleanup", player_id=player_id)

            # Resolve player
            pl = await manager._get_player(player_id)  # pylint: disable=protected-access
            room_id: str | None = getattr(pl, "current_room_id", None) if pl else None
            player_name: str = extract_player_name(pl, player_id) if pl else "Unknown Player"

            # Collect all keys to remove
            keys_to_remove, keys_to_remove_str = _collect_disconnect_keys(player_id, pl)

            # Handle disconnect broadcast (player is now actually leaving)
            await handle_player_disconnect_broadcast(player_id, player_name, room_id, manager)

            # Remove player from online tracking
            _remove_player_from_online_tracking(keys_to_remove, keys_to_remove_str, manager)

            # Clean up ghost players
            manager._cleanup_ghost_players()  # pylint: disable=protected-access

            # Clean up remaining references
            _cleanup_player_references(player_id, manager)

        except asyncio.CancelledError:
            logger.debug("Grace period task cancelled", player_id=player_id)
        except (AttributeError, RuntimeError, ValueError, TypeError, KeyError) as e:
            # Catching broad exceptions here is necessary because cleanup operations
            # can fail for various reasons (missing attributes, database errors, etc.)
            # and we must ensure the grace period task is always removed from tracking
            logger.error("Error in grace period task", player_id=player_id, error=str(e), exc_info=True)
        finally:
            # Remove from grace period tracking
            if player_id in manager.grace_period_players:
                del manager.grace_period_players[player_id]

    # Store the task
    task = asyncio.create_task(grace_period_task())
    manager.grace_period_players[player_id] = task


async def cancel_grace_period(
    player_id: uuid.UUID,
    manager: Any,  # ConnectionManager
) -> None:
    """
    Cancel grace period for a player (e.g., on reconnection).

    Args:
        player_id: The player's ID
        manager: ConnectionManager instance
    """
    if player_id not in manager.grace_period_players:
        return

    logger.info("Cancelling grace period for player", player_id=player_id)

    task = manager.grace_period_players[player_id]
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        pass
    except (AttributeError, RuntimeError, ValueError, TypeError) as e:
        # Catching broad exceptions here is necessary because task cancellation
        # can fail for various reasons and we must ensure cleanup completes
        logger.error("Error cancelling grace period task", player_id=player_id, error=str(e), exc_info=True)
    finally:
        if player_id in manager.grace_period_players:
            del manager.grace_period_players[player_id]


def is_player_in_grace_period(player_id: uuid.UUID, manager: Any) -> bool:
    """
    Check if a player is currently in grace period.

    Args:
        player_id: The player's ID
        manager: ConnectionManager instance

    Returns:
        True if player is in grace period, False otherwise
    """
    if not hasattr(manager, "grace_period_players"):
        return False

    return player_id in manager.grace_period_players
