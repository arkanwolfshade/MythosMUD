"""
Player management API endpoints for MythosMUD server.

This module handles all player-related API operations including
creation, retrieval, listing, and deletion of player characters.
"""

from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel

from ..auth.users import get_current_user
from ..error_types import ErrorMessages
from ..exceptions import RateLimitError
from ..game.player_service import PlayerService
from ..game.stats_generator import StatsGenerator
from ..logging_config import get_logger
from ..models import Stats
from ..models.user import User
from ..schemas.player import PlayerRead
from ..utils.rate_limiter import character_creation_limiter, stats_roll_limiter


class CreateCharacterRequest(BaseModel):
    """Request model for character creation."""

    name: str
    stats: dict
    starting_room_id: str = "earth_arkham_city_northside_intersection_derby_high"


logger = get_logger(__name__)

# Create player router
player_router = APIRouter(prefix="/players", tags=["players"])


@player_router.post("/", response_model=PlayerRead)
def create_player(
    name: str,
    starting_room_id: str = "earth_arkham_city_northside_intersection_derby_high",
    current_user: User = Depends(get_current_user),
    request: Request = None,
):
    """Create a new player character."""
    persistence = request.app.state.persistence
    player_service = PlayerService(persistence)

    try:
        return player_service.create_player(name, starting_room_id)
    except ValueError:
        raise HTTPException(status_code=400, detail=ErrorMessages.INVALID_INPUT) from None


@player_router.get("/", response_model=list[PlayerRead])
def list_players(
    current_user: User = Depends(get_current_user),
    request: Request = None,
):
    """Get a list of all players."""
    persistence = request.app.state.persistence
    player_service = PlayerService(persistence)
    return player_service.list_players()


@player_router.get("/{player_id}", response_model=PlayerRead)
def get_player(
    player_id: str,
    current_user: User = Depends(get_current_user),
    request: Request = None,
):
    """Get a specific player by ID."""
    persistence = request.app.state.persistence
    player_service = PlayerService(persistence)

    player = player_service.get_player_by_id(player_id)
    if not player:
        raise HTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND)

    return player


@player_router.get("/name/{player_name}", response_model=PlayerRead)
def get_player_by_name(
    player_name: str,
    current_user: User = Depends(get_current_user),
    request: Request = None,
):
    """Get a specific player by name."""
    persistence = request.app.state.persistence
    player_service = PlayerService(persistence)

    player = player_service.get_player_by_name(player_name)
    if not player:
        raise HTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND)

    return player


@player_router.delete("/{player_id}")
def delete_player(
    player_id: str,
    current_user: User = Depends(get_current_user),
    request: Request = None,
):
    """Delete a player character."""
    persistence = request.app.state.persistence
    player_service = PlayerService(persistence)

    success, message = player_service.delete_player(player_id)
    if not success:
        raise HTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND)

    return {"message": message}


# Player stats and effects endpoints
@player_router.post("/{player_id}/sanity-loss")
def apply_sanity_loss(
    player_id: str,
    amount: int,
    source: str = "unknown",
    current_user: User = Depends(get_current_user),
    request: Request = None,
):
    """Apply sanity loss to a player."""
    persistence = request.app.state.persistence
    player = persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND)

    persistence.apply_sanity_loss(player, amount, source)
    return {"message": f"Applied {amount} sanity loss to {player.name}"}


@player_router.post("/{player_id}/fear")
def apply_fear(
    player_id: str,
    amount: int,
    source: str = "unknown",
    current_user: User = Depends(get_current_user),
    request: Request = None,
):
    """Apply fear to a player."""
    persistence = request.app.state.persistence
    player = persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND)

    persistence.apply_fear(player, amount, source)
    return {"message": f"Applied {amount} fear to {player.name}"}


@player_router.post("/{player_id}/corruption")
def apply_corruption(
    player_id: str,
    amount: int,
    source: str = "unknown",
    current_user: User = Depends(get_current_user),
    request: Request = None,
):
    """Apply corruption to a player."""
    persistence = request.app.state.persistence
    player = persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND)

    persistence.apply_corruption(player, amount, source)
    return {"message": f"Applied {amount} corruption to {player.name}"}


@player_router.post("/{player_id}/occult-knowledge")
def gain_occult_knowledge(
    player_id: str,
    amount: int,
    source: str = "unknown",
    current_user: User = Depends(get_current_user),
    request: Request = None,
):
    """Gain occult knowledge (with sanity loss)."""
    persistence = request.app.state.persistence
    player = persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND)

    persistence.gain_occult_knowledge(player, amount, source)
    return {"message": f"Gained {amount} occult knowledge for {player.name}"}


@player_router.post("/{player_id}/heal")
def heal_player(
    player_id: str,
    amount: int,
    current_user: User = Depends(get_current_user),
    request: Request = None,
):
    """Heal a player's health."""
    persistence = request.app.state.persistence
    player = persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND)

    persistence.heal_player(player, amount)
    return {"message": f"Healed {player.name} for {amount} health"}


@player_router.post("/{player_id}/damage")
def damage_player(
    player_id: str,
    amount: int,
    damage_type: str = "physical",
    current_user: User = Depends(get_current_user),
    request: Request = None,
):
    """Damage a player's health."""
    persistence = request.app.state.persistence
    player = persistence.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND)

    persistence.damage_player(player, amount, damage_type)
    return {"message": f"Damaged {player.name} for {amount} {damage_type} damage"}


# Character Creation and Stats Generation Endpoints
@player_router.post("/roll-stats")
def roll_character_stats(
    method: str = "3d6",
    required_class: str | None = None,
    max_attempts: int = 10,
    current_user: User = Depends(get_current_user),
):
    """
    Roll random stats for character creation.

    This endpoint generates random character statistics using the specified method
    and validates them against class prerequisites if a required class is specified.

    Rate limited to 10 requests per minute per user.
    """
    # Check if user is authenticated
    logger.debug(f"Authentication check - current_user: {current_user}")
    if not current_user:
        logger.warning("Authentication failed: No user returned from get_current_user")
        raise HTTPException(status_code=401, detail="Authentication required")

    logger.info(f"Authentication successful for user: {current_user.username} (ID: {current_user.id})")

    # Apply rate limiting
    try:
        stats_roll_limiter.enforce_rate_limit(str(current_user.id))
    except RateLimitError as e:
        raise HTTPException(
            status_code=429,
            detail={
                "message": str(e),
                "retry_after": e.retry_after,
                "rate_limit_info": stats_roll_limiter.get_rate_limit_info(current_user.id),
            },
        ) from e

    stats_generator = StatsGenerator()

    try:
        stats, available_classes = stats_generator.roll_stats_with_validation(
            method=method, required_class=required_class, max_attempts=max_attempts
        )

        stat_summary = stats_generator.get_stat_summary(stats)

        return {
            "stats": stats.model_dump(),
            "stat_summary": stat_summary,
            "available_classes": available_classes,
            "method_used": method,
            "meets_class_requirements": required_class in available_classes if required_class else True,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=ErrorMessages.INTERNAL_ERROR) from e


@player_router.post("/create-character")
async def create_character_with_stats(
    request_data: CreateCharacterRequest,
    current_user: User = Depends(get_current_user),
    request: Request = None,
):
    """
    Create a new character with specific stats.

    This endpoint creates a new player character with the provided stats
    and automatically logs the user in with the new character.

    Rate limited to 5 creations per 5 minutes per user.
    """
    # Check if user is authenticated
    if not current_user:
        raise HTTPException(status_code=401, detail=ErrorMessages.AUTHENTICATION_REQUIRED)

    # Apply rate limiting
    try:
        character_creation_limiter.enforce_rate_limit(str(current_user.id))
    except RateLimitError as e:
        raise HTTPException(
            status_code=429,
            detail={
                "message": str(e),
                "retry_after": e.retry_after,
                "rate_limit_info": character_creation_limiter.get_rate_limit_info(current_user.id),
            },
        ) from e

    persistence = request.app.state.persistence
    player_service = PlayerService(persistence)

    try:
        # Validate that character name matches username
        if request_data.name != current_user.username:
            raise HTTPException(status_code=400, detail=ErrorMessages.INVALID_INPUT)

        # Convert dict to Stats object
        stats_obj = Stats(**request_data.stats)

        # Create player with stats
        player = player_service.create_player_with_stats(
            name=request_data.name,
            stats=stats_obj,
            starting_room_id=request_data.starting_room_id,
            user_id=current_user.id,
        )

        # Note: For now, we'll skip marking the invite as used to avoid complexity
        # TODO: Implement a proper way to track and mark invites as used
        logger.info(f"Character {request_data.name} created successfully for user {current_user.id}")

        return {
            "message": f"Character {request_data.name} created successfully",
            "player": player.model_dump(),
            "stats": stats_obj.model_dump(),
        }
    except HTTPException:
        # Re-raise HTTPExceptions without modification
        raise
    except ValueError as e:
        raise HTTPException(status_code=400, detail=ErrorMessages.INVALID_INPUT) from e
    except Exception as e:
        raise HTTPException(status_code=500, detail=ErrorMessages.INTERNAL_ERROR) from e


@player_router.post("/validate-stats")
def validate_character_stats(
    stats: dict,
    class_name: str | None = None,
    current_user: User = Depends(get_current_user),
):
    """
    Validate character stats against class prerequisites.

    This endpoint checks if the provided stats meet the requirements for a given class.
    """
    stats_generator = StatsGenerator()

    try:
        # Convert dict to Stats object
        stats_obj = Stats(**stats)

        if class_name:
            meets_prerequisites, failed_requirements = stats_generator.validate_class_prerequisites(
                stats_obj, class_name
            )
            available_classes = stats_generator.get_available_classes(stats_obj)

            return {
                "meets_prerequisites": meets_prerequisites,
                "failed_requirements": failed_requirements,
                "available_classes": available_classes,
                "requested_class": class_name,
            }
        else:
            available_classes = stats_generator.get_available_classes(stats_obj)
            stat_summary = stats_generator.get_stat_summary(stats_obj)

            return {"available_classes": available_classes, "stat_summary": stat_summary}
    except Exception as e:
        raise HTTPException(status_code=400, detail=ErrorMessages.INVALID_FORMAT) from e


@player_router.get("/available-classes")
def get_available_classes(
    current_user: User = Depends(get_current_user),
):
    """
    Get information about all available character classes and their prerequisites.
    """
    stats_generator = StatsGenerator()

    class_info = {}
    for class_name, prerequisites in stats_generator.CLASS_PREREQUISITES.items():
        class_info[class_name] = {
            "prerequisites": {attr.value: min_value for attr, min_value in prerequisites.items()},
            "description": get_class_description(class_name),
        }

    return {"classes": class_info, "stat_range": {"min": stats_generator.MIN_STAT, "max": stats_generator.MAX_STAT}}


def get_class_description(class_name: str) -> str:
    """Get a description for a character class."""
    descriptions = {
        "investigator": "A skilled researcher and detective, specializing in uncovering mysteries and gathering information.",
        "occultist": "A scholar of forbidden knowledge, capable of wielding dangerous magic at the cost of sanity.",
        "survivor": "A resilient individual who has learned to endure the horrors of the Mythos through sheer determination.",
        "cultist": "A charismatic leader who can manipulate others and has ties to dark organizations.",
        "academic": "A brilliant researcher and scholar, specializing in historical and scientific knowledge.",
        "detective": "A sharp-witted investigator with exceptional intuition and deductive reasoning skills.",
    }
    return descriptions.get(class_name, "A mysterious character with unknown capabilities.")
