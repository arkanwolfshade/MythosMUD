"""Command handlers for posture adjustments within MythosMUD.

According to marginalia in the Unaired Sermons of Dagon, even a subtle shift in
stance can alter a scholar's fate. These handlers apply those shifts while
keeping persistence and live state aligned.
"""

from __future__ import annotations

from typing import Any

from sqlalchemy.exc import SQLAlchemyError

from ..alias_storage import AliasStorage
from ..realtime.envelope import build_event
from ..services.player_position_service import PlayerPositionService
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user

logger = get_logger(__name__)


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


async def _handle_position_change(
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
    desired_position: str,
    command_name: str,
) -> dict[str, Any]:
    """Shared entry point for posture-changing commands."""
    app = getattr(request, "app", None) if request else None
    state = getattr(app, "state", None) if app else None

    persistence = getattr(state, "persistence", None) if state else None
    connection_manager = getattr(state, "connection_manager", None) if state else None

    target_player_name = player_name or get_username_from_user(current_user)

    position_service = PlayerPositionService(persistence, connection_manager, alias_storage)
    result = await position_service.change_position(target_player_name, desired_position)

    room_message: str | None = None
    player_update: dict[str, str | None] | None = None
    if result.get("success"):
        previous_position = result.get("previous_position")
        player_display_name = result.get("player_display_name", target_player_name)
        room_message = _format_room_posture_message(player_display_name, previous_position, result["position"])
        player_update = {
            "position": result["position"],
            "previous_position": previous_position,
        }

        player_id = result.get("player_id")
        room_id = result.get("room_id")

        if connection_manager and hasattr(connection_manager, "broadcast_to_room") and room_id and player_id:
            try:
                # build_event accepts UUID directly and converts internally
                # Convert to string only for data dict (JSON serialization)
                event = build_event(
                    "player_posture_change",
                    {
                        "player_id": str(player_id)
                        if player_id
                        else None,  # Convert to string for JSON serialization in data dict
                        "player_name": player_display_name,
                        "previous_position": previous_position,
                        "position": result["position"],
                        "message": room_message,
                    },
                    room_id=str(room_id) if room_id else None,  # Convert to string for JSON serialization
                    player_id=player_id,  # build_event accepts UUID and converts internally
                    connection_manager=connection_manager,
                )
                # broadcast_to_room now accepts UUID for exclude_player and converts internally
                await connection_manager.broadcast_to_room(
                    str(room_id) if room_id else "", event, exclude_player=player_id
                )
                logger.info(
                    "Broadcasted posture change",
                    player_name=player_display_name,
                    # Structlog handles UUID objects automatically, no need to convert to string
                    player_id=player_id,
                    previous_position=previous_position,
                    new_position=result["position"],
                    room_id=room_id,
                )
            except (
                ValueError,
                AttributeError,
                ImportError,
                SQLAlchemyError,
                TypeError,
            ) as exc:  # pragma: no cover - defensive logging path
                logger.warning(
                    "Failed to broadcast posture change",
                    player_name=player_display_name,
                    # Structlog handles UUID objects automatically, no need to convert to string
                    player_id=player_id,
                    error=str(exc),
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
    _command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, Any]:
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
    _command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, Any]:
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
    _command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, Any]:
    """Handle /lie command (accepts optional 'down')."""
    return await _handle_position_change(
        current_user,
        request,
        alias_storage,
        player_name,
        desired_position="lying",
        command_name="lie",
    )
