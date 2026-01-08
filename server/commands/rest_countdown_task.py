"""
Rest countdown task implementation.

This module contains the async task that handles the 10-second countdown
during the /rest command, including countdown messages and disconnection.
"""

import asyncio
import json
import time
import uuid
from typing import Any

from ..realtime.envelope import build_event
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

REST_COUNTDOWN_DURATION = 10.0  # 10 seconds

# #region agent log
LOG_PATH = r"e:\projects\GitHub\MythosMUD\.cursor\debug.log"
# #endregion


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
        # #region agent log
        task_start_time = time.time()
        try:
            with open(LOG_PATH, "a", encoding="utf-8") as f:
                f.write(
                    json.dumps(
                        {
                            "sessionId": "debug-session",
                            "runId": "run1",
                            "hypothesisId": "A",
                            "location": "rest_countdown_task.py:40",
                            "message": "rest_countdown_task started",
                            "data": {
                                "player_id": str(player_id),
                                "sleep_duration": REST_COUNTDOWN_DURATION,
                                "task_start_time": task_start_time,
                            },
                            "timestamp": task_start_time * 1000,
                        }
                    )
                    + "\n"
                )
        except OSError:
            # Suppress file I/O errors for debug logging - this is non-critical agent logging
            pass
        # #endregion
        try:
            # Send countdown messages every second
            for remaining in range(int(REST_COUNTDOWN_DURATION), 0, -1):
                # #region agent log
                countdown_time = time.time()
                is_still_in_dict = player_id in connection_manager.resting_players
                try:
                    with open(LOG_PATH, "a", encoding="utf-8") as f:
                        f.write(
                            json.dumps(
                                {
                                    "sessionId": "debug-session",
                                    "runId": "run1",
                                    "hypothesisId": "B",
                                    "location": "rest_countdown_task.py:70",
                                    "message": "countdown iteration",
                                    "data": {
                                        "player_id": str(player_id),
                                        "remaining": remaining,
                                        "is_still_in_resting_players": is_still_in_dict,
                                        "time_since_start": countdown_time - task_start_time,
                                    },
                                    "timestamp": countdown_time * 1000,
                                }
                            )
                            + "\n"
                        )
                except OSError:
                    # Suppress file I/O errors for debug logging - this is non-critical agent logging
                    pass
                # #endregion

                # Check if rest was interrupted
                if player_id not in connection_manager.resting_players:
                    # #region agent log
                    try:
                        with open(LOG_PATH, "a", encoding="utf-8") as f:
                            f.write(
                                json.dumps(
                                    {
                                        "sessionId": "debug-session",
                                        "runId": "run1",
                                        "hypothesisId": "A",
                                        "location": "rest_countdown_task.py:95",
                                        "message": "early exit - not in resting_players",
                                        "data": {"player_id": str(player_id), "remaining": remaining},
                                        "timestamp": time.time() * 1000,
                                    }
                                )
                                + "\n"
                            )
                    except OSError:
                        # Suppress file I/O errors for debug logging - this is non-critical agent logging
                        pass
                    # #endregion
                    logger.debug("Rest countdown cancelled (interrupted)", player_id=player_id)
                    return

                # Send countdown message to player
                if remaining > 0:
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

                # Wait 1 second (or remaining time if less than 1 second)
                await asyncio.sleep(1.0)

            # #region agent log
            sleep_end_time = time.time()
            actual_duration = sleep_end_time - task_start_time
            is_still_in_dict = player_id in connection_manager.resting_players
            try:
                with open(LOG_PATH, "a", encoding="utf-8") as f:
                    f.write(
                        json.dumps(
                            {
                                "sessionId": "debug-session",
                                "runId": "run1",
                                "hypothesisId": "C",
                                "location": "rest_countdown_task.py:145",
                                "message": "countdown loop completed",
                                "data": {
                                    "player_id": str(player_id),
                                    "actual_duration": actual_duration,
                                    "expected_duration": REST_COUNTDOWN_DURATION,
                                    "is_still_in_resting_players": is_still_in_dict,
                                },
                                "timestamp": sleep_end_time * 1000,
                            }
                        )
                        + "\n"
                    )
            except OSError:
                # Suppress file I/O errors for debug logging - this is non-critical agent logging
                pass
            # #endregion

            # Check if rest was interrupted (task may have been cancelled)
            if player_id not in connection_manager.resting_players:
                # #region agent log
                try:
                    with open(LOG_PATH, "a", encoding="utf-8") as f:
                        f.write(
                            json.dumps(
                                {
                                    "sessionId": "debug-session",
                                    "runId": "run1",
                                    "hypothesisId": "A",
                                    "location": "rest_countdown_task.py:170",
                                    "message": "early exit after loop - not in resting_players",
                                    "data": {"player_id": str(player_id)},
                                    "timestamp": time.time() * 1000,
                                }
                            )
                            + "\n"
                        )
                except OSError:
                    # Suppress file I/O errors for debug logging - this is non-critical agent logging
                    pass
                # #endregion
                logger.debug("Rest countdown cancelled (interrupted)", player_id=player_id)
                return

            # Countdown completed - disconnect player
            # #region agent log
            disconnect_start_time = time.time()
            try:
                with open(LOG_PATH, "a", encoding="utf-8") as f:
                    f.write(
                        json.dumps(
                            {
                                "sessionId": "debug-session",
                                "runId": "run1",
                                "hypothesisId": "D",
                                "location": "rest_countdown_task.py:195",
                                "message": "countdown completed - calling disconnect",
                                "data": {
                                    "player_id": str(player_id),
                                    "time_since_start": disconnect_start_time - task_start_time,
                                },
                                "timestamp": disconnect_start_time * 1000,
                            }
                        )
                        + "\n"
                    )
            except OSError:
                # Suppress file I/O errors for debug logging - this is non-critical agent logging
                pass
            # #endregion
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
            # #region agent log
            try:
                with open(LOG_PATH, "a", encoding="utf-8") as f:
                    f.write(
                        json.dumps(
                            {
                                "sessionId": "debug-session",
                                "runId": "run1",
                                "hypothesisId": "E",
                                "location": "rest_countdown_task.py:250",
                                "message": "disconnect_func completed",
                                "data": {
                                    "player_id": str(player_id),
                                },
                                "timestamp": time.time() * 1000,
                            }
                        )
                        + "\n"
                    )
            except OSError:
                pass
            # #endregion
            # #region agent log
            disconnect_end_time = time.time()
            try:
                with open(LOG_PATH, "a", encoding="utf-8") as f:
                    f.write(
                        json.dumps(
                            {
                                "sessionId": "debug-session",
                                "runId": "run1",
                                "hypothesisId": "D",
                                "location": "rest_countdown_task.py:220",
                                "message": "disconnect completed",
                                "data": {
                                    "player_id": str(player_id),
                                    "disconnect_duration": disconnect_end_time - disconnect_start_time,
                                },
                                "timestamp": disconnect_end_time * 1000,
                            }
                        )
                        + "\n"
                    )
            except OSError:
                # Suppress file I/O errors for debug logging - this is non-critical agent logging
                pass
            # #endregion

        except asyncio.CancelledError:
            # #region agent log
            cancel_time = time.time()
            try:
                with open(LOG_PATH, "a", encoding="utf-8") as f:
                    f.write(
                        json.dumps(
                            {
                                "sessionId": "debug-session",
                                "runId": "run1",
                                "hypothesisId": "E",
                                "location": "rest_countdown_task.py:240",
                                "message": "task cancelled",
                                "data": {
                                    "player_id": str(player_id),
                                    "time_since_start": cancel_time - task_start_time,
                                },
                                "timestamp": cancel_time * 1000,
                            }
                        )
                        + "\n"
                    )
            except OSError:
                # Suppress file I/O errors for debug logging - this is non-critical agent logging
                pass
            # #endregion
            logger.debug("Rest countdown task cancelled", player_id=player_id)
        except (AttributeError, RuntimeError, ValueError, TypeError, KeyError) as e:
            # #region agent log
            error_time = time.time()
            try:
                with open(LOG_PATH, "a", encoding="utf-8") as f:
                    f.write(
                        json.dumps(
                            {
                                "sessionId": "debug-session",
                                "runId": "run1",
                                "hypothesisId": "F",
                                "location": "rest_countdown_task.py:265",
                                "message": "exception in task",
                                "data": {
                                    "player_id": str(player_id),
                                    "error": str(e),
                                    "error_type": type(e).__name__,
                                    "time_since_start": error_time - task_start_time,
                                },
                                "timestamp": error_time * 1000,
                            }
                        )
                        + "\n"
                    )
            except OSError:
                # Suppress file I/O errors for debug logging - this is non-critical agent logging
                pass
            # #endregion
            # Catching broad exceptions here is necessary because disconnect operations
            # can fail for various reasons and we must ensure the rest task is always removed
            logger.error("Error in rest countdown task", player_id=player_id, error=str(e), exc_info=True)
        finally:
            # #region agent log
            finally_time = time.time()
            was_in_dict = player_id in connection_manager.resting_players
            try:
                with open(LOG_PATH, "a", encoding="utf-8") as f:
                    f.write(
                        json.dumps(
                            {
                                "sessionId": "debug-session",
                                "runId": "run1",
                                "hypothesisId": "G",
                                "location": "rest_countdown_task.py:295",
                                "message": "finally block entered",
                                "data": {
                                    "player_id": str(player_id),
                                    "was_in_dict": was_in_dict,
                                    "time_since_start": finally_time - task_start_time,
                                },
                                "timestamp": finally_time * 1000,
                            }
                        )
                        + "\n"
                    )
            except OSError:
                # Suppress file I/O errors for debug logging - this is non-critical agent logging
                pass
            # #endregion
            # Remove from resting players tracking
            if player_id in connection_manager.resting_players:
                # #region agent log
                try:
                    with open(LOG_PATH, "a", encoding="utf-8") as f:
                        f.write(
                            json.dumps(
                                {
                                    "sessionId": "debug-session",
                                    "runId": "run1",
                                    "hypothesisId": "G",
                                    "location": "rest_countdown_task.py:320",
                                    "message": "removing from resting_players",
                                    "data": {"player_id": str(player_id)},
                                    "timestamp": time.time() * 1000,
                                }
                            )
                            + "\n"
                        )
                except OSError:
                    # Suppress file I/O errors for debug logging - this is non-critical agent logging
                    pass
                # #endregion
                del connection_manager.resting_players[player_id]

    return asyncio.create_task(rest_countdown_task())
