"""
Character creation and stats generation API endpoints.

This module handles endpoints for rolling stats, creating characters,
and validating character stats.
"""

from typing import Annotated, NoReturn, cast

from fastapi import Depends, FastAPI, HTTPException, Request

from ..auth.users import get_current_user
from ..dependencies import get_player_service, get_profession_service, get_skill_service, get_stats_generator
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
    PlayerRead,
    RollStatsRequest,
    RollStatsResponse,
    StatSummary,
    ValidateStatsResponse,
)
from ..schemas.players.stat_values import RolledStats
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.rate_limiter import character_creation_limiter, stats_roll_limiter
from .player_router import player_router

logger = get_logger(__name__)


def _stat_or_default(value: int | None, default: int = 50) -> int:
    """Treat missing stats as the generator default (50)."""
    return default if value is None else value


def _as_int(value: object, default: int = 0) -> int:
    return int(value) if isinstance(value, int | float) else default


def _as_float(value: object, default: float = 0.0) -> float:
    return float(value) if isinstance(value, int | float) else default


def _convert_stat_summary_to_stat_summary_model(stats: Stats, summary_dict: dict[str, object]) -> StatSummary:
    """
    Convert get_stat_summary dict to StatSummary model format.

    Args:
        stats: Stats model instance
        summary_dict: Dict returned from get_stat_summary

    Returns:
        StatSummary model instance
    """
    stat_values = [
        _stat_or_default(stats.strength),
        _stat_or_default(stats.dexterity),
        _stat_or_default(stats.constitution),
        _stat_or_default(stats.size),
        _stat_or_default(stats.intelligence),
        _stat_or_default(stats.power),
        _stat_or_default(stats.education),
        _stat_or_default(stats.charisma),
        _stat_or_default(stats.luck),
    ]
    return StatSummary(
        total=_as_int(summary_dict.get("total_points", 0)),
        average=_as_float(summary_dict.get("average_stat", 0.0)),
        highest=max(stat_values),
        lowest=min(stat_values),
    )


def _require_current_user(current_user: User | None, operation: str) -> User:
    """Reject missing user before rate-limit or shutdown checks (direct-call tests / Depends bypass)."""
    if current_user is None:
        raise LoggedHTTPException(
            status_code=401,
            detail=ErrorMessages.AUTHENTICATION_REQUIRED,
            operation=operation,
        )
    return current_user


def _check_shutdown_status(request: Request, current_user: User) -> None:
    """Check if server is shutting down and raise exception if so."""
    from ..commands.admin_shutdown_command import get_shutdown_blocking_message, is_shutdown_pending

    # Cast: Starlette types request.app as Any; FastAPI instance is the runtime type.
    if request and is_shutdown_pending(cast(FastAPI, request.app)):
        raise LoggedHTTPException(
            status_code=503,
            detail=get_shutdown_blocking_message("stats_rolling"),
            user_id=str(current_user.id) if current_user else None,
            operation="roll_stats",
            reason="server_shutdown",
        )


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


def _apply_stat_modifiers(stats_dict: dict[str, object], modifiers: list[dict[str, object]]) -> dict[str, object]:
    """Apply profession stat_modifiers to a stats dict; returns new dict. Plan 4.4."""
    result = dict(stats_dict)
    for m in modifiers:
        stat_name = m.get("stat")
        delta = m.get("value", 0)
        if isinstance(stat_name, str) and isinstance(delta, int | float):
            current = result.get(stat_name)
            if isinstance(current, int | float):
                result[stat_name] = max(1, min(99, int(current) + int(delta)))
    return result


async def _resolve_stats_with_profession(
    request_data: CreateCharacterRequest, profession_service: ProfessionService
) -> dict[str, object]:
    stats_dict: dict[str, object] = dict(request_data.stats)
    if request_data.profession_id and request_data.profession_id > 0:
        try:
            profession = await profession_service.validate_and_get_profession(request_data.profession_id)
            stats_dict = _apply_stat_modifiers(
                stats_dict, cast(list[dict[str, object]], profession.get_stat_modifiers())
            )
        except ValidationError:
            pass
    return stats_dict


def _skills_payload_from_request(
    request_data: CreateCharacterRequest,
    current_user: User,
) -> tuple[list[dict[str, int]], list[dict[str, int]]] | None:
    if request_data.occupation_slots is None and request_data.personal_interest is None:
        return None
    if request_data.occupation_slots is None or request_data.personal_interest is None:
        raise LoggedHTTPException(
            status_code=400,
            detail="Both occupation_slots and personal_interest must be provided together",
            user_id=str(current_user.id),
            operation="create_character",
        )
    occ = [{"skill_id": s.skill_id, "value": s.value} for s in request_data.occupation_slots]
    pers = [{"skill_id": s.skill_id} for s in request_data.personal_interest]
    return occ, pers


async def _validate_skills_payload(
    request_data: CreateCharacterRequest,
    current_user: User,
    skill_service: SkillService,
    occ: list[dict[str, int]],
    pers: list[dict[str, int]],
) -> None:
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


async def _set_player_skills_if_present(
    request_data: CreateCharacterRequest,
    player: PlayerRead,
    skill_service: SkillService,
    stats_dict: dict[str, object],
    occ: list[dict[str, int]],
    pers: list[dict[str, int]],
) -> None:
    stats_for_edu_raw = stats_dict.get("education") or 50
    stats_for_edu = int(stats_for_edu_raw) if isinstance(stats_for_edu_raw, int | float) else 50
    await skill_service.set_player_skills(
        player_id=player.id,
        occupation_slots=occ,
        personal_interest=pers,
        profession_id=request_data.profession_id,
        stats_for_edu=stats_for_edu,
    )


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
    stats_dict = await _resolve_stats_with_profession(request_data, profession_service)
    stats_obj = Stats.model_validate(stats_dict)

    skills_payload = _skills_payload_from_request(request_data, current_user)
    if skills_payload is not None:
        occ, pers = skills_payload
        await _validate_skills_payload(request_data, current_user, skill_service, occ, pers)

    starting_room_id = player_service.get_default_starting_room(getattr(request_data, "starting_room_id", None))
    start_in_tutorial = getattr(request_data, "start_in_tutorial", True)
    player = await player_service.create_player_with_stats(
        name=request_data.name,
        stats=stats_obj,
        profession_id=request_data.profession_id,
        starting_room_id=starting_room_id,
        user_id=current_user.id,
        start_in_tutorial=start_in_tutorial,
    )

    if skills_payload is not None:
        occ, pers = skills_payload
        await _set_player_skills_if_present(request_data, player, skill_service, stats_dict, occ, pers)

    logger.debug(
        "Character created - invite was already marked as used during registration",
        user_id=current_user.id,
    )
    logger.info("Character created successfully", character_name=request_data.name, user_id=current_user.id)
    return CreateCharacterResponse(player=player)


async def _roll_stats_raw(request_data: RollStatsRequest, stats_generator: StatsGenerator) -> RollStatsResponse:
    """Roll stats with no profession or class requirement. Plan 10.5 A1."""
    stats = stats_generator.roll_stats(method=request_data.method)
    stat_summary_dict: dict[str, object] = dict(stats_generator.get_stat_summary(stats))
    stat_summary = _convert_stat_summary_to_stat_summary_model(stats, stat_summary_dict)
    return RollStatsResponse(
        stats=_stats_to_rolled_stats(stats),
        stat_summary=stat_summary,
        method_used=request_data.method,
    )


async def _roll_stats_with_profession_preview(
    request_data: RollStatsRequest,
    stats_generator: StatsGenerator,
    current_user: User,
    profession_service: ProfessionService,
) -> RollStatsResponse:
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
    stat_summary_dict: dict[str, object] = dict(stats_generator.get_stat_summary(stats))
    stat_summary = _convert_stat_summary_to_stat_summary_model(stats, stat_summary_dict)
    rolled = _stats_to_rolled_stats(stats)
    modifiers = profession.get_stat_modifiers()
    stats_dict: dict[str, object] = dict(stats.model_dump())
    modified_dict = _apply_stat_modifiers(stats_dict, cast(list[dict[str, object]], modifiers))
    stats_with_mods = Stats.model_validate(modified_dict)
    preview = _stats_to_rolled_stats(stats_with_mods)
    return RollStatsResponse(
        stats=rolled,
        stat_summary=stat_summary,
        profession_id=profession_id,
        stats_with_profession_modifiers=preview,
        meets_requirements=True,
        method_used=request_data.method,
    )


def _roll_stats_with_class(
    request_data: RollStatsRequest, stats_generator: StatsGenerator, max_attempts: int
) -> RollStatsResponse:
    """Roll stats using legacy class-based method."""
    stats, available_classes = stats_generator.roll_stats_with_validation(
        method=request_data.method,
        required_class=request_data.required_class,
        max_attempts=max_attempts,
    )
    stat_summary_dict: dict[str, object] = dict(stats_generator.get_stat_summary(stats))
    stat_summary = _convert_stat_summary_to_stat_summary_model(stats, stat_summary_dict)

    return RollStatsResponse(
        stats=_stats_to_rolled_stats(stats),
        stat_summary=stat_summary,
        available_classes=available_classes,
        method_used=request_data.method,
        meets_class_requirements=request_data.required_class in available_classes
        if request_data.required_class
        else True,
    )


async def _dispatch_roll_stats(
    request_data: RollStatsRequest,
    stats_generator: StatsGenerator,
    current_user: User,
    profession_service: ProfessionService,
    max_attempts: int,
) -> RollStatsResponse:
    if request_data.profession_id is not None:
        return await _roll_stats_with_profession_preview(
            request_data, stats_generator, current_user, profession_service
        )
    if request_data.required_class is not None:
        return _roll_stats_with_class(request_data, stats_generator, max_attempts)
    return await _roll_stats_raw(request_data, stats_generator)


def _raise_roll_stats_validation_error(
    exc: ValidationError, current_user: User, request_data: RollStatsRequest
) -> NoReturn:
    status_code = 404 if "not found" in str(exc).lower() else 400
    raise LoggedHTTPException(
        status_code=status_code,
        detail=str(exc),
        user_id=str(current_user.id) if current_user else None,
        operation="roll_stats",
        profession_id=request_data.profession_id if request_data.profession_id else None,
    ) from exc


def _raise_roll_stats_error(exc: Exception, current_user: User, request_data: RollStatsRequest) -> NoReturn:
    if isinstance(exc, ValidationError):
        _raise_roll_stats_validation_error(exc, current_user, request_data)
    if isinstance(exc, ValueError):
        raise LoggedHTTPException(
            status_code=400,
            detail=f"Invalid profession: {str(exc)}",
            user_id=str(current_user.id) if current_user else None,
            operation="roll_stats",
            error=str(exc),
        ) from exc
    if isinstance(exc, LoggedHTTPException):
        raise exc
    raise LoggedHTTPException(
        status_code=500,
        detail=ErrorMessages.INTERNAL_ERROR,
        user_id=str(current_user.id) if current_user else None,
        operation="roll_stats",
    ) from exc


def _prepare_create_character_request(request: Request, current_user: User | None) -> None:
    from ..commands.admin_shutdown_command import get_shutdown_blocking_message, is_shutdown_pending

    user = _require_current_user(current_user, "create_character")
    # Cast: Starlette types request.app as Any; FastAPI instance is the runtime type.
    if request and is_shutdown_pending(cast(FastAPI, request.app)):
        raise LoggedHTTPException(
            status_code=503,
            detail=get_shutdown_blocking_message("character_creation"),
            user_id=str(user.id),
            operation="create_character",
            reason="server_shutdown",
        )
    try:
        character_creation_limiter.enforce_rate_limit(str(user.id))
    except RateLimitError as e:
        raise LoggedHTTPException(
            status_code=429,
            detail="Rate limit exceeded",
            user_id=str(user.id),
            rate_limit_type="character_creation",
        ) from e


@player_router.post("/roll-stats", response_model=RollStatsResponse)
async def roll_character_stats(
    request: Request,
    request_data: RollStatsRequest,
    current_user: Annotated[User, Depends(get_current_user)],
    stats_generator: Annotated[StatsGenerator, Depends(get_stats_generator)],
    profession_service: Annotated[ProfessionService, Depends(get_profession_service)],
) -> RollStatsResponse:
    """
    Roll random stats for character creation.

    This endpoint generates random character statistics using the specified method
    and validates them against class prerequisites if a required class is specified.

    Rate limited to 10 requests per minute per user.
    """
    user = _require_current_user(current_user, "roll_stats")
    _check_shutdown_status(request, user)
    _apply_rate_limiting_for_stats_roll(user)

    try:
        return await _dispatch_roll_stats(request_data, stats_generator, current_user, profession_service, 50)
    # Map all failures through _raise_roll_stats_error (ValidationError/ValueError/LoggedHTTPException/unknown).
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: endpoint must convert any roll failure into LoggedHTTPException; handler dispatches by type
        _raise_roll_stats_error(e, current_user, request_data)


@player_router.post("/create-character", response_model=CreateCharacterResponse)
async def create_character_with_stats(
    request: Request,
    request_data: CreateCharacterRequest,
    current_user: Annotated[User, Depends(get_current_user)],
    player_service: Annotated[PlayerService, Depends(get_player_service)],
    profession_service: Annotated[ProfessionService, Depends(get_profession_service)],
    skill_service: Annotated[SkillService, Depends(get_skill_service)],
) -> CreateCharacterResponse:
    """
    Create a new character with specific stats.

    This endpoint creates a new player character with the provided stats
    and automatically logs the user in with the new character.
    Server applies profession stat_modifiers to rolled stats; if occupation_slots
    and personal_interest are provided, sets player skills.

    Rate limited to 5 creations per 5 minutes per user.
    """
    _prepare_create_character_request(request, current_user)

    try:
        return await _execute_create_character(
            request_data, current_user, player_service, profession_service, skill_service
        )
    except HTTPException:
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
    stats: dict[str, object],
    current_user: Annotated[User, Depends(get_current_user)],
    stats_generator: Annotated[StatsGenerator, Depends(get_stats_generator)],
    class_name: str | None = None,
) -> ValidateStatsResponse:
    """
    Validate character stats against class prerequisites.

    This endpoint checks if the provided stats meet the requirements for a given class.
    """

    try:
        # Convert dict to Stats object
        stats_obj = Stats.model_validate(stats)

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
