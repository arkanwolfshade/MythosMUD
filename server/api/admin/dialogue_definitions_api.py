"""Admin CRUD for dialogue_definitions (#583)."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Request, status

from ...auth.users import get_current_user
from ...exceptions import LoggedHTTPException
from ...models.user import User
from ...persistence.repositories.dialogue_definition_repository import DialogueDefinitionRepository
from ...services.admin_auth_service import AdminAction, get_admin_auth_service
from ...structured_logging.enhanced_logging_config import get_logger
from .dialogue_schemas import (
    DialogueDefinitionCreate,
    DialogueDefinitionResponse,
    DialogueDefinitionUpdate,
)
from .npc_router_core import validate_admin_permission

logger = get_logger(__name__)

dialogue_router = APIRouter(prefix="/admin/dialogue", tags=["admin", "dialogue"])
logger.info("Dialogue Admin API router initialized")


def to_response(row: object) -> DialogueDefinitionResponse:
    """Map repository model to response schema."""
    return DialogueDefinitionResponse(
        id=getattr(row, "id", "") or "",
        definition=dict(getattr(row, "definition", None) or {}),
        npc_definition_id=getattr(row, "npc_definition_id", None),
        created_at=getattr(row, "created_at", None),
        updated_at=getattr(row, "updated_at", None),
    )


@dialogue_router.get("/definitions", response_model=list[DialogueDefinitionResponse])
async def list_dialogue_definitions(
    request: Request,
    current_user: User | None = Depends(get_current_user),
) -> list[DialogueDefinitionResponse]:
    """List all dialogue definitions."""
    try:
        validate_admin_permission(current_user, AdminAction.LIST_DIALOGUE_DEFINITIONS, request)
        auth_service = get_admin_auth_service()
        logger.info("Dialogue definitions requested", user=auth_service.get_username(current_user))
        rows = await DialogueDefinitionRepository().list_all()
        return [to_response(row) for row in rows]
    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: admin list errors unpredictable
        logger.error("Error listing dialogue definitions", error=str(e))
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error listing dialogue definitions",
        ) from e


@dialogue_router.get("/definitions/{dialogue_id}", response_model=DialogueDefinitionResponse)
async def get_dialogue_definition(
    dialogue_id: str,
    request: Request,
    current_user: User | None = Depends(get_current_user),
) -> DialogueDefinitionResponse:
    """Get one dialogue definition by id."""
    try:
        validate_admin_permission(current_user, AdminAction.LIST_DIALOGUE_DEFINITIONS, request)
        row = await DialogueDefinitionRepository().get_by_id(dialogue_id)
        if not row:
            raise LoggedHTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Dialogue definition not found",
                operation="get_dialogue_definition",
                dialogue_id=dialogue_id,
            )
        return to_response(row)
    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: admin get errors unpredictable
        logger.error("Error retrieving dialogue definition", error=str(e))
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving dialogue definition",
        ) from e


@dialogue_router.put("/definitions/{dialogue_id}", response_model=DialogueDefinitionResponse)
async def upsert_dialogue_definition(
    dialogue_id: str,
    body: DialogueDefinitionUpdate,
    request: Request,
    current_user: User | None = Depends(get_current_user),
) -> DialogueDefinitionResponse:
    """Create or update a dialogue definition (path id wins)."""
    try:
        validate_admin_permission(current_user, AdminAction.UPSERT_DIALOGUE_DEFINITION, request)
        auth_service = get_admin_auth_service()
        logger.info(
            "Dialogue definition upsert requested",
            user=auth_service.get_username(current_user),
            dialogue_id=dialogue_id,
        )
        row = await DialogueDefinitionRepository().upsert(
            dialogue_id,
            body.definition.model_dump(),
            body.npc_definition_id,
        )
        return to_response(row)
    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: admin upsert errors unpredictable
        logger.error("Error upserting dialogue definition", error=str(e))
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error saving dialogue definition",
        ) from e


@dialogue_router.post("/definitions", response_model=DialogueDefinitionResponse, status_code=status.HTTP_201_CREATED)
async def create_dialogue_definition(
    body: DialogueDefinitionCreate,
    request: Request,
    current_user: User | None = Depends(get_current_user),
) -> DialogueDefinitionResponse:
    """Create a dialogue definition (upsert by id)."""
    try:
        validate_admin_permission(current_user, AdminAction.UPSERT_DIALOGUE_DEFINITION, request)
        auth_service = get_admin_auth_service()
        logger.info(
            "Dialogue definition create requested",
            user=auth_service.get_username(current_user),
            dialogue_id=body.id,
        )
        row = await DialogueDefinitionRepository().upsert(
            body.id,
            body.definition.model_dump(),
            body.npc_definition_id,
        )
        return to_response(row)
    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: admin create errors unpredictable
        logger.error("Error creating dialogue definition", error=str(e))
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error creating dialogue definition",
        ) from e


@dialogue_router.delete("/definitions/{dialogue_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_dialogue_definition(
    dialogue_id: str,
    request: Request,
    current_user: User | None = Depends(get_current_user),
) -> None:
    """Delete a dialogue definition."""
    try:
        validate_admin_permission(current_user, AdminAction.DELETE_DIALOGUE_DEFINITION, request)
        auth_service = get_admin_auth_service()
        logger.info(
            "Dialogue definition deletion requested",
            user=auth_service.get_username(current_user),
            dialogue_id=dialogue_id,
        )
        deleted = await DialogueDefinitionRepository().delete(dialogue_id)
        if not deleted:
            raise LoggedHTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Dialogue definition not found",
                operation="delete_dialogue_definition",
                dialogue_id=dialogue_id,
            )
    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: admin delete errors unpredictable
        logger.error("Error deleting dialogue definition", error=str(e))
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error deleting dialogue definition",
        ) from e
