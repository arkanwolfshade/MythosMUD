"""
Admin command to set player lucidity levels for testing.

This module provides the handler for the admin setlucidity command,
allowing administrators to set a target player's LCD (Lucidity Countdown) value.
"""

# pylint: disable=too-many-arguments,too-many-locals,too-many-return-statements  # Reason: Admin commands require many parameters and intermediate variables for complex game logic and multiple return statements for early validation returns

from __future__ import annotations

import uuid
from typing import Any

from sqlalchemy.exc import SQLAlchemyError

from ..alias_storage import AliasStorage
from ..database import get_async_session
from ..exceptions import DatabaseError
from ..services.lucidity_service import LucidityService
from ..structured_logging.admin_actions_logger import get_admin_actions_logger
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def _extract_command_args(command_data: dict) -> tuple[str | None, int | None]:
    """Extract target_player and lcd_value from command_data."""
    target_player = command_data.get("target_player") or command_data.get("target_name")
    lcd_value = command_data.get("lcd_value") or command_data.get("value")
    if lcd_value is None:
        args = command_data.get("args", [])
        if len(args) >= 2:
            target_player = args[0] if not target_player else target_player
            try:
                lcd_value = int(args[1])
            except (ValueError, TypeError):
                lcd_value = None
    return target_player, lcd_value


def _validate_lcd_value(lcd_value: Any, player_name: str) -> tuple[int | None, dict[str, str] | None]:
    """Validate LCD value is integer and in valid range (-100 to 100)."""
    if lcd_value is None:
        return None, {
            "result": "Usage: admin setlucidity <target_player> <lcd_value>\nLCD value must be between -100 and 100."
        }

    try:
        lcd_value_int = int(lcd_value)
    except (ValueError, TypeError):
        logger.warning("Admin setlucidity command with invalid LCD value", player_name=player_name, lcd_value=lcd_value)
        return None, {"result": f"Invalid LCD value '{lcd_value}'. LCD value must be an integer between -100 and 100."}

    if lcd_value_int < -100 or lcd_value_int > 100:
        logger.warning(
            "Admin setlucidity command with LCD value out of range", player_name=player_name, lcd_value=lcd_value_int
        )
        return None, {"result": f"LCD value {lcd_value_int} is out of range. LCD value must be between -100 and 100."}

    return lcd_value_int, None


async def _check_admin_permissions(
    app: Any, player_name: str, player_service: Any
) -> tuple[Any | None, dict[str, str] | None]:
    """Check if current player is admin and return player object."""
    user_manager = getattr(app.state, "user_manager", None)
    if not user_manager:
        logger.warning("Admin setlucidity command failed - no user manager", player_name=player_name)
        return None, {"result": "Admin setlucidity functionality is not available."}

    current_player_obj = await player_service.resolve_player_name(player_name)
    if not current_player_obj:
        return None, {"result": "Current player not found."}

    current_user_id = str(current_player_obj.id)
    if not user_manager.is_admin(current_user_id):
        logger.warning("Admin setlucidity command denied - not admin", player_name=player_name)
        return None, {"result": "You do not have permission to use this command."}

    return current_player_obj, None


async def _get_current_lcd(session: Any, target_player_id: uuid.UUID) -> int:
    """Get current LCD value from database, defaulting to 100 if no record exists."""
    from sqlalchemy import select

    from ..models.lucidity import PlayerLucidity

    stmt = select(PlayerLucidity).where(PlayerLucidity.player_id == target_player_id)
    result = await session.execute(stmt)
    lucidity_record = result.scalar_one_or_none()
    return lucidity_record.current_lcd if lucidity_record else 100


async def _apply_lucidity_change(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Admin command requires many parameters for context and lucidity adjustment
    session: Any,
    lucidity_service: LucidityService,
    target_player_id: uuid.UUID,
    current_lcd: int,
    target_lcd: int,
    player_name: str,
    current_user_id: str,
    target_player: str,
) -> dict[str, str] | None:
    """Apply lucidity adjustment and return result message or None on error."""
    delta = target_lcd - current_lcd

    try:
        adjustment_result = await lucidity_service.apply_lucidity_adjustment(
            player_id=target_player_id,
            delta=delta,
            reason_code="admin_set",
            metadata={
                "admin_name": player_name,
                "admin_id": current_user_id,
                "previous_lcd": current_lcd,
                "target_lcd": target_lcd,
                "command": "admin setlucidity",
            },
        )
        await session.commit()

        # Log admin action
        try:
            admin_logger = get_admin_actions_logger()
            admin_logger.log_admin_command(
                admin_name=player_name,
                command=f"admin setlucidity {target_player} {target_lcd}",
                success=True,
                additional_data={
                    "target_player": target_player,
                    "target_player_id": str(target_player_id),
                    "previous_lcd": current_lcd,
                    "new_lcd": adjustment_result.new_lcd,
                    "previous_tier": adjustment_result.previous_tier,
                    "new_tier": adjustment_result.new_tier,
                },
            )
        except (OSError, AttributeError, TypeError) as log_exc:
            logger.warning("Failed to log admin setlucidity command", player_name=player_name, error=str(log_exc))

        logger.info(
            "Admin setlucidity command successful",
            admin_name=player_name,
            target_player=target_player,
            previous_lcd=current_lcd,
            new_lcd=adjustment_result.new_lcd,
            previous_tier=adjustment_result.previous_tier,
            new_tier=adjustment_result.new_tier,
        )

        return {
            "result": (
                f"Set {target_player}'s LCD from {current_lcd} to {adjustment_result.new_lcd} "
                f"({adjustment_result.previous_tier} -> {adjustment_result.new_tier})."
            )
        }

    except (DatabaseError, SQLAlchemyError, ValueError, TypeError, AttributeError) as adjust_exc:
        await session.rollback()
        logger.error(
            "Admin setlucidity command failed during adjustment",
            player_name=player_name,
            target_player=target_player,
            error=str(adjust_exc),
            error_type=type(adjust_exc).__name__,
        )
        return {"result": f"Error setting lucidity for {target_player}: {str(adjust_exc)}"}


async def _handle_admin_set_lucidity_command(  # pylint: disable=too-many-arguments,too-many-locals  # Reason: Admin command requires many parameters and intermediate variables for complex lucidity logic
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
) -> dict[str, str]:
    """
    Handle the admin setlucidity command to set a player's LCD value.

    Usage: admin setlucidity <target_player> <lcd_value>
    LCD value must be between -100 and 100.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance (unused)
        player_name: Player name for logging

    Returns:
        dict: Command result
    """
    _ = current_user  # Intentionally unused - part of standard command handler interface
    _ = alias_storage  # Intentionally unused - part of standard command handler interface

    logger.debug("Processing admin setlucidity command", player_name=player_name, command_data=command_data)

    app = request.app if request else None
    if not app:
        logger.warning("Admin setlucidity command failed - no application context", player_name=player_name)
        return {"result": "Admin setlucidity functionality is not available."}

    # Extract and validate command arguments
    target_player, lcd_value = _extract_command_args(command_data)

    if not target_player:
        logger.warning(
            "Admin setlucidity command with no target player", player_name=player_name, command_data=command_data
        )
        return {"result": "Usage: admin setlucidity <target_player> <lcd_value>"}

    lcd_value_int, validation_error = _validate_lcd_value(lcd_value, player_name)
    if validation_error or lcd_value_int is None:
        return validation_error or {"result": "LCD value is required."}

    # Get player service from app state
    player_service = getattr(app.state, "player_service", None)
    if not player_service:
        return {"result": "Player service not available."}

    # Check admin permissions
    current_player_obj, permission_error = await _check_admin_permissions(app, player_name, player_service)
    if permission_error or current_player_obj is None:
        return permission_error or {"result": "Current player not found."}

    current_user_id = str(current_player_obj.id)

    # Resolve target player name to Player object
    target_player_obj = await player_service.resolve_player_name(target_player)
    if not target_player_obj:
        return {"result": f"Player '{target_player}' not found."}

    target_player_id = (
        uuid.UUID(target_player_obj.id) if isinstance(target_player_obj.id, str) else target_player_obj.id
    )

    # Get current LCD and apply change
    catatonia_observer = getattr(app.state, "catatonia_registry", None)

    try:
        async for session in get_async_session():
            lucidity_service = LucidityService(session, catatonia_observer=catatonia_observer)
            current_lcd = await _get_current_lcd(session, target_player_id)

            result = await _apply_lucidity_change(
                session,
                lucidity_service,
                target_player_id,
                current_lcd,
                lcd_value_int,
                player_name,
                current_user_id,
                target_player,
            )
            if result:
                return result

        # If async for loop didn't execute (empty generator), return error
        return {"result": "Database session could not be established. Please try again."}

    except (DatabaseError, SQLAlchemyError, ValueError, TypeError, AttributeError, OSError) as e:
        logger.error(
            "Admin setlucidity command error", admin_name=player_name, target_player=target_player, error=str(e)
        )
        try:
            admin_logger = get_admin_actions_logger()
            admin_logger.log_admin_command(
                admin_name=player_name,
                command=f"admin setlucidity {target_player} {lcd_value_int}",
                success=False,
                additional_data={"error": str(e), "error_type": type(e).__name__},
            )
        except (OSError, AttributeError, TypeError):
            pass  # Ignore logging errors if command itself failed
        return {"result": f"Error setting lucidity for {target_player}: {str(e)}"}
