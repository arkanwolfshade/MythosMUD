"""
Movement validation helpers for MovementService.

Cohesive validation and room-membership checks extracted to keep
movement_service.py under file NLOC limits.
"""

from __future__ import annotations

import uuid
from collections.abc import Awaitable, Callable
from typing import TYPE_CHECKING, Any, NamedTuple, cast

from sqlalchemy.exc import SQLAlchemyError

from ..exceptions import DatabaseError
from ..models.room import Room
from ..structured_logging.enhanced_logging_config import get_logger
from .quest.collect_inventory import collect_player_stacks, count_prototype_in_stacks

if TYPE_CHECKING:
    from ..async_persistence import AsyncPersistenceLayer
    from ..models.player import Player
    from ..services.player_combat_service import PlayerCombatService

_logger = get_logger(__name__)  # the helpers below that take a `logger` parameter log through it

# Shown when a gated exit names no refusal text of its own.
DEFAULT_EXIT_REFUSAL = "Something bars the way."

# Answers "has this player completed the quest activity <target>?" (see ExitRequirement.quest_activity).
QuestActivityReader = Callable[[uuid.UUID, str], Awaitable[bool]]

_quest_activity_reader: QuestActivityReader | None = None  # pylint: disable=invalid-name  # Reason: process-wide hook wired once at startup


def set_quest_activity_reader(reader: QuestActivityReader | None) -> None:
    """Wire how exits learn a player's quest progress (startup; tests)."""
    global _quest_activity_reader  # pylint: disable=global-statement  # Reason: process-wide hook wired once at startup
    _quest_activity_reader = reader


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


class ExitRequirement(NamedTuple):
    """What a gated exit asks of the player; every condition it names must hold."""

    item: str | None  # a prototype id the player must hold
    quest_activity: str | None  # a complete_activity target the player must have completed (any quest, any state)
    refusal: str


def _text(value: object) -> str | None:
    return value if isinstance(value, str) and value else None


def _exit_requirement(room: Room, direction: str) -> ExitRequirement | None:
    """The requirement on a gated exit; None if it is open or its data is malformed.

    Rooms declare ``attributes["exit_requirements"] = {"down": {"item": "<prototype id>", "refusal": "<text>"}}``,
    and/or ``"quest_activity": "<complete_activity target>"`` for an exit a quest unlocks (e.g. ``cmd_look`` or
    ``dialogue_complete_lamplighter``). Anything that is not that shape is ignored: bad world data must not trap a
    player behind an exit.
    """
    raw = cast(object, room.attributes.get("exit_requirements"))
    if not isinstance(raw, dict):
        return None
    entry = cast(dict[str, object], raw).get(direction)
    if not isinstance(entry, dict):
        return None
    spec = cast(dict[str, object], entry)
    item, activity = _text(spec.get("item")), _text(spec.get("quest_activity"))
    if item is None and activity is None:
        return None
    return ExitRequirement(item, activity, _text(spec.get("refusal")) or DEFAULT_EXIT_REFUSAL)


async def _quest_activity_done(player: Player, target: str) -> bool:
    """Whether the player has completed the activity; open (with a warning) when progress cannot be read."""
    if _quest_activity_reader is None:
        _logger.warning("Exit needs quest progress but no reader is wired; leaving it open", target=target)
        return True
    try:
        player_id = uuid.UUID(str(player.player_id))
    except ValueError:
        return True
    return await _quest_activity_reader(player_id, target)


async def exit_refusal(player: Player, room: Room, direction: str) -> str | None:
    """Why the player may not leave ``room`` by ``direction`` (the refusal text), or None if they may.

    An exit is gated when the room's exit_requirements name an item and/or a quest activity for that direction.
    The item counts wherever the player holds it: inventory, equipped, or inside a carried container.
    """
    requirement = _exit_requirement(room, direction)
    if requirement is None:
        return None
    if requirement.item and not count_prototype_in_stacks(collect_player_stacks(player), requirement.item):
        return requirement.refusal
    if requirement.quest_activity and not await _quest_activity_done(player, requirement.quest_activity):
        return requirement.refusal
    return None


async def room_exit_refusal(player: Player, room: Room, to_room_id: str) -> str | None:
    """Why the player may not move from ``room`` to ``to_room_id``, or None if they may.

    Used where only the destination is known (flee, follow). Several exits can lead to the same room;
    the move is allowed if any one of them is open to the player.
    """
    exits = cast(dict[str, str], room.exits)
    refusals = [await exit_refusal(player, room, d) for d, target in exits.items() if target == to_room_id]
    if not refusals or None in refusals:
        return None
    return refusals[0]
