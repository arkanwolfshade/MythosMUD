"""Unified posture change notifications for GameInfo and room observers."""

from __future__ import annotations

import uuid
from typing import Protocol, cast

from sqlalchemy.exc import SQLAlchemyError

from ..services.position_messages import POSITION_MESSAGES
from ..structured_logging.enhanced_logging_config import get_logger
from .envelope import build_event

logger = get_logger(__name__)


class _PostureConnectionManager(Protocol):  # pylint: disable=too-few-public-methods
    """Connection manager surface for posture fan-out."""

    sequence_counter: int

    async def broadcast_to_room(self, room_id: str, event: object, exclude_player: object = None) -> None:
        """Send event to occupants of room_id."""

    async def send_personal_message(self, player_id: uuid.UUID, event: dict[str, object]) -> object:
        """Send a personal WebSocket event to one player."""


def normalize_posture(value: object | None) -> str:
    """Normalize posture from stats JSON or enum to lowercase string."""
    if value is None:
        return "standing"
    if hasattr(value, "value"):
        return str(getattr(value, "value", value)).lower()
    return str(value).lower()


def format_room_posture_message(player_name: str, previous_position: str | None, new_position: str) -> str:
    """Create a descriptive room message for posture changes."""
    previous = normalize_posture(previous_position) if previous_position else ""
    current = normalize_posture(new_position)

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


def _self_posture_message(position: str) -> str:
    normalized = position.lower()
    entry = POSITION_MESSAGES.get(normalized)
    if entry is not None:
        return entry["success"]
    return "You adjust your posture."


async def _broadcast_room_posture_change(
    connection_manager: _PostureConnectionManager | None,
    player_id: object,
    room_id: object,
    player_display_name: str,
    previous_position: str | None,
    new_position: str,
    room_message: str,
) -> None:
    if connection_manager is None:
        return
    if not hasattr(connection_manager, "broadcast_to_room"):
        return
    if not room_id or not player_id:
        return
    player_id_str = str(player_id)
    room_id_str = str(room_id)
    try:
        event = build_event(
            "player_posture_change",
            {
                "player_id": player_id_str,
                "player_name": player_display_name,
                "previous_position": previous_position,
                "position": new_position,
                "message": room_message,
            },
            room_id=room_id_str,
            player_id=player_id_str,
            connection_manager=connection_manager,
        )
        await connection_manager.broadcast_to_room(room_id_str, event, exclude_player=player_id)
    except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as exc:
        logger.warning(
            "Failed to broadcast posture change",
            player_name=player_display_name,
            player_id=player_id,
            error=str(exc),
        )


async def _send_personal_posture_message(
    connection_manager: _PostureConnectionManager,
    player_id: uuid.UUID,
    self_message: str,
    previous_position: str | None,
    new_position: str,
) -> None:
    update_event = build_event(
        "player_update",
        {
            "posture_message": self_message,
            "previous_position": previous_position,
            "stats": {"position": new_position},
        },
        player_id=str(player_id),
    )
    _ = await connection_manager.send_personal_message(player_id, update_event)


async def emit_posture_change(
    connection_manager: object | None,
    *,
    player_id: uuid.UUID | str,
    display_name: str,
    room_id: str | None,
    previous_position: str | None,
    new_position: str,
    include_self_message: bool = True,
    send_personal_update: bool = True,
) -> str | None:
    """
    Notify room (and optionally self) when posture actually changed.

    Returns the second-person self message when posture changed and include_self_message is True,
    so callers can attach posture_message to an existing personal payload (e.g. player_dp_updated).
    When send_personal_update is True and include_self_message is True, also sends player_update.
    """
    prev_norm = normalize_posture(previous_position)
    new_norm = normalize_posture(new_position)
    if prev_norm == new_norm:
        return None

    player_uuid = player_id if isinstance(player_id, uuid.UUID) else uuid.UUID(str(player_id))
    room_message = format_room_posture_message(display_name, previous_position, new_position)
    cm = cast(_PostureConnectionManager | None, connection_manager)
    await _broadcast_room_posture_change(
        cm,
        player_uuid,
        room_id,
        display_name,
        previous_position,
        new_norm,
        room_message,
    )

    if not include_self_message:
        return None

    self_message = _self_posture_message(new_norm)
    if send_personal_update and cm is not None:
        await _send_personal_posture_message(cm, player_uuid, self_message, previous_position, new_norm)
    return self_message
