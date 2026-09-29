"""
Admin global mute command handlers for MythosMUD (mute_global / unmute_global).

Split out of admin_mute_commands.py to keep that module under the size limit.
"""

from typing import Protocol, cast

from sqlalchemy.exc import SQLAlchemyError

from ..alias_storage import AliasStorage
from ..exceptions import DatabaseError
from ..structured_logging.enhanced_logging_config import get_logger
from .admin_mute_commands import extract_mute_target, mute_duration_display, parse_mute_duration_minutes
from .admin_permission_utils import validate_admin_permission

logger = get_logger(__name__)


class _MutePlayerRef(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """What the global-mute flow reads from a resolved player (PlayerRead)."""

    id: object
    is_admin: bool


class _MutePlayerResolver(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """PlayerService surface used by the global-mute flow."""

    async def resolve_player_name(self, player_name: str) -> _MutePlayerRef | None: ...  # pylint: disable=missing-function-docstring


class _GlobalMuteManager(Protocol):
    """UserManager surface used by the global-mute flow."""

    async def mute_global(  # pylint: disable=missing-function-docstring,too-many-arguments,too-many-positional-arguments  # Reason: mirrors UserManager.mute_global
        self,
        muter_id: str,
        muter_name: str,
        target_id: str,
        target_name: str,
        duration_minutes: int | None = None,
        reason: str = "",
    ) -> bool: ...

    async def unmute_global(  # pylint: disable=missing-function-docstring
        self, unmuter_id: str, unmuter_name: str, target_id: str, target_name: str
    ) -> bool: ...


def _global_mute_services(request: object) -> tuple[_GlobalMuteManager | None, _MutePlayerResolver | None]:
    """UserManager and PlayerService from app.state, typed to what the global-mute flow uses."""
    app = cast(object | None, getattr(request, "app", None))
    state = cast(object | None, getattr(app, "state", None))
    return (
        cast(_GlobalMuteManager | None, getattr(state, "user_manager", None)),
        cast(_MutePlayerResolver | None, getattr(state, "player_service", None)),
    )


async def _resolve_global_mute_players(
    player_service: _MutePlayerResolver | None,
    player_name: str,
    target_player: str,
) -> tuple[_MutePlayerRef, _MutePlayerRef] | dict[str, str]:
    """Resolve the acting admin and the target; an error result if either fails or the actor isn't an admin."""
    if not player_service:
        return {"result": "Player service not available."}
    admin = await player_service.resolve_player_name(player_name)
    if admin is None or not await validate_admin_permission(admin, player_name):
        return {"result": "You do not have permission to use global mutes."}
    target = await player_service.resolve_player_name(target_player)
    if target is None:
        return {"result": f"Player '{target_player}' not found."}
    return admin, target


async def _perform_global_mute(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: mirrors the mute_global command fields
    user_manager: _GlobalMuteManager,
    player_service: _MutePlayerResolver | None,
    player_name: str,
    target_player: str,
    duration: int | None,
    reason: str,
) -> dict[str, str]:
    """Resolve players, check admin, and apply a global mute."""
    resolved = await _resolve_global_mute_players(player_service, player_name, target_player)
    if isinstance(resolved, dict):
        return resolved
    admin, target = resolved
    if await user_manager.mute_global(str(admin.id), player_name, str(target.id), target_player, duration, reason):
        logger.info("Global mute applied", admin_name=player_name, target_player=target_player, duration=duration)
        return {"result": f"You have globally muted {target_player} {mute_duration_display(duration)}."}
    logger.warning("Global mute command failed", admin_name=player_name, target_player=target_player)
    return {"result": f"Failed to globally mute {target_player}."}


async def _perform_global_unmute(
    user_manager: _GlobalMuteManager,
    player_service: _MutePlayerResolver | None,
    player_name: str,
    target_player: str,
) -> dict[str, str]:
    """Resolve players, check admin, and remove a global mute."""
    resolved = await _resolve_global_mute_players(player_service, player_name, target_player)
    if isinstance(resolved, dict):
        return resolved
    admin, target = resolved
    if await user_manager.unmute_global(str(admin.id), player_name, str(target.id), target_player):
        logger.info("Global mute removed", admin_name=player_name, target_player=target_player)
        return {"result": f"You have globally unmuted {target_player}."}
    logger.warning("Global unmute command failed", admin_name=player_name, target_player=target_player)
    return {"result": f"{target_player} is not globally muted."}


async def handle_mute_global_command(
    command_data: dict[str, object],
    current_user: dict[str, object],
    request: object,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """
    Handle the mute_global command for global muting.

    Args:
        command_data: Command data dictionary containing args and other info
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Mute global command result
    """
    _ = current_user  # Intentionally unused - part of standard command handler interface
    _ = alias_storage  # Intentionally unused - part of standard command handler interface
    logger.debug("Processing mute_global command", player_name=player_name)

    user_manager, player_service = _global_mute_services(request)

    if not user_manager:
        logger.warning("Mute global command failed - no user manager", player_name=player_name)
        return {"result": "Global mute functionality is not available."}

    target_player = extract_mute_target(command_data)
    if not target_player:
        return {"result": "Usage: mute_global <player> [duration_in_minutes] [reason]"}

    duration = parse_mute_duration_minutes(command_data.get("duration_minutes"))
    reason = str(command_data.get("reason") or "")

    try:
        return await _perform_global_mute(user_manager, player_service, player_name, target_player, duration, reason)
    except (DatabaseError, SQLAlchemyError, ValueError, TypeError, AttributeError) as e:
        logger.error("Global mute command error", player_name=player_name, error=str(e))
        return {"result": f"Error globally muting {target_player}: {str(e)}"}


async def handle_unmute_global_command(
    command_data: dict[str, object],
    current_user: dict[str, object],
    request: object,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """
    Handle the unmute_global command for removing global mute.

    Args:
        command_data: Command data dictionary containing args and other info
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Unmute global command result
    """
    _ = current_user  # Intentionally unused - part of standard command handler interface
    _ = alias_storage  # Intentionally unused - part of standard command handler interface
    logger.debug("Processing unmute_global command", player_name=player_name)

    user_manager, player_service = _global_mute_services(request)

    if not user_manager:
        logger.warning("Unmute global command failed - no user manager", player_name=player_name)
        return {"result": "Global unmute functionality is not available."}

    target_player = extract_mute_target(command_data)
    if not target_player:
        return {"result": "Usage: unmute_global <player>"}

    try:
        return await _perform_global_unmute(user_manager, player_service, player_name, target_player)
    except (DatabaseError, SQLAlchemyError, ValueError, TypeError, AttributeError) as e:
        logger.error("Global unmute command error", player_name=player_name, error=str(e))
        return {"result": f"Error globally unmuting {target_player}: {str(e)}"}


__all__ = ["handle_mute_global_command", "handle_unmute_global_command"]
