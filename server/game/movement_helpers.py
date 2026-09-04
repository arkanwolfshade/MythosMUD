"""
Movement validation helpers for MovementService.

Cohesive validation and room-membership checks extracted to keep
movement_service.py under file NLOC limits.
"""

from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any

from sqlalchemy.exc import SQLAlchemyError

from ..exceptions import DatabaseError
from ..models.room import Room

if TYPE_CHECKING:
    from ..async_persistence import AsyncPersistenceLayer
    from ..services.player_combat_service import PlayerCombatService


def extract_player_id(logger: Any, player_obj: Any, from_room_id: str, to_room_id: str) -> uuid.UUID | None:
    """Extract and validate player ID from player object."""
    if not player_obj:
        logger.error(
            "POSITION CHECK: Player object missing during validation", from_room=from_room_id, to_room=to_room_id
        )
        return None

    try:
        if not hasattr(player_obj, "player_id") or not player_obj.player_id:
            logger.warning(
                "COMBAT CHECK: Player object missing player_id attribute, allowing movement",
                from_room=from_room_id,
                to_room=to_room_id,
            )
            return None

        return uuid.UUID(player_obj.player_id)
    except (ValueError, AttributeError, TypeError) as e:
        logger.warning(
            "COMBAT CHECK: Failed to extract player_id as UUID, allowing movement",
            from_room=from_room_id,
            to_room=to_room_id,
            error=str(e),
        )
        return None


def check_combat_state(
    logger: Any,
    combat_service: PlayerCombatService | None,
    player_id: uuid.UUID,
    from_room_id: str,
    to_room_id: str,
) -> bool:
    """Check if player is in combat (blocks movement)."""
    if not combat_service:
        logger.warning("COMBAT CHECK: No combat service available, allowing movement by default")
        return True

    try:
        is_in_combat = combat_service.is_player_in_combat_sync(player_id)
        if is_in_combat:
            logger.warning(
                "COMBAT CHECK: BLOCKING MOVEMENT - Player is in combat",
                player_id=player_id,
                from_room=from_room_id,
                to_room=to_room_id,
            )
            return False
        return True
    except (DatabaseError, SQLAlchemyError) as e:
        logger.warning(
            "COMBAT CHECK: Exception during combat check, allowing movement",
            player_id=player_id,
            error=str(e),
            exc_info=True,
        )
        return True


def check_player_posture(
    logger: Any,
    player_obj: Any,
    player_id: uuid.UUID,
    from_room_id: str,
    to_room_id: str,
) -> bool:
    """Check if player posture allows movement (only standing allowed)."""
    posture = "standing"
    if hasattr(player_obj, "get_stats"):
        try:
            stats = player_obj.get_stats() or {}
            if not isinstance(stats, dict):
                stats = {}
            posture_value = stats.get("position", "standing")
            posture = posture_value.lower() if isinstance(posture_value, str) else "standing"
        except (DatabaseError, SQLAlchemyError) as exc:
            logger.warning(
                "POSITION CHECK: Failed to load player stats",
                player_id=player_id,
                error=str(exc),
                from_room=from_room_id,
                to_room=to_room_id,
            )
            posture = "standing"

    if posture not in {"standing"}:
        logger.info(
            "POSITION CHECK: Movement blocked due to posture",
            player_id=player_id,
            posture=posture,
            from_room=from_room_id,
            to_room=to_room_id,
        )
        return False
    return True


async def validate_player_room_membership(
    logger: Any,
    persistence: AsyncPersistenceLayer,
    player_id: uuid.UUID,
    from_room: Room,
    from_room_id: str,
) -> bool:
    """Validate player is in the from_room, auto-adding if database matches."""
    if from_room.has_player(player_id):
        return True

    try:
        db_player = await persistence.get_player_by_id(player_id)
        if db_player and hasattr(db_player, "current_room_id") and db_player.current_room_id:
            if str(db_player.current_room_id) == from_room_id:
                logger.info(
                    "Adding player to room in-memory state (database room matches)",
                    player_id=player_id,
                    room_id=from_room_id,
                )
                from_room.add_player_silently(player_id)
                return True

            logger.error(
                "Player not in expected room",
                player_id=player_id,
                expected_room=from_room_id,
                actual_room=str(db_player.current_room_id),
            )
            return False

        logger.error("Player not found in database", player_id=player_id)
        return False
    except (DatabaseError, SQLAlchemyError) as e:
        logger.warning(
            "Failed to verify player room from database",
            player_id=player_id,
            room_id=from_room_id,
            error=str(e),
        )
        return False


def validate_exit(logger: Any, persistence: AsyncPersistenceLayer, from_room: Room, to_room_id: str) -> bool:
    """Validate that there's a valid exit from the room to the target room."""
    exits = from_room.exits
    if not exits:
        logger.warning("No exits found in room", room_id=from_room.id, room_name=from_room.name)
        return False

    for direction, target_id in exits.items():
        if target_id == to_room_id:
            logger.debug("Valid exit found", direction=direction, room_id=to_room_id)
            return True

    logger.warning(
        "Exit validation failed - room ID mismatch",
        from_room_id=from_room.id,
        from_room_name=from_room.name,
        to_room_id=to_room_id,
        available_exits=exits,
        exit_directions=list(exits.keys()),
        exit_targets=list(exits.values()),
    )

    target_room = persistence.get_room_by_id(to_room_id)
    if not target_room:
        logger.error(
            "Target room not found in persistence",
            to_room_id=to_room_id,
            from_room_id=from_room.id,
        )

    return False
