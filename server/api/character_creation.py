"""
Character creation and stats generation API endpoints.

This module handles endpoints for rolling stats, creating characters,
and validating character stats.
"""

from typing import TYPE_CHECKING, Any

from fastapi import Depends, HTTPException, Request

from ..auth.users import get_current_user
from ..dependencies import PlayerServiceDep, ProfessionServiceDep, StatsGeneratorDep
from ..error_types import ErrorMessages
from ..exceptions import LoggedHTTPException, RateLimitError, ValidationError, create_error_context
from ..game.player_service import PlayerService
from ..game.profession_service import ProfessionService
from ..game.stats_generator import StatsGenerator
from ..models import Stats
from ..models.user import User
from ..schemas.players import (
    CreateCharacterRequest,
    CreateCharacterResponse,
    RollStatsRequest,
    RollStatsResponse,
    StatSummary,
    ValidateStatsResponse,
)
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.rate_limiter import character_creation_limiter, stats_roll_limiter
from .player_helpers import create_error_context as create_error_context_helper
from .players import player_router

if TYPE_CHECKING:
    pass

logger = get_logger(__name__)


def _convert_stat_summary_to_stat_summary_model(stats: Stats, summary_dict: dict[str, Any]) -> StatSummary:
    """
    Convert get_stat_summary dict to StatSummary model format.

    Args:
        stats: Stats model instance
        summary_dict: Dict returned from get_stat_summary

    Returns:
        StatSummary model instance
    """
    # Calculate highest and lowest stat values
    stat_values = [
        stats.strength or 50,
        stats.dexterity or 50,
        stats.constitution or 50,
        stats.size or 50,
        stats.intelligence or 50,
        stats.power or 50,
        stats.education or 50,
        stats.charisma or 50,
        stats.luck or 50,
    ]
    highest = max(stat_values)
    lowest = min(stat_values)

    return StatSummary(
        total=summary_dict.get("total_points", 0),
        average=summary_dict.get("average_stat", 0.0),
        highest=highest,
        lowest=lowest,
    )


def _check_shutdown_status(request: Request, current_user: User) -> None:
    """Check if server is shutting down and raise exception if so."""
    from ..commands.admin_shutdown_command import get_shutdown_blocking_message, is_shutdown_pending

    if request and is_shutdown_pending(request.app):
        context = create_error_context(user_id=str(current_user.id) if current_user else None)
        context.metadata["operation"] = "roll_stats"
        context.metadata["reason"] = "server_shutdown"
        raise LoggedHTTPException(
            status_code=503, detail=get_shutdown_blocking_message("stats_rolling"), context=context
        )


def _validate_user_for_stats_roll(current_user: User) -> None:
    """Validate user is authenticated for stats roll."""
    logger.debug("Authentication check", current_user=current_user)
    if not current_user:
        logger.warning("Authentication failed: No user returned from get_current_active_user")
        context = create_error_context()
        raise LoggedHTTPException(status_code=401, detail="Authentication required", context=context)

    logger.info("Authentication successful for user", username=current_user.username, user_id=current_user.id)


def _apply_rate_limiting_for_stats_roll(current_user: User) -> None:
    """Apply rate limiting for stats roll operation."""
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


async def _roll_stats_with_profession(
    request_data: RollStatsRequest,
    stats_generator: StatsGenerator,
    current_user: User,
    max_attempts: int,
    profession_service: ProfessionService,
) -> dict[str, Any]:
    """
    Roll stats using profession-based method.

    Delegates profession validation to ProfessionService.validate_and_get_profession()
    to centralize business logic and improve reusability.
    """
    # Validate and get profession using ProfessionService
    try:
        # After None check, profession_id is guaranteed to be non-None
        if request_data.profession_id is None:
            context = create_error_context()
            if current_user:
                context.user_id = str(current_user.id)
            context.metadata["operation"] = "roll_stats"
            raise LoggedHTTPException(
                status_code=400,
                detail="profession_id is required for profession-based rolling",
                context=context,
            )
        profession_id: int = request_data.profession_id

        profession = await profession_service.validate_and_get_profession(profession_id)
    except ValidationError as e:
        context = create_error_context()
        if current_user:
            context.user_id = str(current_user.id)
        context.metadata["operation"] = "roll_stats"
        if request_data.profession_id:
            context.metadata["profession_id"] = request_data.profession_id
        # Convert ValidationError to appropriate HTTP status code
        if "not found" in str(e).lower():
            status_code = 404
        else:
            status_code = 400
        raise LoggedHTTPException(status_code=status_code, detail=str(e), context=context) from e

    # Roll stats with validated profession
    stats, meets_requirements = stats_generator.roll_stats_with_profession(
        method=request_data.method,
        profession_id=profession_id,
        timeout_seconds=request_data.timeout_seconds,
        max_attempts=max_attempts,
        profession=profession,
    )
    stat_summary_dict = stats_generator.get_stat_summary(stats)
    stat_summary = _convert_stat_summary_to_stat_summary_model(stats, stat_summary_dict)

    return {
        "stats": stats.model_dump(),
        "stat_summary": stat_summary,
        "profession_id": profession_id,
        "meets_requirements": meets_requirements,
        "method_used": request_data.method,
    }


def _roll_stats_with_class(
    request_data: RollStatsRequest, stats_generator: StatsGenerator, max_attempts: int
) -> dict[str, Any]:
    """Roll stats using legacy class-based method."""
    stats, available_classes = stats_generator.roll_stats_with_validation(
        method=request_data.method,
        required_class=request_data.required_class,
        max_attempts=max_attempts,
    )
    stat_summary_dict = stats_generator.get_stat_summary(stats)
    stat_summary = _convert_stat_summary_to_stat_summary_model(stats, stat_summary_dict)

    return {
        "stats": stats.model_dump(),
        "stat_summary": stat_summary,
        "available_classes": available_classes,
        "method_used": request_data.method,
        "meets_class_requirements": request_data.required_class in available_classes
        if request_data.required_class
        else True,
    }


@player_router.post("/roll-stats", response_model=RollStatsResponse)
async def roll_character_stats(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: FastAPI endpoint requires request, user, and service dependencies; max_attempts is a configurable parameter
    request_data: RollStatsRequest,
    request: Request,
    max_attempts: int = 50,  # Increased from 10 to improve success rate for profession requirements
    current_user: User = Depends(get_current_user),
    stats_generator: StatsGenerator = StatsGeneratorDep,
    profession_service: ProfessionService = ProfessionServiceDep,
) -> RollStatsResponse:
    """
    Roll random stats for character creation.

    This endpoint generates random character statistics using the specified method
    and validates them against class prerequisites if a required class is specified.

    Rate limited to 10 requests per minute per user.
    """
    _check_shutdown_status(request, current_user)
    _validate_user_for_stats_roll(current_user)
    _apply_rate_limiting_for_stats_roll(current_user)

    try:
        if request_data.profession_id is not None:
            result = await _roll_stats_with_profession(
                request_data, stats_generator, current_user, max_attempts, profession_service
            )
            return RollStatsResponse(**result)
        result = _roll_stats_with_class(request_data, stats_generator, max_attempts)
        return RollStatsResponse(**result)
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
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Character creation errors unpredictable, must create error context
        context = create_error_context()
        if current_user:
            context.user_id = str(current_user.id)
        context.metadata["operation"] = "roll_stats"
        raise LoggedHTTPException(status_code=500, detail=ErrorMessages.INTERNAL_ERROR, context=context) from e


@player_router.post("/create-character", response_model=CreateCharacterResponse)
async def create_character_with_stats(
    request_data: CreateCharacterRequest,
    request: Request,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> CreateCharacterResponse:
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

        # Determine starting room from request or config default using PlayerService
        requested_room_id = getattr(request_data, "starting_room_id", None)
        starting_room_id = player_service.get_default_starting_room(requested_room_id)

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

        return CreateCharacterResponse(player=player)
    except HTTPException:
        # Re-raise HTTPExceptions without modification
        raise
    except ValueError as e:
        context = create_error_context_helper(request, current_user, operation="create_character")
        raise LoggedHTTPException(status_code=400, detail=ErrorMessages.INVALID_INPUT, context=context) from e
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Character creation errors unpredictable, must create error context
        context = create_error_context_helper(request, current_user, operation="create_character")
        raise LoggedHTTPException(status_code=500, detail=ErrorMessages.INTERNAL_ERROR, context=context) from e


@player_router.post("/validate-stats", response_model=ValidateStatsResponse)
async def validate_character_stats(
    stats: dict[str, Any],
    class_name: str | None = None,
    current_user: User = Depends(get_current_user),
    stats_generator: StatsGenerator = StatsGeneratorDep,
) -> ValidateStatsResponse:
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

            return ValidateStatsResponse(
                meets_prerequisites=meets_prerequisites,
                failed_requirements=failed_requirements,
                available_classes=available_classes,
                requested_class=class_name,
            )

        available_classes = stats_generator.get_available_classes(stats_obj)
        stat_summary = stats_generator.get_stat_summary(stats_obj)

        return ValidateStatsResponse(available_classes=available_classes, stat_summary=stat_summary)
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Class retrieval errors unpredictable, must create error context
        context = create_error_context()
        if current_user:
            context.user_id = str(current_user.id)
        context.metadata["operation"] = "validate_stats"
        raise LoggedHTTPException(status_code=400, detail=ErrorMessages.INVALID_FORMAT, context=context) from e
