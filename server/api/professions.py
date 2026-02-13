"""
Profession management API endpoints for MythosMUD server.

This module handles all profession-related API operations including
retrieval of available professions and profession details.
"""

from fastapi import APIRouter, Depends, Request

from ..auth.users import get_current_user
from ..dependencies import ProfessionServiceDep
from ..error_types import ErrorMessages
from ..exceptions import LoggedHTTPException
from ..game.profession_service import ProfessionService
from ..models.user import User
from ..schemas.players import ProfessionListResponse, ProfessionResponse
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

# Create profession router
profession_router = APIRouter(prefix="/professions", tags=["professions"])


@profession_router.get("/", response_model=ProfessionListResponse)
async def get_all_professions(
    _request: Request,
    current_user: User = Depends(get_current_user),
    profession_service: ProfessionService = ProfessionServiceDep,
) -> ProfessionListResponse:
    """Retrieve all available professions for character creation with caching.

    :param _request: FastAPI request (unused; kept for dependency injection).
    :param current_user: Authenticated user (injected).
    :param profession_service: Profession service (injected).
    :return: List of professions with descriptions and stat requirements.
    :raises LoggedHTTPException: If not authenticated (401) or on server error (500).
    """
    # Check if user is authenticated
    if not current_user:
        raise LoggedHTTPException(
            status_code=401,
            detail=ErrorMessages.AUTHENTICATION_REQUIRED,
            operation="get_all_professions",
        )

    try:
        # Get professions using ProfessionService
        profession_list = await profession_service.get_all_professions_dict()
        response_obj = ProfessionListResponse(professions=profession_list)
        return response_obj

    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Profession retrieval errors unpredictable, must create error context
        logger.error("Error retrieving professions", error=str(e))
        raise LoggedHTTPException(
            status_code=500,
            detail=ErrorMessages.INTERNAL_ERROR,
            user_id=str(current_user.id) if current_user else None,
            operation="get_all_professions",
        ) from e


@profession_router.get("/{profession_id}", response_model=ProfessionResponse)
async def get_profession_by_id(
    profession_id: int,
    _request: Request,
    current_user: User = Depends(get_current_user),
    profession_service: ProfessionService = ProfessionServiceDep,
) -> ProfessionResponse:
    """Retrieve specific profession details by ID with caching.

    :param profession_id: ID of the profession to fetch.
    :param _request: FastAPI request (unused; kept for dependency injection).
    :param current_user: Authenticated user (injected).
    :param profession_service: Profession service (injected).
    :return: Profession details including description and stat requirements.
    :raises LoggedHTTPException: If not authenticated (401), not found (404), or error (500).
    """
    # Check if user is authenticated
    if not current_user:
        raise LoggedHTTPException(
            status_code=401,
            detail=ErrorMessages.AUTHENTICATION_REQUIRED,
            operation="get_profession_by_id",
        )

    try:
        # Get profession using ProfessionService
        profession_dict = await profession_service.get_profession_by_id_dict(profession_id)

        if not profession_dict:
            raise LoggedHTTPException(
                status_code=404,
                detail=ErrorMessages.PROFESSION_NOT_FOUND,
                user_id=str(current_user.id) if current_user else None,
                profession_id=profession_id,
            )

        return ProfessionResponse(**profession_dict)

    except LoggedHTTPException:
        # Re-raise LoggedHTTPException as-is
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Profession selection errors unpredictable, must create error context
        logger.error("Error retrieving profession", profession_id=profession_id, error=str(e))
        raise LoggedHTTPException(
            status_code=500,
            detail=ErrorMessages.INTERNAL_ERROR,
            user_id=str(current_user.id) if current_user else None,
            operation="get_profession_by_id",
            profession_id=profession_id,
        ) from e
