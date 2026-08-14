"""Command handlers for posture adjustments within MythosMUD.

According to marginalia in the Unaired Sermons of Dagon, even a subtle shift in
stance can alter a scholar's fate. These handlers apply those shifts while
keeping persistence and live state aligned.
"""

# pylint: disable=too-many-arguments,too-many-locals  # Reason: Position commands require many parameters and intermediate variables for complex position logic

from __future__ import annotations

from typing import Protocol, cast

from fastapi import Request
from sqlalchemy.exc import SQLAlchemyError

from ..alias_storage import AliasStorage
from ..realtime.envelope import build_event
from ..services.player_position_service import (
    PlayerPositionService,
    SupportsConnectionManager,
    SupportsPlayerPersistence,
)
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user

logger = get_logger(__name__)


class _EventSequence(Protocol):
    """Sequence counter surface used by build_event."""

    sequence_counter: int


class _RoomBroadcaster(Protocol):
    """Connection manager surface used to fan out posture events."""

    async def broadcast_to_room(self, room_id: str, event: object, exclude_player: object = None) -> None:
        """Send event to occupants of room_id."""


def _format_room_posture_message(player_name: str, previous_position: str | None, new_position: str) -> str:
    """Create a descriptive room message for posture changes."""
    previous = (previous_position or "").lower()
    current = new_position.lower()

    if current == "sitting":
        return f"{player_name} settles into a seated position."
    if current == "lying":
        return f"{player_name} stretches out and lies prone upon the floor."
    if current == "standing":
        if previous == "lying":
            return f"{player_name} pushes up from the floor and stands once more."
        if previous == "sitting":
            return f"{player_name} rises from their seat, ready to move again."
        return f"{player_name} straightens and stands tall."
    return f"{player_name} shifts their posture uneasily."


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


def _build_posture_change_event(
    connection_manager: SupportsConnectionManager | None,
    player_id: object,
    room_id: object,
    player_display_name: str,
    previous_position: str | None,
    new_position: str,
    room_message: str,
) -> dict[str, object]:
    return build_event(
        "player_posture_change",
        {
            "player_id": str(player_id) if player_id else None,
            "player_name": player_display_name,
            "previous_position": previous_position,
            "position": new_position,
            "message": room_message,
        },
        room_id=str(room_id) if room_id else None,
        player_id=str(player_id) if player_id else None,
        connection_manager=(
            cast(_EventSequence, cast(object, connection_manager)) if connection_manager is not None else None
        ),
    )


async def _broadcast_posture_change(
    connection_manager: SupportsConnectionManager | None,
    player_id: object,
    room_id: object,
    player_display_name: str,
    previous_position: str | None,
    new_position: str,
    room_message: str,
) -> None:
    if connection_manager is None or not hasattr(connection_manager, "broadcast_to_room"):
        return
    if not room_id or not player_id:
        return
    try:
        event = _build_posture_change_event(
            connection_manager,
            player_id,
            room_id,
            player_display_name,
            previous_position,
            new_position,
            room_message,
        )
        broadcaster = cast(_RoomBroadcaster, cast(object, connection_manager))
        await broadcaster.broadcast_to_room(str(room_id) if room_id else "", event, exclude_player=player_id)
        logger.info(
            "Broadcasted posture change",
            player_name=player_display_name,
            player_id=player_id,
            previous_position=previous_position,
            new_position=new_position,
            room_id=room_id,
        )
    except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as exc:
        logger.warning(
            "Failed to broadcast posture change",
            player_name=player_display_name,
            player_id=player_id,
            error=str(exc),
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

    room_message: str | None = None
    # Always sync posture to client (including "already standing"): UI can show Sitting
    # after cancelled /rest while persistence already has standing.
    previous_position = result.get("previous_position")
    player_update: dict[str, str | None] | None = {
        "position": result["position"],
        "previous_position": previous_position,
    }
    if result.get("success"):
        player_display_name = result.get("player_display_name", target_player_name)
        room_message = _format_room_posture_message(player_display_name, previous_position, result["position"])
        await _broadcast_posture_change(
            connection_manager,
            result.get("player_id"),
            result.get("room_id"),
            player_display_name,
            previous_position,
            result["position"],
            room_message,
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
        "room_message": room_message,
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
