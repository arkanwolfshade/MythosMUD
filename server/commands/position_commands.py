"""Command handlers for posture adjustments within MythosMUD.

According to marginalia in the Unaired Sermons of Dagon, even a subtle shift in
stance can alter a scholar's fate. These handlers apply those shifts while
keeping persistence and live state aligned.
"""

# pylint: disable=too-many-arguments,too-many-locals  # Reason: Position commands require many parameters and intermediate variables for complex position logic

from __future__ import annotations

from typing import cast

from fastapi import Request

from ..alias_storage import AliasStorage
from ..realtime.posture_notify import emit_posture_change
from ..services.player_position_service import (
    PlayerPositionService,
    SupportsConnectionManager,
    SupportsPlayerPersistence,
)
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user

logger = get_logger(__name__)


def _get_position_command_services(
    request: Request | None,
) -> tuple[SupportsPlayerPersistence | None, SupportsConnectionManager | None]:
    if request is None:
        return None, None
    # Cast: Starlette types app as Any; we only read known state attributes via getattr.
    app = cast(object, request.app)
    state = cast(object | None, getattr(app, "state", None))
    if state is None:
        return None, None
    container = cast(object | None, getattr(state, "container", None))
    if container is not None:
        persistence = getattr(container, "async_persistence", None)
        connection_manager = getattr(container, "connection_manager", None)
        # Cast: container fields are untyped app.state attributes; runtime objects match the Protocols.
        return (
            cast(SupportsPlayerPersistence | None, persistence),
            cast(SupportsConnectionManager | None, connection_manager),
        )
    persistence = getattr(state, "persistence", None)
    connection_manager = getattr(state, "connection_manager", None)
    return (
        cast(SupportsPlayerPersistence | None, persistence),
        cast(SupportsConnectionManager | None, connection_manager),
    )


async def _handle_position_change(
    current_user: dict[str, object],
    request: Request | None,
    alias_storage: AliasStorage | None,
    player_name: str,
    desired_position: str,
    command_name: str,
) -> dict[str, object]:
    """Shared entry point for posture-changing commands."""
    persistence, connection_manager = _get_position_command_services(request)
    target_player_name = player_name or get_username_from_user(current_user)

    position_service = PlayerPositionService(persistence, connection_manager, alias_storage)
    result = await position_service.change_position(target_player_name, desired_position)

    # Always sync posture to client (including "already standing"): UI can show Sitting
    # after cancelled /rest while persistence already has standing.
    previous_position = result.get("previous_position")
    player_update: dict[str, str | None] | None = {
        "position": result["position"],
        "previous_position": previous_position,
    }
    if result.get("success"):
        player_display_name = result.get("player_display_name", target_player_name)
        player_id = result.get("player_id")
        room_id = result.get("room_id")
        # Self line goes via command_response; room via player_posture_change (M1).
        _ = await emit_posture_change(
            connection_manager,
            player_id=str(player_id) if player_id else target_player_name,
            display_name=player_display_name,
            room_id=str(room_id) if room_id else None,
            previous_position=previous_position,
            new_position=result["position"],
            include_self_message=False,
        )

    logger.info(
        "Processed position command",
        player_name=target_player_name,
        command=command_name,
        success=result["success"],
        new_position=result["position"],
    )

    return {
        "result": result["message"],
        "position": result["position"],
        "changed": result["success"],
        "player_update": player_update,
        "game_log_message": result["message"],
        "game_log_channel": "game-log",
        "suppress_chat": True,
    }


async def handle_sit_command(
    _command_data: dict[str, object],
    current_user: dict[str, object],
    request: Request | None,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, object]:
    """Handle /sit command."""
    return await _handle_position_change(
        current_user,
        request,
        alias_storage,
        player_name,
        desired_position="sitting",
        command_name="sit",
    )


async def handle_stand_command(
    _command_data: dict[str, object],
    current_user: dict[str, object],
    request: Request | None,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, object]:
    """Handle /stand command."""
    return await _handle_position_change(
        current_user,
        request,
        alias_storage,
        player_name,
        desired_position="standing",
        command_name="stand",
    )


async def handle_lie_command(
    _command_data: dict[str, object],
    current_user: dict[str, object],
    request: Request | None,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, object]:
    """Handle /lie command (accepts optional 'down')."""
    return await _handle_position_change(
        current_user,
        request,
        alias_storage,
        player_name,
        desired_position="lying",
        command_name="lie",
    )
