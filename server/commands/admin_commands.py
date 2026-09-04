"""
Administrative commands for MythosMUD.

This module contains the main admin command router and status/time subcommands.
Other admin commands have been extracted to separate modules for better organization:
- admin_permission_utils.py: Permission validation utilities
- admin_teleport_utils.py: Teleport utility functions
- admin_mute_commands.py: Mute/unmute command handlers
- admin_teleport_commands.py: Teleport/goto command handlers
"""

# pylint: disable=too-many-locals  # Reason: Command handlers require many intermediate variables for complex game logic

from typing import Any

from sqlalchemy.exc import SQLAlchemyError

from ..alias_storage import AliasStorage
from ..exceptions import DatabaseError
from ..structured_logging.admin_actions_logger import get_admin_actions_logger
from ..structured_logging.enhanced_logging_config import get_logger
from ..time.time_service import get_mythos_chronicle
from .admin_mute_commands import (
    handle_add_admin_command,
    handle_mute_command,
    handle_mute_global_command,
    handle_mutes_command,
    handle_unmute_command,
    handle_unmute_global_command,
)
from .admin_setlucidity_command import _handle_admin_set_lucidity_command
from .admin_setstat_command import _handle_admin_set_stat_command
from .admin_teleport_commands import DIRECTION_OPPOSITES, handle_goto_command, handle_teleport_command
from .admin_teleport_utils import create_teleport_effect_message

logger = get_logger(__name__)

# Re-export for backward compatibility (tests import these)
__all__ = [
    "handle_admin_command",
    "handle_add_admin_command",
    "handle_mute_command",
    "handle_unmute_command",
    "handle_mute_global_command",
    "handle_unmute_global_command",
    "handle_mutes_command",
    "handle_teleport_command",
    "handle_goto_command",
    "DIRECTION_OPPOSITES",
    "create_teleport_effect_message",
]


# --- Admin Command Routing ---


async def handle_admin_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """
    Entry point for general admin commands that expose subcommands like `admin status`.
    """
    subcommand = (command_data.get("subcommand") or "").lower()

    if subcommand == "status":
        return await _handle_admin_status_command(command_data, current_user, request, alias_storage, player_name)
    if subcommand == "time":
        return await _handle_admin_time_command(command_data, current_user, request, alias_storage, player_name)
    if subcommand in ("setlucidity", "lcd"):
        return await _handle_admin_set_lucidity_command(command_data, current_user, request, alias_storage, player_name)
    if subcommand == "set":
        return await _handle_admin_set_stat_command(command_data, current_user, request, alias_storage, player_name)

    logger.warning("Unknown admin subcommand requested", player_name=player_name, subcommand=subcommand)
    return {"result": f"Unknown admin subcommand '{subcommand}'."}


async def _handle_admin_status_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """
    Provide contextual status information about the caller's administrative privileges.
    """
    _ = alias_storage  # Intentionally unused - part of standard command handler interface
    _ = command_data  # Intentionally unused - status command takes no arguments
    _ = current_user  # Intentionally unused - status command doesn't need user object

    app = request.app if request else None
    if not app:
        logger.warning("Admin status command failed - no application context", player_name=player_name)
        return {"result": "Admin status information is not available."}

    player_service = getattr(app.state, "player_service", None)
    user_manager = getattr(app.state, "user_manager", None)

    if not player_service:
        logger.warning("Admin status command failed - no player service", player_name=player_name)
        return {"result": "Admin status information is not available."}

    try:
        player_record = await player_service.resolve_player_name(player_name)
    except (DatabaseError, SQLAlchemyError) as exc:
        logger.error(
            "Admin status command failed while resolving player name",
            player_name=player_name,
            error=str(exc),
            error_type=type(exc).__name__,
        )
        return {"result": f"Unable to resolve player '{player_name}': {str(exc)}"}

    if not player_record:
        logger.warning("Admin status command failed - player record not found", player_name=player_name)
        return {"result": f"Player '{player_name}' not found."}

    # Determine identifiers for downstream checks
    player_identifier = getattr(player_record, "id", None)
    if player_identifier is None:
        player_identifier = getattr(player_record, "player_id", None)

    is_admin_database = bool(getattr(player_record, "is_admin", False))
    is_admin_runtime: bool | None = None

    if user_manager and player_identifier is not None:
        try:
            is_admin_runtime = user_manager.is_admin(player_identifier)
        except (ValueError, TypeError, AttributeError, OSError) as exc:
            logger.error(
                "Admin status cache lookup failed",
                player_name=player_name,
                # Structlog handles UUID objects automatically, no need to convert to string
                player_identifier=player_identifier,
                error=str(exc),
                error_type=type(exc).__name__,
            )
            is_admin_runtime = None

    is_admin_effective = bool(is_admin_database or (is_admin_runtime is True))

    header = f"ADMIN STATUS FOR {player_record.name.upper()}"
    privilege_line = f"Admin privileges: {'Active' if is_admin_effective else 'Inactive'}"
    database_line = f"- Database record: {'Active' if is_admin_database else 'Inactive'}"
    runtime_line = (
        f"- Session cache: {'Active' if is_admin_runtime else 'Inactive'}"
        if is_admin_runtime is not None
        else "- Session cache: Unavailable"
    )

    if is_admin_effective:
        guidance_lines = [
            "You currently have access to administrative utilities such as teleportation, moderation, and system management commands.",
            "Remember to log critical actions using the appropriate audit-approved procedures.",
        ]
    else:
        guidance_lines = [
            "You do not currently have administrative privileges.",
            "If you believe this is an error, contact a senior archivist for review.",
        ]

    message_lines = [header, "", privilege_line, database_line, runtime_line, ""]
    message_lines.extend(guidance_lines)
    result_text = "\n".join(message_lines)

    try:
        admin_logger = get_admin_actions_logger()
        admin_logger.log_admin_command(
            admin_name=player_name,
            command="admin status",
            success=True,
            additional_data={
                "is_admin_effective": is_admin_effective,
                "is_admin_database": is_admin_database,
                "is_admin_runtime": is_admin_runtime,
            },
        )
    except (OSError, AttributeError, TypeError) as exc:
        logger.warning(
            "Failed to log admin status command",
            player_name=player_name,
            error=str(exc),
            error_type=type(exc).__name__,
        )

    return {"result": result_text}


async def _handle_admin_time_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Expose current Mythos time metadata, active holidays, and freeze diagnostics."""
    _ = alias_storage  # Intentionally unused - part of standard command handler interface
    _ = command_data  # Intentionally unused - time command takes no arguments
    _ = current_user  # Intentionally unused - time command doesn't need user object
    _ = player_name  # Intentionally unused - time command doesn't need player name

    app = request.app if request else None
    chronicle = get_mythos_chronicle()
    mythos_dt = chronicle.get_current_mythos_datetime()
    components = chronicle.get_calendar_components(mythos_dt)

    holiday_service = getattr(app.state, "holiday_service", None) if app and hasattr(app, "state") else None
    active_holidays: list[str] = []
    upcoming: list[str] = []
    if holiday_service:
        try:
            holiday_service.refresh_active(mythos_dt)
            active_holidays = holiday_service.get_active_holiday_names()
            upcoming = holiday_service.get_upcoming_summary()
        except (AttributeError, TypeError, ValueError, KeyError) as exc:
            logger.warning("Admin time command failed to refresh holiday state", error=str(exc))

    last_freeze = chronicle.get_last_freeze_state()
    if last_freeze:
        freeze_line = (
            f"Last freeze: {last_freeze.real_timestamp.isoformat()} (Mythos {last_freeze.mythos_timestamp.isoformat()})"
        )
    else:
        freeze_line = "Last freeze: no recorded freeze events"

    active_text = ", ".join(active_holidays) if active_holidays else "None active"
    upcoming_lines = upcoming or ["No upcoming holidays recorded"]

    lines = [
        "MYTHOS TEMPORAL STATUS",
        "",
        f"Current Mythos time: {mythos_dt.strftime('%Y-%m-%d %H:%M')} ({components.daypart}, {components.season})",
        f"Week {components.week_of_month} of {components.month_name}, day {components.day_of_week + 1} ({components.day_name})",
        f"Active holidays: {active_text}",
        "Next triggers:",
    ]
    lines.extend([f"- {entry}" for entry in upcoming_lines])
    lines.append(freeze_line)

    return {"result": "\n".join(lines)}
