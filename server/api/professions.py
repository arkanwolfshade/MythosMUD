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
from ..utils.error_logging import create_context_from_request

logger = get_logger(__name__)

# Create profession router
profession_router = APIRouter(prefix="/professions", tags=["professions"])


@profession_router.get("/", response_model=ProfessionListResponse)
async def get_all_professions(
    request: Request,
    current_user: User = Depends(get_current_user),
    profession_service: ProfessionService = ProfessionServiceDep,
) -> ProfessionListResponse:
    """Retrieve all available professions for character creation with caching.

    :param request: FastAPI request (for error context).
    :param current_user: Authenticated user (injected).
    :param profession_service: Profession service (injected).
    :return: List of professions with descriptions and stat requirements.
    :raises LoggedHTTPException: If not authenticated (401) or on server error (500).
    """
    # Check if user is authenticated
    if not current_user:
        context = create_context_from_request(request)
        raise LoggedHTTPException(status_code=401, detail=ErrorMessages.AUTHENTICATION_REQUIRED, context=context)

    try:
        # Get professions using ProfessionService
        profession_list = await profession_service.get_all_professions_dict()
        response_obj = ProfessionListResponse(professions=profession_list)
        return response_obj

    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Profession retrieval errors unpredictable, must create error context
        context = create_context_from_request(request)
        if current_user:
            context.user_id = str(current_user.id)
        context.metadata["operation"] = "get_all_professions"
        logger.error("Error retrieving professions", error=str(e), extra={"context": context})
        raise LoggedHTTPException(status_code=500, detail=ErrorMessages.INTERNAL_ERROR, context=context) from e


@profession_router.get("/{profession_id}", response_model=ProfessionResponse)
async def get_profession_by_id(
    profession_id: int,
    request: Request,
    current_user: User = Depends(get_current_user),
    profession_service: ProfessionService = ProfessionServiceDep,
) -> ProfessionResponse:
    """Retrieve specific profession details by ID with caching.

    :param profession_id: ID of the profession to fetch.
    :param request: FastAPI request (for error context).
    :param current_user: Authenticated user (injected).
    :param profession_service: Profession service (injected).
    :return: Profession details including description and stat requirements.
    :raises LoggedHTTPException: If not authenticated (401), not found (404), or error (500).
    """
    # Check if user is authenticated
    if not current_user:
        context = create_context_from_request(request)
        raise LoggedHTTPException(status_code=401, detail=ErrorMessages.AUTHENTICATION_REQUIRED, context=context)

    try:
        # Get profession using ProfessionService
        profession_dict = await profession_service.get_profession_by_id_dict(profession_id)

        if not profession_dict:
            context = create_context_from_request(request)
            if current_user:
                context.user_id = str(current_user.id)
            context.metadata["profession_id"] = profession_id
            raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PROFESSION_NOT_FOUND, context=context)

        return ProfessionResponse(**profession_dict)

    except LoggedHTTPException:
        # Re-raise LoggedHTTPException as-is
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Profession selection errors unpredictable, must create error context
        context = create_context_from_request(request)
        if current_user:
            context.user_id = str(current_user.id)
        context.metadata["operation"] = "get_profession_by_id"
        context.metadata["profession_id"] = profession_id
        logger.error(
            "Error retrieving profession", profession_id=profession_id, error=str(e), extra={"context": context}
        )
        raise LoggedHTTPException(status_code=500, detail=ErrorMessages.INTERNAL_ERROR, context=context) from e
