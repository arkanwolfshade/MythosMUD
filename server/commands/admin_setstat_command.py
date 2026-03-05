"""
Admin command to set player statistics.

This module provides the handler for the admin set command,
allowing administrators to set any player statistic including attributes,
DP, MP, lucidity, occult, and corruption.
"""

# pylint: disable=too-many-arguments,too-many-locals,too-many-return-statements  # Reason: Admin commands require many parameters and intermediate variables for complex game logic and multiple return statements for early validation returns

from __future__ import annotations

import math
import uuid
from dataclasses import dataclass
from typing import Any

from sqlalchemy.exc import SQLAlchemyError

from ..alias_storage import AliasStorage
from ..exceptions import DatabaseError
from ..realtime.envelope import build_event
from ..structured_logging.admin_actions_logger import get_admin_actions_logger
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


@dataclass(frozen=True)
class _AdminSetStatLogContext:
    """Context for logging an admin set-stat command (reduces parameter count)."""

    stat_name_input: str
    target_player: str
    value_input: str | int | None
    target_player_obj: Any
    stat_key: str
    old_value: Any
    value: int


@dataclass(frozen=True)
class _AdminSetStatApplyContext:
    """Context for applying an admin set-stat change (reduces parameter count)."""

    app: Any
    persistence: Any
    target_player_obj: Any
    stat_name_input: str
    target_player: str
    stat_key: str
    value: int
    value_input: str | int | None
    player_name: str


# Stat name mapping: supports uppercase abbreviations, lowercase abbreviations, and full names
STAT_NAME_MAPPING: dict[str, str] = {
    # Uppercase abbreviations
    "STR": "strength",
    "CON": "constitution",
    "INT": "intelligence",
    "EDU": "education",
    "LUCK": "luck",
    "DEX": "dexterity",
    "SIZ": "size",
    "POW": "power",
    "CHA": "charisma",
    "DP": "current_dp",
    "MP": "magic_points",
    "LCD": "lucidity",
    # Lowercase abbreviations
    "str": "strength",
    "con": "constitution",
    "int": "intelligence",
    "edu": "education",
    "luck": "luck",
    "dex": "dexterity",
    "siz": "size",
    "pow": "power",
    "cha": "charisma",
    "dp": "current_dp",
    "mp": "magic_points",
    "lcd": "lucidity",
    # Full names (case-insensitive matching will handle these)
    "strength": "strength",
    "constitution": "constitution",
    "intelligence": "intelligence",
    "education": "education",
    "dexterity": "dexterity",
    "power": "power",
    "charisma": "charisma",
    "current_dp": "current_dp",
    "magic_points": "magic_points",
    "lucidity": "lucidity",
    "occult": "occult",
    "corruption": "corruption",
    # Case variations
    "Occult": "occult",
    "Corruption": "corruption",
}


def _parse_value_from_args(value_input: str | int | None, args: list[str]) -> str | int | None:
    """Parse value from args[2] when value_input is None and args has at least 3 elements."""
    if value_input is not None or len(args) < 3:
        return value_input
    try:
        return int(args[2])
    except (ValueError, TypeError):
        return args[2]


def _parse_set_stat_args(command_data: dict[str, Any]) -> tuple[str | None, str | None, str | int | None]:
    """Parse stat name, target player, and value from command data."""
    args = command_data.get("args", [])
    stat_name_input = command_data.get("stat_name")
    target_player = command_data.get("target_player") or command_data.get("target_name")
    value_input = command_data.get("value")

    if not stat_name_input and len(args) >= 1:
        stat_name_input = args[0]
    if not target_player and len(args) >= 2:
        target_player = args[1]
    value_input = _parse_value_from_args(value_input, args)

    return stat_name_input, target_player, value_input


def _validate_set_stat_inputs(
    stat_name_input: str | None, target_player: str | None, value_input: str | int | None, player_name: str
) -> tuple[str, int] | dict[str, str]:
    """Validate stat name and value inputs."""
    if not stat_name_input:
        logger.warning("Admin set command with no stat name", player_name=player_name)
        return {"result": "Usage: admin set <stat_name> <target_player> <value>"}

    if not target_player:
        logger.warning("Admin set command with no target player", player_name=player_name)
        return {"result": "Usage: admin set <stat_name> <target_player> <value>"}

    if value_input is None:
        logger.warning("Admin set command with no value", player_name=player_name)
        return {"result": "Usage: admin set <stat_name> <target_player> <value>"}

    stat_name_lower = stat_name_input.lower()
    stat_key = STAT_NAME_MAPPING.get(stat_name_input) or STAT_NAME_MAPPING.get(stat_name_lower)

    if not stat_key:
        logger.warning("Admin set command with invalid stat name", player_name=player_name, stat_name=stat_name_input)
        valid_stats = ", ".join(sorted(set(STAT_NAME_MAPPING.values())))
        return {
            "result": f"Invalid stat name '{stat_name_input}'. Valid stats: {valid_stats}\nUsage: admin set <stat_name> <target_player> <value>"
        }

    try:
        value = int(value_input)
    except (ValueError, TypeError):
        logger.warning("Admin set command with invalid value", player_name=player_name, value=value_input)
        return {"result": f"Invalid value '{value_input}'. Value must be an integer."}

    return stat_key, value


_PRIMARY_STATS = frozenset(
    {"strength", "dexterity", "constitution", "size", "intelligence", "power", "education", "charisma", "luck"}
)
_OCCULT_RANGE_STATS = frozenset({"occult", "corruption", "lucidity"})


def _warning_for_cap_stat(stat_key: str, value: int, stats: dict[str, Any]) -> str:
    """Return warning message if value exceeds DP or MP calculated maximum; else empty string."""
    if stat_key == "current_dp":
        con = stats.get("constitution", 50)
        siz = stats.get("size", 50)
        max_dp = (con + siz) // 5
        if value > max_dp:
            return f" Warning: DP value {value} exceeds calculated maximum {max_dp} (based on CON {con} + SIZ {siz})."
    elif stat_key == "magic_points":
        pow_val = stats.get("power", 50)
        max_mp = math.ceil(pow_val * 0.2)
        if value > max_mp:
            return f" Warning: MP value {value} exceeds calculated maximum {max_mp} (based on POW {pow_val})."
    return ""


def _warning_for_stat_range(stat_key: str, value: int) -> str:
    """Return warning message if value is outside normal range for stat; else empty string."""
    if stat_key in _PRIMARY_STATS:
        if value < 1 or value > 100:
            return f" Warning: {stat_key} value {value} is outside normal range (1-100)."
    elif stat_key in _OCCULT_RANGE_STATS:
        if value < 0 or value > 100:
            return f" Warning: {stat_key} value {value} is outside normal range (0-100)."
    return ""


def _calculate_stat_warnings(stat_key: str, value: int, stats: dict[str, Any]) -> tuple[str, str]:
    """Calculate warnings for stat values that exceed maximums or normal ranges."""
    warning_message = _warning_for_cap_stat(stat_key, value, stats)
    range_warning = _warning_for_stat_range(stat_key, value)
    return warning_message, range_warning


async def _notify_player_stat_change(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Admin command requires many parameters for context and notification
    app: Any,
    target_player_obj: Any,
    stat_name_input: str,
    old_value: Any,
    value: int,
    warning_message: str,
    range_warning: str,
) -> None:
    """Notify target player of stat change and send player update event."""
    try:
        connection_manager = getattr(app.state, "connection_manager", None)
        if not connection_manager:
            return

        target_player_id = (
            target_player_obj.player_id
            if hasattr(target_player_obj, "player_id")
            else getattr(target_player_obj, "id", None)
        )
        if not target_player_id:
            return

        if isinstance(target_player_id, str):
            target_player_id = uuid.UUID(target_player_id)

        notification_message = f"An administrator has set your {stat_name_input} from {old_value} to {value}."
        if warning_message:
            notification_message += warning_message
        if range_warning:
            notification_message += range_warning

        notification_event = build_event(
            "command_response",
            {"result": notification_message},
            player_id=target_player_id,
            connection_manager=connection_manager,
        )
        await connection_manager.send_personal_message(target_player_id, notification_event)

        updated_stats = target_player_obj.get_stats()
        player_update_event = build_event(
            "player_update",
            {"player_id": str(target_player_id), "stats": updated_stats},
            player_id=target_player_id,
            connection_manager=connection_manager,
        )
        await connection_manager.send_personal_message(target_player_id, player_update_event)
    except (AttributeError, TypeError, ValueError, OSError) as notify_exc:
        logger.warning("Failed to notify target player of stat change", error=str(notify_exc))


async def _resolve_admin_services_and_permissions(
    app: Any, player_name: str, target_player: str
) -> tuple[Any, Any] | dict[str, str]:
    """Resolve required services and check admin permissions."""
    user_manager = getattr(app.state, "user_manager", None)
    if not user_manager:
        logger.warning("Admin set command failed - no user manager", player_name=player_name)
        return {"result": "Admin set functionality is not available."}

    player_service = getattr(app.state, "player_service", None)
    if not player_service:
        return {"result": "Player service not available."}

    persistence = getattr(app.state, "persistence", None)
    if not persistence:
        return {"result": "Persistence layer not available."}

    current_player_obj = await player_service.resolve_player_name(player_name)
    if not current_player_obj:
        return {"result": "Current player not found."}

    current_user_id = str(current_player_obj.id)
    if not await user_manager.is_admin(current_user_id):
        logger.debug("Admin set command denied - not admin", player_name=player_name)
        return {"result": "You do not have permission to use this command."}

    target_player_obj = await persistence.get_player_by_name(target_player)
    if not target_player_obj:
        return {"result": f"Player '{target_player}' not found."}

    return persistence, target_player_obj


def _log_admin_set_stat(
    player_name: str,
    ctx: _AdminSetStatLogContext,
    success: bool = True,
    error: str | None = None,
) -> None:
    """Log admin set stat command."""
    try:
        admin_logger = get_admin_actions_logger()
        admin_logger.log_admin_command(
            admin_name=player_name,
            command=f"admin set {ctx.stat_name_input} {ctx.target_player} {ctx.value_input}",
            success=success,
            additional_data={
                "target_player": ctx.target_player,
                "target_player_id": str(ctx.target_player_obj.player_id) if ctx.target_player_obj else None,
                "stat_name": ctx.stat_key,
                "old_value": ctx.old_value,
                "new_value": ctx.value,
                "error": error,
                "error_type": type(error).__name__ if error else None,
            }
            if success
            else {"error": str(error), "error_type": type(error).__name__ if error else None},
        )
    except (OSError, AttributeError, TypeError) as log_exc:
        logger.warning("Failed to log admin set command", player_name=player_name, error=str(log_exc))


def _build_set_stat_error_response(
    player_name: str,
    stat_name_input: str | None,
    target_player: str | None,
    value_input: str | int | None,
    error: BaseException,
) -> dict[str, str]:
    """Log error and admin action failure, return error result dict."""
    stat_s = stat_name_input or "unknown"
    target_s = target_player or "unknown"
    logger.error(
        "Admin set command error",
        admin_name=player_name,
        target_player=target_s,
        stat_name=stat_s,
        error=str(error),
        error_type=type(error).__name__,
    )
    _log_admin_set_stat(
        player_name,
        _AdminSetStatLogContext(stat_s, target_s, value_input, None, "", None, 0),
        success=False,
        error=str(error),
    )
    return {"result": f"Error setting {stat_s} for {target_s}: {str(error)}"}


def _get_app_or_error(request: Any, player_name: str) -> tuple[Any | None, dict[str, str] | None]:
    """Return (app, None) if request has app, else (None, error_dict)."""
    if not request:
        return None, {"result": "Admin set functionality is not available."}
    app = getattr(request, "app", None)
    if not app:
        logger.warning("Admin set command failed - no application context", player_name=player_name)
        return None, {"result": "Admin set functionality is not available."}
    return app, None


async def _apply_stat_change_and_build_result(
    ctx: _AdminSetStatApplyContext,
) -> dict[str, str]:
    """Apply stat change, persist, notify, log; return success result dict."""
    stats = ctx.target_player_obj.get_stats()
    old_value = stats.get(ctx.stat_key)
    warning_message, range_warning = _calculate_stat_warnings(ctx.stat_key, ctx.value, stats)
    stats[ctx.stat_key] = ctx.value
    ctx.target_player_obj.set_stats(stats)
    await ctx.persistence.save_player(ctx.target_player_obj)
    await _notify_player_stat_change(
        ctx.app,
        ctx.target_player_obj,
        ctx.stat_name_input,
        old_value,
        ctx.value,
        warning_message,
        range_warning,
    )
    _log_admin_set_stat(
        ctx.player_name,
        _AdminSetStatLogContext(
            ctx.stat_name_input,
            ctx.target_player,
            ctx.value_input,
            ctx.target_player_obj,
            ctx.stat_key,
            old_value,
            ctx.value,
        ),
    )
    logger.info(
        "Admin set command successful",
        admin_name=ctx.player_name,
        target_player=ctx.target_player,
        stat_name=ctx.stat_key,
        old_value=old_value,
        new_value=ctx.value,
    )
    result_message = f"Set {ctx.target_player}'s {ctx.stat_name_input} from {old_value} to {ctx.value}."
    if warning_message:
        result_message += warning_message
    if range_warning:
        result_message += range_warning
    return {"result": result_message}


async def _handle_admin_set_stat_command(  # pylint: disable=too-many-arguments,too-many-locals  # Reason: Admin command requires many parameters and intermediate variables for complex stat setting logic
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """
    Handle the admin set command to set a player's statistic.

    Usage: admin set <stat_name> <target_player> <value>

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

    logger.debug("Processing admin set command", player_name=player_name, command_data=command_data)

    app, app_error = _get_app_or_error(request, player_name)
    if app_error is not None:
        return app_error

    stat_name_input, target_player, value_input = _parse_set_stat_args(command_data)
    validation_result = _validate_set_stat_inputs(stat_name_input, target_player, value_input, player_name)
    if isinstance(validation_result, dict):
        return validation_result

    stat_key, value = validation_result
    if not stat_name_input or not target_player:
        return {"result": "Target player and stat name are required."}

    service_result = await _resolve_admin_services_and_permissions(app, player_name, target_player)
    if isinstance(service_result, dict):
        return service_result

    persistence, target_player_obj = service_result

    try:
        return await _apply_stat_change_and_build_result(
            _AdminSetStatApplyContext(
                app=app,
                persistence=persistence,
                target_player_obj=target_player_obj,
                stat_name_input=stat_name_input,
                target_player=target_player,
                stat_key=stat_key,
                value=value,
                value_input=value_input,
                player_name=player_name,
            )
        )
    except (DatabaseError, SQLAlchemyError, ValueError, TypeError, AttributeError, OSError) as e:
        return _build_set_stat_error_response(player_name, stat_name_input, target_player, value_input, e)
