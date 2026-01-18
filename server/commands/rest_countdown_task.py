"""
Rest countdown task implementation.

This module contains the async task that handles the 10-second countdown
during the /rest command, including countdown messages and disconnection.
"""

# pylint: disable=too-many-arguments  # Reason: Rest countdown requires many parameters for game state and effect context

import asyncio
import uuid
from typing import Any

from anyio import sleep

from ..realtime.envelope import build_event
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

REST_COUNTDOWN_DURATION = 10.0  # 10 seconds


def _is_rest_interrupted(player_id: uuid.UUID, connection_manager: Any) -> bool:
    """
    Check if rest countdown was interrupted.

    Args:
        player_id: Player UUID
        connection_manager: Connection manager instance

    Returns:
        True if rest was interrupted, False otherwise
    """
    return player_id not in connection_manager.resting_players


async def _send_countdown_message(player_id: uuid.UUID, remaining: int, connection_manager: Any) -> None:
    """
    Send countdown message to player.

    Args:
        player_id: Player UUID
        remaining: Remaining seconds
        connection_manager: Connection manager instance
    """
    if remaining <= 0:
        return

    try:
        message = f"You will disconnect in {remaining} second{'s' if remaining != 1 else ''}..."
        countdown_event = build_event(
            "command_response",
            {"result": message},
            player_id=player_id,
            connection_manager=connection_manager,
        )
        await connection_manager.send_personal_message(player_id, countdown_event)
    except (AttributeError, RuntimeError, ValueError, TypeError) as e:
        logger.debug("Error sending countdown message", player_id=player_id, error=str(e))


async def _handle_countdown_loop(player_id: uuid.UUID, connection_manager: Any) -> bool:
    """
    Execute countdown loop, sending messages every second.

    Args:
        player_id: Player UUID
        connection_manager: Connection manager instance

    Returns:
        True if countdown completed, False if interrupted
    """
    for remaining in range(int(REST_COUNTDOWN_DURATION), 0, -1):
        if _is_rest_interrupted(player_id, connection_manager):
            logger.debug("Rest countdown cancelled (interrupted)", player_id=player_id)
            return False

        await _send_countdown_message(player_id, remaining, connection_manager)
        await sleep(1.0)

    return True


async def _disconnect_player_after_rest(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Rest countdown requires many parameters for game state and disconnection logic
    player_id: uuid.UUID,
    player_name: str,
    connection_manager: Any,
    persistence: Any,
    disconnect_func: Any,
) -> None:
    """
    Disconnect player after rest countdown completes.

    Args:
        player_id: Player UUID
        player_name: Player name
        connection_manager: Connection manager instance
        persistence: Persistence layer
        disconnect_func: Function to call for disconnection
    """
    logger.info("Rest countdown completed, disconnecting player", player_id=player_id, player_name=player_name)

    # Send intentional_disconnect event to client before disconnecting
    try:
        disconnect_event = build_event(
            "intentional_disconnect",
            {"message": "You have rested and disconnected from the game."},
            player_id=player_id,
            connection_manager=connection_manager,
        )
        await connection_manager.send_personal_message(player_id, disconnect_event)
    except (AttributeError, RuntimeError, ValueError, TypeError) as e:
        # Catching specific exceptions for event building/sending failures
        # This is non-critical since we're about to disconnect anyway
        logger.debug("Error sending intentional_disconnect event", player_id=player_id, error=str(e))

    await disconnect_func(player_id, connection_manager, persistence)


def create_rest_countdown_task(
    player_id: uuid.UUID,
    player_name: str,
    connection_manager: Any,
    persistence: Any,
    disconnect_func: Any,
) -> asyncio.Task[None]:
    """
    Create and return a rest countdown task.

    Args:
        player_id: The player's ID
        player_name: The player's name
        connection_manager: ConnectionManager instance
        persistence: Persistence layer
        disconnect_func: Function to call for disconnection

    Returns:
        asyncio.Task: The created countdown task
    """

    async def rest_countdown_task() -> None:
        try:
            # Execute countdown loop
            countdown_completed = await _handle_countdown_loop(player_id, connection_manager)

            if not countdown_completed:
                return

            # Check if rest was interrupted after loop
            if _is_rest_interrupted(player_id, connection_manager):
                logger.debug("Rest countdown cancelled (interrupted)", player_id=player_id)
                return

            # Countdown completed - disconnect player
            await _disconnect_player_after_rest(
                player_id, player_name, connection_manager, persistence, disconnect_func
            )

        except asyncio.CancelledError:
            logger.debug("Rest countdown task cancelled", player_id=player_id)
        except (AttributeError, RuntimeError, ValueError, TypeError, KeyError) as e:
            # Catching broad exceptions here is necessary because disconnect operations
            # can fail for various reasons and we must ensure the rest task is always removed
            logger.error("Error in rest countdown task", player_id=player_id, error=str(e), exc_info=True)
        finally:
            # Remove from resting players tracking
            if player_id in connection_manager.resting_players:
                del connection_manager.resting_players[player_id]

    return asyncio.create_task(rest_countdown_task())
