"""
Rest command handler for clean disconnection.

This module handles the /rest command which allows players to cleanly disconnect
from the game. In rest locations (inns/hotels/motels), disconnection is instant
when not in combat. Otherwise, a 10-second countdown begins during which the
player can be interrupted by combat, movement, or spellcasting.

As documented in "The Art of Restful Departure" - Dr. Armitage, 1931,
proper rest requires tranquility and freedom from disturbance.
"""

# pylint: disable=too-many-return-statements  # Reason: Rest command handler requires multiple return statements for early validation returns (combat checks, rest location validation, error handling)

import asyncio
import uuid
from typing import Any

from ..alias_storage import AliasStorage
from ..services.player_position_service import PlayerPositionService
from ..structured_logging.enhanced_logging_config import get_logger
from .rest_countdown_task import create_rest_countdown_task

logger = get_logger(__name__)

REST_COUNTDOWN_DURATION = 10.0  # 10 seconds


async def _check_player_in_combat(player_id: uuid.UUID, app: Any) -> bool:
    """
    Check if a player is currently in combat.

    Args:
        player_id: The player's ID
        app: FastAPI app instance

    Returns:
        True if player is in combat, False otherwise
    """
    combat_service = getattr(app.state, "combat_service", None) if app else None
    if not combat_service:
        return False

    try:
        combat = await combat_service.get_combat_by_participant(str(player_id))
        return combat is not None
    except (AttributeError, TypeError, ValueError) as e:
        logger.debug("Error checking combat status", player_id=player_id, error=str(e))
        return False


async def _check_rest_location(room_id: str | None, persistence: Any) -> bool:
    """
    Check if the current room is a rest location (inn/hotel/motel).

    Args:
        room_id: The room ID
        persistence: Persistence layer

    Returns:
        True if room is a rest location, False otherwise
    """
    if not room_id or not persistence:
        return False

    try:
        room = persistence.get_room_by_id(room_id)
        if room and hasattr(room, "rest_location"):
            return room.rest_location
    except (AttributeError, TypeError) as e:
        logger.debug("Error checking rest location", room_id=room_id, error=str(e))

    return False


async def _disconnect_player_intentionally(
    player_id: uuid.UUID,
    connection_manager: Any,
    _persistence: Any,  # Unused but kept for API consistency
) -> None:
    """
    Disconnect a player intentionally (via /rest command).

    This marks the disconnect as intentional so no grace period is applied.

    Args:
        player_id: The player's ID
        connection_manager: ConnectionManager instance
        _persistence: Persistence layer (unused, kept for API consistency)
    """
    logger.info("Disconnecting player intentionally via /rest", player_id=player_id)

    # Mark as intentional disconnect (no grace period)
    connection_manager.intentional_disconnects.add(player_id)

    # Disconnect all connections
    try:
        await connection_manager.force_disconnect_player(player_id)
    except (AttributeError, RuntimeError, ValueError, TypeError) as e:
        logger.error("Error disconnecting player", player_id=player_id, error=str(e), exc_info=True)
    finally:
        # Remove from intentional disconnects set after a delay to ensure cleanup
        # This is handled in track_player_disconnected_impl, but we clean up here too
        connection_manager.intentional_disconnects.discard(player_id)


async def _start_rest_countdown(
    player_id: uuid.UUID,
    player_name: str,
    connection_manager: Any,
    persistence: Any,
) -> None:
    """
    Start the 10-second rest countdown.

    Args:
        player_id: The player's ID
        player_name: The player's name
        connection_manager: ConnectionManager instance
        persistence: Persistence layer
    """
    logger.info(
        "Starting rest countdown", player_id=player_id, player_name=player_name, duration=REST_COUNTDOWN_DURATION
    )

    # Create and store the task
    task = create_rest_countdown_task(
        player_id, player_name, connection_manager, persistence, _disconnect_player_intentionally
    )
    connection_manager.resting_players[player_id] = task


async def _cancel_rest_countdown(player_id: uuid.UUID, connection_manager: Any) -> None:
    """
    Cancel the rest countdown for a player.

    Args:
        player_id: The player's ID
        connection_manager: ConnectionManager instance
    """
    if player_id not in connection_manager.resting_players:
        return

    logger.info("Cancelling rest countdown", player_id=player_id)

    task = connection_manager.resting_players[player_id]
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        pass
    except (AttributeError, RuntimeError, ValueError, TypeError) as e:
        logger.error("Error cancelling rest countdown task", player_id=player_id, error=str(e), exc_info=True)
    finally:
        if player_id in connection_manager.resting_players:
            del connection_manager.resting_players[player_id]


def is_player_resting(player_id: uuid.UUID, connection_manager: Any) -> bool:
    """
    Check if a player is currently resting (in /rest countdown).

    Args:
        player_id: The player's ID
        connection_manager: ConnectionManager instance

    Returns:
        True if player is resting, False otherwise
    """
    if not hasattr(connection_manager, "resting_players"):
        return False

    return player_id in connection_manager.resting_players


async def _get_services_from_app(app: Any) -> tuple[Any, Any]:
    """
    Get persistence and connection_manager services from app state.

    Args:
        app: FastAPI app instance

    Returns:
        Tuple of (persistence, connection_manager) or (None, None) if unavailable
    """
    if not app:
        return None, None

    # Prefer container, fallback to app.state for backward compatibility
    persistence = None
    if hasattr(app.state, "container") and app.state.container:
        persistence = app.state.container.async_persistence
    else:
        persistence = getattr(app.state, "persistence", None)

    # Prefer container, fallback to app.state for backward compatibility
    connection_manager = None
    if hasattr(app.state, "container") and app.state.container:
        connection_manager = app.state.container.connection_manager
    else:
        connection_manager = getattr(app.state, "connection_manager", None)

    return persistence, connection_manager


async def handle_rest_command(
    command_data: dict,
    _current_user: dict,  # Unused: player_name parameter is used instead
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, Any]:
    """
    Handle /rest command for clean disconnection.

    Usage: /rest

    Behavior:
    - If in combat: Command is blocked
    - If in rest location (inn/hotel/motel) and not in combat: Instant disconnect
    - Otherwise: Sets position to sitting, starts 10-second countdown
    - Countdown can be interrupted by: combat, movement, spellcasting
    - Countdown does NOT interrupt on: chat, look, inventory management
    - On completion: Clean disconnect (no grace period)

    Args:
        command_data: Command data dictionary
        _current_user: Current user information (unused, player_name is used instead)
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name

    Returns:
        dict: Command result
    """
    logger.debug("Handling rest command", player_name=player_name, command_data=command_data)

    # Get services from app state
    app = request.app if request else None
    if not app:
        return {"result": "System error: application not available."}

    persistence, connection_manager = await _get_services_from_app(app)

    if not persistence:
        return {"result": "System error: persistence layer not available."}

    if not connection_manager:
        return {"result": "System error: connection manager not available."}

    # Get player using player_name parameter (preferred over extracting from current_user)
    player = await persistence.get_player_by_name(player_name)
    if not player:
        return {"result": "You are not recognized by the cosmic forces."}

    player_id = uuid.UUID(player.player_id) if isinstance(player.player_id, str) else player.player_id

    # Check if player is already resting
    if is_player_resting(player_id, connection_manager):
        return {"result": "You are already resting. The countdown will complete shortly."}

    # Check if player is in combat - block command entirely
    in_combat = await _check_player_in_combat(player_id, app)
    if in_combat:
        return {"result": "You cannot rest during combat. End combat first."}

    # Get room information
    room_id = getattr(player, "current_room_id", None)

    # Check if in rest location (inn/hotel/motel)
    is_rest_location = await _check_rest_location(room_id, persistence)

    if is_rest_location:
        # Instant disconnect in rest location (when not in combat)
        logger.info("Player resting in rest location, instant disconnect", player_id=player_id, player_name=player_name)
        await _disconnect_player_intentionally(player_id, connection_manager, persistence)
        return {"result": "You rest peacefully and disconnect from the game."}

    # Not in rest location - start countdown
    # First, set player to sitting position
    position_service = PlayerPositionService(persistence, connection_manager, alias_storage)
    position_result = await position_service.change_position(player_name, "sitting")

    # If position change failed, check if player is already in the desired position
    # For /rest command, being already sitting should still allow rest to proceed
    if not position_result.get("success"):
        # Check if the player is already in the desired sitting position
        if position_result.get("position") == "sitting":
            # Player is already sitting, which is fine for /rest - proceed with rest countdown
            pass  # Continue to rest countdown below
        else:
            # Actual position change failure (not just already in position)
            return {"result": position_result.get("message", "Failed to assume resting position.")}

    # Start rest countdown
    await _start_rest_countdown(player_id, player_name, connection_manager, persistence)

    # Include player_update in response to update Character Info panel
    player_update = {
        "position": position_result.get("position", "sitting"),
        "previous_position": position_result.get("previous_position"),
    }

    return {
        "result": f"You settle into a seated position and begin to rest. You will disconnect in {int(REST_COUNTDOWN_DURATION)} seconds. Any movement, combat, or spellcasting will interrupt your rest.",
        "player_update": player_update,
    }
