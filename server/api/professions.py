"""
Profession management API endpoints for MythosMUD server.

This module handles all profession-related API operations including
retrieval of available professions and profession details.
"""

from typing import Any

from fastapi import APIRouter, Depends, Request

from ..auth.users import get_current_user
from ..error_types import ErrorMessages
from ..exceptions import LoggedHTTPException
from ..models.user import User
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.error_logging import create_context_from_request

logger = get_logger(__name__)

# Create profession router
profession_router = APIRouter(prefix="/professions", tags=["professions"])


@profession_router.get("/")
async def get_all_professions(
    request: Request,
    current_user: User = Depends(get_current_user),
) -> dict[str, Any]:
    """
    Retrieve all available professions for character creation with caching.

    Returns a list of all professions that are currently available
    for character creation, including their descriptions, flavor text,
    and stat requirements.
    """
    # Check if user is authenticated
    if not current_user:
        context = create_context_from_request(request)
        raise LoggedHTTPException(status_code=401, detail=ErrorMessages.AUTHENTICATION_REQUIRED, context=context)

    try:
        # Ensure request is available
        if not request:
            raise LoggedHTTPException(status_code=500, detail=ErrorMessages.INTERNAL_ERROR)

        # Use async persistence layer
        from ..async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        if not async_persistence:
            context = create_context_from_request(request)
            if current_user:
                context.user_id = str(current_user.id)
            context.metadata["operation"] = "get_all_professions"
            raise LoggedHTTPException(status_code=500, detail=ErrorMessages.INTERNAL_ERROR, context=context)

        # Query using async persistence method
        professions = await async_persistence.get_professions()

        # Convert profession objects to dictionaries
        profession_list = []
        for profession in professions:
            profession_dict = {
                "id": profession.id,
                "name": profession.name,
                "description": profession.description,
                "flavor_text": profession.flavor_text,
                "stat_requirements": profession.get_stat_requirements(),
                "mechanical_effects": profession.get_mechanical_effects(),
                "is_available": profession.is_available,
            }
            profession_list.append(profession_dict)

        return {"professions": profession_list}

    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: Profession retrieval errors unpredictable, must create error context
        context = create_context_from_request(request)
        if current_user:
            context.user_id = str(current_user.id)
        context.metadata["operation"] = "get_all_professions"
        logger.error("Error retrieving professions", error=str(e), extra={"context": context})
        raise LoggedHTTPException(status_code=500, detail=ErrorMessages.INTERNAL_ERROR, context=context) from e


@profession_router.get("/{profession_id}")
async def get_profession_by_id(
    profession_id: int,
    request: Request,
    current_user: User = Depends(get_current_user),
) -> dict[str, Any]:
    """
    Retrieve specific profession details by ID with caching.

    Returns detailed information about a specific profession including
    its description, flavor text, stat requirements, and mechanical effects.
    """
    # Check if user is authenticated
    if not current_user:
        context = create_context_from_request(request)
        raise LoggedHTTPException(status_code=401, detail=ErrorMessages.AUTHENTICATION_REQUIRED, context=context)

    try:
        # Ensure request is available
        if not request:
            raise LoggedHTTPException(status_code=500, detail=ErrorMessages.INTERNAL_ERROR)

        # Use async persistence layer
        from ..async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        if not async_persistence:
            context = create_context_from_request(request)
            if current_user:
                context.user_id = str(current_user.id)
            context.metadata["operation"] = "get_profession_by_id"
            context.metadata["profession_id"] = profession_id
            raise LoggedHTTPException(status_code=500, detail=ErrorMessages.INTERNAL_ERROR, context=context)

        # Query using async persistence method
        profession = await async_persistence.get_profession_by_id(profession_id)

        if not profession:
            context = create_context_from_request(request)
            if current_user:
                context.user_id = str(current_user.id)
            context.metadata["profession_id"] = profession_id
            raise LoggedHTTPException(status_code=404, detail=ErrorMessages.PROFESSION_NOT_FOUND, context=context)

        # Convert profession object to dictionary
        profession_dict = {
            "id": profession.id,
            "name": profession.name,
            "description": profession.description,
            "flavor_text": profession.flavor_text,
            "stat_requirements": profession.get_stat_requirements(),
            "mechanical_effects": profession.get_mechanical_effects(),
            "is_available": profession.is_available,
        }

        return profession_dict

    except LoggedHTTPException:
        # Re-raise LoggedHTTPException as-is
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: Profession selection errors unpredictable, must create error context
        context = create_context_from_request(request)
        if current_user:
            context.user_id = str(current_user.id)
        context.metadata["operation"] = "get_profession_by_id"
        context.metadata["profession_id"] = profession_id
        logger.error(
            "Error retrieving profession", profession_id=profession_id, error=str(e), extra={"context": context}
        )
        raise LoggedHTTPException(status_code=500, detail=ErrorMessages.INTERNAL_ERROR, context=context) from e
