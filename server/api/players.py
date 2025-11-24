"""
Player management API endpoints for MythosMUD server.

This module handles all player-related API operations including
creation, retrieval, listing, and deletion of player characters.
"""

import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel, Field, field_validator

from ..auth.users import get_current_active_user, get_current_user
from ..dependencies import PlayerServiceDep, StatsGeneratorDep
from ..error_types import ErrorMessages
from ..exceptions import ErrorContext, LoggedHTTPException, RateLimitError, ValidationError, create_error_context
from ..game.player_service import PlayerService
from ..game.stats_generator import StatsGenerator
from ..logging.enhanced_logging_config import get_logger
from ..models import Stats
from ..models.user import User
from ..schemas.player import PlayerRead
from ..utils.error_logging import create_context_from_request
from ..utils.rate_limiter import character_creation_limiter, stats_roll_limiter


class CreateCharacterRequest(BaseModel):
    """Request model for character creation."""

    __slots__ = ()  # Performance optimization

    name: str = Field(..., min_length=1, max_length=50, description="Character name")
    stats: dict = Field(..., description="Character stats dictionary")
    profession_id: int = Field(default=0, ge=0, description="Profession ID")

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        """Validate character name format."""
        if not v or not v.strip():
            raise ValueError("Character name cannot be empty or whitespace")
        return v.strip()


class RollStatsRequest(BaseModel):
    """Request model for rolling character stats."""

    __slots__ = ()  # Performance optimization

    method: str = "3d6"
    required_class: str | None = None
    timeout_seconds: float = 1.0
    profession_id: int | None = None


class SanityLossRequest(BaseModel):
    """Request model for applying sanity loss."""

    __slots__ = ()  # Performance optimization

    amount: int = Field(..., ge=0, le=100, description="Amount of sanity to lose (0-100)")
    source: str = Field(default="unknown", description="Source of sanity loss")


class FearRequest(BaseModel):
    """Request model for applying fear."""

    __slots__ = ()  # Performance optimization

    amount: int = Field(..., ge=0, le=100, description="Amount of fear to apply (0-100)")
    source: str = Field(default="unknown", description="Source of fear")


class CorruptionRequest(BaseModel):
    """Request model for applying corruption."""

    __slots__ = ()  # Performance optimization

    amount: int = Field(..., ge=0, le=100, description="Amount of corruption to apply (0-100)")
    source: str = Field(default="unknown", description="Source of corruption")


class OccultKnowledgeRequest(BaseModel):
    """Request model for gaining occult knowledge."""

    __slots__ = ()  # Performance optimization

    amount: int = Field(..., ge=0, le=100, description="Amount of occult knowledge to gain (0-100)")
    source: str = Field(default="unknown", description="Source of occult knowledge")


class HealRequest(BaseModel):
    """Request model for healing a player."""

    __slots__ = ()  # Performance optimization

    amount: int = Field(..., ge=0, le=1000, description="Amount of health to restore (0-1000)")


class DamageRequest(BaseModel):
    """Request model for damaging a player."""

    __slots__ = ()  # Performance optimization

    amount: int = Field(..., ge=0, le=1000, description="Amount of damage to apply (0-1000)")
    damage_type: str = Field(default="physical", description="Type of damage")


logger = get_logger(__name__)

# Create player router
player_router = APIRouter(prefix="/api/players", tags=["players"])


def _create_error_context(request: Request, current_user: User | None, **metadata: Any) -> ErrorContext:
    """
    Create error context from request and user.

    Helper function to reduce duplication in exception handling.

    Args:
        request: FastAPI Request object
        current_user: Current user or None
        **metadata: Additional metadata to add to context

    Returns:
        ErrorContext: Error context with request and user information
    """

    context = create_context_from_request(request)
    if current_user:
        context.user_id = str(current_user.id)
    context.metadata.update(metadata)
    return context


@player_router.post("/", response_model=PlayerRead)
async def create_player(
    name: str,
    request: Request,
    starting_room_id: str = "earth_arkhamcity_sanitarium_room_foyer_001",
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> dict[str, Any]:
    """Create a new player character."""
    try:
        player = await player_service.create_player(name, profession_id=0, starting_room_id=starting_room_id)
        return player.model_dump()
    except ValidationError:
        context = _create_error_context(request, current_user, player_name=name, starting_room_id=starting_room_id)
        raise LoggedHTTPException(status_code=400, detail=ErrorMessages.INVALID_INPUT, context=context) from None


@player_router.get("/", response_model=list[PlayerRead])
async def list_players(
    request: Request,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> list[dict[str, Any]]:
    """Get a list of all players."""
    result = await player_service.list_players()
    if not isinstance(result, list):
        raise RuntimeError(f"Expected list from player_service.list_players(), got {type(result).__name__}")
    # Convert all PlayerRead objects to dicts
    return [player.model_dump() for player in result]


@player_router.get("/available-classes")
async def get_available_classes(
    current_user: User = Depends(get_current_user),
    stats_generator: StatsGenerator = StatsGeneratorDep,
) -> dict[str, Any]:
    """
    Get information about all available character classes and their prerequisites.
    """

    class_info = {}
    for class_name, prerequisites in stats_generator.CLASS_PREREQUISITES.items():
        class_info[class_name] = {
            "prerequisites": {attr.value: min_value for attr, min_value in prerequisites.items()},
            "description": get_class_description(class_name),
        }

    return {"classes": class_info, "stat_range": {"min": stats_generator.MIN_STAT, "max": stats_generator.MAX_STAT}}


@player_router.get("/{player_id}", response_model=PlayerRead)
async def get_player(
    player_id: uuid.UUID,
    request: Request,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> dict[str, Any]:
    """Get a specific player by ID."""
    player = await player_service.get_player_by_id(player_id)
    if not player:
        context = _create_error_context(request, current_user, requested_player_id=player_id)
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context)

    return player.model_dump()


@player_router.get("/name/{player_name}", response_model=PlayerRead)
async def get_player_by_name(
    player_name: str,
    request: Request,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> dict[str, Any]:
    """Get a specific player by name."""
    player = await player_service.get_player_by_name(player_name)
    if not player:
        context = _create_error_context(request, current_user, requested_player_name=player_name)
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context)

    return player.model_dump()


@player_router.delete("/{player_id}")
async def delete_player(
    player_id: uuid.UUID,
    request: Request,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> dict[str, str]:
    """Delete a player character."""
    try:
        success, message = await player_service.delete_player(player_id)
        if not success:
            context = _create_error_context(request, current_user, requested_player_id=player_id)
            raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context)

        return {"message": message}
    except ValidationError as e:
        context = _create_error_context(request, current_user, requested_player_id=player_id)
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context) from e


# Player stats and effects endpoints
@player_router.post("/{player_id}/sanity-loss")
async def apply_sanity_loss(
    player_id: uuid.UUID,
    request_data: SanityLossRequest,
    request: Request,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> dict[str, str]:
    """Apply sanity loss to a player."""
    try:
        result = await player_service.apply_sanity_loss(player_id, request_data.amount, request_data.source)
        if not isinstance(result, dict):
            raise RuntimeError(f"Expected dict from player_service.apply_sanity_loss(), got {type(result).__name__}")
        return result
    except ValidationError as e:
        context = _create_error_context(request, current_user, requested_player_id=player_id)
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context) from e


@player_router.post("/{player_id}/fear")
async def apply_fear(
    player_id: uuid.UUID,
    request_data: FearRequest,
    request: Request,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> dict[str, str]:
    """Apply fear to a player."""
    try:
        result = await player_service.apply_fear(player_id, request_data.amount, request_data.source)
        if not isinstance(result, dict):
            raise RuntimeError(f"Expected dict from player_service.apply_fear(), got {type(result).__name__}")
        return result
    except ValidationError as e:
        context = _create_error_context(request, current_user, requested_player_id=player_id)
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context) from e


@player_router.post("/{player_id}/corruption")
async def apply_corruption(
    player_id: uuid.UUID,
    request_data: CorruptionRequest,
    request: Request,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> dict[str, str]:
    """Apply corruption to a player."""
    try:
        result = await player_service.apply_corruption(player_id, request_data.amount, request_data.source)
        if not isinstance(result, dict):
            raise RuntimeError(f"Expected dict from player_service.apply_corruption(), got {type(result).__name__}")
        return result
    except ValidationError as e:
        context = _create_error_context(request, current_user, requested_player_id=player_id)
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context) from e


@player_router.post("/{player_id}/occult-knowledge")
async def gain_occult_knowledge(
    player_id: uuid.UUID,
    request_data: OccultKnowledgeRequest,
    request: Request,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> dict[str, str]:
    """Gain occult knowledge (with sanity loss)."""
    try:
        result = await player_service.gain_occult_knowledge(player_id, request_data.amount, request_data.source)
        if not isinstance(result, dict):
            raise RuntimeError(
                f"Expected dict from player_service.gain_occult_knowledge(), got {type(result).__name__}"
            )
        return result
    except ValidationError as e:
        context = _create_error_context(request, current_user, requested_player_id=player_id)
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context) from e


@player_router.post("/{player_id}/heal")
async def heal_player(
    player_id: uuid.UUID,
    request_data: HealRequest,
    request: Request,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> dict[str, str]:
    """Heal a player's health."""
    try:
        result = await player_service.heal_player(player_id, request_data.amount)
        if not isinstance(result, dict):
            raise RuntimeError(f"Expected dict from player_service.heal_player(), got {type(result).__name__}")
        return result
    except ValidationError as e:
        context = _create_error_context(request, current_user, requested_player_id=player_id)
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context) from e


@player_router.post("/{player_id}/damage")
async def damage_player(
    player_id: uuid.UUID,
    request_data: DamageRequest,
    request: Request,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> dict[str, str]:
    """Damage a player's health."""
    try:
        result = await player_service.damage_player(player_id, request_data.amount, request_data.damage_type)
        if not isinstance(result, dict):
            raise RuntimeError(f"Expected dict from player_service.damage_player(), got {type(result).__name__}")
        return result
    except ValidationError as e:
        context = _create_error_context(request, current_user, requested_player_id=player_id)
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context) from e


@player_router.post("/respawn")
async def respawn_player(
    request: Request,
    current_user: User = Depends(get_current_active_user),
    player_service: PlayerService = PlayerServiceDep,
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
        async for session in get_async_session():
            try:
                # Get respawn service from app.state
                respawn_service = request.app.state.player_respawn_service
                persistence = get_persistence()

                # Use service layer method to handle respawn logic
                return await player_service.respawn_player_by_user_id(
                    user_id=str(current_user.id),
                    session=session,
                    respawn_service=respawn_service,
                    persistence=persistence,
                )
            except ValidationError as e:
                # Convert ValidationError to appropriate HTTPException
                context = _create_error_context(request, current_user)
                if "not found" in str(e).lower():
                    raise LoggedHTTPException(status_code=404, detail="Player not found", context=context) from e
                elif "must be dead" in str(e).lower():
                    raise LoggedHTTPException(
                        status_code=403,
                        detail="Player must be dead to respawn (HP must be -10 or below)",
                        context=context,
                    ) from e
                else:
                    raise LoggedHTTPException(
                        status_code=500, detail="Failed to respawn player", context=context
                    ) from e
            except LoggedHTTPException:
                raise
            except Exception as e:
                context = _create_error_context(request, current_user, operation="respawn_player")
                logger.error(
                    "Error in respawn endpoint",
                    error=str(e),
                    exc_info=True,
                    context=context.to_dict(),
                )
                raise LoggedHTTPException(
                    status_code=500, detail="Failed to process respawn request", context=context
                ) from e

        # This should never be reached, but mypy needs it
        raise LoggedHTTPException(
            status_code=500,
            detail="No database session available",
            context=_create_error_context(request, current_user),
        )

    except LoggedHTTPException:
        raise
    except Exception as e:
        context = _create_error_context(request, current_user, operation="respawn_player")
        logger.error(
            "Unexpected error in respawn endpoint",
            error=str(e),
            exc_info=True,
            context=context.to_dict(),
        )
        raise LoggedHTTPException(status_code=500, detail="Unexpected error during respawn", context=context) from e


# Character Creation and Stats Generation Endpoints
@player_router.post("/roll-stats")
async def roll_character_stats(
    request_data: RollStatsRequest,
    request: Request,
    max_attempts: int = 10,
    current_user: User = Depends(get_current_user),
    stats_generator: StatsGenerator = StatsGeneratorDep,
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

    try:
        # Extract parameters from request data
        method = request_data.method
        profession_id = request_data.profession_id
        required_class = request_data.required_class
        timeout_seconds = request_data.timeout_seconds

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
) -> dict[str, Any]:
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
        context = _create_error_context(request, current_user)
        raise LoggedHTTPException(status_code=401, detail=ErrorMessages.AUTHENTICATION_REQUIRED, context=context)

    # Apply rate limiting
    try:
        character_creation_limiter.enforce_rate_limit(str(current_user.id))
    except RateLimitError as e:
        context = _create_error_context(request, current_user, rate_limit_type="character_creation")
        raise LoggedHTTPException(
            status_code=429,
            detail="Rate limit exceeded",
            context=context,
        ) from e

    try:
        # Validate that character name matches username
        if request_data.name != current_user.username:
            context = _create_error_context(
                request, current_user, character_name=request_data.name, username=current_user.username
            )
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

        # Convert PlayerRead to dict for better performance
        return player.model_dump()
    except HTTPException:
        # Re-raise HTTPExceptions without modification
        raise
    except ValueError as e:
        context = _create_error_context(request, current_user, operation="create_character")
        raise LoggedHTTPException(status_code=400, detail=ErrorMessages.INVALID_INPUT, context=context) from e
    except Exception as e:
        context = _create_error_context(request, current_user, operation="create_character")
        raise LoggedHTTPException(status_code=500, detail=ErrorMessages.INTERNAL_ERROR, context=context) from e


@player_router.post("/validate-stats")
async def validate_character_stats(
    stats: dict,
    class_name: str | None = None,
    current_user: User = Depends(get_current_user),
    stats_generator: StatsGenerator = StatsGeneratorDep,
) -> dict[str, Any]:
    """
    Validate character stats against class prerequisites.

    This endpoint checks if the provided stats meet the requirements for a given class.
    """

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
