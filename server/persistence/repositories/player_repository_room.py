"""
Player room validation helpers for PlayerRepository.

Validates and fixes invalid player room assignments against the room cache.
"""

from typing import Any

from sqlalchemy import text

from server.models.player import Player


def should_skip_room_validation(room_cache: dict[str, Any], player: Player) -> bool:
    """Return True if room validation should be skipped (cache empty, instanced, or tutorial bedroom)."""
    if not room_cache:
        return True
    if player.current_room_id and player.current_room_id.startswith("instance_"):
        return True
    if player.current_room_id == "earth_arkhamcity_sanitarium_room_tutorial_bedroom_001" and getattr(
        player, "tutorial_instance_id", None
    ):
        return True
    return False


def validate_and_fix_player_room(room_cache: dict[str, Any], player: Player, logger: Any) -> bool:
    """
    Validate player's current room and fix if invalid.

    Args:
        room_cache: Shared room cache for validation
        player: Player to validate
        logger: Logger for debug/info messages

    Returns:
        bool: True if room was fixed, False if valid
    """
    if should_skip_room_validation(room_cache, player):
        return False
    if player.current_room_id not in room_cache:
        fallback_room_id = "earth_arkhamcity_sanitarium_room_foyer_001"
        if fallback_room_id not in room_cache:
            logger.debug(
                "Player in invalid room and fallback room not in cache, skipping fix",
                player_id=player.player_id,
                player_name=player.name,
                invalid_room_id=player.current_room_id,
                fallback_room_id=fallback_room_id,
            )
            return False
        if player.current_room_id == fallback_room_id:
            return False
        logger.info(
            "Player in invalid room, moving to Main Foyer",
            player_id=player.player_id,
            player_name=player.name,
            invalid_room_id=player.current_room_id,
            fallback_room_id=fallback_room_id,
        )
        player.current_room_id = fallback_room_id
        return True
    return False


async def validate_and_fix_player_room_with_persistence(
    room_cache: dict[str, Any], player: Player, session: Any, logger: Any
) -> bool:
    """
    Validate and fix player room, persisting the fix if needed.

    Args:
        room_cache: Shared room cache for validation
        player: Player to validate
        session: SQLAlchemy session for persisting fixes
        logger: Logger for debug messages

    Returns:
        bool: True if room was fixed and persisted, False if valid or not fixed
    """
    room_fixed = validate_and_fix_player_room(room_cache, player, logger)
    if room_fixed:
        await session.execute(
            text("SELECT update_player_current_room(:id, :room_id)"),
            {"id": str(player.player_id), "room_id": player.current_room_id},
        )
        await session.commit()
        logger.debug(
            "Fixed and persisted invalid room for player",
            player_id=player.player_id,
            player_name=player.name,
            new_room_id=player.current_room_id,
        )
    return room_fixed
