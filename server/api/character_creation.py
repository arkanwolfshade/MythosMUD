"""
Character creation and stats generation API endpoints.

This module handles endpoints for rolling stats, creating characters,
and validating character stats.
"""

from typing import Any

from fastapi import Depends, HTTPException, Request

from ..auth.users import get_current_user
from ..dependencies import PlayerServiceDep, StatsGeneratorDep
from ..error_types import ErrorMessages
from ..exceptions import LoggedHTTPException, RateLimitError, create_error_context
from ..game.player_service import PlayerService
from ..game.stats_generator import StatsGenerator
from ..models import Stats
from ..models.user import User
from ..schemas.player_requests import CreateCharacterRequest, RollStatsRequest
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.rate_limiter import character_creation_limiter, stats_roll_limiter
from .player_helpers import create_error_context as create_error_context_helper
from .players import player_router

logger = get_logger(__name__)


@player_router.post("/roll-stats")
async def roll_character_stats(
    request_data: RollStatsRequest,
    request: Request,
    max_attempts: int = 50,  # Increased from 10 to improve success rate for profession requirements
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
            # Fetch profession first (async)
            from ..async_persistence import get_async_persistence

            async_persistence = get_async_persistence()
            if not async_persistence:
                context = create_error_context()
                if current_user:
                    context.user_id = str(current_user.id)
                context.metadata["operation"] = "roll_stats"
                context.metadata["profession_id"] = profession_id
                raise LoggedHTTPException(status_code=500, detail="Persistence layer not available", context=context)
            profession = await async_persistence.get_profession_by_id(profession_id)

            if not profession:
                context = create_error_context()
                if current_user:
                    context.user_id = str(current_user.id)
                context.metadata["operation"] = "roll_stats"
                context.metadata["profession_id"] = profession_id
                raise LoggedHTTPException(
                    status_code=404, detail=f"Profession with ID {profession_id} not found", context=context
                )

            # Use profession-based stat rolling with fetched profession
            stats, meets_requirements = stats_generator.roll_stats_with_profession(
                method=method,
                profession_id=profession_id,
                timeout_seconds=timeout_seconds,
                max_attempts=max_attempts,
                profession=profession,  # Pass profession to avoid async lookup
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
    except LoggedHTTPException:
        # Re-raise LoggedHTTPException without modification
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: Character creation errors unpredictable, must create error context
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
        context = create_error_context(user_id=str(current_user.id) if current_user else None)
        context.metadata["operation"] = "create_character"
        context.metadata["reason"] = "server_shutdown"
        raise LoggedHTTPException(
            status_code=503, detail=get_shutdown_blocking_message("character_creation"), context=context
        )

    # Check if user is authenticated
    if not current_user:
        context = create_error_context_helper(request, current_user)
        raise LoggedHTTPException(status_code=401, detail=ErrorMessages.AUTHENTICATION_REQUIRED, context=context)

    # Apply rate limiting
    try:
        character_creation_limiter.enforce_rate_limit(str(current_user.id))
    except RateLimitError as e:
        context = create_error_context_helper(request, current_user, rate_limit_type="character_creation")
        raise LoggedHTTPException(
            status_code=429,
            detail="Rate limit exceeded",
            context=context,
        ) from e

    try:
        # MULTI-CHARACTER: Removed username validation - character names are independent of usernames
        # Character limit check and name uniqueness are handled in PlayerService.create_player_with_stats

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
        context = create_error_context_helper(request, current_user, operation="create_character")
        raise LoggedHTTPException(status_code=400, detail=ErrorMessages.INVALID_INPUT, context=context) from e
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: Character creation errors unpredictable, must create error context
        context = create_error_context_helper(request, current_user, operation="create_character")
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
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: Class retrieval errors unpredictable, must create error context
        context = create_error_context()
        if current_user:
            context.user_id = str(current_user.id)
        context.metadata["operation"] = "validate_stats"
        raise LoggedHTTPException(status_code=400, detail=ErrorMessages.INVALID_FORMAT, context=context) from e
