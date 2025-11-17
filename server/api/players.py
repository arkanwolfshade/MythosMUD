"""
Player management API endpoints for MythosMUD server.

This module handles all player-related API operations including
creation, retrieval, listing, and deletion of player characters.
"""

from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel

from ..auth.users import get_current_active_user, get_current_user
from ..dependencies import PlayerServiceDep
from ..error_types import ErrorMessages
from ..exceptions import LoggedHTTPException, RateLimitError, ValidationError, create_error_context
from ..game.player_service import PlayerService
from ..game.stats_generator import StatsGenerator
from ..logging.enhanced_logging_config import get_logger
from ..models import Player, Stats
from ..models.user import User
from ..schemas.player import PlayerRead
from ..utils.error_logging import create_context_from_request
from ..utils.rate_limiter import character_creation_limiter, stats_roll_limiter


class CreateCharacterRequest(BaseModel):
    """Request model for character creation."""

    name: str
    stats: dict
    profession_id: int = 0


class RollStatsRequest(BaseModel):
    """Request model for rolling character stats."""

    method: str = "3d6"
    required_class: str | None = None
    timeout_seconds: float = 1.0
    profession_id: int | None = None


logger = get_logger(__name__)

# Create player router
player_router = APIRouter(prefix="/api/players", tags=["players"])


@player_router.post("/", response_model=PlayerRead)
async def create_player(
    name: str,
    request: Request,
    starting_room_id: str = "earth_arkhamcity_sanitarium_room_foyer_001",
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> PlayerRead:
    """Create a new player character."""
    try:
        return await player_service.create_player(name, profession_id=0, starting_room_id=starting_room_id)
    except ValidationError:
        context = create_context_from_request(request)
        if current_user:
            context.user_id = str(current_user.id)
        context.metadata["player_name"] = name
        context.metadata["starting_room_id"] = starting_room_id
        raise LoggedHTTPException(status_code=400, detail=ErrorMessages.INVALID_INPUT, context=context) from None


@player_router.get("/", response_model=list[PlayerRead])
async def list_players(
    request: Request,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> list[PlayerRead]:
    """Get a list of all players."""
    result = await player_service.list_players()
    assert isinstance(result, list)
    return result


@player_router.get("/available-classes")
async def get_available_classes(
    current_user: User = Depends(get_current_user),
) -> dict[str, Any]:
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


@player_router.get("/{player_id}", response_model=PlayerRead)
async def get_player(
    player_id: str,
    request: Request,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> PlayerRead:
    """Get a specific player by ID."""
    player = await player_service.get_player_by_id(player_id)
    if not player:
        context = create_context_from_request(request)
        if current_user:
            context.user_id = str(current_user.id)
        context.metadata["requested_player_id"] = player_id
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context)

    return player


@player_router.get("/name/{player_name}", response_model=PlayerRead)
async def get_player_by_name(
    player_name: str,
    request: Request,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> PlayerRead:
    """Get a specific player by name."""
    player = await player_service.get_player_by_name(player_name)
    if not player:
        context = create_context_from_request(request)
        if current_user:
            context.user_id = str(current_user.id)
        context.metadata["requested_player_name"] = player_name
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context)

    return player


@player_router.delete("/{player_id}")
async def delete_player(
    player_id: str,
    request: Request,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> dict[str, str]:
    """Delete a player character."""
    try:
        success, message = await player_service.delete_player(player_id)
        if not success:
            context = create_context_from_request(request)
            if current_user:
                context.user_id = str(current_user.id)
            context.metadata["requested_player_id"] = player_id
            raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context)

        return {"message": message}
    except ValidationError as e:
        context = create_context_from_request(request)
        if current_user:
            context.user_id = str(current_user.id)
        context.metadata["requested_player_id"] = player_id
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context) from e


# Player stats and effects endpoints
@player_router.post("/{player_id}/sanity-loss")
async def apply_sanity_loss(
    player_id: str,
    amount: int,
    request: Request,
    source: str = "unknown",
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> dict[str, str]:
    """Apply sanity loss to a player."""
    try:
        result = await player_service.apply_sanity_loss(player_id, amount, source)
        assert isinstance(result, dict)
        return result
    except ValidationError as e:
        context = create_context_from_request(request)
        if current_user:
            context.user_id = str(current_user.id)
        context.metadata["requested_player_id"] = player_id
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context) from e


@player_router.post("/{player_id}/fear")
async def apply_fear(
    player_id: str,
    amount: int,
    request: Request,
    source: str = "unknown",
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> dict[str, str]:
    """Apply fear to a player."""
    try:
        result = await player_service.apply_fear(player_id, amount, source)
        assert isinstance(result, dict)
        return result
    except ValidationError as e:
        context = create_context_from_request(request)
        if current_user:
            context.user_id = str(current_user.id)
        context.metadata["requested_player_id"] = player_id
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context) from e


@player_router.post("/{player_id}/corruption")
async def apply_corruption(
    player_id: str,
    amount: int,
    request: Request,
    source: str = "unknown",
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> dict[str, str]:
    """Apply corruption to a player."""
    try:
        result = await player_service.apply_corruption(player_id, amount, source)
        assert isinstance(result, dict)
        return result
    except ValidationError as e:
        context = create_context_from_request(request)
        if current_user:
            context.user_id = str(current_user.id)
        context.metadata["requested_player_id"] = player_id
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context) from e


@player_router.post("/{player_id}/occult-knowledge")
async def gain_occult_knowledge(
    player_id: str,
    amount: int,
    request: Request,
    source: str = "unknown",
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> dict[str, str]:
    """Gain occult knowledge (with sanity loss)."""
    try:
        result = await player_service.gain_occult_knowledge(player_id, amount, source)
        assert isinstance(result, dict)
        return result
    except ValidationError as e:
        context = create_context_from_request(request)
        if current_user:
            context.user_id = str(current_user.id)
        context.metadata["requested_player_id"] = player_id
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context) from e


@player_router.post("/{player_id}/heal")
async def heal_player(
    player_id: str,
    amount: int,
    request: Request,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> dict[str, str]:
    """Heal a player's health."""
    try:
        result = await player_service.heal_player(player_id, amount)
        assert isinstance(result, dict)
        return result
    except ValidationError as e:
        context = create_context_from_request(request)
        if current_user:
            context.user_id = str(current_user.id)
        context.metadata["requested_player_id"] = player_id
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context) from e


@player_router.post("/{player_id}/damage")
async def damage_player(
    player_id: str,
    amount: int,
    request: Request,
    damage_type: str = "physical",
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> dict[str, str]:
    """Damage a player's health."""
    try:
        result = await player_service.damage_player(player_id, amount, damage_type)
        assert isinstance(result, dict)
        return result
    except ValidationError as e:
        context = create_context_from_request(request)
        if current_user:
            context.user_id = str(current_user.id)
        context.metadata["requested_player_id"] = player_id
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context) from e


@player_router.post("/respawn")
async def respawn_player(
    request: Request,
    current_user: User = Depends(get_current_active_user),
) -> dict[str, Any]:
    """
    Respawn a dead player at their respawn location with full HP.

    This endpoint handles player resurrection after death, moving them from
    limbo to their designated respawn room and restoring their HP to 100.

    Rate limited to 1 request per 5 seconds per user.

    Returns:
        dict: Respawn room data and updated player state

    Raises:
        HTTPException(403): Player is not dead
        HTTPException(404): Player not found
        HTTPException(500): Respawn failed
    """
    from ..database import get_async_session
    from ..persistence import get_persistence

    logger.info("Respawn request received", user_id=current_user.id, username=current_user.username)

    try:
        # Get player data
        async for session in get_async_session():
            try:
                # Look up player by user_id (not primary key player_id)
                from sqlalchemy import select

                result = await session.execute(select(Player).where(Player.user_id == str(current_user.id)))
                player = result.scalar_one_or_none()
                if not player:
                    context = create_context_from_request(request)
                    context.user_id = str(current_user.id)
                    raise LoggedHTTPException(status_code=404, detail="Player not found", context=context)

                # Verify player is dead
                if not player.is_dead():
                    context = create_context_from_request(request)
                    context.user_id = str(current_user.id)
                    context.metadata["player_hp"] = player.get_stats().get("current_health", 0)
                    raise LoggedHTTPException(
                        status_code=403,
                        detail="Player must be dead to respawn (HP must be -10 or below)",
                        context=context,
                    )

                # BUGFIX #244: Use shared respawn service instance from app.state
                # This ensures player_combat_service is available for clearing combat state
                # As documented in "Service Lifecycle and State Management" - Dr. Armitage, 1930
                respawn_service = request.app.state.player_respawn_service

                # Respawn the player
                success = await respawn_service.respawn_player(str(player.player_id), session)

                if not success:
                    logger.error("Respawn failed", player_id=player.player_id)
                    raise LoggedHTTPException(
                        status_code=500, detail="Failed to respawn player", context=create_context_from_request(request)
                    )

                # Get respawn room data
                persistence = get_persistence()
                respawn_room_id = player.current_room_id  # Updated by respawn_player
                room = persistence.get_room(str(respawn_room_id))

                if not room:
                    logger.warning("Respawn room not found", respawn_room_id=respawn_room_id)
                    room_data = {"id": respawn_room_id, "name": "Unknown Room"}
                else:
                    room_data = room.to_dict()

                # Get updated player state
                updated_stats = player.get_stats()

                logger.info("Player respawned successfully", player_id=player.player_id, respawn_room=respawn_room_id)

                return {
                    "success": True,
                    "player": {
                        "id": player.player_id,
                        "name": player.name,
                        "hp": updated_stats.get("current_health", 100),
                        "max_hp": 100,
                        "current_room_id": respawn_room_id,
                    },
                    "room": room_data,
                    "message": "You have been resurrected and returned to the waking world",
                }

            except LoggedHTTPException:
                raise
            except Exception as e:
                logger.error("Error in respawn endpoint", error=str(e), exc_info=True)
                context = create_context_from_request(request)
                if current_user:
                    context.user_id = str(current_user.id)
                raise LoggedHTTPException(
                    status_code=500, detail="Failed to process respawn request", context=context
                ) from e

        # This should never be reached, but mypy needs it
        raise LoggedHTTPException(
            status_code=500, detail="No database session available", context=create_context_from_request(request)
        )

    except LoggedHTTPException:
        raise
    except Exception as e:
        logger.error("Unexpected error in respawn endpoint", error=str(e), exc_info=True)
        context = create_context_from_request(request)
        if current_user:
            context.user_id = str(current_user.id)
        raise LoggedHTTPException(status_code=500, detail="Unexpected error during respawn", context=context) from e


# Character Creation and Stats Generation Endpoints
@player_router.post("/roll-stats")
async def roll_character_stats(
    request: Request,
    method: str = "3d6",
    required_class: str | None = None,
    max_attempts: int = 10,
    profession_id: int | None = None,
    current_user: User = Depends(get_current_user),
    timeout_seconds: float = 1.0,
) -> dict[str, Any]:
    """
    Roll random stats for character creation.

    This endpoint generates random character statistics using the specified method
    and validates them against class prerequisites if a required class is specified.

    Rate limited to 10 requests per minute per user.
    """
    # Check if server is shutting down
    from ..commands.admin_shutdown_command import get_shutdown_blocking_message, is_shutdown_pending

    if request and is_shutdown_pending(request.app):
        context = create_error_context(user_id=str(current_user.id) if current_user else None)
        context.metadata["operation"] = "roll_stats"
        context.metadata["reason"] = "server_shutdown"
        raise LoggedHTTPException(
            status_code=503, detail=get_shutdown_blocking_message("stats_rolling"), context=context
        )
    # Check if user is authenticated
    logger.debug("Authentication check", current_user=current_user)
    if not current_user:
        logger.warning("Authentication failed: No user returned from get_current_active_user")
        # Note: We don't have request context here, so we'll create a minimal context
        context = create_error_context()
        raise LoggedHTTPException(status_code=401, detail="Authentication required", context=context)

    logger.info("Authentication successful for user", username=current_user.username, user_id=current_user.id)

    # Apply rate limiting
    try:
        stats_roll_limiter.enforce_rate_limit(str(current_user.id))
    except RateLimitError as e:
        context = create_error_context()
        if current_user:
            context.user_id = str(current_user.id)
        context.metadata["rate_limit_type"] = "stats_roll"
        raise LoggedHTTPException(
            status_code=429,
            detail=f"Rate limit exceeded: {str(e)}. Retry after {e.retry_after} seconds",
            context=context,
        ) from e

    stats_generator = StatsGenerator()
    try:
        if profession_id is not None:
            # Use profession-based stat rolling
            stats, meets_requirements = stats_generator.roll_stats_with_profession(
                method=method,
                profession_id=profession_id,
                timeout_seconds=timeout_seconds,
                max_attempts=max_attempts,
            )
            stat_summary = stats_generator.get_stat_summary(stats)

            return {
                "stats": stats.model_dump(),
                "stat_summary": stat_summary,
                "profession_id": profession_id,
                "meets_requirements": meets_requirements,
                "method_used": method,
            }
        else:
            # Use legacy class-based stat rolling
            stats, available_classes = stats_generator.roll_stats_with_validation(
                method=method,
                required_class=required_class,
                max_attempts=max_attempts,
            )
            stat_summary = stats_generator.get_stat_summary(stats)

            return {
                "stats": stats.model_dump(),
                "stat_summary": stat_summary,
                "available_classes": available_classes,
                "method_used": method,
                "meets_class_requirements": required_class in available_classes if required_class else True,
            }
    except ValueError as e:
        # Handle validation errors (e.g., invalid profession ID)
        context = create_error_context()
        if current_user:
            context.user_id = str(current_user.id)
        context.metadata["operation"] = "roll_stats"
        context.metadata["error"] = str(e)
        raise LoggedHTTPException(status_code=400, detail=f"Invalid profession: {str(e)}", context=context) from e
    except Exception as e:
        context = create_error_context()
        if current_user:
            context.user_id = str(current_user.id)
        context.metadata["operation"] = "roll_stats"
        raise LoggedHTTPException(status_code=500, detail=ErrorMessages.INTERNAL_ERROR, context=context) from e


@player_router.post("/create-character")
async def create_character_with_stats(
    request_data: CreateCharacterRequest,
    request: Request,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> PlayerRead:
    """
    Create a new character with specific stats.

    This endpoint creates a new player character with the provided stats
    and automatically logs the user in with the new character.

    Rate limited to 5 creations per 5 minutes per user.
    """
    # Check if server is shutting down
    from ..commands.admin_shutdown_command import get_shutdown_blocking_message, is_shutdown_pending

    if request and is_shutdown_pending(request.app):
        from ..utils.error_logging import create_error_context

        context = create_error_context(user_id=str(current_user.id) if current_user else None)
        context.metadata["operation"] = "create_character"
        context.metadata["reason"] = "server_shutdown"
        raise LoggedHTTPException(
            status_code=503, detail=get_shutdown_blocking_message("character_creation"), context=context
        )

    # Check if user is authenticated
    if not current_user:
        context = create_context_from_request(request)
        raise LoggedHTTPException(status_code=401, detail=ErrorMessages.AUTHENTICATION_REQUIRED, context=context)

    # Apply rate limiting
    try:
        character_creation_limiter.enforce_rate_limit(str(current_user.id))
    except RateLimitError as e:
        context = create_context_from_request(request)
        if current_user:
            context.user_id = str(current_user.id)
        context.metadata["rate_limit_type"] = "character_creation"
        raise LoggedHTTPException(
            status_code=429,
            detail="Rate limit exceeded",
            context=context,
        ) from e

    try:
        # Validate that character name matches username
        if request_data.name != current_user.username:
            context = create_context_from_request(request)
            if current_user:
                context.user_id = str(current_user.id)
            context.metadata["character_name"] = request_data.name
            context.metadata["username"] = current_user.username
            raise LoggedHTTPException(status_code=400, detail=ErrorMessages.INVALID_INPUT, context=context)

        # Convert dict to Stats object
        stats_obj = Stats(**request_data.stats)

        # Determine starting room from request or config default
        try:
            from ..config import get_config

            default_start_room = get_config().game.default_player_room
        except (ImportError, AttributeError, ValueError) as e:
            logger.error("Error getting default start room config", error=str(e), error_type=type(e).__name__)
            default_start_room = "earth_arkhamcity_northside_intersection_derby_high"

        starting_room_id = getattr(request_data, "starting_room_id", None) or default_start_room

        # Create player with stats
        player = await player_service.create_player_with_stats(
            name=request_data.name,
            stats=stats_obj,
            profession_id=request_data.profession_id,
            starting_room_id=starting_room_id,
            user_id=current_user.id,
        )

        # Note: Invite codes are now marked as used during registration, not during character creation
        # This ensures invites are consumed when users register, preventing invite code reuse
        logger.debug(
            "Character created - invite was already marked as used during registration",
            user_id=current_user.id,
        )

        logger.info("Character created successfully", character_name=request_data.name, user_id=current_user.id)

        # player is already a PlayerRead from the service layer
        return player
    except HTTPException:
        # Re-raise HTTPExceptions without modification
        raise
    except ValueError as e:
        context = create_context_from_request(request)
        if current_user:
            context.user_id = str(current_user.id)
        context.metadata["operation"] = "create_character"
        raise LoggedHTTPException(status_code=400, detail=ErrorMessages.INVALID_INPUT, context=context) from e
    except Exception as e:
        context = create_context_from_request(request)
        if current_user:
            context.user_id = str(current_user.id)
        context.metadata["operation"] = "create_character"
        raise LoggedHTTPException(status_code=500, detail=ErrorMessages.INTERNAL_ERROR, context=context) from e


@player_router.post("/validate-stats")
async def validate_character_stats(
    stats: dict,
    class_name: str | None = None,
    current_user: User = Depends(get_current_user),
) -> dict[str, Any]:
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
        context = create_error_context()
        if current_user:
            context.user_id = str(current_user.id)
        context.metadata["operation"] = "validate_stats"
        raise LoggedHTTPException(status_code=400, detail=ErrorMessages.INVALID_FORMAT, context=context) from e


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
