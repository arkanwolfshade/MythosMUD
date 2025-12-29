"""
Player management API endpoints for MythosMUD server.

This module handles basic player CRUD operations and multi-character management.
"""

import uuid
from typing import Any

from fastapi import APIRouter, Depends
from fastapi import Request as FastAPIRequest

from ..auth.users import get_current_active_user, get_current_user
from ..dependencies import PlayerServiceDep, StatsGeneratorDep
from ..error_types import ErrorMessages
from ..exceptions import DatabaseError, LoggedHTTPException, ValidationError
from ..game.player_service import PlayerService
from ..game.stats_generator import StatsGenerator
from ..models.user import User
from ..schemas.player import PlayerRead
from ..schemas.player_requests import SelectCharacterRequest
from ..structured_logging.enhanced_logging_config import get_logger
from .player_helpers import create_error_context

logger = get_logger(__name__)

# Create player router
player_router = APIRouter(prefix="/api/players", tags=["players"])

# Import sub-modules to register their routes with player_router
# This must happen after player_router is created but before it's exported
# The imports trigger the decorators which register routes
from . import character_creation, player_effects, player_respawn  # noqa: E402

# Explicitly reference the imports to indicate they're used for side effects
_ = (character_creation, player_effects, player_respawn)  # noqa: F401


@player_router.post("/", response_model=PlayerRead)
async def create_player(
    name: str,
    request: FastAPIRequest,
    starting_room_id: str = "earth_arkhamcity_sanitarium_room_foyer_001",
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> dict[str, Any]:
    """Create a new player character."""
    try:
        player = await player_service.create_player(name, profession_id=0, starting_room_id=starting_room_id)
        return player.model_dump()
    except ValidationError:
        context = create_error_context(request, current_user, player_name=name, starting_room_id=starting_room_id)
        raise LoggedHTTPException(status_code=400, detail=ErrorMessages.INVALID_INPUT, context=context) from None


@player_router.get("/", response_model=list[PlayerRead])
async def list_players(
    _request: FastAPIRequest,
    _current_user: User | None = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> list[dict[str, Any]]:
    """Get a list of all players."""
    # Note: _current_user is optional for CORS testing, but endpoint requires auth for actual use
    if _current_user is None:
        from fastapi import HTTPException

        raise HTTPException(status_code=401, detail="Authentication required")
    result = await player_service.list_players()
    if not isinstance(result, list):
        raise RuntimeError(f"Expected list from player_service.list_players(), got {type(result).__name__}")
    # Convert all PlayerRead objects to dicts
    return [player.model_dump() for player in result]


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


@player_router.get("/available-classes")
async def get_available_classes(
    _current_user: User = Depends(get_current_user),
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
    except Exception as e:
        context = create_error_context(request, current_user, operation="get_user_characters")
        logger.error("Error getting user characters", error=str(e), user_id=current_user.id)
        raise LoggedHTTPException(status_code=500, detail=ErrorMessages.INTERNAL_ERROR, context=context) from e


@player_router.get("/{player_id}", response_model=PlayerRead)
async def get_player(
    player_id: uuid.UUID,
    request: FastAPIRequest,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> dict[str, Any]:
    """Get a specific player by ID."""
    player = await player_service.get_player_by_id(player_id)
    if not player:
        context = create_error_context(request, current_user, requested_player_id=player_id)
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context)

    return player.model_dump()


@player_router.get("/name/{player_name}", response_model=PlayerRead)
async def get_player_by_name(
    player_name: str,
    request: FastAPIRequest,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> dict[str, Any]:
    """Get a specific player by name."""
    player = await player_service.get_player_by_name(player_name)
    if not player:
        context = create_error_context(request, current_user, requested_player_name=player_name)
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context)

    return player.model_dump()


@player_router.delete("/{player_id}")
async def delete_player(
    player_id: uuid.UUID,
    request: FastAPIRequest,
    current_user: User = Depends(get_current_user),
    player_service: PlayerService = PlayerServiceDep,
) -> dict[str, str]:
    """Delete a player character."""
    try:
        success, message = await player_service.delete_player(player_id)
        if not success:
            context = create_error_context(request, current_user, requested_player_id=player_id)
            raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context)

        return {"message": message}
    except ValidationError as e:
        context = create_error_context(request, current_user, requested_player_id=player_id)
        raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PLAYER_NOT_FOUND, context=context) from e


@player_router.delete("/characters/{character_id}")
async def delete_character(
    character_id: str,
    request: FastAPIRequest,
    current_user: User = Depends(get_current_active_user),
    player_service: PlayerService = PlayerServiceDep,
) -> dict[str, Any]:
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

        return {"success": True, "message": message}
    except LoggedHTTPException:
        raise
    except Exception as e:
        context = create_error_context(request, current_user, operation="delete_character")
        logger.error("Error deleting character", error=str(e), character_id=character_id, user_id=current_user.id)
        raise LoggedHTTPException(status_code=500, detail=ErrorMessages.INTERNAL_ERROR, context=context) from e


@player_router.post("/select-character")
async def select_character(
    request_data: SelectCharacterRequest,
    request: FastAPIRequest,
    current_user: User = Depends(get_current_active_user),
    player_service: PlayerService = PlayerServiceDep,
) -> dict[str, Any]:
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
        # Convert character_id to UUID
        try:
            character_uuid = uuid.UUID(request_data.character_id)
        except ValueError:
            context = create_error_context(request, current_user, operation="select_character")
            raise LoggedHTTPException(status_code=400, detail="Invalid character ID format", context=context) from None

        # Get character and validate it belongs to user and is not deleted
        character = await player_service.get_player_by_id(character_uuid)
        if not character:
            context = create_error_context(request, current_user, operation="select_character")
            raise LoggedHTTPException(status_code=404, detail="Character not found", context=context)

        # Get the actual Player object to check is_deleted and user_id
        from ..async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        if not async_persistence:
            context = create_error_context(request, current_user, operation="select_character")
            raise LoggedHTTPException(status_code=500, detail="Persistence layer not available", context=context)

        player = await async_persistence.get_player_by_id(character_uuid)
        if not player:
            context = create_error_context(request, current_user, operation="select_character")
            raise LoggedHTTPException(status_code=404, detail="Character not found", context=context)

        # Validate character belongs to user
        if str(player.user_id) != str(current_user.id):
            context = create_error_context(request, current_user, operation="select_character")
            raise LoggedHTTPException(status_code=403, detail="Character does not belong to user", context=context)

        # Validate character is not deleted
        if player.is_deleted:
            context = create_error_context(request, current_user, operation="select_character")
            raise LoggedHTTPException(status_code=404, detail="Character has been deleted", context=context)

        # SINGLE-CHARACTER LOGIN: Disconnect all other characters for this user
        # Users can only be logged in with one character at a time
        try:
            # Get connection manager from app state
            connection_manager = getattr(request.app.state, "container", None)
            if connection_manager:
                connection_manager = getattr(connection_manager, "connection_manager", None)

            if connection_manager:
                # Get all active characters for this user
                active_characters = await async_persistence.get_active_players_by_user_id(str(current_user.id))

                # Disconnect connections for other characters
                disconnected_count = 0
                for other_character in active_characters:
                    if str(other_character.player_id) != str(character_uuid):
                        # Check if this character has active connections
                        other_character_id = uuid.UUID(str(other_character.player_id))
                        if other_character_id in connection_manager.player_websockets:
                            # Disconnect all connections for this character
                            try:
                                await connection_manager.disconnect_websocket(
                                    other_character_id, is_force_disconnect=True
                                )
                                disconnected_count += 1
                                logger.info(
                                    "Disconnected existing character connection for user",
                                    user_id=str(current_user.id),
                                    disconnected_character_id=str(other_character.player_id),
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
                                # Log error but continue with selection
                                logger.warning(
                                    "Failed to disconnect character connection",
                                    user_id=str(current_user.id),
                                    character_id=str(other_character.player_id),
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
            # Log error but don't fail character selection
            logger.warning(
                "Error disconnecting other character connections",
                user_id=str(current_user.id),
                selected_character_id=str(character_uuid),
                error=str(disconnect_error),
            )

        # Return character details
        return character.model_dump()
    except LoggedHTTPException:
        raise
    except Exception as e:
        context = create_error_context(request, current_user, operation="select_character")
        logger.error(
            "Error selecting character",
            error=str(e),
            character_id=request_data.character_id,
            user_id=current_user.id,
        )
        raise LoggedHTTPException(status_code=500, detail=ErrorMessages.INTERNAL_ERROR, context=context) from e
