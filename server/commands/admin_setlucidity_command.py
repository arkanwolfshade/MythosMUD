"""
Admin command to set player lucidity levels for testing.

This module provides the handler for the admin setlucidity command,
allowing administrators to set a target player's LCD (Lucidity Countdown) value.
"""

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


async def _handle_admin_set_lucidity_command(
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

    # Extract target player and LCD value from command_data
    # Support both "target_player" and "target_name" for compatibility
    target_player = command_data.get("target_player") or command_data.get("target_name")
    # LCD value might be in "lcd_value", "value", or "args"
    lcd_value = command_data.get("lcd_value") or command_data.get("value")
    if lcd_value is None:
        args = command_data.get("args", [])
        if len(args) >= 2:
            target_player = args[0] if not target_player else target_player
            try:
                lcd_value = int(args[1])
            except (ValueError, TypeError):
                lcd_value = None

    if not target_player:
        logger.warning(
            "Admin setlucidity command with no target player", player_name=player_name, command_data=command_data
        )
        return {"result": "Usage: admin setlucidity <target_player> <lcd_value>"}

    if lcd_value is None:
        logger.warning(
            "Admin setlucidity command with no LCD value", player_name=player_name, command_data=command_data
        )
        return {
            "result": "Usage: admin setlucidity <target_player> <lcd_value>\nLCD value must be between -100 and 100."
        }

    try:
        lcd_value_int = int(lcd_value)
    except (ValueError, TypeError):
        logger.warning("Admin setlucidity command with invalid LCD value", player_name=player_name, lcd_value=lcd_value)
        return {"result": f"Invalid LCD value '{lcd_value}'. LCD value must be an integer between -100 and 100."}

    # Validate LCD range
    if lcd_value_int < -100 or lcd_value_int > 100:
        logger.warning(
            "Admin setlucidity command with LCD value out of range", player_name=player_name, lcd_value=lcd_value_int
        )
        return {"result": f"LCD value {lcd_value_int} is out of range. LCD value must be between -100 and 100."}

    # Check admin permissions
    user_manager = getattr(app.state, "user_manager", None)
    if not user_manager:
        logger.warning("Admin setlucidity command failed - no user manager", player_name=player_name)
        return {"result": "Admin setlucidity functionality is not available."}

    try:
        # Get player service from app state
        player_service = getattr(app.state, "player_service", None)
        if not player_service:
            return {"result": "Player service not available."}

        # Get current player's actual player object and ID
        current_player_obj = await player_service.resolve_player_name(player_name)
        if not current_player_obj:
            return {"result": "Current player not found."}

        # Check if current player is admin
        current_user_id = str(current_player_obj.id)
        if not user_manager.is_admin(current_user_id):
            logger.warning("Admin setlucidity command denied - not admin", player_name=player_name)
            return {"result": "You do not have permission to use this command."}

        # Resolve target player name to Player object
        target_player_obj = await player_service.resolve_player_name(target_player)
        if not target_player_obj:
            return {"result": f"Player '{target_player}' not found."}

        target_player_id = (
            uuid.UUID(target_player_obj.id) if isinstance(target_player_obj.id, str) else target_player_obj.id
        )

        # Get current LCD and calculate delta
        catatonia_observer = getattr(app.state, "catatonia_registry", None)

        async for session in get_async_session():
            lucidity_service = LucidityService(session, catatonia_observer=catatonia_observer)

            # Get current LCD
            from sqlalchemy import select

            from ..models.lucidity import PlayerLucidity

            stmt = select(PlayerLucidity).where(PlayerLucidity.player_id == target_player_id)
            result = await session.execute(stmt)
            lucidity_record = result.scalar_one_or_none()

            current_lcd = lucidity_record.current_lcd if lucidity_record else 100  # Default to 100 if no record exists

            # Calculate delta to reach target LCD
            delta = lcd_value_int - current_lcd

            # Apply lucidity adjustment
            try:
                adjustment_result = await lucidity_service.apply_lucidity_adjustment(
                    player_id=target_player_id,
                    delta=delta,
                    reason_code="admin_set",
                    metadata={
                        "admin_name": player_name,
                        "admin_id": current_user_id,
                        "previous_lcd": current_lcd,
                        "target_lcd": lcd_value_int,
                        "command": "admin setlucidity",
                    },
                )
                await session.commit()

                # Log admin action
                try:
                    admin_logger = get_admin_actions_logger()
                    admin_logger.log_admin_command(
                        admin_name=player_name,
                        command=f"admin setlucidity {target_player} {lcd_value_int}",
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
                    logger.warning(
                        "Failed to log admin setlucidity command", player_name=player_name, error=str(log_exc)
                    )

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
