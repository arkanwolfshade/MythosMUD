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
from typing import Any, Protocol, cast

from anyio import sleep

from ..config import get_config
from ..models.player import Player
from ..structured_logging.enhanced_logging_config import get_logger
from .disconnect_catchup import CatchupManager, capture_grace_snapshot
from .player_disconnect_handlers import (
    _cleanup_player_references,
    _collect_disconnect_keys,
    _remove_player_from_online_tracking,
    handle_player_disconnect_broadcast,
)
from .player_presence_utils import extract_player_name

logger = get_logger(__name__)

GRACE_PERIOD_DURATION = 30.0  # 30 seconds (GameConfig.disconnect_grace_period_seconds default)


class _PlayerLookupManager(Protocol):  # pylint: disable=too-few-public-methods
    """The one typed slice of ConnectionManager needed to snapshot DP at grace start."""

    async def _get_player(self, player_id: uuid.UUID) -> Player | None: ...


def _grace_period_seconds() -> float:
    """Read the disconnect grace period duration from `GameConfig` (`#297`), retunable via
    `GAME_DISCONNECT_GRACE_PERIOD_SECONDS` without a redeploy."""
    return get_config().game.disconnect_grace_period_seconds


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

    duration = _grace_period_seconds()
    logger.info("Starting grace period for player", player_id=player_id, duration=duration)

    # Snapshot DP now, for the reconnect catch-up summary (#297). Best-effort: a snapshot
    # failure must never block the grace period itself from starting.
    lookup_manager = cast(_PlayerLookupManager, manager)
    catchup_manager = cast(CatchupManager, manager)
    try:
        pl_at_start = await lookup_manager._get_player(  # pyright: ignore[reportPrivateUsage]  # pylint: disable=protected-access  # Reason: Accessing protected member _get_player is necessary for disconnect grace period implementation, this is part of the internal API
            player_id
        )
        if pl_at_start is not None:
            capture_grace_snapshot(player_id, pl_at_start, catchup_manager)
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: Best-effort snapshot; any failure here must not prevent the grace period from starting
        logger.debug("Could not snapshot DP for grace period catch-up", player_id=player_id, error=str(e))

    # Create grace period task
    async def grace_period_task() -> None:
        try:
            # Wait for grace period duration
            await sleep(duration)

            # Check if player reconnected (task may have been cancelled)
            if player_id not in manager.grace_period_players:
                logger.debug("Grace period cancelled (player reconnected)", player_id=player_id)
                return

            # Grace period expired - perform normal disconnect cleanup
            logger.info("Grace period expired, performing disconnect cleanup", player_id=player_id)

            # Resolve player
            pl = await lookup_manager._get_player(player_id)  # pyright: ignore[reportPrivateUsage]  # pylint: disable=protected-access  # Reason: Accessing protected member _get_player is necessary for disconnect grace period implementation, this is part of the internal API
            room_id: str | None = getattr(pl, "current_room_id", None) if pl else None
            player_name: str = extract_player_name(pl, player_id) if pl else "Unknown Player"

            # Collect all keys to remove
            keys_to_remove, keys_to_remove_str = _collect_disconnect_keys(player_id, pl)

            # Handle disconnect broadcast (player is now actually leaving)
            await handle_player_disconnect_broadcast(player_id, player_name, room_id, manager)

            # Remove player from online tracking
            _remove_player_from_online_tracking(keys_to_remove, keys_to_remove_str, manager)

            # Clean up ghost players
            manager._cleanup_ghost_players()  # pylint: disable=protected-access  # Reason: Accessing protected member _cleanup_ghost_players is necessary for disconnect grace period implementation, this is part of the internal API

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
            _ = catchup_manager.grace_period_snapshots.pop(player_id, None)

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

    catchup_manager = cast(CatchupManager, manager)
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
        _ = catchup_manager.grace_period_snapshots.pop(player_id, None)


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
