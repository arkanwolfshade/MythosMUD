"""
Player management API endpoints for MythosMUD server.

This module handles basic player CRUD operations and multi-character management.
"""

# pylint: disable=too-many-lines  # Reason: Player API requires extensive endpoint handlers for player management, character operations, and state queries

import uuid
from typing import Any, cast

from fastapi import APIRouter, Depends
from fastapi import Request as FastAPIRequest

from ..app.game_tick_processing import get_current_tick, get_tick_interval
from ..auth.users import get_current_active_user, get_current_user
from ..dependencies import PlayerServiceDep, StatsGeneratorDep
from ..error_types import ErrorMessages
from ..exceptions import DatabaseError, LoggedHTTPException, ValidationError
from ..game.player_service import PlayerService
from ..game.stats_generator import StatsGenerator
from ..models.user import User
from ..realtime.login_grace_period import (
    get_login_grace_period_remaining,
    is_player_in_login_grace_period,
    start_login_grace_period,
)
from ..schemas.players import (
    AvailableClassesResponse,
    DeleteCharacterResponse,
    LoginGracePeriodResponse,
    MessageResponse,
    PlayerRead,
    SelectCharacterRequest,
)
from ..structured_logging.enhanced_logging_config import get_logger
from .player_helpers import create_error_context

logger = get_logger(__name__)

# Create player router
player_router = APIRouter(prefix="/api/players", tags=["players"])

# Import sub-modules to register their routes with player_router
# This must happen after player_router is created but before it's exported
# The imports trigger the decorators which register routes
# pylint: disable=wrong-import-position  # noqa: E402  # Reason: Imports must occur after router creation to trigger route registration decorators
from . import (  # noqa: E402  # pylint: disable=wrong-import-position  # Reason: Imports must occur after router creation to trigger route registration decorators
    character_creation,
    player_effects,
    player_respawn,
)

# Explicitly reference the imports to indicate they're used for side effects
_ = (character_creation, player_effects, player_respawn)  # noqa: F401  # pylint: disable=unused-import  # Reason: Imports are used for side effects (route registration), not direct usage, assignment prevents unused import warning


@player_router.post("/", response_model=PlayerRead)
async def create_player(
    name: str,
    request: FastAPIRequest,
    starting_room_id: str = "earth_arkhamcity_sanitarium_room_foyer_001",
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> PlayerRead:
    """Create a new player character.

    :param name: Display name for the new character.
    :param request: FastAPI request (for error context).
    :param starting_room_id: Room ID where the character will spawn.
    :param current_user: Authenticated user (injected).
    :param player_service: Player service (injected).
    :return: The created player as PlayerRead.
    :raises LoggedHTTPException: On validation error (400) or auth failure (401).
    """
    try:
        player = await player_service.create_player(name, profession_id=0, starting_room_id=starting_room_id)
        return player
    except ValidationError:
        context = create_error_context(request, current_user, player_name=name, starting_room_id=starting_room_id)
        raise LoggedHTTPException(status_code=400, detail=ErrorMessages.INVALID_INPUT, context=context) from None


@player_router.get("/", response_model=list[PlayerRead])
async def list_players(
    _request: FastAPIRequest,
    _current_user: User | None = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> list[PlayerRead]:
    """Get a list of all players.

    :param _request: FastAPI request (for error context).
    :param _current_user: Authenticated user if any (injected).
    :param player_service: Player service (injected).
    :return: List of all players as PlayerRead.
    :raises LoggedHTTPException: If not authenticated (401).
    """
    # Note: _current_user is optional for CORS testing, but endpoint requires auth for actual use
    if _current_user is None:
        context = create_error_context(_request, _current_user, operation="list_players")
        raise LoggedHTTPException(status_code=401, detail="Authentication required", context=context)
    result = await player_service.list_players()
    if not isinstance(result, list):
        raise RuntimeError(f"Expected list from player_service.list_players(), got {type(result).__name__}")
    return result


def get_class_description(class_name: str) -> str:
    """Get a description for a character class."""
    descriptions = {
        "investigator": "A skilled researcher and detective, specializing in uncovering mysteries and gathering information.",
        "occultist": "A scholar of forbidden knowledge, capable of wielding dangerous magic at the cost of lucidity.",
        "survivor": "A resilient individual who has learned to endure the horrors of the Mythos through sheer determination.",
        "cultist": "A charismatic leader who can manipulate others and has ties to dark organizations.",
        "academic": "A brilliant researcher and scholar, specializing in historical and scientific knowledge.",
        "detective": "A sharp-witted investigator with exceptional intuition and deductive reasoning skills.",
    }
    return descriptions.get(class_name, "A mysterious character with unknown capabilities.")


@player_router.get("/available-classes", response_model=AvailableClassesResponse)
async def get_available_classes(
    _current_user: User = Depends(get_current_user),
    stats_generator: StatsGenerator = StatsGeneratorDep,
) -> AvailableClassesResponse:
    """
    Get information about all available character classes and their prerequisites.
    """
    from server.schemas.players.class_definition import ClassDefinition

    class_info = {}
    for class_name, prerequisites in stats_generator.CLASS_PREREQUISITES.items():
        class_info[class_name] = ClassDefinition(
            prerequisites={attr.value: min_value for attr, min_value in prerequisites.items()},
            description=get_class_description(class_name),
        )

    return AvailableClassesResponse(
        classes=class_info, stat_range={"min": stats_generator.MIN_STAT, "max": stats_generator.MAX_STAT}
    )


@player_router.get("/characters", response_model=list[PlayerRead])
async def get_user_characters(
    request: FastAPIRequest,
    current_user: User = Depends(get_current_active_user),
    player_service: PlayerService = PlayerServiceDep,
) -> list[PlayerRead]:
    """
    Get all active characters for the current user.

    MULTI-CHARACTER: Returns list of active (non-deleted) characters for the authenticated user.

    Returns:
        list[PlayerRead]: List of active character data
    """
    if not current_user:
        context = create_error_context(request, current_user)
        raise LoggedHTTPException(status_code=401, detail=ErrorMessages.AUTHENTICATION_REQUIRED, context=context)

    try:
        characters = await player_service.get_user_characters(current_user.id)
        return characters
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Character retrieval errors unpredictable, must create error context
        context = create_error_context(request, current_user, operation="get_user_characters")
        logger.error("Error getting user characters", error=str(e), user_id=current_user.id)
        raise LoggedHTTPException(status_code=500, detail=ErrorMessages.INTERNAL_ERROR, context=context) from e


@player_router.get("/{player_id}", response_model=PlayerRead)
async def get_player(
    player_id: uuid.UUID,
    request: FastAPIRequest,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> PlayerRead:
    """Get a specific player by ID."""
    player = await player_service.get_player_by_id(player_id)
    if not player:
        context = create_error_context(request, current_user, requested_player_id=player_id)
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context)

    return player


@player_router.get("/name/{player_name}", response_model=PlayerRead)
async def get_player_by_name(
    player_name: str,
    request: FastAPIRequest,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> PlayerRead:
    """Get a specific player by name."""
    player = await player_service.get_player_by_name(player_name)
    if not player:
        context = create_error_context(request, current_user, requested_player_name=player_name)
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context)

    return player


@player_router.delete("/{player_id}", response_model=MessageResponse)
async def delete_player(
    player_id: uuid.UUID,
    request: FastAPIRequest,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> MessageResponse:
    """Delete a player character."""
    try:
        success, message = await player_service.delete_player(player_id)
        if not success:
            context = create_error_context(request, current_user, requested_player_id=player_id)
            raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context)

        return MessageResponse(message=message)
    except ValidationError as e:
        context = create_error_context(request, current_user, requested_player_id=player_id)
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context) from e


@player_router.delete("/characters/{character_id}", response_model=DeleteCharacterResponse)
async def delete_character(
    character_id: str,
    request: FastAPIRequest,
    current_user: User = Depends(get_current_active_user),
    player_service: PlayerService = PlayerServiceDep,
) -> DeleteCharacterResponse:
    """
    Soft delete a character.

    MULTI-CHARACTER: Soft deletes a character (sets is_deleted=True) belonging to the current user.
    Character data is preserved but the character is hidden from selection.

    Args:
        character_id: Character ID (player_id) to delete

    Returns:
        dict: Success message

    Raises:
        HTTPException: If character not found or doesn't belong to user
    """
    if not current_user:
        context = create_error_context(request, current_user)
        raise LoggedHTTPException(status_code=401, detail=ErrorMessages.AUTHENTICATION_REQUIRED, context=context)

    try:
        # Convert character_id to UUID
        try:
            character_uuid = uuid.UUID(character_id)
        except ValueError:
            context = create_error_context(request, current_user, operation="delete_character")
            raise LoggedHTTPException(status_code=400, detail="Invalid character ID format", context=context) from None

        success, message = await player_service.soft_delete_character(character_uuid, current_user.id)
        if not success:
            context = create_error_context(request, current_user, operation="delete_character")
            raise LoggedHTTPException(status_code=404, detail=message, context=context)

        return DeleteCharacterResponse(success=True, message=message)
    except LoggedHTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Character deletion errors unpredictable, must create error context
        context = create_error_context(request, current_user, operation="delete_character")
        logger.error("Error deleting character", error=str(e), character_id=character_id, user_id=current_user.id)
        raise LoggedHTTPException(status_code=500, detail=ErrorMessages.INTERNAL_ERROR, context=context) from e


def _validate_character_id(character_id: str, request: FastAPIRequest, current_user: User) -> uuid.UUID:
    """
    Validate and convert character ID string to UUID.

    Args:
        character_id: Character ID string to validate
        request: FastAPI request object
        current_user: Current user object

    Returns:
        uuid.UUID: Validated character UUID

    Raises:
        LoggedHTTPException: If character ID format is invalid
    """
    try:
        return uuid.UUID(character_id)
    except ValueError:
        context = create_error_context(request, current_user, operation="select_character")
        raise LoggedHTTPException(status_code=400, detail="Invalid character ID format", context=context) from None


async def _validate_character_access(
    character_uuid: uuid.UUID, current_user: User, request: FastAPIRequest, player_service: PlayerService
) -> Any:
    """
    Validate character exists, belongs to user, and is not deleted.

    Delegates to PlayerService.validate_character_access() for business logic,
    then converts validation result to appropriate HTTP exceptions.

    Args:
        character_uuid: Character UUID to validate
        current_user: Current user object
        request: FastAPI request object
        player_service: Player service instance

    Returns:
        Character object from player service

    Raises:
        LoggedHTTPException: If character not found, deleted, or doesn't belong to user
    """
    is_valid, character, error_message = await player_service.validate_character_access(character_uuid, current_user.id)

    if not is_valid:
        context = create_error_context(request, current_user, operation="select_character")
        # Determine appropriate status code based on error message
        if "not found" in error_message.lower():
            status_code = 404
        elif "does not belong" in error_message.lower():
            status_code = 403
        elif "deleted" in error_message.lower():
            status_code = 404
        else:
            status_code = 400
        raise LoggedHTTPException(status_code=status_code, detail=error_message, context=context)

    return character


def _get_connection_manager(request: FastAPIRequest) -> Any:
    """
    Extract connection manager from request app state.

    Args:
        request: FastAPI request object

    Returns:
        Connection manager instance or None if not available
    """
    container = getattr(request.app.state, "container", None)
    if container:
        return getattr(container, "connection_manager", None)
    return None


async def _disconnect_other_characters(
    character_uuid: uuid.UUID, current_user: User, connection_manager: Any, player_service: PlayerService
) -> None:
    """
    Disconnect all other active characters for the user.

    SINGLE-CHARACTER LOGIN: Users can only be logged in with one character at a time.

    Args:
        character_uuid: UUID of the character being selected
        current_user: Current user object
        connection_manager: Connection manager instance
        player_service: Player service instance for getting user characters
    """
    if not connection_manager:
        return

    try:
        # Get all active characters for this user using PlayerService
        active_characters = await player_service.get_user_characters(current_user.id)

        # Disconnect connections for other characters
        disconnected_count = 0
        for other_character in active_characters:
            if str(other_character.id) != str(character_uuid):
                other_character_id = uuid.UUID(str(other_character.id))
                if other_character_id in connection_manager.player_websockets:
                    try:
                        await connection_manager.disconnect_websocket(other_character_id, is_force_disconnect=True)
                        disconnected_count += 1
                        logger.info(
                            "Disconnected existing character connection for user (debug: mid-run drops)",
                            disconnect_reason="select_character_other",
                            user_id=str(current_user.id),
                            disconnected_character_id=str(other_character.id),
                            disconnected_character_name=other_character.name,
                            selected_character_id=str(character_uuid),
                        )
                    except (
                        TimeoutError,
                        DatabaseError,
                        AttributeError,
                        RuntimeError,
                        ValueError,
                        TypeError,
                    ) as disconnect_error:
                        logger.warning(
                            "Failed to disconnect character connection",
                            user_id=str(current_user.id),
                            character_id=str(other_character.id),
                            error=str(disconnect_error),
                        )

        if disconnected_count > 0:
            logger.info(
                "Disconnected other character connections for user",
                user_id=str(current_user.id),
                selected_character_id=str(character_uuid),
                disconnected_count=disconnected_count,
            )
    except (TimeoutError, DatabaseError, AttributeError, RuntimeError, ValueError, TypeError) as disconnect_error:
        logger.warning(
            "Error disconnecting other character connections",
            user_id=str(current_user.id),
            selected_character_id=str(character_uuid),
            error=str(disconnect_error),
        )


@player_router.post("/select-character", response_model=PlayerRead)
async def select_character(
    request_data: SelectCharacterRequest,
    request: FastAPIRequest,
    current_user: User = Depends(get_current_active_user),
    player_service: PlayerService = PlayerServiceDep,
) -> PlayerRead:
    """
    Select a character to play.

    MULTI-CHARACTER: Validates that the character belongs to the user and is not deleted,
    then returns character details for game connection.

    Args:
        request_data: Character selection request containing character_id

    Returns:
        dict: Character details for game connection

    Raises:
        HTTPException: If character not found, deleted, or doesn't belong to user
    """
    if not current_user:
        context = create_error_context(request, current_user)
        raise LoggedHTTPException(status_code=401, detail=ErrorMessages.AUTHENTICATION_REQUIRED, context=context)

    try:
        character_uuid = _validate_character_id(request_data.character_id, request, current_user)
        character = await _validate_character_access(character_uuid, current_user, request, player_service)

        # SINGLE-CHARACTER LOGIN: Disconnect all other characters for this user
        connection_manager = _get_connection_manager(request)
        if connection_manager:
            await _disconnect_other_characters(character_uuid, current_user, connection_manager, player_service)

        return cast("PlayerRead", character)
    except LoggedHTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Character selection errors unpredictable, must create error context
        context = create_error_context(request, current_user, operation="select_character")
        logger.error(
            "Error selecting character",
            error=str(e),
            character_id=request_data.character_id,
            user_id=current_user.id,
        )
        raise LoggedHTTPException(status_code=500, detail=ErrorMessages.INTERNAL_ERROR, context=context) from e


async def _validate_player_for_grace_period(
    player_id: uuid.UUID, current_user: User, request: FastAPIRequest, player_service: PlayerService
) -> Any:
    """
    Validate player exists and belongs to user for grace period operations.

    Delegates to PlayerService.validate_character_access() for business logic,
    then converts validation result to appropriate HTTP exceptions.

    Args:
        player_id: Player UUID to validate
        current_user: Current user object
        request: FastAPI request object
        player_service: Player service instance

    Returns:
        PlayerRead object

    Raises:
        LoggedHTTPException: If player not found, persistence unavailable, or doesn't belong to user
    """
    is_valid, character, error_message = await player_service.validate_character_access(player_id, current_user.id)

    if not is_valid:
        context = create_error_context(request, current_user, operation="start_login_grace_period")
        # Determine appropriate status code based on error message
        if "not found" in error_message.lower():
            status_code = 404
        elif "does not belong" in error_message.lower():
            status_code = 403
        elif "deleted" in error_message.lower():
            status_code = 404
        else:
            status_code = 400
        raise LoggedHTTPException(status_code=status_code, detail=error_message, context=context)

    return character


async def _end_combat_for_grace_period(player_id: uuid.UUID) -> None:
    """
    End combat for player entering login grace period.

    Args:
        player_id: Player UUID
    """
    # Lazy import to avoid circular dependency with combat_service
    from ..services.combat_service import (
        get_combat_service,  # noqa: E402  # pylint: disable=wrong-import-position  # Reason: Lazy import inside function to break circular dependency between API and combat service modules
    )

    combat_service = get_combat_service()
    if not combat_service:
        return

    combat = await combat_service.get_combat_by_participant(player_id)
    if not combat:
        return

    try:
        await combat_service.end_combat(combat.combat_id, "Player entered login grace period")
        logger.info(
            "Ended combat for player entering login grace period",
            player_id=player_id,
            combat_id=combat.combat_id,
        )
    except Exception as combat_error:  # pylint: disable=broad-exception-caught  # noqa: B904        # Log but don't fail - combat cleanup is best effort
        logger.warning(
            "Error ending combat for login grace period",
            player_id=player_id,
            combat_id=combat.combat_id,
            error=str(combat_error),
        )


@player_router.post("/{player_id}/start-login-grace-period", response_model=LoginGracePeriodResponse)
async def start_login_grace_period_endpoint(
    player_id: uuid.UUID,
    request: FastAPIRequest,
    current_user: User = Depends(get_current_active_user),
    player_service: PlayerService = PlayerServiceDep,
) -> LoginGracePeriodResponse:
    """
    Start login grace period for a player after MOTD dismissal.

    This endpoint is called when a player clicks through the MOTD screen
    to enter the game, starting their 10-second grace period of immunity.

    Args:
        player_id: The player's ID
        request: FastAPI request object
        current_user: Current authenticated user

    Returns:
        dict: Success status and grace period details

    Raises:
        HTTPException: If player not found, doesn't belong to user, or already in grace period
    """
    try:
        connection_manager = _get_connection_manager(request)
        if not connection_manager:
            context = create_error_context(request, current_user, operation="start_login_grace_period")
            raise LoggedHTTPException(status_code=500, detail="Connection manager not available", context=context)

        character = await _validate_player_for_grace_period(player_id, current_user, request, player_service)

        # Check if already in grace period
        if is_player_in_login_grace_period(player_id, connection_manager):
            remaining = get_login_grace_period_remaining(player_id, connection_manager)
            return LoginGracePeriodResponse(
                success=True,
                message="Login grace period already active",
                grace_period_active=True,
                grace_period_remaining=remaining,
            )

        # Remove player from combat if they're in combat
        await _end_combat_for_grace_period(player_id)

        # Start login grace period (effects system: pass async_persistence and tick getters)
        container = getattr(request.app.state, "container", None)
        async_persistence = getattr(container, "async_persistence", None) if container else None
        await start_login_grace_period(
            player_id,
            connection_manager,
            async_persistence=async_persistence,
            get_current_tick=get_current_tick,
            get_tick_interval=get_tick_interval,
        )
        remaining = get_login_grace_period_remaining(player_id, connection_manager)
        logger.info(
            "Login grace period started",
            player_id=player_id,
            player_name=character.name,
            remaining=remaining,
        )

        return LoginGracePeriodResponse(
            success=True,
            message="Login grace period started",
            grace_period_active=True,
            grace_period_remaining=remaining,
        )

    except LoggedHTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Login grace period errors unpredictable (service, database, validation), must create error context and return user-friendly message
        context = create_error_context(request, current_user, operation="start_login_grace_period")
        logger.error(
            "Error starting login grace period",
            error=str(e),
            player_id=player_id,
            user_id=current_user.id if current_user else None,
            exc_info=True,
        )
        raise LoggedHTTPException(
            status_code=500, detail=f"Error starting login grace period: {str(e)}", context=context
        ) from e
