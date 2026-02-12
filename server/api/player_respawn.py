"""
Player respawn API endpoints.

This module handles endpoints for respawning players after death or delirium.
"""

from typing import TYPE_CHECKING

from fastapi import Depends, Request

from ..auth.users import get_current_active_user
from ..dependencies import AsyncPersistenceDep, PlayerRespawnServiceDep, PlayerServiceDep
from ..exceptions import LoggedHTTPException, ValidationError
from ..game.player_service import PlayerService
from ..models.user import User
from ..schemas.players import RespawnResponse
from ..structured_logging.enhanced_logging_config import get_logger
from .player_helpers import create_error_context
from .players import player_router

if TYPE_CHECKING:
    from ..async_persistence import AsyncPersistenceLayer
    from ..services.player_respawn_service import PlayerRespawnService

logger = get_logger(__name__)


def _handle_respawn_validation_error(e: ValidationError, request: Request, current_user: User) -> None:
    """
    Convert ValidationError to appropriate HTTPException for respawn.

    Args:
        e: ValidationError exception
        request: FastAPI Request object
        current_user: Current authenticated user

    Raises:
        LoggedHTTPException: With appropriate status code based on error message
    """
    context = create_error_context(request, current_user)
    error_message = str(e).lower()

    if "not found" in error_message:
        raise LoggedHTTPException(status_code=404, detail="Player not found", context=context) from e
    if "must be dead" in error_message:
        raise LoggedHTTPException(
            status_code=403,
            detail="Player must be dead to respawn (DP must be -10 or below)",
            context=context,
        ) from e
    raise LoggedHTTPException(status_code=500, detail="Failed to respawn player", context=context) from e


def _handle_delirium_respawn_validation_error(e: ValidationError, request: Request, current_user: User) -> None:
    """
    Convert ValidationError to appropriate HTTPException for delirium respawn.

    Args:
        e: ValidationError exception
        request: FastAPI Request object
        current_user: Current authenticated user

    Raises:
        LoggedHTTPException: With appropriate status code based on error message
    """
    context = create_error_context(request, current_user)
    error_message = str(e).lower()

    if "not found" in error_message:
        raise LoggedHTTPException(status_code=404, detail="Player not found", context=context) from e
    if "must be delirious" in error_message or "lucidity" in error_message:
        raise LoggedHTTPException(
            status_code=403,
            detail="Player must be delirious to respawn (lucidity must be -10 or below)",
            context=context,
        ) from e
    raise LoggedHTTPException(status_code=500, detail="Failed to respawn player from delirium", context=context) from e


@player_router.post("/respawn-delirium", response_model=RespawnResponse)
async def respawn_player_from_delirium(
    request: Request,
    current_user: User = Depends(get_current_active_user),
    player_service: PlayerService = PlayerServiceDep,
    respawn_service: "PlayerRespawnService" = PlayerRespawnServiceDep,
    persistence: "AsyncPersistenceLayer" = AsyncPersistenceDep,
) -> RespawnResponse:
    """
    Respawn a delirious player at the Sanitarium with restored lucidity.

    This endpoint handles player respawn after delirium, moving them to
    the Sanitarium and restoring their lucidity to 10.

    Rate limited to 1 request per 5 seconds per user.

    Returns:
        dict: Respawn room data and updated player state

    Raises:
        HTTPException(403): Player is not delirious
        HTTPException(404): Player not found
        HTTPException(500): Respawn failed
    """
    from ..database import get_async_session

    logger.info("Delirium respawn request received", user_id=current_user.id, username=current_user.username)

    try:
        async for session in get_async_session():
            try:
                # Use service layer method to handle delirium respawn logic
                result = await player_service.respawn_player_from_delirium_by_user_id(
                    user_id=str(current_user.id),
                    session=session,
                    respawn_service=respawn_service,
                    persistence=persistence,
                )
                return RespawnResponse(**result)
            except ValidationError as e:
                _handle_delirium_respawn_validation_error(e, request, current_user)
            except LoggedHTTPException:
                raise
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Respawn errors unpredictable, must create error context
                context = create_error_context(request, current_user, operation="respawn_player_from_delirium")
                logger.error(
                    "Error in delirium respawn endpoint",
                    error=str(e),
                    exc_info=True,
                    context=context.to_dict(),
                )
                raise LoggedHTTPException(
                    status_code=500, detail="Failed to process delirium respawn request", context=context
                ) from e

        # This should never be reached, but mypy needs it
        raise LoggedHTTPException(
            status_code=500,
            detail="No database session available",
            context=create_error_context(request, current_user),
        )

    except LoggedHTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Respawn errors unpredictable, must create error context
        context = create_error_context(request, current_user, operation="respawn_player_from_delirium")
        logger.error(
            "Unexpected error in delirium respawn endpoint",
            error=str(e),
            exc_info=True,
            context=context.to_dict(),
        )
        raise LoggedHTTPException(
            status_code=500, detail="Unexpected error during delirium respawn", context=context
        ) from e


@player_router.post("/respawn", response_model=RespawnResponse)
async def respawn_player(
    request: Request,
    current_user: User = Depends(get_current_active_user),
    player_service: PlayerService = PlayerServiceDep,
    respawn_service: "PlayerRespawnService" = PlayerRespawnServiceDep,
    persistence: "AsyncPersistenceLayer" = AsyncPersistenceDep,
) -> RespawnResponse:
    """
    Respawn a dead player at their respawn location with full DP.

    This endpoint handles player resurrection after death, moving them from
    limbo to their designated respawn room and restoring their DP to 100.

    Rate limited to 1 request per 5 seconds per user.

    Returns:
        dict: Respawn room data and updated player state

    Raises:
        HTTPException(403): Player is not dead
        HTTPException(404): Player not found
        HTTPException(500): Respawn failed
    """
    from ..database import get_async_session

    logger.info("Respawn request received", user_id=current_user.id, username=current_user.username)

    try:
        async for session in get_async_session():
            try:
                # Use service layer method to handle respawn logic
                result = await player_service.respawn_player_by_user_id(
                    user_id=str(current_user.id),
                    session=session,
                    respawn_service=respawn_service,
                    persistence=persistence,
                )
                return RespawnResponse(**result)
            except ValidationError as e:
                _handle_respawn_validation_error(e, request, current_user)
            except LoggedHTTPException:
                raise
            except Exception as e:
                context = create_error_context(request, current_user, operation="respawn_player")
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
            context=create_error_context(request, current_user),
        )

    except LoggedHTTPException:
        raise
    except Exception as e:
        context = create_error_context(request, current_user, operation="respawn_player")
        logger.error(
            "Unexpected error in respawn endpoint",
            error=str(e),
            exc_info=True,
            context=context.to_dict(),
        )
        raise LoggedHTTPException(status_code=500, detail="Unexpected error during respawn", context=context) from e
