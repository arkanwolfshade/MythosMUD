"""
Character creation and stats generation API endpoints.

This module handles endpoints for rolling stats, creating characters,
and validating character stats.
"""

from typing import TYPE_CHECKING, Any

from fastapi import Depends, HTTPException, Request

from ..auth.users import get_current_user
from ..dependencies import PlayerServiceDep, ProfessionServiceDep, SkillServiceDep, StatsGeneratorDep
from ..error_types import ErrorMessages
from ..exceptions import LoggedHTTPException, RateLimitError, ValidationError
from ..game.player_service import PlayerService
from ..game.profession_service import ProfessionService
from ..game.skill_service import SkillService
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
from ..schemas.players.stat_values import RolledStats
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.rate_limiter import character_creation_limiter, stats_roll_limiter
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
        raise LoggedHTTPException(
            status_code=503,
            detail=get_shutdown_blocking_message("stats_rolling"),
            user_id=str(current_user.id) if current_user else None,
            operation="roll_stats",
            reason="server_shutdown",
        )


def _validate_user_for_stats_roll(current_user: User) -> None:
    """Validate user is authenticated for stats roll."""
    logger.debug("Authentication check", current_user=current_user)
    if not current_user:
        logger.warning("Authentication failed: No user returned from get_current_active_user")
        raise LoggedHTTPException(status_code=401, detail="Authentication required")

    logger.info("Authentication successful for user", username=current_user.username, user_id=current_user.id)


def _apply_rate_limiting_for_stats_roll(current_user: User) -> None:
    """Apply rate limiting for stats roll operation."""
    try:
        stats_roll_limiter.enforce_rate_limit(str(current_user.id))
    except RateLimitError as e:
        raise LoggedHTTPException(
            status_code=429,
            detail=f"Rate limit exceeded: {str(e)}. Retry after {e.retry_after} seconds",
            user_id=str(current_user.id) if current_user else None,
            rate_limit_type="stats_roll",
        ) from e


def _stats_to_rolled_stats(stats: Stats) -> RolledStats:
    """Convert Stats model to RolledStats schema."""
    stats_dict = stats.model_dump()
    return RolledStats(
        strength=stats_dict.get("strength") or 50,
        dexterity=stats_dict.get("dexterity") or 50,
        constitution=stats_dict.get("constitution") or 50,
        size=stats_dict.get("size") or 50,
        intelligence=stats_dict.get("intelligence") or 50,
        power=stats_dict.get("power") or 50,
        education=stats_dict.get("education") or 50,
        charisma=stats_dict.get("charisma") or 50,
        luck=stats_dict.get("luck") or 50,
    )


def _apply_stat_modifiers(stats_dict: dict[str, Any], modifiers: list[dict[str, Any]]) -> dict[str, Any]:
    """Apply profession stat_modifiers to a stats dict; returns new dict. Plan 4.4."""
    result = dict(stats_dict)
    for m in modifiers:
        stat_name = m.get("stat")
        delta = m.get("value", 0)
        if stat_name and isinstance(delta, int | float):
            current = result.get(stat_name)
            if current is not None:
                result[stat_name] = max(1, min(99, int(current) + int(delta)))
    return result


async def _execute_create_character(
    request_data: CreateCharacterRequest,
    current_user: User,
    player_service: PlayerService,
    profession_service: ProfessionService,
    skill_service: SkillService,
) -> CreateCharacterResponse:
    """
    Perform character creation: apply stat modifiers, validate skills, create player, set skills.
    Extracted to keep create_character_with_stats under ruff complexity limit (C901).
    """
    stats_dict = dict(request_data.stats)
    if request_data.profession_id and request_data.profession_id > 0:
        try:
            profession = await profession_service.validate_and_get_profession(request_data.profession_id)
            modifiers = profession.get_stat_modifiers()
            stats_dict = _apply_stat_modifiers(stats_dict, modifiers)
        except ValidationError:
            pass
    stats_obj = Stats(**stats_dict)

    if request_data.occupation_slots is not None or request_data.personal_interest is not None:
        if request_data.occupation_slots is None or request_data.personal_interest is None:
            raise LoggedHTTPException(
                status_code=400,
                detail="Both occupation_slots and personal_interest must be provided together",
                user_id=str(current_user.id),
                operation="create_character",
            )
        occ = [{"skill_id": s.skill_id, "value": s.value} for s in request_data.occupation_slots]
        pers = [{"skill_id": s.skill_id} for s in request_data.personal_interest]
        try:
            await skill_service.validate_skills_payload(
                occupation_slots=occ,
                personal_interest=pers,
                profession_id=request_data.profession_id,
            )
        except ValueError as e:
            raise LoggedHTTPException(
                status_code=400,
                detail=str(e),
                user_id=str(current_user.id),
                operation="create_character",
            ) from e

    requested_room_id = getattr(request_data, "starting_room_id", None)
    starting_room_id = player_service.get_default_starting_room(requested_room_id)
    start_in_tutorial = getattr(request_data, "start_in_tutorial", True)
    player = await player_service.create_player_with_stats(
        name=request_data.name,
        stats=stats_obj,
        profession_id=request_data.profession_id,
        starting_room_id=starting_room_id,
        user_id=current_user.id,
        start_in_tutorial=start_in_tutorial,
    )

    if request_data.occupation_slots is not None and request_data.personal_interest is not None:
        occ = [{"skill_id": s.skill_id, "value": s.value} for s in request_data.occupation_slots]
        pers = [{"skill_id": s.skill_id} for s in request_data.personal_interest]
        stats_for_edu = stats_dict.get("education") or 50
        await skill_service.set_player_skills(
            player_id=player.id,
            occupation_slots=occ,
            personal_interest=pers,
            profession_id=request_data.profession_id,
            stats_for_edu=stats_for_edu,
        )

    logger.debug(
        "Character created - invite was already marked as used during registration",
        user_id=current_user.id,
    )
    logger.info("Character created successfully", character_name=request_data.name, user_id=current_user.id)
    return CreateCharacterResponse(player=player)


async def _roll_stats_raw(request_data: RollStatsRequest, stats_generator: StatsGenerator) -> dict[str, Any]:
    """Roll stats with no profession or class requirement. Plan 10.5 A1."""
    stats = stats_generator.roll_stats(method=request_data.method)
    stat_summary_dict = stats_generator.get_stat_summary(stats)
    stat_summary = _convert_stat_summary_to_stat_summary_model(stats, stat_summary_dict)
    return {
        "stats": _stats_to_rolled_stats(stats),
        "stat_summary": stat_summary,
        "method_used": request_data.method,
    }


async def _roll_stats_with_profession_preview(
    request_data: RollStatsRequest,
    stats_generator: StatsGenerator,
    current_user: User,
    profession_service: ProfessionService,
) -> dict[str, Any]:
    """Roll once, apply profession stat_modifiers for preview. Plan 10.5 A1."""
    if request_data.profession_id is None:
        raise LoggedHTTPException(
            status_code=400,
            detail="profession_id is required for profession preview",
            user_id=str(current_user.id) if current_user else None,
            operation="roll_stats",
        )
    profession_id: int = request_data.profession_id
    profession = await profession_service.validate_and_get_profession(profession_id)
    stats = stats_generator.roll_stats(method=request_data.method)
    stat_summary_dict = stats_generator.get_stat_summary(stats)
    stat_summary = _convert_stat_summary_to_stat_summary_model(stats, stat_summary_dict)
    rolled = _stats_to_rolled_stats(stats)
    modifiers = profession.get_stat_modifiers()
    stats_dict = stats.model_dump()
    modified_dict = _apply_stat_modifiers(stats_dict, modifiers)
    stats_with_mods = Stats(**modified_dict)
    preview = _stats_to_rolled_stats(stats_with_mods)
    return {
        "stats": rolled,
        "stat_summary": stat_summary,
        "profession_id": profession_id,
        "stats_with_profession_modifiers": preview,
        "meets_requirements": True,
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
        "stats": _stats_to_rolled_stats(stats),
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
            result = await _roll_stats_with_profession_preview(
                request_data, stats_generator, current_user, profession_service
            )
            return RollStatsResponse(**result)
        if request_data.required_class is not None:
            result = _roll_stats_with_class(request_data, stats_generator, max_attempts)
            return RollStatsResponse(**result)
        result = await _roll_stats_raw(request_data, stats_generator)
        return RollStatsResponse(**result)
    except ValidationError as e:
        status_code = 404 if "not found" in str(e).lower() else 400
        raise LoggedHTTPException(
            status_code=status_code,
            detail=str(e),
            user_id=str(current_user.id) if current_user else None,
            operation="roll_stats",
            profession_id=request_data.profession_id if request_data.profession_id else None,
        ) from e
    except ValueError as e:
        # Handle validation errors (e.g., invalid profession ID)
        raise LoggedHTTPException(
            status_code=400,
            detail=f"Invalid profession: {str(e)}",
            user_id=str(current_user.id) if current_user else None,
            operation="roll_stats",
            error=str(e),
        ) from e
    except LoggedHTTPException:
        # Re-raise LoggedHTTPException without modification
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Character creation errors unpredictable, must create error context
        raise LoggedHTTPException(
            status_code=500,
            detail=ErrorMessages.INTERNAL_ERROR,
            user_id=str(current_user.id) if current_user else None,
            operation="roll_stats",
        ) from e


@player_router.post("/create-character", response_model=CreateCharacterResponse)
async def create_character_with_stats(
    request_data: CreateCharacterRequest,
    request: Request,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
    profession_service: ProfessionService = ProfessionServiceDep,
    skill_service: SkillService = SkillServiceDep,
) -> CreateCharacterResponse:
    """
    Create a new character with specific stats.

    This endpoint creates a new player character with the provided stats
    and automatically logs the user in with the new character.
    Server applies profession stat_modifiers to rolled stats; if occupation_slots
    and personal_interest are provided, sets player skills.

    Rate limited to 5 creations per 5 minutes per user.
    """
    # Check if server is shutting down
    from ..commands.admin_shutdown_command import get_shutdown_blocking_message, is_shutdown_pending

    if request and is_shutdown_pending(request.app):
        raise LoggedHTTPException(
            status_code=503,
            detail=get_shutdown_blocking_message("character_creation"),
            user_id=str(current_user.id) if current_user else None,
            operation="create_character",
            reason="server_shutdown",
        )

    # Check if user is authenticated
    if not current_user:
        raise LoggedHTTPException(status_code=401, detail=ErrorMessages.AUTHENTICATION_REQUIRED)

    # Apply rate limiting
    try:
        character_creation_limiter.enforce_rate_limit(str(current_user.id))
    except RateLimitError as e:
        raise LoggedHTTPException(
            status_code=429,
            detail="Rate limit exceeded",
            user_id=str(current_user.id) if current_user else None,
            rate_limit_type="character_creation",
        ) from e

    try:
        return await _execute_create_character(
            request_data, current_user, player_service, profession_service, skill_service
        )
    except HTTPException:
        # Re-raise HTTPExceptions without modification
        raise
    except ValueError as e:
        raise LoggedHTTPException(
            status_code=400,
            detail=ErrorMessages.INVALID_INPUT,
            user_id=str(current_user.id) if current_user else None,
            operation="create_character",
        ) from e
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Character creation errors unpredictable, must create error context
        raise LoggedHTTPException(
            status_code=500,
            detail=ErrorMessages.INTERNAL_ERROR,
            user_id=str(current_user.id) if current_user else None,
            operation="create_character",
        ) from e


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
        stat_summary_dict = stats_generator.get_stat_summary(stats_obj)
        stat_summary = _convert_stat_summary_to_stat_summary_model(stats_obj, stat_summary_dict)

        return ValidateStatsResponse(available_classes=available_classes, stat_summary=stat_summary)
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Class retrieval errors unpredictable, must create error context
        raise LoggedHTTPException(
            status_code=400,
            detail=ErrorMessages.INVALID_FORMAT,
            user_id=str(current_user.id) if current_user else None,
            operation="validate_stats",
        ) from e
