"""
Rest countdown task implementation.

This module contains the async task that handles the 10-second countdown
during the /rest command, including countdown messages and disconnection.
"""

# pylint: disable=too-many-arguments  # Reason: Rest countdown requires many parameters for game state and effect context

import asyncio
import json
import time
import uuid
from typing import Any

from anyio import sleep

from ..realtime.envelope import build_event
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

REST_COUNTDOWN_DURATION = 10.0  # 10 seconds

# #region agent log
LOG_PATH = r"e:\projects\GitHub\MythosMUD\.cursor\debug.log"
# #endregion


def _write_debug_log(message: str, location: str, hypothesis_id: str, data: dict[str, Any]) -> None:
    """
    Write debug log entry (non-critical, suppresses I/O errors).

    Args:
        message: Log message
        location: Code location
        hypothesis_id: Hypothesis identifier
        data: Additional data to log
    """
    try:
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(
                json.dumps(
                    {
                        "sessionId": "debug-session",
                        "runId": "run1",
                        "hypothesisId": hypothesis_id,
                        "location": location,
                        "message": message,
                        "data": data,
                        "timestamp": time.time() * 1000,
                    }
                )
                + "\n"
            )
    except OSError:
        # Suppress file I/O errors for debug logging - this is non-critical agent logging
        pass


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


async def _handle_countdown_loop(player_id: uuid.UUID, connection_manager: Any, task_start_time: float) -> bool:
    """
    Execute countdown loop, sending messages every second.

    Args:
        player_id: Player UUID
        connection_manager: Connection manager instance
        task_start_time: Task start timestamp

    Returns:
        True if countdown completed, False if interrupted
    """
    for remaining in range(int(REST_COUNTDOWN_DURATION), 0, -1):
        countdown_time = time.time()
        _write_debug_log(
            "countdown iteration",
            "rest_countdown_task.py:70",
            "B",
            {
                "player_id": str(player_id),
                "remaining": remaining,
                "is_still_in_resting_players": player_id in connection_manager.resting_players,
                "time_since_start": countdown_time - task_start_time,
            },
        )

        if _is_rest_interrupted(player_id, connection_manager):
            _write_debug_log(
                "early exit - not in resting_players",
                "rest_countdown_task.py:95",
                "A",
                {"player_id": str(player_id), "remaining": remaining},
            )
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
    task_start_time: float,
) -> None:
    """
    Disconnect player after rest countdown completes.

    Args:
        player_id: Player UUID
        player_name: Player name
        connection_manager: Connection manager instance
        persistence: Persistence layer
        disconnect_func: Function to call for disconnection
        task_start_time: Task start timestamp
    """
    disconnect_start_time = time.time()
    _write_debug_log(
        "countdown completed - calling disconnect",
        "rest_countdown_task.py:195",
        "D",
        {
            "player_id": str(player_id),
            "time_since_start": disconnect_start_time - task_start_time,
        },
    )

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

    _write_debug_log(
        "disconnect_func completed",
        "rest_countdown_task.py:250",
        "E",
        {"player_id": str(player_id)},
    )

    disconnect_end_time = time.time()
    _write_debug_log(
        "disconnect completed",
        "rest_countdown_task.py:220",
        "D",
        {
            "player_id": str(player_id),
            "disconnect_duration": disconnect_end_time - disconnect_start_time,
        },
    )


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
        task_start_time = time.time()
        _write_debug_log(
            "rest_countdown_task started",
            "rest_countdown_task.py:40",
            "A",
            {
                "player_id": str(player_id),
                "sleep_duration": REST_COUNTDOWN_DURATION,
                "task_start_time": task_start_time,
            },
        )

        try:
            # Execute countdown loop
            countdown_completed = await _handle_countdown_loop(player_id, connection_manager, task_start_time)

            if not countdown_completed:
                return

            # Log countdown loop completion
            sleep_end_time = time.time()
            _write_debug_log(
                "countdown loop completed",
                "rest_countdown_task.py:145",
                "C",
                {
                    "player_id": str(player_id),
                    "actual_duration": sleep_end_time - task_start_time,
                    "expected_duration": REST_COUNTDOWN_DURATION,
                    "is_still_in_resting_players": player_id in connection_manager.resting_players,
                },
            )

            # Check if rest was interrupted after loop
            if _is_rest_interrupted(player_id, connection_manager):
                _write_debug_log(
                    "early exit after loop - not in resting_players",
                    "rest_countdown_task.py:170",
                    "A",
                    {"player_id": str(player_id)},
                )
                logger.debug("Rest countdown cancelled (interrupted)", player_id=player_id)
                return

            # Countdown completed - disconnect player
            await _disconnect_player_after_rest(
                player_id, player_name, connection_manager, persistence, disconnect_func, task_start_time
            )

        except asyncio.CancelledError:
            cancel_time = time.time()
            _write_debug_log(
                "task cancelled",
                "rest_countdown_task.py:240",
                "E",
                {
                    "player_id": str(player_id),
                    "time_since_start": cancel_time - task_start_time,
                },
            )
            logger.debug("Rest countdown task cancelled", player_id=player_id)
        except (AttributeError, RuntimeError, ValueError, TypeError, KeyError) as e:
            error_time = time.time()
            _write_debug_log(
                "exception in task",
                "rest_countdown_task.py:265",
                "F",
                {
                    "player_id": str(player_id),
                    "error": str(e),
                    "error_type": type(e).__name__,
                    "time_since_start": error_time - task_start_time,
                },
            )
            # Catching broad exceptions here is necessary because disconnect operations
            # can fail for various reasons and we must ensure the rest task is always removed
            logger.error("Error in rest countdown task", player_id=player_id, error=str(e), exc_info=True)
        finally:
            finally_time = time.time()
            _write_debug_log(
                "finally block entered",
                "rest_countdown_task.py:295",
                "G",
                {
                    "player_id": str(player_id),
                    "was_in_dict": player_id in connection_manager.resting_players,
                    "time_since_start": finally_time - task_start_time,
                },
            )
            # Remove from resting players tracking
            if player_id in connection_manager.resting_players:
                _write_debug_log(
                    "removing from resting_players",
                    "rest_countdown_task.py:320",
                    "G",
                    {"player_id": str(player_id)},
                )
                del connection_manager.resting_players[player_id]

    return asyncio.create_task(rest_countdown_task())
